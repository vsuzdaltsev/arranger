'''
# `kubernetes_manifest`

Refer to the Terraform Registory for docs: [`kubernetes_manifest`](https://www.terraform.io/docs/providers/kubernetes/r/manifest).
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


class Manifest(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.manifest.Manifest",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest kubernetes_manifest}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        manifest: typing.Mapping[builtins.str, typing.Any],
        computed_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
        field_manager: typing.Optional[typing.Union["ManifestFieldManager", typing.Dict[builtins.str, typing.Any]]] = None,
        object: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        timeouts: typing.Optional[typing.Union["ManifestTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        wait: typing.Optional[typing.Union["ManifestWait", typing.Dict[builtins.str, typing.Any]]] = None,
        wait_for: typing.Optional[typing.Union[typing.Union["ManifestWaitFor", typing.Dict[builtins.str, typing.Any]], _cdktf_9a9027ec.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest kubernetes_manifest} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param manifest: A Kubernetes manifest describing the desired state of the resource in HCL format. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#manifest Manifest#manifest}
        :param computed_fields: List of manifest fields whose values can be altered by the API server during 'apply'. Defaults to: ["metadata.annotations", "metadata.labels"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#computed_fields Manifest#computed_fields}
        :param field_manager: field_manager block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#field_manager Manifest#field_manager}
        :param object: The resulting resource state, as returned by the API server after applying the desired state from ``manifest``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#object Manifest#object}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#timeouts Manifest#timeouts}
        :param wait: wait block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#wait Manifest#wait}
        :param wait_for: A map of attribute paths and desired patterns to be matched. After each apply the provider will wait for all attributes listed here to reach a value that matches the desired pattern. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#wait_for Manifest#wait_for}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40157812e663140f6fdd42d0af8ecf268c076e19d6df6503a28a7348726cd2ce)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = ManifestConfig(
            manifest=manifest,
            computed_fields=computed_fields,
            field_manager=field_manager,
            object=object,
            timeouts=timeouts,
            wait=wait,
            wait_for=wait_for,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="putFieldManager")
    def put_field_manager(
        self,
        *,
        force_conflicts: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param force_conflicts: Force changes against conflicts. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#force_conflicts Manifest#force_conflicts}
        :param name: The name to use for the field manager when creating and updating the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#name Manifest#name}
        '''
        value = ManifestFieldManager(force_conflicts=force_conflicts, name=name)

        return typing.cast(None, jsii.invoke(self, "putFieldManager", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Timeout for the create operation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#create Manifest#create}
        :param delete: Timeout for the delete operation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#delete Manifest#delete}
        :param update: Timeout for the update operation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#update Manifest#update}
        '''
        value = ManifestTimeouts(create=create, delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putWait")
    def put_wait(
        self,
        *,
        condition: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ManifestWaitCondition", typing.Dict[builtins.str, typing.Any]]]]] = None,
        fields: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        rollout: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param condition: condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#condition Manifest#condition}
        :param fields: A map of paths to fields to wait for a specific field value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#fields Manifest#fields}
        :param rollout: Wait for rollout to complete on resources that support ``kubectl rollout status``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#rollout Manifest#rollout}
        '''
        value = ManifestWait(condition=condition, fields=fields, rollout=rollout)

        return typing.cast(None, jsii.invoke(self, "putWait", [value]))

    @jsii.member(jsii_name="resetComputedFields")
    def reset_computed_fields(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComputedFields", []))

    @jsii.member(jsii_name="resetFieldManager")
    def reset_field_manager(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFieldManager", []))

    @jsii.member(jsii_name="resetObject")
    def reset_object(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetObject", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetWait")
    def reset_wait(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWait", []))

    @jsii.member(jsii_name="resetWaitFor")
    def reset_wait_for(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWaitFor", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="fieldManager")
    def field_manager(self) -> "ManifestFieldManagerOutputReference":
        return typing.cast("ManifestFieldManagerOutputReference", jsii.get(self, "fieldManager"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ManifestTimeoutsOutputReference":
        return typing.cast("ManifestTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="wait")
    def wait(self) -> "ManifestWaitOutputReference":
        return typing.cast("ManifestWaitOutputReference", jsii.get(self, "wait"))

    @builtins.property
    @jsii.member(jsii_name="computedFieldsInput")
    def computed_fields_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "computedFieldsInput"))

    @builtins.property
    @jsii.member(jsii_name="fieldManagerInput")
    def field_manager_input(self) -> typing.Optional["ManifestFieldManager"]:
        return typing.cast(typing.Optional["ManifestFieldManager"], jsii.get(self, "fieldManagerInput"))

    @builtins.property
    @jsii.member(jsii_name="manifestInput")
    def manifest_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], jsii.get(self, "manifestInput"))

    @builtins.property
    @jsii.member(jsii_name="objectInput")
    def object_input(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(self) -> typing.Optional["ManifestTimeouts"]:
        return typing.cast(typing.Optional["ManifestTimeouts"], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="waitForInput")
    def wait_for_input(
        self,
    ) -> typing.Optional[typing.Union["ManifestWaitFor", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ManifestWaitFor", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "waitForInput"))

    @builtins.property
    @jsii.member(jsii_name="waitInput")
    def wait_input(self) -> typing.Optional["ManifestWait"]:
        return typing.cast(typing.Optional["ManifestWait"], jsii.get(self, "waitInput"))

    @builtins.property
    @jsii.member(jsii_name="computedFields")
    def computed_fields(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "computedFields"))

    @computed_fields.setter
    def computed_fields(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14857a5c9737e7cd61739c774f785080774105cfd53ab505a56c1b8e959c300f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "computedFields", value)

    @builtins.property
    @jsii.member(jsii_name="manifest")
    def manifest(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "manifest"))

    @manifest.setter
    def manifest(self, value: typing.Mapping[builtins.str, typing.Any]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3322d2fa8e410d3561c35a35ad226bec78748b3b040e4187809c4a66d8c1147e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "manifest", value)

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "object"))

    @object.setter
    def object(self, value: typing.Mapping[builtins.str, typing.Any]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83d28b4d34e4cef4a85cb7ed7cb3017a479bab272528e65f013b62ecbb9dabb5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "object", value)

    @builtins.property
    @jsii.member(jsii_name="waitFor")
    def wait_for(self) -> typing.Union["ManifestWaitFor", _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union["ManifestWaitFor", _cdktf_9a9027ec.IResolvable], jsii.get(self, "waitFor"))

    @wait_for.setter
    def wait_for(
        self,
        value: typing.Union["ManifestWaitFor", _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd9cd52f7ae8f8b0465ad8da3ea17fb391b864ac4cb2e0cef7edc4aebc2874c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitFor", value)


@jsii.data_type(
    jsii_type="kubernetes.manifest.ManifestConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "manifest": "manifest",
        "computed_fields": "computedFields",
        "field_manager": "fieldManager",
        "object": "object",
        "timeouts": "timeouts",
        "wait": "wait",
        "wait_for": "waitFor",
    },
)
class ManifestConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        manifest: typing.Mapping[builtins.str, typing.Any],
        computed_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
        field_manager: typing.Optional[typing.Union["ManifestFieldManager", typing.Dict[builtins.str, typing.Any]]] = None,
        object: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        timeouts: typing.Optional[typing.Union["ManifestTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        wait: typing.Optional[typing.Union["ManifestWait", typing.Dict[builtins.str, typing.Any]]] = None,
        wait_for: typing.Optional[typing.Union[typing.Union["ManifestWaitFor", typing.Dict[builtins.str, typing.Any]], _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param manifest: A Kubernetes manifest describing the desired state of the resource in HCL format. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#manifest Manifest#manifest}
        :param computed_fields: List of manifest fields whose values can be altered by the API server during 'apply'. Defaults to: ["metadata.annotations", "metadata.labels"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#computed_fields Manifest#computed_fields}
        :param field_manager: field_manager block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#field_manager Manifest#field_manager}
        :param object: The resulting resource state, as returned by the API server after applying the desired state from ``manifest``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#object Manifest#object}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#timeouts Manifest#timeouts}
        :param wait: wait block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#wait Manifest#wait}
        :param wait_for: A map of attribute paths and desired patterns to be matched. After each apply the provider will wait for all attributes listed here to reach a value that matches the desired pattern. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#wait_for Manifest#wait_for}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(field_manager, dict):
            field_manager = ManifestFieldManager(**field_manager)
        if isinstance(timeouts, dict):
            timeouts = ManifestTimeouts(**timeouts)
        if isinstance(wait, dict):
            wait = ManifestWait(**wait)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1eaa12c2faba964d788e7fd6bde32021edcf7026eca884e7df5ab3265f91d028)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument manifest", value=manifest, expected_type=type_hints["manifest"])
            check_type(argname="argument computed_fields", value=computed_fields, expected_type=type_hints["computed_fields"])
            check_type(argname="argument field_manager", value=field_manager, expected_type=type_hints["field_manager"])
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument wait", value=wait, expected_type=type_hints["wait"])
            check_type(argname="argument wait_for", value=wait_for, expected_type=type_hints["wait_for"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "manifest": manifest,
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
        if computed_fields is not None:
            self._values["computed_fields"] = computed_fields
        if field_manager is not None:
            self._values["field_manager"] = field_manager
        if object is not None:
            self._values["object"] = object
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if wait is not None:
            self._values["wait"] = wait
        if wait_for is not None:
            self._values["wait_for"] = wait_for

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
    def manifest(self) -> typing.Mapping[builtins.str, typing.Any]:
        '''A Kubernetes manifest describing the desired state of the resource in HCL format.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#manifest Manifest#manifest}
        '''
        result = self._values.get("manifest")
        assert result is not None, "Required property 'manifest' is missing"
        return typing.cast(typing.Mapping[builtins.str, typing.Any], result)

    @builtins.property
    def computed_fields(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of manifest fields whose values can be altered by the API server during 'apply'. Defaults to: ["metadata.annotations", "metadata.labels"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#computed_fields Manifest#computed_fields}
        '''
        result = self._values.get("computed_fields")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def field_manager(self) -> typing.Optional["ManifestFieldManager"]:
        '''field_manager block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#field_manager Manifest#field_manager}
        '''
        result = self._values.get("field_manager")
        return typing.cast(typing.Optional["ManifestFieldManager"], result)

    @builtins.property
    def object(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''The resulting resource state, as returned by the API server after applying the desired state from ``manifest``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#object Manifest#object}
        '''
        result = self._values.get("object")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ManifestTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#timeouts Manifest#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ManifestTimeouts"], result)

    @builtins.property
    def wait(self) -> typing.Optional["ManifestWait"]:
        '''wait block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#wait Manifest#wait}
        '''
        result = self._values.get("wait")
        return typing.cast(typing.Optional["ManifestWait"], result)

    @builtins.property
    def wait_for(
        self,
    ) -> typing.Optional[typing.Union["ManifestWaitFor", _cdktf_9a9027ec.IResolvable]]:
        '''A map of attribute paths and desired patterns to be matched.

        After each apply the provider will wait for all attributes listed here to reach a value that matches the desired pattern.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#wait_for Manifest#wait_for}
        '''
        result = self._values.get("wait_for")
        return typing.cast(typing.Optional[typing.Union["ManifestWaitFor", _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManifestConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.manifest.ManifestFieldManager",
    jsii_struct_bases=[],
    name_mapping={"force_conflicts": "forceConflicts", "name": "name"},
)
class ManifestFieldManager:
    def __init__(
        self,
        *,
        force_conflicts: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param force_conflicts: Force changes against conflicts. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#force_conflicts Manifest#force_conflicts}
        :param name: The name to use for the field manager when creating and updating the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#name Manifest#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b51101c0c4086249ee8b0d9ed522acf85b96ba4edb99262ee426c79e8116a50)
            check_type(argname="argument force_conflicts", value=force_conflicts, expected_type=type_hints["force_conflicts"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if force_conflicts is not None:
            self._values["force_conflicts"] = force_conflicts
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def force_conflicts(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Force changes against conflicts.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#force_conflicts Manifest#force_conflicts}
        '''
        result = self._values.get("force_conflicts")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name to use for the field manager when creating and updating the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#name Manifest#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManifestFieldManager(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ManifestFieldManagerOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.manifest.ManifestFieldManagerOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__080764f7fd31d2888188d09ba9e9f0105f5aeb6a8df4e76817f0a3f2aaec5024)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetForceConflicts")
    def reset_force_conflicts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForceConflicts", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="forceConflictsInput")
    def force_conflicts_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "forceConflictsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="forceConflicts")
    def force_conflicts(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "forceConflicts"))

    @force_conflicts.setter
    def force_conflicts(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf8d2655fa84d140a58c9e93b3392a68fc9a19ae03e32e78bd8b09676753e962)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forceConflicts", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f15240ab6823872ed53bfef50673ee51d16ff7f6ad55a3203bc04b8f900e50f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ManifestFieldManager]:
        return typing.cast(typing.Optional[ManifestFieldManager], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ManifestFieldManager]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43571777259559f90d26c869b85cbdcca475ea462b45d9596eb929fdc2a0e7b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.manifest.ManifestTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class ManifestTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Timeout for the create operation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#create Manifest#create}
        :param delete: Timeout for the delete operation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#delete Manifest#delete}
        :param update: Timeout for the update operation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#update Manifest#update}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e77c9b5ee29330394c04963891c9423bc44af9daa68c470c31874ba497456108)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Timeout for the create operation.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#create Manifest#create}
        '''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Timeout for the delete operation.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#delete Manifest#delete}
        '''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Timeout for the update operation.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#update Manifest#update}
        '''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManifestTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ManifestTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.manifest.ManifestTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8647cd1c429c68e81265623ea6279b047f93a6aee527f78ee78e02a3dc07ea11)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a8121a2db87c6d679e27aee9fb0f5f594892203764a5c976e2783642b65a94a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91ec79b61155565ab3babcef3551e37bdf993c705cf43999c7142e9483c41d31)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2979d11e49e7fbaed6a63ba38d279a892470facbb7a52684b7cc107dc840804)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ManifestTimeouts]:
        return typing.cast(typing.Optional[ManifestTimeouts], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ManifestTimeouts]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__add94757281d51fa0a9992cc65fc441bd1bdb5d7716b7f078e8a663729c2982c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.manifest.ManifestWait",
    jsii_struct_bases=[],
    name_mapping={"condition": "condition", "fields": "fields", "rollout": "rollout"},
)
class ManifestWait:
    def __init__(
        self,
        *,
        condition: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ManifestWaitCondition", typing.Dict[builtins.str, typing.Any]]]]] = None,
        fields: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        rollout: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param condition: condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#condition Manifest#condition}
        :param fields: A map of paths to fields to wait for a specific field value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#fields Manifest#fields}
        :param rollout: Wait for rollout to complete on resources that support ``kubectl rollout status``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#rollout Manifest#rollout}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__766f10703ce54c720b31cb8ab5e37125d9474578d1962e7d57475b4f0270ecff)
            check_type(argname="argument condition", value=condition, expected_type=type_hints["condition"])
            check_type(argname="argument fields", value=fields, expected_type=type_hints["fields"])
            check_type(argname="argument rollout", value=rollout, expected_type=type_hints["rollout"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if condition is not None:
            self._values["condition"] = condition
        if fields is not None:
            self._values["fields"] = fields
        if rollout is not None:
            self._values["rollout"] = rollout

    @builtins.property
    def condition(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ManifestWaitCondition"]]]:
        '''condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#condition Manifest#condition}
        '''
        result = self._values.get("condition")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ManifestWaitCondition"]]], result)

    @builtins.property
    def fields(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of paths to fields to wait for a specific field value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#fields Manifest#fields}
        '''
        result = self._values.get("fields")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def rollout(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Wait for rollout to complete on resources that support ``kubectl rollout status``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#rollout Manifest#rollout}
        '''
        result = self._values.get("rollout")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManifestWait(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.manifest.ManifestWaitCondition",
    jsii_struct_bases=[],
    name_mapping={"status": "status", "type": "type"},
)
class ManifestWaitCondition:
    def __init__(
        self,
        *,
        status: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param status: The condition status. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#status Manifest#status}
        :param type: The type of condition. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#type Manifest#type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b2f58431a48f9a122b0d03ce0f1410e47ca01535557f60ecc22d26c15725d65)
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if status is not None:
            self._values["status"] = status
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''The condition status.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#status Manifest#status}
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The type of condition.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#type Manifest#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManifestWaitCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ManifestWaitConditionList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.manifest.ManifestWaitConditionList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__534ebfe3a298af0c1018464feb813ea595d19d41611f3c78da25c3fbb93ef8f2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ManifestWaitConditionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7edd82800b7ffd86163ceb8718d012d39f89dbbc9c9abba02e26ea184560526a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ManifestWaitConditionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__596af8eeca598df1c4d0a097143b9e693f2c3b56eb9df51118172805fabf1eb3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__015d871e95dbafd0fe372c1e09cc3bb2459a752f4f65aca121f6ef210c8b1d05)
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
            type_hints = typing.get_type_hints(_typecheckingstub__03af4030d71881549721594b0dc7cf186ca652e725e1b90ad3eaafe8dc4fb42d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ManifestWaitCondition]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ManifestWaitCondition]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ManifestWaitCondition]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75bdc557d1ef5052bf5f274391d385729ff4e5e1007eadfed0a89fc53979163f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ManifestWaitConditionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.manifest.ManifestWaitConditionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4597f56932fdb7fefd9133fe4fdfba98181055191c876920b3a8928d5db1cdf0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetStatus")
    def reset_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatus", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b3fc8c0b060735b6d4bfb12b495efa209ae6ed9f02a27dc10952825fe4bc2e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12d3a802dcfe5ddd85191e395a7ade207afa8ec0d1f0b446252c0eb6b5de2f34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ManifestWaitCondition, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ManifestWaitCondition, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ManifestWaitCondition, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5462034aad739d8465202702288f44d5104bd167a7cf5663c8c1fc8fabbf9e34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.manifest.ManifestWaitFor",
    jsii_struct_bases=[],
    name_mapping={"fields": "fields"},
)
class ManifestWaitFor:
    def __init__(
        self,
        *,
        fields: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param fields: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#fields Manifest#fields}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__722d88211458308e991b51f5ee534e76e21aa5b33e32d16ad8df1ae6f379e4a9)
            check_type(argname="argument fields", value=fields, expected_type=type_hints["fields"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if fields is not None:
            self._values["fields"] = fields

    @builtins.property
    def fields(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/manifest#fields Manifest#fields}.'''
        result = self._values.get("fields")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManifestWaitFor(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ManifestWaitForOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.manifest.ManifestWaitForOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d127bac51e358e8e24a1c0a823cf0e5fd0b95a4fc8b4efad9a5d6158fb82e219)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFields")
    def reset_fields(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFields", []))

    @builtins.property
    @jsii.member(jsii_name="fieldsInput")
    def fields_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "fieldsInput"))

    @builtins.property
    @jsii.member(jsii_name="fields")
    def fields(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "fields"))

    @fields.setter
    def fields(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__731eb3b1e1b193d98f0ce0374ba04bd66f281a173781e1bd2ee15dfa3107fb26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fields", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ManifestWaitFor, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ManifestWaitFor, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ManifestWaitFor, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6bff4a66084a9b37a955142d875401796ca9ed098bb551d8a995018eb41612d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ManifestWaitOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.manifest.ManifestWaitOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b2fa473f9f17819df2fe5db42da95bb0ac7269717909f92a1f039973425693cf)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCondition")
    def put_condition(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ManifestWaitCondition, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e69e9fef66c0d14ff57faea33f69f71b0fc05fbe8cebdee9224da40a533eb53)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCondition", [value]))

    @jsii.member(jsii_name="resetCondition")
    def reset_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCondition", []))

    @jsii.member(jsii_name="resetFields")
    def reset_fields(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFields", []))

    @jsii.member(jsii_name="resetRollout")
    def reset_rollout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRollout", []))

    @builtins.property
    @jsii.member(jsii_name="condition")
    def condition(self) -> ManifestWaitConditionList:
        return typing.cast(ManifestWaitConditionList, jsii.get(self, "condition"))

    @builtins.property
    @jsii.member(jsii_name="conditionInput")
    def condition_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ManifestWaitCondition]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ManifestWaitCondition]]], jsii.get(self, "conditionInput"))

    @builtins.property
    @jsii.member(jsii_name="fieldsInput")
    def fields_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "fieldsInput"))

    @builtins.property
    @jsii.member(jsii_name="rolloutInput")
    def rollout_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "rolloutInput"))

    @builtins.property
    @jsii.member(jsii_name="fields")
    def fields(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "fields"))

    @fields.setter
    def fields(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7a32303b4d9eb4eea4e4474a1fc9506e7a234413ecab75a457c7b36abebd3d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fields", value)

    @builtins.property
    @jsii.member(jsii_name="rollout")
    def rollout(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "rollout"))

    @rollout.setter
    def rollout(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ea750e84c6cefdab4dcc414da11f7193c89f9a19f8249bcc64836b6bcffbd3e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rollout", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ManifestWait]:
        return typing.cast(typing.Optional[ManifestWait], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ManifestWait]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13abd69b1afb2f64dca94956a1cdebf919570c6abb79b61242b18b9dc8f0462c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Manifest",
    "ManifestConfig",
    "ManifestFieldManager",
    "ManifestFieldManagerOutputReference",
    "ManifestTimeouts",
    "ManifestTimeoutsOutputReference",
    "ManifestWait",
    "ManifestWaitCondition",
    "ManifestWaitConditionList",
    "ManifestWaitConditionOutputReference",
    "ManifestWaitFor",
    "ManifestWaitForOutputReference",
    "ManifestWaitOutputReference",
]

publication.publish()

def _typecheckingstub__40157812e663140f6fdd42d0af8ecf268c076e19d6df6503a28a7348726cd2ce(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    manifest: typing.Mapping[builtins.str, typing.Any],
    computed_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
    field_manager: typing.Optional[typing.Union[ManifestFieldManager, typing.Dict[builtins.str, typing.Any]]] = None,
    object: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    timeouts: typing.Optional[typing.Union[ManifestTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    wait: typing.Optional[typing.Union[ManifestWait, typing.Dict[builtins.str, typing.Any]]] = None,
    wait_for: typing.Optional[typing.Union[typing.Union[ManifestWaitFor, typing.Dict[builtins.str, typing.Any]], _cdktf_9a9027ec.IResolvable]] = None,
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

def _typecheckingstub__14857a5c9737e7cd61739c774f785080774105cfd53ab505a56c1b8e959c300f(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3322d2fa8e410d3561c35a35ad226bec78748b3b040e4187809c4a66d8c1147e(
    value: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83d28b4d34e4cef4a85cb7ed7cb3017a479bab272528e65f013b62ecbb9dabb5(
    value: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd9cd52f7ae8f8b0465ad8da3ea17fb391b864ac4cb2e0cef7edc4aebc2874c4(
    value: typing.Union[ManifestWaitFor, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1eaa12c2faba964d788e7fd6bde32021edcf7026eca884e7df5ab3265f91d028(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    manifest: typing.Mapping[builtins.str, typing.Any],
    computed_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
    field_manager: typing.Optional[typing.Union[ManifestFieldManager, typing.Dict[builtins.str, typing.Any]]] = None,
    object: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    timeouts: typing.Optional[typing.Union[ManifestTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    wait: typing.Optional[typing.Union[ManifestWait, typing.Dict[builtins.str, typing.Any]]] = None,
    wait_for: typing.Optional[typing.Union[typing.Union[ManifestWaitFor, typing.Dict[builtins.str, typing.Any]], _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b51101c0c4086249ee8b0d9ed522acf85b96ba4edb99262ee426c79e8116a50(
    *,
    force_conflicts: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__080764f7fd31d2888188d09ba9e9f0105f5aeb6a8df4e76817f0a3f2aaec5024(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf8d2655fa84d140a58c9e93b3392a68fc9a19ae03e32e78bd8b09676753e962(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f15240ab6823872ed53bfef50673ee51d16ff7f6ad55a3203bc04b8f900e50f5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43571777259559f90d26c869b85cbdcca475ea462b45d9596eb929fdc2a0e7b6(
    value: typing.Optional[ManifestFieldManager],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e77c9b5ee29330394c04963891c9423bc44af9daa68c470c31874ba497456108(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8647cd1c429c68e81265623ea6279b047f93a6aee527f78ee78e02a3dc07ea11(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a8121a2db87c6d679e27aee9fb0f5f594892203764a5c976e2783642b65a94a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91ec79b61155565ab3babcef3551e37bdf993c705cf43999c7142e9483c41d31(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2979d11e49e7fbaed6a63ba38d279a892470facbb7a52684b7cc107dc840804(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__add94757281d51fa0a9992cc65fc441bd1bdb5d7716b7f078e8a663729c2982c(
    value: typing.Optional[ManifestTimeouts],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__766f10703ce54c720b31cb8ab5e37125d9474578d1962e7d57475b4f0270ecff(
    *,
    condition: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ManifestWaitCondition, typing.Dict[builtins.str, typing.Any]]]]] = None,
    fields: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    rollout: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b2f58431a48f9a122b0d03ce0f1410e47ca01535557f60ecc22d26c15725d65(
    *,
    status: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__534ebfe3a298af0c1018464feb813ea595d19d41611f3c78da25c3fbb93ef8f2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7edd82800b7ffd86163ceb8718d012d39f89dbbc9c9abba02e26ea184560526a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__596af8eeca598df1c4d0a097143b9e693f2c3b56eb9df51118172805fabf1eb3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__015d871e95dbafd0fe372c1e09cc3bb2459a752f4f65aca121f6ef210c8b1d05(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03af4030d71881549721594b0dc7cf186ca652e725e1b90ad3eaafe8dc4fb42d(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75bdc557d1ef5052bf5f274391d385729ff4e5e1007eadfed0a89fc53979163f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ManifestWaitCondition]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4597f56932fdb7fefd9133fe4fdfba98181055191c876920b3a8928d5db1cdf0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b3fc8c0b060735b6d4bfb12b495efa209ae6ed9f02a27dc10952825fe4bc2e0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12d3a802dcfe5ddd85191e395a7ade207afa8ec0d1f0b446252c0eb6b5de2f34(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5462034aad739d8465202702288f44d5104bd167a7cf5663c8c1fc8fabbf9e34(
    value: typing.Optional[typing.Union[ManifestWaitCondition, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__722d88211458308e991b51f5ee534e76e21aa5b33e32d16ad8df1ae6f379e4a9(
    *,
    fields: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d127bac51e358e8e24a1c0a823cf0e5fd0b95a4fc8b4efad9a5d6158fb82e219(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__731eb3b1e1b193d98f0ce0374ba04bd66f281a173781e1bd2ee15dfa3107fb26(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bff4a66084a9b37a955142d875401796ca9ed098bb551d8a995018eb41612d2(
    value: typing.Optional[typing.Union[ManifestWaitFor, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2fa473f9f17819df2fe5db42da95bb0ac7269717909f92a1f039973425693cf(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e69e9fef66c0d14ff57faea33f69f71b0fc05fbe8cebdee9224da40a533eb53(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ManifestWaitCondition, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7a32303b4d9eb4eea4e4474a1fc9506e7a234413ecab75a457c7b36abebd3d7(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ea750e84c6cefdab4dcc414da11f7193c89f9a19f8249bcc64836b6bcffbd3e(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13abd69b1afb2f64dca94956a1cdebf919570c6abb79b61242b18b9dc8f0462c(
    value: typing.Optional[ManifestWait],
) -> None:
    """Type checking stubs"""
    pass
