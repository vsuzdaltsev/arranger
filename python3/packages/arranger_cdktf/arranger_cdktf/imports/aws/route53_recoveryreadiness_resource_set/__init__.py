'''
# `aws_route53recoveryreadiness_resource_set`

Refer to the Terraform Registory for docs: [`aws_route53recoveryreadiness_resource_set`](https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set).
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


class Route53RecoveryreadinessResourceSet(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.route53RecoveryreadinessResourceSet.Route53RecoveryreadinessResourceSet",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set aws_route53recoveryreadiness_resource_set}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        resources: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["Route53RecoveryreadinessResourceSetResources", typing.Dict[builtins.str, typing.Any]]]],
        resource_set_name: builtins.str,
        resource_set_type: builtins.str,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["Route53RecoveryreadinessResourceSetTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set aws_route53recoveryreadiness_resource_set} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param resources: resources block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#resources Route53RecoveryreadinessResourceSet#resources}
        :param resource_set_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#resource_set_name Route53RecoveryreadinessResourceSet#resource_set_name}.
        :param resource_set_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#resource_set_type Route53RecoveryreadinessResourceSet#resource_set_type}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#id Route53RecoveryreadinessResourceSet#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#tags Route53RecoveryreadinessResourceSet#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#tags_all Route53RecoveryreadinessResourceSet#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#timeouts Route53RecoveryreadinessResourceSet#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03c67db289b03576b6239876520d4aef6201d2f699f659c44b2b154f7f12d744)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = Route53RecoveryreadinessResourceSetConfig(
            resources=resources,
            resource_set_name=resource_set_name,
            resource_set_type=resource_set_type,
            id=id,
            tags=tags,
            tags_all=tags_all,
            timeouts=timeouts,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putResources")
    def put_resources(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["Route53RecoveryreadinessResourceSetResources", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8669d72d034c45defcd42b045d496d8424363061887265efa9e1331a896b57dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putResources", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(self, *, delete: typing.Optional[builtins.str] = None) -> None:
        '''
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#delete Route53RecoveryreadinessResourceSet#delete}.
        '''
        value = Route53RecoveryreadinessResourceSetTimeouts(delete=delete)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

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
    @jsii.member(jsii_name="resources")
    def resources(self) -> "Route53RecoveryreadinessResourceSetResourcesList":
        return typing.cast("Route53RecoveryreadinessResourceSetResourcesList", jsii.get(self, "resources"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "Route53RecoveryreadinessResourceSetTimeoutsOutputReference":
        return typing.cast("Route53RecoveryreadinessResourceSetTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceSetNameInput")
    def resource_set_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceSetNameInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceSetTypeInput")
    def resource_set_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceSetTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="resourcesInput")
    def resources_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Route53RecoveryreadinessResourceSetResources"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Route53RecoveryreadinessResourceSetResources"]]], jsii.get(self, "resourcesInput"))

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
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["Route53RecoveryreadinessResourceSetTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["Route53RecoveryreadinessResourceSetTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7eaaedb90fae2c23f7736e6b3f4cd4434b24a52f8615ebcb701aad6723d695e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="resourceSetName")
    def resource_set_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceSetName"))

    @resource_set_name.setter
    def resource_set_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38ab61dff6d4f23c397b5cde2e54952051c6ea44adda8cb7182ae4d76052f12b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceSetName", value)

    @builtins.property
    @jsii.member(jsii_name="resourceSetType")
    def resource_set_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceSetType"))

    @resource_set_type.setter
    def resource_set_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f767289a3e40728823c763777ea84e3a2077cd46556962ee7f1da68e776eeaf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceSetType", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a7607029fa2b7538299a205f908a5568c765e3a569591564c633d89d3a97e43)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac7e6c14ad3fba2e59e0c8045591bd1239e803a2d8b679e8427b1a6b823cd324)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.route53RecoveryreadinessResourceSet.Route53RecoveryreadinessResourceSetConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "resources": "resources",
        "resource_set_name": "resourceSetName",
        "resource_set_type": "resourceSetType",
        "id": "id",
        "tags": "tags",
        "tags_all": "tagsAll",
        "timeouts": "timeouts",
    },
)
class Route53RecoveryreadinessResourceSetConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        resources: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["Route53RecoveryreadinessResourceSetResources", typing.Dict[builtins.str, typing.Any]]]],
        resource_set_name: builtins.str,
        resource_set_type: builtins.str,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["Route53RecoveryreadinessResourceSetTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param resources: resources block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#resources Route53RecoveryreadinessResourceSet#resources}
        :param resource_set_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#resource_set_name Route53RecoveryreadinessResourceSet#resource_set_name}.
        :param resource_set_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#resource_set_type Route53RecoveryreadinessResourceSet#resource_set_type}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#id Route53RecoveryreadinessResourceSet#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#tags Route53RecoveryreadinessResourceSet#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#tags_all Route53RecoveryreadinessResourceSet#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#timeouts Route53RecoveryreadinessResourceSet#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = Route53RecoveryreadinessResourceSetTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__244786ee753968301a1a0b6ee2f59adbc5f9861d724766577bd7bed65dd9276b)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
            check_type(argname="argument resource_set_name", value=resource_set_name, expected_type=type_hints["resource_set_name"])
            check_type(argname="argument resource_set_type", value=resource_set_type, expected_type=type_hints["resource_set_type"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resources": resources,
            "resource_set_name": resource_set_name,
            "resource_set_type": resource_set_type,
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
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if timeouts is not None:
            self._values["timeouts"] = timeouts

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
    def resources(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Route53RecoveryreadinessResourceSetResources"]]:
        '''resources block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#resources Route53RecoveryreadinessResourceSet#resources}
        '''
        result = self._values.get("resources")
        assert result is not None, "Required property 'resources' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Route53RecoveryreadinessResourceSetResources"]], result)

    @builtins.property
    def resource_set_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#resource_set_name Route53RecoveryreadinessResourceSet#resource_set_name}.'''
        result = self._values.get("resource_set_name")
        assert result is not None, "Required property 'resource_set_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_set_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#resource_set_type Route53RecoveryreadinessResourceSet#resource_set_type}.'''
        result = self._values.get("resource_set_type")
        assert result is not None, "Required property 'resource_set_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#id Route53RecoveryreadinessResourceSet#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#tags Route53RecoveryreadinessResourceSet#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#tags_all Route53RecoveryreadinessResourceSet#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(
        self,
    ) -> typing.Optional["Route53RecoveryreadinessResourceSetTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#timeouts Route53RecoveryreadinessResourceSet#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["Route53RecoveryreadinessResourceSetTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Route53RecoveryreadinessResourceSetConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.route53RecoveryreadinessResourceSet.Route53RecoveryreadinessResourceSetResources",
    jsii_struct_bases=[],
    name_mapping={
        "dns_target_resource": "dnsTargetResource",
        "readiness_scopes": "readinessScopes",
        "resource_arn": "resourceArn",
    },
)
class Route53RecoveryreadinessResourceSetResources:
    def __init__(
        self,
        *,
        dns_target_resource: typing.Optional[typing.Union["Route53RecoveryreadinessResourceSetResourcesDnsTargetResource", typing.Dict[builtins.str, typing.Any]]] = None,
        readiness_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
        resource_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param dns_target_resource: dns_target_resource block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#dns_target_resource Route53RecoveryreadinessResourceSet#dns_target_resource}
        :param readiness_scopes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#readiness_scopes Route53RecoveryreadinessResourceSet#readiness_scopes}.
        :param resource_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#resource_arn Route53RecoveryreadinessResourceSet#resource_arn}.
        '''
        if isinstance(dns_target_resource, dict):
            dns_target_resource = Route53RecoveryreadinessResourceSetResourcesDnsTargetResource(**dns_target_resource)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84989b814394695be4878fd80590cba2dc1343065c059ee120fe52386f62ed6d)
            check_type(argname="argument dns_target_resource", value=dns_target_resource, expected_type=type_hints["dns_target_resource"])
            check_type(argname="argument readiness_scopes", value=readiness_scopes, expected_type=type_hints["readiness_scopes"])
            check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dns_target_resource is not None:
            self._values["dns_target_resource"] = dns_target_resource
        if readiness_scopes is not None:
            self._values["readiness_scopes"] = readiness_scopes
        if resource_arn is not None:
            self._values["resource_arn"] = resource_arn

    @builtins.property
    def dns_target_resource(
        self,
    ) -> typing.Optional["Route53RecoveryreadinessResourceSetResourcesDnsTargetResource"]:
        '''dns_target_resource block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#dns_target_resource Route53RecoveryreadinessResourceSet#dns_target_resource}
        '''
        result = self._values.get("dns_target_resource")
        return typing.cast(typing.Optional["Route53RecoveryreadinessResourceSetResourcesDnsTargetResource"], result)

    @builtins.property
    def readiness_scopes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#readiness_scopes Route53RecoveryreadinessResourceSet#readiness_scopes}.'''
        result = self._values.get("readiness_scopes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def resource_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#resource_arn Route53RecoveryreadinessResourceSet#resource_arn}.'''
        result = self._values.get("resource_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Route53RecoveryreadinessResourceSetResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.route53RecoveryreadinessResourceSet.Route53RecoveryreadinessResourceSetResourcesDnsTargetResource",
    jsii_struct_bases=[],
    name_mapping={
        "domain_name": "domainName",
        "hosted_zone_arn": "hostedZoneArn",
        "record_set_id": "recordSetId",
        "record_type": "recordType",
        "target_resource": "targetResource",
    },
)
class Route53RecoveryreadinessResourceSetResourcesDnsTargetResource:
    def __init__(
        self,
        *,
        domain_name: builtins.str,
        hosted_zone_arn: typing.Optional[builtins.str] = None,
        record_set_id: typing.Optional[builtins.str] = None,
        record_type: typing.Optional[builtins.str] = None,
        target_resource: typing.Optional[typing.Union["Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResource", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#domain_name Route53RecoveryreadinessResourceSet#domain_name}.
        :param hosted_zone_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#hosted_zone_arn Route53RecoveryreadinessResourceSet#hosted_zone_arn}.
        :param record_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#record_set_id Route53RecoveryreadinessResourceSet#record_set_id}.
        :param record_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#record_type Route53RecoveryreadinessResourceSet#record_type}.
        :param target_resource: target_resource block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#target_resource Route53RecoveryreadinessResourceSet#target_resource}
        '''
        if isinstance(target_resource, dict):
            target_resource = Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResource(**target_resource)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__627faf76f6e77afcb8bd0f3f11ec71faf981010317cd8496e9a830a8253aee4c)
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument hosted_zone_arn", value=hosted_zone_arn, expected_type=type_hints["hosted_zone_arn"])
            check_type(argname="argument record_set_id", value=record_set_id, expected_type=type_hints["record_set_id"])
            check_type(argname="argument record_type", value=record_type, expected_type=type_hints["record_type"])
            check_type(argname="argument target_resource", value=target_resource, expected_type=type_hints["target_resource"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_name": domain_name,
        }
        if hosted_zone_arn is not None:
            self._values["hosted_zone_arn"] = hosted_zone_arn
        if record_set_id is not None:
            self._values["record_set_id"] = record_set_id
        if record_type is not None:
            self._values["record_type"] = record_type
        if target_resource is not None:
            self._values["target_resource"] = target_resource

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#domain_name Route53RecoveryreadinessResourceSet#domain_name}.'''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def hosted_zone_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#hosted_zone_arn Route53RecoveryreadinessResourceSet#hosted_zone_arn}.'''
        result = self._values.get("hosted_zone_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def record_set_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#record_set_id Route53RecoveryreadinessResourceSet#record_set_id}.'''
        result = self._values.get("record_set_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def record_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#record_type Route53RecoveryreadinessResourceSet#record_type}.'''
        result = self._values.get("record_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_resource(
        self,
    ) -> typing.Optional["Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResource"]:
        '''target_resource block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#target_resource Route53RecoveryreadinessResourceSet#target_resource}
        '''
        result = self._values.get("target_resource")
        return typing.cast(typing.Optional["Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResource"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Route53RecoveryreadinessResourceSetResourcesDnsTargetResource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.route53RecoveryreadinessResourceSet.Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0207e67fe5f53ad21f13a13ca2266cfcf80f7f13e4ef618cdeeafd304e2d85e6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putTargetResource")
    def put_target_resource(
        self,
        *,
        nlb_resource: typing.Optional[typing.Union["Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResourceNlbResource", typing.Dict[builtins.str, typing.Any]]] = None,
        r53_resource: typing.Optional[typing.Union["Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResourceR53Resource", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param nlb_resource: nlb_resource block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#nlb_resource Route53RecoveryreadinessResourceSet#nlb_resource}
        :param r53_resource: r53_resource block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#r53_resource Route53RecoveryreadinessResourceSet#r53_resource}
        '''
        value = Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResource(
            nlb_resource=nlb_resource, r53_resource=r53_resource
        )

        return typing.cast(None, jsii.invoke(self, "putTargetResource", [value]))

    @jsii.member(jsii_name="resetHostedZoneArn")
    def reset_hosted_zone_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostedZoneArn", []))

    @jsii.member(jsii_name="resetRecordSetId")
    def reset_record_set_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecordSetId", []))

    @jsii.member(jsii_name="resetRecordType")
    def reset_record_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecordType", []))

    @jsii.member(jsii_name="resetTargetResource")
    def reset_target_resource(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetResource", []))

    @builtins.property
    @jsii.member(jsii_name="targetResource")
    def target_resource(
        self,
    ) -> "Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResourceOutputReference":
        return typing.cast("Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResourceOutputReference", jsii.get(self, "targetResource"))

    @builtins.property
    @jsii.member(jsii_name="domainNameInput")
    def domain_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainNameInput"))

    @builtins.property
    @jsii.member(jsii_name="hostedZoneArnInput")
    def hosted_zone_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostedZoneArnInput"))

    @builtins.property
    @jsii.member(jsii_name="recordSetIdInput")
    def record_set_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recordSetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="recordTypeInput")
    def record_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recordTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="targetResourceInput")
    def target_resource_input(
        self,
    ) -> typing.Optional["Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResource"]:
        return typing.cast(typing.Optional["Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResource"], jsii.get(self, "targetResourceInput"))

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b7400fb01055db3b28b243254fc7a7ba3329b867f39b8eda21fe4f7053473e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value)

    @builtins.property
    @jsii.member(jsii_name="hostedZoneArn")
    def hosted_zone_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostedZoneArn"))

    @hosted_zone_arn.setter
    def hosted_zone_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb63e4d893c066f686bccd11f2c784d7aacb112059b50876f612de19186d19d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostedZoneArn", value)

    @builtins.property
    @jsii.member(jsii_name="recordSetId")
    def record_set_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recordSetId"))

    @record_set_id.setter
    def record_set_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e15409e55c4469d5470a1e878d697a39ba77f2101879dc938f30af3f02317ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordSetId", value)

    @builtins.property
    @jsii.member(jsii_name="recordType")
    def record_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recordType"))

    @record_type.setter
    def record_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0b1677e27ecefc61267e78dd7601ab75ab5c631d69220a53642a49d1ce9e733)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Route53RecoveryreadinessResourceSetResourcesDnsTargetResource]:
        return typing.cast(typing.Optional[Route53RecoveryreadinessResourceSetResourcesDnsTargetResource], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Route53RecoveryreadinessResourceSetResourcesDnsTargetResource],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e03bc149936ae8e3f6cf855a2416fee1294024448051824d821832b1da1965ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.route53RecoveryreadinessResourceSet.Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResource",
    jsii_struct_bases=[],
    name_mapping={"nlb_resource": "nlbResource", "r53_resource": "r53Resource"},
)
class Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResource:
    def __init__(
        self,
        *,
        nlb_resource: typing.Optional[typing.Union["Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResourceNlbResource", typing.Dict[builtins.str, typing.Any]]] = None,
        r53_resource: typing.Optional[typing.Union["Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResourceR53Resource", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param nlb_resource: nlb_resource block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#nlb_resource Route53RecoveryreadinessResourceSet#nlb_resource}
        :param r53_resource: r53_resource block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#r53_resource Route53RecoveryreadinessResourceSet#r53_resource}
        '''
        if isinstance(nlb_resource, dict):
            nlb_resource = Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResourceNlbResource(**nlb_resource)
        if isinstance(r53_resource, dict):
            r53_resource = Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResourceR53Resource(**r53_resource)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75a2f5585abfc65caf7b22a8d5aa21f0c2d79355bcd61b120d6078079278617b)
            check_type(argname="argument nlb_resource", value=nlb_resource, expected_type=type_hints["nlb_resource"])
            check_type(argname="argument r53_resource", value=r53_resource, expected_type=type_hints["r53_resource"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if nlb_resource is not None:
            self._values["nlb_resource"] = nlb_resource
        if r53_resource is not None:
            self._values["r53_resource"] = r53_resource

    @builtins.property
    def nlb_resource(
        self,
    ) -> typing.Optional["Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResourceNlbResource"]:
        '''nlb_resource block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#nlb_resource Route53RecoveryreadinessResourceSet#nlb_resource}
        '''
        result = self._values.get("nlb_resource")
        return typing.cast(typing.Optional["Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResourceNlbResource"], result)

    @builtins.property
    def r53_resource(
        self,
    ) -> typing.Optional["Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResourceR53Resource"]:
        '''r53_resource block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#r53_resource Route53RecoveryreadinessResourceSet#r53_resource}
        '''
        result = self._values.get("r53_resource")
        return typing.cast(typing.Optional["Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResourceR53Resource"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.route53RecoveryreadinessResourceSet.Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResourceNlbResource",
    jsii_struct_bases=[],
    name_mapping={"arn": "arn"},
)
class Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResourceNlbResource:
    def __init__(self, *, arn: typing.Optional[builtins.str] = None) -> None:
        '''
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#arn Route53RecoveryreadinessResourceSet#arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc9085938add7074327398ce13aa76399b70df495278d6969c87ca16c2a3ff42)
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#arn Route53RecoveryreadinessResourceSet#arn}.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResourceNlbResource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResourceNlbResourceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.route53RecoveryreadinessResourceSet.Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResourceNlbResourceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__105eb43776910ca8b87f5d77b6943b4acfcfe943eb01e659b020aac23571ee95)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetArn")
    def reset_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArn", []))

    @builtins.property
    @jsii.member(jsii_name="arnInput")
    def arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "arnInput"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @arn.setter
    def arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fca1b2cf309ec15e0da138550d9b03c2876242def6a6b49128d721322fd164f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "arn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResourceNlbResource]:
        return typing.cast(typing.Optional[Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResourceNlbResource], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResourceNlbResource],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e64f05fd0384746e363813df448babe038156645cf7847da144e318d6cc51b7c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResourceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.route53RecoveryreadinessResourceSet.Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResourceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__54f0da7d04468d1c00b21ad672ae01c7dee13133bb6938d75f64fd789d1bbb62)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putNlbResource")
    def put_nlb_resource(self, *, arn: typing.Optional[builtins.str] = None) -> None:
        '''
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#arn Route53RecoveryreadinessResourceSet#arn}.
        '''
        value = Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResourceNlbResource(
            arn=arn
        )

        return typing.cast(None, jsii.invoke(self, "putNlbResource", [value]))

    @jsii.member(jsii_name="putR53Resource")
    def put_r53_resource(
        self,
        *,
        domain_name: typing.Optional[builtins.str] = None,
        record_set_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#domain_name Route53RecoveryreadinessResourceSet#domain_name}.
        :param record_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#record_set_id Route53RecoveryreadinessResourceSet#record_set_id}.
        '''
        value = Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResourceR53Resource(
            domain_name=domain_name, record_set_id=record_set_id
        )

        return typing.cast(None, jsii.invoke(self, "putR53Resource", [value]))

    @jsii.member(jsii_name="resetNlbResource")
    def reset_nlb_resource(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNlbResource", []))

    @jsii.member(jsii_name="resetR53Resource")
    def reset_r53_resource(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetR53Resource", []))

    @builtins.property
    @jsii.member(jsii_name="nlbResource")
    def nlb_resource(
        self,
    ) -> Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResourceNlbResourceOutputReference:
        return typing.cast(Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResourceNlbResourceOutputReference, jsii.get(self, "nlbResource"))

    @builtins.property
    @jsii.member(jsii_name="r53Resource")
    def r53_resource(
        self,
    ) -> "Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResourceR53ResourceOutputReference":
        return typing.cast("Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResourceR53ResourceOutputReference", jsii.get(self, "r53Resource"))

    @builtins.property
    @jsii.member(jsii_name="nlbResourceInput")
    def nlb_resource_input(
        self,
    ) -> typing.Optional[Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResourceNlbResource]:
        return typing.cast(typing.Optional[Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResourceNlbResource], jsii.get(self, "nlbResourceInput"))

    @builtins.property
    @jsii.member(jsii_name="r53ResourceInput")
    def r53_resource_input(
        self,
    ) -> typing.Optional["Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResourceR53Resource"]:
        return typing.cast(typing.Optional["Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResourceR53Resource"], jsii.get(self, "r53ResourceInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResource]:
        return typing.cast(typing.Optional[Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResource], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResource],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ba90dd3cc014e198a2f4e47d7fa165c3c93ec3eeef359af2c82b9be7187dd30)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.route53RecoveryreadinessResourceSet.Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResourceR53Resource",
    jsii_struct_bases=[],
    name_mapping={"domain_name": "domainName", "record_set_id": "recordSetId"},
)
class Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResourceR53Resource:
    def __init__(
        self,
        *,
        domain_name: typing.Optional[builtins.str] = None,
        record_set_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#domain_name Route53RecoveryreadinessResourceSet#domain_name}.
        :param record_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#record_set_id Route53RecoveryreadinessResourceSet#record_set_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__708669cc433c7d23ffd910b96ee768a71c1eb821ad4bbdb4b7596af23067244c)
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument record_set_id", value=record_set_id, expected_type=type_hints["record_set_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if domain_name is not None:
            self._values["domain_name"] = domain_name
        if record_set_id is not None:
            self._values["record_set_id"] = record_set_id

    @builtins.property
    def domain_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#domain_name Route53RecoveryreadinessResourceSet#domain_name}.'''
        result = self._values.get("domain_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def record_set_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#record_set_id Route53RecoveryreadinessResourceSet#record_set_id}.'''
        result = self._values.get("record_set_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResourceR53Resource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResourceR53ResourceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.route53RecoveryreadinessResourceSet.Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResourceR53ResourceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__716c502d1db7c6d6daff18959559f6e1a7c94e5f32b39cadd426505548ca5b50)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDomainName")
    def reset_domain_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDomainName", []))

    @jsii.member(jsii_name="resetRecordSetId")
    def reset_record_set_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecordSetId", []))

    @builtins.property
    @jsii.member(jsii_name="domainNameInput")
    def domain_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainNameInput"))

    @builtins.property
    @jsii.member(jsii_name="recordSetIdInput")
    def record_set_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recordSetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1f9d7c0eab4ac78fc0528a647df1ecf7992e5983dac78f0a545304f84de696f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value)

    @builtins.property
    @jsii.member(jsii_name="recordSetId")
    def record_set_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recordSetId"))

    @record_set_id.setter
    def record_set_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8804ec462800990be6ef9b2a08474548efaacda8a0b670d48545a2d6483aab2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordSetId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResourceR53Resource]:
        return typing.cast(typing.Optional[Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResourceR53Resource], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResourceR53Resource],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5caf7eeb9bf3a61d601037accbbe8a8878ec52db29e10f83153a3da77bd850d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Route53RecoveryreadinessResourceSetResourcesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.route53RecoveryreadinessResourceSet.Route53RecoveryreadinessResourceSetResourcesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8e03495320fb1d039c6a6acdd9f1aa9d9a89c4ba1275e64d3bfccb879d485767)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Route53RecoveryreadinessResourceSetResourcesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86eee78665139032211cd4833ca00dcd7fee95ae0863b38be8a734dccd02e77f)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Route53RecoveryreadinessResourceSetResourcesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5303cb3cb237c1b26ce5d5b3f240522ad68676bf94df077a8d8a232fea93d0b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__41104c307a3f3e8db2acfeb2e3a091f87590a4096fef930094fed57d5cd32c43)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c09935ab9adbcaa525f84e6dcb547e73595329c77476e9883260f5b78b8615c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Route53RecoveryreadinessResourceSetResources]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Route53RecoveryreadinessResourceSetResources]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Route53RecoveryreadinessResourceSetResources]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef0e1c7455d2d9441a7052dfdc476c882c4b1255860ab0b09f552bfb1959a10d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Route53RecoveryreadinessResourceSetResourcesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.route53RecoveryreadinessResourceSet.Route53RecoveryreadinessResourceSetResourcesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7731d3600a4fc98a104696fa2d715451165ad0fae75999c8473cf8cb11a2a04e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putDnsTargetResource")
    def put_dns_target_resource(
        self,
        *,
        domain_name: builtins.str,
        hosted_zone_arn: typing.Optional[builtins.str] = None,
        record_set_id: typing.Optional[builtins.str] = None,
        record_type: typing.Optional[builtins.str] = None,
        target_resource: typing.Optional[typing.Union[Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResource, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#domain_name Route53RecoveryreadinessResourceSet#domain_name}.
        :param hosted_zone_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#hosted_zone_arn Route53RecoveryreadinessResourceSet#hosted_zone_arn}.
        :param record_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#record_set_id Route53RecoveryreadinessResourceSet#record_set_id}.
        :param record_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#record_type Route53RecoveryreadinessResourceSet#record_type}.
        :param target_resource: target_resource block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#target_resource Route53RecoveryreadinessResourceSet#target_resource}
        '''
        value = Route53RecoveryreadinessResourceSetResourcesDnsTargetResource(
            domain_name=domain_name,
            hosted_zone_arn=hosted_zone_arn,
            record_set_id=record_set_id,
            record_type=record_type,
            target_resource=target_resource,
        )

        return typing.cast(None, jsii.invoke(self, "putDnsTargetResource", [value]))

    @jsii.member(jsii_name="resetDnsTargetResource")
    def reset_dns_target_resource(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDnsTargetResource", []))

    @jsii.member(jsii_name="resetReadinessScopes")
    def reset_readiness_scopes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadinessScopes", []))

    @jsii.member(jsii_name="resetResourceArn")
    def reset_resource_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceArn", []))

    @builtins.property
    @jsii.member(jsii_name="componentId")
    def component_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "componentId"))

    @builtins.property
    @jsii.member(jsii_name="dnsTargetResource")
    def dns_target_resource(
        self,
    ) -> Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceOutputReference:
        return typing.cast(Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceOutputReference, jsii.get(self, "dnsTargetResource"))

    @builtins.property
    @jsii.member(jsii_name="dnsTargetResourceInput")
    def dns_target_resource_input(
        self,
    ) -> typing.Optional[Route53RecoveryreadinessResourceSetResourcesDnsTargetResource]:
        return typing.cast(typing.Optional[Route53RecoveryreadinessResourceSetResourcesDnsTargetResource], jsii.get(self, "dnsTargetResourceInput"))

    @builtins.property
    @jsii.member(jsii_name="readinessScopesInput")
    def readiness_scopes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "readinessScopesInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceArnInput")
    def resource_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceArnInput"))

    @builtins.property
    @jsii.member(jsii_name="readinessScopes")
    def readiness_scopes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "readinessScopes"))

    @readiness_scopes.setter
    def readiness_scopes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b44f1fb156602b59d4cfe63d2fc12a9356bee9fdd93c1750a69692dad367f0ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readinessScopes", value)

    @builtins.property
    @jsii.member(jsii_name="resourceArn")
    def resource_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceArn"))

    @resource_arn.setter
    def resource_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d130f90be3dfc6c6ee97f2f28eb6c3670543be80ca2fe968e32215f23fb16ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[Route53RecoveryreadinessResourceSetResources, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Route53RecoveryreadinessResourceSetResources, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Route53RecoveryreadinessResourceSetResources, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__817878af3fee6ee8a7f309312968003b0544f0acd086763f4426779537acdba9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.route53RecoveryreadinessResourceSet.Route53RecoveryreadinessResourceSetTimeouts",
    jsii_struct_bases=[],
    name_mapping={"delete": "delete"},
)
class Route53RecoveryreadinessResourceSetTimeouts:
    def __init__(self, *, delete: typing.Optional[builtins.str] = None) -> None:
        '''
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#delete Route53RecoveryreadinessResourceSet#delete}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9ad46b0025cfebaefcadf7e87963a2a0518c9e0845de6194199b924204043ae)
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if delete is not None:
            self._values["delete"] = delete

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53recoveryreadiness_resource_set#delete Route53RecoveryreadinessResourceSet#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Route53RecoveryreadinessResourceSetTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Route53RecoveryreadinessResourceSetTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.route53RecoveryreadinessResourceSet.Route53RecoveryreadinessResourceSetTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0d76931278d4bdb28f8c3b67a6538bf4c8cb37e74316762c4736d66e6fe0706d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e30160945a01a4da517557cf1f0c27677a5421c790a5f4ab249f33c97746475d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[Route53RecoveryreadinessResourceSetTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Route53RecoveryreadinessResourceSetTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Route53RecoveryreadinessResourceSetTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6de6fb4a1dc31b85ea1b36055c09f29c2ea7143a2703378d2c4632dbba9dd3d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Route53RecoveryreadinessResourceSet",
    "Route53RecoveryreadinessResourceSetConfig",
    "Route53RecoveryreadinessResourceSetResources",
    "Route53RecoveryreadinessResourceSetResourcesDnsTargetResource",
    "Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceOutputReference",
    "Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResource",
    "Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResourceNlbResource",
    "Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResourceNlbResourceOutputReference",
    "Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResourceOutputReference",
    "Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResourceR53Resource",
    "Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResourceR53ResourceOutputReference",
    "Route53RecoveryreadinessResourceSetResourcesList",
    "Route53RecoveryreadinessResourceSetResourcesOutputReference",
    "Route53RecoveryreadinessResourceSetTimeouts",
    "Route53RecoveryreadinessResourceSetTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__03c67db289b03576b6239876520d4aef6201d2f699f659c44b2b154f7f12d744(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    resources: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Route53RecoveryreadinessResourceSetResources, typing.Dict[builtins.str, typing.Any]]]],
    resource_set_name: builtins.str,
    resource_set_type: builtins.str,
    id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[Route53RecoveryreadinessResourceSetTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__8669d72d034c45defcd42b045d496d8424363061887265efa9e1331a896b57dc(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Route53RecoveryreadinessResourceSetResources, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7eaaedb90fae2c23f7736e6b3f4cd4434b24a52f8615ebcb701aad6723d695e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38ab61dff6d4f23c397b5cde2e54952051c6ea44adda8cb7182ae4d76052f12b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f767289a3e40728823c763777ea84e3a2077cd46556962ee7f1da68e776eeaf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a7607029fa2b7538299a205f908a5568c765e3a569591564c633d89d3a97e43(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac7e6c14ad3fba2e59e0c8045591bd1239e803a2d8b679e8427b1a6b823cd324(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__244786ee753968301a1a0b6ee2f59adbc5f9861d724766577bd7bed65dd9276b(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    resources: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Route53RecoveryreadinessResourceSetResources, typing.Dict[builtins.str, typing.Any]]]],
    resource_set_name: builtins.str,
    resource_set_type: builtins.str,
    id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[Route53RecoveryreadinessResourceSetTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84989b814394695be4878fd80590cba2dc1343065c059ee120fe52386f62ed6d(
    *,
    dns_target_resource: typing.Optional[typing.Union[Route53RecoveryreadinessResourceSetResourcesDnsTargetResource, typing.Dict[builtins.str, typing.Any]]] = None,
    readiness_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    resource_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__627faf76f6e77afcb8bd0f3f11ec71faf981010317cd8496e9a830a8253aee4c(
    *,
    domain_name: builtins.str,
    hosted_zone_arn: typing.Optional[builtins.str] = None,
    record_set_id: typing.Optional[builtins.str] = None,
    record_type: typing.Optional[builtins.str] = None,
    target_resource: typing.Optional[typing.Union[Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResource, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0207e67fe5f53ad21f13a13ca2266cfcf80f7f13e4ef618cdeeafd304e2d85e6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b7400fb01055db3b28b243254fc7a7ba3329b867f39b8eda21fe4f7053473e9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb63e4d893c066f686bccd11f2c784d7aacb112059b50876f612de19186d19d6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e15409e55c4469d5470a1e878d697a39ba77f2101879dc938f30af3f02317ab(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0b1677e27ecefc61267e78dd7601ab75ab5c631d69220a53642a49d1ce9e733(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e03bc149936ae8e3f6cf855a2416fee1294024448051824d821832b1da1965ae(
    value: typing.Optional[Route53RecoveryreadinessResourceSetResourcesDnsTargetResource],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75a2f5585abfc65caf7b22a8d5aa21f0c2d79355bcd61b120d6078079278617b(
    *,
    nlb_resource: typing.Optional[typing.Union[Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResourceNlbResource, typing.Dict[builtins.str, typing.Any]]] = None,
    r53_resource: typing.Optional[typing.Union[Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResourceR53Resource, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc9085938add7074327398ce13aa76399b70df495278d6969c87ca16c2a3ff42(
    *,
    arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__105eb43776910ca8b87f5d77b6943b4acfcfe943eb01e659b020aac23571ee95(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fca1b2cf309ec15e0da138550d9b03c2876242def6a6b49128d721322fd164f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e64f05fd0384746e363813df448babe038156645cf7847da144e318d6cc51b7c(
    value: typing.Optional[Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResourceNlbResource],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54f0da7d04468d1c00b21ad672ae01c7dee13133bb6938d75f64fd789d1bbb62(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ba90dd3cc014e198a2f4e47d7fa165c3c93ec3eeef359af2c82b9be7187dd30(
    value: typing.Optional[Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResource],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__708669cc433c7d23ffd910b96ee768a71c1eb821ad4bbdb4b7596af23067244c(
    *,
    domain_name: typing.Optional[builtins.str] = None,
    record_set_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__716c502d1db7c6d6daff18959559f6e1a7c94e5f32b39cadd426505548ca5b50(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1f9d7c0eab4ac78fc0528a647df1ecf7992e5983dac78f0a545304f84de696f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8804ec462800990be6ef9b2a08474548efaacda8a0b670d48545a2d6483aab2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5caf7eeb9bf3a61d601037accbbe8a8878ec52db29e10f83153a3da77bd850d6(
    value: typing.Optional[Route53RecoveryreadinessResourceSetResourcesDnsTargetResourceTargetResourceR53Resource],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e03495320fb1d039c6a6acdd9f1aa9d9a89c4ba1275e64d3bfccb879d485767(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86eee78665139032211cd4833ca00dcd7fee95ae0863b38be8a734dccd02e77f(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5303cb3cb237c1b26ce5d5b3f240522ad68676bf94df077a8d8a232fea93d0b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41104c307a3f3e8db2acfeb2e3a091f87590a4096fef930094fed57d5cd32c43(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c09935ab9adbcaa525f84e6dcb547e73595329c77476e9883260f5b78b8615c9(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef0e1c7455d2d9441a7052dfdc476c882c4b1255860ab0b09f552bfb1959a10d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Route53RecoveryreadinessResourceSetResources]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7731d3600a4fc98a104696fa2d715451165ad0fae75999c8473cf8cb11a2a04e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b44f1fb156602b59d4cfe63d2fc12a9356bee9fdd93c1750a69692dad367f0ac(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d130f90be3dfc6c6ee97f2f28eb6c3670543be80ca2fe968e32215f23fb16ac(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__817878af3fee6ee8a7f309312968003b0544f0acd086763f4426779537acdba9(
    value: typing.Optional[typing.Union[Route53RecoveryreadinessResourceSetResources, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9ad46b0025cfebaefcadf7e87963a2a0518c9e0845de6194199b924204043ae(
    *,
    delete: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d76931278d4bdb28f8c3b67a6538bf4c8cb37e74316762c4736d66e6fe0706d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e30160945a01a4da517557cf1f0c27677a5421c790a5f4ab249f33c97746475d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6de6fb4a1dc31b85ea1b36055c09f29c2ea7143a2703378d2c4632dbba9dd3d(
    value: typing.Optional[typing.Union[Route53RecoveryreadinessResourceSetTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
