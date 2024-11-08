'''
# `aws_datapipeline_pipeline_definition`

Refer to the Terraform Registory for docs: [`aws_datapipeline_pipeline_definition`](https://www.terraform.io/docs/providers/aws/r/datapipeline_pipeline_definition).
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


class DatapipelinePipelineDefinition(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.datapipelinePipelineDefinition.DatapipelinePipelineDefinition",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/datapipeline_pipeline_definition aws_datapipeline_pipeline_definition}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        pipeline_id: builtins.str,
        pipeline_object: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DatapipelinePipelineDefinitionPipelineObject", typing.Dict[builtins.str, typing.Any]]]],
        id: typing.Optional[builtins.str] = None,
        parameter_object: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DatapipelinePipelineDefinitionParameterObject", typing.Dict[builtins.str, typing.Any]]]]] = None,
        parameter_value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DatapipelinePipelineDefinitionParameterValue", typing.Dict[builtins.str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/datapipeline_pipeline_definition aws_datapipeline_pipeline_definition} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param pipeline_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datapipeline_pipeline_definition#pipeline_id DatapipelinePipelineDefinition#pipeline_id}.
        :param pipeline_object: pipeline_object block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datapipeline_pipeline_definition#pipeline_object DatapipelinePipelineDefinition#pipeline_object}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datapipeline_pipeline_definition#id DatapipelinePipelineDefinition#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param parameter_object: parameter_object block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datapipeline_pipeline_definition#parameter_object DatapipelinePipelineDefinition#parameter_object}
        :param parameter_value: parameter_value block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datapipeline_pipeline_definition#parameter_value DatapipelinePipelineDefinition#parameter_value}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d95d62c42224b9947ff5a8a34bd22d819c814d687a4dab917ec6af6888748fd)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DatapipelinePipelineDefinitionConfig(
            pipeline_id=pipeline_id,
            pipeline_object=pipeline_object,
            id=id,
            parameter_object=parameter_object,
            parameter_value=parameter_value,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putParameterObject")
    def put_parameter_object(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DatapipelinePipelineDefinitionParameterObject", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b511dab153f935723046678be65399c21b16208bcd0b3559ba7556832906855e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putParameterObject", [value]))

    @jsii.member(jsii_name="putParameterValue")
    def put_parameter_value(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DatapipelinePipelineDefinitionParameterValue", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca6efad9cb199020891810704c76807a572ece68b18cff0da0b9b063f7ab13a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putParameterValue", [value]))

    @jsii.member(jsii_name="putPipelineObject")
    def put_pipeline_object(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DatapipelinePipelineDefinitionPipelineObject", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27522ab7c42fe15e8b8591bb47a5119c6e5b3f4288b68243548cdf3e3e6bc9cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPipelineObject", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetParameterObject")
    def reset_parameter_object(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameterObject", []))

    @jsii.member(jsii_name="resetParameterValue")
    def reset_parameter_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameterValue", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="parameterObject")
    def parameter_object(self) -> "DatapipelinePipelineDefinitionParameterObjectList":
        return typing.cast("DatapipelinePipelineDefinitionParameterObjectList", jsii.get(self, "parameterObject"))

    @builtins.property
    @jsii.member(jsii_name="parameterValue")
    def parameter_value(self) -> "DatapipelinePipelineDefinitionParameterValueList":
        return typing.cast("DatapipelinePipelineDefinitionParameterValueList", jsii.get(self, "parameterValue"))

    @builtins.property
    @jsii.member(jsii_name="pipelineObject")
    def pipeline_object(self) -> "DatapipelinePipelineDefinitionPipelineObjectList":
        return typing.cast("DatapipelinePipelineDefinitionPipelineObjectList", jsii.get(self, "pipelineObject"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="parameterObjectInput")
    def parameter_object_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DatapipelinePipelineDefinitionParameterObject"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DatapipelinePipelineDefinitionParameterObject"]]], jsii.get(self, "parameterObjectInput"))

    @builtins.property
    @jsii.member(jsii_name="parameterValueInput")
    def parameter_value_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DatapipelinePipelineDefinitionParameterValue"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DatapipelinePipelineDefinitionParameterValue"]]], jsii.get(self, "parameterValueInput"))

    @builtins.property
    @jsii.member(jsii_name="pipelineIdInput")
    def pipeline_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pipelineIdInput"))

    @builtins.property
    @jsii.member(jsii_name="pipelineObjectInput")
    def pipeline_object_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DatapipelinePipelineDefinitionPipelineObject"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DatapipelinePipelineDefinitionPipelineObject"]]], jsii.get(self, "pipelineObjectInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32e758d6d453fb4f46edee2b10f72b970fb57e8cd68fdfc0acdd01378a491a21)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="pipelineId")
    def pipeline_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pipelineId"))

    @pipeline_id.setter
    def pipeline_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__158527d197f8a3737e14cca5a73dda338fb584a3e0fbbf844ec8119c6fecc4e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pipelineId", value)


@jsii.data_type(
    jsii_type="aws.datapipelinePipelineDefinition.DatapipelinePipelineDefinitionConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "pipeline_id": "pipelineId",
        "pipeline_object": "pipelineObject",
        "id": "id",
        "parameter_object": "parameterObject",
        "parameter_value": "parameterValue",
    },
)
class DatapipelinePipelineDefinitionConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        pipeline_id: builtins.str,
        pipeline_object: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DatapipelinePipelineDefinitionPipelineObject", typing.Dict[builtins.str, typing.Any]]]],
        id: typing.Optional[builtins.str] = None,
        parameter_object: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DatapipelinePipelineDefinitionParameterObject", typing.Dict[builtins.str, typing.Any]]]]] = None,
        parameter_value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DatapipelinePipelineDefinitionParameterValue", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param pipeline_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datapipeline_pipeline_definition#pipeline_id DatapipelinePipelineDefinition#pipeline_id}.
        :param pipeline_object: pipeline_object block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datapipeline_pipeline_definition#pipeline_object DatapipelinePipelineDefinition#pipeline_object}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datapipeline_pipeline_definition#id DatapipelinePipelineDefinition#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param parameter_object: parameter_object block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datapipeline_pipeline_definition#parameter_object DatapipelinePipelineDefinition#parameter_object}
        :param parameter_value: parameter_value block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datapipeline_pipeline_definition#parameter_value DatapipelinePipelineDefinition#parameter_value}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d5a12a080ef17325c5a28764b8b74cfbe04dfb2b7bdb7f8ea71a5fee785a978)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument pipeline_id", value=pipeline_id, expected_type=type_hints["pipeline_id"])
            check_type(argname="argument pipeline_object", value=pipeline_object, expected_type=type_hints["pipeline_object"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument parameter_object", value=parameter_object, expected_type=type_hints["parameter_object"])
            check_type(argname="argument parameter_value", value=parameter_value, expected_type=type_hints["parameter_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "pipeline_id": pipeline_id,
            "pipeline_object": pipeline_object,
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
        if parameter_object is not None:
            self._values["parameter_object"] = parameter_object
        if parameter_value is not None:
            self._values["parameter_value"] = parameter_value

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
    def pipeline_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datapipeline_pipeline_definition#pipeline_id DatapipelinePipelineDefinition#pipeline_id}.'''
        result = self._values.get("pipeline_id")
        assert result is not None, "Required property 'pipeline_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def pipeline_object(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DatapipelinePipelineDefinitionPipelineObject"]]:
        '''pipeline_object block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datapipeline_pipeline_definition#pipeline_object DatapipelinePipelineDefinition#pipeline_object}
        '''
        result = self._values.get("pipeline_object")
        assert result is not None, "Required property 'pipeline_object' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DatapipelinePipelineDefinitionPipelineObject"]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datapipeline_pipeline_definition#id DatapipelinePipelineDefinition#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameter_object(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DatapipelinePipelineDefinitionParameterObject"]]]:
        '''parameter_object block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datapipeline_pipeline_definition#parameter_object DatapipelinePipelineDefinition#parameter_object}
        '''
        result = self._values.get("parameter_object")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DatapipelinePipelineDefinitionParameterObject"]]], result)

    @builtins.property
    def parameter_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DatapipelinePipelineDefinitionParameterValue"]]]:
        '''parameter_value block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datapipeline_pipeline_definition#parameter_value DatapipelinePipelineDefinition#parameter_value}
        '''
        result = self._values.get("parameter_value")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DatapipelinePipelineDefinitionParameterValue"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatapipelinePipelineDefinitionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.datapipelinePipelineDefinition.DatapipelinePipelineDefinitionParameterObject",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "attribute": "attribute"},
)
class DatapipelinePipelineDefinitionParameterObject:
    def __init__(
        self,
        *,
        id: builtins.str,
        attribute: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DatapipelinePipelineDefinitionParameterObjectAttribute", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datapipeline_pipeline_definition#id DatapipelinePipelineDefinition#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param attribute: attribute block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datapipeline_pipeline_definition#attribute DatapipelinePipelineDefinition#attribute}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6643680fc2bc478fc6fd7b70058c2b2bb4915458ae8c30cfadcf9d9105161bb)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument attribute", value=attribute, expected_type=type_hints["attribute"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "id": id,
        }
        if attribute is not None:
            self._values["attribute"] = attribute

    @builtins.property
    def id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datapipeline_pipeline_definition#id DatapipelinePipelineDefinition#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def attribute(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DatapipelinePipelineDefinitionParameterObjectAttribute"]]]:
        '''attribute block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datapipeline_pipeline_definition#attribute DatapipelinePipelineDefinition#attribute}
        '''
        result = self._values.get("attribute")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DatapipelinePipelineDefinitionParameterObjectAttribute"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatapipelinePipelineDefinitionParameterObject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.datapipelinePipelineDefinition.DatapipelinePipelineDefinitionParameterObjectAttribute",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "string_value": "stringValue"},
)
class DatapipelinePipelineDefinitionParameterObjectAttribute:
    def __init__(self, *, key: builtins.str, string_value: builtins.str) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datapipeline_pipeline_definition#key DatapipelinePipelineDefinition#key}.
        :param string_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datapipeline_pipeline_definition#string_value DatapipelinePipelineDefinition#string_value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bdc91c8d68757285baf5d040c9b0029c9e17083405d062afd2aeae36c62f536)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument string_value", value=string_value, expected_type=type_hints["string_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "string_value": string_value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datapipeline_pipeline_definition#key DatapipelinePipelineDefinition#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def string_value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datapipeline_pipeline_definition#string_value DatapipelinePipelineDefinition#string_value}.'''
        result = self._values.get("string_value")
        assert result is not None, "Required property 'string_value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatapipelinePipelineDefinitionParameterObjectAttribute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatapipelinePipelineDefinitionParameterObjectAttributeList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.datapipelinePipelineDefinition.DatapipelinePipelineDefinitionParameterObjectAttributeList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ed44702f997c91689fd958ee0aa33bd48a83e0671e8239089ae34d12a3406fdf)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DatapipelinePipelineDefinitionParameterObjectAttributeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__852d08212824cd64191ccce6f9464226a8084fb77cf30b30b2160b4566446862)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DatapipelinePipelineDefinitionParameterObjectAttributeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9248e4d1c89deae9ee69da9dfaa21912f2d366a7b66dbbe1e551438290dea92c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__710311afd653ee97bfd9d1b3739d6e02676c433ed6297118a2d87d5cd9fc470b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c115d99df2f761b4ef11713f782d79a5ab9a5ccc41c715c75ef1e94e0af8c0d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatapipelinePipelineDefinitionParameterObjectAttribute]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatapipelinePipelineDefinitionParameterObjectAttribute]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatapipelinePipelineDefinitionParameterObjectAttribute]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a28c1f00a1f00d80e5c905587e9ff8794a946e6f5cad81367064c0732bfa83b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DatapipelinePipelineDefinitionParameterObjectAttributeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.datapipelinePipelineDefinition.DatapipelinePipelineDefinitionParameterObjectAttributeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3ed1bce6d4e3b2042ec2f987e69f7369175dce2d9a12007e90f8821464b2853f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="stringValueInput")
    def string_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stringValueInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42a47b5cb5cc33cd47a4176ad46e8a3d38ec9f7f75e30e5e0be44159cc381f2a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="stringValue")
    def string_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stringValue"))

    @string_value.setter
    def string_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e152455990f1294523da1ca2115914e64ab1f66c5dd411bdf1fc0e61865df41)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stringValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DatapipelinePipelineDefinitionParameterObjectAttribute, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DatapipelinePipelineDefinitionParameterObjectAttribute, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DatapipelinePipelineDefinitionParameterObjectAttribute, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b80f10e4d32e7a8c9a2837c7a4d2274aa503d367204991ab498802fb72638f8f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DatapipelinePipelineDefinitionParameterObjectList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.datapipelinePipelineDefinition.DatapipelinePipelineDefinitionParameterObjectList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cbecdbb29838f1957a3af738b802267f29ec725fa920878489bbb3a1025ff26f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DatapipelinePipelineDefinitionParameterObjectOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b70292fe87cb27f06d5dc00c8ac7fa093e588685d1c61f9fe9584ae1c9f9fa5)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DatapipelinePipelineDefinitionParameterObjectOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0eb845dcd8bda1bd814a73f39501f94c417886ae51475c9a983be482b009c5fa)
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
            type_hints = typing.get_type_hints(_typecheckingstub__eed4cb924c97557c0039fd09ba493f326ecce2edbec68ac3a511edf2a95bcb27)
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
            type_hints = typing.get_type_hints(_typecheckingstub__315029d4a945cfbad7747ce338da20193f02360d9be7cd959d4ae53fc8cf49c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatapipelinePipelineDefinitionParameterObject]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatapipelinePipelineDefinitionParameterObject]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatapipelinePipelineDefinitionParameterObject]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8557fe2d9a32f3274135bcee8dbf4f7e04520c5e5c895fcba86da0e59124bc21)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DatapipelinePipelineDefinitionParameterObjectOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.datapipelinePipelineDefinition.DatapipelinePipelineDefinitionParameterObjectOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a116978a64cd0e2bca3dbefccdffbf05f845162447ccd8cc671843e51854a798)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAttribute")
    def put_attribute(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DatapipelinePipelineDefinitionParameterObjectAttribute, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2190894ac637c61f794e6da5f975f72ebadcab16e7bf99c00b0ef956f0c2c81)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAttribute", [value]))

    @jsii.member(jsii_name="resetAttribute")
    def reset_attribute(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAttribute", []))

    @builtins.property
    @jsii.member(jsii_name="attribute")
    def attribute(self) -> DatapipelinePipelineDefinitionParameterObjectAttributeList:
        return typing.cast(DatapipelinePipelineDefinitionParameterObjectAttributeList, jsii.get(self, "attribute"))

    @builtins.property
    @jsii.member(jsii_name="attributeInput")
    def attribute_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatapipelinePipelineDefinitionParameterObjectAttribute]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatapipelinePipelineDefinitionParameterObjectAttribute]]], jsii.get(self, "attributeInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1d5485bf717f36f0df69c51d07c91cb5223d79ac2f62e4f30aed18f74262db8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DatapipelinePipelineDefinitionParameterObject, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DatapipelinePipelineDefinitionParameterObject, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DatapipelinePipelineDefinitionParameterObject, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07f826004be5b52caf9cc7867fd4d41e7388451321fc628c245208b5130d97ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.datapipelinePipelineDefinition.DatapipelinePipelineDefinitionParameterValue",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "string_value": "stringValue"},
)
class DatapipelinePipelineDefinitionParameterValue:
    def __init__(self, *, id: builtins.str, string_value: builtins.str) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datapipeline_pipeline_definition#id DatapipelinePipelineDefinition#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param string_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datapipeline_pipeline_definition#string_value DatapipelinePipelineDefinition#string_value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a60fafc7c4c8d9020f10f745741fef3fd0d24813c1f3d1e8fdf74f55a126d2b)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument string_value", value=string_value, expected_type=type_hints["string_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "id": id,
            "string_value": string_value,
        }

    @builtins.property
    def id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datapipeline_pipeline_definition#id DatapipelinePipelineDefinition#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def string_value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datapipeline_pipeline_definition#string_value DatapipelinePipelineDefinition#string_value}.'''
        result = self._values.get("string_value")
        assert result is not None, "Required property 'string_value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatapipelinePipelineDefinitionParameterValue(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatapipelinePipelineDefinitionParameterValueList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.datapipelinePipelineDefinition.DatapipelinePipelineDefinitionParameterValueList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__be09de2b95141462d89a9b1add984194121e0a82bd5c5decb1a8843eac2ae91e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DatapipelinePipelineDefinitionParameterValueOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__174fd90a79333ac3d4396a20d2e6ce7b5876a8b0441f4cdaaf6db9ef52439cd7)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DatapipelinePipelineDefinitionParameterValueOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f48d991ef4e0b25de372804b1bd192624169801ef60d555725284a87a82ec83)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4b997c6137c5b30dc828ca5ec7b2f87527ee5d8b53a9ccc69a4ea8d726a7f1ea)
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
            type_hints = typing.get_type_hints(_typecheckingstub__49fb5efee8b6201f6d307aec240a1f6135e97bff69f1bb66504085fbda51ea3b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatapipelinePipelineDefinitionParameterValue]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatapipelinePipelineDefinitionParameterValue]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatapipelinePipelineDefinitionParameterValue]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4242a122381f37056abb19150fa5979c297fd726b5519ed072e0b75748a01399)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DatapipelinePipelineDefinitionParameterValueOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.datapipelinePipelineDefinition.DatapipelinePipelineDefinitionParameterValueOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b4a8ed28af7af5106a857aa0d844809ea76c8c8adce1e92eef462d53da7d0854)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="stringValueInput")
    def string_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stringValueInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f3b9ba73d6d6d0ded396d74653f823af7ea361f282dddec04667a403e8818e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="stringValue")
    def string_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stringValue"))

    @string_value.setter
    def string_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37edf2ccf6e16e6ae12beb23366e2fc6894298a2573916c663ac9b17754b516b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stringValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DatapipelinePipelineDefinitionParameterValue, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DatapipelinePipelineDefinitionParameterValue, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DatapipelinePipelineDefinitionParameterValue, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09f8bfb4da552557a6deef8e264d2ece75c8323bbc2533fc6a896b30b018f64f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.datapipelinePipelineDefinition.DatapipelinePipelineDefinitionPipelineObject",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name", "field": "field"},
)
class DatapipelinePipelineDefinitionPipelineObject:
    def __init__(
        self,
        *,
        id: builtins.str,
        name: builtins.str,
        field: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DatapipelinePipelineDefinitionPipelineObjectField", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datapipeline_pipeline_definition#id DatapipelinePipelineDefinition#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datapipeline_pipeline_definition#name DatapipelinePipelineDefinition#name}.
        :param field: field block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datapipeline_pipeline_definition#field DatapipelinePipelineDefinition#field}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4575168a24b7ee29819cb1043b8619797469b29384bb1b11fb1d1a36897a8e8e)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument field", value=field, expected_type=type_hints["field"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "id": id,
            "name": name,
        }
        if field is not None:
            self._values["field"] = field

    @builtins.property
    def id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datapipeline_pipeline_definition#id DatapipelinePipelineDefinition#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datapipeline_pipeline_definition#name DatapipelinePipelineDefinition#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def field(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DatapipelinePipelineDefinitionPipelineObjectField"]]]:
        '''field block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datapipeline_pipeline_definition#field DatapipelinePipelineDefinition#field}
        '''
        result = self._values.get("field")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DatapipelinePipelineDefinitionPipelineObjectField"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatapipelinePipelineDefinitionPipelineObject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.datapipelinePipelineDefinition.DatapipelinePipelineDefinitionPipelineObjectField",
    jsii_struct_bases=[],
    name_mapping={
        "key": "key",
        "ref_value": "refValue",
        "string_value": "stringValue",
    },
)
class DatapipelinePipelineDefinitionPipelineObjectField:
    def __init__(
        self,
        *,
        key: builtins.str,
        ref_value: typing.Optional[builtins.str] = None,
        string_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datapipeline_pipeline_definition#key DatapipelinePipelineDefinition#key}.
        :param ref_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datapipeline_pipeline_definition#ref_value DatapipelinePipelineDefinition#ref_value}.
        :param string_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datapipeline_pipeline_definition#string_value DatapipelinePipelineDefinition#string_value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fcdfa3238bedde39856f9def4bc5355c3c4531a401f94ce721e9677604a8816)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument ref_value", value=ref_value, expected_type=type_hints["ref_value"])
            check_type(argname="argument string_value", value=string_value, expected_type=type_hints["string_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
        }
        if ref_value is not None:
            self._values["ref_value"] = ref_value
        if string_value is not None:
            self._values["string_value"] = string_value

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datapipeline_pipeline_definition#key DatapipelinePipelineDefinition#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ref_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datapipeline_pipeline_definition#ref_value DatapipelinePipelineDefinition#ref_value}.'''
        result = self._values.get("ref_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def string_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datapipeline_pipeline_definition#string_value DatapipelinePipelineDefinition#string_value}.'''
        result = self._values.get("string_value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatapipelinePipelineDefinitionPipelineObjectField(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatapipelinePipelineDefinitionPipelineObjectFieldList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.datapipelinePipelineDefinition.DatapipelinePipelineDefinitionPipelineObjectFieldList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ae1c810917ca8ed91cd26944103f8e24a49de9718ea7496d073cf0bfe3a84e66)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DatapipelinePipelineDefinitionPipelineObjectFieldOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__314351e036da80f749bb9f86748788c0f576102983940434a52a99ff70f63b71)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DatapipelinePipelineDefinitionPipelineObjectFieldOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a4de857b36878a855a8190ea0c98394a55d237c97e97cee700bb8348ba19ef4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__07d0a6ef37795ec937bf43a596ff633ca2a1370e28d6f3fe4b8d95eddc106a61)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0f5691c55faf77d2a7c7fe3c334716ca193a4064407bb9e9e3125c254a431e2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatapipelinePipelineDefinitionPipelineObjectField]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatapipelinePipelineDefinitionPipelineObjectField]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatapipelinePipelineDefinitionPipelineObjectField]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb8f612a6bfd5381b11dbadc0401bcfded0f380394eb2b7b18fe34d03ba0f1f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DatapipelinePipelineDefinitionPipelineObjectFieldOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.datapipelinePipelineDefinition.DatapipelinePipelineDefinitionPipelineObjectFieldOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f7b1ab8d0add8c8248d6261d3ea695ffb09bb1156ffe83cd997715bd37efde5a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetRefValue")
    def reset_ref_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRefValue", []))

    @jsii.member(jsii_name="resetStringValue")
    def reset_string_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStringValue", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="refValueInput")
    def ref_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "refValueInput"))

    @builtins.property
    @jsii.member(jsii_name="stringValueInput")
    def string_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stringValueInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9043d107c58c5df8934a430f0cbe84c538a2c50c5fa2625029511269facbf543)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="refValue")
    def ref_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "refValue"))

    @ref_value.setter
    def ref_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aac9976c8db4f18dd81da93baefc1b2c7d78606e6fd819321e4ad8f82fa54d02)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "refValue", value)

    @builtins.property
    @jsii.member(jsii_name="stringValue")
    def string_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stringValue"))

    @string_value.setter
    def string_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2efdaaf7800b1ac6d43de0b6aaf5e308e6e3e82b58c06cc9705449e4e3d49c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stringValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DatapipelinePipelineDefinitionPipelineObjectField, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DatapipelinePipelineDefinitionPipelineObjectField, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DatapipelinePipelineDefinitionPipelineObjectField, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac191419677951ba310e6d12c5064ebec1450b83337b873770596882d6ec4bf9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DatapipelinePipelineDefinitionPipelineObjectList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.datapipelinePipelineDefinition.DatapipelinePipelineDefinitionPipelineObjectList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__377708101cc8bb06953eb78d6b7809ebdd5dc0ec69e4c021abc359af7631425d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DatapipelinePipelineDefinitionPipelineObjectOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e41d8cdbddd461a9c41386160a83aaf6200351f42eaf6d5bde7d7341f0bcc08)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DatapipelinePipelineDefinitionPipelineObjectOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9a7818273ee9ef9a326830be00c5828a837832468a4f998e259fb7726ecb817)
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
            type_hints = typing.get_type_hints(_typecheckingstub__32e4b9789a87b2cf3e2bb715b38033f293d682671a9d71c2721ec1057ddfaf10)
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
            type_hints = typing.get_type_hints(_typecheckingstub__dc1704a4308fccc4d29671a3abf9a32a5d53f222e5167951c87007836151f273)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatapipelinePipelineDefinitionPipelineObject]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatapipelinePipelineDefinitionPipelineObject]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatapipelinePipelineDefinitionPipelineObject]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d6689bb57bf9a02393b9e98b8c234e7de11c14aaef58d39302d564c0938bebb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DatapipelinePipelineDefinitionPipelineObjectOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.datapipelinePipelineDefinition.DatapipelinePipelineDefinitionPipelineObjectOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ce0cc31e06eab6076a103f7601ab6159448d99db01e25ed4446fa5a74efb318a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putField")
    def put_field(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DatapipelinePipelineDefinitionPipelineObjectField, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__656cc35ca8ddeb7ba82df8bdb4a13cf394e92f5282ed810a2b12b6a6a887c9e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putField", [value]))

    @jsii.member(jsii_name="resetField")
    def reset_field(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetField", []))

    @builtins.property
    @jsii.member(jsii_name="field")
    def field(self) -> DatapipelinePipelineDefinitionPipelineObjectFieldList:
        return typing.cast(DatapipelinePipelineDefinitionPipelineObjectFieldList, jsii.get(self, "field"))

    @builtins.property
    @jsii.member(jsii_name="fieldInput")
    def field_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatapipelinePipelineDefinitionPipelineObjectField]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatapipelinePipelineDefinitionPipelineObjectField]]], jsii.get(self, "fieldInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__3572e5f13b38ac3df1c303be8b909aefc48d371dc24b4eca6097e6727215cdf1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9da754e0cf9bb13be73abf01418ac0775ba1863f060db5b15d59ee09d20951d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DatapipelinePipelineDefinitionPipelineObject, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DatapipelinePipelineDefinitionPipelineObject, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DatapipelinePipelineDefinitionPipelineObject, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0eb31e54748c08a027f28f521969724fb8154d5e634472863650a5d3c6bbdb46)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DatapipelinePipelineDefinition",
    "DatapipelinePipelineDefinitionConfig",
    "DatapipelinePipelineDefinitionParameterObject",
    "DatapipelinePipelineDefinitionParameterObjectAttribute",
    "DatapipelinePipelineDefinitionParameterObjectAttributeList",
    "DatapipelinePipelineDefinitionParameterObjectAttributeOutputReference",
    "DatapipelinePipelineDefinitionParameterObjectList",
    "DatapipelinePipelineDefinitionParameterObjectOutputReference",
    "DatapipelinePipelineDefinitionParameterValue",
    "DatapipelinePipelineDefinitionParameterValueList",
    "DatapipelinePipelineDefinitionParameterValueOutputReference",
    "DatapipelinePipelineDefinitionPipelineObject",
    "DatapipelinePipelineDefinitionPipelineObjectField",
    "DatapipelinePipelineDefinitionPipelineObjectFieldList",
    "DatapipelinePipelineDefinitionPipelineObjectFieldOutputReference",
    "DatapipelinePipelineDefinitionPipelineObjectList",
    "DatapipelinePipelineDefinitionPipelineObjectOutputReference",
]

