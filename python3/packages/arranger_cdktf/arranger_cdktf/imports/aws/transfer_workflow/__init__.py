'''
# `aws_transfer_workflow`

Refer to the Terraform Registory for docs: [`aws_transfer_workflow`](https://www.terraform.io/docs/providers/aws/r/transfer_workflow).
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


class TransferWorkflow(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.transferWorkflow.TransferWorkflow",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow aws_transfer_workflow}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        steps: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["TransferWorkflowSteps", typing.Dict[builtins.str, typing.Any]]]],
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        on_exception_steps: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["TransferWorkflowOnExceptionSteps", typing.Dict[builtins.str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow aws_transfer_workflow} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param steps: steps block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#steps TransferWorkflow#steps}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#description TransferWorkflow#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#id TransferWorkflow#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param on_exception_steps: on_exception_steps block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#on_exception_steps TransferWorkflow#on_exception_steps}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#tags TransferWorkflow#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#tags_all TransferWorkflow#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9d6f2b7bb4a7359f88f1dbf67426a4056cb2e5034a88d1349419a4157b3eb27)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = TransferWorkflowConfig(
            steps=steps,
            description=description,
            id=id,
            on_exception_steps=on_exception_steps,
            tags=tags,
            tags_all=tags_all,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putOnExceptionSteps")
    def put_on_exception_steps(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["TransferWorkflowOnExceptionSteps", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcd93dc63c4035a3281cd70a08164036c7bc8055fb7be04cd6a571402f28c91c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOnExceptionSteps", [value]))

    @jsii.member(jsii_name="putSteps")
    def put_steps(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["TransferWorkflowSteps", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93ce3f271f88390eb14459830eda0e030d308f0ac059857f677fa5eb1fc2ecdf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSteps", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetOnExceptionSteps")
    def reset_on_exception_steps(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnExceptionSteps", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

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
    @jsii.member(jsii_name="onExceptionSteps")
    def on_exception_steps(self) -> "TransferWorkflowOnExceptionStepsList":
        return typing.cast("TransferWorkflowOnExceptionStepsList", jsii.get(self, "onExceptionSteps"))

    @builtins.property
    @jsii.member(jsii_name="steps")
    def steps(self) -> "TransferWorkflowStepsList":
        return typing.cast("TransferWorkflowStepsList", jsii.get(self, "steps"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="onExceptionStepsInput")
    def on_exception_steps_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["TransferWorkflowOnExceptionSteps"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["TransferWorkflowOnExceptionSteps"]]], jsii.get(self, "onExceptionStepsInput"))

    @builtins.property
    @jsii.member(jsii_name="stepsInput")
    def steps_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["TransferWorkflowSteps"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["TransferWorkflowSteps"]]], jsii.get(self, "stepsInput"))

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
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b7b4df8f2bbc915a6ada34299c9476118e5b579f7aebdc7013fff36039889f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02eddb6decd435dd7920687ad9981873f6f164ce541d55bd6c990d5b184d7240)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3e900035fb0487af3dc3cca5e6a4839ebace1079617d2b6467f1fa6b137c260)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bce9f7ede8ded0ecb927a108247df06cfaba92f25dbe1576cd27f2b9ac1f1963)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.transferWorkflow.TransferWorkflowConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "steps": "steps",
        "description": "description",
        "id": "id",
        "on_exception_steps": "onExceptionSteps",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class TransferWorkflowConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        steps: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["TransferWorkflowSteps", typing.Dict[builtins.str, typing.Any]]]],
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        on_exception_steps: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["TransferWorkflowOnExceptionSteps", typing.Dict[builtins.str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param steps: steps block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#steps TransferWorkflow#steps}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#description TransferWorkflow#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#id TransferWorkflow#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param on_exception_steps: on_exception_steps block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#on_exception_steps TransferWorkflow#on_exception_steps}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#tags TransferWorkflow#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#tags_all TransferWorkflow#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6332750adf44b05132732f9264f73724387af4a0006169f3077f9e5c02e16c88)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument steps", value=steps, expected_type=type_hints["steps"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument on_exception_steps", value=on_exception_steps, expected_type=type_hints["on_exception_steps"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "steps": steps,
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
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if on_exception_steps is not None:
            self._values["on_exception_steps"] = on_exception_steps
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all

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
    def steps(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["TransferWorkflowSteps"]]:
        '''steps block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#steps TransferWorkflow#steps}
        '''
        result = self._values.get("steps")
        assert result is not None, "Required property 'steps' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["TransferWorkflowSteps"]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#description TransferWorkflow#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#id TransferWorkflow#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def on_exception_steps(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["TransferWorkflowOnExceptionSteps"]]]:
        '''on_exception_steps block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#on_exception_steps TransferWorkflow#on_exception_steps}
        '''
        result = self._values.get("on_exception_steps")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["TransferWorkflowOnExceptionSteps"]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#tags TransferWorkflow#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#tags_all TransferWorkflow#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransferWorkflowConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.transferWorkflow.TransferWorkflowOnExceptionSteps",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "copy_step_details": "copyStepDetails",
        "custom_step_details": "customStepDetails",
        "delete_step_details": "deleteStepDetails",
        "tag_step_details": "tagStepDetails",
    },
)
class TransferWorkflowOnExceptionSteps:
    def __init__(
        self,
        *,
        type: builtins.str,
        copy_step_details: typing.Optional[typing.Union["TransferWorkflowOnExceptionStepsCopyStepDetails", typing.Dict[builtins.str, typing.Any]]] = None,
        custom_step_details: typing.Optional[typing.Union["TransferWorkflowOnExceptionStepsCustomStepDetails", typing.Dict[builtins.str, typing.Any]]] = None,
        delete_step_details: typing.Optional[typing.Union["TransferWorkflowOnExceptionStepsDeleteStepDetails", typing.Dict[builtins.str, typing.Any]]] = None,
        tag_step_details: typing.Optional[typing.Union["TransferWorkflowOnExceptionStepsTagStepDetails", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#type TransferWorkflow#type}.
        :param copy_step_details: copy_step_details block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#copy_step_details TransferWorkflow#copy_step_details}
        :param custom_step_details: custom_step_details block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#custom_step_details TransferWorkflow#custom_step_details}
        :param delete_step_details: delete_step_details block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#delete_step_details TransferWorkflow#delete_step_details}
        :param tag_step_details: tag_step_details block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#tag_step_details TransferWorkflow#tag_step_details}
        '''
        if isinstance(copy_step_details, dict):
            copy_step_details = TransferWorkflowOnExceptionStepsCopyStepDetails(**copy_step_details)
        if isinstance(custom_step_details, dict):
            custom_step_details = TransferWorkflowOnExceptionStepsCustomStepDetails(**custom_step_details)
        if isinstance(delete_step_details, dict):
            delete_step_details = TransferWorkflowOnExceptionStepsDeleteStepDetails(**delete_step_details)
        if isinstance(tag_step_details, dict):
            tag_step_details = TransferWorkflowOnExceptionStepsTagStepDetails(**tag_step_details)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c6b846e517f707976208e684304ca77d0f37021253b4e003ba3dbc61dc0c38b)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument copy_step_details", value=copy_step_details, expected_type=type_hints["copy_step_details"])
            check_type(argname="argument custom_step_details", value=custom_step_details, expected_type=type_hints["custom_step_details"])
            check_type(argname="argument delete_step_details", value=delete_step_details, expected_type=type_hints["delete_step_details"])
            check_type(argname="argument tag_step_details", value=tag_step_details, expected_type=type_hints["tag_step_details"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if copy_step_details is not None:
            self._values["copy_step_details"] = copy_step_details
        if custom_step_details is not None:
            self._values["custom_step_details"] = custom_step_details
        if delete_step_details is not None:
            self._values["delete_step_details"] = delete_step_details
        if tag_step_details is not None:
            self._values["tag_step_details"] = tag_step_details

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#type TransferWorkflow#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def copy_step_details(
        self,
    ) -> typing.Optional["TransferWorkflowOnExceptionStepsCopyStepDetails"]:
        '''copy_step_details block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#copy_step_details TransferWorkflow#copy_step_details}
        '''
        result = self._values.get("copy_step_details")
        return typing.cast(typing.Optional["TransferWorkflowOnExceptionStepsCopyStepDetails"], result)

    @builtins.property
    def custom_step_details(
        self,
    ) -> typing.Optional["TransferWorkflowOnExceptionStepsCustomStepDetails"]:
        '''custom_step_details block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#custom_step_details TransferWorkflow#custom_step_details}
        '''
        result = self._values.get("custom_step_details")
        return typing.cast(typing.Optional["TransferWorkflowOnExceptionStepsCustomStepDetails"], result)

    @builtins.property
    def delete_step_details(
        self,
    ) -> typing.Optional["TransferWorkflowOnExceptionStepsDeleteStepDetails"]:
        '''delete_step_details block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#delete_step_details TransferWorkflow#delete_step_details}
        '''
        result = self._values.get("delete_step_details")
        return typing.cast(typing.Optional["TransferWorkflowOnExceptionStepsDeleteStepDetails"], result)

    @builtins.property
    def tag_step_details(
        self,
    ) -> typing.Optional["TransferWorkflowOnExceptionStepsTagStepDetails"]:
        '''tag_step_details block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#tag_step_details TransferWorkflow#tag_step_details}
        '''
        result = self._values.get("tag_step_details")
        return typing.cast(typing.Optional["TransferWorkflowOnExceptionStepsTagStepDetails"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransferWorkflowOnExceptionSteps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.transferWorkflow.TransferWorkflowOnExceptionStepsCopyStepDetails",
    jsii_struct_bases=[],
    name_mapping={
        "destination_file_location": "destinationFileLocation",
        "name": "name",
        "overwrite_existing": "overwriteExisting",
        "source_file_location": "sourceFileLocation",
    },
)
class TransferWorkflowOnExceptionStepsCopyStepDetails:
    def __init__(
        self,
        *,
        destination_file_location: typing.Optional[typing.Union["TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocation", typing.Dict[builtins.str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
        overwrite_existing: typing.Optional[builtins.str] = None,
        source_file_location: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param destination_file_location: destination_file_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#destination_file_location TransferWorkflow#destination_file_location}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#name TransferWorkflow#name}.
        :param overwrite_existing: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#overwrite_existing TransferWorkflow#overwrite_existing}.
        :param source_file_location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#source_file_location TransferWorkflow#source_file_location}.
        '''
        if isinstance(destination_file_location, dict):
            destination_file_location = TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocation(**destination_file_location)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b096881d5a19b8b9f3907e362b62da865072e439d517194594624189bfea583)
            check_type(argname="argument destination_file_location", value=destination_file_location, expected_type=type_hints["destination_file_location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument overwrite_existing", value=overwrite_existing, expected_type=type_hints["overwrite_existing"])
            check_type(argname="argument source_file_location", value=source_file_location, expected_type=type_hints["source_file_location"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if destination_file_location is not None:
            self._values["destination_file_location"] = destination_file_location
        if name is not None:
            self._values["name"] = name
        if overwrite_existing is not None:
            self._values["overwrite_existing"] = overwrite_existing
        if source_file_location is not None:
            self._values["source_file_location"] = source_file_location

    @builtins.property
    def destination_file_location(
        self,
    ) -> typing.Optional["TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocation"]:
        '''destination_file_location block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#destination_file_location TransferWorkflow#destination_file_location}
        '''
        result = self._values.get("destination_file_location")
        return typing.cast(typing.Optional["TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocation"], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#name TransferWorkflow#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def overwrite_existing(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#overwrite_existing TransferWorkflow#overwrite_existing}.'''
        result = self._values.get("overwrite_existing")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_file_location(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#source_file_location TransferWorkflow#source_file_location}.'''
        result = self._values.get("source_file_location")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransferWorkflowOnExceptionStepsCopyStepDetails(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.transferWorkflow.TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocation",
    jsii_struct_bases=[],
    name_mapping={
        "efs_file_location": "efsFileLocation",
        "s3_file_location": "s3FileLocation",
    },
)
class TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocation:
    def __init__(
        self,
        *,
        efs_file_location: typing.Optional[typing.Union["TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationEfsFileLocation", typing.Dict[builtins.str, typing.Any]]] = None,
        s3_file_location: typing.Optional[typing.Union["TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationS3FileLocation", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param efs_file_location: efs_file_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#efs_file_location TransferWorkflow#efs_file_location}
        :param s3_file_location: s3_file_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#s3_file_location TransferWorkflow#s3_file_location}
        '''
        if isinstance(efs_file_location, dict):
            efs_file_location = TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationEfsFileLocation(**efs_file_location)
        if isinstance(s3_file_location, dict):
            s3_file_location = TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationS3FileLocation(**s3_file_location)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a515a239a9f90c0dab3da8ff16d5c676c42d9d6c2b2eda48269402fcf237611)
            check_type(argname="argument efs_file_location", value=efs_file_location, expected_type=type_hints["efs_file_location"])
            check_type(argname="argument s3_file_location", value=s3_file_location, expected_type=type_hints["s3_file_location"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if efs_file_location is not None:
            self._values["efs_file_location"] = efs_file_location
        if s3_file_location is not None:
            self._values["s3_file_location"] = s3_file_location

    @builtins.property
    def efs_file_location(
        self,
    ) -> typing.Optional["TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationEfsFileLocation"]:
        '''efs_file_location block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#efs_file_location TransferWorkflow#efs_file_location}
        '''
        result = self._values.get("efs_file_location")
        return typing.cast(typing.Optional["TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationEfsFileLocation"], result)

    @builtins.property
    def s3_file_location(
        self,
    ) -> typing.Optional["TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationS3FileLocation"]:
        '''s3_file_location block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#s3_file_location TransferWorkflow#s3_file_location}
        '''
        result = self._values.get("s3_file_location")
        return typing.cast(typing.Optional["TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationS3FileLocation"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.transferWorkflow.TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationEfsFileLocation",
    jsii_struct_bases=[],
    name_mapping={"file_system_id": "fileSystemId", "path": "path"},
)
class TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationEfsFileLocation:
    def __init__(
        self,
        *,
        file_system_id: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param file_system_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#file_system_id TransferWorkflow#file_system_id}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#path TransferWorkflow#path}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f90100ddd528701a40bc2b013a02d2d625ef65c6f25eaeade82e5ee30ae4a15)
            check_type(argname="argument file_system_id", value=file_system_id, expected_type=type_hints["file_system_id"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if file_system_id is not None:
            self._values["file_system_id"] = file_system_id
        if path is not None:
            self._values["path"] = path

    @builtins.property
    def file_system_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#file_system_id TransferWorkflow#file_system_id}.'''
        result = self._values.get("file_system_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#path TransferWorkflow#path}.'''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationEfsFileLocation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationEfsFileLocationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.transferWorkflow.TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationEfsFileLocationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3ba6391517ca527a27dcff93da12537c841258660d51e68dd81c039a4986948d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFileSystemId")
    def reset_file_system_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileSystemId", []))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @builtins.property
    @jsii.member(jsii_name="fileSystemIdInput")
    def file_system_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileSystemIdInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="fileSystemId")
    def file_system_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileSystemId"))

    @file_system_id.setter
    def file_system_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__166b944fca393b1a94ecde768653b26db7ea9e03eed35f9700f0252d1f8a4f26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileSystemId", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2615a87faabe0c0ce84302b979d1845b4562ebebc9daa1468a18c6221d2a04be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationEfsFileLocation]:
        return typing.cast(typing.Optional[TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationEfsFileLocation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationEfsFileLocation],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67cfb0ecfa1dc9da1c15f2eb3c471d9440d602f5186ca7af03b320bd214747ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.transferWorkflow.TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9abd82c4e1e77c1c3453501df6f6dacb036c000eeabdcc51fde5f8c70ce6e6ec)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putEfsFileLocation")
    def put_efs_file_location(
        self,
        *,
        file_system_id: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param file_system_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#file_system_id TransferWorkflow#file_system_id}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#path TransferWorkflow#path}.
        '''
        value = TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationEfsFileLocation(
            file_system_id=file_system_id, path=path
        )

        return typing.cast(None, jsii.invoke(self, "putEfsFileLocation", [value]))

    @jsii.member(jsii_name="putS3FileLocation")
    def put_s3_file_location(
        self,
        *,
        bucket: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#bucket TransferWorkflow#bucket}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#key TransferWorkflow#key}.
        '''
        value = TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationS3FileLocation(
            bucket=bucket, key=key
        )

        return typing.cast(None, jsii.invoke(self, "putS3FileLocation", [value]))

    @jsii.member(jsii_name="resetEfsFileLocation")
    def reset_efs_file_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEfsFileLocation", []))

    @jsii.member(jsii_name="resetS3FileLocation")
    def reset_s3_file_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3FileLocation", []))

    @builtins.property
    @jsii.member(jsii_name="efsFileLocation")
    def efs_file_location(
        self,
    ) -> TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationEfsFileLocationOutputReference:
        return typing.cast(TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationEfsFileLocationOutputReference, jsii.get(self, "efsFileLocation"))

    @builtins.property
    @jsii.member(jsii_name="s3FileLocation")
    def s3_file_location(
        self,
    ) -> "TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationS3FileLocationOutputReference":
        return typing.cast("TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationS3FileLocationOutputReference", jsii.get(self, "s3FileLocation"))

    @builtins.property
    @jsii.member(jsii_name="efsFileLocationInput")
    def efs_file_location_input(
        self,
    ) -> typing.Optional[TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationEfsFileLocation]:
        return typing.cast(typing.Optional[TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationEfsFileLocation], jsii.get(self, "efsFileLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="s3FileLocationInput")
    def s3_file_location_input(
        self,
    ) -> typing.Optional["TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationS3FileLocation"]:
        return typing.cast(typing.Optional["TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationS3FileLocation"], jsii.get(self, "s3FileLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocation]:
        return typing.cast(typing.Optional[TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocation],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c45565b963bae7d2e21e100949ccc28ada96ab6848e8321c23755c4f261ba34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.transferWorkflow.TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationS3FileLocation",
    jsii_struct_bases=[],
    name_mapping={"bucket": "bucket", "key": "key"},
)
class TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationS3FileLocation:
    def __init__(
        self,
        *,
        bucket: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#bucket TransferWorkflow#bucket}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#key TransferWorkflow#key}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4364cb35a90e5fa7bf2266f57f196783d47b5e64617ec54efeefcf57e31e29ee)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if bucket is not None:
            self._values["bucket"] = bucket
        if key is not None:
            self._values["key"] = key

    @builtins.property
    def bucket(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#bucket TransferWorkflow#bucket}.'''
        result = self._values.get("bucket")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#key TransferWorkflow#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationS3FileLocation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationS3FileLocationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.transferWorkflow.TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationS3FileLocationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3ac18357aeb4231dab1013984523b25e7e686e72e2b97a574706ccc7f08be08d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBucket")
    def reset_bucket(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucket", []))

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @builtins.property
    @jsii.member(jsii_name="bucketInput")
    def bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67a001d03f3d6b06a3176fb490bceb76ef033359bd59fa45c378e293a0bd58f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucket", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1de486f3e5a50e1097d4122585174e83d189703fd89d7af7576dcbc38a7ecde1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationS3FileLocation]:
        return typing.cast(typing.Optional[TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationS3FileLocation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationS3FileLocation],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__665bf568d496e5efcbb732f709b973d5fb4e5f19a14146cbbc80ef9ab71d3400)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class TransferWorkflowOnExceptionStepsCopyStepDetailsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.transferWorkflow.TransferWorkflowOnExceptionStepsCopyStepDetailsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0b313645f29d00c686b5ecad84bf0fcee9d3847c957efe67bddec3f3df7c6cf8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDestinationFileLocation")
    def put_destination_file_location(
        self,
        *,
        efs_file_location: typing.Optional[typing.Union[TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationEfsFileLocation, typing.Dict[builtins.str, typing.Any]]] = None,
        s3_file_location: typing.Optional[typing.Union[TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationS3FileLocation, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param efs_file_location: efs_file_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#efs_file_location TransferWorkflow#efs_file_location}
        :param s3_file_location: s3_file_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#s3_file_location TransferWorkflow#s3_file_location}
        '''
        value = TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocation(
            efs_file_location=efs_file_location, s3_file_location=s3_file_location
        )

        return typing.cast(None, jsii.invoke(self, "putDestinationFileLocation", [value]))

    @jsii.member(jsii_name="resetDestinationFileLocation")
    def reset_destination_file_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationFileLocation", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetOverwriteExisting")
    def reset_overwrite_existing(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOverwriteExisting", []))

    @jsii.member(jsii_name="resetSourceFileLocation")
    def reset_source_file_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceFileLocation", []))

    @builtins.property
    @jsii.member(jsii_name="destinationFileLocation")
    def destination_file_location(
        self,
    ) -> TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationOutputReference:
        return typing.cast(TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationOutputReference, jsii.get(self, "destinationFileLocation"))

    @builtins.property
    @jsii.member(jsii_name="destinationFileLocationInput")
    def destination_file_location_input(
        self,
    ) -> typing.Optional[TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocation]:
        return typing.cast(typing.Optional[TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocation], jsii.get(self, "destinationFileLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="overwriteExistingInput")
    def overwrite_existing_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "overwriteExistingInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceFileLocationInput")
    def source_file_location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceFileLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2a766ea155d4c3f2ed1da773b5f7525cda06c2f003105999c9331d2e2ac86ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="overwriteExisting")
    def overwrite_existing(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "overwriteExisting"))

    @overwrite_existing.setter
    def overwrite_existing(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4966a6820922a7ea3971910341d1b6f6d6e65bcab9fc9fea6a8ed0f6b312d5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "overwriteExisting", value)

    @builtins.property
    @jsii.member(jsii_name="sourceFileLocation")
    def source_file_location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceFileLocation"))

    @source_file_location.setter
    def source_file_location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf4b736bbbd05f539db1037b9bbc9ed9e9398b0e23d73600a449d526e6ea2029)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceFileLocation", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[TransferWorkflowOnExceptionStepsCopyStepDetails]:
        return typing.cast(typing.Optional[TransferWorkflowOnExceptionStepsCopyStepDetails], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[TransferWorkflowOnExceptionStepsCopyStepDetails],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6693bcc674bedff9f1df08dc505098d68d27c0d6eebb62d12e29bf42e641319)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.transferWorkflow.TransferWorkflowOnExceptionStepsCustomStepDetails",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "source_file_location": "sourceFileLocation",
        "target": "target",
        "timeout_seconds": "timeoutSeconds",
    },
)
class TransferWorkflowOnExceptionStepsCustomStepDetails:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        source_file_location: typing.Optional[builtins.str] = None,
        target: typing.Optional[builtins.str] = None,
        timeout_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#name TransferWorkflow#name}.
        :param source_file_location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#source_file_location TransferWorkflow#source_file_location}.
        :param target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#target TransferWorkflow#target}.
        :param timeout_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#timeout_seconds TransferWorkflow#timeout_seconds}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__395fea0fc841dfe6272d9720466b4e5fe0278736499fe9396af569ce98374bb6)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument source_file_location", value=source_file_location, expected_type=type_hints["source_file_location"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument timeout_seconds", value=timeout_seconds, expected_type=type_hints["timeout_seconds"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if source_file_location is not None:
            self._values["source_file_location"] = source_file_location
        if target is not None:
            self._values["target"] = target
        if timeout_seconds is not None:
            self._values["timeout_seconds"] = timeout_seconds

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#name TransferWorkflow#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_file_location(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#source_file_location TransferWorkflow#source_file_location}.'''
        result = self._values.get("source_file_location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#target TransferWorkflow#target}.'''
        result = self._values.get("target")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeout_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#timeout_seconds TransferWorkflow#timeout_seconds}.'''
        result = self._values.get("timeout_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransferWorkflowOnExceptionStepsCustomStepDetails(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TransferWorkflowOnExceptionStepsCustomStepDetailsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.transferWorkflow.TransferWorkflowOnExceptionStepsCustomStepDetailsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1114eee3c3bd19260804673733354abb57d47ccaf36acabb14aebd50ed6de1c6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetSourceFileLocation")
    def reset_source_file_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceFileLocation", []))

    @jsii.member(jsii_name="resetTarget")
    def reset_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTarget", []))

    @jsii.member(jsii_name="resetTimeoutSeconds")
    def reset_timeout_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeoutSeconds", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceFileLocationInput")
    def source_file_location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceFileLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutSecondsInput")
    def timeout_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__276e11a87b4b21ebd4ae8ca0f63dda4d9233045cae3829006910a645f9a5316f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="sourceFileLocation")
    def source_file_location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceFileLocation"))

    @source_file_location.setter
    def source_file_location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f7aa46ed4c5fa695679f7789c0a71fa36a499f86a312e81c44cfc4447decc43)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceFileLocation", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afc366d3fc1bf39845245da0a08f4c34843c97a6bcfefb249b12fb38ccb70728)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="timeoutSeconds")
    def timeout_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeoutSeconds"))

    @timeout_seconds.setter
    def timeout_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e0785b1f4833413ea215aba1abd731d7b31eca628c3d449c20d64e2252aca96)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[TransferWorkflowOnExceptionStepsCustomStepDetails]:
        return typing.cast(typing.Optional[TransferWorkflowOnExceptionStepsCustomStepDetails], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[TransferWorkflowOnExceptionStepsCustomStepDetails],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__966d839ba4743b798376d7ce2a3adc36b81b41782337f6edb4f5ac9615ab3c2c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.transferWorkflow.TransferWorkflowOnExceptionStepsDeleteStepDetails",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "source_file_location": "sourceFileLocation"},
)
class TransferWorkflowOnExceptionStepsDeleteStepDetails:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        source_file_location: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#name TransferWorkflow#name}.
        :param source_file_location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#source_file_location TransferWorkflow#source_file_location}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e86a6ff798fe174119f51b0698c124144100be67cc19f0067b0a896342b403e)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument source_file_location", value=source_file_location, expected_type=type_hints["source_file_location"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if source_file_location is not None:
            self._values["source_file_location"] = source_file_location

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#name TransferWorkflow#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_file_location(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#source_file_location TransferWorkflow#source_file_location}.'''
        result = self._values.get("source_file_location")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransferWorkflowOnExceptionStepsDeleteStepDetails(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TransferWorkflowOnExceptionStepsDeleteStepDetailsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.transferWorkflow.TransferWorkflowOnExceptionStepsDeleteStepDetailsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bb621bfb471b444fdd8e206a15f4ad3c8e60588ab20da8854e1dc6408bad890b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetSourceFileLocation")
    def reset_source_file_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceFileLocation", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceFileLocationInput")
    def source_file_location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceFileLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f08c5a18d537a8b96120d88f8ffb0ac98454f498dbb553900a52fab4a7222842)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="sourceFileLocation")
    def source_file_location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceFileLocation"))

    @source_file_location.setter
    def source_file_location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f1e00179b27760ad2cdeab150e3abf75ec5570848c0faccaa325ed3372c7e55)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceFileLocation", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[TransferWorkflowOnExceptionStepsDeleteStepDetails]:
        return typing.cast(typing.Optional[TransferWorkflowOnExceptionStepsDeleteStepDetails], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[TransferWorkflowOnExceptionStepsDeleteStepDetails],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aba932bdbde0f0167bcff68b245239ba08b3ef190092370d1875d2481fabbe64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class TransferWorkflowOnExceptionStepsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.transferWorkflow.TransferWorkflowOnExceptionStepsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c3d0bad5ca0e426a797fe74ed6e4481e36f8a89ee433f1794f7c053d9af68526)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "TransferWorkflowOnExceptionStepsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9585e681ec0d577fe294037e645fe67d56c24720110fa53148f1c53eb4628cd5)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("TransferWorkflowOnExceptionStepsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9074c2b7efb74aef9d2e961229b1e965639e6d56f462f5f774e83797f1506299)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7912531e3d606baff4c355653854ee4841d3bfcf49d5fb0af01ec6f2701d8fd2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0b8b12ce36d9483b9ec05446990a9c6c6ec1bdb79259b288aac6992765653eb3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[TransferWorkflowOnExceptionSteps]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[TransferWorkflowOnExceptionSteps]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[TransferWorkflowOnExceptionSteps]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d80963edc30b9df439d15a2e8c238fa58d2b92bba9065eb93d2c72c5baf6806)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class TransferWorkflowOnExceptionStepsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.transferWorkflow.TransferWorkflowOnExceptionStepsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__85ef5d2d6beb1b0d907c9bec0ae54022ba16966adfe07bb9d9e31ecc4f723b1f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putCopyStepDetails")
    def put_copy_step_details(
        self,
        *,
        destination_file_location: typing.Optional[typing.Union[TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocation, typing.Dict[builtins.str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
        overwrite_existing: typing.Optional[builtins.str] = None,
        source_file_location: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param destination_file_location: destination_file_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#destination_file_location TransferWorkflow#destination_file_location}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#name TransferWorkflow#name}.
        :param overwrite_existing: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#overwrite_existing TransferWorkflow#overwrite_existing}.
        :param source_file_location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#source_file_location TransferWorkflow#source_file_location}.
        '''
        value = TransferWorkflowOnExceptionStepsCopyStepDetails(
            destination_file_location=destination_file_location,
            name=name,
            overwrite_existing=overwrite_existing,
            source_file_location=source_file_location,
        )

        return typing.cast(None, jsii.invoke(self, "putCopyStepDetails", [value]))

    @jsii.member(jsii_name="putCustomStepDetails")
    def put_custom_step_details(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        source_file_location: typing.Optional[builtins.str] = None,
        target: typing.Optional[builtins.str] = None,
        timeout_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#name TransferWorkflow#name}.
        :param source_file_location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#source_file_location TransferWorkflow#source_file_location}.
        :param target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#target TransferWorkflow#target}.
        :param timeout_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#timeout_seconds TransferWorkflow#timeout_seconds}.
        '''
        value = TransferWorkflowOnExceptionStepsCustomStepDetails(
            name=name,
            source_file_location=source_file_location,
            target=target,
            timeout_seconds=timeout_seconds,
        )

        return typing.cast(None, jsii.invoke(self, "putCustomStepDetails", [value]))

    @jsii.member(jsii_name="putDeleteStepDetails")
    def put_delete_step_details(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        source_file_location: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#name TransferWorkflow#name}.
        :param source_file_location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#source_file_location TransferWorkflow#source_file_location}.
        '''
        value = TransferWorkflowOnExceptionStepsDeleteStepDetails(
            name=name, source_file_location=source_file_location
        )

        return typing.cast(None, jsii.invoke(self, "putDeleteStepDetails", [value]))

    @jsii.member(jsii_name="putTagStepDetails")
    def put_tag_step_details(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        source_file_location: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["TransferWorkflowOnExceptionStepsTagStepDetailsTags", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#name TransferWorkflow#name}.
        :param source_file_location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#source_file_location TransferWorkflow#source_file_location}.
        :param tags: tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#tags TransferWorkflow#tags}
        '''
        value = TransferWorkflowOnExceptionStepsTagStepDetails(
            name=name, source_file_location=source_file_location, tags=tags
        )

        return typing.cast(None, jsii.invoke(self, "putTagStepDetails", [value]))

    @jsii.member(jsii_name="resetCopyStepDetails")
    def reset_copy_step_details(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCopyStepDetails", []))

    @jsii.member(jsii_name="resetCustomStepDetails")
    def reset_custom_step_details(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomStepDetails", []))

    @jsii.member(jsii_name="resetDeleteStepDetails")
    def reset_delete_step_details(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeleteStepDetails", []))

    @jsii.member(jsii_name="resetTagStepDetails")
    def reset_tag_step_details(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagStepDetails", []))

    @builtins.property
    @jsii.member(jsii_name="copyStepDetails")
    def copy_step_details(
        self,
    ) -> TransferWorkflowOnExceptionStepsCopyStepDetailsOutputReference:
        return typing.cast(TransferWorkflowOnExceptionStepsCopyStepDetailsOutputReference, jsii.get(self, "copyStepDetails"))

    @builtins.property
    @jsii.member(jsii_name="customStepDetails")
    def custom_step_details(
        self,
    ) -> TransferWorkflowOnExceptionStepsCustomStepDetailsOutputReference:
        return typing.cast(TransferWorkflowOnExceptionStepsCustomStepDetailsOutputReference, jsii.get(self, "customStepDetails"))

    @builtins.property
    @jsii.member(jsii_name="deleteStepDetails")
    def delete_step_details(
        self,
    ) -> TransferWorkflowOnExceptionStepsDeleteStepDetailsOutputReference:
        return typing.cast(TransferWorkflowOnExceptionStepsDeleteStepDetailsOutputReference, jsii.get(self, "deleteStepDetails"))

    @builtins.property
    @jsii.member(jsii_name="tagStepDetails")
    def tag_step_details(
        self,
    ) -> "TransferWorkflowOnExceptionStepsTagStepDetailsOutputReference":
        return typing.cast("TransferWorkflowOnExceptionStepsTagStepDetailsOutputReference", jsii.get(self, "tagStepDetails"))

    @builtins.property
    @jsii.member(jsii_name="copyStepDetailsInput")
    def copy_step_details_input(
        self,
    ) -> typing.Optional[TransferWorkflowOnExceptionStepsCopyStepDetails]:
        return typing.cast(typing.Optional[TransferWorkflowOnExceptionStepsCopyStepDetails], jsii.get(self, "copyStepDetailsInput"))

    @builtins.property
    @jsii.member(jsii_name="customStepDetailsInput")
    def custom_step_details_input(
        self,
    ) -> typing.Optional[TransferWorkflowOnExceptionStepsCustomStepDetails]:
        return typing.cast(typing.Optional[TransferWorkflowOnExceptionStepsCustomStepDetails], jsii.get(self, "customStepDetailsInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteStepDetailsInput")
    def delete_step_details_input(
        self,
    ) -> typing.Optional[TransferWorkflowOnExceptionStepsDeleteStepDetails]:
        return typing.cast(typing.Optional[TransferWorkflowOnExceptionStepsDeleteStepDetails], jsii.get(self, "deleteStepDetailsInput"))

    @builtins.property
    @jsii.member(jsii_name="tagStepDetailsInput")
    def tag_step_details_input(
        self,
    ) -> typing.Optional["TransferWorkflowOnExceptionStepsTagStepDetails"]:
        return typing.cast(typing.Optional["TransferWorkflowOnExceptionStepsTagStepDetails"], jsii.get(self, "tagStepDetailsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a89f6eaecac5a870f8876c4e414751a8cc493d4be29c0704249af92f0240ee34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[TransferWorkflowOnExceptionSteps, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[TransferWorkflowOnExceptionSteps, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[TransferWorkflowOnExceptionSteps, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74b8ee568113f4ea1e69d534252a1f2ae996da143902c614f2b83dd00dd5312e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.transferWorkflow.TransferWorkflowOnExceptionStepsTagStepDetails",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "source_file_location": "sourceFileLocation",
        "tags": "tags",
    },
)
class TransferWorkflowOnExceptionStepsTagStepDetails:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        source_file_location: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["TransferWorkflowOnExceptionStepsTagStepDetailsTags", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#name TransferWorkflow#name}.
        :param source_file_location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#source_file_location TransferWorkflow#source_file_location}.
        :param tags: tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#tags TransferWorkflow#tags}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c98bd22be5efab6cf2a53f5a76296681dff1c3d9bdcaf8777d35926b53d50bf1)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument source_file_location", value=source_file_location, expected_type=type_hints["source_file_location"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if source_file_location is not None:
            self._values["source_file_location"] = source_file_location
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#name TransferWorkflow#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_file_location(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#source_file_location TransferWorkflow#source_file_location}.'''
        result = self._values.get("source_file_location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["TransferWorkflowOnExceptionStepsTagStepDetailsTags"]]]:
        '''tags block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#tags TransferWorkflow#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["TransferWorkflowOnExceptionStepsTagStepDetailsTags"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransferWorkflowOnExceptionStepsTagStepDetails(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TransferWorkflowOnExceptionStepsTagStepDetailsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.transferWorkflow.TransferWorkflowOnExceptionStepsTagStepDetailsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ec5894b709efe12e56d78d02f72d6f5db6f4fbaba37a66902d098467e9c49c7e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putTags")
    def put_tags(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["TransferWorkflowOnExceptionStepsTagStepDetailsTags", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f766b7a064c21b88b70ea5ca0f9a86a4de6058150877ee408a63837af6af8b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTags", [value]))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetSourceFileLocation")
    def reset_source_file_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceFileLocation", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> "TransferWorkflowOnExceptionStepsTagStepDetailsTagsList":
        return typing.cast("TransferWorkflowOnExceptionStepsTagStepDetailsTagsList", jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceFileLocationInput")
    def source_file_location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceFileLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["TransferWorkflowOnExceptionStepsTagStepDetailsTags"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["TransferWorkflowOnExceptionStepsTagStepDetailsTags"]]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79f954b7de487aca7a332f335f1606546f98bc87a8f97f6de5b3c43435cfe3b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="sourceFileLocation")
    def source_file_location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceFileLocation"))

    @source_file_location.setter
    def source_file_location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc4811284c327604abf057679b9acb711ca4ac31a2fef47d27678aaf5327e2ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceFileLocation", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[TransferWorkflowOnExceptionStepsTagStepDetails]:
        return typing.cast(typing.Optional[TransferWorkflowOnExceptionStepsTagStepDetails], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[TransferWorkflowOnExceptionStepsTagStepDetails],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__351d3edc8a5616f802f3615925749bf4f91ef34b3dfa7bd5782f3cbce33af729)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.transferWorkflow.TransferWorkflowOnExceptionStepsTagStepDetailsTags",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class TransferWorkflowOnExceptionStepsTagStepDetailsTags:
    def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#key TransferWorkflow#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#value TransferWorkflow#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b814195b3904ecdb9d0737ad7405a0d15de7b4103a7e9da670b964c2fe2a771)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#key TransferWorkflow#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#value TransferWorkflow#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransferWorkflowOnExceptionStepsTagStepDetailsTags(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TransferWorkflowOnExceptionStepsTagStepDetailsTagsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.transferWorkflow.TransferWorkflowOnExceptionStepsTagStepDetailsTagsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a3c6107c3a46738974d2380d80e939e22ae74a0b833a3d2c947eed39ae57c849)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "TransferWorkflowOnExceptionStepsTagStepDetailsTagsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9686140de42a345e275a4e835b62d00fc9b5dad905f7ee01d80d01d7654c848e)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("TransferWorkflowOnExceptionStepsTagStepDetailsTagsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7edf2b99544ba00c64fe5870bebd2da693ad998790ee34d4e188ce4a7bd12bb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6a478a226b703581d403b6fb55b50d75e760ae68865745f32712140f31dd1426)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ab1dde8bb519e0352c17b65b7366a0fe910618b6b78853fb002154312e09880b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[TransferWorkflowOnExceptionStepsTagStepDetailsTags]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[TransferWorkflowOnExceptionStepsTagStepDetailsTags]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[TransferWorkflowOnExceptionStepsTagStepDetailsTags]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02524976489b86bcd03e2a98e0445594aec62e94953736c5fd3b740496b45778)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class TransferWorkflowOnExceptionStepsTagStepDetailsTagsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.transferWorkflow.TransferWorkflowOnExceptionStepsTagStepDetailsTagsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e8d61c9a358cf08ea1da4b7445a8b35c98bee1dfd266fc62321f03000ef26f66)
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
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b6ed9265a07cbec24afb3f55ad8e5068a9f9720a9e13c4ae26568aed0711359)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20180f542bb1d03f2c331efc99ed74e7ff200954eb5d5fa1423987cf24988886)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[TransferWorkflowOnExceptionStepsTagStepDetailsTags, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[TransferWorkflowOnExceptionStepsTagStepDetailsTags, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[TransferWorkflowOnExceptionStepsTagStepDetailsTags, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ab0778ca8205144eb04b5272a26204a06b19a4e08dd3bd120ba13e1772d9378)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.transferWorkflow.TransferWorkflowSteps",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "copy_step_details": "copyStepDetails",
        "custom_step_details": "customStepDetails",
        "delete_step_details": "deleteStepDetails",
        "tag_step_details": "tagStepDetails",
    },
)
class TransferWorkflowSteps:
    def __init__(
        self,
        *,
        type: builtins.str,
        copy_step_details: typing.Optional[typing.Union["TransferWorkflowStepsCopyStepDetails", typing.Dict[builtins.str, typing.Any]]] = None,
        custom_step_details: typing.Optional[typing.Union["TransferWorkflowStepsCustomStepDetails", typing.Dict[builtins.str, typing.Any]]] = None,
        delete_step_details: typing.Optional[typing.Union["TransferWorkflowStepsDeleteStepDetails", typing.Dict[builtins.str, typing.Any]]] = None,
        tag_step_details: typing.Optional[typing.Union["TransferWorkflowStepsTagStepDetails", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#type TransferWorkflow#type}.
        :param copy_step_details: copy_step_details block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#copy_step_details TransferWorkflow#copy_step_details}
        :param custom_step_details: custom_step_details block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#custom_step_details TransferWorkflow#custom_step_details}
        :param delete_step_details: delete_step_details block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#delete_step_details TransferWorkflow#delete_step_details}
        :param tag_step_details: tag_step_details block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#tag_step_details TransferWorkflow#tag_step_details}
        '''
        if isinstance(copy_step_details, dict):
            copy_step_details = TransferWorkflowStepsCopyStepDetails(**copy_step_details)
        if isinstance(custom_step_details, dict):
            custom_step_details = TransferWorkflowStepsCustomStepDetails(**custom_step_details)
        if isinstance(delete_step_details, dict):
            delete_step_details = TransferWorkflowStepsDeleteStepDetails(**delete_step_details)
        if isinstance(tag_step_details, dict):
            tag_step_details = TransferWorkflowStepsTagStepDetails(**tag_step_details)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1927df0b5ded0553dc87d4bc1e7f9a06693581a197829ffde1deb355ee42ee7)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument copy_step_details", value=copy_step_details, expected_type=type_hints["copy_step_details"])
            check_type(argname="argument custom_step_details", value=custom_step_details, expected_type=type_hints["custom_step_details"])
            check_type(argname="argument delete_step_details", value=delete_step_details, expected_type=type_hints["delete_step_details"])
            check_type(argname="argument tag_step_details", value=tag_step_details, expected_type=type_hints["tag_step_details"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if copy_step_details is not None:
            self._values["copy_step_details"] = copy_step_details
        if custom_step_details is not None:
            self._values["custom_step_details"] = custom_step_details
        if delete_step_details is not None:
            self._values["delete_step_details"] = delete_step_details
        if tag_step_details is not None:
            self._values["tag_step_details"] = tag_step_details

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#type TransferWorkflow#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def copy_step_details(
        self,
    ) -> typing.Optional["TransferWorkflowStepsCopyStepDetails"]:
        '''copy_step_details block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#copy_step_details TransferWorkflow#copy_step_details}
        '''
        result = self._values.get("copy_step_details")
        return typing.cast(typing.Optional["TransferWorkflowStepsCopyStepDetails"], result)

    @builtins.property
    def custom_step_details(
        self,
    ) -> typing.Optional["TransferWorkflowStepsCustomStepDetails"]:
        '''custom_step_details block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#custom_step_details TransferWorkflow#custom_step_details}
        '''
        result = self._values.get("custom_step_details")
        return typing.cast(typing.Optional["TransferWorkflowStepsCustomStepDetails"], result)

    @builtins.property
    def delete_step_details(
        self,
    ) -> typing.Optional["TransferWorkflowStepsDeleteStepDetails"]:
        '''delete_step_details block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#delete_step_details TransferWorkflow#delete_step_details}
        '''
        result = self._values.get("delete_step_details")
        return typing.cast(typing.Optional["TransferWorkflowStepsDeleteStepDetails"], result)

    @builtins.property
    def tag_step_details(
        self,
    ) -> typing.Optional["TransferWorkflowStepsTagStepDetails"]:
        '''tag_step_details block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#tag_step_details TransferWorkflow#tag_step_details}
        '''
        result = self._values.get("tag_step_details")
        return typing.cast(typing.Optional["TransferWorkflowStepsTagStepDetails"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransferWorkflowSteps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.transferWorkflow.TransferWorkflowStepsCopyStepDetails",
    jsii_struct_bases=[],
    name_mapping={
        "destination_file_location": "destinationFileLocation",
        "name": "name",
        "overwrite_existing": "overwriteExisting",
        "source_file_location": "sourceFileLocation",
    },
)
class TransferWorkflowStepsCopyStepDetails:
    def __init__(
        self,
        *,
        destination_file_location: typing.Optional[typing.Union["TransferWorkflowStepsCopyStepDetailsDestinationFileLocation", typing.Dict[builtins.str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
        overwrite_existing: typing.Optional[builtins.str] = None,
        source_file_location: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param destination_file_location: destination_file_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#destination_file_location TransferWorkflow#destination_file_location}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#name TransferWorkflow#name}.
        :param overwrite_existing: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#overwrite_existing TransferWorkflow#overwrite_existing}.
        :param source_file_location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#source_file_location TransferWorkflow#source_file_location}.
        '''
        if isinstance(destination_file_location, dict):
            destination_file_location = TransferWorkflowStepsCopyStepDetailsDestinationFileLocation(**destination_file_location)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1d930ce67d59cc205f8e515c8639f41ef7e50b226cae773b20ca846913f1165)
            check_type(argname="argument destination_file_location", value=destination_file_location, expected_type=type_hints["destination_file_location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument overwrite_existing", value=overwrite_existing, expected_type=type_hints["overwrite_existing"])
            check_type(argname="argument source_file_location", value=source_file_location, expected_type=type_hints["source_file_location"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if destination_file_location is not None:
            self._values["destination_file_location"] = destination_file_location
        if name is not None:
            self._values["name"] = name
        if overwrite_existing is not None:
            self._values["overwrite_existing"] = overwrite_existing
        if source_file_location is not None:
            self._values["source_file_location"] = source_file_location

    @builtins.property
    def destination_file_location(
        self,
    ) -> typing.Optional["TransferWorkflowStepsCopyStepDetailsDestinationFileLocation"]:
        '''destination_file_location block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#destination_file_location TransferWorkflow#destination_file_location}
        '''
        result = self._values.get("destination_file_location")
        return typing.cast(typing.Optional["TransferWorkflowStepsCopyStepDetailsDestinationFileLocation"], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#name TransferWorkflow#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def overwrite_existing(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#overwrite_existing TransferWorkflow#overwrite_existing}.'''
        result = self._values.get("overwrite_existing")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_file_location(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#source_file_location TransferWorkflow#source_file_location}.'''
        result = self._values.get("source_file_location")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransferWorkflowStepsCopyStepDetails(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.transferWorkflow.TransferWorkflowStepsCopyStepDetailsDestinationFileLocation",
    jsii_struct_bases=[],
    name_mapping={
        "efs_file_location": "efsFileLocation",
        "s3_file_location": "s3FileLocation",
    },
)
class TransferWorkflowStepsCopyStepDetailsDestinationFileLocation:
    def __init__(
        self,
        *,
        efs_file_location: typing.Optional[typing.Union["TransferWorkflowStepsCopyStepDetailsDestinationFileLocationEfsFileLocation", typing.Dict[builtins.str, typing.Any]]] = None,
        s3_file_location: typing.Optional[typing.Union["TransferWorkflowStepsCopyStepDetailsDestinationFileLocationS3FileLocation", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param efs_file_location: efs_file_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#efs_file_location TransferWorkflow#efs_file_location}
        :param s3_file_location: s3_file_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#s3_file_location TransferWorkflow#s3_file_location}
        '''
        if isinstance(efs_file_location, dict):
            efs_file_location = TransferWorkflowStepsCopyStepDetailsDestinationFileLocationEfsFileLocation(**efs_file_location)
        if isinstance(s3_file_location, dict):
            s3_file_location = TransferWorkflowStepsCopyStepDetailsDestinationFileLocationS3FileLocation(**s3_file_location)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b56b3db6f4432e4d453d4c0049b50e52d4d61f5a82221d7e239db2f1e53c5756)
            check_type(argname="argument efs_file_location", value=efs_file_location, expected_type=type_hints["efs_file_location"])
            check_type(argname="argument s3_file_location", value=s3_file_location, expected_type=type_hints["s3_file_location"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if efs_file_location is not None:
            self._values["efs_file_location"] = efs_file_location
        if s3_file_location is not None:
            self._values["s3_file_location"] = s3_file_location

    @builtins.property
    def efs_file_location(
        self,
    ) -> typing.Optional["TransferWorkflowStepsCopyStepDetailsDestinationFileLocationEfsFileLocation"]:
        '''efs_file_location block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#efs_file_location TransferWorkflow#efs_file_location}
        '''
        result = self._values.get("efs_file_location")
        return typing.cast(typing.Optional["TransferWorkflowStepsCopyStepDetailsDestinationFileLocationEfsFileLocation"], result)

    @builtins.property
    def s3_file_location(
        self,
    ) -> typing.Optional["TransferWorkflowStepsCopyStepDetailsDestinationFileLocationS3FileLocation"]:
        '''s3_file_location block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#s3_file_location TransferWorkflow#s3_file_location}
        '''
        result = self._values.get("s3_file_location")
        return typing.cast(typing.Optional["TransferWorkflowStepsCopyStepDetailsDestinationFileLocationS3FileLocation"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransferWorkflowStepsCopyStepDetailsDestinationFileLocation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.transferWorkflow.TransferWorkflowStepsCopyStepDetailsDestinationFileLocationEfsFileLocation",
    jsii_struct_bases=[],
    name_mapping={"file_system_id": "fileSystemId", "path": "path"},
)
class TransferWorkflowStepsCopyStepDetailsDestinationFileLocationEfsFileLocation:
    def __init__(
        self,
        *,
        file_system_id: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param file_system_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#file_system_id TransferWorkflow#file_system_id}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#path TransferWorkflow#path}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28753952b2a399b788e7e0a347c26c2dea438c5d59bb7e5c73f8297795a998c0)
            check_type(argname="argument file_system_id", value=file_system_id, expected_type=type_hints["file_system_id"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if file_system_id is not None:
            self._values["file_system_id"] = file_system_id
        if path is not None:
            self._values["path"] = path

    @builtins.property
    def file_system_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#file_system_id TransferWorkflow#file_system_id}.'''
        result = self._values.get("file_system_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#path TransferWorkflow#path}.'''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransferWorkflowStepsCopyStepDetailsDestinationFileLocationEfsFileLocation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TransferWorkflowStepsCopyStepDetailsDestinationFileLocationEfsFileLocationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.transferWorkflow.TransferWorkflowStepsCopyStepDetailsDestinationFileLocationEfsFileLocationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ebd1a24a9c9b4937a83e90eb78b811b58f25fbd1a17583f90d0a4ec0af30c6b2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFileSystemId")
    def reset_file_system_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileSystemId", []))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @builtins.property
    @jsii.member(jsii_name="fileSystemIdInput")
    def file_system_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileSystemIdInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="fileSystemId")
    def file_system_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileSystemId"))

    @file_system_id.setter
    def file_system_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d48e19a951b8d8ee16151b30e03647decc37655c8a5780420216717761804df4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileSystemId", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57b7608ee31d7c29872f46841c29eea37ecceb5cb4f64336f9ed0e5bd61d9e00)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[TransferWorkflowStepsCopyStepDetailsDestinationFileLocationEfsFileLocation]:
        return typing.cast(typing.Optional[TransferWorkflowStepsCopyStepDetailsDestinationFileLocationEfsFileLocation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[TransferWorkflowStepsCopyStepDetailsDestinationFileLocationEfsFileLocation],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d89719768571d3e737b6b73c1b2c451ec53ec4638d0ab383933b3a37ad98cb1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class TransferWorkflowStepsCopyStepDetailsDestinationFileLocationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.transferWorkflow.TransferWorkflowStepsCopyStepDetailsDestinationFileLocationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__58566bb457afbf6fcb3a75aefc65310efba9b69e2cd1903ce48b72aa5f716fff)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putEfsFileLocation")
    def put_efs_file_location(
        self,
        *,
        file_system_id: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param file_system_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#file_system_id TransferWorkflow#file_system_id}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#path TransferWorkflow#path}.
        '''
        value = TransferWorkflowStepsCopyStepDetailsDestinationFileLocationEfsFileLocation(
            file_system_id=file_system_id, path=path
        )

        return typing.cast(None, jsii.invoke(self, "putEfsFileLocation", [value]))

    @jsii.member(jsii_name="putS3FileLocation")
    def put_s3_file_location(
        self,
        *,
        bucket: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#bucket TransferWorkflow#bucket}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#key TransferWorkflow#key}.
        '''
        value = TransferWorkflowStepsCopyStepDetailsDestinationFileLocationS3FileLocation(
            bucket=bucket, key=key
        )

        return typing.cast(None, jsii.invoke(self, "putS3FileLocation", [value]))

    @jsii.member(jsii_name="resetEfsFileLocation")
    def reset_efs_file_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEfsFileLocation", []))

    @jsii.member(jsii_name="resetS3FileLocation")
    def reset_s3_file_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3FileLocation", []))

    @builtins.property
    @jsii.member(jsii_name="efsFileLocation")
    def efs_file_location(
        self,
    ) -> TransferWorkflowStepsCopyStepDetailsDestinationFileLocationEfsFileLocationOutputReference:
        return typing.cast(TransferWorkflowStepsCopyStepDetailsDestinationFileLocationEfsFileLocationOutputReference, jsii.get(self, "efsFileLocation"))

    @builtins.property
    @jsii.member(jsii_name="s3FileLocation")
    def s3_file_location(
        self,
    ) -> "TransferWorkflowStepsCopyStepDetailsDestinationFileLocationS3FileLocationOutputReference":
        return typing.cast("TransferWorkflowStepsCopyStepDetailsDestinationFileLocationS3FileLocationOutputReference", jsii.get(self, "s3FileLocation"))

    @builtins.property
    @jsii.member(jsii_name="efsFileLocationInput")
    def efs_file_location_input(
        self,
    ) -> typing.Optional[TransferWorkflowStepsCopyStepDetailsDestinationFileLocationEfsFileLocation]:
        return typing.cast(typing.Optional[TransferWorkflowStepsCopyStepDetailsDestinationFileLocationEfsFileLocation], jsii.get(self, "efsFileLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="s3FileLocationInput")
    def s3_file_location_input(
        self,
    ) -> typing.Optional["TransferWorkflowStepsCopyStepDetailsDestinationFileLocationS3FileLocation"]:
        return typing.cast(typing.Optional["TransferWorkflowStepsCopyStepDetailsDestinationFileLocationS3FileLocation"], jsii.get(self, "s3FileLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[TransferWorkflowStepsCopyStepDetailsDestinationFileLocation]:
        return typing.cast(typing.Optional[TransferWorkflowStepsCopyStepDetailsDestinationFileLocation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[TransferWorkflowStepsCopyStepDetailsDestinationFileLocation],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6276eabec7ca1e6710528a7b5762c33b70090a4a37083327dd1581b298e6a31b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.transferWorkflow.TransferWorkflowStepsCopyStepDetailsDestinationFileLocationS3FileLocation",
    jsii_struct_bases=[],
    name_mapping={"bucket": "bucket", "key": "key"},
)
class TransferWorkflowStepsCopyStepDetailsDestinationFileLocationS3FileLocation:
    def __init__(
        self,
        *,
        bucket: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#bucket TransferWorkflow#bucket}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#key TransferWorkflow#key}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2c61b15e89dd60bed93573f65d8618e9b58a298751d668ad3cb731103fcc9ba)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if bucket is not None:
            self._values["bucket"] = bucket
        if key is not None:
            self._values["key"] = key

    @builtins.property
    def bucket(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#bucket TransferWorkflow#bucket}.'''
        result = self._values.get("bucket")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#key TransferWorkflow#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransferWorkflowStepsCopyStepDetailsDestinationFileLocationS3FileLocation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TransferWorkflowStepsCopyStepDetailsDestinationFileLocationS3FileLocationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.transferWorkflow.TransferWorkflowStepsCopyStepDetailsDestinationFileLocationS3FileLocationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ee9d3c6ef43f7c43da30c3291b42af46bbaf2e61deac0c5e6558549012a5bc65)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBucket")
    def reset_bucket(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucket", []))

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @builtins.property
    @jsii.member(jsii_name="bucketInput")
    def bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0b13aba046a2ddc603f7442535256c13a7a2677260a11ee8386f1650fa4856e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucket", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ebe6c5771ffcdaecf9cb63d1bab9e2c1af2dc9d766073d24e0d62cee50ccad1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[TransferWorkflowStepsCopyStepDetailsDestinationFileLocationS3FileLocation]:
        return typing.cast(typing.Optional[TransferWorkflowStepsCopyStepDetailsDestinationFileLocationS3FileLocation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[TransferWorkflowStepsCopyStepDetailsDestinationFileLocationS3FileLocation],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97c56f3314ea4f8313f1584572b31fd20c7d6be884b98f65df174b4e7512551b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class TransferWorkflowStepsCopyStepDetailsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.transferWorkflow.TransferWorkflowStepsCopyStepDetailsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__36d5468b61e8ff42ff73ccae62598386e34508443b48f5ff0b40cd4975d02ad5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDestinationFileLocation")
    def put_destination_file_location(
        self,
        *,
        efs_file_location: typing.Optional[typing.Union[TransferWorkflowStepsCopyStepDetailsDestinationFileLocationEfsFileLocation, typing.Dict[builtins.str, typing.Any]]] = None,
        s3_file_location: typing.Optional[typing.Union[TransferWorkflowStepsCopyStepDetailsDestinationFileLocationS3FileLocation, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param efs_file_location: efs_file_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#efs_file_location TransferWorkflow#efs_file_location}
        :param s3_file_location: s3_file_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#s3_file_location TransferWorkflow#s3_file_location}
        '''
        value = TransferWorkflowStepsCopyStepDetailsDestinationFileLocation(
            efs_file_location=efs_file_location, s3_file_location=s3_file_location
        )

        return typing.cast(None, jsii.invoke(self, "putDestinationFileLocation", [value]))

    @jsii.member(jsii_name="resetDestinationFileLocation")
    def reset_destination_file_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationFileLocation", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetOverwriteExisting")
    def reset_overwrite_existing(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOverwriteExisting", []))

    @jsii.member(jsii_name="resetSourceFileLocation")
    def reset_source_file_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceFileLocation", []))

    @builtins.property
    @jsii.member(jsii_name="destinationFileLocation")
    def destination_file_location(
        self,
    ) -> TransferWorkflowStepsCopyStepDetailsDestinationFileLocationOutputReference:
        return typing.cast(TransferWorkflowStepsCopyStepDetailsDestinationFileLocationOutputReference, jsii.get(self, "destinationFileLocation"))

    @builtins.property
    @jsii.member(jsii_name="destinationFileLocationInput")
    def destination_file_location_input(
        self,
    ) -> typing.Optional[TransferWorkflowStepsCopyStepDetailsDestinationFileLocation]:
        return typing.cast(typing.Optional[TransferWorkflowStepsCopyStepDetailsDestinationFileLocation], jsii.get(self, "destinationFileLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="overwriteExistingInput")
    def overwrite_existing_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "overwriteExistingInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceFileLocationInput")
    def source_file_location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceFileLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc1bf50e1af52b4da410951d1ed7946b330642d47830c0457ee327359b317795)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="overwriteExisting")
    def overwrite_existing(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "overwriteExisting"))

    @overwrite_existing.setter
    def overwrite_existing(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c991b8ace67d92653e26cfe122d092a3be45ec83cbeef10db9a3eabdfc70d1f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "overwriteExisting", value)

    @builtins.property
    @jsii.member(jsii_name="sourceFileLocation")
    def source_file_location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceFileLocation"))

    @source_file_location.setter
    def source_file_location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53ae6bd10685ab5dbb04b22ffe8b24e6e47259ac9f77101f6fe164d85b47e230)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceFileLocation", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[TransferWorkflowStepsCopyStepDetails]:
        return typing.cast(typing.Optional[TransferWorkflowStepsCopyStepDetails], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[TransferWorkflowStepsCopyStepDetails],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d1c63c5a58f7ecde7e1f921142404eeddbe65aab23a54a2681bdb7ef9aba540)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.transferWorkflow.TransferWorkflowStepsCustomStepDetails",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "source_file_location": "sourceFileLocation",
        "target": "target",
        "timeout_seconds": "timeoutSeconds",
    },
)
class TransferWorkflowStepsCustomStepDetails:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        source_file_location: typing.Optional[builtins.str] = None,
        target: typing.Optional[builtins.str] = None,
        timeout_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#name TransferWorkflow#name}.
        :param source_file_location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#source_file_location TransferWorkflow#source_file_location}.
        :param target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#target TransferWorkflow#target}.
        :param timeout_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#timeout_seconds TransferWorkflow#timeout_seconds}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__296d334727db5906b7fef9c564b0685bb47befa69b6283bf5e47d00e17562c7c)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument source_file_location", value=source_file_location, expected_type=type_hints["source_file_location"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument timeout_seconds", value=timeout_seconds, expected_type=type_hints["timeout_seconds"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if source_file_location is not None:
            self._values["source_file_location"] = source_file_location
        if target is not None:
            self._values["target"] = target
        if timeout_seconds is not None:
            self._values["timeout_seconds"] = timeout_seconds

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#name TransferWorkflow#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_file_location(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#source_file_location TransferWorkflow#source_file_location}.'''
        result = self._values.get("source_file_location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#target TransferWorkflow#target}.'''
        result = self._values.get("target")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeout_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#timeout_seconds TransferWorkflow#timeout_seconds}.'''
        result = self._values.get("timeout_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransferWorkflowStepsCustomStepDetails(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TransferWorkflowStepsCustomStepDetailsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.transferWorkflow.TransferWorkflowStepsCustomStepDetailsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__06bd18b1ceb332c72c6505089c7d9c7d1e51768ce21a914bb5e48d4aa452a80b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetSourceFileLocation")
    def reset_source_file_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceFileLocation", []))

    @jsii.member(jsii_name="resetTarget")
    def reset_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTarget", []))

    @jsii.member(jsii_name="resetTimeoutSeconds")
    def reset_timeout_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeoutSeconds", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceFileLocationInput")
    def source_file_location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceFileLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutSecondsInput")
    def timeout_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0aa37165098cf34c6e1ec256e2e848afee03c85a5b658960080dc43b8bec4189)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="sourceFileLocation")
    def source_file_location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceFileLocation"))

    @source_file_location.setter
    def source_file_location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83f7e31307ccdff27e931d81d34394f8e5a457b8a322886ff2d293f8c2b76ac7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceFileLocation", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d98f665e6a1b4cff4e9ca0a15eb5847d66a982b9b960d90e91f582c1ec1d72d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="timeoutSeconds")
    def timeout_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeoutSeconds"))

    @timeout_seconds.setter
    def timeout_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e06d71b2ffcd9bf4b529a53ed40ba518c3984342ca7f5606ca2e716d15e638ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[TransferWorkflowStepsCustomStepDetails]:
        return typing.cast(typing.Optional[TransferWorkflowStepsCustomStepDetails], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[TransferWorkflowStepsCustomStepDetails],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8b5cd7de7d636c7a3d850a57783f7ad439345ebd2a017b8b45b4a8f04e7478c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.transferWorkflow.TransferWorkflowStepsDeleteStepDetails",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "source_file_location": "sourceFileLocation"},
)
class TransferWorkflowStepsDeleteStepDetails:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        source_file_location: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#name TransferWorkflow#name}.
        :param source_file_location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#source_file_location TransferWorkflow#source_file_location}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca24fa27d7c5c45fa7ee7f3adbde9506ee6f4bd9f8c887e6a4c52bd9e4eae9f2)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument source_file_location", value=source_file_location, expected_type=type_hints["source_file_location"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if source_file_location is not None:
            self._values["source_file_location"] = source_file_location

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#name TransferWorkflow#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_file_location(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#source_file_location TransferWorkflow#source_file_location}.'''
        result = self._values.get("source_file_location")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransferWorkflowStepsDeleteStepDetails(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TransferWorkflowStepsDeleteStepDetailsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.transferWorkflow.TransferWorkflowStepsDeleteStepDetailsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__04e370f59edb77c830c3881e8561105a3fd331bc43a1300752599319839f2f0e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetSourceFileLocation")
    def reset_source_file_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceFileLocation", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceFileLocationInput")
    def source_file_location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceFileLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bc74bdfdd6ea17df68216a2fcbd018767c064847023245f22cc2d5525bf19a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="sourceFileLocation")
    def source_file_location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceFileLocation"))

    @source_file_location.setter
    def source_file_location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__873f08e6c9cde75e44e6215aace9e425b0e7ad72fbaa2b4f3b2cfdd971a44954)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceFileLocation", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[TransferWorkflowStepsDeleteStepDetails]:
        return typing.cast(typing.Optional[TransferWorkflowStepsDeleteStepDetails], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[TransferWorkflowStepsDeleteStepDetails],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c602da39ab8cd99c6d0dff241a329a0469e3356be7ab7e70d9cd178810a8291a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class TransferWorkflowStepsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.transferWorkflow.TransferWorkflowStepsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__58724a787dcb670fcdfc1037cb67b589731170b6c290a787f4f67cf2b1e513dc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "TransferWorkflowStepsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fe5555a2b9eefd60423b65052145a7946256a28ec0ac68e5ed0ed58becb27d6)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("TransferWorkflowStepsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2448d16a68199c7ef92b38f42677a8d2960788c66115a1891aac5d9ba4f61c21)
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
            type_hints = typing.get_type_hints(_typecheckingstub__eb287e7af550754a994e04e346149447bd77cae8353f8d97e2e664de5eb5fca9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6ea6a809a41413aeefcb21183187feacb21c2d44da650a68185ec93caab017ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[TransferWorkflowSteps]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[TransferWorkflowSteps]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[TransferWorkflowSteps]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36cb97278f54b4adb2cf29b823b3bd0a19580cd44f85ebe48550b023ab4bb4bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class TransferWorkflowStepsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.transferWorkflow.TransferWorkflowStepsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5e7abbb19ffba41d5bf9522dbd40d454ee64ccdec2c6507b31cb75c402016f82)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putCopyStepDetails")
    def put_copy_step_details(
        self,
        *,
        destination_file_location: typing.Optional[typing.Union[TransferWorkflowStepsCopyStepDetailsDestinationFileLocation, typing.Dict[builtins.str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
        overwrite_existing: typing.Optional[builtins.str] = None,
        source_file_location: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param destination_file_location: destination_file_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#destination_file_location TransferWorkflow#destination_file_location}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#name TransferWorkflow#name}.
        :param overwrite_existing: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#overwrite_existing TransferWorkflow#overwrite_existing}.
        :param source_file_location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#source_file_location TransferWorkflow#source_file_location}.
        '''
        value = TransferWorkflowStepsCopyStepDetails(
            destination_file_location=destination_file_location,
            name=name,
            overwrite_existing=overwrite_existing,
            source_file_location=source_file_location,
        )

        return typing.cast(None, jsii.invoke(self, "putCopyStepDetails", [value]))

    @jsii.member(jsii_name="putCustomStepDetails")
    def put_custom_step_details(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        source_file_location: typing.Optional[builtins.str] = None,
        target: typing.Optional[builtins.str] = None,
        timeout_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#name TransferWorkflow#name}.
        :param source_file_location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#source_file_location TransferWorkflow#source_file_location}.
        :param target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#target TransferWorkflow#target}.
        :param timeout_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#timeout_seconds TransferWorkflow#timeout_seconds}.
        '''
        value = TransferWorkflowStepsCustomStepDetails(
            name=name,
            source_file_location=source_file_location,
            target=target,
            timeout_seconds=timeout_seconds,
        )

        return typing.cast(None, jsii.invoke(self, "putCustomStepDetails", [value]))

    @jsii.member(jsii_name="putDeleteStepDetails")
    def put_delete_step_details(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        source_file_location: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#name TransferWorkflow#name}.
        :param source_file_location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#source_file_location TransferWorkflow#source_file_location}.
        '''
        value = TransferWorkflowStepsDeleteStepDetails(
            name=name, source_file_location=source_file_location
        )

        return typing.cast(None, jsii.invoke(self, "putDeleteStepDetails", [value]))

    @jsii.member(jsii_name="putTagStepDetails")
    def put_tag_step_details(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        source_file_location: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["TransferWorkflowStepsTagStepDetailsTags", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#name TransferWorkflow#name}.
        :param source_file_location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#source_file_location TransferWorkflow#source_file_location}.
        :param tags: tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#tags TransferWorkflow#tags}
        '''
        value = TransferWorkflowStepsTagStepDetails(
            name=name, source_file_location=source_file_location, tags=tags
        )

        return typing.cast(None, jsii.invoke(self, "putTagStepDetails", [value]))

    @jsii.member(jsii_name="resetCopyStepDetails")
    def reset_copy_step_details(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCopyStepDetails", []))

    @jsii.member(jsii_name="resetCustomStepDetails")
    def reset_custom_step_details(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomStepDetails", []))

    @jsii.member(jsii_name="resetDeleteStepDetails")
    def reset_delete_step_details(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeleteStepDetails", []))

    @jsii.member(jsii_name="resetTagStepDetails")
    def reset_tag_step_details(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagStepDetails", []))

    @builtins.property
    @jsii.member(jsii_name="copyStepDetails")
    def copy_step_details(self) -> TransferWorkflowStepsCopyStepDetailsOutputReference:
        return typing.cast(TransferWorkflowStepsCopyStepDetailsOutputReference, jsii.get(self, "copyStepDetails"))

    @builtins.property
    @jsii.member(jsii_name="customStepDetails")
    def custom_step_details(
        self,
    ) -> TransferWorkflowStepsCustomStepDetailsOutputReference:
        return typing.cast(TransferWorkflowStepsCustomStepDetailsOutputReference, jsii.get(self, "customStepDetails"))

    @builtins.property
    @jsii.member(jsii_name="deleteStepDetails")
    def delete_step_details(
        self,
    ) -> TransferWorkflowStepsDeleteStepDetailsOutputReference:
        return typing.cast(TransferWorkflowStepsDeleteStepDetailsOutputReference, jsii.get(self, "deleteStepDetails"))

    @builtins.property
    @jsii.member(jsii_name="tagStepDetails")
    def tag_step_details(self) -> "TransferWorkflowStepsTagStepDetailsOutputReference":
        return typing.cast("TransferWorkflowStepsTagStepDetailsOutputReference", jsii.get(self, "tagStepDetails"))

    @builtins.property
    @jsii.member(jsii_name="copyStepDetailsInput")
    def copy_step_details_input(
        self,
    ) -> typing.Optional[TransferWorkflowStepsCopyStepDetails]:
        return typing.cast(typing.Optional[TransferWorkflowStepsCopyStepDetails], jsii.get(self, "copyStepDetailsInput"))

    @builtins.property
    @jsii.member(jsii_name="customStepDetailsInput")
    def custom_step_details_input(
        self,
    ) -> typing.Optional[TransferWorkflowStepsCustomStepDetails]:
        return typing.cast(typing.Optional[TransferWorkflowStepsCustomStepDetails], jsii.get(self, "customStepDetailsInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteStepDetailsInput")
    def delete_step_details_input(
        self,
    ) -> typing.Optional[TransferWorkflowStepsDeleteStepDetails]:
        return typing.cast(typing.Optional[TransferWorkflowStepsDeleteStepDetails], jsii.get(self, "deleteStepDetailsInput"))

    @builtins.property
    @jsii.member(jsii_name="tagStepDetailsInput")
    def tag_step_details_input(
        self,
    ) -> typing.Optional["TransferWorkflowStepsTagStepDetails"]:
        return typing.cast(typing.Optional["TransferWorkflowStepsTagStepDetails"], jsii.get(self, "tagStepDetailsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__100cd3331d15ae874f5c7e2a8875afe09a080eb9272fe41b89655cba7ba9e6a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[TransferWorkflowSteps, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[TransferWorkflowSteps, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[TransferWorkflowSteps, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__503bc381d204bc12d57b9b136ff064845378ce6793f1b3f087a06e74000f9280)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.transferWorkflow.TransferWorkflowStepsTagStepDetails",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "source_file_location": "sourceFileLocation",
        "tags": "tags",
    },
)
class TransferWorkflowStepsTagStepDetails:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        source_file_location: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["TransferWorkflowStepsTagStepDetailsTags", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#name TransferWorkflow#name}.
        :param source_file_location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#source_file_location TransferWorkflow#source_file_location}.
        :param tags: tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#tags TransferWorkflow#tags}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66e06f9dec853a465092e59cc5f38f5d77a6644e3a3497fbddd9f8f68e7c686b)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument source_file_location", value=source_file_location, expected_type=type_hints["source_file_location"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if source_file_location is not None:
            self._values["source_file_location"] = source_file_location
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#name TransferWorkflow#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_file_location(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#source_file_location TransferWorkflow#source_file_location}.'''
        result = self._values.get("source_file_location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["TransferWorkflowStepsTagStepDetailsTags"]]]:
        '''tags block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#tags TransferWorkflow#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["TransferWorkflowStepsTagStepDetailsTags"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransferWorkflowStepsTagStepDetails(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TransferWorkflowStepsTagStepDetailsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.transferWorkflow.TransferWorkflowStepsTagStepDetailsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5beba088e58dc804339781ed1f3c0ddd205dd33f04e52765c8a27411acfdd1c9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putTags")
    def put_tags(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["TransferWorkflowStepsTagStepDetailsTags", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8976869b710d50f7e269167f3d8a34b2005dbe768d337598a83dc97c064260e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTags", [value]))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetSourceFileLocation")
    def reset_source_file_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceFileLocation", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> "TransferWorkflowStepsTagStepDetailsTagsList":
        return typing.cast("TransferWorkflowStepsTagStepDetailsTagsList", jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceFileLocationInput")
    def source_file_location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceFileLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["TransferWorkflowStepsTagStepDetailsTags"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["TransferWorkflowStepsTagStepDetailsTags"]]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9046fc7d39d33c0cf18af6f84ed91ed7c92380b9241fffa6afcf765bbf17099)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="sourceFileLocation")
    def source_file_location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceFileLocation"))

    @source_file_location.setter
    def source_file_location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ea2f75381e1bf12e56aaee62ca9186616929f12af4b6979a39a9942bf000eaa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceFileLocation", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[TransferWorkflowStepsTagStepDetails]:
        return typing.cast(typing.Optional[TransferWorkflowStepsTagStepDetails], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[TransferWorkflowStepsTagStepDetails],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20f95b94fb3aae6cb5e195c5f448ab7f8f218e1ccd22e1c6bdc03c03cab7d646)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.transferWorkflow.TransferWorkflowStepsTagStepDetailsTags",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class TransferWorkflowStepsTagStepDetailsTags:
    def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#key TransferWorkflow#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#value TransferWorkflow#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e974ae278d8d28f0c1adbdf384d7f9171e55da9533a63d5f3bff54a581e5977c)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#key TransferWorkflow#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#value TransferWorkflow#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransferWorkflowStepsTagStepDetailsTags(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TransferWorkflowStepsTagStepDetailsTagsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.transferWorkflow.TransferWorkflowStepsTagStepDetailsTagsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5a74e244f4c6514a6f780f40b3474c1034de45ec1967c182f87739b5ab001058)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "TransferWorkflowStepsTagStepDetailsTagsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f95721272a35684dc33c6c503d0570a44c30bf167c4d24c8270c41b6c12fadf3)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("TransferWorkflowStepsTagStepDetailsTagsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3ac2a579f6ce14285acabdd07a4012fc6cbe4dfed9c6a8fe4c5f645f49e5b7b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c01aeb4772562f901b98589e996f5ff1cbc14aa88e5702dd785d187aac8aa77d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1b894210a14c03bbf1d772e3ff14e07274a0540c157841830f81e2695c2246e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[TransferWorkflowStepsTagStepDetailsTags]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[TransferWorkflowStepsTagStepDetailsTags]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[TransferWorkflowStepsTagStepDetailsTags]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be8788a31591dc09ebda235d4174be71f9083a94e374587553b1e6ebe14144d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class TransferWorkflowStepsTagStepDetailsTagsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.transferWorkflow.TransferWorkflowStepsTagStepDetailsTagsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__384b1200fd076a6604a14369636f379ac7574ef8be6c3b49681ffb605f519f7a)
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
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__196b2c6e311629e9f88a7d72af603740d7cd8f3c48e0aa4ced57cea840eb293e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15e9f87cef3cac70b150eb8d537cdc65e6fe12764b966d10a67f2e819c08c6d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[TransferWorkflowStepsTagStepDetailsTags, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[TransferWorkflowStepsTagStepDetailsTags, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[TransferWorkflowStepsTagStepDetailsTags, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23e3286298af25d317ece09811f4b143e9b947da4a9f94c4102514d7dc38c3af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "TransferWorkflow",
    "TransferWorkflowConfig",
    "TransferWorkflowOnExceptionSteps",
    "TransferWorkflowOnExceptionStepsCopyStepDetails",
    "TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocation",
    "TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationEfsFileLocation",
    "TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationEfsFileLocationOutputReference",
    "TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationOutputReference",
    "TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationS3FileLocation",
    "TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationS3FileLocationOutputReference",
    "TransferWorkflowOnExceptionStepsCopyStepDetailsOutputReference",
    "TransferWorkflowOnExceptionStepsCustomStepDetails",
    "TransferWorkflowOnExceptionStepsCustomStepDetailsOutputReference",
    "TransferWorkflowOnExceptionStepsDeleteStepDetails",
    "TransferWorkflowOnExceptionStepsDeleteStepDetailsOutputReference",
    "TransferWorkflowOnExceptionStepsList",
    "TransferWorkflowOnExceptionStepsOutputReference",
    "TransferWorkflowOnExceptionStepsTagStepDetails",
    "TransferWorkflowOnExceptionStepsTagStepDetailsOutputReference",
    "TransferWorkflowOnExceptionStepsTagStepDetailsTags",
    "TransferWorkflowOnExceptionStepsTagStepDetailsTagsList",
    "TransferWorkflowOnExceptionStepsTagStepDetailsTagsOutputReference",
    "TransferWorkflowSteps",
    "TransferWorkflowStepsCopyStepDetails",
    "TransferWorkflowStepsCopyStepDetailsDestinationFileLocation",
    "TransferWorkflowStepsCopyStepDetailsDestinationFileLocationEfsFileLocation",
    "TransferWorkflowStepsCopyStepDetailsDestinationFileLocationEfsFileLocationOutputReference",
    "TransferWorkflowStepsCopyStepDetailsDestinationFileLocationOutputReference",
    "TransferWorkflowStepsCopyStepDetailsDestinationFileLocationS3FileLocation",
    "TransferWorkflowStepsCopyStepDetailsDestinationFileLocationS3FileLocationOutputReference",
    "TransferWorkflowStepsCopyStepDetailsOutputReference",
    "TransferWorkflowStepsCustomStepDetails",
    "TransferWorkflowStepsCustomStepDetailsOutputReference",
    "TransferWorkflowStepsDeleteStepDetails",
    "TransferWorkflowStepsDeleteStepDetailsOutputReference",
    "TransferWorkflowStepsList",
    "TransferWorkflowStepsOutputReference",
    "TransferWorkflowStepsTagStepDetails",
    "TransferWorkflowStepsTagStepDetailsOutputReference",
    "TransferWorkflowStepsTagStepDetailsTags",
    "TransferWorkflowStepsTagStepDetailsTagsList",
    "TransferWorkflowStepsTagStepDetailsTagsOutputReference",
]

publication.publish()

def _typecheckingstub__c9d6f2b7bb4a7359f88f1dbf67426a4056cb2e5034a88d1349419a4157b3eb27(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    steps: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[TransferWorkflowSteps, typing.Dict[builtins.str, typing.Any]]]],
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    on_exception_steps: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[TransferWorkflowOnExceptionSteps, typing.Dict[builtins.str, typing.Any]]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
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

def _typecheckingstub__bcd93dc63c4035a3281cd70a08164036c7bc8055fb7be04cd6a571402f28c91c(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[TransferWorkflowOnExceptionSteps, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93ce3f271f88390eb14459830eda0e030d308f0ac059857f677fa5eb1fc2ecdf(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[TransferWorkflowSteps, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b7b4df8f2bbc915a6ada34299c9476118e5b579f7aebdc7013fff36039889f6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02eddb6decd435dd7920687ad9981873f6f164ce541d55bd6c990d5b184d7240(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3e900035fb0487af3dc3cca5e6a4839ebace1079617d2b6467f1fa6b137c260(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bce9f7ede8ded0ecb927a108247df06cfaba92f25dbe1576cd27f2b9ac1f1963(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6332750adf44b05132732f9264f73724387af4a0006169f3077f9e5c02e16c88(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    steps: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[TransferWorkflowSteps, typing.Dict[builtins.str, typing.Any]]]],
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    on_exception_steps: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[TransferWorkflowOnExceptionSteps, typing.Dict[builtins.str, typing.Any]]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c6b846e517f707976208e684304ca77d0f37021253b4e003ba3dbc61dc0c38b(
    *,
    type: builtins.str,
    copy_step_details: typing.Optional[typing.Union[TransferWorkflowOnExceptionStepsCopyStepDetails, typing.Dict[builtins.str, typing.Any]]] = None,
    custom_step_details: typing.Optional[typing.Union[TransferWorkflowOnExceptionStepsCustomStepDetails, typing.Dict[builtins.str, typing.Any]]] = None,
    delete_step_details: typing.Optional[typing.Union[TransferWorkflowOnExceptionStepsDeleteStepDetails, typing.Dict[builtins.str, typing.Any]]] = None,
    tag_step_details: typing.Optional[typing.Union[TransferWorkflowOnExceptionStepsTagStepDetails, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b096881d5a19b8b9f3907e362b62da865072e439d517194594624189bfea583(
    *,
    destination_file_location: typing.Optional[typing.Union[TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocation, typing.Dict[builtins.str, typing.Any]]] = None,
    name: typing.Optional[builtins.str] = None,
    overwrite_existing: typing.Optional[builtins.str] = None,
    source_file_location: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a515a239a9f90c0dab3da8ff16d5c676c42d9d6c2b2eda48269402fcf237611(
    *,
    efs_file_location: typing.Optional[typing.Union[TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationEfsFileLocation, typing.Dict[builtins.str, typing.Any]]] = None,
    s3_file_location: typing.Optional[typing.Union[TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationS3FileLocation, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f90100ddd528701a40bc2b013a02d2d625ef65c6f25eaeade82e5ee30ae4a15(
    *,
    file_system_id: typing.Optional[builtins.str] = None,
    path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ba6391517ca527a27dcff93da12537c841258660d51e68dd81c039a4986948d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__166b944fca393b1a94ecde768653b26db7ea9e03eed35f9700f0252d1f8a4f26(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2615a87faabe0c0ce84302b979d1845b4562ebebc9daa1468a18c6221d2a04be(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67cfb0ecfa1dc9da1c15f2eb3c471d9440d602f5186ca7af03b320bd214747ac(
    value: typing.Optional[TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationEfsFileLocation],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9abd82c4e1e77c1c3453501df6f6dacb036c000eeabdcc51fde5f8c70ce6e6ec(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c45565b963bae7d2e21e100949ccc28ada96ab6848e8321c23755c4f261ba34(
    value: typing.Optional[TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocation],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4364cb35a90e5fa7bf2266f57f196783d47b5e64617ec54efeefcf57e31e29ee(
    *,
    bucket: typing.Optional[builtins.str] = None,
    key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ac18357aeb4231dab1013984523b25e7e686e72e2b97a574706ccc7f08be08d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67a001d03f3d6b06a3176fb490bceb76ef033359bd59fa45c378e293a0bd58f4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1de486f3e5a50e1097d4122585174e83d189703fd89d7af7576dcbc38a7ecde1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__665bf568d496e5efcbb732f709b973d5fb4e5f19a14146cbbc80ef9ab71d3400(
    value: typing.Optional[TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationS3FileLocation],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b313645f29d00c686b5ecad84bf0fcee9d3847c957efe67bddec3f3df7c6cf8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2a766ea155d4c3f2ed1da773b5f7525cda06c2f003105999c9331d2e2ac86ae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4966a6820922a7ea3971910341d1b6f6d6e65bcab9fc9fea6a8ed0f6b312d5d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf4b736bbbd05f539db1037b9bbc9ed9e9398b0e23d73600a449d526e6ea2029(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6693bcc674bedff9f1df08dc505098d68d27c0d6eebb62d12e29bf42e641319(
    value: typing.Optional[TransferWorkflowOnExceptionStepsCopyStepDetails],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__395fea0fc841dfe6272d9720466b4e5fe0278736499fe9396af569ce98374bb6(
    *,
    name: typing.Optional[builtins.str] = None,
    source_file_location: typing.Optional[builtins.str] = None,
    target: typing.Optional[builtins.str] = None,
    timeout_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1114eee3c3bd19260804673733354abb57d47ccaf36acabb14aebd50ed6de1c6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__276e11a87b4b21ebd4ae8ca0f63dda4d9233045cae3829006910a645f9a5316f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f7aa46ed4c5fa695679f7789c0a71fa36a499f86a312e81c44cfc4447decc43(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afc366d3fc1bf39845245da0a08f4c34843c97a6bcfefb249b12fb38ccb70728(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e0785b1f4833413ea215aba1abd731d7b31eca628c3d449c20d64e2252aca96(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__966d839ba4743b798376d7ce2a3adc36b81b41782337f6edb4f5ac9615ab3c2c(
    value: typing.Optional[TransferWorkflowOnExceptionStepsCustomStepDetails],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e86a6ff798fe174119f51b0698c124144100be67cc19f0067b0a896342b403e(
    *,
    name: typing.Optional[builtins.str] = None,
    source_file_location: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb621bfb471b444fdd8e206a15f4ad3c8e60588ab20da8854e1dc6408bad890b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f08c5a18d537a8b96120d88f8ffb0ac98454f498dbb553900a52fab4a7222842(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f1e00179b27760ad2cdeab150e3abf75ec5570848c0faccaa325ed3372c7e55(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aba932bdbde0f0167bcff68b245239ba08b3ef190092370d1875d2481fabbe64(
    value: typing.Optional[TransferWorkflowOnExceptionStepsDeleteStepDetails],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3d0bad5ca0e426a797fe74ed6e4481e36f8a89ee433f1794f7c053d9af68526(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9585e681ec0d577fe294037e645fe67d56c24720110fa53148f1c53eb4628cd5(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9074c2b7efb74aef9d2e961229b1e965639e6d56f462f5f774e83797f1506299(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7912531e3d606baff4c355653854ee4841d3bfcf49d5fb0af01ec6f2701d8fd2(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b8b12ce36d9483b9ec05446990a9c6c6ec1bdb79259b288aac6992765653eb3(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d80963edc30b9df439d15a2e8c238fa58d2b92bba9065eb93d2c72c5baf6806(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[TransferWorkflowOnExceptionSteps]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85ef5d2d6beb1b0d907c9bec0ae54022ba16966adfe07bb9d9e31ecc4f723b1f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a89f6eaecac5a870f8876c4e414751a8cc493d4be29c0704249af92f0240ee34(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74b8ee568113f4ea1e69d534252a1f2ae996da143902c614f2b83dd00dd5312e(
    value: typing.Optional[typing.Union[TransferWorkflowOnExceptionSteps, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c98bd22be5efab6cf2a53f5a76296681dff1c3d9bdcaf8777d35926b53d50bf1(
    *,
    name: typing.Optional[builtins.str] = None,
    source_file_location: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[TransferWorkflowOnExceptionStepsTagStepDetailsTags, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec5894b709efe12e56d78d02f72d6f5db6f4fbaba37a66902d098467e9c49c7e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f766b7a064c21b88b70ea5ca0f9a86a4de6058150877ee408a63837af6af8b0(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[TransferWorkflowOnExceptionStepsTagStepDetailsTags, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79f954b7de487aca7a332f335f1606546f98bc87a8f97f6de5b3c43435cfe3b0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc4811284c327604abf057679b9acb711ca4ac31a2fef47d27678aaf5327e2ea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__351d3edc8a5616f802f3615925749bf4f91ef34b3dfa7bd5782f3cbce33af729(
    value: typing.Optional[TransferWorkflowOnExceptionStepsTagStepDetails],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b814195b3904ecdb9d0737ad7405a0d15de7b4103a7e9da670b964c2fe2a771(
    *,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3c6107c3a46738974d2380d80e939e22ae74a0b833a3d2c947eed39ae57c849(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9686140de42a345e275a4e835b62d00fc9b5dad905f7ee01d80d01d7654c848e(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7edf2b99544ba00c64fe5870bebd2da693ad998790ee34d4e188ce4a7bd12bb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a478a226b703581d403b6fb55b50d75e760ae68865745f32712140f31dd1426(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab1dde8bb519e0352c17b65b7366a0fe910618b6b78853fb002154312e09880b(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02524976489b86bcd03e2a98e0445594aec62e94953736c5fd3b740496b45778(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[TransferWorkflowOnExceptionStepsTagStepDetailsTags]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8d61c9a358cf08ea1da4b7445a8b35c98bee1dfd266fc62321f03000ef26f66(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b6ed9265a07cbec24afb3f55ad8e5068a9f9720a9e13c4ae26568aed0711359(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20180f542bb1d03f2c331efc99ed74e7ff200954eb5d5fa1423987cf24988886(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ab0778ca8205144eb04b5272a26204a06b19a4e08dd3bd120ba13e1772d9378(
    value: typing.Optional[typing.Union[TransferWorkflowOnExceptionStepsTagStepDetailsTags, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1927df0b5ded0553dc87d4bc1e7f9a06693581a197829ffde1deb355ee42ee7(
    *,
    type: builtins.str,
    copy_step_details: typing.Optional[typing.Union[TransferWorkflowStepsCopyStepDetails, typing.Dict[builtins.str, typing.Any]]] = None,
    custom_step_details: typing.Optional[typing.Union[TransferWorkflowStepsCustomStepDetails, typing.Dict[builtins.str, typing.Any]]] = None,
    delete_step_details: typing.Optional[typing.Union[TransferWorkflowStepsDeleteStepDetails, typing.Dict[builtins.str, typing.Any]]] = None,
    tag_step_details: typing.Optional[typing.Union[TransferWorkflowStepsTagStepDetails, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1d930ce67d59cc205f8e515c8639f41ef7e50b226cae773b20ca846913f1165(
    *,
    destination_file_location: typing.Optional[typing.Union[TransferWorkflowStepsCopyStepDetailsDestinationFileLocation, typing.Dict[builtins.str, typing.Any]]] = None,
    name: typing.Optional[builtins.str] = None,
    overwrite_existing: typing.Optional[builtins.str] = None,
    source_file_location: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b56b3db6f4432e4d453d4c0049b50e52d4d61f5a82221d7e239db2f1e53c5756(
    *,
    efs_file_location: typing.Optional[typing.Union[TransferWorkflowStepsCopyStepDetailsDestinationFileLocationEfsFileLocation, typing.Dict[builtins.str, typing.Any]]] = None,
    s3_file_location: typing.Optional[typing.Union[TransferWorkflowStepsCopyStepDetailsDestinationFileLocationS3FileLocation, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28753952b2a399b788e7e0a347c26c2dea438c5d59bb7e5c73f8297795a998c0(
    *,
    file_system_id: typing.Optional[builtins.str] = None,
    path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebd1a24a9c9b4937a83e90eb78b811b58f25fbd1a17583f90d0a4ec0af30c6b2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d48e19a951b8d8ee16151b30e03647decc37655c8a5780420216717761804df4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57b7608ee31d7c29872f46841c29eea37ecceb5cb4f64336f9ed0e5bd61d9e00(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d89719768571d3e737b6b73c1b2c451ec53ec4638d0ab383933b3a37ad98cb1(
    value: typing.Optional[TransferWorkflowStepsCopyStepDetailsDestinationFileLocationEfsFileLocation],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58566bb457afbf6fcb3a75aefc65310efba9b69e2cd1903ce48b72aa5f716fff(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6276eabec7ca1e6710528a7b5762c33b70090a4a37083327dd1581b298e6a31b(
    value: typing.Optional[TransferWorkflowStepsCopyStepDetailsDestinationFileLocation],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2c61b15e89dd60bed93573f65d8618e9b58a298751d668ad3cb731103fcc9ba(
    *,
    bucket: typing.Optional[builtins.str] = None,
    key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee9d3c6ef43f7c43da30c3291b42af46bbaf2e61deac0c5e6558549012a5bc65(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0b13aba046a2ddc603f7442535256c13a7a2677260a11ee8386f1650fa4856e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ebe6c5771ffcdaecf9cb63d1bab9e2c1af2dc9d766073d24e0d62cee50ccad1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97c56f3314ea4f8313f1584572b31fd20c7d6be884b98f65df174b4e7512551b(
    value: typing.Optional[TransferWorkflowStepsCopyStepDetailsDestinationFileLocationS3FileLocation],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36d5468b61e8ff42ff73ccae62598386e34508443b48f5ff0b40cd4975d02ad5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc1bf50e1af52b4da410951d1ed7946b330642d47830c0457ee327359b317795(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c991b8ace67d92653e26cfe122d092a3be45ec83cbeef10db9a3eabdfc70d1f6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53ae6bd10685ab5dbb04b22ffe8b24e6e47259ac9f77101f6fe164d85b47e230(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d1c63c5a58f7ecde7e1f921142404eeddbe65aab23a54a2681bdb7ef9aba540(
    value: typing.Optional[TransferWorkflowStepsCopyStepDetails],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__296d334727db5906b7fef9c564b0685bb47befa69b6283bf5e47d00e17562c7c(
    *,
    name: typing.Optional[builtins.str] = None,
    source_file_location: typing.Optional[builtins.str] = None,
    target: typing.Optional[builtins.str] = None,
    timeout_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06bd18b1ceb332c72c6505089c7d9c7d1e51768ce21a914bb5e48d4aa452a80b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0aa37165098cf34c6e1ec256e2e848afee03c85a5b658960080dc43b8bec4189(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83f7e31307ccdff27e931d81d34394f8e5a457b8a322886ff2d293f8c2b76ac7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d98f665e6a1b4cff4e9ca0a15eb5847d66a982b9b960d90e91f582c1ec1d72d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e06d71b2ffcd9bf4b529a53ed40ba518c3984342ca7f5606ca2e716d15e638ab(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8b5cd7de7d636c7a3d850a57783f7ad439345ebd2a017b8b45b4a8f04e7478c(
    value: typing.Optional[TransferWorkflowStepsCustomStepDetails],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca24fa27d7c5c45fa7ee7f3adbde9506ee6f4bd9f8c887e6a4c52bd9e4eae9f2(
    *,
    name: typing.Optional[builtins.str] = None,
    source_file_location: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04e370f59edb77c830c3881e8561105a3fd331bc43a1300752599319839f2f0e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bc74bdfdd6ea17df68216a2fcbd018767c064847023245f22cc2d5525bf19a6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__873f08e6c9cde75e44e6215aace9e425b0e7ad72fbaa2b4f3b2cfdd971a44954(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c602da39ab8cd99c6d0dff241a329a0469e3356be7ab7e70d9cd178810a8291a(
    value: typing.Optional[TransferWorkflowStepsDeleteStepDetails],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58724a787dcb670fcdfc1037cb67b589731170b6c290a787f4f67cf2b1e513dc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fe5555a2b9eefd60423b65052145a7946256a28ec0ac68e5ed0ed58becb27d6(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2448d16a68199c7ef92b38f42677a8d2960788c66115a1891aac5d9ba4f61c21(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb287e7af550754a994e04e346149447bd77cae8353f8d97e2e664de5eb5fca9(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ea6a809a41413aeefcb21183187feacb21c2d44da650a68185ec93caab017ab(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36cb97278f54b4adb2cf29b823b3bd0a19580cd44f85ebe48550b023ab4bb4bf(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[TransferWorkflowSteps]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e7abbb19ffba41d5bf9522dbd40d454ee64ccdec2c6507b31cb75c402016f82(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__100cd3331d15ae874f5c7e2a8875afe09a080eb9272fe41b89655cba7ba9e6a2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__503bc381d204bc12d57b9b136ff064845378ce6793f1b3f087a06e74000f9280(
    value: typing.Optional[typing.Union[TransferWorkflowSteps, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66e06f9dec853a465092e59cc5f38f5d77a6644e3a3497fbddd9f8f68e7c686b(
    *,
    name: typing.Optional[builtins.str] = None,
    source_file_location: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[TransferWorkflowStepsTagStepDetailsTags, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5beba088e58dc804339781ed1f3c0ddd205dd33f04e52765c8a27411acfdd1c9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8976869b710d50f7e269167f3d8a34b2005dbe768d337598a83dc97c064260e0(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[TransferWorkflowStepsTagStepDetailsTags, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9046fc7d39d33c0cf18af6f84ed91ed7c92380b9241fffa6afcf765bbf17099(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ea2f75381e1bf12e56aaee62ca9186616929f12af4b6979a39a9942bf000eaa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20f95b94fb3aae6cb5e195c5f448ab7f8f218e1ccd22e1c6bdc03c03cab7d646(
    value: typing.Optional[TransferWorkflowStepsTagStepDetails],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e974ae278d8d28f0c1adbdf384d7f9171e55da9533a63d5f3bff54a581e5977c(
    *,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a74e244f4c6514a6f780f40b3474c1034de45ec1967c182f87739b5ab001058(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f95721272a35684dc33c6c503d0570a44c30bf167c4d24c8270c41b6c12fadf3(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3ac2a579f6ce14285acabdd07a4012fc6cbe4dfed9c6a8fe4c5f645f49e5b7b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c01aeb4772562f901b98589e996f5ff1cbc14aa88e5702dd785d187aac8aa77d(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b894210a14c03bbf1d772e3ff14e07274a0540c157841830f81e2695c2246e1(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be8788a31591dc09ebda235d4174be71f9083a94e374587553b1e6ebe14144d2(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[TransferWorkflowStepsTagStepDetailsTags]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__384b1200fd076a6604a14369636f379ac7574ef8be6c3b49681ffb605f519f7a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__196b2c6e311629e9f88a7d72af603740d7cd8f3c48e0aa4ced57cea840eb293e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15e9f87cef3cac70b150eb8d537cdc65e6fe12764b966d10a67f2e819c08c6d9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23e3286298af25d317ece09811f4b143e9b947da4a9f94c4102514d7dc38c3af(
    value: typing.Optional[typing.Union[TransferWorkflowStepsTagStepDetailsTags, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
