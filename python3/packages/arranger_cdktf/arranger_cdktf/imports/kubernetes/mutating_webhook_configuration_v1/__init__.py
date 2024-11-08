'''
# `kubernetes_mutating_webhook_configuration_v1`

Refer to the Terraform Registory for docs: [`kubernetes_mutating_webhook_configuration_v1`](https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1).
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


class MutatingWebhookConfigurationV1(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.mutatingWebhookConfigurationV1.MutatingWebhookConfigurationV1",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1 kubernetes_mutating_webhook_configuration_v1}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        metadata: typing.Union["MutatingWebhookConfigurationV1Metadata", typing.Dict[builtins.str, typing.Any]],
        webhook: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["MutatingWebhookConfigurationV1Webhook", typing.Dict[builtins.str, typing.Any]]]],
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1 kubernetes_mutating_webhook_configuration_v1} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#metadata MutatingWebhookConfigurationV1#metadata}
        :param webhook: webhook block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#webhook MutatingWebhookConfigurationV1#webhook}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#id MutatingWebhookConfigurationV1#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__547276484cc0da69573d2578b682343d2560cbef1171881eae3b26f4f2e09b8d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = MutatingWebhookConfigurationV1Config(
            metadata=metadata,
            webhook=webhook,
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
        :param annotations: An unstructured key value map stored with the mutating webhook configuration that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#annotations MutatingWebhookConfigurationV1#annotations}
        :param generate_name: Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided. This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#generate_name MutatingWebhookConfigurationV1#generate_name}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the mutating webhook configuration. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#labels MutatingWebhookConfigurationV1#labels}
        :param name: Name of the mutating webhook configuration, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#name MutatingWebhookConfigurationV1#name}
        '''
        value = MutatingWebhookConfigurationV1Metadata(
            annotations=annotations,
            generate_name=generate_name,
            labels=labels,
            name=name,
        )

        return typing.cast(None, jsii.invoke(self, "putMetadata", [value]))

    @jsii.member(jsii_name="putWebhook")
    def put_webhook(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["MutatingWebhookConfigurationV1Webhook", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d23d15e3dc2b077d14d14fd1ff94383820c304a539071b1fbab1fc923b247a4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putWebhook", [value]))

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
    def metadata(self) -> "MutatingWebhookConfigurationV1MetadataOutputReference":
        return typing.cast("MutatingWebhookConfigurationV1MetadataOutputReference", jsii.get(self, "metadata"))

    @builtins.property
    @jsii.member(jsii_name="webhook")
    def webhook(self) -> "MutatingWebhookConfigurationV1WebhookList":
        return typing.cast("MutatingWebhookConfigurationV1WebhookList", jsii.get(self, "webhook"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(
        self,
    ) -> typing.Optional["MutatingWebhookConfigurationV1Metadata"]:
        return typing.cast(typing.Optional["MutatingWebhookConfigurationV1Metadata"], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="webhookInput")
    def webhook_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MutatingWebhookConfigurationV1Webhook"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MutatingWebhookConfigurationV1Webhook"]]], jsii.get(self, "webhookInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b2cb54b627edca0ec55932ebdeb819e6983dbbcf3c56750f10cfd28659863f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="kubernetes.mutatingWebhookConfigurationV1.MutatingWebhookConfigurationV1Config",
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
        "webhook": "webhook",
        "id": "id",
    },
)
class MutatingWebhookConfigurationV1Config(_cdktf_9a9027ec.TerraformMetaArguments):
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
        metadata: typing.Union["MutatingWebhookConfigurationV1Metadata", typing.Dict[builtins.str, typing.Any]],
        webhook: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["MutatingWebhookConfigurationV1Webhook", typing.Dict[builtins.str, typing.Any]]]],
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
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#metadata MutatingWebhookConfigurationV1#metadata}
        :param webhook: webhook block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#webhook MutatingWebhookConfigurationV1#webhook}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#id MutatingWebhookConfigurationV1#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(metadata, dict):
            metadata = MutatingWebhookConfigurationV1Metadata(**metadata)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__582a6c04646adefb36a6703524af4ebfe139fb0e3bab305e030c2cc2a9bddc5b)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument webhook", value=webhook, expected_type=type_hints["webhook"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "metadata": metadata,
            "webhook": webhook,
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
    def metadata(self) -> "MutatingWebhookConfigurationV1Metadata":
        '''metadata block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#metadata MutatingWebhookConfigurationV1#metadata}
        '''
        result = self._values.get("metadata")
        assert result is not None, "Required property 'metadata' is missing"
        return typing.cast("MutatingWebhookConfigurationV1Metadata", result)

    @builtins.property
    def webhook(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MutatingWebhookConfigurationV1Webhook"]]:
        '''webhook block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#webhook MutatingWebhookConfigurationV1#webhook}
        '''
        result = self._values.get("webhook")
        assert result is not None, "Required property 'webhook' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MutatingWebhookConfigurationV1Webhook"]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#id MutatingWebhookConfigurationV1#id}.

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
        return "MutatingWebhookConfigurationV1Config(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.mutatingWebhookConfigurationV1.MutatingWebhookConfigurationV1Metadata",
    jsii_struct_bases=[],
    name_mapping={
        "annotations": "annotations",
        "generate_name": "generateName",
        "labels": "labels",
        "name": "name",
    },
)
class MutatingWebhookConfigurationV1Metadata:
    def __init__(
        self,
        *,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        generate_name: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param annotations: An unstructured key value map stored with the mutating webhook configuration that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#annotations MutatingWebhookConfigurationV1#annotations}
        :param generate_name: Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided. This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#generate_name MutatingWebhookConfigurationV1#generate_name}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the mutating webhook configuration. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#labels MutatingWebhookConfigurationV1#labels}
        :param name: Name of the mutating webhook configuration, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#name MutatingWebhookConfigurationV1#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__adaa44c40e2b3b9d4582266f24132a2f494101d6fb2ca85660418079b6b448bd)
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
        '''An unstructured key value map stored with the mutating webhook configuration that may be used to store arbitrary metadata.

        More info: http://kubernetes.io/docs/user-guide/annotations

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#annotations MutatingWebhookConfigurationV1#annotations}
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def generate_name(self) -> typing.Optional[builtins.str]:
        '''Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided.

        This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#generate_name MutatingWebhookConfigurationV1#generate_name}
        '''
        result = self._values.get("generate_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Map of string keys and values that can be used to organize and categorize (scope and select) the mutating webhook configuration.

        May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#labels MutatingWebhookConfigurationV1#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the mutating webhook configuration, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#name MutatingWebhookConfigurationV1#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MutatingWebhookConfigurationV1Metadata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MutatingWebhookConfigurationV1MetadataOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.mutatingWebhookConfigurationV1.MutatingWebhookConfigurationV1MetadataOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__baa8c3b4e5dfbdcaa897bf96043f5aa343cf555c9fda630c7ed365b934ecc6ee)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d6e55dd00204774b60a18dea7782d22af2748690cae49634c953978f438e4ae4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "annotations", value)

    @builtins.property
    @jsii.member(jsii_name="generateName")
    def generate_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "generateName"))

    @generate_name.setter
    def generate_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51c59ecf0c39e05447b3216cdff6b16d8deea9802ed3bbe0c86cf556a972cab0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "generateName", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae5ef4f187a8c1b123bd15fe160c7dca12c7608739784371cdd4bb9ef5fb1481)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c8c78301ddcc52713abf83882f7da8cc53e0195f6ad1f7dbee848ad076e21a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MutatingWebhookConfigurationV1Metadata]:
        return typing.cast(typing.Optional[MutatingWebhookConfigurationV1Metadata], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MutatingWebhookConfigurationV1Metadata],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__384062841760b9a79c1bd663d35516c60ee3e2ecf4ade3f7f551ac718fe5cf10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.mutatingWebhookConfigurationV1.MutatingWebhookConfigurationV1Webhook",
    jsii_struct_bases=[],
    name_mapping={
        "client_config": "clientConfig",
        "name": "name",
        "admission_review_versions": "admissionReviewVersions",
        "failure_policy": "failurePolicy",
        "match_policy": "matchPolicy",
        "namespace_selector": "namespaceSelector",
        "object_selector": "objectSelector",
        "reinvocation_policy": "reinvocationPolicy",
        "rule": "rule",
        "side_effects": "sideEffects",
        "timeout_seconds": "timeoutSeconds",
    },
)
class MutatingWebhookConfigurationV1Webhook:
    def __init__(
        self,
        *,
        client_config: typing.Union["MutatingWebhookConfigurationV1WebhookClientConfig", typing.Dict[builtins.str, typing.Any]],
        name: builtins.str,
        admission_review_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
        failure_policy: typing.Optional[builtins.str] = None,
        match_policy: typing.Optional[builtins.str] = None,
        namespace_selector: typing.Optional[typing.Union["MutatingWebhookConfigurationV1WebhookNamespaceSelector", typing.Dict[builtins.str, typing.Any]]] = None,
        object_selector: typing.Optional[typing.Union["MutatingWebhookConfigurationV1WebhookObjectSelector", typing.Dict[builtins.str, typing.Any]]] = None,
        reinvocation_policy: typing.Optional[builtins.str] = None,
        rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["MutatingWebhookConfigurationV1WebhookRule", typing.Dict[builtins.str, typing.Any]]]]] = None,
        side_effects: typing.Optional[builtins.str] = None,
        timeout_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param client_config: client_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#client_config MutatingWebhookConfigurationV1#client_config}
        :param name: The name of the admission webhook. Name should be fully qualified, e.g., imagepolicy.kubernetes.io, where "imagepolicy" is the name of the webhook, and kubernetes.io is the name of the organization. Required. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#name MutatingWebhookConfigurationV1#name}
        :param admission_review_versions: AdmissionReviewVersions is an ordered list of preferred ``AdmissionReview`` versions the Webhook expects. API server will try to use first version in the list which it supports. If none of the versions specified in this list supported by API server, validation will fail for this object. If a persisted webhook configuration specifies allowed versions and does not include any versions known to the API Server, calls to the webhook will fail and be subject to the failure policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#admission_review_versions MutatingWebhookConfigurationV1#admission_review_versions}
        :param failure_policy: FailurePolicy defines how unrecognized errors from the admission endpoint are handled - allowed values are Ignore or Fail. Defaults to Fail. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#failure_policy MutatingWebhookConfigurationV1#failure_policy}
        :param match_policy: matchPolicy defines how the "rules" list is used to match incoming requests. Allowed values are "Exact" or "Equivalent". - Exact: match a request only if it exactly matches a specified rule. For example, if deployments can be modified via apps/v1, apps/v1beta1, and extensions/v1beta1, but "rules" only included ``apiGroups:["apps"], apiVersions:["v1"], resources: ["deployments"]``, a request to apps/v1beta1 or extensions/v1beta1 would not be sent to the webhook. - Equivalent: match a request if modifies a resource listed in rules, even via another API group or version. For example, if deployments can be modified via apps/v1, apps/v1beta1, and extensions/v1beta1, and "rules" only included ``apiGroups:["apps"], apiVersions:["v1"], resources: ["deployments"]``, a request to apps/v1beta1 or extensions/v1beta1 would be converted to apps/v1 and sent to the webhook. Defaults to "Equivalent" Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#match_policy MutatingWebhookConfigurationV1#match_policy}
        :param namespace_selector: namespace_selector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#namespace_selector MutatingWebhookConfigurationV1#namespace_selector}
        :param object_selector: object_selector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#object_selector MutatingWebhookConfigurationV1#object_selector}
        :param reinvocation_policy: reinvocationPolicy indicates whether this webhook should be called multiple times as part of a single admission evaluation. Allowed values are "Never" and "IfNeeded". Never: the webhook will not be called more than once in a single admission evaluation. IfNeeded: the webhook will be called at least one additional time as part of the admission evaluation if the object being admitted is modified by other admission plugins after the initial webhook call. Webhooks that specify this option *must* be idempotent, able to process objects they previously admitted. Note: * the number of additional invocations is not guaranteed to be exactly one. * if additional invocations result in further modifications to the object, webhooks are not guaranteed to be invoked again. * webhooks that use this option may be reordered to minimize the number of additional invocations. * to validate an object after all mutations are guaranteed complete, use a validating admission webhook instead. Defaults to "Never". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#reinvocation_policy MutatingWebhookConfigurationV1#reinvocation_policy}
        :param rule: rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#rule MutatingWebhookConfigurationV1#rule}
        :param side_effects: SideEffects states whether this webhook has side effects. Acceptable values are: None, NoneOnDryRun (webhooks created via v1beta1 may also specify Some or Unknown). Webhooks with side effects MUST implement a reconciliation system, since a request may be rejected by a future step in the admission chain and the side effects therefore need to be undone. Requests with the dryRun attribute will be auto-rejected if they match a webhook with sideEffects == Unknown or Some. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#side_effects MutatingWebhookConfigurationV1#side_effects}
        :param timeout_seconds: TimeoutSeconds specifies the timeout for this webhook. After the timeout passes, the webhook call will be ignored or the API call will fail based on the failure policy. The timeout value must be between 1 and 30 seconds. Default to 10 seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#timeout_seconds MutatingWebhookConfigurationV1#timeout_seconds}
        '''
        if isinstance(client_config, dict):
            client_config = MutatingWebhookConfigurationV1WebhookClientConfig(**client_config)
        if isinstance(namespace_selector, dict):
            namespace_selector = MutatingWebhookConfigurationV1WebhookNamespaceSelector(**namespace_selector)
        if isinstance(object_selector, dict):
            object_selector = MutatingWebhookConfigurationV1WebhookObjectSelector(**object_selector)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__edc31732d1fb19b50a98c5a92ea7df8801708997e237592a7b57fc3bb76c2924)
            check_type(argname="argument client_config", value=client_config, expected_type=type_hints["client_config"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument admission_review_versions", value=admission_review_versions, expected_type=type_hints["admission_review_versions"])
            check_type(argname="argument failure_policy", value=failure_policy, expected_type=type_hints["failure_policy"])
            check_type(argname="argument match_policy", value=match_policy, expected_type=type_hints["match_policy"])
            check_type(argname="argument namespace_selector", value=namespace_selector, expected_type=type_hints["namespace_selector"])
            check_type(argname="argument object_selector", value=object_selector, expected_type=type_hints["object_selector"])
            check_type(argname="argument reinvocation_policy", value=reinvocation_policy, expected_type=type_hints["reinvocation_policy"])
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument side_effects", value=side_effects, expected_type=type_hints["side_effects"])
            check_type(argname="argument timeout_seconds", value=timeout_seconds, expected_type=type_hints["timeout_seconds"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "client_config": client_config,
            "name": name,
        }
        if admission_review_versions is not None:
            self._values["admission_review_versions"] = admission_review_versions
        if failure_policy is not None:
            self._values["failure_policy"] = failure_policy
        if match_policy is not None:
            self._values["match_policy"] = match_policy
        if namespace_selector is not None:
            self._values["namespace_selector"] = namespace_selector
        if object_selector is not None:
            self._values["object_selector"] = object_selector
        if reinvocation_policy is not None:
            self._values["reinvocation_policy"] = reinvocation_policy
        if rule is not None:
            self._values["rule"] = rule
        if side_effects is not None:
            self._values["side_effects"] = side_effects
        if timeout_seconds is not None:
            self._values["timeout_seconds"] = timeout_seconds

    @builtins.property
    def client_config(self) -> "MutatingWebhookConfigurationV1WebhookClientConfig":
        '''client_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#client_config MutatingWebhookConfigurationV1#client_config}
        '''
        result = self._values.get("client_config")
        assert result is not None, "Required property 'client_config' is missing"
        return typing.cast("MutatingWebhookConfigurationV1WebhookClientConfig", result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the admission webhook.

        Name should be fully qualified, e.g., imagepolicy.kubernetes.io, where "imagepolicy" is the name of the webhook, and kubernetes.io is the name of the organization. Required.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#name MutatingWebhookConfigurationV1#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def admission_review_versions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''AdmissionReviewVersions is an ordered list of preferred ``AdmissionReview`` versions the Webhook expects.

        API server will try to use first version in the list which it supports. If none of the versions specified in this list supported by API server, validation will fail for this object. If a persisted webhook configuration specifies allowed versions and does not include any versions known to the API Server, calls to the webhook will fail and be subject to the failure policy.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#admission_review_versions MutatingWebhookConfigurationV1#admission_review_versions}
        '''
        result = self._values.get("admission_review_versions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def failure_policy(self) -> typing.Optional[builtins.str]:
        '''FailurePolicy defines how unrecognized errors from the admission endpoint are handled - allowed values are Ignore or Fail.

        Defaults to Fail.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#failure_policy MutatingWebhookConfigurationV1#failure_policy}
        '''
        result = self._values.get("failure_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_policy(self) -> typing.Optional[builtins.str]:
        '''matchPolicy defines how the "rules" list is used to match incoming requests. Allowed values are "Exact" or "Equivalent".

        - Exact: match a request only if it exactly matches a specified rule. For example, if deployments can be modified via apps/v1, apps/v1beta1, and extensions/v1beta1, but "rules" only included ``apiGroups:["apps"], apiVersions:["v1"], resources: ["deployments"]``, a request to apps/v1beta1 or extensions/v1beta1 would not be sent to the webhook.
        - Equivalent: match a request if modifies a resource listed in rules, even via another API group or version. For example, if deployments can be modified via apps/v1, apps/v1beta1, and extensions/v1beta1, and "rules" only included ``apiGroups:["apps"], apiVersions:["v1"], resources: ["deployments"]``, a request to apps/v1beta1 or extensions/v1beta1 would be converted to apps/v1 and sent to the webhook.

        Defaults to "Equivalent"

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#match_policy MutatingWebhookConfigurationV1#match_policy}
        '''
        result = self._values.get("match_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace_selector(
        self,
    ) -> typing.Optional["MutatingWebhookConfigurationV1WebhookNamespaceSelector"]:
        '''namespace_selector block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#namespace_selector MutatingWebhookConfigurationV1#namespace_selector}
        '''
        result = self._values.get("namespace_selector")
        return typing.cast(typing.Optional["MutatingWebhookConfigurationV1WebhookNamespaceSelector"], result)

    @builtins.property
    def object_selector(
        self,
    ) -> typing.Optional["MutatingWebhookConfigurationV1WebhookObjectSelector"]:
        '''object_selector block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#object_selector MutatingWebhookConfigurationV1#object_selector}
        '''
        result = self._values.get("object_selector")
        return typing.cast(typing.Optional["MutatingWebhookConfigurationV1WebhookObjectSelector"], result)

    @builtins.property
    def reinvocation_policy(self) -> typing.Optional[builtins.str]:
        '''reinvocationPolicy indicates whether this webhook should be called multiple times as part of a single admission evaluation.

        Allowed values are "Never" and "IfNeeded".

        Never: the webhook will not be called more than once in a single admission evaluation.

        IfNeeded: the webhook will be called at least one additional time as part of the admission evaluation if the object being admitted is modified by other admission plugins after the initial webhook call. Webhooks that specify this option *must* be idempotent, able to process objects they previously admitted. Note: * the number of additional invocations is not guaranteed to be exactly one. * if additional invocations result in further modifications to the object, webhooks are not guaranteed to be invoked again. * webhooks that use this option may be reordered to minimize the number of additional invocations. * to validate an object after all mutations are guaranteed complete, use a validating admission webhook instead.

        Defaults to "Never".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#reinvocation_policy MutatingWebhookConfigurationV1#reinvocation_policy}
        '''
        result = self._values.get("reinvocation_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rule(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MutatingWebhookConfigurationV1WebhookRule"]]]:
        '''rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#rule MutatingWebhookConfigurationV1#rule}
        '''
        result = self._values.get("rule")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MutatingWebhookConfigurationV1WebhookRule"]]], result)

    @builtins.property
    def side_effects(self) -> typing.Optional[builtins.str]:
        '''SideEffects states whether this webhook has side effects.

        Acceptable values are: None, NoneOnDryRun (webhooks created via v1beta1 may also specify Some or Unknown). Webhooks with side effects MUST implement a reconciliation system, since a request may be rejected by a future step in the admission chain and the side effects therefore need to be undone. Requests with the dryRun attribute will be auto-rejected if they match a webhook with sideEffects == Unknown or Some.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#side_effects MutatingWebhookConfigurationV1#side_effects}
        '''
        result = self._values.get("side_effects")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeout_seconds(self) -> typing.Optional[jsii.Number]:
        '''TimeoutSeconds specifies the timeout for this webhook.

        After the timeout passes, the webhook call will be ignored or the API call will fail based on the failure policy. The timeout value must be between 1 and 30 seconds. Default to 10 seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#timeout_seconds MutatingWebhookConfigurationV1#timeout_seconds}
        '''
        result = self._values.get("timeout_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MutatingWebhookConfigurationV1Webhook(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.mutatingWebhookConfigurationV1.MutatingWebhookConfigurationV1WebhookClientConfig",
    jsii_struct_bases=[],
    name_mapping={"ca_bundle": "caBundle", "service": "service", "url": "url"},
)
class MutatingWebhookConfigurationV1WebhookClientConfig:
    def __init__(
        self,
        *,
        ca_bundle: typing.Optional[builtins.str] = None,
        service: typing.Optional[typing.Union["MutatingWebhookConfigurationV1WebhookClientConfigService", typing.Dict[builtins.str, typing.Any]]] = None,
        url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param ca_bundle: ``caBundle`` is a PEM encoded CA bundle which will be used to validate the webhook's server certificate. If unspecified, system trust roots on the apiserver are used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#ca_bundle MutatingWebhookConfigurationV1#ca_bundle}
        :param service: service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#service MutatingWebhookConfigurationV1#service}
        :param url: ``url`` gives the location of the webhook, in standard URL form (``scheme://host:port/path``). Exactly one of ``url`` or ``service`` must be specified. The ``host`` should not refer to a service running in the cluster; use the ``service`` field instead. The host might be resolved via external DNS in some apiservers (e.g., ``kube-apiserver`` cannot resolve in-cluster DNS as that would be a layering violation). ``host`` may also be an IP address. Please note that using ``localhost`` or ``127.0.0.1`` as a ``host`` is risky unless you take great care to run this webhook on all hosts which run an apiserver which might need to make calls to this webhook. Such installs are likely to be non-portable, i.e., not easy to turn up in a new cluster. The scheme must be "https"; the URL must begin with "https://". A path is optional, and if present may be any string permissible in a URL. You may use the path to pass an arbitrary string to the webhook, for example, a cluster identifier. Attempting to use a user or basic auth e.g. "user:password@" is not allowed. Fragments ("#...") and query parameters ("?...") are not allowed, either. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#url MutatingWebhookConfigurationV1#url}
        '''
        if isinstance(service, dict):
            service = MutatingWebhookConfigurationV1WebhookClientConfigService(**service)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e18849ea1433e5063631a18c071792dacb0dfec93e0ca728adfe8d1d0def28a)
            check_type(argname="argument ca_bundle", value=ca_bundle, expected_type=type_hints["ca_bundle"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if ca_bundle is not None:
            self._values["ca_bundle"] = ca_bundle
        if service is not None:
            self._values["service"] = service
        if url is not None:
            self._values["url"] = url

    @builtins.property
    def ca_bundle(self) -> typing.Optional[builtins.str]:
        '''``caBundle`` is a PEM encoded CA bundle which will be used to validate the webhook's server certificate.

        If unspecified, system trust roots on the apiserver are used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#ca_bundle MutatingWebhookConfigurationV1#ca_bundle}
        '''
        result = self._values.get("ca_bundle")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service(
        self,
    ) -> typing.Optional["MutatingWebhookConfigurationV1WebhookClientConfigService"]:
        '''service block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#service MutatingWebhookConfigurationV1#service}
        '''
        result = self._values.get("service")
        return typing.cast(typing.Optional["MutatingWebhookConfigurationV1WebhookClientConfigService"], result)

    @builtins.property
    def url(self) -> typing.Optional[builtins.str]:
        '''``url`` gives the location of the webhook, in standard URL form (``scheme://host:port/path``).

        Exactly one of ``url`` or ``service`` must be specified.

        The ``host`` should not refer to a service running in the cluster; use the ``service`` field instead. The host might be resolved via external DNS in some apiservers (e.g., ``kube-apiserver`` cannot resolve in-cluster DNS as that would be a layering violation). ``host`` may also be an IP address.

        Please note that using ``localhost`` or ``127.0.0.1`` as a ``host`` is risky unless you take great care to run this webhook on all hosts which run an apiserver which might need to make calls to this webhook. Such installs are likely to be non-portable, i.e., not easy to turn up in a new cluster.

        The scheme must be "https"; the URL must begin with "https://".

        A path is optional, and if present may be any string permissible in a URL. You may use the path to pass an arbitrary string to the webhook, for example, a cluster identifier.

        Attempting to use a user or basic auth e.g. "user:password@" is not allowed. Fragments ("#...") and query parameters ("?...") are not allowed, either.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#url MutatingWebhookConfigurationV1#url}
        '''
        result = self._values.get("url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MutatingWebhookConfigurationV1WebhookClientConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MutatingWebhookConfigurationV1WebhookClientConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.mutatingWebhookConfigurationV1.MutatingWebhookConfigurationV1WebhookClientConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__473d49de4e963f693ccafe0724e1fdc79724a9bbd6d2e557a8a8b8198a5ffb94)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putService")
    def put_service(
        self,
        *,
        name: builtins.str,
        namespace: builtins.str,
        path: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param name: ``name`` is the name of the service. Required. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#name MutatingWebhookConfigurationV1#name}
        :param namespace: ``namespace`` is the namespace of the service. Required. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#namespace MutatingWebhookConfigurationV1#namespace}
        :param path: ``path`` is an optional URL path which will be sent in any request to this service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#path MutatingWebhookConfigurationV1#path}
        :param port: If specified, the port on the service that hosting webhook. Default to 443 for backward compatibility. ``port`` should be a valid port number (1-65535, inclusive). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#port MutatingWebhookConfigurationV1#port}
        '''
        value = MutatingWebhookConfigurationV1WebhookClientConfigService(
            name=name, namespace=namespace, path=path, port=port
        )

        return typing.cast(None, jsii.invoke(self, "putService", [value]))

    @jsii.member(jsii_name="resetCaBundle")
    def reset_ca_bundle(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCaBundle", []))

    @jsii.member(jsii_name="resetService")
    def reset_service(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetService", []))

    @jsii.member(jsii_name="resetUrl")
    def reset_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrl", []))

    @builtins.property
    @jsii.member(jsii_name="service")
    def service(
        self,
    ) -> "MutatingWebhookConfigurationV1WebhookClientConfigServiceOutputReference":
        return typing.cast("MutatingWebhookConfigurationV1WebhookClientConfigServiceOutputReference", jsii.get(self, "service"))

    @builtins.property
    @jsii.member(jsii_name="caBundleInput")
    def ca_bundle_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "caBundleInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceInput")
    def service_input(
        self,
    ) -> typing.Optional["MutatingWebhookConfigurationV1WebhookClientConfigService"]:
        return typing.cast(typing.Optional["MutatingWebhookConfigurationV1WebhookClientConfigService"], jsii.get(self, "serviceInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="caBundle")
    def ca_bundle(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "caBundle"))

    @ca_bundle.setter
    def ca_bundle(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af8e56845a2f27a43bf6f68ef16a1f8be3e7bb617a3c998416866e6f712ea6c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caBundle", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0aee4d614da235af863a5de6500b27689ceca7061158120913360aa54366e156)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MutatingWebhookConfigurationV1WebhookClientConfig]:
        return typing.cast(typing.Optional[MutatingWebhookConfigurationV1WebhookClientConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MutatingWebhookConfigurationV1WebhookClientConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06927bb3484c004cafcbb5da477b535d9fe0a916500ff8db54f2e9b408c3346b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.mutatingWebhookConfigurationV1.MutatingWebhookConfigurationV1WebhookClientConfigService",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "namespace": "namespace",
        "path": "path",
        "port": "port",
    },
)
class MutatingWebhookConfigurationV1WebhookClientConfigService:
    def __init__(
        self,
        *,
        name: builtins.str,
        namespace: builtins.str,
        path: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param name: ``name`` is the name of the service. Required. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#name MutatingWebhookConfigurationV1#name}
        :param namespace: ``namespace`` is the namespace of the service. Required. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#namespace MutatingWebhookConfigurationV1#namespace}
        :param path: ``path`` is an optional URL path which will be sent in any request to this service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#path MutatingWebhookConfigurationV1#path}
        :param port: If specified, the port on the service that hosting webhook. Default to 443 for backward compatibility. ``port`` should be a valid port number (1-65535, inclusive). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#port MutatingWebhookConfigurationV1#port}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61a7a1b92e6b62f9928020b9de9b5c4ef6ffe5b26938ffb163c87d048a8c6920)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "namespace": namespace,
        }
        if path is not None:
            self._values["path"] = path
        if port is not None:
            self._values["port"] = port

    @builtins.property
    def name(self) -> builtins.str:
        '''``name`` is the name of the service. Required.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#name MutatingWebhookConfigurationV1#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''``namespace`` is the namespace of the service. Required.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#namespace MutatingWebhookConfigurationV1#namespace}
        '''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''``path`` is an optional URL path which will be sent in any request to this service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#path MutatingWebhookConfigurationV1#path}
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''If specified, the port on the service that hosting webhook.

        Default to 443 for backward compatibility. ``port`` should be a valid port number (1-65535, inclusive).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#port MutatingWebhookConfigurationV1#port}
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MutatingWebhookConfigurationV1WebhookClientConfigService(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MutatingWebhookConfigurationV1WebhookClientConfigServiceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.mutatingWebhookConfigurationV1.MutatingWebhookConfigurationV1WebhookClientConfigServiceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8b8c7e54e7479f3d71f3834c992c0582daf6dd75604662b9595a52aac8e09982)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

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
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__e907915bc20ec075b03649b952e5abf3de7a58b9551b756919024e34e9493b9e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db2aeb4f9b17cf83a6d6cedee903a885ba83212f2bd9dae8d68ae057e1511d6a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2883c8c632f4dfcdad4fb15c59f83f86aa6d2b074511bc9673f082a20c63eba8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52937c0d34acd2476a8459c0833f5b019e49340fd1705db02c43d8ecc4103802)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MutatingWebhookConfigurationV1WebhookClientConfigService]:
        return typing.cast(typing.Optional[MutatingWebhookConfigurationV1WebhookClientConfigService], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MutatingWebhookConfigurationV1WebhookClientConfigService],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c9d88b6a9d21091c42a11c28afa6d39698d7000ade5664bb7894c8006c77b52)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MutatingWebhookConfigurationV1WebhookList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.mutatingWebhookConfigurationV1.MutatingWebhookConfigurationV1WebhookList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a17cf73e567c4975e0b74d0a65824106df14a9f8759acea892c8e0ee09c87946)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MutatingWebhookConfigurationV1WebhookOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__995692a7e1c830c04f8714eaaf9e17fd36e873278634254b319bc4865e16d451)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MutatingWebhookConfigurationV1WebhookOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f55c9dd9b7e8ec65648858e914da46b83baa60012542d66e23a2a7f72a1d57dd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1bc93340c1557d10cdfb355ec842bbbabb8ba86c7fc3f0094a86c732353c0f18)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fd262517bb4fb330de783f85a02c9b257e7583d3104bea723f39921adc78202a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MutatingWebhookConfigurationV1Webhook]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MutatingWebhookConfigurationV1Webhook]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MutatingWebhookConfigurationV1Webhook]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__142437511db6d9402ee76a2a132043c4c00e64953361a506d15b92e5fdf37a3e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.mutatingWebhookConfigurationV1.MutatingWebhookConfigurationV1WebhookNamespaceSelector",
    jsii_struct_bases=[],
    name_mapping={
        "match_expressions": "matchExpressions",
        "match_labels": "matchLabels",
    },
)
class MutatingWebhookConfigurationV1WebhookNamespaceSelector:
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["MutatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param match_expressions: match_expressions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#match_expressions MutatingWebhookConfigurationV1#match_expressions}
        :param match_labels: A map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of ``match_expressions``, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#match_labels MutatingWebhookConfigurationV1#match_labels}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01811384b8f5c106e1b8de35a09c0258ac44977fcded07442db9eb47017d03bc)
            check_type(argname="argument match_expressions", value=match_expressions, expected_type=type_hints["match_expressions"])
            check_type(argname="argument match_labels", value=match_labels, expected_type=type_hints["match_labels"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if match_expressions is not None:
            self._values["match_expressions"] = match_expressions
        if match_labels is not None:
            self._values["match_labels"] = match_labels

    @builtins.property
    def match_expressions(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MutatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressions"]]]:
        '''match_expressions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#match_expressions MutatingWebhookConfigurationV1#match_expressions}
        '''
        result = self._values.get("match_expressions")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MutatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressions"]]], result)

    @builtins.property
    def match_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of {key,value} pairs.

        A single {key,value} in the matchLabels map is equivalent to an element of ``match_expressions``, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#match_labels MutatingWebhookConfigurationV1#match_labels}
        '''
        result = self._values.get("match_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MutatingWebhookConfigurationV1WebhookNamespaceSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.mutatingWebhookConfigurationV1.MutatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressions",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class MutatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressions:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        operator: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: The label key that the selector applies to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#key MutatingWebhookConfigurationV1#key}
        :param operator: A key's relationship to a set of values. Valid operators ard ``In``, ``NotIn``, ``Exists`` and ``DoesNotExist``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#operator MutatingWebhookConfigurationV1#operator}
        :param values: An array of string values. If the operator is ``In`` or ``NotIn``, the values array must be non-empty. If the operator is ``Exists`` or ``DoesNotExist``, the values array must be empty. This array is replaced during a strategic merge patch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#values MutatingWebhookConfigurationV1#values}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88b0bf4fe32a0aefdc07b2084782988a492f5995a111dbacdb4ea9bf901efe0d)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if operator is not None:
            self._values["operator"] = operator
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''The label key that the selector applies to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#key MutatingWebhookConfigurationV1#key}
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''A key's relationship to a set of values. Valid operators ard ``In``, ``NotIn``, ``Exists`` and ``DoesNotExist``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#operator MutatingWebhookConfigurationV1#operator}
        '''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of string values.

        If the operator is ``In`` or ``NotIn``, the values array must be non-empty. If the operator is ``Exists`` or ``DoesNotExist``, the values array must be empty. This array is replaced during a strategic merge patch.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#values MutatingWebhookConfigurationV1#values}
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MutatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MutatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.mutatingWebhookConfigurationV1.MutatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7768d2e604621fb0d6ef3bb10b1db1245ac028d9bcd615dfa0ccfe01905abef6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MutatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__840813195ff493d8956c306b6b3c223bb4866e8af285bd181ab5cdb85e523508)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MutatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b3deeed790d930532529045f92bd2a14ac827d97eefd66099ff7bf8dc1da0c7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__35ea26afb925905832db54561fc16b5e4a1a1ac4ff25599fad2e256465f8dc2e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__72aeb327144128558a6de9c2b08e39788975f369d02a2ebf43a837a99e09e029)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MutatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MutatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MutatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af0d70ef35eeb46c38c848f9586b3e7dc9df538ab301e49df363a1b2caf785e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MutatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.mutatingWebhookConfigurationV1.MutatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c3f42339861c90387a1034c9b57b37bcd86fc23b079d998bee6f2d70c3ce18ab)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetOperator")
    def reset_operator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperator", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abc506edce0ce834dff405fafa7a717a98f8f5daad803877cbaf9ad0f486fb3d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60886bad1163d19e9b42ab813268ce94db835b800044141b63ba9dcd51cd0047)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0dfe36d3ed62f6677963640a64dd1fad5ebca1be65b797f7eca5551ac8a41e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MutatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MutatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MutatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd8c4fc7324ff9c89588a39a02bd7f68da360d2137eb8fe0d9d2944228d2a7c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MutatingWebhookConfigurationV1WebhookNamespaceSelectorOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.mutatingWebhookConfigurationV1.MutatingWebhookConfigurationV1WebhookNamespaceSelectorOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d1225c6ee0bb16bcb2757231ee21ca3d333b1fed4ef075f8cbf487c01864538b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMatchExpressions")
    def put_match_expressions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[MutatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d4e69ccbafafccbf8f11e8c7ef48f3eb37df7b94e770915b18486ec94406640)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMatchExpressions", [value]))

    @jsii.member(jsii_name="resetMatchExpressions")
    def reset_match_expressions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchExpressions", []))

    @jsii.member(jsii_name="resetMatchLabels")
    def reset_match_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchLabels", []))

    @builtins.property
    @jsii.member(jsii_name="matchExpressions")
    def match_expressions(
        self,
    ) -> MutatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressionsList:
        return typing.cast(MutatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressionsList, jsii.get(self, "matchExpressions"))

    @builtins.property
    @jsii.member(jsii_name="matchExpressionsInput")
    def match_expressions_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MutatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MutatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressions]]], jsii.get(self, "matchExpressionsInput"))

    @builtins.property
    @jsii.member(jsii_name="matchLabelsInput")
    def match_labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "matchLabelsInput"))

    @builtins.property
    @jsii.member(jsii_name="matchLabels")
    def match_labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "matchLabels"))

    @match_labels.setter
    def match_labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__116c917ffd2b00370a93eccea5c430cc3408b2eb0e3f5e02d348ac52aeb05a99)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchLabels", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MutatingWebhookConfigurationV1WebhookNamespaceSelector]:
        return typing.cast(typing.Optional[MutatingWebhookConfigurationV1WebhookNamespaceSelector], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MutatingWebhookConfigurationV1WebhookNamespaceSelector],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fb820f164118ef8fc06e2e39d78f9f49d2002b616358bd7d330a5cfaa31fe0d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.mutatingWebhookConfigurationV1.MutatingWebhookConfigurationV1WebhookObjectSelector",
    jsii_struct_bases=[],
    name_mapping={
        "match_expressions": "matchExpressions",
        "match_labels": "matchLabels",
    },
)
class MutatingWebhookConfigurationV1WebhookObjectSelector:
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["MutatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param match_expressions: match_expressions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#match_expressions MutatingWebhookConfigurationV1#match_expressions}
        :param match_labels: A map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of ``match_expressions``, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#match_labels MutatingWebhookConfigurationV1#match_labels}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15470c8b533d3187581bc359f01ac20da35b545806440c355e87fba1876f938f)
            check_type(argname="argument match_expressions", value=match_expressions, expected_type=type_hints["match_expressions"])
            check_type(argname="argument match_labels", value=match_labels, expected_type=type_hints["match_labels"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if match_expressions is not None:
            self._values["match_expressions"] = match_expressions
        if match_labels is not None:
            self._values["match_labels"] = match_labels

    @builtins.property
    def match_expressions(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MutatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressions"]]]:
        '''match_expressions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#match_expressions MutatingWebhookConfigurationV1#match_expressions}
        '''
        result = self._values.get("match_expressions")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MutatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressions"]]], result)

    @builtins.property
    def match_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of {key,value} pairs.

        A single {key,value} in the matchLabels map is equivalent to an element of ``match_expressions``, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#match_labels MutatingWebhookConfigurationV1#match_labels}
        '''
        result = self._values.get("match_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MutatingWebhookConfigurationV1WebhookObjectSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.mutatingWebhookConfigurationV1.MutatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressions",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class MutatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressions:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        operator: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: The label key that the selector applies to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#key MutatingWebhookConfigurationV1#key}
        :param operator: A key's relationship to a set of values. Valid operators ard ``In``, ``NotIn``, ``Exists`` and ``DoesNotExist``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#operator MutatingWebhookConfigurationV1#operator}
        :param values: An array of string values. If the operator is ``In`` or ``NotIn``, the values array must be non-empty. If the operator is ``Exists`` or ``DoesNotExist``, the values array must be empty. This array is replaced during a strategic merge patch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#values MutatingWebhookConfigurationV1#values}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c80aa022b0fa4315bb3b1436983a70a5fffdd6f24a1e26de15f794c4c74082a)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if operator is not None:
            self._values["operator"] = operator
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''The label key that the selector applies to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#key MutatingWebhookConfigurationV1#key}
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''A key's relationship to a set of values. Valid operators ard ``In``, ``NotIn``, ``Exists`` and ``DoesNotExist``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#operator MutatingWebhookConfigurationV1#operator}
        '''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of string values.

        If the operator is ``In`` or ``NotIn``, the values array must be non-empty. If the operator is ``Exists`` or ``DoesNotExist``, the values array must be empty. This array is replaced during a strategic merge patch.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#values MutatingWebhookConfigurationV1#values}
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MutatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MutatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.mutatingWebhookConfigurationV1.MutatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2d3fe5c33bb0e7cb87a19db3a4c8009ab7086e52f0cb9d2d0ed8eb20a7a4b546)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MutatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ef30534f9dbeb694f96f9501bfef19d012305a6293a6eda40a226832653bf49)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MutatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60a594e9d87d21230266589257c680597a863d4d006eb88d0f00dc9896563c48)
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
            type_hints = typing.get_type_hints(_typecheckingstub__576a9532d1c3f39936350f38a3b551326b2b757a526a7598e898ade89d0510a3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e7661efb48ffc9bc2633dabd7c172c4f9263aaa7d65ee3c644313fd02341b911)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MutatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MutatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MutatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c1387c8846cf96b69dbdc971e0223df4d28636d08928484f65d6feeea0c392d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MutatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.mutatingWebhookConfigurationV1.MutatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__81e2def8bdefe1f56dedf03a803b4fc153d3f215348434d6fd83890d54535786)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetOperator")
    def reset_operator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperator", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a40774aaa11a787c3cdc574f3bece950d0630f95ac695dec10cd95dbb2ffa78)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9b108d2d96165894e11af39e5a24dfddd3c649c9f7b921a5998565b8a5aca03)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b68da924b2f4142ba397345ac1ca7f20b37f42501c312e5cec019a0512eb068)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MutatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MutatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MutatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07dd63f4f1fcfd7243ffaaeb43d31b5289e64aab0284332fcc03c2ad937c4829)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MutatingWebhookConfigurationV1WebhookObjectSelectorOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.mutatingWebhookConfigurationV1.MutatingWebhookConfigurationV1WebhookObjectSelectorOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__caa40b97aec26e97c0344d936958ca39562b5a07b75aa7793e8da6e2d6eded6a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMatchExpressions")
    def put_match_expressions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[MutatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5db1ade32e0415b6c7cc1b19948dc52dc911b843ab2e9b5c99b04fdbef23ac02)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMatchExpressions", [value]))

    @jsii.member(jsii_name="resetMatchExpressions")
    def reset_match_expressions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchExpressions", []))

    @jsii.member(jsii_name="resetMatchLabels")
    def reset_match_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchLabels", []))

    @builtins.property
    @jsii.member(jsii_name="matchExpressions")
    def match_expressions(
        self,
    ) -> MutatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressionsList:
        return typing.cast(MutatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressionsList, jsii.get(self, "matchExpressions"))

    @builtins.property
    @jsii.member(jsii_name="matchExpressionsInput")
    def match_expressions_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MutatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MutatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressions]]], jsii.get(self, "matchExpressionsInput"))

    @builtins.property
    @jsii.member(jsii_name="matchLabelsInput")
    def match_labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "matchLabelsInput"))

    @builtins.property
    @jsii.member(jsii_name="matchLabels")
    def match_labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "matchLabels"))

    @match_labels.setter
    def match_labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c1ebef72bbb83c2b2c8f21884fa525fd7507a2f226aa6102d139aee9b038492)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchLabels", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MutatingWebhookConfigurationV1WebhookObjectSelector]:
        return typing.cast(typing.Optional[MutatingWebhookConfigurationV1WebhookObjectSelector], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MutatingWebhookConfigurationV1WebhookObjectSelector],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d901bed1b68e4666ba155d0cef661ab65fca52b5ceb7efcb835246b35c1d4936)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MutatingWebhookConfigurationV1WebhookOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.mutatingWebhookConfigurationV1.MutatingWebhookConfigurationV1WebhookOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__51654a0c5b7779a3099f3cd13564c15b0eb5ae589c07ed6877b58e6d46053ca2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putClientConfig")
    def put_client_config(
        self,
        *,
        ca_bundle: typing.Optional[builtins.str] = None,
        service: typing.Optional[typing.Union[MutatingWebhookConfigurationV1WebhookClientConfigService, typing.Dict[builtins.str, typing.Any]]] = None,
        url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param ca_bundle: ``caBundle`` is a PEM encoded CA bundle which will be used to validate the webhook's server certificate. If unspecified, system trust roots on the apiserver are used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#ca_bundle MutatingWebhookConfigurationV1#ca_bundle}
        :param service: service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#service MutatingWebhookConfigurationV1#service}
        :param url: ``url`` gives the location of the webhook, in standard URL form (``scheme://host:port/path``). Exactly one of ``url`` or ``service`` must be specified. The ``host`` should not refer to a service running in the cluster; use the ``service`` field instead. The host might be resolved via external DNS in some apiservers (e.g., ``kube-apiserver`` cannot resolve in-cluster DNS as that would be a layering violation). ``host`` may also be an IP address. Please note that using ``localhost`` or ``127.0.0.1`` as a ``host`` is risky unless you take great care to run this webhook on all hosts which run an apiserver which might need to make calls to this webhook. Such installs are likely to be non-portable, i.e., not easy to turn up in a new cluster. The scheme must be "https"; the URL must begin with "https://". A path is optional, and if present may be any string permissible in a URL. You may use the path to pass an arbitrary string to the webhook, for example, a cluster identifier. Attempting to use a user or basic auth e.g. "user:password@" is not allowed. Fragments ("#...") and query parameters ("?...") are not allowed, either. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#url MutatingWebhookConfigurationV1#url}
        '''
        value = MutatingWebhookConfigurationV1WebhookClientConfig(
            ca_bundle=ca_bundle, service=service, url=url
        )

        return typing.cast(None, jsii.invoke(self, "putClientConfig", [value]))

    @jsii.member(jsii_name="putNamespaceSelector")
    def put_namespace_selector(
        self,
        *,
        match_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[MutatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]]] = None,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param match_expressions: match_expressions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#match_expressions MutatingWebhookConfigurationV1#match_expressions}
        :param match_labels: A map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of ``match_expressions``, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#match_labels MutatingWebhookConfigurationV1#match_labels}
        '''
        value = MutatingWebhookConfigurationV1WebhookNamespaceSelector(
            match_expressions=match_expressions, match_labels=match_labels
        )

        return typing.cast(None, jsii.invoke(self, "putNamespaceSelector", [value]))

    @jsii.member(jsii_name="putObjectSelector")
    def put_object_selector(
        self,
        *,
        match_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[MutatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]]] = None,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param match_expressions: match_expressions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#match_expressions MutatingWebhookConfigurationV1#match_expressions}
        :param match_labels: A map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of ``match_expressions``, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#match_labels MutatingWebhookConfigurationV1#match_labels}
        '''
        value = MutatingWebhookConfigurationV1WebhookObjectSelector(
            match_expressions=match_expressions, match_labels=match_labels
        )

        return typing.cast(None, jsii.invoke(self, "putObjectSelector", [value]))

    @jsii.member(jsii_name="putRule")
    def put_rule(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["MutatingWebhookConfigurationV1WebhookRule", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b6cb810e3b8ab4413e70b58a1cb2910b685f79eb4dd1333dd12d32e8aaf7b39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRule", [value]))

    @jsii.member(jsii_name="resetAdmissionReviewVersions")
    def reset_admission_review_versions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdmissionReviewVersions", []))

    @jsii.member(jsii_name="resetFailurePolicy")
    def reset_failure_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailurePolicy", []))

    @jsii.member(jsii_name="resetMatchPolicy")
    def reset_match_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchPolicy", []))

    @jsii.member(jsii_name="resetNamespaceSelector")
    def reset_namespace_selector(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespaceSelector", []))

    @jsii.member(jsii_name="resetObjectSelector")
    def reset_object_selector(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetObjectSelector", []))

    @jsii.member(jsii_name="resetReinvocationPolicy")
    def reset_reinvocation_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReinvocationPolicy", []))

    @jsii.member(jsii_name="resetRule")
    def reset_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRule", []))

    @jsii.member(jsii_name="resetSideEffects")
    def reset_side_effects(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSideEffects", []))

    @jsii.member(jsii_name="resetTimeoutSeconds")
    def reset_timeout_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeoutSeconds", []))

    @builtins.property
    @jsii.member(jsii_name="clientConfig")
    def client_config(
        self,
    ) -> MutatingWebhookConfigurationV1WebhookClientConfigOutputReference:
        return typing.cast(MutatingWebhookConfigurationV1WebhookClientConfigOutputReference, jsii.get(self, "clientConfig"))

    @builtins.property
    @jsii.member(jsii_name="namespaceSelector")
    def namespace_selector(
        self,
    ) -> MutatingWebhookConfigurationV1WebhookNamespaceSelectorOutputReference:
        return typing.cast(MutatingWebhookConfigurationV1WebhookNamespaceSelectorOutputReference, jsii.get(self, "namespaceSelector"))

    @builtins.property
    @jsii.member(jsii_name="objectSelector")
    def object_selector(
        self,
    ) -> MutatingWebhookConfigurationV1WebhookObjectSelectorOutputReference:
        return typing.cast(MutatingWebhookConfigurationV1WebhookObjectSelectorOutputReference, jsii.get(self, "objectSelector"))

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> "MutatingWebhookConfigurationV1WebhookRuleList":
        return typing.cast("MutatingWebhookConfigurationV1WebhookRuleList", jsii.get(self, "rule"))

    @builtins.property
    @jsii.member(jsii_name="admissionReviewVersionsInput")
    def admission_review_versions_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "admissionReviewVersionsInput"))

    @builtins.property
    @jsii.member(jsii_name="clientConfigInput")
    def client_config_input(
        self,
    ) -> typing.Optional[MutatingWebhookConfigurationV1WebhookClientConfig]:
        return typing.cast(typing.Optional[MutatingWebhookConfigurationV1WebhookClientConfig], jsii.get(self, "clientConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="failurePolicyInput")
    def failure_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "failurePolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="matchPolicyInput")
    def match_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "matchPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceSelectorInput")
    def namespace_selector_input(
        self,
    ) -> typing.Optional[MutatingWebhookConfigurationV1WebhookNamespaceSelector]:
        return typing.cast(typing.Optional[MutatingWebhookConfigurationV1WebhookNamespaceSelector], jsii.get(self, "namespaceSelectorInput"))

    @builtins.property
    @jsii.member(jsii_name="objectSelectorInput")
    def object_selector_input(
        self,
    ) -> typing.Optional[MutatingWebhookConfigurationV1WebhookObjectSelector]:
        return typing.cast(typing.Optional[MutatingWebhookConfigurationV1WebhookObjectSelector], jsii.get(self, "objectSelectorInput"))

    @builtins.property
    @jsii.member(jsii_name="reinvocationPolicyInput")
    def reinvocation_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "reinvocationPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MutatingWebhookConfigurationV1WebhookRule"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MutatingWebhookConfigurationV1WebhookRule"]]], jsii.get(self, "ruleInput"))

    @builtins.property
    @jsii.member(jsii_name="sideEffectsInput")
    def side_effects_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sideEffectsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutSecondsInput")
    def timeout_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="admissionReviewVersions")
    def admission_review_versions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "admissionReviewVersions"))

    @admission_review_versions.setter
    def admission_review_versions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90d9064a1fb077bff126a38059e2b4b5ef8f9e70ac56d4d15423be18bb6bbc3b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "admissionReviewVersions", value)

    @builtins.property
    @jsii.member(jsii_name="failurePolicy")
    def failure_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "failurePolicy"))

    @failure_policy.setter
    def failure_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a28a5acd4890fa9cea5b7edae657a1e700d55748b3a78e9b5008e427a722fd88)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failurePolicy", value)

    @builtins.property
    @jsii.member(jsii_name="matchPolicy")
    def match_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "matchPolicy"))

    @match_policy.setter
    def match_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__236e540dd93a130e72e63a58e803e8e26928283df2493d2cba165b70abda8b7a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15232fbd3b75158d18a0d253e28f0392f3f2b082ef03a9b1756903cbd5c2ced7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="reinvocationPolicy")
    def reinvocation_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "reinvocationPolicy"))

    @reinvocation_policy.setter
    def reinvocation_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__935d0043fa00b9d21e751e7806eab6023ee1f9d8ec090f7dc4272e2f263b6752)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reinvocationPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="sideEffects")
    def side_effects(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sideEffects"))

    @side_effects.setter
    def side_effects(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32de90101d37d8e7aeac0652095d4be8886c8331cff229a629f0c12078ff2dc1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sideEffects", value)

    @builtins.property
    @jsii.member(jsii_name="timeoutSeconds")
    def timeout_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeoutSeconds"))

    @timeout_seconds.setter
    def timeout_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b623a12b01a72903be596edd77fcf0bba4e02725a40957cc7d866a985415618)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MutatingWebhookConfigurationV1Webhook, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MutatingWebhookConfigurationV1Webhook, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MutatingWebhookConfigurationV1Webhook, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa50c1f4fd1ad17eaae7fa8f068bc4a5d7194a63f6f22f27f30a9d15364acd61)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.mutatingWebhookConfigurationV1.MutatingWebhookConfigurationV1WebhookRule",
    jsii_struct_bases=[],
    name_mapping={
        "api_groups": "apiGroups",
        "api_versions": "apiVersions",
        "operations": "operations",
        "resources": "resources",
        "scope": "scope",
    },
)
class MutatingWebhookConfigurationV1WebhookRule:
    def __init__(
        self,
        *,
        api_groups: typing.Sequence[builtins.str],
        api_versions: typing.Sequence[builtins.str],
        operations: typing.Sequence[builtins.str],
        resources: typing.Sequence[builtins.str],
        scope: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param api_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#api_groups MutatingWebhookConfigurationV1#api_groups}.
        :param api_versions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#api_versions MutatingWebhookConfigurationV1#api_versions}.
        :param operations: Operations is the operations the admission hook cares about - CREATE, UPDATE, DELETE, CONNECT or * for all of those operations and any future admission operations that are added. If '*' is present, the length of the slice must be one. Required. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#operations MutatingWebhookConfigurationV1#operations}
        :param resources: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#resources MutatingWebhookConfigurationV1#resources}.
        :param scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#scope MutatingWebhookConfigurationV1#scope}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0646d449f00775436347091e3be983d324d0af15f30a18e11138801ad65fb945)
            check_type(argname="argument api_groups", value=api_groups, expected_type=type_hints["api_groups"])
            check_type(argname="argument api_versions", value=api_versions, expected_type=type_hints["api_versions"])
            check_type(argname="argument operations", value=operations, expected_type=type_hints["operations"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_groups": api_groups,
            "api_versions": api_versions,
            "operations": operations,
            "resources": resources,
        }
        if scope is not None:
            self._values["scope"] = scope

    @builtins.property
    def api_groups(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#api_groups MutatingWebhookConfigurationV1#api_groups}.'''
        result = self._values.get("api_groups")
        assert result is not None, "Required property 'api_groups' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def api_versions(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#api_versions MutatingWebhookConfigurationV1#api_versions}.'''
        result = self._values.get("api_versions")
        assert result is not None, "Required property 'api_versions' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def operations(self) -> typing.List[builtins.str]:
        '''Operations is the operations the admission hook cares about - CREATE, UPDATE, DELETE, CONNECT or * for all of those operations and any future admission operations that are added.

        If '*' is present, the length of the slice must be one. Required.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#operations MutatingWebhookConfigurationV1#operations}
        '''
        result = self._values.get("operations")
        assert result is not None, "Required property 'operations' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def resources(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#resources MutatingWebhookConfigurationV1#resources}.'''
        result = self._values.get("resources")
        assert result is not None, "Required property 'resources' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def scope(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/mutating_webhook_configuration_v1#scope MutatingWebhookConfigurationV1#scope}.'''
        result = self._values.get("scope")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MutatingWebhookConfigurationV1WebhookRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MutatingWebhookConfigurationV1WebhookRuleList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.mutatingWebhookConfigurationV1.MutatingWebhookConfigurationV1WebhookRuleList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__57ea6a5df3fb4510076ac2556bb9d523d062086db10bbb109d0413fd365b3787)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MutatingWebhookConfigurationV1WebhookRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b07b537f0f6766a391d8efeaffaad4907ccc7c543bd4bf4a6f300ebb36e8b97d)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MutatingWebhookConfigurationV1WebhookRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90813792e19a44c8462689a592712c8ccd909819481687835ed84d7c81c53e0a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b7a5ae1e2a5c38e271467e0af465b13a7277d76b139e906df95b467b7ccb2756)
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
            type_hints = typing.get_type_hints(_typecheckingstub__dcbbdc5ed9df47f6c8afa765feb00eada78f0d64897d2fbcb9a4c31775e6da44)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MutatingWebhookConfigurationV1WebhookRule]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MutatingWebhookConfigurationV1WebhookRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MutatingWebhookConfigurationV1WebhookRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac21d3214c66884470159e02e6975f73b1bed28ddf7ae4bfadd96e10f5ae4cc7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MutatingWebhookConfigurationV1WebhookRuleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.mutatingWebhookConfigurationV1.MutatingWebhookConfigurationV1WebhookRuleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__686a95ba7426a10303fbd468b0e324fb93f2b9d89ef030716d5b4c8f9926ff6d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetScope")
    def reset_scope(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScope", []))

    @builtins.property
    @jsii.member(jsii_name="apiGroupsInput")
    def api_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "apiGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="apiVersionsInput")
    def api_versions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "apiVersionsInput"))

    @builtins.property
    @jsii.member(jsii_name="operationsInput")
    def operations_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "operationsInput"))

    @builtins.property
    @jsii.member(jsii_name="resourcesInput")
    def resources_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="scopeInput")
    def scope_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scopeInput"))

    @builtins.property
    @jsii.member(jsii_name="apiGroups")
    def api_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "apiGroups"))

    @api_groups.setter
    def api_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e29d669b9b8f835f36902d6e5b1262c0f6e2ef9d39a142622fe2fc1574d0722)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiGroups", value)

    @builtins.property
    @jsii.member(jsii_name="apiVersions")
    def api_versions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "apiVersions"))

    @api_versions.setter
    def api_versions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e5056d470ae48ea5b67d03fdbbdb0b6fdce85bff6d02822165361cb6cb6f098)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiVersions", value)

    @builtins.property
    @jsii.member(jsii_name="operations")
    def operations(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "operations"))

    @operations.setter
    def operations(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e728953c5d3cf390aaea83473077dd58447449b0d4e9aa062d2b5a917873035d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operations", value)

    @builtins.property
    @jsii.member(jsii_name="resources")
    def resources(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "resources"))

    @resources.setter
    def resources(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5181cb82eb9aea0b749b84eb977c81830c7080576215b86b70e40660985ea290)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resources", value)

    @builtins.property
    @jsii.member(jsii_name="scope")
    def scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scope"))

    @scope.setter
    def scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__967ba9b7d087b2028790f184af7cf0a54fb06d155ef30699356c69a9af3d45c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scope", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MutatingWebhookConfigurationV1WebhookRule, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MutatingWebhookConfigurationV1WebhookRule, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MutatingWebhookConfigurationV1WebhookRule, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44dca72e2c6c0090a7290e9e172a71b83124f1147fa2e79d07b0c88d89b2f65c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "MutatingWebhookConfigurationV1",
    "MutatingWebhookConfigurationV1Config",
    "MutatingWebhookConfigurationV1Metadata",
    "MutatingWebhookConfigurationV1MetadataOutputReference",
    "MutatingWebhookConfigurationV1Webhook",
    "MutatingWebhookConfigurationV1WebhookClientConfig",
    "MutatingWebhookConfigurationV1WebhookClientConfigOutputReference",
    "MutatingWebhookConfigurationV1WebhookClientConfigService",
    "MutatingWebhookConfigurationV1WebhookClientConfigServiceOutputReference",
    "MutatingWebhookConfigurationV1WebhookList",
    "MutatingWebhookConfigurationV1WebhookNamespaceSelector",
    "MutatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressions",
    "MutatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressionsList",
    "MutatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressionsOutputReference",
    "MutatingWebhookConfigurationV1WebhookNamespaceSelectorOutputReference",
    "MutatingWebhookConfigurationV1WebhookObjectSelector",
    "MutatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressions",
    "MutatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressionsList",
    "MutatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressionsOutputReference",
    "MutatingWebhookConfigurationV1WebhookObjectSelectorOutputReference",
    "MutatingWebhookConfigurationV1WebhookOutputReference",
    "MutatingWebhookConfigurationV1WebhookRule",
    "MutatingWebhookConfigurationV1WebhookRuleList",
    "MutatingWebhookConfigurationV1WebhookRuleOutputReference",
]

