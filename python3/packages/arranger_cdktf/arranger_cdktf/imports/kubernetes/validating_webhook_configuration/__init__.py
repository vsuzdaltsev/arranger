'''
# `kubernetes_validating_webhook_configuration`

Refer to the Terraform Registory for docs: [`kubernetes_validating_webhook_configuration`](https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration).
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


class ValidatingWebhookConfiguration(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.validatingWebhookConfiguration.ValidatingWebhookConfiguration",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration kubernetes_validating_webhook_configuration}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        metadata: typing.Union["ValidatingWebhookConfigurationMetadata", typing.Dict[builtins.str, typing.Any]],
        webhook: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ValidatingWebhookConfigurationWebhook", typing.Dict[builtins.str, typing.Any]]]],
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration kubernetes_validating_webhook_configuration} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#metadata ValidatingWebhookConfiguration#metadata}
        :param webhook: webhook block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#webhook ValidatingWebhookConfiguration#webhook}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#id ValidatingWebhookConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1be00009fe1623b2547fe440035670ec35a74233bbec2b4e3b29f17c41aa1482)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ValidatingWebhookConfigurationConfig(
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
        :param annotations: An unstructured key value map stored with the validating webhook configuration that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#annotations ValidatingWebhookConfiguration#annotations}
        :param generate_name: Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided. This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#generate_name ValidatingWebhookConfiguration#generate_name}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the validating webhook configuration. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#labels ValidatingWebhookConfiguration#labels}
        :param name: Name of the validating webhook configuration, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#name ValidatingWebhookConfiguration#name}
        '''
        value = ValidatingWebhookConfigurationMetadata(
            annotations=annotations,
            generate_name=generate_name,
            labels=labels,
            name=name,
        )

        return typing.cast(None, jsii.invoke(self, "putMetadata", [value]))

    @jsii.member(jsii_name="putWebhook")
    def put_webhook(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ValidatingWebhookConfigurationWebhook", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b79ee33705090b1ec2e83215aa8b5b618c9521cadbea6c4a01d10cf2857a07b)
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
    def metadata(self) -> "ValidatingWebhookConfigurationMetadataOutputReference":
        return typing.cast("ValidatingWebhookConfigurationMetadataOutputReference", jsii.get(self, "metadata"))

    @builtins.property
    @jsii.member(jsii_name="webhook")
    def webhook(self) -> "ValidatingWebhookConfigurationWebhookList":
        return typing.cast("ValidatingWebhookConfigurationWebhookList", jsii.get(self, "webhook"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(
        self,
    ) -> typing.Optional["ValidatingWebhookConfigurationMetadata"]:
        return typing.cast(typing.Optional["ValidatingWebhookConfigurationMetadata"], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="webhookInput")
    def webhook_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ValidatingWebhookConfigurationWebhook"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ValidatingWebhookConfigurationWebhook"]]], jsii.get(self, "webhookInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61bbaebe3a9d96e5f8888a20fcd482d19ac01f5547e328b998a66828b250f907)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="kubernetes.validatingWebhookConfiguration.ValidatingWebhookConfigurationConfig",
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
class ValidatingWebhookConfigurationConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        metadata: typing.Union["ValidatingWebhookConfigurationMetadata", typing.Dict[builtins.str, typing.Any]],
        webhook: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ValidatingWebhookConfigurationWebhook", typing.Dict[builtins.str, typing.Any]]]],
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
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#metadata ValidatingWebhookConfiguration#metadata}
        :param webhook: webhook block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#webhook ValidatingWebhookConfiguration#webhook}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#id ValidatingWebhookConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(metadata, dict):
            metadata = ValidatingWebhookConfigurationMetadata(**metadata)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__797b05ce740994871805f95e0af875c6521f469507703342520cee75427ee0de)
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
    def metadata(self) -> "ValidatingWebhookConfigurationMetadata":
        '''metadata block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#metadata ValidatingWebhookConfiguration#metadata}
        '''
        result = self._values.get("metadata")
        assert result is not None, "Required property 'metadata' is missing"
        return typing.cast("ValidatingWebhookConfigurationMetadata", result)

    @builtins.property
    def webhook(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ValidatingWebhookConfigurationWebhook"]]:
        '''webhook block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#webhook ValidatingWebhookConfiguration#webhook}
        '''
        result = self._values.get("webhook")
        assert result is not None, "Required property 'webhook' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ValidatingWebhookConfigurationWebhook"]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#id ValidatingWebhookConfiguration#id}.

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
        return "ValidatingWebhookConfigurationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.validatingWebhookConfiguration.ValidatingWebhookConfigurationMetadata",
    jsii_struct_bases=[],
    name_mapping={
        "annotations": "annotations",
        "generate_name": "generateName",
        "labels": "labels",
        "name": "name",
    },
)
class ValidatingWebhookConfigurationMetadata:
    def __init__(
        self,
        *,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        generate_name: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param annotations: An unstructured key value map stored with the validating webhook configuration that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#annotations ValidatingWebhookConfiguration#annotations}
        :param generate_name: Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided. This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#generate_name ValidatingWebhookConfiguration#generate_name}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the validating webhook configuration. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#labels ValidatingWebhookConfiguration#labels}
        :param name: Name of the validating webhook configuration, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#name ValidatingWebhookConfiguration#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e72260881c0ff219034c1cafd9de2b336333f09734fbb3c3ba42c60d88403854)
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
        '''An unstructured key value map stored with the validating webhook configuration that may be used to store arbitrary metadata.

        More info: http://kubernetes.io/docs/user-guide/annotations

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#annotations ValidatingWebhookConfiguration#annotations}
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def generate_name(self) -> typing.Optional[builtins.str]:
        '''Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided.

        This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#generate_name ValidatingWebhookConfiguration#generate_name}
        '''
        result = self._values.get("generate_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Map of string keys and values that can be used to organize and categorize (scope and select) the validating webhook configuration.

        May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#labels ValidatingWebhookConfiguration#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the validating webhook configuration, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#name ValidatingWebhookConfiguration#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ValidatingWebhookConfigurationMetadata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ValidatingWebhookConfigurationMetadataOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.validatingWebhookConfiguration.ValidatingWebhookConfigurationMetadataOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__08f8c00b7c2be73cba07523a483aa6248aa0da8827b340882d2988ca43d5c5e3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6511c660fa1b20f87cc81cb26e03cf4f1ef3da899f6bc189e109fb2a57777d11)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "annotations", value)

    @builtins.property
    @jsii.member(jsii_name="generateName")
    def generate_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "generateName"))

    @generate_name.setter
    def generate_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74bdf4309cb32eb23957a0276b2ef41c4ae8df825ea918c19153d4b9d9d9120d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "generateName", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccc1d25077996ce5457b53cce6714dfe02e1e3b7c28c847b15fed27709d88d8b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2050abc5529493e589f63fac79553a37a3f05b40b4a0b895b636d74ae22f2b20)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ValidatingWebhookConfigurationMetadata]:
        return typing.cast(typing.Optional[ValidatingWebhookConfigurationMetadata], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ValidatingWebhookConfigurationMetadata],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce7a4ffb9beca1a8bb8cad9fb8a476a6a2e23efce68dc09f7e5691b12e115272)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.validatingWebhookConfiguration.ValidatingWebhookConfigurationWebhook",
    jsii_struct_bases=[],
    name_mapping={
        "client_config": "clientConfig",
        "name": "name",
        "admission_review_versions": "admissionReviewVersions",
        "failure_policy": "failurePolicy",
        "match_policy": "matchPolicy",
        "namespace_selector": "namespaceSelector",
        "object_selector": "objectSelector",
        "rule": "rule",
        "side_effects": "sideEffects",
        "timeout_seconds": "timeoutSeconds",
    },
)
class ValidatingWebhookConfigurationWebhook:
    def __init__(
        self,
        *,
        client_config: typing.Union["ValidatingWebhookConfigurationWebhookClientConfig", typing.Dict[builtins.str, typing.Any]],
        name: builtins.str,
        admission_review_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
        failure_policy: typing.Optional[builtins.str] = None,
        match_policy: typing.Optional[builtins.str] = None,
        namespace_selector: typing.Optional[typing.Union["ValidatingWebhookConfigurationWebhookNamespaceSelector", typing.Dict[builtins.str, typing.Any]]] = None,
        object_selector: typing.Optional[typing.Union["ValidatingWebhookConfigurationWebhookObjectSelector", typing.Dict[builtins.str, typing.Any]]] = None,
        rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ValidatingWebhookConfigurationWebhookRule", typing.Dict[builtins.str, typing.Any]]]]] = None,
        side_effects: typing.Optional[builtins.str] = None,
        timeout_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param client_config: client_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#client_config ValidatingWebhookConfiguration#client_config}
        :param name: The name of the admission webhook. Name should be fully qualified, e.g., imagepolicy.kubernetes.io, where "imagepolicy" is the name of the webhook, and kubernetes.io is the name of the organization. Required. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#name ValidatingWebhookConfiguration#name}
        :param admission_review_versions: AdmissionReviewVersions is an ordered list of preferred ``AdmissionReview`` versions the Webhook expects. API server will try to use first version in the list which it supports. If none of the versions specified in this list supported by API server, validation will fail for this object. If a persisted webhook configuration specifies allowed versions and does not include any versions known to the API Server, calls to the webhook will fail and be subject to the failure policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#admission_review_versions ValidatingWebhookConfiguration#admission_review_versions}
        :param failure_policy: FailurePolicy defines how unrecognized errors from the admission endpoint are handled - allowed values are Ignore or Fail. Defaults to Fail. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#failure_policy ValidatingWebhookConfiguration#failure_policy}
        :param match_policy: matchPolicy defines how the "rules" list is used to match incoming requests. Allowed values are "Exact" or "Equivalent". - Exact: match a request only if it exactly matches a specified rule. For example, if deployments can be modified via apps/v1, apps/v1beta1, and extensions/v1beta1, but "rules" only included ``apiGroups:["apps"], apiVersions:["v1"], resources: ["deployments"]``, a request to apps/v1beta1 or extensions/v1beta1 would not be sent to the webhook. - Equivalent: match a request if modifies a resource listed in rules, even via another API group or version. For example, if deployments can be modified via apps/v1, apps/v1beta1, and extensions/v1beta1, and "rules" only included ``apiGroups:["apps"], apiVersions:["v1"], resources: ["deployments"]``, a request to apps/v1beta1 or extensions/v1beta1 would be converted to apps/v1 and sent to the webhook. Defaults to "Equivalent" Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#match_policy ValidatingWebhookConfiguration#match_policy}
        :param namespace_selector: namespace_selector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#namespace_selector ValidatingWebhookConfiguration#namespace_selector}
        :param object_selector: object_selector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#object_selector ValidatingWebhookConfiguration#object_selector}
        :param rule: rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#rule ValidatingWebhookConfiguration#rule}
        :param side_effects: SideEffects states whether this webhook has side effects. Acceptable values are: None, NoneOnDryRun (webhooks created via v1beta1 may also specify Some or Unknown). Webhooks with side effects MUST implement a reconciliation system, since a request may be rejected by a future step in the admission chain and the side effects therefore need to be undone. Requests with the dryRun attribute will be auto-rejected if they match a webhook with sideEffects == Unknown or Some. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#side_effects ValidatingWebhookConfiguration#side_effects}
        :param timeout_seconds: TimeoutSeconds specifies the timeout for this webhook. After the timeout passes, the webhook call will be ignored or the API call will fail based on the failure policy. The timeout value must be between 1 and 30 seconds. Default to 10 seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#timeout_seconds ValidatingWebhookConfiguration#timeout_seconds}
        '''
        if isinstance(client_config, dict):
            client_config = ValidatingWebhookConfigurationWebhookClientConfig(**client_config)
        if isinstance(namespace_selector, dict):
            namespace_selector = ValidatingWebhookConfigurationWebhookNamespaceSelector(**namespace_selector)
        if isinstance(object_selector, dict):
            object_selector = ValidatingWebhookConfigurationWebhookObjectSelector(**object_selector)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1a81b69e7defb7ccff5922ec20ec9a42457667c9d790c36d694c97d097ff116)
            check_type(argname="argument client_config", value=client_config, expected_type=type_hints["client_config"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument admission_review_versions", value=admission_review_versions, expected_type=type_hints["admission_review_versions"])
            check_type(argname="argument failure_policy", value=failure_policy, expected_type=type_hints["failure_policy"])
            check_type(argname="argument match_policy", value=match_policy, expected_type=type_hints["match_policy"])
            check_type(argname="argument namespace_selector", value=namespace_selector, expected_type=type_hints["namespace_selector"])
            check_type(argname="argument object_selector", value=object_selector, expected_type=type_hints["object_selector"])
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
        if rule is not None:
            self._values["rule"] = rule
        if side_effects is not None:
            self._values["side_effects"] = side_effects
        if timeout_seconds is not None:
            self._values["timeout_seconds"] = timeout_seconds

    @builtins.property
    def client_config(self) -> "ValidatingWebhookConfigurationWebhookClientConfig":
        '''client_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#client_config ValidatingWebhookConfiguration#client_config}
        '''
        result = self._values.get("client_config")
        assert result is not None, "Required property 'client_config' is missing"
        return typing.cast("ValidatingWebhookConfigurationWebhookClientConfig", result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the admission webhook.

        Name should be fully qualified, e.g., imagepolicy.kubernetes.io, where "imagepolicy" is the name of the webhook, and kubernetes.io is the name of the organization. Required.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#name ValidatingWebhookConfiguration#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def admission_review_versions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''AdmissionReviewVersions is an ordered list of preferred ``AdmissionReview`` versions the Webhook expects.

        API server will try to use first version in the list which it supports. If none of the versions specified in this list supported by API server, validation will fail for this object. If a persisted webhook configuration specifies allowed versions and does not include any versions known to the API Server, calls to the webhook will fail and be subject to the failure policy.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#admission_review_versions ValidatingWebhookConfiguration#admission_review_versions}
        '''
        result = self._values.get("admission_review_versions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def failure_policy(self) -> typing.Optional[builtins.str]:
        '''FailurePolicy defines how unrecognized errors from the admission endpoint are handled - allowed values are Ignore or Fail.

        Defaults to Fail.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#failure_policy ValidatingWebhookConfiguration#failure_policy}
        '''
        result = self._values.get("failure_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_policy(self) -> typing.Optional[builtins.str]:
        '''matchPolicy defines how the "rules" list is used to match incoming requests. Allowed values are "Exact" or "Equivalent".

        - Exact: match a request only if it exactly matches a specified rule. For example, if deployments can be modified via apps/v1, apps/v1beta1, and extensions/v1beta1, but "rules" only included ``apiGroups:["apps"], apiVersions:["v1"], resources: ["deployments"]``, a request to apps/v1beta1 or extensions/v1beta1 would not be sent to the webhook.
        - Equivalent: match a request if modifies a resource listed in rules, even via another API group or version. For example, if deployments can be modified via apps/v1, apps/v1beta1, and extensions/v1beta1, and "rules" only included ``apiGroups:["apps"], apiVersions:["v1"], resources: ["deployments"]``, a request to apps/v1beta1 or extensions/v1beta1 would be converted to apps/v1 and sent to the webhook.

        Defaults to "Equivalent"

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#match_policy ValidatingWebhookConfiguration#match_policy}
        '''
        result = self._values.get("match_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace_selector(
        self,
    ) -> typing.Optional["ValidatingWebhookConfigurationWebhookNamespaceSelector"]:
        '''namespace_selector block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#namespace_selector ValidatingWebhookConfiguration#namespace_selector}
        '''
        result = self._values.get("namespace_selector")
        return typing.cast(typing.Optional["ValidatingWebhookConfigurationWebhookNamespaceSelector"], result)

    @builtins.property
    def object_selector(
        self,
    ) -> typing.Optional["ValidatingWebhookConfigurationWebhookObjectSelector"]:
        '''object_selector block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#object_selector ValidatingWebhookConfiguration#object_selector}
        '''
        result = self._values.get("object_selector")
        return typing.cast(typing.Optional["ValidatingWebhookConfigurationWebhookObjectSelector"], result)

    @builtins.property
    def rule(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ValidatingWebhookConfigurationWebhookRule"]]]:
        '''rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#rule ValidatingWebhookConfiguration#rule}
        '''
        result = self._values.get("rule")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ValidatingWebhookConfigurationWebhookRule"]]], result)

    @builtins.property
    def side_effects(self) -> typing.Optional[builtins.str]:
        '''SideEffects states whether this webhook has side effects.

        Acceptable values are: None, NoneOnDryRun (webhooks created via v1beta1 may also specify Some or Unknown). Webhooks with side effects MUST implement a reconciliation system, since a request may be rejected by a future step in the admission chain and the side effects therefore need to be undone. Requests with the dryRun attribute will be auto-rejected if they match a webhook with sideEffects == Unknown or Some.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#side_effects ValidatingWebhookConfiguration#side_effects}
        '''
        result = self._values.get("side_effects")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeout_seconds(self) -> typing.Optional[jsii.Number]:
        '''TimeoutSeconds specifies the timeout for this webhook.

        After the timeout passes, the webhook call will be ignored or the API call will fail based on the failure policy. The timeout value must be between 1 and 30 seconds. Default to 10 seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#timeout_seconds ValidatingWebhookConfiguration#timeout_seconds}
        '''
        result = self._values.get("timeout_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ValidatingWebhookConfigurationWebhook(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.validatingWebhookConfiguration.ValidatingWebhookConfigurationWebhookClientConfig",
    jsii_struct_bases=[],
    name_mapping={"ca_bundle": "caBundle", "service": "service", "url": "url"},
)
class ValidatingWebhookConfigurationWebhookClientConfig:
    def __init__(
        self,
        *,
        ca_bundle: typing.Optional[builtins.str] = None,
        service: typing.Optional[typing.Union["ValidatingWebhookConfigurationWebhookClientConfigService", typing.Dict[builtins.str, typing.Any]]] = None,
        url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param ca_bundle: ``caBundle`` is a PEM encoded CA bundle which will be used to validate the webhook's server certificate. If unspecified, system trust roots on the apiserver are used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#ca_bundle ValidatingWebhookConfiguration#ca_bundle}
        :param service: service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#service ValidatingWebhookConfiguration#service}
        :param url: ``url`` gives the location of the webhook, in standard URL form (``scheme://host:port/path``). Exactly one of ``url`` or ``service`` must be specified. The ``host`` should not refer to a service running in the cluster; use the ``service`` field instead. The host might be resolved via external DNS in some apiservers (e.g., ``kube-apiserver`` cannot resolve in-cluster DNS as that would be a layering violation). ``host`` may also be an IP address. Please note that using ``localhost`` or ``127.0.0.1`` as a ``host`` is risky unless you take great care to run this webhook on all hosts which run an apiserver which might need to make calls to this webhook. Such installs are likely to be non-portable, i.e., not easy to turn up in a new cluster. The scheme must be "https"; the URL must begin with "https://". A path is optional, and if present may be any string permissible in a URL. You may use the path to pass an arbitrary string to the webhook, for example, a cluster identifier. Attempting to use a user or basic auth e.g. "user:password@" is not allowed. Fragments ("#...") and query parameters ("?...") are not allowed, either. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#url ValidatingWebhookConfiguration#url}
        '''
        if isinstance(service, dict):
            service = ValidatingWebhookConfigurationWebhookClientConfigService(**service)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__286f0e06b6ca1ad159fc6811c06d9627b18e7bc8024932d2b1ccb0f4e05afcd2)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#ca_bundle ValidatingWebhookConfiguration#ca_bundle}
        '''
        result = self._values.get("ca_bundle")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service(
        self,
    ) -> typing.Optional["ValidatingWebhookConfigurationWebhookClientConfigService"]:
        '''service block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#service ValidatingWebhookConfiguration#service}
        '''
        result = self._values.get("service")
        return typing.cast(typing.Optional["ValidatingWebhookConfigurationWebhookClientConfigService"], result)

    @builtins.property
    def url(self) -> typing.Optional[builtins.str]:
        '''``url`` gives the location of the webhook, in standard URL form (``scheme://host:port/path``).

        Exactly one of ``url`` or ``service`` must be specified.

        The ``host`` should not refer to a service running in the cluster; use the ``service`` field instead. The host might be resolved via external DNS in some apiservers (e.g., ``kube-apiserver`` cannot resolve in-cluster DNS as that would be a layering violation). ``host`` may also be an IP address.

        Please note that using ``localhost`` or ``127.0.0.1`` as a ``host`` is risky unless you take great care to run this webhook on all hosts which run an apiserver which might need to make calls to this webhook. Such installs are likely to be non-portable, i.e., not easy to turn up in a new cluster.

        The scheme must be "https"; the URL must begin with "https://".

        A path is optional, and if present may be any string permissible in a URL. You may use the path to pass an arbitrary string to the webhook, for example, a cluster identifier.

        Attempting to use a user or basic auth e.g. "user:password@" is not allowed. Fragments ("#...") and query parameters ("?...") are not allowed, either.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#url ValidatingWebhookConfiguration#url}
        '''
        result = self._values.get("url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ValidatingWebhookConfigurationWebhookClientConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ValidatingWebhookConfigurationWebhookClientConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.validatingWebhookConfiguration.ValidatingWebhookConfigurationWebhookClientConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5707471e1f4044340754bc8486dc2bbc0d0178b0614e047b594dfba09ec7cc1a)
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
        :param name: ``name`` is the name of the service. Required. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#name ValidatingWebhookConfiguration#name}
        :param namespace: ``namespace`` is the namespace of the service. Required. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#namespace ValidatingWebhookConfiguration#namespace}
        :param path: ``path`` is an optional URL path which will be sent in any request to this service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#path ValidatingWebhookConfiguration#path}
        :param port: If specified, the port on the service that hosting webhook. Default to 443 for backward compatibility. ``port`` should be a valid port number (1-65535, inclusive). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#port ValidatingWebhookConfiguration#port}
        '''
        value = ValidatingWebhookConfigurationWebhookClientConfigService(
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
    ) -> "ValidatingWebhookConfigurationWebhookClientConfigServiceOutputReference":
        return typing.cast("ValidatingWebhookConfigurationWebhookClientConfigServiceOutputReference", jsii.get(self, "service"))

    @builtins.property
    @jsii.member(jsii_name="caBundleInput")
    def ca_bundle_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "caBundleInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceInput")
    def service_input(
        self,
    ) -> typing.Optional["ValidatingWebhookConfigurationWebhookClientConfigService"]:
        return typing.cast(typing.Optional["ValidatingWebhookConfigurationWebhookClientConfigService"], jsii.get(self, "serviceInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__b629823356e9d971a8252f2d5cb2dbef0d9328411706e6ee7d080f86954c8ca1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caBundle", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__441ba746745333ca0e0f399fcba4bf0c9a2605762d5dc9e5840817fe0cbd676a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ValidatingWebhookConfigurationWebhookClientConfig]:
        return typing.cast(typing.Optional[ValidatingWebhookConfigurationWebhookClientConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ValidatingWebhookConfigurationWebhookClientConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e93d6a3e9ef51b9557ed3583274823da36124bb991b533f1d4632aaa0bcae50)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.validatingWebhookConfiguration.ValidatingWebhookConfigurationWebhookClientConfigService",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "namespace": "namespace",
        "path": "path",
        "port": "port",
    },
)
class ValidatingWebhookConfigurationWebhookClientConfigService:
    def __init__(
        self,
        *,
        name: builtins.str,
        namespace: builtins.str,
        path: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param name: ``name`` is the name of the service. Required. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#name ValidatingWebhookConfiguration#name}
        :param namespace: ``namespace`` is the namespace of the service. Required. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#namespace ValidatingWebhookConfiguration#namespace}
        :param path: ``path`` is an optional URL path which will be sent in any request to this service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#path ValidatingWebhookConfiguration#path}
        :param port: If specified, the port on the service that hosting webhook. Default to 443 for backward compatibility. ``port`` should be a valid port number (1-65535, inclusive). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#port ValidatingWebhookConfiguration#port}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d4928d2a88f11133864981ef96f2589b74b72f21d90087092978d766de1e11a)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#name ValidatingWebhookConfiguration#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''``namespace`` is the namespace of the service. Required.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#namespace ValidatingWebhookConfiguration#namespace}
        '''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''``path`` is an optional URL path which will be sent in any request to this service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#path ValidatingWebhookConfiguration#path}
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''If specified, the port on the service that hosting webhook.

        Default to 443 for backward compatibility. ``port`` should be a valid port number (1-65535, inclusive).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#port ValidatingWebhookConfiguration#port}
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ValidatingWebhookConfigurationWebhookClientConfigService(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ValidatingWebhookConfigurationWebhookClientConfigServiceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.validatingWebhookConfiguration.ValidatingWebhookConfigurationWebhookClientConfigServiceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__752f4687b61b1b17029e9fe1fa3df9f5f04a87626ad66a4629b5b42aa0388f2a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4dee8a1539285f79f830315833ec6694e5494f7544621f71257841df23cf71d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__053d68bff3714edb94a67bb498c4d0a4359951e98d3b4fa37e0da6730f54df28)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__431621ef57cef5dd1a4d62b6da70e1ae4c3fcc2b78270104f536172015f7d013)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1610840e1adc47d59bcff8df3c369713af4454aa56f923da0352039b539f82dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ValidatingWebhookConfigurationWebhookClientConfigService]:
        return typing.cast(typing.Optional[ValidatingWebhookConfigurationWebhookClientConfigService], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ValidatingWebhookConfigurationWebhookClientConfigService],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2dd0b63bbc6c74aa207e18a3c11636e3cec8b974b77d88b5c82ecabc02753fc1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ValidatingWebhookConfigurationWebhookList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.validatingWebhookConfiguration.ValidatingWebhookConfigurationWebhookList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c34d49ed4f707fb9f83578e7bbb63e1e28a1efb861a487576628ab8a0cbdd032)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ValidatingWebhookConfigurationWebhookOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92dfda61bf298173fc5e46ecd53e9caedbe22e59bda8a1a325062925b1d04e5e)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ValidatingWebhookConfigurationWebhookOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__146eabb0c4f6a774db79b5eee5ef86ed9a0e11a1b83d066c36d6282efd906f9b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__aa2617f9ae2583dbe822ddd20364b491ab774856acda5ccac0e9493604cf20ae)
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
            type_hints = typing.get_type_hints(_typecheckingstub__723fc3305d47bd482f901abdb381712d8d5849f2b500f421effeb3051b44181c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ValidatingWebhookConfigurationWebhook]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ValidatingWebhookConfigurationWebhook]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ValidatingWebhookConfigurationWebhook]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22af0fc59a92a509e280ca6f552c97ff80e780170254bcc1ad0f839537d8e1ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.validatingWebhookConfiguration.ValidatingWebhookConfigurationWebhookNamespaceSelector",
    jsii_struct_bases=[],
    name_mapping={
        "match_expressions": "matchExpressions",
        "match_labels": "matchLabels",
    },
)
class ValidatingWebhookConfigurationWebhookNamespaceSelector:
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ValidatingWebhookConfigurationWebhookNamespaceSelectorMatchExpressions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param match_expressions: match_expressions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#match_expressions ValidatingWebhookConfiguration#match_expressions}
        :param match_labels: A map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of ``match_expressions``, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#match_labels ValidatingWebhookConfiguration#match_labels}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a288a564ffb56ad59e48914f7845d46461ebed711dad54add71d6f025d48050)
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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ValidatingWebhookConfigurationWebhookNamespaceSelectorMatchExpressions"]]]:
        '''match_expressions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#match_expressions ValidatingWebhookConfiguration#match_expressions}
        '''
        result = self._values.get("match_expressions")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ValidatingWebhookConfigurationWebhookNamespaceSelectorMatchExpressions"]]], result)

    @builtins.property
    def match_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of {key,value} pairs.

        A single {key,value} in the matchLabels map is equivalent to an element of ``match_expressions``, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#match_labels ValidatingWebhookConfiguration#match_labels}
        '''
        result = self._values.get("match_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ValidatingWebhookConfigurationWebhookNamespaceSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.validatingWebhookConfiguration.ValidatingWebhookConfigurationWebhookNamespaceSelectorMatchExpressions",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class ValidatingWebhookConfigurationWebhookNamespaceSelectorMatchExpressions:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        operator: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: The label key that the selector applies to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#key ValidatingWebhookConfiguration#key}
        :param operator: A key's relationship to a set of values. Valid operators ard ``In``, ``NotIn``, ``Exists`` and ``DoesNotExist``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#operator ValidatingWebhookConfiguration#operator}
        :param values: An array of string values. If the operator is ``In`` or ``NotIn``, the values array must be non-empty. If the operator is ``Exists`` or ``DoesNotExist``, the values array must be empty. This array is replaced during a strategic merge patch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#values ValidatingWebhookConfiguration#values}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9da65697217b7d047cdebbd6f18e0cafca226b4f54f0b09d06a2d557ab310dbd)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#key ValidatingWebhookConfiguration#key}
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''A key's relationship to a set of values. Valid operators ard ``In``, ``NotIn``, ``Exists`` and ``DoesNotExist``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#operator ValidatingWebhookConfiguration#operator}
        '''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of string values.

        If the operator is ``In`` or ``NotIn``, the values array must be non-empty. If the operator is ``Exists`` or ``DoesNotExist``, the values array must be empty. This array is replaced during a strategic merge patch.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#values ValidatingWebhookConfiguration#values}
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ValidatingWebhookConfigurationWebhookNamespaceSelectorMatchExpressions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ValidatingWebhookConfigurationWebhookNamespaceSelectorMatchExpressionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.validatingWebhookConfiguration.ValidatingWebhookConfigurationWebhookNamespaceSelectorMatchExpressionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a77f554891c3204350fd00efefa31b799b81a5066b5ce73f02d80060f8a91192)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ValidatingWebhookConfigurationWebhookNamespaceSelectorMatchExpressionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8900f68f81a812ba463d8fb893daafb047d1feeaacf01754b551e24be1d6a1a7)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ValidatingWebhookConfigurationWebhookNamespaceSelectorMatchExpressionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab0c54cdbdf2e7bf7f503864ac3165b6c6e6c0d0d317e9fc1706bbe4f9dc0273)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2f634a1412d1888d1521891ef701dc9f7851800f69c4bd3e67eee1e847baf24e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d391065ce08f338fd6916d0550c2c0f2ac40df8b905300a5e51572dbdbb30754)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ValidatingWebhookConfigurationWebhookNamespaceSelectorMatchExpressions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ValidatingWebhookConfigurationWebhookNamespaceSelectorMatchExpressions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ValidatingWebhookConfigurationWebhookNamespaceSelectorMatchExpressions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68efc5559dc93372c9bd8aa1919f11be2aea6f2efc150f5d696ac07eadfbc762)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ValidatingWebhookConfigurationWebhookNamespaceSelectorMatchExpressionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.validatingWebhookConfiguration.ValidatingWebhookConfigurationWebhookNamespaceSelectorMatchExpressionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2affa847c76d6c2d17b457d2f91fe110bcb2374803adc2a8ba52ba33c738bb8d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4eace623fe6861211f3591388c17665b24cef703f4ae5643578df03e093a01f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f89292306407526e161fda4ff26dfa4f5ea2d8dbbc997a3a1781f66334ae18f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6f85cd6e0767b68e000727fca3ea69f0db45e49f18ccff512c5cd5a27a9e6cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ValidatingWebhookConfigurationWebhookNamespaceSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ValidatingWebhookConfigurationWebhookNamespaceSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ValidatingWebhookConfigurationWebhookNamespaceSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92623ff0a139213f0ae21686c18cc6cd7ba7ea90bc057eaea57338f17481995d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ValidatingWebhookConfigurationWebhookNamespaceSelectorOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.validatingWebhookConfiguration.ValidatingWebhookConfigurationWebhookNamespaceSelectorOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2c6e67522191891b388b0096123b969d7b2b33fb85d83c86d178fe238650bd5c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMatchExpressions")
    def put_match_expressions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ValidatingWebhookConfigurationWebhookNamespaceSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eab8406807f1145bf5e7a99a3bc9da6aa0f387a28b47d6add062988c49e8fab8)
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
    ) -> ValidatingWebhookConfigurationWebhookNamespaceSelectorMatchExpressionsList:
        return typing.cast(ValidatingWebhookConfigurationWebhookNamespaceSelectorMatchExpressionsList, jsii.get(self, "matchExpressions"))

    @builtins.property
    @jsii.member(jsii_name="matchExpressionsInput")
    def match_expressions_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ValidatingWebhookConfigurationWebhookNamespaceSelectorMatchExpressions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ValidatingWebhookConfigurationWebhookNamespaceSelectorMatchExpressions]]], jsii.get(self, "matchExpressionsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__cb9550163bef57c81f5f830228a354ceb0917605437b846f340ad85bf2e00903)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchLabels", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ValidatingWebhookConfigurationWebhookNamespaceSelector]:
        return typing.cast(typing.Optional[ValidatingWebhookConfigurationWebhookNamespaceSelector], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ValidatingWebhookConfigurationWebhookNamespaceSelector],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49dd190824f0c052f40dbd7a5f0a03954c3403ed9fd7b3484ccc72a8ef9b6693)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.validatingWebhookConfiguration.ValidatingWebhookConfigurationWebhookObjectSelector",
    jsii_struct_bases=[],
    name_mapping={
        "match_expressions": "matchExpressions",
        "match_labels": "matchLabels",
    },
)
class ValidatingWebhookConfigurationWebhookObjectSelector:
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ValidatingWebhookConfigurationWebhookObjectSelectorMatchExpressions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param match_expressions: match_expressions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#match_expressions ValidatingWebhookConfiguration#match_expressions}
        :param match_labels: A map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of ``match_expressions``, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#match_labels ValidatingWebhookConfiguration#match_labels}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__458be6cb9ab66da6f3d3bd3ee83bc29f1df5b4f2ac20d27b15886249e0eda5ee)
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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ValidatingWebhookConfigurationWebhookObjectSelectorMatchExpressions"]]]:
        '''match_expressions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#match_expressions ValidatingWebhookConfiguration#match_expressions}
        '''
        result = self._values.get("match_expressions")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ValidatingWebhookConfigurationWebhookObjectSelectorMatchExpressions"]]], result)

    @builtins.property
    def match_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of {key,value} pairs.

        A single {key,value} in the matchLabels map is equivalent to an element of ``match_expressions``, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#match_labels ValidatingWebhookConfiguration#match_labels}
        '''
        result = self._values.get("match_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ValidatingWebhookConfigurationWebhookObjectSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.validatingWebhookConfiguration.ValidatingWebhookConfigurationWebhookObjectSelectorMatchExpressions",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class ValidatingWebhookConfigurationWebhookObjectSelectorMatchExpressions:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        operator: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: The label key that the selector applies to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#key ValidatingWebhookConfiguration#key}
        :param operator: A key's relationship to a set of values. Valid operators ard ``In``, ``NotIn``, ``Exists`` and ``DoesNotExist``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#operator ValidatingWebhookConfiguration#operator}
        :param values: An array of string values. If the operator is ``In`` or ``NotIn``, the values array must be non-empty. If the operator is ``Exists`` or ``DoesNotExist``, the values array must be empty. This array is replaced during a strategic merge patch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#values ValidatingWebhookConfiguration#values}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__897ac043dd182c99e30c8d4b777fb69c1853632e168fa2265c1649432a38fb7a)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#key ValidatingWebhookConfiguration#key}
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''A key's relationship to a set of values. Valid operators ard ``In``, ``NotIn``, ``Exists`` and ``DoesNotExist``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#operator ValidatingWebhookConfiguration#operator}
        '''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of string values.

        If the operator is ``In`` or ``NotIn``, the values array must be non-empty. If the operator is ``Exists`` or ``DoesNotExist``, the values array must be empty. This array is replaced during a strategic merge patch.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#values ValidatingWebhookConfiguration#values}
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ValidatingWebhookConfigurationWebhookObjectSelectorMatchExpressions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ValidatingWebhookConfigurationWebhookObjectSelectorMatchExpressionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.validatingWebhookConfiguration.ValidatingWebhookConfigurationWebhookObjectSelectorMatchExpressionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__aa4e180d3053e3057e8bd6cc9334055b4140e3ebce3258eb182237eb06078ef3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ValidatingWebhookConfigurationWebhookObjectSelectorMatchExpressionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__772ce08a1d00c6d39f366ebec4cff67afa8cbf6c9feff8c4badacf3b05d50183)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ValidatingWebhookConfigurationWebhookObjectSelectorMatchExpressionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f9c5e899bd852b7364bcdc65dbb9a7aa78764d75dc4343cadcb52b4cba5e6cb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2e42276706facbfeba57bf28ac015fe5d248fbe942bfd364f2ed129e9e5c78e1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__de98ff8bafa2560eaf9257073c47db7cc0e4fbcca03f57c139c46583202310a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ValidatingWebhookConfigurationWebhookObjectSelectorMatchExpressions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ValidatingWebhookConfigurationWebhookObjectSelectorMatchExpressions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ValidatingWebhookConfigurationWebhookObjectSelectorMatchExpressions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af146fc4a5611bbe732c31d6a7046a4324a4e569f7d61d0136478f8003511812)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ValidatingWebhookConfigurationWebhookObjectSelectorMatchExpressionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.validatingWebhookConfiguration.ValidatingWebhookConfigurationWebhookObjectSelectorMatchExpressionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__25620d5a1334ec01709f4a15b79588b6388e9d479b37fcbfac3ebf990d1b97a7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c995b97d5ed66925779b73ffd74922aada59b3b6b041487e7f875479de042a70)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40c50c4eabe3a463c8a2da83fb33eeea0b6368f4a32cf44ed1d4d80f28fa9918)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b6e91f40d5babf4d641df000391a08c003a74f0eec8de4d255f148d4e0a93ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ValidatingWebhookConfigurationWebhookObjectSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ValidatingWebhookConfigurationWebhookObjectSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ValidatingWebhookConfigurationWebhookObjectSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d88d8ce19394b23240a5349f39def3acfa9cf5fd5fe0d971714f244d63ea30a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ValidatingWebhookConfigurationWebhookObjectSelectorOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.validatingWebhookConfiguration.ValidatingWebhookConfigurationWebhookObjectSelectorOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0730fe1bdd68b34b643574f3e820f3d0c9fa383bad8aab1daa487e3bf0871114)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMatchExpressions")
    def put_match_expressions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ValidatingWebhookConfigurationWebhookObjectSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86284ade657e837cda508e59729ba1f80387e61598ca1bc272218ef5dbcc0807)
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
    ) -> ValidatingWebhookConfigurationWebhookObjectSelectorMatchExpressionsList:
        return typing.cast(ValidatingWebhookConfigurationWebhookObjectSelectorMatchExpressionsList, jsii.get(self, "matchExpressions"))

    @builtins.property
    @jsii.member(jsii_name="matchExpressionsInput")
    def match_expressions_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ValidatingWebhookConfigurationWebhookObjectSelectorMatchExpressions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ValidatingWebhookConfigurationWebhookObjectSelectorMatchExpressions]]], jsii.get(self, "matchExpressionsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__bbf467890986925aa32dc4f68915f81caf142046663926e1db2a7c67bf1f5535)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchLabels", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ValidatingWebhookConfigurationWebhookObjectSelector]:
        return typing.cast(typing.Optional[ValidatingWebhookConfigurationWebhookObjectSelector], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ValidatingWebhookConfigurationWebhookObjectSelector],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__662ef9aadd70bb1188abc72e295bffc48c7305ab53bbe6542d37256a4db8dfda)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ValidatingWebhookConfigurationWebhookOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.validatingWebhookConfiguration.ValidatingWebhookConfigurationWebhookOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__99db1eed32b6843dc46afe9e4bcca0d720db1185d83f2e4a73942528d1d7a0b3)
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
        service: typing.Optional[typing.Union[ValidatingWebhookConfigurationWebhookClientConfigService, typing.Dict[builtins.str, typing.Any]]] = None,
        url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param ca_bundle: ``caBundle`` is a PEM encoded CA bundle which will be used to validate the webhook's server certificate. If unspecified, system trust roots on the apiserver are used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#ca_bundle ValidatingWebhookConfiguration#ca_bundle}
        :param service: service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#service ValidatingWebhookConfiguration#service}
        :param url: ``url`` gives the location of the webhook, in standard URL form (``scheme://host:port/path``). Exactly one of ``url`` or ``service`` must be specified. The ``host`` should not refer to a service running in the cluster; use the ``service`` field instead. The host might be resolved via external DNS in some apiservers (e.g., ``kube-apiserver`` cannot resolve in-cluster DNS as that would be a layering violation). ``host`` may also be an IP address. Please note that using ``localhost`` or ``127.0.0.1`` as a ``host`` is risky unless you take great care to run this webhook on all hosts which run an apiserver which might need to make calls to this webhook. Such installs are likely to be non-portable, i.e., not easy to turn up in a new cluster. The scheme must be "https"; the URL must begin with "https://". A path is optional, and if present may be any string permissible in a URL. You may use the path to pass an arbitrary string to the webhook, for example, a cluster identifier. Attempting to use a user or basic auth e.g. "user:password@" is not allowed. Fragments ("#...") and query parameters ("?...") are not allowed, either. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#url ValidatingWebhookConfiguration#url}
        '''
        value = ValidatingWebhookConfigurationWebhookClientConfig(
            ca_bundle=ca_bundle, service=service, url=url
        )

        return typing.cast(None, jsii.invoke(self, "putClientConfig", [value]))

    @jsii.member(jsii_name="putNamespaceSelector")
    def put_namespace_selector(
        self,
        *,
        match_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ValidatingWebhookConfigurationWebhookNamespaceSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]]] = None,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param match_expressions: match_expressions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#match_expressions ValidatingWebhookConfiguration#match_expressions}
        :param match_labels: A map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of ``match_expressions``, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#match_labels ValidatingWebhookConfiguration#match_labels}
        '''
        value = ValidatingWebhookConfigurationWebhookNamespaceSelector(
            match_expressions=match_expressions, match_labels=match_labels
        )

        return typing.cast(None, jsii.invoke(self, "putNamespaceSelector", [value]))

    @jsii.member(jsii_name="putObjectSelector")
    def put_object_selector(
        self,
        *,
        match_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ValidatingWebhookConfigurationWebhookObjectSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]]] = None,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param match_expressions: match_expressions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#match_expressions ValidatingWebhookConfiguration#match_expressions}
        :param match_labels: A map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of ``match_expressions``, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#match_labels ValidatingWebhookConfiguration#match_labels}
        '''
        value = ValidatingWebhookConfigurationWebhookObjectSelector(
            match_expressions=match_expressions, match_labels=match_labels
        )

        return typing.cast(None, jsii.invoke(self, "putObjectSelector", [value]))

    @jsii.member(jsii_name="putRule")
    def put_rule(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ValidatingWebhookConfigurationWebhookRule", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aecf461163790152936cd64b1c51ecfdb71e2c2422398038ef86bf2136ce70fe)
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
    ) -> ValidatingWebhookConfigurationWebhookClientConfigOutputReference:
        return typing.cast(ValidatingWebhookConfigurationWebhookClientConfigOutputReference, jsii.get(self, "clientConfig"))

    @builtins.property
    @jsii.member(jsii_name="namespaceSelector")
    def namespace_selector(
        self,
    ) -> ValidatingWebhookConfigurationWebhookNamespaceSelectorOutputReference:
        return typing.cast(ValidatingWebhookConfigurationWebhookNamespaceSelectorOutputReference, jsii.get(self, "namespaceSelector"))

    @builtins.property
    @jsii.member(jsii_name="objectSelector")
    def object_selector(
        self,
    ) -> ValidatingWebhookConfigurationWebhookObjectSelectorOutputReference:
        return typing.cast(ValidatingWebhookConfigurationWebhookObjectSelectorOutputReference, jsii.get(self, "objectSelector"))

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> "ValidatingWebhookConfigurationWebhookRuleList":
        return typing.cast("ValidatingWebhookConfigurationWebhookRuleList", jsii.get(self, "rule"))

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
    ) -> typing.Optional[ValidatingWebhookConfigurationWebhookClientConfig]:
        return typing.cast(typing.Optional[ValidatingWebhookConfigurationWebhookClientConfig], jsii.get(self, "clientConfigInput"))

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
    ) -> typing.Optional[ValidatingWebhookConfigurationWebhookNamespaceSelector]:
        return typing.cast(typing.Optional[ValidatingWebhookConfigurationWebhookNamespaceSelector], jsii.get(self, "namespaceSelectorInput"))

    @builtins.property
    @jsii.member(jsii_name="objectSelectorInput")
    def object_selector_input(
        self,
    ) -> typing.Optional[ValidatingWebhookConfigurationWebhookObjectSelector]:
        return typing.cast(typing.Optional[ValidatingWebhookConfigurationWebhookObjectSelector], jsii.get(self, "objectSelectorInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ValidatingWebhookConfigurationWebhookRule"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ValidatingWebhookConfigurationWebhookRule"]]], jsii.get(self, "ruleInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__9ec5cd99f7d7dd9e4701b7133e7e0c841f52f4c59c8d85daee199cc85e7693fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "admissionReviewVersions", value)

    @builtins.property
    @jsii.member(jsii_name="failurePolicy")
    def failure_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "failurePolicy"))

    @failure_policy.setter
    def failure_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30b712cb3e8fef177311392a8b760e80c3ecb49cd3a2f988eb1304019dc66586)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failurePolicy", value)

    @builtins.property
    @jsii.member(jsii_name="matchPolicy")
    def match_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "matchPolicy"))

    @match_policy.setter
    def match_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd6e502cb50be55dd6f4518ecda70a00dea383c5ec06de749699537187647b28)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3fe83e425f325a6ffc1cf18c9f67c1a8bcdcee9f6c2ad9fca3c01bb903ca8086)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="sideEffects")
    def side_effects(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sideEffects"))

    @side_effects.setter
    def side_effects(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5ebde04cb0a35a1c89e1832b0cded9b2bf24b375faa435db1e79d4d1e75b831)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sideEffects", value)

    @builtins.property
    @jsii.member(jsii_name="timeoutSeconds")
    def timeout_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeoutSeconds"))

    @timeout_seconds.setter
    def timeout_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62c59267ab15178fac0c4c2da5160e604fd94d58b3ebe3fd8875abe0acc53eab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ValidatingWebhookConfigurationWebhook, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ValidatingWebhookConfigurationWebhook, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ValidatingWebhookConfigurationWebhook, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca7661b682990ad45be0cc90b5f8c31aba0330473796392258371e2f3261c050)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.validatingWebhookConfiguration.ValidatingWebhookConfigurationWebhookRule",
    jsii_struct_bases=[],
    name_mapping={
        "api_groups": "apiGroups",
        "api_versions": "apiVersions",
        "operations": "operations",
        "resources": "resources",
        "scope": "scope",
    },
)
class ValidatingWebhookConfigurationWebhookRule:
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
        :param api_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#api_groups ValidatingWebhookConfiguration#api_groups}.
        :param api_versions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#api_versions ValidatingWebhookConfiguration#api_versions}.
        :param operations: Operations is the operations the admission hook cares about - CREATE, UPDATE, DELETE, CONNECT or * for all of those operations and any future admission operations that are added. If '*' is present, the length of the slice must be one. Required. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#operations ValidatingWebhookConfiguration#operations}
        :param resources: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#resources ValidatingWebhookConfiguration#resources}.
        :param scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#scope ValidatingWebhookConfiguration#scope}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1b76a0f4cacaa54c21f931b468617625bba1c109ce2bd5e4da3f67a3c429945)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#api_groups ValidatingWebhookConfiguration#api_groups}.'''
        result = self._values.get("api_groups")
        assert result is not None, "Required property 'api_groups' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def api_versions(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#api_versions ValidatingWebhookConfiguration#api_versions}.'''
        result = self._values.get("api_versions")
        assert result is not None, "Required property 'api_versions' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def operations(self) -> typing.List[builtins.str]:
        '''Operations is the operations the admission hook cares about - CREATE, UPDATE, DELETE, CONNECT or * for all of those operations and any future admission operations that are added.

        If '*' is present, the length of the slice must be one. Required.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#operations ValidatingWebhookConfiguration#operations}
        '''
        result = self._values.get("operations")
        assert result is not None, "Required property 'operations' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def resources(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#resources ValidatingWebhookConfiguration#resources}.'''
        result = self._values.get("resources")
        assert result is not None, "Required property 'resources' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def scope(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration#scope ValidatingWebhookConfiguration#scope}.'''
        result = self._values.get("scope")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ValidatingWebhookConfigurationWebhookRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ValidatingWebhookConfigurationWebhookRuleList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.validatingWebhookConfiguration.ValidatingWebhookConfigurationWebhookRuleList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__82a90324b9131d1eace410da9b0f0de61e1b07c92c7b5cd4557eb25a0c06bce7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ValidatingWebhookConfigurationWebhookRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee07d084673832213280fef8b1b251b60f9012c6cf74738388e690a4e64c244c)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ValidatingWebhookConfigurationWebhookRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79a3acfc005a7c4bf7a7c457797a0d72aa2ba6d2c9d7b3905a7907f24df25c67)
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
            type_hints = typing.get_type_hints(_typecheckingstub__25d011058659dfc1e86807d8223b588c1545caf16811a0b24e91e62e341ef764)
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
            type_hints = typing.get_type_hints(_typecheckingstub__32afa7860953be4f21ff91dfccf135bba4ea9454295bb2d7d19a472910117d3f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ValidatingWebhookConfigurationWebhookRule]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ValidatingWebhookConfigurationWebhookRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ValidatingWebhookConfigurationWebhookRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6fea249c97217320417f2201f391aa7b23c6f022f51900aeb213ba16069744ca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ValidatingWebhookConfigurationWebhookRuleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.validatingWebhookConfiguration.ValidatingWebhookConfigurationWebhookRuleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__56126d3dc741da0aac95f5396779ce1a7849d7f5e7ac49d7825d1770102ffa9d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__720bb809c11fb044533cdcb476d8f569b2d3c556575cbd0e830aa9b0755676a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiGroups", value)

    @builtins.property
    @jsii.member(jsii_name="apiVersions")
    def api_versions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "apiVersions"))

    @api_versions.setter
    def api_versions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48011e02413f991b7f7671eedba8ee6dbbe7dd3e6c910022fb36b9c4af0739cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiVersions", value)

    @builtins.property
    @jsii.member(jsii_name="operations")
    def operations(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "operations"))

    @operations.setter
    def operations(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a925831647e2d0fcce7973dd472b8fb8f05eaadb59d235daca875a3b5d9d1c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operations", value)

    @builtins.property
    @jsii.member(jsii_name="resources")
    def resources(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "resources"))

    @resources.setter
    def resources(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3de1c85744f52b062124ceef2b25c9552f2ae07e7b0c8128e02db453e5ee003f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resources", value)

    @builtins.property
    @jsii.member(jsii_name="scope")
    def scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scope"))

    @scope.setter
    def scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65fcfc8ce63408f582b8ddeb60cc8bd5dd7b8ae0a2a9ee6f4446c824c5a93cf1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scope", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ValidatingWebhookConfigurationWebhookRule, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ValidatingWebhookConfigurationWebhookRule, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ValidatingWebhookConfigurationWebhookRule, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f359622e8351914025b71d238cdb41f613fe5f8a03e5ca87eb5a154911ae629a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ValidatingWebhookConfiguration",
    "ValidatingWebhookConfigurationConfig",
    "ValidatingWebhookConfigurationMetadata",
    "ValidatingWebhookConfigurationMetadataOutputReference",
    "ValidatingWebhookConfigurationWebhook",
    "ValidatingWebhookConfigurationWebhookClientConfig",
    "ValidatingWebhookConfigurationWebhookClientConfigOutputReference",
    "ValidatingWebhookConfigurationWebhookClientConfigService",
    "ValidatingWebhookConfigurationWebhookClientConfigServiceOutputReference",
    "ValidatingWebhookConfigurationWebhookList",
    "ValidatingWebhookConfigurationWebhookNamespaceSelector",
    "ValidatingWebhookConfigurationWebhookNamespaceSelectorMatchExpressions",
    "ValidatingWebhookConfigurationWebhookNamespaceSelectorMatchExpressionsList",
    "ValidatingWebhookConfigurationWebhookNamespaceSelectorMatchExpressionsOutputReference",
    "ValidatingWebhookConfigurationWebhookNamespaceSelectorOutputReference",
    "ValidatingWebhookConfigurationWebhookObjectSelector",
    "ValidatingWebhookConfigurationWebhookObjectSelectorMatchExpressions",
    "ValidatingWebhookConfigurationWebhookObjectSelectorMatchExpressionsList",
    "ValidatingWebhookConfigurationWebhookObjectSelectorMatchExpressionsOutputReference",
    "ValidatingWebhookConfigurationWebhookObjectSelectorOutputReference",
    "ValidatingWebhookConfigurationWebhookOutputReference",
    "ValidatingWebhookConfigurationWebhookRule",
    "ValidatingWebhookConfigurationWebhookRuleList",
    "ValidatingWebhookConfigurationWebhookRuleOutputReference",
]

