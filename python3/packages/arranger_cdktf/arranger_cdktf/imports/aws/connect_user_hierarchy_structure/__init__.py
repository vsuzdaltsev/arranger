'''
# `aws_connect_user_hierarchy_structure`

Refer to the Terraform Registory for docs: [`aws_connect_user_hierarchy_structure`](https://www.terraform.io/docs/providers/aws/r/connect_user_hierarchy_structure).
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


class ConnectUserHierarchyStructure(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.connectUserHierarchyStructure.ConnectUserHierarchyStructure",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/connect_user_hierarchy_structure aws_connect_user_hierarchy_structure}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        hierarchy_structure: typing.Union["ConnectUserHierarchyStructureHierarchyStructure", typing.Dict[builtins.str, typing.Any]],
        instance_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/connect_user_hierarchy_structure aws_connect_user_hierarchy_structure} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param hierarchy_structure: hierarchy_structure block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user_hierarchy_structure#hierarchy_structure ConnectUserHierarchyStructure#hierarchy_structure}
        :param instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user_hierarchy_structure#instance_id ConnectUserHierarchyStructure#instance_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user_hierarchy_structure#id ConnectUserHierarchyStructure#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c32b7ee3b77f8f41aa9ee178598492d51b0ac6d0003f80a0be73fcc4815ac336)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ConnectUserHierarchyStructureConfig(
            hierarchy_structure=hierarchy_structure,
            instance_id=instance_id,
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

    @jsii.member(jsii_name="putHierarchyStructure")
    def put_hierarchy_structure(
        self,
        *,
        level_five: typing.Optional[typing.Union["ConnectUserHierarchyStructureHierarchyStructureLevelFive", typing.Dict[builtins.str, typing.Any]]] = None,
        level_four: typing.Optional[typing.Union["ConnectUserHierarchyStructureHierarchyStructureLevelFour", typing.Dict[builtins.str, typing.Any]]] = None,
        level_one: typing.Optional[typing.Union["ConnectUserHierarchyStructureHierarchyStructureLevelOne", typing.Dict[builtins.str, typing.Any]]] = None,
        level_three: typing.Optional[typing.Union["ConnectUserHierarchyStructureHierarchyStructureLevelThree", typing.Dict[builtins.str, typing.Any]]] = None,
        level_two: typing.Optional[typing.Union["ConnectUserHierarchyStructureHierarchyStructureLevelTwo", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param level_five: level_five block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user_hierarchy_structure#level_five ConnectUserHierarchyStructure#level_five}
        :param level_four: level_four block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user_hierarchy_structure#level_four ConnectUserHierarchyStructure#level_four}
        :param level_one: level_one block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user_hierarchy_structure#level_one ConnectUserHierarchyStructure#level_one}
        :param level_three: level_three block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user_hierarchy_structure#level_three ConnectUserHierarchyStructure#level_three}
        :param level_two: level_two block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user_hierarchy_structure#level_two ConnectUserHierarchyStructure#level_two}
        '''
        value = ConnectUserHierarchyStructureHierarchyStructure(
            level_five=level_five,
            level_four=level_four,
            level_one=level_one,
            level_three=level_three,
            level_two=level_two,
        )

        return typing.cast(None, jsii.invoke(self, "putHierarchyStructure", [value]))

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
    @jsii.member(jsii_name="hierarchyStructure")
    def hierarchy_structure(
        self,
    ) -> "ConnectUserHierarchyStructureHierarchyStructureOutputReference":
        return typing.cast("ConnectUserHierarchyStructureHierarchyStructureOutputReference", jsii.get(self, "hierarchyStructure"))

    @builtins.property
    @jsii.member(jsii_name="hierarchyStructureInput")
    def hierarchy_structure_input(
        self,
    ) -> typing.Optional["ConnectUserHierarchyStructureHierarchyStructure"]:
        return typing.cast(typing.Optional["ConnectUserHierarchyStructureHierarchyStructure"], jsii.get(self, "hierarchyStructureInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceIdInput")
    def instance_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf740153f0f075e502c752b2fe0016a257d8bb62e5ac67d2f9b6739781d720d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceId"))

    @instance_id.setter
    def instance_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0d0e7d764003b3db1013a9c16a87e61605fe90a23242e880833d8ea18f10d16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceId", value)


@jsii.data_type(
    jsii_type="aws.connectUserHierarchyStructure.ConnectUserHierarchyStructureConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "hierarchy_structure": "hierarchyStructure",
        "instance_id": "instanceId",
        "id": "id",
    },
)
class ConnectUserHierarchyStructureConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        hierarchy_structure: typing.Union["ConnectUserHierarchyStructureHierarchyStructure", typing.Dict[builtins.str, typing.Any]],
        instance_id: builtins.str,
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
        :param hierarchy_structure: hierarchy_structure block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user_hierarchy_structure#hierarchy_structure ConnectUserHierarchyStructure#hierarchy_structure}
        :param instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user_hierarchy_structure#instance_id ConnectUserHierarchyStructure#instance_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user_hierarchy_structure#id ConnectUserHierarchyStructure#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(hierarchy_structure, dict):
            hierarchy_structure = ConnectUserHierarchyStructureHierarchyStructure(**hierarchy_structure)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5231a7234933b06aa1a12bdde373791be775683f1d482811e4d23c7245e54bf6)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument hierarchy_structure", value=hierarchy_structure, expected_type=type_hints["hierarchy_structure"])
            check_type(argname="argument instance_id", value=instance_id, expected_type=type_hints["instance_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "hierarchy_structure": hierarchy_structure,
            "instance_id": instance_id,
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
    def hierarchy_structure(self) -> "ConnectUserHierarchyStructureHierarchyStructure":
        '''hierarchy_structure block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user_hierarchy_structure#hierarchy_structure ConnectUserHierarchyStructure#hierarchy_structure}
        '''
        result = self._values.get("hierarchy_structure")
        assert result is not None, "Required property 'hierarchy_structure' is missing"
        return typing.cast("ConnectUserHierarchyStructureHierarchyStructure", result)

    @builtins.property
    def instance_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user_hierarchy_structure#instance_id ConnectUserHierarchyStructure#instance_id}.'''
        result = self._values.get("instance_id")
        assert result is not None, "Required property 'instance_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user_hierarchy_structure#id ConnectUserHierarchyStructure#id}.

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
        return "ConnectUserHierarchyStructureConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.connectUserHierarchyStructure.ConnectUserHierarchyStructureHierarchyStructure",
    jsii_struct_bases=[],
    name_mapping={
        "level_five": "levelFive",
        "level_four": "levelFour",
        "level_one": "levelOne",
        "level_three": "levelThree",
        "level_two": "levelTwo",
    },
)
class ConnectUserHierarchyStructureHierarchyStructure:
    def __init__(
        self,
        *,
        level_five: typing.Optional[typing.Union["ConnectUserHierarchyStructureHierarchyStructureLevelFive", typing.Dict[builtins.str, typing.Any]]] = None,
        level_four: typing.Optional[typing.Union["ConnectUserHierarchyStructureHierarchyStructureLevelFour", typing.Dict[builtins.str, typing.Any]]] = None,
        level_one: typing.Optional[typing.Union["ConnectUserHierarchyStructureHierarchyStructureLevelOne", typing.Dict[builtins.str, typing.Any]]] = None,
        level_three: typing.Optional[typing.Union["ConnectUserHierarchyStructureHierarchyStructureLevelThree", typing.Dict[builtins.str, typing.Any]]] = None,
        level_two: typing.Optional[typing.Union["ConnectUserHierarchyStructureHierarchyStructureLevelTwo", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param level_five: level_five block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user_hierarchy_structure#level_five ConnectUserHierarchyStructure#level_five}
        :param level_four: level_four block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user_hierarchy_structure#level_four ConnectUserHierarchyStructure#level_four}
        :param level_one: level_one block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user_hierarchy_structure#level_one ConnectUserHierarchyStructure#level_one}
        :param level_three: level_three block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user_hierarchy_structure#level_three ConnectUserHierarchyStructure#level_three}
        :param level_two: level_two block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user_hierarchy_structure#level_two ConnectUserHierarchyStructure#level_two}
        '''
        if isinstance(level_five, dict):
            level_five = ConnectUserHierarchyStructureHierarchyStructureLevelFive(**level_five)
        if isinstance(level_four, dict):
            level_four = ConnectUserHierarchyStructureHierarchyStructureLevelFour(**level_four)
        if isinstance(level_one, dict):
            level_one = ConnectUserHierarchyStructureHierarchyStructureLevelOne(**level_one)
        if isinstance(level_three, dict):
            level_three = ConnectUserHierarchyStructureHierarchyStructureLevelThree(**level_three)
        if isinstance(level_two, dict):
            level_two = ConnectUserHierarchyStructureHierarchyStructureLevelTwo(**level_two)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31107181027b7ff106c98be4758592876ec160e82d27009a2ee90f30948d776f)
            check_type(argname="argument level_five", value=level_five, expected_type=type_hints["level_five"])
            check_type(argname="argument level_four", value=level_four, expected_type=type_hints["level_four"])
            check_type(argname="argument level_one", value=level_one, expected_type=type_hints["level_one"])
            check_type(argname="argument level_three", value=level_three, expected_type=type_hints["level_three"])
            check_type(argname="argument level_two", value=level_two, expected_type=type_hints["level_two"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if level_five is not None:
            self._values["level_five"] = level_five
        if level_four is not None:
            self._values["level_four"] = level_four
        if level_one is not None:
            self._values["level_one"] = level_one
        if level_three is not None:
            self._values["level_three"] = level_three
        if level_two is not None:
            self._values["level_two"] = level_two

    @builtins.property
    def level_five(
        self,
    ) -> typing.Optional["ConnectUserHierarchyStructureHierarchyStructureLevelFive"]:
        '''level_five block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user_hierarchy_structure#level_five ConnectUserHierarchyStructure#level_five}
        '''
        result = self._values.get("level_five")
        return typing.cast(typing.Optional["ConnectUserHierarchyStructureHierarchyStructureLevelFive"], result)

    @builtins.property
    def level_four(
        self,
    ) -> typing.Optional["ConnectUserHierarchyStructureHierarchyStructureLevelFour"]:
        '''level_four block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user_hierarchy_structure#level_four ConnectUserHierarchyStructure#level_four}
        '''
        result = self._values.get("level_four")
        return typing.cast(typing.Optional["ConnectUserHierarchyStructureHierarchyStructureLevelFour"], result)

    @builtins.property
    def level_one(
        self,
    ) -> typing.Optional["ConnectUserHierarchyStructureHierarchyStructureLevelOne"]:
        '''level_one block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user_hierarchy_structure#level_one ConnectUserHierarchyStructure#level_one}
        '''
        result = self._values.get("level_one")
        return typing.cast(typing.Optional["ConnectUserHierarchyStructureHierarchyStructureLevelOne"], result)

    @builtins.property
    def level_three(
        self,
    ) -> typing.Optional["ConnectUserHierarchyStructureHierarchyStructureLevelThree"]:
        '''level_three block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user_hierarchy_structure#level_three ConnectUserHierarchyStructure#level_three}
        '''
        result = self._values.get("level_three")
        return typing.cast(typing.Optional["ConnectUserHierarchyStructureHierarchyStructureLevelThree"], result)

    @builtins.property
    def level_two(
        self,
    ) -> typing.Optional["ConnectUserHierarchyStructureHierarchyStructureLevelTwo"]:
        '''level_two block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user_hierarchy_structure#level_two ConnectUserHierarchyStructure#level_two}
        '''
        result = self._values.get("level_two")
        return typing.cast(typing.Optional["ConnectUserHierarchyStructureHierarchyStructureLevelTwo"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectUserHierarchyStructureHierarchyStructure(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.connectUserHierarchyStructure.ConnectUserHierarchyStructureHierarchyStructureLevelFive",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class ConnectUserHierarchyStructureHierarchyStructureLevelFive:
    def __init__(self, *, name: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user_hierarchy_structure#name ConnectUserHierarchyStructure#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b29fb8e6290b345892f8097b4cebe629fc7841d8bf6aed541862b7c43fa02c4)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user_hierarchy_structure#name ConnectUserHierarchyStructure#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectUserHierarchyStructureHierarchyStructureLevelFive(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ConnectUserHierarchyStructureHierarchyStructureLevelFiveOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.connectUserHierarchyStructure.ConnectUserHierarchyStructureHierarchyStructureLevelFiveOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5d9fc8aa438205713aa93be0a3be25b3ab0251564075a0c36c3c4af0acee9054)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ed38985bc69b99362a7d516145d1150dd10bee330f791e9a789ae3cc239391a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ConnectUserHierarchyStructureHierarchyStructureLevelFive]:
        return typing.cast(typing.Optional[ConnectUserHierarchyStructureHierarchyStructureLevelFive], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ConnectUserHierarchyStructureHierarchyStructureLevelFive],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3a9de0d0bd38d1f69e8709531de38cf19b76e49511892ecbd9e080ab6e4a540)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.connectUserHierarchyStructure.ConnectUserHierarchyStructureHierarchyStructureLevelFour",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class ConnectUserHierarchyStructureHierarchyStructureLevelFour:
    def __init__(self, *, name: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user_hierarchy_structure#name ConnectUserHierarchyStructure#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f214a85009c44cb8e5fc5f16b7efa62b0ac29ba851bde7aee369b32875a9ac83)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user_hierarchy_structure#name ConnectUserHierarchyStructure#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectUserHierarchyStructureHierarchyStructureLevelFour(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ConnectUserHierarchyStructureHierarchyStructureLevelFourOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.connectUserHierarchyStructure.ConnectUserHierarchyStructureHierarchyStructureLevelFourOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0c72f0c532c58a96fd4960fcdb9874b980d64184869f923a972c14c19f35914c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d50cfaef185b1a0ac6ceb116ab6f6e9bc40ee70e817be04de4015fc273516ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ConnectUserHierarchyStructureHierarchyStructureLevelFour]:
        return typing.cast(typing.Optional[ConnectUserHierarchyStructureHierarchyStructureLevelFour], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ConnectUserHierarchyStructureHierarchyStructureLevelFour],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c99ab9952129f32fb7393b43874323774c5eef4fb914bf0571db0956ea9b63c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.connectUserHierarchyStructure.ConnectUserHierarchyStructureHierarchyStructureLevelOne",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class ConnectUserHierarchyStructureHierarchyStructureLevelOne:
    def __init__(self, *, name: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user_hierarchy_structure#name ConnectUserHierarchyStructure#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__889c24c685fb1d81e4c213882d734f0295283b3a6ddee7c17ec8c0214ea480c0)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user_hierarchy_structure#name ConnectUserHierarchyStructure#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectUserHierarchyStructureHierarchyStructureLevelOne(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ConnectUserHierarchyStructureHierarchyStructureLevelOneOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.connectUserHierarchyStructure.ConnectUserHierarchyStructureHierarchyStructureLevelOneOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__da055fab7e7151468213940d47c84ab4d92bbe5b0b7bab72ebad719438195331)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03ed4f677f4699c21bb525e06d95070a60088cd83967db657141b678e20bfe5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ConnectUserHierarchyStructureHierarchyStructureLevelOne]:
        return typing.cast(typing.Optional[ConnectUserHierarchyStructureHierarchyStructureLevelOne], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ConnectUserHierarchyStructureHierarchyStructureLevelOne],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45e95c422fa020146a9f2086fe11b6e9584c97cbe95ebf354cabc65a63eeb79b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.connectUserHierarchyStructure.ConnectUserHierarchyStructureHierarchyStructureLevelThree",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class ConnectUserHierarchyStructureHierarchyStructureLevelThree:
    def __init__(self, *, name: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user_hierarchy_structure#name ConnectUserHierarchyStructure#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c4a463d937b07a1f1ba8bfddf4eebf1c7a822cc5ea875516ae583e7a3d52b6b)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user_hierarchy_structure#name ConnectUserHierarchyStructure#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectUserHierarchyStructureHierarchyStructureLevelThree(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ConnectUserHierarchyStructureHierarchyStructureLevelThreeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.connectUserHierarchyStructure.ConnectUserHierarchyStructureHierarchyStructureLevelThreeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a4a3a33b3bed19bb521ba4f0a56b164a3abab4ca055c6baad32247f216a114f4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f75d21beabcd1de75a42bfa46aa567dddef173eea04181de7117e9550af947ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ConnectUserHierarchyStructureHierarchyStructureLevelThree]:
        return typing.cast(typing.Optional[ConnectUserHierarchyStructureHierarchyStructureLevelThree], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ConnectUserHierarchyStructureHierarchyStructureLevelThree],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e073c7e6471496b0ccc78926fcfd4d231890e5f80e80bff2479a09f74a607710)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.connectUserHierarchyStructure.ConnectUserHierarchyStructureHierarchyStructureLevelTwo",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class ConnectUserHierarchyStructureHierarchyStructureLevelTwo:
    def __init__(self, *, name: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user_hierarchy_structure#name ConnectUserHierarchyStructure#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04a9c87bd440aad6f7c275aba10a7385e06ce089bdd5cac11deeff5c4e92c64e)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user_hierarchy_structure#name ConnectUserHierarchyStructure#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectUserHierarchyStructureHierarchyStructureLevelTwo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ConnectUserHierarchyStructureHierarchyStructureLevelTwoOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.connectUserHierarchyStructure.ConnectUserHierarchyStructureHierarchyStructureLevelTwoOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__681529ca99f3ca406c7d6b104fab70e3e137b0ea513b461d78503f4d2a292e39)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e75699eec0244f0410175913cf389f2d4a251052e936869abc3a434d2c2a9018)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ConnectUserHierarchyStructureHierarchyStructureLevelTwo]:
        return typing.cast(typing.Optional[ConnectUserHierarchyStructureHierarchyStructureLevelTwo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ConnectUserHierarchyStructureHierarchyStructureLevelTwo],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf79f89bbe5d88fd42d918b7aa043db7d190204ad9526d6ef24ad373c6ebba1e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ConnectUserHierarchyStructureHierarchyStructureOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.connectUserHierarchyStructure.ConnectUserHierarchyStructureHierarchyStructureOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1c1ad9cb67fa4e128903ebf6ca80bebb34ca5c09e024567a4d1da93c857e6782)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putLevelFive")
    def put_level_five(self, *, name: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user_hierarchy_structure#name ConnectUserHierarchyStructure#name}.
        '''
        value = ConnectUserHierarchyStructureHierarchyStructureLevelFive(name=name)

        return typing.cast(None, jsii.invoke(self, "putLevelFive", [value]))

    @jsii.member(jsii_name="putLevelFour")
    def put_level_four(self, *, name: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user_hierarchy_structure#name ConnectUserHierarchyStructure#name}.
        '''
        value = ConnectUserHierarchyStructureHierarchyStructureLevelFour(name=name)

        return typing.cast(None, jsii.invoke(self, "putLevelFour", [value]))

    @jsii.member(jsii_name="putLevelOne")
    def put_level_one(self, *, name: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user_hierarchy_structure#name ConnectUserHierarchyStructure#name}.
        '''
        value = ConnectUserHierarchyStructureHierarchyStructureLevelOne(name=name)

        return typing.cast(None, jsii.invoke(self, "putLevelOne", [value]))

    @jsii.member(jsii_name="putLevelThree")
    def put_level_three(self, *, name: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user_hierarchy_structure#name ConnectUserHierarchyStructure#name}.
        '''
        value = ConnectUserHierarchyStructureHierarchyStructureLevelThree(name=name)

        return typing.cast(None, jsii.invoke(self, "putLevelThree", [value]))

    @jsii.member(jsii_name="putLevelTwo")
    def put_level_two(self, *, name: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_user_hierarchy_structure#name ConnectUserHierarchyStructure#name}.
        '''
        value = ConnectUserHierarchyStructureHierarchyStructureLevelTwo(name=name)

        return typing.cast(None, jsii.invoke(self, "putLevelTwo", [value]))

    @jsii.member(jsii_name="resetLevelFive")
    def reset_level_five(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLevelFive", []))

    @jsii.member(jsii_name="resetLevelFour")
    def reset_level_four(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLevelFour", []))

    @jsii.member(jsii_name="resetLevelOne")
    def reset_level_one(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLevelOne", []))

    @jsii.member(jsii_name="resetLevelThree")
    def reset_level_three(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLevelThree", []))

    @jsii.member(jsii_name="resetLevelTwo")
    def reset_level_two(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLevelTwo", []))

    @builtins.property
    @jsii.member(jsii_name="levelFive")
    def level_five(
        self,
    ) -> ConnectUserHierarchyStructureHierarchyStructureLevelFiveOutputReference:
        return typing.cast(ConnectUserHierarchyStructureHierarchyStructureLevelFiveOutputReference, jsii.get(self, "levelFive"))

    @builtins.property
    @jsii.member(jsii_name="levelFour")
    def level_four(
        self,
    ) -> ConnectUserHierarchyStructureHierarchyStructureLevelFourOutputReference:
        return typing.cast(ConnectUserHierarchyStructureHierarchyStructureLevelFourOutputReference, jsii.get(self, "levelFour"))

    @builtins.property
    @jsii.member(jsii_name="levelOne")
    def level_one(
        self,
    ) -> ConnectUserHierarchyStructureHierarchyStructureLevelOneOutputReference:
        return typing.cast(ConnectUserHierarchyStructureHierarchyStructureLevelOneOutputReference, jsii.get(self, "levelOne"))

    @builtins.property
    @jsii.member(jsii_name="levelThree")
    def level_three(
        self,
    ) -> ConnectUserHierarchyStructureHierarchyStructureLevelThreeOutputReference:
        return typing.cast(ConnectUserHierarchyStructureHierarchyStructureLevelThreeOutputReference, jsii.get(self, "levelThree"))

    @builtins.property
    @jsii.member(jsii_name="levelTwo")
    def level_two(
        self,
    ) -> ConnectUserHierarchyStructureHierarchyStructureLevelTwoOutputReference:
        return typing.cast(ConnectUserHierarchyStructureHierarchyStructureLevelTwoOutputReference, jsii.get(self, "levelTwo"))

    @builtins.property
    @jsii.member(jsii_name="levelFiveInput")
    def level_five_input(
        self,
    ) -> typing.Optional[ConnectUserHierarchyStructureHierarchyStructureLevelFive]:
        return typing.cast(typing.Optional[ConnectUserHierarchyStructureHierarchyStructureLevelFive], jsii.get(self, "levelFiveInput"))

    @builtins.property
    @jsii.member(jsii_name="levelFourInput")
    def level_four_input(
        self,
    ) -> typing.Optional[ConnectUserHierarchyStructureHierarchyStructureLevelFour]:
        return typing.cast(typing.Optional[ConnectUserHierarchyStructureHierarchyStructureLevelFour], jsii.get(self, "levelFourInput"))

    @builtins.property
    @jsii.member(jsii_name="levelOneInput")
    def level_one_input(
        self,
    ) -> typing.Optional[ConnectUserHierarchyStructureHierarchyStructureLevelOne]:
        return typing.cast(typing.Optional[ConnectUserHierarchyStructureHierarchyStructureLevelOne], jsii.get(self, "levelOneInput"))

    @builtins.property
    @jsii.member(jsii_name="levelThreeInput")
    def level_three_input(
        self,
    ) -> typing.Optional[ConnectUserHierarchyStructureHierarchyStructureLevelThree]:
        return typing.cast(typing.Optional[ConnectUserHierarchyStructureHierarchyStructureLevelThree], jsii.get(self, "levelThreeInput"))

    @builtins.property
    @jsii.member(jsii_name="levelTwoInput")
    def level_two_input(
        self,
    ) -> typing.Optional[ConnectUserHierarchyStructureHierarchyStructureLevelTwo]:
        return typing.cast(typing.Optional[ConnectUserHierarchyStructureHierarchyStructureLevelTwo], jsii.get(self, "levelTwoInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ConnectUserHierarchyStructureHierarchyStructure]:
        return typing.cast(typing.Optional[ConnectUserHierarchyStructureHierarchyStructure], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ConnectUserHierarchyStructureHierarchyStructure],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a252df4d474c78b0a044789920df0d109573db0e6e4319ae33517d7a1bc2a24)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ConnectUserHierarchyStructure",
    "ConnectUserHierarchyStructureConfig",
    "ConnectUserHierarchyStructureHierarchyStructure",
    "ConnectUserHierarchyStructureHierarchyStructureLevelFive",
    "ConnectUserHierarchyStructureHierarchyStructureLevelFiveOutputReference",
    "ConnectUserHierarchyStructureHierarchyStructureLevelFour",
    "ConnectUserHierarchyStructureHierarchyStructureLevelFourOutputReference",
    "ConnectUserHierarchyStructureHierarchyStructureLevelOne",
    "ConnectUserHierarchyStructureHierarchyStructureLevelOneOutputReference",
    "ConnectUserHierarchyStructureHierarchyStructureLevelThree",
    "ConnectUserHierarchyStructureHierarchyStructureLevelThreeOutputReference",
    "ConnectUserHierarchyStructureHierarchyStructureLevelTwo",
    "ConnectUserHierarchyStructureHierarchyStructureLevelTwoOutputReference",
    "ConnectUserHierarchyStructureHierarchyStructureOutputReference",
]

publication.publish()

def _typecheckingstub__c32b7ee3b77f8f41aa9ee178598492d51b0ac6d0003f80a0be73fcc4815ac336(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    hierarchy_structure: typing.Union[ConnectUserHierarchyStructureHierarchyStructure, typing.Dict[builtins.str, typing.Any]],
    instance_id: builtins.str,
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

def _typecheckingstub__cf740153f0f075e502c752b2fe0016a257d8bb62e5ac67d2f9b6739781d720d8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0d0e7d764003b3db1013a9c16a87e61605fe90a23242e880833d8ea18f10d16(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5231a7234933b06aa1a12bdde373791be775683f1d482811e4d23c7245e54bf6(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    hierarchy_structure: typing.Union[ConnectUserHierarchyStructureHierarchyStructure, typing.Dict[builtins.str, typing.Any]],
    instance_id: builtins.str,
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31107181027b7ff106c98be4758592876ec160e82d27009a2ee90f30948d776f(
    *,
    level_five: typing.Optional[typing.Union[ConnectUserHierarchyStructureHierarchyStructureLevelFive, typing.Dict[builtins.str, typing.Any]]] = None,
    level_four: typing.Optional[typing.Union[ConnectUserHierarchyStructureHierarchyStructureLevelFour, typing.Dict[builtins.str, typing.Any]]] = None,
    level_one: typing.Optional[typing.Union[ConnectUserHierarchyStructureHierarchyStructureLevelOne, typing.Dict[builtins.str, typing.Any]]] = None,
    level_three: typing.Optional[typing.Union[ConnectUserHierarchyStructureHierarchyStructureLevelThree, typing.Dict[builtins.str, typing.Any]]] = None,
    level_two: typing.Optional[typing.Union[ConnectUserHierarchyStructureHierarchyStructureLevelTwo, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b29fb8e6290b345892f8097b4cebe629fc7841d8bf6aed541862b7c43fa02c4(
    *,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d9fc8aa438205713aa93be0a3be25b3ab0251564075a0c36c3c4af0acee9054(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ed38985bc69b99362a7d516145d1150dd10bee330f791e9a789ae3cc239391a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3a9de0d0bd38d1f69e8709531de38cf19b76e49511892ecbd9e080ab6e4a540(
    value: typing.Optional[ConnectUserHierarchyStructureHierarchyStructureLevelFive],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f214a85009c44cb8e5fc5f16b7efa62b0ac29ba851bde7aee369b32875a9ac83(
    *,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c72f0c532c58a96fd4960fcdb9874b980d64184869f923a972c14c19f35914c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d50cfaef185b1a0ac6ceb116ab6f6e9bc40ee70e817be04de4015fc273516ff(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c99ab9952129f32fb7393b43874323774c5eef4fb914bf0571db0956ea9b63c6(
    value: typing.Optional[ConnectUserHierarchyStructureHierarchyStructureLevelFour],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__889c24c685fb1d81e4c213882d734f0295283b3a6ddee7c17ec8c0214ea480c0(
    *,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da055fab7e7151468213940d47c84ab4d92bbe5b0b7bab72ebad719438195331(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03ed4f677f4699c21bb525e06d95070a60088cd83967db657141b678e20bfe5e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45e95c422fa020146a9f2086fe11b6e9584c97cbe95ebf354cabc65a63eeb79b(
    value: typing.Optional[ConnectUserHierarchyStructureHierarchyStructureLevelOne],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c4a463d937b07a1f1ba8bfddf4eebf1c7a822cc5ea875516ae583e7a3d52b6b(
    *,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4a3a33b3bed19bb521ba4f0a56b164a3abab4ca055c6baad32247f216a114f4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f75d21beabcd1de75a42bfa46aa567dddef173eea04181de7117e9550af947ec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e073c7e6471496b0ccc78926fcfd4d231890e5f80e80bff2479a09f74a607710(
    value: typing.Optional[ConnectUserHierarchyStructureHierarchyStructureLevelThree],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04a9c87bd440aad6f7c275aba10a7385e06ce089bdd5cac11deeff5c4e92c64e(
    *,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__681529ca99f3ca406c7d6b104fab70e3e137b0ea513b461d78503f4d2a292e39(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e75699eec0244f0410175913cf389f2d4a251052e936869abc3a434d2c2a9018(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf79f89bbe5d88fd42d918b7aa043db7d190204ad9526d6ef24ad373c6ebba1e(
    value: typing.Optional[ConnectUserHierarchyStructureHierarchyStructureLevelTwo],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c1ad9cb67fa4e128903ebf6ca80bebb34ca5c09e024567a4d1da93c857e6782(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a252df4d474c78b0a044789920df0d109573db0e6e4319ae33517d7a1bc2a24(
    value: typing.Optional[ConnectUserHierarchyStructureHierarchyStructure],
) -> None:
    """Type checking stubs"""
    pass
