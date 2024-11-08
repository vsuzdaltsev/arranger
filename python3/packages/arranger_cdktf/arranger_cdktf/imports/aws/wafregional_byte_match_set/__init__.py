'''
# `aws_wafregional_byte_match_set`

Refer to the Terraform Registory for docs: [`aws_wafregional_byte_match_set`](https://www.terraform.io/docs/providers/aws/r/wafregional_byte_match_set).
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


class WafregionalByteMatchSet(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.wafregionalByteMatchSet.WafregionalByteMatchSet",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/wafregional_byte_match_set aws_wafregional_byte_match_set}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        byte_match_tuples: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WafregionalByteMatchSetByteMatchTuples", typing.Dict[builtins.str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/wafregional_byte_match_set aws_wafregional_byte_match_set} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_byte_match_set#name WafregionalByteMatchSet#name}.
        :param byte_match_tuples: byte_match_tuples block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_byte_match_set#byte_match_tuples WafregionalByteMatchSet#byte_match_tuples}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_byte_match_set#id WafregionalByteMatchSet#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa7442818f69ed1348e19dcd555a882b421dec4a331afca22e983376df149b59)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = WafregionalByteMatchSetConfig(
            name=name,
            byte_match_tuples=byte_match_tuples,
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

    @jsii.member(jsii_name="putByteMatchTuples")
    def put_byte_match_tuples(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WafregionalByteMatchSetByteMatchTuples", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7518968677d0c1306b44ba9bfb031439697c8c90efb320feac8c2161d1f04e71)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putByteMatchTuples", [value]))

    @jsii.member(jsii_name="resetByteMatchTuples")
    def reset_byte_match_tuples(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetByteMatchTuples", []))

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
    @jsii.member(jsii_name="byteMatchTuples")
    def byte_match_tuples(self) -> "WafregionalByteMatchSetByteMatchTuplesList":
        return typing.cast("WafregionalByteMatchSetByteMatchTuplesList", jsii.get(self, "byteMatchTuples"))

    @builtins.property
    @jsii.member(jsii_name="byteMatchTuplesInput")
    def byte_match_tuples_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WafregionalByteMatchSetByteMatchTuples"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WafregionalByteMatchSetByteMatchTuples"]]], jsii.get(self, "byteMatchTuplesInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f555971109eb7aa3a88269bfeec48769ed6b404cff80dd5963fb22d784bb8414)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c9b3d88a94c56c066645325f9cda8353285b033383341ddd762301fb5e68191)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="aws.wafregionalByteMatchSet.WafregionalByteMatchSetByteMatchTuples",
    jsii_struct_bases=[],
    name_mapping={
        "field_to_match": "fieldToMatch",
        "positional_constraint": "positionalConstraint",
        "text_transformation": "textTransformation",
        "target_string": "targetString",
    },
)
class WafregionalByteMatchSetByteMatchTuples:
    def __init__(
        self,
        *,
        field_to_match: typing.Union["WafregionalByteMatchSetByteMatchTuplesFieldToMatch", typing.Dict[builtins.str, typing.Any]],
        positional_constraint: builtins.str,
        text_transformation: builtins.str,
        target_string: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param field_to_match: field_to_match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_byte_match_set#field_to_match WafregionalByteMatchSet#field_to_match}
        :param positional_constraint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_byte_match_set#positional_constraint WafregionalByteMatchSet#positional_constraint}.
        :param text_transformation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_byte_match_set#text_transformation WafregionalByteMatchSet#text_transformation}.
        :param target_string: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_byte_match_set#target_string WafregionalByteMatchSet#target_string}.
        '''
        if isinstance(field_to_match, dict):
            field_to_match = WafregionalByteMatchSetByteMatchTuplesFieldToMatch(**field_to_match)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79bd2573e35fe883ba99158f462b489e33acc84a4bedc395cef79d76b814ceb6)
            check_type(argname="argument field_to_match", value=field_to_match, expected_type=type_hints["field_to_match"])
            check_type(argname="argument positional_constraint", value=positional_constraint, expected_type=type_hints["positional_constraint"])
            check_type(argname="argument text_transformation", value=text_transformation, expected_type=type_hints["text_transformation"])
            check_type(argname="argument target_string", value=target_string, expected_type=type_hints["target_string"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "field_to_match": field_to_match,
            "positional_constraint": positional_constraint,
            "text_transformation": text_transformation,
        }
        if target_string is not None:
            self._values["target_string"] = target_string

    @builtins.property
    def field_to_match(self) -> "WafregionalByteMatchSetByteMatchTuplesFieldToMatch":
        '''field_to_match block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_byte_match_set#field_to_match WafregionalByteMatchSet#field_to_match}
        '''
        result = self._values.get("field_to_match")
        assert result is not None, "Required property 'field_to_match' is missing"
        return typing.cast("WafregionalByteMatchSetByteMatchTuplesFieldToMatch", result)

    @builtins.property
    def positional_constraint(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_byte_match_set#positional_constraint WafregionalByteMatchSet#positional_constraint}.'''
        result = self._values.get("positional_constraint")
        assert result is not None, "Required property 'positional_constraint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def text_transformation(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_byte_match_set#text_transformation WafregionalByteMatchSet#text_transformation}.'''
        result = self._values.get("text_transformation")
        assert result is not None, "Required property 'text_transformation' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_string(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_byte_match_set#target_string WafregionalByteMatchSet#target_string}.'''
        result = self._values.get("target_string")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WafregionalByteMatchSetByteMatchTuples(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.wafregionalByteMatchSet.WafregionalByteMatchSetByteMatchTuplesFieldToMatch",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "data": "data"},
)
class WafregionalByteMatchSetByteMatchTuplesFieldToMatch:
    def __init__(
        self,
        *,
        type: builtins.str,
        data: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_byte_match_set#type WafregionalByteMatchSet#type}.
        :param data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_byte_match_set#data WafregionalByteMatchSet#data}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d79e3ab11e5d100a12e342027c10e7cef8d210995604fe945019c6847f7af826)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if data is not None:
            self._values["data"] = data

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_byte_match_set#type WafregionalByteMatchSet#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_byte_match_set#data WafregionalByteMatchSet#data}.'''
        result = self._values.get("data")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WafregionalByteMatchSetByteMatchTuplesFieldToMatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WafregionalByteMatchSetByteMatchTuplesFieldToMatchOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.wafregionalByteMatchSet.WafregionalByteMatchSetByteMatchTuplesFieldToMatchOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__46a363f6de5c3c37efa984dbf2073df5ddfed95eb50b7a941f6e459e6252f6c8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetData")
    def reset_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetData", []))

    @builtins.property
    @jsii.member(jsii_name="dataInput")
    def data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="data")
    def data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "data"))

    @data.setter
    def data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d4915eaa9a71becadbbdedccb7059b93f564e71b3ec685f4951aa76158f8235)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "data", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06918d3b84f953b492d77f350a1db09be1d886bf8a2794ee8c08c853f94d46a5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WafregionalByteMatchSetByteMatchTuplesFieldToMatch]:
        return typing.cast(typing.Optional[WafregionalByteMatchSetByteMatchTuplesFieldToMatch], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WafregionalByteMatchSetByteMatchTuplesFieldToMatch],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a8f9d73926c8f18de578821f03949ab63980a2556bdc15b7f4eb41a16af7ba3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WafregionalByteMatchSetByteMatchTuplesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.wafregionalByteMatchSet.WafregionalByteMatchSetByteMatchTuplesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__050dbb56b0c8bf921514bce75f41d0e07902b675033fcfba9b917b6eb557069b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "WafregionalByteMatchSetByteMatchTuplesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8dcd096fd888e05cba471b60252ab4022a7959f1b2fd97169967a2b6c10ce6a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WafregionalByteMatchSetByteMatchTuplesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__460123fb3a47a9ca4a24d4a0bf5c3cbecb59600885a7362314c64f4856179249)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5368493b0d3ae784701d7bba60e4a8760280b8d4a6beed9c78b5353f29b6493c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3ca42287afd036f0398d6bb44355f8a2d383c205f9a1ef9bcf75b80baee6debd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WafregionalByteMatchSetByteMatchTuples]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WafregionalByteMatchSetByteMatchTuples]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WafregionalByteMatchSetByteMatchTuples]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d78062c40b5c20ee06adfc688f2938ea20b062c8b9bcf914c2748920bb3e4c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WafregionalByteMatchSetByteMatchTuplesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.wafregionalByteMatchSet.WafregionalByteMatchSetByteMatchTuplesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ae36bea889177f32d1c1ffa2694c271a58eafaf1397355b16aa77a3a04950be7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putFieldToMatch")
    def put_field_to_match(
        self,
        *,
        type: builtins.str,
        data: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_byte_match_set#type WafregionalByteMatchSet#type}.
        :param data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_byte_match_set#data WafregionalByteMatchSet#data}.
        '''
        value = WafregionalByteMatchSetByteMatchTuplesFieldToMatch(
            type=type, data=data
        )

        return typing.cast(None, jsii.invoke(self, "putFieldToMatch", [value]))

    @jsii.member(jsii_name="resetTargetString")
    def reset_target_string(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetString", []))

    @builtins.property
    @jsii.member(jsii_name="fieldToMatch")
    def field_to_match(
        self,
    ) -> WafregionalByteMatchSetByteMatchTuplesFieldToMatchOutputReference:
        return typing.cast(WafregionalByteMatchSetByteMatchTuplesFieldToMatchOutputReference, jsii.get(self, "fieldToMatch"))

    @builtins.property
    @jsii.member(jsii_name="fieldToMatchInput")
    def field_to_match_input(
        self,
    ) -> typing.Optional[WafregionalByteMatchSetByteMatchTuplesFieldToMatch]:
        return typing.cast(typing.Optional[WafregionalByteMatchSetByteMatchTuplesFieldToMatch], jsii.get(self, "fieldToMatchInput"))

    @builtins.property
    @jsii.member(jsii_name="positionalConstraintInput")
    def positional_constraint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "positionalConstraintInput"))

    @builtins.property
    @jsii.member(jsii_name="targetStringInput")
    def target_string_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetStringInput"))

    @builtins.property
    @jsii.member(jsii_name="textTransformationInput")
    def text_transformation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "textTransformationInput"))

    @builtins.property
    @jsii.member(jsii_name="positionalConstraint")
    def positional_constraint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "positionalConstraint"))

    @positional_constraint.setter
    def positional_constraint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07d5fff585e7f458058ba9abed21d9ff42150b0f3b32e3ef57160fcd40d0bb58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "positionalConstraint", value)

    @builtins.property
    @jsii.member(jsii_name="targetString")
    def target_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetString"))

    @target_string.setter
    def target_string(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b89e4e43dc5654fa7caacdad73dc77eeccd6a5c6a2ad064def386c685a504ead)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetString", value)

    @builtins.property
    @jsii.member(jsii_name="textTransformation")
    def text_transformation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "textTransformation"))

    @text_transformation.setter
    def text_transformation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9cbde74e15e97c7191bc20ebd708bcb0892cbe54e92af5c6b5557cee265bd884)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "textTransformation", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WafregionalByteMatchSetByteMatchTuples, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WafregionalByteMatchSetByteMatchTuples, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WafregionalByteMatchSetByteMatchTuples, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fe247580a594582efb05c45326d7bf9d8c89867b0105b965bdbc120bd04ae3d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.wafregionalByteMatchSet.WafregionalByteMatchSetConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "byte_match_tuples": "byteMatchTuples",
        "id": "id",
    },
)
class WafregionalByteMatchSetConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        name: builtins.str,
        byte_match_tuples: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WafregionalByteMatchSetByteMatchTuples, typing.Dict[builtins.str, typing.Any]]]]] = None,
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
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_byte_match_set#name WafregionalByteMatchSet#name}.
        :param byte_match_tuples: byte_match_tuples block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_byte_match_set#byte_match_tuples WafregionalByteMatchSet#byte_match_tuples}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_byte_match_set#id WafregionalByteMatchSet#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4508b02797ad7d3fc43753ee47c58365756484b61a7cabd6021e097bbc0f0e68)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument byte_match_tuples", value=byte_match_tuples, expected_type=type_hints["byte_match_tuples"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
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
        if byte_match_tuples is not None:
            self._values["byte_match_tuples"] = byte_match_tuples
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
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_byte_match_set#name WafregionalByteMatchSet#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def byte_match_tuples(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WafregionalByteMatchSetByteMatchTuples]]]:
        '''byte_match_tuples block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_byte_match_set#byte_match_tuples WafregionalByteMatchSet#byte_match_tuples}
        '''
        result = self._values.get("byte_match_tuples")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WafregionalByteMatchSetByteMatchTuples]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_byte_match_set#id WafregionalByteMatchSet#id}.

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
        return "WafregionalByteMatchSetConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "WafregionalByteMatchSet",
    "WafregionalByteMatchSetByteMatchTuples",
    "WafregionalByteMatchSetByteMatchTuplesFieldToMatch",
    "WafregionalByteMatchSetByteMatchTuplesFieldToMatchOutputReference",
    "WafregionalByteMatchSetByteMatchTuplesList",
    "WafregionalByteMatchSetByteMatchTuplesOutputReference",
    "WafregionalByteMatchSetConfig",
]

publication.publish()

def _typecheckingstub__aa7442818f69ed1348e19dcd555a882b421dec4a331afca22e983376df149b59(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    byte_match_tuples: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WafregionalByteMatchSetByteMatchTuples, typing.Dict[builtins.str, typing.Any]]]]] = None,
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

def _typecheckingstub__7518968677d0c1306b44ba9bfb031439697c8c90efb320feac8c2161d1f04e71(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WafregionalByteMatchSetByteMatchTuples, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f555971109eb7aa3a88269bfeec48769ed6b404cff80dd5963fb22d784bb8414(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c9b3d88a94c56c066645325f9cda8353285b033383341ddd762301fb5e68191(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79bd2573e35fe883ba99158f462b489e33acc84a4bedc395cef79d76b814ceb6(
    *,
    field_to_match: typing.Union[WafregionalByteMatchSetByteMatchTuplesFieldToMatch, typing.Dict[builtins.str, typing.Any]],
    positional_constraint: builtins.str,
    text_transformation: builtins.str,
    target_string: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d79e3ab11e5d100a12e342027c10e7cef8d210995604fe945019c6847f7af826(
    *,
    type: builtins.str,
    data: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46a363f6de5c3c37efa984dbf2073df5ddfed95eb50b7a941f6e459e6252f6c8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d4915eaa9a71becadbbdedccb7059b93f564e71b3ec685f4951aa76158f8235(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06918d3b84f953b492d77f350a1db09be1d886bf8a2794ee8c08c853f94d46a5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a8f9d73926c8f18de578821f03949ab63980a2556bdc15b7f4eb41a16af7ba3(
    value: typing.Optional[WafregionalByteMatchSetByteMatchTuplesFieldToMatch],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__050dbb56b0c8bf921514bce75f41d0e07902b675033fcfba9b917b6eb557069b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8dcd096fd888e05cba471b60252ab4022a7959f1b2fd97169967a2b6c10ce6a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__460123fb3a47a9ca4a24d4a0bf5c3cbecb59600885a7362314c64f4856179249(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5368493b0d3ae784701d7bba60e4a8760280b8d4a6beed9c78b5353f29b6493c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ca42287afd036f0398d6bb44355f8a2d383c205f9a1ef9bcf75b80baee6debd(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d78062c40b5c20ee06adfc688f2938ea20b062c8b9bcf914c2748920bb3e4c9(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WafregionalByteMatchSetByteMatchTuples]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae36bea889177f32d1c1ffa2694c271a58eafaf1397355b16aa77a3a04950be7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07d5fff585e7f458058ba9abed21d9ff42150b0f3b32e3ef57160fcd40d0bb58(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b89e4e43dc5654fa7caacdad73dc77eeccd6a5c6a2ad064def386c685a504ead(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cbde74e15e97c7191bc20ebd708bcb0892cbe54e92af5c6b5557cee265bd884(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fe247580a594582efb05c45326d7bf9d8c89867b0105b965bdbc120bd04ae3d(
    value: typing.Optional[typing.Union[WafregionalByteMatchSetByteMatchTuples, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4508b02797ad7d3fc43753ee47c58365756484b61a7cabd6021e097bbc0f0e68(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    byte_match_tuples: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WafregionalByteMatchSetByteMatchTuples, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
