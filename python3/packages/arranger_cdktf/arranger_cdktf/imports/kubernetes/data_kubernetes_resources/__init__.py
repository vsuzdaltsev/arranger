'''
# `data_kubernetes_resources`

Refer to the Terraform Registory for docs: [`data_kubernetes_resources`](https://www.terraform.io/docs/providers/kubernetes/d/resources).
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


class DataKubernetesResources(
    _cdktf_9a9027ec.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.dataKubernetesResources.DataKubernetesResources",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/kubernetes/d/resources kubernetes_resources}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        api_version: builtins.str,
        kind: builtins.str,
        field_selector: typing.Optional[builtins.str] = None,
        label_selector: typing.Optional[builtins.str] = None,
        limit: typing.Optional[jsii.Number] = None,
        namespace: typing.Optional[builtins.str] = None,
        objects: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/kubernetes/d/resources kubernetes_resources} Data Source.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param api_version: The resource apiVersion. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/resources#api_version DataKubernetesResources#api_version}
        :param kind: The resource kind. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/resources#kind DataKubernetesResources#kind}
        :param field_selector: A selector to restrict the list of returned objects by their fields. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/resources#field_selector DataKubernetesResources#field_selector}
        :param label_selector: A selector to restrict the list of returned objects by their labels. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/resources#label_selector DataKubernetesResources#label_selector}
        :param limit: Limit is a maximum number of responses to return for a list call. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/resources#limit DataKubernetesResources#limit}
        :param namespace: The resource namespace. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/resources#namespace DataKubernetesResources#namespace}
        :param objects: The response from the API server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/resources#objects DataKubernetesResources#objects}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34e5aebc27000ed08d902b2c0602879675d413271208dfb8e89c1e5a5e79152e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = DataKubernetesResourcesConfig(
            api_version=api_version,
            kind=kind,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            namespace=namespace,
            objects=objects,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetFieldSelector")
    def reset_field_selector(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFieldSelector", []))

    @jsii.member(jsii_name="resetLabelSelector")
    def reset_label_selector(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabelSelector", []))

    @jsii.member(jsii_name="resetLimit")
    def reset_limit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLimit", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @jsii.member(jsii_name="resetObjects")
    def reset_objects(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetObjects", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="apiVersionInput")
    def api_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="fieldSelectorInput")
    def field_selector_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fieldSelectorInput"))

    @builtins.property
    @jsii.member(jsii_name="kindInput")
    def kind_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kindInput"))

    @builtins.property
    @jsii.member(jsii_name="labelSelectorInput")
    def label_selector_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "labelSelectorInput"))

    @builtins.property
    @jsii.member(jsii_name="limitInput")
    def limit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "limitInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="objectsInput")
    def objects_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], jsii.get(self, "objectsInput"))

    @builtins.property
    @jsii.member(jsii_name="apiVersion")
    def api_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiVersion"))

    @api_version.setter
    def api_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e09ccf2e2c8f4f188bfa0e5776a410b933855a1db0b3bd0ed01246184fb63f09)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiVersion", value)

    @builtins.property
    @jsii.member(jsii_name="fieldSelector")
    def field_selector(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fieldSelector"))

    @field_selector.setter
    def field_selector(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0bb6c31d529d27e826533b3e7157623633b0753cad5160b8f909a1b243105645)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fieldSelector", value)

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @kind.setter
    def kind(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e57d26de72f7352e6054607a7da4e580df663fd9e1850f87adc0d8c8f149ab2f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kind", value)

    @builtins.property
    @jsii.member(jsii_name="labelSelector")
    def label_selector(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "labelSelector"))

    @label_selector.setter
    def label_selector(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd2a1675fc5724849d9d71ee903c3e419b4581e0e5ae71915f046604f1acf0b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labelSelector", value)

    @builtins.property
    @jsii.member(jsii_name="limit")
    def limit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "limit"))

    @limit.setter
    def limit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e5b9fab3ed6b1c330f1a8aef482d0e1e34686385eb7f34fe9d1c73e2e253bb2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "limit", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fe7a0adb8706c7fdd31ae11587712ae7456a584b6b29410baeeed6ae8c01654)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="objects")
    def objects(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "objects"))

    @objects.setter
    def objects(self, value: typing.Mapping[builtins.str, typing.Any]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d7a9b24997a3fb825843166b4f505ab60581790fe5c5cb6e178551d68219f4c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objects", value)


@jsii.data_type(
    jsii_type="kubernetes.dataKubernetesResources.DataKubernetesResourcesConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "api_version": "apiVersion",
        "kind": "kind",
        "field_selector": "fieldSelector",
        "label_selector": "labelSelector",
        "limit": "limit",
        "namespace": "namespace",
        "objects": "objects",
    },
)
class DataKubernetesResourcesConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        api_version: builtins.str,
        kind: builtins.str,
        field_selector: typing.Optional[builtins.str] = None,
        label_selector: typing.Optional[builtins.str] = None,
        limit: typing.Optional[jsii.Number] = None,
        namespace: typing.Optional[builtins.str] = None,
        objects: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param api_version: The resource apiVersion. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/resources#api_version DataKubernetesResources#api_version}
        :param kind: The resource kind. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/resources#kind DataKubernetesResources#kind}
        :param field_selector: A selector to restrict the list of returned objects by their fields. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/resources#field_selector DataKubernetesResources#field_selector}
        :param label_selector: A selector to restrict the list of returned objects by their labels. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/resources#label_selector DataKubernetesResources#label_selector}
        :param limit: Limit is a maximum number of responses to return for a list call. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/resources#limit DataKubernetesResources#limit}
        :param namespace: The resource namespace. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/resources#namespace DataKubernetesResources#namespace}
        :param objects: The response from the API server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/resources#objects DataKubernetesResources#objects}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28c36d288c7dd24a9d43ce3f6ced02c8a052f1005fe9605a72a8c871d083a0ce)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument api_version", value=api_version, expected_type=type_hints["api_version"])
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
            check_type(argname="argument field_selector", value=field_selector, expected_type=type_hints["field_selector"])
            check_type(argname="argument label_selector", value=label_selector, expected_type=type_hints["label_selector"])
            check_type(argname="argument limit", value=limit, expected_type=type_hints["limit"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument objects", value=objects, expected_type=type_hints["objects"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_version": api_version,
            "kind": kind,
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
        if field_selector is not None:
            self._values["field_selector"] = field_selector
        if label_selector is not None:
            self._values["label_selector"] = label_selector
        if limit is not None:
            self._values["limit"] = limit
        if namespace is not None:
            self._values["namespace"] = namespace
        if objects is not None:
            self._values["objects"] = objects

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
    def api_version(self) -> builtins.str:
        '''The resource apiVersion.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/resources#api_version DataKubernetesResources#api_version}
        '''
        result = self._values.get("api_version")
        assert result is not None, "Required property 'api_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def kind(self) -> builtins.str:
        '''The resource kind.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/resources#kind DataKubernetesResources#kind}
        '''
        result = self._values.get("kind")
        assert result is not None, "Required property 'kind' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def field_selector(self) -> typing.Optional[builtins.str]:
        '''A selector to restrict the list of returned objects by their fields.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/resources#field_selector DataKubernetesResources#field_selector}
        '''
        result = self._values.get("field_selector")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def label_selector(self) -> typing.Optional[builtins.str]:
        '''A selector to restrict the list of returned objects by their labels.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/resources#label_selector DataKubernetesResources#label_selector}
        '''
        result = self._values.get("label_selector")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def limit(self) -> typing.Optional[jsii.Number]:
        '''Limit is a maximum number of responses to return for a list call.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/resources#limit DataKubernetesResources#limit}
        '''
        result = self._values.get("limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''The resource namespace.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/resources#namespace DataKubernetesResources#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def objects(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''The response from the API server.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/resources#objects DataKubernetesResources#objects}
        '''
        result = self._values.get("objects")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKubernetesResourcesConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DataKubernetesResources",
    "DataKubernetesResourcesConfig",
]