publication.publish()

def _typecheckingstub__547276484cc0da69573d2578b682343d2560cbef1171881eae3b26f4f2e09b8d(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    metadata: typing.Union[MutatingWebhookConfigurationV1Metadata, typing.Dict[builtins.str, typing.Any]],
    webhook: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[MutatingWebhookConfigurationV1Webhook, typing.Dict[builtins.str, typing.Any]]]],
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

def _typecheckingstub__d23d15e3dc2b077d14d14fd1ff94383820c304a539071b1fbab1fc923b247a4e(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[MutatingWebhookConfigurationV1Webhook, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b2cb54b627edca0ec55932ebdeb819e6983dbbcf3c56750f10cfd28659863f4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__582a6c04646adefb36a6703524af4ebfe139fb0e3bab305e030c2cc2a9bddc5b(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    metadata: typing.Union[MutatingWebhookConfigurationV1Metadata, typing.Dict[builtins.str, typing.Any]],
    webhook: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[MutatingWebhookConfigurationV1Webhook, typing.Dict[builtins.str, typing.Any]]]],
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adaa44c40e2b3b9d4582266f24132a2f494101d6fb2ca85660418079b6b448bd(
    *,
    annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    generate_name: typing.Optional[builtins.str] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__baa8c3b4e5dfbdcaa897bf96043f5aa343cf555c9fda630c7ed365b934ecc6ee(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6e55dd00204774b60a18dea7782d22af2748690cae49634c953978f438e4ae4(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51c59ecf0c39e05447b3216cdff6b16d8deea9802ed3bbe0c86cf556a972cab0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae5ef4f187a8c1b123bd15fe160c7dca12c7608739784371cdd4bb9ef5fb1481(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c8c78301ddcc52713abf83882f7da8cc53e0195f6ad1f7dbee848ad076e21a7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__384062841760b9a79c1bd663d35516c60ee3e2ecf4ade3f7f551ac718fe5cf10(
    value: typing.Optional[MutatingWebhookConfigurationV1Metadata],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__edc31732d1fb19b50a98c5a92ea7df8801708997e237592a7b57fc3bb76c2924(
    *,
    client_config: typing.Union[MutatingWebhookConfigurationV1WebhookClientConfig, typing.Dict[builtins.str, typing.Any]],
    name: builtins.str,
    admission_review_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
    failure_policy: typing.Optional[builtins.str] = None,
    match_policy: typing.Optional[builtins.str] = None,
    namespace_selector: typing.Optional[typing.Union[MutatingWebhookConfigurationV1WebhookNamespaceSelector, typing.Dict[builtins.str, typing.Any]]] = None,
    object_selector: typing.Optional[typing.Union[MutatingWebhookConfigurationV1WebhookObjectSelector, typing.Dict[builtins.str, typing.Any]]] = None,
    reinvocation_policy: typing.Optional[builtins.str] = None,
    rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[MutatingWebhookConfigurationV1WebhookRule, typing.Dict[builtins.str, typing.Any]]]]] = None,
    side_effects: typing.Optional[builtins.str] = None,
    timeout_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e18849ea1433e5063631a18c071792dacb0dfec93e0ca728adfe8d1d0def28a(
    *,
    ca_bundle: typing.Optional[builtins.str] = None,
    service: typing.Optional[typing.Union[MutatingWebhookConfigurationV1WebhookClientConfigService, typing.Dict[builtins.str, typing.Any]]] = None,
    url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__473d49de4e963f693ccafe0724e1fdc79724a9bbd6d2e557a8a8b8198a5ffb94(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af8e56845a2f27a43bf6f68ef16a1f8be3e7bb617a3c998416866e6f712ea6c3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0aee4d614da235af863a5de6500b27689ceca7061158120913360aa54366e156(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06927bb3484c004cafcbb5da477b535d9fe0a916500ff8db54f2e9b408c3346b(
    value: typing.Optional[MutatingWebhookConfigurationV1WebhookClientConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61a7a1b92e6b62f9928020b9de9b5c4ef6ffe5b26938ffb163c87d048a8c6920(
    *,
    name: builtins.str,
    namespace: builtins.str,
    path: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b8c7e54e7479f3d71f3834c992c0582daf6dd75604662b9595a52aac8e09982(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e907915bc20ec075b03649b952e5abf3de7a58b9551b756919024e34e9493b9e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db2aeb4f9b17cf83a6d6cedee903a885ba83212f2bd9dae8d68ae057e1511d6a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2883c8c632f4dfcdad4fb15c59f83f86aa6d2b074511bc9673f082a20c63eba8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52937c0d34acd2476a8459c0833f5b019e49340fd1705db02c43d8ecc4103802(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c9d88b6a9d21091c42a11c28afa6d39698d7000ade5664bb7894c8006c77b52(
    value: typing.Optional[MutatingWebhookConfigurationV1WebhookClientConfigService],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a17cf73e567c4975e0b74d0a65824106df14a9f8759acea892c8e0ee09c87946(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__995692a7e1c830c04f8714eaaf9e17fd36e873278634254b319bc4865e16d451(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f55c9dd9b7e8ec65648858e914da46b83baa60012542d66e23a2a7f72a1d57dd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bc93340c1557d10cdfb355ec842bbbabb8ba86c7fc3f0094a86c732353c0f18(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd262517bb4fb330de783f85a02c9b257e7583d3104bea723f39921adc78202a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__142437511db6d9402ee76a2a132043c4c00e64953361a506d15b92e5fdf37a3e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MutatingWebhookConfigurationV1Webhook]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01811384b8f5c106e1b8de35a09c0258ac44977fcded07442db9eb47017d03bc(
    *,
    match_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[MutatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88b0bf4fe32a0aefdc07b2084782988a492f5995a111dbacdb4ea9bf901efe0d(
    *,
    key: typing.Optional[builtins.str] = None,
    operator: typing.Optional[builtins.str] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7768d2e604621fb0d6ef3bb10b1db1245ac028d9bcd615dfa0ccfe01905abef6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__840813195ff493d8956c306b6b3c223bb4866e8af285bd181ab5cdb85e523508(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b3deeed790d930532529045f92bd2a14ac827d97eefd66099ff7bf8dc1da0c7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35ea26afb925905832db54561fc16b5e4a1a1ac4ff25599fad2e256465f8dc2e(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72aeb327144128558a6de9c2b08e39788975f369d02a2ebf43a837a99e09e029(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af0d70ef35eeb46c38c848f9586b3e7dc9df538ab301e49df363a1b2caf785e6(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MutatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3f42339861c90387a1034c9b57b37bcd86fc23b079d998bee6f2d70c3ce18ab(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abc506edce0ce834dff405fafa7a717a98f8f5daad803877cbaf9ad0f486fb3d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60886bad1163d19e9b42ab813268ce94db835b800044141b63ba9dcd51cd0047(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0dfe36d3ed62f6677963640a64dd1fad5ebca1be65b797f7eca5551ac8a41e6(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd8c4fc7324ff9c89588a39a02bd7f68da360d2137eb8fe0d9d2944228d2a7c4(
    value: typing.Optional[typing.Union[MutatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1225c6ee0bb16bcb2757231ee21ca3d333b1fed4ef075f8cbf487c01864538b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d4e69ccbafafccbf8f11e8c7ef48f3eb37df7b94e770915b18486ec94406640(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[MutatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__116c917ffd2b00370a93eccea5c430cc3408b2eb0e3f5e02d348ac52aeb05a99(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fb820f164118ef8fc06e2e39d78f9f49d2002b616358bd7d330a5cfaa31fe0d(
    value: typing.Optional[MutatingWebhookConfigurationV1WebhookNamespaceSelector],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15470c8b533d3187581bc359f01ac20da35b545806440c355e87fba1876f938f(
    *,
    match_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[MutatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c80aa022b0fa4315bb3b1436983a70a5fffdd6f24a1e26de15f794c4c74082a(
    *,
    key: typing.Optional[builtins.str] = None,
    operator: typing.Optional[builtins.str] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d3fe5c33bb0e7cb87a19db3a4c8009ab7086e52f0cb9d2d0ed8eb20a7a4b546(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ef30534f9dbeb694f96f9501bfef19d012305a6293a6eda40a226832653bf49(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60a594e9d87d21230266589257c680597a863d4d006eb88d0f00dc9896563c48(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__576a9532d1c3f39936350f38a3b551326b2b757a526a7598e898ade89d0510a3(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7661efb48ffc9bc2633dabd7c172c4f9263aaa7d65ee3c644313fd02341b911(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c1387c8846cf96b69dbdc971e0223df4d28636d08928484f65d6feeea0c392d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MutatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81e2def8bdefe1f56dedf03a803b4fc153d3f215348434d6fd83890d54535786(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a40774aaa11a787c3cdc574f3bece950d0630f95ac695dec10cd95dbb2ffa78(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9b108d2d96165894e11af39e5a24dfddd3c649c9f7b921a5998565b8a5aca03(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b68da924b2f4142ba397345ac1ca7f20b37f42501c312e5cec019a0512eb068(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07dd63f4f1fcfd7243ffaaeb43d31b5289e64aab0284332fcc03c2ad937c4829(
    value: typing.Optional[typing.Union[MutatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__caa40b97aec26e97c0344d936958ca39562b5a07b75aa7793e8da6e2d6eded6a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5db1ade32e0415b6c7cc1b19948dc52dc911b843ab2e9b5c99b04fdbef23ac02(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[MutatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c1ebef72bbb83c2b2c8f21884fa525fd7507a2f226aa6102d139aee9b038492(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d901bed1b68e4666ba155d0cef661ab65fca52b5ceb7efcb835246b35c1d4936(
    value: typing.Optional[MutatingWebhookConfigurationV1WebhookObjectSelector],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51654a0c5b7779a3099f3cd13564c15b0eb5ae589c07ed6877b58e6d46053ca2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b6cb810e3b8ab4413e70b58a1cb2910b685f79eb4dd1333dd12d32e8aaf7b39(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[MutatingWebhookConfigurationV1WebhookRule, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90d9064a1fb077bff126a38059e2b4b5ef8f9e70ac56d4d15423be18bb6bbc3b(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a28a5acd4890fa9cea5b7edae657a1e700d55748b3a78e9b5008e427a722fd88(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__236e540dd93a130e72e63a58e803e8e26928283df2493d2cba165b70abda8b7a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15232fbd3b75158d18a0d253e28f0392f3f2b082ef03a9b1756903cbd5c2ced7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__935d0043fa00b9d21e751e7806eab6023ee1f9d8ec090f7dc4272e2f263b6752(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32de90101d37d8e7aeac0652095d4be8886c8331cff229a629f0c12078ff2dc1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b623a12b01a72903be596edd77fcf0bba4e02725a40957cc7d866a985415618(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa50c1f4fd1ad17eaae7fa8f068bc4a5d7194a63f6f22f27f30a9d15364acd61(
    value: typing.Optional[typing.Union[MutatingWebhookConfigurationV1Webhook, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0646d449f00775436347091e3be983d324d0af15f30a18e11138801ad65fb945(
    *,
    api_groups: typing.Sequence[builtins.str],
    api_versions: typing.Sequence[builtins.str],
    operations: typing.Sequence[builtins.str],
    resources: typing.Sequence[builtins.str],
    scope: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57ea6a5df3fb4510076ac2556bb9d523d062086db10bbb109d0413fd365b3787(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b07b537f0f6766a391d8efeaffaad4907ccc7c543bd4bf4a6f300ebb36e8b97d(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90813792e19a44c8462689a592712c8ccd909819481687835ed84d7c81c53e0a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7a5ae1e2a5c38e271467e0af465b13a7277d76b139e906df95b467b7ccb2756(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcbbdc5ed9df47f6c8afa765feb00eada78f0d64897d2fbcb9a4c31775e6da44(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac21d3214c66884470159e02e6975f73b1bed28ddf7ae4bfadd96e10f5ae4cc7(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MutatingWebhookConfigurationV1WebhookRule]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__686a95ba7426a10303fbd468b0e324fb93f2b9d89ef030716d5b4c8f9926ff6d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e29d669b9b8f835f36902d6e5b1262c0f6e2ef9d39a142622fe2fc1574d0722(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e5056d470ae48ea5b67d03fdbbdb0b6fdce85bff6d02822165361cb6cb6f098(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e728953c5d3cf390aaea83473077dd58447449b0d4e9aa062d2b5a917873035d(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5181cb82eb9aea0b749b84eb977c81830c7080576215b86b70e40660985ea290(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__967ba9b7d087b2028790f184af7cf0a54fb06d155ef30699356c69a9af3d45c3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44dca72e2c6c0090a7290e9e172a71b83124f1147fa2e79d07b0c88d89b2f65c(
    value: typing.Optional[typing.Union[MutatingWebhookConfigurationV1WebhookRule, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