publication.publish()

def _typecheckingstub__1be00009fe1623b2547fe440035670ec35a74233bbec2b4e3b29f17c41aa1482(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    metadata: typing.Union[ValidatingWebhookConfigurationMetadata, typing.Dict[builtins.str, typing.Any]],
    webhook: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ValidatingWebhookConfigurationWebhook, typing.Dict[builtins.str, typing.Any]]]],
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

def _typecheckingstub__6b79ee33705090b1ec2e83215aa8b5b618c9521cadbea6c4a01d10cf2857a07b(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ValidatingWebhookConfigurationWebhook, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61bbaebe3a9d96e5f8888a20fcd482d19ac01f5547e328b998a66828b250f907(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__797b05ce740994871805f95e0af875c6521f469507703342520cee75427ee0de(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    metadata: typing.Union[ValidatingWebhookConfigurationMetadata, typing.Dict[builtins.str, typing.Any]],
    webhook: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ValidatingWebhookConfigurationWebhook, typing.Dict[builtins.str, typing.Any]]]],
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e72260881c0ff219034c1cafd9de2b336333f09734fbb3c3ba42c60d88403854(
    *,
    annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    generate_name: typing.Optional[builtins.str] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08f8c00b7c2be73cba07523a483aa6248aa0da8827b340882d2988ca43d5c5e3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6511c660fa1b20f87cc81cb26e03cf4f1ef3da899f6bc189e109fb2a57777d11(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74bdf4309cb32eb23957a0276b2ef41c4ae8df825ea918c19153d4b9d9d9120d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccc1d25077996ce5457b53cce6714dfe02e1e3b7c28c847b15fed27709d88d8b(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2050abc5529493e589f63fac79553a37a3f05b40b4a0b895b636d74ae22f2b20(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce7a4ffb9beca1a8bb8cad9fb8a476a6a2e23efce68dc09f7e5691b12e115272(
    value: typing.Optional[ValidatingWebhookConfigurationMetadata],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1a81b69e7defb7ccff5922ec20ec9a42457667c9d790c36d694c97d097ff116(
    *,
    client_config: typing.Union[ValidatingWebhookConfigurationWebhookClientConfig, typing.Dict[builtins.str, typing.Any]],
    name: builtins.str,
    admission_review_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
    failure_policy: typing.Optional[builtins.str] = None,
    match_policy: typing.Optional[builtins.str] = None,
    namespace_selector: typing.Optional[typing.Union[ValidatingWebhookConfigurationWebhookNamespaceSelector, typing.Dict[builtins.str, typing.Any]]] = None,
    object_selector: typing.Optional[typing.Union[ValidatingWebhookConfigurationWebhookObjectSelector, typing.Dict[builtins.str, typing.Any]]] = None,
    rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ValidatingWebhookConfigurationWebhookRule, typing.Dict[builtins.str, typing.Any]]]]] = None,
    side_effects: typing.Optional[builtins.str] = None,
    timeout_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__286f0e06b6ca1ad159fc6811c06d9627b18e7bc8024932d2b1ccb0f4e05afcd2(
    *,
    ca_bundle: typing.Optional[builtins.str] = None,
    service: typing.Optional[typing.Union[ValidatingWebhookConfigurationWebhookClientConfigService, typing.Dict[builtins.str, typing.Any]]] = None,
    url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5707471e1f4044340754bc8486dc2bbc0d0178b0614e047b594dfba09ec7cc1a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b629823356e9d971a8252f2d5cb2dbef0d9328411706e6ee7d080f86954c8ca1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__441ba746745333ca0e0f399fcba4bf0c9a2605762d5dc9e5840817fe0cbd676a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e93d6a3e9ef51b9557ed3583274823da36124bb991b533f1d4632aaa0bcae50(
    value: typing.Optional[ValidatingWebhookConfigurationWebhookClientConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d4928d2a88f11133864981ef96f2589b74b72f21d90087092978d766de1e11a(
    *,
    name: builtins.str,
    namespace: builtins.str,
    path: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__752f4687b61b1b17029e9fe1fa3df9f5f04a87626ad66a4629b5b42aa0388f2a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4dee8a1539285f79f830315833ec6694e5494f7544621f71257841df23cf71d6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__053d68bff3714edb94a67bb498c4d0a4359951e98d3b4fa37e0da6730f54df28(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__431621ef57cef5dd1a4d62b6da70e1ae4c3fcc2b78270104f536172015f7d013(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1610840e1adc47d59bcff8df3c369713af4454aa56f923da0352039b539f82dc(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2dd0b63bbc6c74aa207e18a3c11636e3cec8b974b77d88b5c82ecabc02753fc1(
    value: typing.Optional[ValidatingWebhookConfigurationWebhookClientConfigService],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c34d49ed4f707fb9f83578e7bbb63e1e28a1efb861a487576628ab8a0cbdd032(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92dfda61bf298173fc5e46ecd53e9caedbe22e59bda8a1a325062925b1d04e5e(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__146eabb0c4f6a774db79b5eee5ef86ed9a0e11a1b83d066c36d6282efd906f9b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa2617f9ae2583dbe822ddd20364b491ab774856acda5ccac0e9493604cf20ae(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__723fc3305d47bd482f901abdb381712d8d5849f2b500f421effeb3051b44181c(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22af0fc59a92a509e280ca6f552c97ff80e780170254bcc1ad0f839537d8e1ec(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ValidatingWebhookConfigurationWebhook]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a288a564ffb56ad59e48914f7845d46461ebed711dad54add71d6f025d48050(
    *,
    match_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ValidatingWebhookConfigurationWebhookNamespaceSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9da65697217b7d047cdebbd6f18e0cafca226b4f54f0b09d06a2d557ab310dbd(
    *,
    key: typing.Optional[builtins.str] = None,
    operator: typing.Optional[builtins.str] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a77f554891c3204350fd00efefa31b799b81a5066b5ce73f02d80060f8a91192(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8900f68f81a812ba463d8fb893daafb047d1feeaacf01754b551e24be1d6a1a7(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab0c54cdbdf2e7bf7f503864ac3165b6c6e6c0d0d317e9fc1706bbe4f9dc0273(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f634a1412d1888d1521891ef701dc9f7851800f69c4bd3e67eee1e847baf24e(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d391065ce08f338fd6916d0550c2c0f2ac40df8b905300a5e51572dbdbb30754(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68efc5559dc93372c9bd8aa1919f11be2aea6f2efc150f5d696ac07eadfbc762(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ValidatingWebhookConfigurationWebhookNamespaceSelectorMatchExpressions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2affa847c76d6c2d17b457d2f91fe110bcb2374803adc2a8ba52ba33c738bb8d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4eace623fe6861211f3591388c17665b24cef703f4ae5643578df03e093a01f3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f89292306407526e161fda4ff26dfa4f5ea2d8dbbc997a3a1781f66334ae18f3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6f85cd6e0767b68e000727fca3ea69f0db45e49f18ccff512c5cd5a27a9e6cf(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92623ff0a139213f0ae21686c18cc6cd7ba7ea90bc057eaea57338f17481995d(
    value: typing.Optional[typing.Union[ValidatingWebhookConfigurationWebhookNamespaceSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c6e67522191891b388b0096123b969d7b2b33fb85d83c86d178fe238650bd5c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eab8406807f1145bf5e7a99a3bc9da6aa0f387a28b47d6add062988c49e8fab8(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ValidatingWebhookConfigurationWebhookNamespaceSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb9550163bef57c81f5f830228a354ceb0917605437b846f340ad85bf2e00903(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49dd190824f0c052f40dbd7a5f0a03954c3403ed9fd7b3484ccc72a8ef9b6693(
    value: typing.Optional[ValidatingWebhookConfigurationWebhookNamespaceSelector],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__458be6cb9ab66da6f3d3bd3ee83bc29f1df5b4f2ac20d27b15886249e0eda5ee(
    *,
    match_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ValidatingWebhookConfigurationWebhookObjectSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__897ac043dd182c99e30c8d4b777fb69c1853632e168fa2265c1649432a38fb7a(
    *,
    key: typing.Optional[builtins.str] = None,
    operator: typing.Optional[builtins.str] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa4e180d3053e3057e8bd6cc9334055b4140e3ebce3258eb182237eb06078ef3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__772ce08a1d00c6d39f366ebec4cff67afa8cbf6c9feff8c4badacf3b05d50183(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f9c5e899bd852b7364bcdc65dbb9a7aa78764d75dc4343cadcb52b4cba5e6cb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e42276706facbfeba57bf28ac015fe5d248fbe942bfd364f2ed129e9e5c78e1(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de98ff8bafa2560eaf9257073c47db7cc0e4fbcca03f57c139c46583202310a7(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af146fc4a5611bbe732c31d6a7046a4324a4e569f7d61d0136478f8003511812(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ValidatingWebhookConfigurationWebhookObjectSelectorMatchExpressions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25620d5a1334ec01709f4a15b79588b6388e9d479b37fcbfac3ebf990d1b97a7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c995b97d5ed66925779b73ffd74922aada59b3b6b041487e7f875479de042a70(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40c50c4eabe3a463c8a2da83fb33eeea0b6368f4a32cf44ed1d4d80f28fa9918(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b6e91f40d5babf4d641df000391a08c003a74f0eec8de4d255f148d4e0a93ba(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d88d8ce19394b23240a5349f39def3acfa9cf5fd5fe0d971714f244d63ea30a(
    value: typing.Optional[typing.Union[ValidatingWebhookConfigurationWebhookObjectSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0730fe1bdd68b34b643574f3e820f3d0c9fa383bad8aab1daa487e3bf0871114(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86284ade657e837cda508e59729ba1f80387e61598ca1bc272218ef5dbcc0807(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ValidatingWebhookConfigurationWebhookObjectSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbf467890986925aa32dc4f68915f81caf142046663926e1db2a7c67bf1f5535(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__662ef9aadd70bb1188abc72e295bffc48c7305ab53bbe6542d37256a4db8dfda(
    value: typing.Optional[ValidatingWebhookConfigurationWebhookObjectSelector],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99db1eed32b6843dc46afe9e4bcca0d720db1185d83f2e4a73942528d1d7a0b3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aecf461163790152936cd64b1c51ecfdb71e2c2422398038ef86bf2136ce70fe(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ValidatingWebhookConfigurationWebhookRule, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ec5cd99f7d7dd9e4701b7133e7e0c841f52f4c59c8d85daee199cc85e7693fd(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30b712cb3e8fef177311392a8b760e80c3ecb49cd3a2f988eb1304019dc66586(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd6e502cb50be55dd6f4518ecda70a00dea383c5ec06de749699537187647b28(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fe83e425f325a6ffc1cf18c9f67c1a8bcdcee9f6c2ad9fca3c01bb903ca8086(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5ebde04cb0a35a1c89e1832b0cded9b2bf24b375faa435db1e79d4d1e75b831(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62c59267ab15178fac0c4c2da5160e604fd94d58b3ebe3fd8875abe0acc53eab(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca7661b682990ad45be0cc90b5f8c31aba0330473796392258371e2f3261c050(
    value: typing.Optional[typing.Union[ValidatingWebhookConfigurationWebhook, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1b76a0f4cacaa54c21f931b468617625bba1c109ce2bd5e4da3f67a3c429945(
    *,
    api_groups: typing.Sequence[builtins.str],
    api_versions: typing.Sequence[builtins.str],
    operations: typing.Sequence[builtins.str],
    resources: typing.Sequence[builtins.str],
    scope: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82a90324b9131d1eace410da9b0f0de61e1b07c92c7b5cd4557eb25a0c06bce7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee07d084673832213280fef8b1b251b60f9012c6cf74738388e690a4e64c244c(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79a3acfc005a7c4bf7a7c457797a0d72aa2ba6d2c9d7b3905a7907f24df25c67(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25d011058659dfc1e86807d8223b588c1545caf16811a0b24e91e62e341ef764(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32afa7860953be4f21ff91dfccf135bba4ea9454295bb2d7d19a472910117d3f(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fea249c97217320417f2201f391aa7b23c6f022f51900aeb213ba16069744ca(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ValidatingWebhookConfigurationWebhookRule]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56126d3dc741da0aac95f5396779ce1a7849d7f5e7ac49d7825d1770102ffa9d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__720bb809c11fb044533cdcb476d8f569b2d3c556575cbd0e830aa9b0755676a1(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48011e02413f991b7f7671eedba8ee6dbbe7dd3e6c910022fb36b9c4af0739cc(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a925831647e2d0fcce7973dd472b8fb8f05eaadb59d235daca875a3b5d9d1c1(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3de1c85744f52b062124ceef2b25c9552f2ae07e7b0c8128e02db453e5ee003f(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65fcfc8ce63408f582b8ddeb60cc8bd5dd7b8ae0a2a9ee6f4446c824c5a93cf1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f359622e8351914025b71d238cdb41f613fe5f8a03e5ca87eb5a154911ae629a(
    value: typing.Optional[typing.Union[ValidatingWebhookConfigurationWebhookRule, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