publication.publish()

def _typecheckingstub__34e5aebc27000ed08d902b2c0602879675d413271208dfb8e89c1e5a5e79152e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    api_version: builtins.str,
    kind: builtins.str,
    field_selector: typing.Optional[builtins.str] = None,
    label_selector: typing.Optional[builtins.str] = None,
    limit: typing.Optional[jsii.Number] = None,
    namespace: typing.Optional[builtins.str] = None,
    objects: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
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

def _typecheckingstub__e09ccf2e2c8f4f188bfa0e5776a410b933855a1db0b3bd0ed01246184fb63f09(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bb6c31d529d27e826533b3e7157623633b0753cad5160b8f909a1b243105645(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e57d26de72f7352e6054607a7da4e580df663fd9e1850f87adc0d8c8f149ab2f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd2a1675fc5724849d9d71ee903c3e419b4581e0e5ae71915f046604f1acf0b9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e5b9fab3ed6b1c330f1a8aef482d0e1e34686385eb7f34fe9d1c73e2e253bb2(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fe7a0adb8706c7fdd31ae11587712ae7456a584b6b29410baeeed6ae8c01654(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d7a9b24997a3fb825843166b4f505ab60581790fe5c5cb6e178551d68219f4c(
    value: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28c36d288c7dd24a9d43ce3f6ced02c8a052f1005fe9605a72a8c871d083a0ce(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    api_version: builtins.str,
    kind: builtins.str,
    field_selector: typing.Optional[builtins.str] = None,
    label_selector: typing.Optional[builtins.str] = None,
    limit: typing.Optional[jsii.Number] = None,
    namespace: typing.Optional[builtins.str] = None,
    objects: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass
