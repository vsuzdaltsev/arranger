'''
# `kubernetes_api_service_v1`

Refer to the Terraform Registory for docs: [`kubernetes_api_service_v1`](https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1).
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


class ApiServiceV1(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.apiServiceV1.ApiServiceV1",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1 kubernetes_api_service_v1}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        metadata: typing.Union["ApiServiceV1Metadata", typing.Dict[builtins.str, typing.Any]],
        spec: typing.Union["ApiServiceV1Spec", typing.Dict[builtins.str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1 kubernetes_api_service_v1} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#metadata ApiServiceV1#metadata}
        :param spec: spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#spec ApiServiceV1#spec}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#id ApiServiceV1#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd49c7588e9a5cb6a368dfbc9060741a3158dcaeb32fea930ad9731c7609d16b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ApiServiceV1Config(
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
        generate_name: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param annotations: An unstructured key value map stored with the api_service that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#annotations ApiServiceV1#annotations}
        :param generate_name: Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided. This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#generate_name ApiServiceV1#generate_name}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the api_service. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#labels ApiServiceV1#labels}
        :param name: Name of the api_service, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#name ApiServiceV1#name}
        '''
        value = ApiServiceV1Metadata(
            annotations=annotations,
            generate_name=generate_name,
            labels=labels,
            name=name,
        )

        return typing.cast(None, jsii.invoke(self, "putMetadata", [value]))

    @jsii.member(jsii_name="putSpec")
    def put_spec(
        self,
        *,
        group: builtins.str,
        group_priority_minimum: jsii.Number,
        version: builtins.str,
        version_priority: jsii.Number,
        ca_bundle: typing.Optional[builtins.str] = None,
        insecure_skip_tls_verify: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        service: typing.Optional[typing.Union["ApiServiceV1SpecService", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param group: Group is the API group name this server hosts. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#group ApiServiceV1#group}
        :param group_priority_minimum: GroupPriorityMinimum is the priority this group should have at least. Higher priority means that the group is preferred by clients over lower priority ones. Note that other versions of this group might specify even higher GroupPriorityMininum values such that the whole group gets a higher priority. The primary sort is based on GroupPriorityMinimum, ordered highest number to lowest (20 before 10). The secondary sort is based on the alphabetical comparison of the name of the object. (v1.bar before v1.foo) We'd recommend something like: *.k8s.io (except extensions) at 18000 and PaaSes (OpenShift, Deis) are recommended to be in the 2000s. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#group_priority_minimum ApiServiceV1#group_priority_minimum}
        :param version: Version is the API version this server hosts. For example, ``v1``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#version ApiServiceV1#version}
        :param version_priority: VersionPriority controls the ordering of this API version inside of its group. Must be greater than zero. The primary sort is based on VersionPriority, ordered highest to lowest (20 before 10). Since it's inside of a group, the number can be small, probably in the 10s. In case of equal version priorities, the version string will be used to compute the order inside a group. If the version string is ``kube-like``, it will sort above non ``kube-like`` version strings, which are ordered lexicographically. ``Kube-like`` versions start with a ``v``, then are followed by a number (the major version), then optionally the string ``alpha`` or ``beta`` and another number (the minor version). These are sorted first by GA > ``beta`` > ``alpha`` (where GA is a version with no suffix such as ``beta`` or ``alpha``), and then by comparing major version, then minor version. An example sorted list of versions: ``v10``, ``v2``, ``v1``, ``v11beta2``, ``v10beta3``, ``v3beta1``, ``v12alpha1``, ``v11alpha2``, ``foo1``, ``foo10``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#version_priority ApiServiceV1#version_priority}
        :param ca_bundle: CABundle is a PEM encoded CA bundle which will be used to validate an API server's serving certificate. If unspecified, system trust roots on the apiserver are used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#ca_bundle ApiServiceV1#ca_bundle}
        :param insecure_skip_tls_verify: InsecureSkipTLSVerify disables TLS certificate verification when communicating with this server. This is strongly discouraged. You should use the CABundle instead. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#insecure_skip_tls_verify ApiServiceV1#insecure_skip_tls_verify}
        :param service: service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#service ApiServiceV1#service}
        '''
        value = ApiServiceV1Spec(
            group=group,
            group_priority_minimum=group_priority_minimum,
            version=version,
            version_priority=version_priority,
            ca_bundle=ca_bundle,
            insecure_skip_tls_verify=insecure_skip_tls_verify,
            service=service,
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
    def metadata(self) -> "ApiServiceV1MetadataOutputReference":
        return typing.cast("ApiServiceV1MetadataOutputReference", jsii.get(self, "metadata"))

    @builtins.property
    @jsii.member(jsii_name="spec")
    def spec(self) -> "ApiServiceV1SpecOutputReference":
        return typing.cast("ApiServiceV1SpecOutputReference", jsii.get(self, "spec"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(self) -> typing.Optional["ApiServiceV1Metadata"]:
        return typing.cast(typing.Optional["ApiServiceV1Metadata"], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="specInput")
    def spec_input(self) -> typing.Optional["ApiServiceV1Spec"]:
        return typing.cast(typing.Optional["ApiServiceV1Spec"], jsii.get(self, "specInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34a4654e86023538c5c30ec5c59ee9091843f7b70f0233ddc48347eaf285ef95)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="kubernetes.apiServiceV1.ApiServiceV1Config",
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
class ApiServiceV1Config(_cdktf_9a9027ec.TerraformMetaArguments):
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
        metadata: typing.Union["ApiServiceV1Metadata", typing.Dict[builtins.str, typing.Any]],
        spec: typing.Union["ApiServiceV1Spec", typing.Dict[builtins.str, typing.Any]],
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
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#metadata ApiServiceV1#metadata}
        :param spec: spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#spec ApiServiceV1#spec}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#id ApiServiceV1#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(metadata, dict):
            metadata = ApiServiceV1Metadata(**metadata)
        if isinstance(spec, dict):
            spec = ApiServiceV1Spec(**spec)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b8ce6cfb281c3938dfd97a86ab9a862ec3d9a4c005d79f63f3f8e1190765e21)
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
    def metadata(self) -> "ApiServiceV1Metadata":
        '''metadata block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#metadata ApiServiceV1#metadata}
        '''
        result = self._values.get("metadata")
        assert result is not None, "Required property 'metadata' is missing"
        return typing.cast("ApiServiceV1Metadata", result)

    @builtins.property
    def spec(self) -> "ApiServiceV1Spec":
        '''spec block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#spec ApiServiceV1#spec}
        '''
        result = self._values.get("spec")
        assert result is not None, "Required property 'spec' is missing"
        return typing.cast("ApiServiceV1Spec", result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#id ApiServiceV1#id}.

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
        return "ApiServiceV1Config(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.apiServiceV1.ApiServiceV1Metadata",
    jsii_struct_bases=[],
    name_mapping={
        "annotations": "annotations",
        "generate_name": "generateName",
        "labels": "labels",
        "name": "name",
    },
)
class ApiServiceV1Metadata:
    def __init__(
        self,
        *,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        generate_name: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param annotations: An unstructured key value map stored with the api_service that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#annotations ApiServiceV1#annotations}
        :param generate_name: Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided. This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#generate_name ApiServiceV1#generate_name}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the api_service. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#labels ApiServiceV1#labels}
        :param name: Name of the api_service, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#name ApiServiceV1#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__353f08ac7cd0a58608567a95750605d1d32dc2d8c6c09dbb2452ae37246b00c6)
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument generate_name", value=generate_name, expected_type=type_hints["generate_name"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if annotations is not None:
            self._values["annotations"] = annotations
        if generate_name is not None:
            self._values["generate_name"] = generate_name
        if labels is not None:
            self._values["labels"] = labels
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def annotations(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''An unstructured key value map stored with the api_service that may be used to store arbitrary metadata.

        More info: http://kubernetes.io/docs/user-guide/annotations

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#annotations ApiServiceV1#annotations}
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def generate_name(self) -> typing.Optional[builtins.str]:
        '''Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided.

        This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#generate_name ApiServiceV1#generate_name}
        '''
        result = self._values.get("generate_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Map of string keys and values that can be used to organize and categorize (scope and select) the api_service.

        May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#labels ApiServiceV1#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the api_service, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#name ApiServiceV1#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiServiceV1Metadata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiServiceV1MetadataOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.apiServiceV1.ApiServiceV1MetadataOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b9811e30501fd6f1f102457709074d7d4dbf2eebe1c58ad3ddc6aa0d86252c21)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAnnotations")
    def reset_annotations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnnotations", []))

    @jsii.member(jsii_name="resetGenerateName")
    def reset_generate_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGenerateName", []))

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
    @jsii.member(jsii_name="generateNameInput")
    def generate_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "generateNameInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__a30e968fe9bf7788038d3acbe9e3385c6128010b6f103220a1b8d86b6b526e42)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "annotations", value)

    @builtins.property
    @jsii.member(jsii_name="generateName")
    def generate_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "generateName"))

    @generate_name.setter
    def generate_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78badda32f34dbb7df0d48269e72b8dfb721402109275746d8dc762730be0d89)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "generateName", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2702aff4c23db58945cbc09597cc9029a6d6b3f6e3c2ee5d12faf9b7ad3d3c11)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70f44a74663216099bad156383d8b24938ddb0c1ce7b8b12de31f556376191c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApiServiceV1Metadata]:
        return typing.cast(typing.Optional[ApiServiceV1Metadata], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ApiServiceV1Metadata]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72e0d614cd0fe45a8434869dda0942e52d5d1fd8b3491db1c0e64cba7b4ca812)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.apiServiceV1.ApiServiceV1Spec",
    jsii_struct_bases=[],
    name_mapping={
        "group": "group",
        "group_priority_minimum": "groupPriorityMinimum",
        "version": "version",
        "version_priority": "versionPriority",
        "ca_bundle": "caBundle",
        "insecure_skip_tls_verify": "insecureSkipTlsVerify",
        "service": "service",
    },
)
class ApiServiceV1Spec:
    def __init__(
        self,
        *,
        group: builtins.str,
        group_priority_minimum: jsii.Number,
        version: builtins.str,
        version_priority: jsii.Number,
        ca_bundle: typing.Optional[builtins.str] = None,
        insecure_skip_tls_verify: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        service: typing.Optional[typing.Union["ApiServiceV1SpecService", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param group: Group is the API group name this server hosts. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#group ApiServiceV1#group}
        :param group_priority_minimum: GroupPriorityMinimum is the priority this group should have at least. Higher priority means that the group is preferred by clients over lower priority ones. Note that other versions of this group might specify even higher GroupPriorityMininum values such that the whole group gets a higher priority. The primary sort is based on GroupPriorityMinimum, ordered highest number to lowest (20 before 10). The secondary sort is based on the alphabetical comparison of the name of the object. (v1.bar before v1.foo) We'd recommend something like: *.k8s.io (except extensions) at 18000 and PaaSes (OpenShift, Deis) are recommended to be in the 2000s. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#group_priority_minimum ApiServiceV1#group_priority_minimum}
        :param version: Version is the API version this server hosts. For example, ``v1``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#version ApiServiceV1#version}
        :param version_priority: VersionPriority controls the ordering of this API version inside of its group. Must be greater than zero. The primary sort is based on VersionPriority, ordered highest to lowest (20 before 10). Since it's inside of a group, the number can be small, probably in the 10s. In case of equal version priorities, the version string will be used to compute the order inside a group. If the version string is ``kube-like``, it will sort above non ``kube-like`` version strings, which are ordered lexicographically. ``Kube-like`` versions start with a ``v``, then are followed by a number (the major version), then optionally the string ``alpha`` or ``beta`` and another number (the minor version). These are sorted first by GA > ``beta`` > ``alpha`` (where GA is a version with no suffix such as ``beta`` or ``alpha``), and then by comparing major version, then minor version. An example sorted list of versions: ``v10``, ``v2``, ``v1``, ``v11beta2``, ``v10beta3``, ``v3beta1``, ``v12alpha1``, ``v11alpha2``, ``foo1``, ``foo10``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#version_priority ApiServiceV1#version_priority}
        :param ca_bundle: CABundle is a PEM encoded CA bundle which will be used to validate an API server's serving certificate. If unspecified, system trust roots on the apiserver are used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#ca_bundle ApiServiceV1#ca_bundle}
        :param insecure_skip_tls_verify: InsecureSkipTLSVerify disables TLS certificate verification when communicating with this server. This is strongly discouraged. You should use the CABundle instead. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#insecure_skip_tls_verify ApiServiceV1#insecure_skip_tls_verify}
        :param service: service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#service ApiServiceV1#service}
        '''
        if isinstance(service, dict):
            service = ApiServiceV1SpecService(**service)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a697f974baf8b3b07a33678ddefd0037c68644b3afe9d6abab56190b93152d6f)
            check_type(argname="argument group", value=group, expected_type=type_hints["group"])
            check_type(argname="argument group_priority_minimum", value=group_priority_minimum, expected_type=type_hints["group_priority_minimum"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument version_priority", value=version_priority, expected_type=type_hints["version_priority"])
            check_type(argname="argument ca_bundle", value=ca_bundle, expected_type=type_hints["ca_bundle"])
            check_type(argname="argument insecure_skip_tls_verify", value=insecure_skip_tls_verify, expected_type=type_hints["insecure_skip_tls_verify"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "group": group,
            "group_priority_minimum": group_priority_minimum,
            "version": version,
            "version_priority": version_priority,
        }
        if ca_bundle is not None:
            self._values["ca_bundle"] = ca_bundle
        if insecure_skip_tls_verify is not None:
            self._values["insecure_skip_tls_verify"] = insecure_skip_tls_verify
        if service is not None:
            self._values["service"] = service

    @builtins.property
    def group(self) -> builtins.str:
        '''Group is the API group name this server hosts.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#group ApiServiceV1#group}
        '''
        result = self._values.get("group")
        assert result is not None, "Required property 'group' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_priority_minimum(self) -> jsii.Number:
        '''GroupPriorityMinimum is the priority this group should have at least.

        Higher priority means that the group is preferred by clients over lower priority ones. Note that other versions of this group might specify even higher GroupPriorityMininum values such that the whole group gets a higher priority. The primary sort is based on GroupPriorityMinimum, ordered highest number to lowest (20 before 10). The secondary sort is based on the alphabetical comparison of the name of the object. (v1.bar before v1.foo) We'd recommend something like: *.k8s.io (except extensions) at 18000 and PaaSes (OpenShift, Deis) are recommended to be in the 2000s.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#group_priority_minimum ApiServiceV1#group_priority_minimum}
        '''
        result = self._values.get("group_priority_minimum")
        assert result is not None, "Required property 'group_priority_minimum' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def version(self) -> builtins.str:
        '''Version is the API version this server hosts. For example, ``v1``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#version ApiServiceV1#version}
        '''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version_priority(self) -> jsii.Number:
        '''VersionPriority controls the ordering of this API version inside of its group.

        Must be greater than zero. The primary sort is based on VersionPriority, ordered highest to lowest (20 before 10). Since it's inside of a group, the number can be small, probably in the 10s. In case of equal version priorities, the version string will be used to compute the order inside a group. If the version string is ``kube-like``, it will sort above non ``kube-like`` version strings, which are ordered lexicographically. ``Kube-like`` versions start with a ``v``, then are followed by a number (the major version), then optionally the string ``alpha`` or ``beta`` and another number (the minor version). These are sorted first by GA > ``beta`` > ``alpha`` (where GA is a version with no suffix such as ``beta`` or ``alpha``), and then by comparing major version, then minor version. An example sorted list of versions: ``v10``, ``v2``, ``v1``, ``v11beta2``, ``v10beta3``, ``v3beta1``, ``v12alpha1``, ``v11alpha2``, ``foo1``, ``foo10``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#version_priority ApiServiceV1#version_priority}
        '''
        result = self._values.get("version_priority")
        assert result is not None, "Required property 'version_priority' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def ca_bundle(self) -> typing.Optional[builtins.str]:
        '''CABundle is a PEM encoded CA bundle which will be used to validate an API server's serving certificate.

        If unspecified, system trust roots on the apiserver are used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#ca_bundle ApiServiceV1#ca_bundle}
        '''
        result = self._values.get("ca_bundle")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def insecure_skip_tls_verify(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''InsecureSkipTLSVerify disables TLS certificate verification when communicating with this server.

        This is strongly discouraged. You should use the CABundle instead.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#insecure_skip_tls_verify ApiServiceV1#insecure_skip_tls_verify}
        '''
        result = self._values.get("insecure_skip_tls_verify")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def service(self) -> typing.Optional["ApiServiceV1SpecService"]:
        '''service block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#service ApiServiceV1#service}
        '''
        result = self._values.get("service")
        return typing.cast(typing.Optional["ApiServiceV1SpecService"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiServiceV1Spec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiServiceV1SpecOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.apiServiceV1.ApiServiceV1SpecOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4234399a089505494a40e764f8e6e08072b3b7166d36b57e892486177d41a4a7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putService")
    def put_service(
        self,
        *,
        name: builtins.str,
        namespace: builtins.str,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param name: Name is the name of the service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#name ApiServiceV1#name}
        :param namespace: Namespace is the namespace of the service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#namespace ApiServiceV1#namespace}
        :param port: If specified, the port on the service that is hosting the service. Defaults to 443 for backward compatibility. Should be a valid port number (1-65535, inclusive). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#port ApiServiceV1#port}
        '''
        value = ApiServiceV1SpecService(name=name, namespace=namespace, port=port)

        return typing.cast(None, jsii.invoke(self, "putService", [value]))

    @jsii.member(jsii_name="resetCaBundle")
    def reset_ca_bundle(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCaBundle", []))

    @jsii.member(jsii_name="resetInsecureSkipTlsVerify")
    def reset_insecure_skip_tls_verify(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInsecureSkipTlsVerify", []))

    @jsii.member(jsii_name="resetService")
    def reset_service(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetService", []))

    @builtins.property
    @jsii.member(jsii_name="service")
    def service(self) -> "ApiServiceV1SpecServiceOutputReference":
        return typing.cast("ApiServiceV1SpecServiceOutputReference", jsii.get(self, "service"))

    @builtins.property
    @jsii.member(jsii_name="caBundleInput")
    def ca_bundle_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "caBundleInput"))

    @builtins.property
    @jsii.member(jsii_name="groupInput")
    def group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupInput"))

    @builtins.property
    @jsii.member(jsii_name="groupPriorityMinimumInput")
    def group_priority_minimum_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "groupPriorityMinimumInput"))

    @builtins.property
    @jsii.member(jsii_name="insecureSkipTlsVerifyInput")
    def insecure_skip_tls_verify_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "insecureSkipTlsVerifyInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceInput")
    def service_input(self) -> typing.Optional["ApiServiceV1SpecService"]:
        return typing.cast(typing.Optional["ApiServiceV1SpecService"], jsii.get(self, "serviceInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="versionPriorityInput")
    def version_priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "versionPriorityInput"))

    @builtins.property
    @jsii.member(jsii_name="caBundle")
    def ca_bundle(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "caBundle"))

    @ca_bundle.setter
    def ca_bundle(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98f4ba440cd0ed61fe1a62d81c6f94cd66c4f966d681fa037afae16afc1afbd3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caBundle", value)

    @builtins.property
    @jsii.member(jsii_name="group")
    def group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "group"))

    @group.setter
    def group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0e8477ec9ff8e00542702e56666d4d9289059874b1e7825db83b30b63f33163)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "group", value)

    @builtins.property
    @jsii.member(jsii_name="groupPriorityMinimum")
    def group_priority_minimum(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "groupPriorityMinimum"))

    @group_priority_minimum.setter
    def group_priority_minimum(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c8969fa095a385c6c030f0161d28545927bfff7b96489ba2ab27cc4f0c8084d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupPriorityMinimum", value)

    @builtins.property
    @jsii.member(jsii_name="insecureSkipTlsVerify")
    def insecure_skip_tls_verify(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "insecureSkipTlsVerify"))

    @insecure_skip_tls_verify.setter
    def insecure_skip_tls_verify(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__338811ba43612fafcddc273e079cba4fe6623963d81984011fc1e9713bf1d6fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insecureSkipTlsVerify", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__766347a6e4c7e78bca0335ed5bddf9e193314ea4bf25e0502e7b2cf98289294c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="versionPriority")
    def version_priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "versionPriority"))

    @version_priority.setter
    def version_priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14368f68407711bf0d173601b489bd9ee62731d0bd6aef08cf25520d18905ce4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "versionPriority", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApiServiceV1Spec]:
        return typing.cast(typing.Optional[ApiServiceV1Spec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ApiServiceV1Spec]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00b1986e970badc0262915bda5c5288c550144f29bfc4dbc59b22ee13fad4569)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.apiServiceV1.ApiServiceV1SpecService",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "namespace": "namespace", "port": "port"},
)
class ApiServiceV1SpecService:
    def __init__(
        self,
        *,
        name: builtins.str,
        namespace: builtins.str,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param name: Name is the name of the service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#name ApiServiceV1#name}
        :param namespace: Namespace is the namespace of the service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#namespace ApiServiceV1#namespace}
        :param port: If specified, the port on the service that is hosting the service. Defaults to 443 for backward compatibility. Should be a valid port number (1-65535, inclusive). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#port ApiServiceV1#port}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__acfbaf0d7d5188c517662590783cae54bf7c0755b78508cb519c50ba7525aa94)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "namespace": namespace,
        }
        if port is not None:
            self._values["port"] = port

    @builtins.property
    def name(self) -> builtins.str:
        '''Name is the name of the service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#name ApiServiceV1#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''Namespace is the namespace of the service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#namespace ApiServiceV1#namespace}
        '''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''If specified, the port on the service that is hosting the service.

        Defaults to 443 for backward compatibility. Should be a valid port number (1-65535, inclusive).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/api_service_v1#port ApiServiceV1#port}
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiServiceV1SpecService(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiServiceV1SpecServiceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.apiServiceV1.ApiServiceV1SpecServiceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b51cb4e8a563a41e07123b7d85cf7285ab4e6a4045c239e13e2ae733fc831484)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2431f9fe86629b1f12eb49e92f3f9a4646d6ee1205be6bfd9569d72bb586bf88)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eac33c07d3aface04e9ae67c57bb0ee60aacda248c8f692b49393c21a01833e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__723eb24c629cb6a8fcdc9294a2dc17ce43631c17eb9e533dc7b288406fb04c58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApiServiceV1SpecService]:
        return typing.cast(typing.Optional[ApiServiceV1SpecService], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ApiServiceV1SpecService]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df4336e4cbe2a9b5e6f16568dc19370d66c89b4f8d28cd4905a66ad12b440edc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ApiServiceV1",
    "ApiServiceV1Config",
    "ApiServiceV1Metadata",
    "ApiServiceV1MetadataOutputReference",
    "ApiServiceV1Spec",
    "ApiServiceV1SpecOutputReference",
    "ApiServiceV1SpecService",
    "ApiServiceV1SpecServiceOutputReference",
]

publication.publish()

def _typecheckingstub__fd49c7588e9a5cb6a368dfbc9060741a3158dcaeb32fea930ad9731c7609d16b(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    metadata: typing.Union[ApiServiceV1Metadata, typing.Dict[builtins.str, typing.Any]],
    spec: typing.Union[ApiServiceV1Spec, typing.Dict[builtins.str, typing.Any]],
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

def _typecheckingstub__34a4654e86023538c5c30ec5c59ee9091843f7b70f0233ddc48347eaf285ef95(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b8ce6cfb281c3938dfd97a86ab9a862ec3d9a4c005d79f63f3f8e1190765e21(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    metadata: typing.Union[ApiServiceV1Metadata, typing.Dict[builtins.str, typing.Any]],
    spec: typing.Union[ApiServiceV1Spec, typing.Dict[builtins.str, typing.Any]],
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__353f08ac7cd0a58608567a95750605d1d32dc2d8c6c09dbb2452ae37246b00c6(
    *,
    annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    generate_name: typing.Optional[builtins.str] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9811e30501fd6f1f102457709074d7d4dbf2eebe1c58ad3ddc6aa0d86252c21(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a30e968fe9bf7788038d3acbe9e3385c6128010b6f103220a1b8d86b6b526e42(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78badda32f34dbb7df0d48269e72b8dfb721402109275746d8dc762730be0d89(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2702aff4c23db58945cbc09597cc9029a6d6b3f6e3c2ee5d12faf9b7ad3d3c11(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70f44a74663216099bad156383d8b24938ddb0c1ce7b8b12de31f556376191c9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72e0d614cd0fe45a8434869dda0942e52d5d1fd8b3491db1c0e64cba7b4ca812(
    value: typing.Optional[ApiServiceV1Metadata],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a697f974baf8b3b07a33678ddefd0037c68644b3afe9d6abab56190b93152d6f(
    *,
    group: builtins.str,
    group_priority_minimum: jsii.Number,
    version: builtins.str,
    version_priority: jsii.Number,
    ca_bundle: typing.Optional[builtins.str] = None,
    insecure_skip_tls_verify: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    service: typing.Optional[typing.Union[ApiServiceV1SpecService, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4234399a089505494a40e764f8e6e08072b3b7166d36b57e892486177d41a4a7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98f4ba440cd0ed61fe1a62d81c6f94cd66c4f966d681fa037afae16afc1afbd3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0e8477ec9ff8e00542702e56666d4d9289059874b1e7825db83b30b63f33163(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c8969fa095a385c6c030f0161d28545927bfff7b96489ba2ab27cc4f0c8084d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__338811ba43612fafcddc273e079cba4fe6623963d81984011fc1e9713bf1d6fe(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__766347a6e4c7e78bca0335ed5bddf9e193314ea4bf25e0502e7b2cf98289294c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14368f68407711bf0d173601b489bd9ee62731d0bd6aef08cf25520d18905ce4(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00b1986e970badc0262915bda5c5288c550144f29bfc4dbc59b22ee13fad4569(
    value: typing.Optional[ApiServiceV1Spec],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acfbaf0d7d5188c517662590783cae54bf7c0755b78508cb519c50ba7525aa94(
    *,
    name: builtins.str,
    namespace: builtins.str,
    port: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b51cb4e8a563a41e07123b7d85cf7285ab4e6a4045c239e13e2ae733fc831484(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2431f9fe86629b1f12eb49e92f3f9a4646d6ee1205be6bfd9569d72bb586bf88(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eac33c07d3aface04e9ae67c57bb0ee60aacda248c8f692b49393c21a01833e6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__723eb24c629cb6a8fcdc9294a2dc17ce43631c17eb9e533dc7b288406fb04c58(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df4336e4cbe2a9b5e6f16568dc19370d66c89b4f8d28cd4905a66ad12b440edc(
    value: typing.Optional[ApiServiceV1SpecService],
) -> None:
    """Type checking stubs"""
    pass