publication.publish()

def _typecheckingstub__1d95d62c42224b9947ff5a8a34bd22d819c814d687a4dab917ec6af6888748fd(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    pipeline_id: builtins.str,
    pipeline_object: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DatapipelinePipelineDefinitionPipelineObject, typing.Dict[builtins.str, typing.Any]]]],
    id: typing.Optional[builtins.str] = None,
    parameter_object: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DatapipelinePipelineDefinitionParameterObject, typing.Dict[builtins.str, typing.Any]]]]] = None,
    parameter_value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DatapipelinePipelineDefinitionParameterValue, typing.Dict[builtins.str, typing.Any]]]]] = None,
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

def _typecheckingstub__b511dab153f935723046678be65399c21b16208bcd0b3559ba7556832906855e(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DatapipelinePipelineDefinitionParameterObject, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca6efad9cb199020891810704c76807a572ece68b18cff0da0b9b063f7ab13a1(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DatapipelinePipelineDefinitionParameterValue, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27522ab7c42fe15e8b8591bb47a5119c6e5b3f4288b68243548cdf3e3e6bc9cc(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DatapipelinePipelineDefinitionPipelineObject, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32e758d6d453fb4f46edee2b10f72b970fb57e8cd68fdfc0acdd01378a491a21(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__158527d197f8a3737e14cca5a73dda338fb584a3e0fbbf844ec8119c6fecc4e0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d5a12a080ef17325c5a28764b8b74cfbe04dfb2b7bdb7f8ea71a5fee785a978(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    pipeline_id: builtins.str,
    pipeline_object: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DatapipelinePipelineDefinitionPipelineObject, typing.Dict[builtins.str, typing.Any]]]],
    id: typing.Optional[builtins.str] = None,
    parameter_object: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DatapipelinePipelineDefinitionParameterObject, typing.Dict[builtins.str, typing.Any]]]]] = None,
    parameter_value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DatapipelinePipelineDefinitionParameterValue, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6643680fc2bc478fc6fd7b70058c2b2bb4915458ae8c30cfadcf9d9105161bb(
    *,
    id: builtins.str,
    attribute: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DatapipelinePipelineDefinitionParameterObjectAttribute, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bdc91c8d68757285baf5d040c9b0029c9e17083405d062afd2aeae36c62f536(
    *,
    key: builtins.str,
    string_value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed44702f997c91689fd958ee0aa33bd48a83e0671e8239089ae34d12a3406fdf(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__852d08212824cd64191ccce6f9464226a8084fb77cf30b30b2160b4566446862(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9248e4d1c89deae9ee69da9dfaa21912f2d366a7b66dbbe1e551438290dea92c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__710311afd653ee97bfd9d1b3739d6e02676c433ed6297118a2d87d5cd9fc470b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c115d99df2f761b4ef11713f782d79a5ab9a5ccc41c715c75ef1e94e0af8c0d4(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a28c1f00a1f00d80e5c905587e9ff8794a946e6f5cad81367064c0732bfa83b6(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatapipelinePipelineDefinitionParameterObjectAttribute]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ed1bce6d4e3b2042ec2f987e69f7369175dce2d9a12007e90f8821464b2853f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42a47b5cb5cc33cd47a4176ad46e8a3d38ec9f7f75e30e5e0be44159cc381f2a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e152455990f1294523da1ca2115914e64ab1f66c5dd411bdf1fc0e61865df41(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b80f10e4d32e7a8c9a2837c7a4d2274aa503d367204991ab498802fb72638f8f(
    value: typing.Optional[typing.Union[DatapipelinePipelineDefinitionParameterObjectAttribute, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbecdbb29838f1957a3af738b802267f29ec725fa920878489bbb3a1025ff26f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b70292fe87cb27f06d5dc00c8ac7fa093e588685d1c61f9fe9584ae1c9f9fa5(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0eb845dcd8bda1bd814a73f39501f94c417886ae51475c9a983be482b009c5fa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eed4cb924c97557c0039fd09ba493f326ecce2edbec68ac3a511edf2a95bcb27(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__315029d4a945cfbad7747ce338da20193f02360d9be7cd959d4ae53fc8cf49c9(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8557fe2d9a32f3274135bcee8dbf4f7e04520c5e5c895fcba86da0e59124bc21(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatapipelinePipelineDefinitionParameterObject]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a116978a64cd0e2bca3dbefccdffbf05f845162447ccd8cc671843e51854a798(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2190894ac637c61f794e6da5f975f72ebadcab16e7bf99c00b0ef956f0c2c81(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DatapipelinePipelineDefinitionParameterObjectAttribute, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1d5485bf717f36f0df69c51d07c91cb5223d79ac2f62e4f30aed18f74262db8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07f826004be5b52caf9cc7867fd4d41e7388451321fc628c245208b5130d97ba(
    value: typing.Optional[typing.Union[DatapipelinePipelineDefinitionParameterObject, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a60fafc7c4c8d9020f10f745741fef3fd0d24813c1f3d1e8fdf74f55a126d2b(
    *,
    id: builtins.str,
    string_value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be09de2b95141462d89a9b1add984194121e0a82bd5c5decb1a8843eac2ae91e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__174fd90a79333ac3d4396a20d2e6ce7b5876a8b0441f4cdaaf6db9ef52439cd7(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f48d991ef4e0b25de372804b1bd192624169801ef60d555725284a87a82ec83(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b997c6137c5b30dc828ca5ec7b2f87527ee5d8b53a9ccc69a4ea8d726a7f1ea(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49fb5efee8b6201f6d307aec240a1f6135e97bff69f1bb66504085fbda51ea3b(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4242a122381f37056abb19150fa5979c297fd726b5519ed072e0b75748a01399(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatapipelinePipelineDefinitionParameterValue]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4a8ed28af7af5106a857aa0d844809ea76c8c8adce1e92eef462d53da7d0854(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f3b9ba73d6d6d0ded396d74653f823af7ea361f282dddec04667a403e8818e3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37edf2ccf6e16e6ae12beb23366e2fc6894298a2573916c663ac9b17754b516b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09f8bfb4da552557a6deef8e264d2ece75c8323bbc2533fc6a896b30b018f64f(
    value: typing.Optional[typing.Union[DatapipelinePipelineDefinitionParameterValue, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4575168a24b7ee29819cb1043b8619797469b29384bb1b11fb1d1a36897a8e8e(
    *,
    id: builtins.str,
    name: builtins.str,
    field: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DatapipelinePipelineDefinitionPipelineObjectField, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fcdfa3238bedde39856f9def4bc5355c3c4531a401f94ce721e9677604a8816(
    *,
    key: builtins.str,
    ref_value: typing.Optional[builtins.str] = None,
    string_value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae1c810917ca8ed91cd26944103f8e24a49de9718ea7496d073cf0bfe3a84e66(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__314351e036da80f749bb9f86748788c0f576102983940434a52a99ff70f63b71(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a4de857b36878a855a8190ea0c98394a55d237c97e97cee700bb8348ba19ef4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07d0a6ef37795ec937bf43a596ff633ca2a1370e28d6f3fe4b8d95eddc106a61(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f5691c55faf77d2a7c7fe3c334716ca193a4064407bb9e9e3125c254a431e2d(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb8f612a6bfd5381b11dbadc0401bcfded0f380394eb2b7b18fe34d03ba0f1f3(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatapipelinePipelineDefinitionPipelineObjectField]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7b1ab8d0add8c8248d6261d3ea695ffb09bb1156ffe83cd997715bd37efde5a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9043d107c58c5df8934a430f0cbe84c538a2c50c5fa2625029511269facbf543(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aac9976c8db4f18dd81da93baefc1b2c7d78606e6fd819321e4ad8f82fa54d02(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2efdaaf7800b1ac6d43de0b6aaf5e308e6e3e82b58c06cc9705449e4e3d49c1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac191419677951ba310e6d12c5064ebec1450b83337b873770596882d6ec4bf9(
    value: typing.Optional[typing.Union[DatapipelinePipelineDefinitionPipelineObjectField, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__377708101cc8bb06953eb78d6b7809ebdd5dc0ec69e4c021abc359af7631425d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e41d8cdbddd461a9c41386160a83aaf6200351f42eaf6d5bde7d7341f0bcc08(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9a7818273ee9ef9a326830be00c5828a837832468a4f998e259fb7726ecb817(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32e4b9789a87b2cf3e2bb715b38033f293d682671a9d71c2721ec1057ddfaf10(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc1704a4308fccc4d29671a3abf9a32a5d53f222e5167951c87007836151f273(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d6689bb57bf9a02393b9e98b8c234e7de11c14aaef58d39302d564c0938bebb(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatapipelinePipelineDefinitionPipelineObject]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce0cc31e06eab6076a103f7601ab6159448d99db01e25ed4446fa5a74efb318a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__656cc35ca8ddeb7ba82df8bdb4a13cf394e92f5282ed810a2b12b6a6a887c9e5(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DatapipelinePipelineDefinitionPipelineObjectField, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3572e5f13b38ac3df1c303be8b909aefc48d371dc24b4eca6097e6727215cdf1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9da754e0cf9bb13be73abf01418ac0775ba1863f060db5b15d59ee09d20951d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0eb31e54748c08a027f28f521969724fb8154d5e634472863650a5d3c6bbdb46(
    value: typing.Optional[typing.Union[DatapipelinePipelineDefinitionPipelineObject, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
