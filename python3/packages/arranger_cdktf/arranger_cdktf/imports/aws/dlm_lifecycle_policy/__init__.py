'''
# `aws_dlm_lifecycle_policy`

Refer to the Terraform Registory for docs: [`aws_dlm_lifecycle_policy`](https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy).
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


class DlmLifecyclePolicy(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dlmLifecyclePolicy.DlmLifecyclePolicy",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy aws_dlm_lifecycle_policy}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        description: builtins.str,
        execution_role_arn: builtins.str,
        policy_details: typing.Union["DlmLifecyclePolicyPolicyDetails", typing.Dict[builtins.str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy aws_dlm_lifecycle_policy} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#description DlmLifecyclePolicy#description}.
        :param execution_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#execution_role_arn DlmLifecyclePolicy#execution_role_arn}.
        :param policy_details: policy_details block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#policy_details DlmLifecyclePolicy#policy_details}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#id DlmLifecyclePolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#state DlmLifecyclePolicy#state}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#tags DlmLifecyclePolicy#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#tags_all DlmLifecyclePolicy#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a711b3694b2b58c3a2eafae18cca5fef5ec5b0cb85bf0b1d7c76d4ebe733345)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DlmLifecyclePolicyConfig(
            description=description,
            execution_role_arn=execution_role_arn,
            policy_details=policy_details,
            id=id,
            state=state,
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

    @jsii.member(jsii_name="putPolicyDetails")
    def put_policy_details(
        self,
        *,
        action: typing.Optional[typing.Union["DlmLifecyclePolicyPolicyDetailsAction", typing.Dict[builtins.str, typing.Any]]] = None,
        event_source: typing.Optional[typing.Union["DlmLifecyclePolicyPolicyDetailsEventSource", typing.Dict[builtins.str, typing.Any]]] = None,
        parameters: typing.Optional[typing.Union["DlmLifecyclePolicyPolicyDetailsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        policy_type: typing.Optional[builtins.str] = None,
        resource_locations: typing.Optional[typing.Sequence[builtins.str]] = None,
        resource_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        schedule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DlmLifecyclePolicyPolicyDetailsSchedule", typing.Dict[builtins.str, typing.Any]]]]] = None,
        target_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param action: action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#action DlmLifecyclePolicy#action}
        :param event_source: event_source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#event_source DlmLifecyclePolicy#event_source}
        :param parameters: parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#parameters DlmLifecyclePolicy#parameters}
        :param policy_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#policy_type DlmLifecyclePolicy#policy_type}.
        :param resource_locations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#resource_locations DlmLifecyclePolicy#resource_locations}.
        :param resource_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#resource_types DlmLifecyclePolicy#resource_types}.
        :param schedule: schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#schedule DlmLifecyclePolicy#schedule}
        :param target_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#target_tags DlmLifecyclePolicy#target_tags}.
        '''
        value = DlmLifecyclePolicyPolicyDetails(
            action=action,
            event_source=event_source,
            parameters=parameters,
            policy_type=policy_type,
            resource_locations=resource_locations,
            resource_types=resource_types,
            schedule=schedule,
            target_tags=target_tags,
        )

        return typing.cast(None, jsii.invoke(self, "putPolicyDetails", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetState")
    def reset_state(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetState", []))

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
    @jsii.member(jsii_name="policyDetails")
    def policy_details(self) -> "DlmLifecyclePolicyPolicyDetailsOutputReference":
        return typing.cast("DlmLifecyclePolicyPolicyDetailsOutputReference", jsii.get(self, "policyDetails"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="executionRoleArnInput")
    def execution_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "executionRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="policyDetailsInput")
    def policy_details_input(
        self,
    ) -> typing.Optional["DlmLifecyclePolicyPolicyDetails"]:
        return typing.cast(typing.Optional["DlmLifecyclePolicyPolicyDetails"], jsii.get(self, "policyDetailsInput"))

    @builtins.property
    @jsii.member(jsii_name="stateInput")
    def state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stateInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__cb51c46523bc4dfa848063df9e12153b679169d0f52947ba5c35261d2324cc1d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="executionRoleArn")
    def execution_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "executionRoleArn"))

    @execution_role_arn.setter
    def execution_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8224ec627227a5ca04eda7fb4ddcd39613083201ad3f98a0f0ef2d25fd53f59)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__001fd7ce3bf9a783b2e59ba343e55a24f1483d393d226d648f092ce04c2ae071)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @state.setter
    def state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__711db73513a2e3feff3baa6d90e6bd0ae0ccf2a0afd7edc2e6d31fe7ab6e2ea1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "state", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb752cfabe1cd3871753b8b40c4dfbad9669060160beea013c594f12024f5a3f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06f651a57513a0d108d4d0388e2e3bb4a5c8c616d800ccbd6c69702b1eb4dbce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.dlmLifecyclePolicy.DlmLifecyclePolicyConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "description": "description",
        "execution_role_arn": "executionRoleArn",
        "policy_details": "policyDetails",
        "id": "id",
        "state": "state",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class DlmLifecyclePolicyConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        description: builtins.str,
        execution_role_arn: builtins.str,
        policy_details: typing.Union["DlmLifecyclePolicyPolicyDetails", typing.Dict[builtins.str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
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
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#description DlmLifecyclePolicy#description}.
        :param execution_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#execution_role_arn DlmLifecyclePolicy#execution_role_arn}.
        :param policy_details: policy_details block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#policy_details DlmLifecyclePolicy#policy_details}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#id DlmLifecyclePolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#state DlmLifecyclePolicy#state}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#tags DlmLifecyclePolicy#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#tags_all DlmLifecyclePolicy#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(policy_details, dict):
            policy_details = DlmLifecyclePolicyPolicyDetails(**policy_details)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f5d54b72101466ce55a8b0c6568181b2a83ed98514f38e8b7eac7a35e8b2923)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument execution_role_arn", value=execution_role_arn, expected_type=type_hints["execution_role_arn"])
            check_type(argname="argument policy_details", value=policy_details, expected_type=type_hints["policy_details"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument state", value=state, expected_type=type_hints["state"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "execution_role_arn": execution_role_arn,
            "policy_details": policy_details,
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
        if state is not None:
            self._values["state"] = state
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
    def description(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#description DlmLifecyclePolicy#description}.'''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def execution_role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#execution_role_arn DlmLifecyclePolicy#execution_role_arn}.'''
        result = self._values.get("execution_role_arn")
        assert result is not None, "Required property 'execution_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_details(self) -> "DlmLifecyclePolicyPolicyDetails":
        '''policy_details block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#policy_details DlmLifecyclePolicy#policy_details}
        '''
        result = self._values.get("policy_details")
        assert result is not None, "Required property 'policy_details' is missing"
        return typing.cast("DlmLifecyclePolicyPolicyDetails", result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#id DlmLifecyclePolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def state(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#state DlmLifecyclePolicy#state}.'''
        result = self._values.get("state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#tags DlmLifecyclePolicy#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#tags_all DlmLifecyclePolicy#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DlmLifecyclePolicyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.dlmLifecyclePolicy.DlmLifecyclePolicyPolicyDetails",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "event_source": "eventSource",
        "parameters": "parameters",
        "policy_type": "policyType",
        "resource_locations": "resourceLocations",
        "resource_types": "resourceTypes",
        "schedule": "schedule",
        "target_tags": "targetTags",
    },
)
class DlmLifecyclePolicyPolicyDetails:
    def __init__(
        self,
        *,
        action: typing.Optional[typing.Union["DlmLifecyclePolicyPolicyDetailsAction", typing.Dict[builtins.str, typing.Any]]] = None,
        event_source: typing.Optional[typing.Union["DlmLifecyclePolicyPolicyDetailsEventSource", typing.Dict[builtins.str, typing.Any]]] = None,
        parameters: typing.Optional[typing.Union["DlmLifecyclePolicyPolicyDetailsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        policy_type: typing.Optional[builtins.str] = None,
        resource_locations: typing.Optional[typing.Sequence[builtins.str]] = None,
        resource_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        schedule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DlmLifecyclePolicyPolicyDetailsSchedule", typing.Dict[builtins.str, typing.Any]]]]] = None,
        target_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param action: action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#action DlmLifecyclePolicy#action}
        :param event_source: event_source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#event_source DlmLifecyclePolicy#event_source}
        :param parameters: parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#parameters DlmLifecyclePolicy#parameters}
        :param policy_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#policy_type DlmLifecyclePolicy#policy_type}.
        :param resource_locations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#resource_locations DlmLifecyclePolicy#resource_locations}.
        :param resource_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#resource_types DlmLifecyclePolicy#resource_types}.
        :param schedule: schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#schedule DlmLifecyclePolicy#schedule}
        :param target_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#target_tags DlmLifecyclePolicy#target_tags}.
        '''
        if isinstance(action, dict):
            action = DlmLifecyclePolicyPolicyDetailsAction(**action)
        if isinstance(event_source, dict):
            event_source = DlmLifecyclePolicyPolicyDetailsEventSource(**event_source)
        if isinstance(parameters, dict):
            parameters = DlmLifecyclePolicyPolicyDetailsParameters(**parameters)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19c9abf860401b5a2a67ec8023fa0c4f5af72cd2befd2cb184798abb8ec97cd0)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument event_source", value=event_source, expected_type=type_hints["event_source"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument policy_type", value=policy_type, expected_type=type_hints["policy_type"])
            check_type(argname="argument resource_locations", value=resource_locations, expected_type=type_hints["resource_locations"])
            check_type(argname="argument resource_types", value=resource_types, expected_type=type_hints["resource_types"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            check_type(argname="argument target_tags", value=target_tags, expected_type=type_hints["target_tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if action is not None:
            self._values["action"] = action
        if event_source is not None:
            self._values["event_source"] = event_source
        if parameters is not None:
            self._values["parameters"] = parameters
        if policy_type is not None:
            self._values["policy_type"] = policy_type
        if resource_locations is not None:
            self._values["resource_locations"] = resource_locations
        if resource_types is not None:
            self._values["resource_types"] = resource_types
        if schedule is not None:
            self._values["schedule"] = schedule
        if target_tags is not None:
            self._values["target_tags"] = target_tags

    @builtins.property
    def action(self) -> typing.Optional["DlmLifecyclePolicyPolicyDetailsAction"]:
        '''action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#action DlmLifecyclePolicy#action}
        '''
        result = self._values.get("action")
        return typing.cast(typing.Optional["DlmLifecyclePolicyPolicyDetailsAction"], result)

    @builtins.property
    def event_source(
        self,
    ) -> typing.Optional["DlmLifecyclePolicyPolicyDetailsEventSource"]:
        '''event_source block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#event_source DlmLifecyclePolicy#event_source}
        '''
        result = self._values.get("event_source")
        return typing.cast(typing.Optional["DlmLifecyclePolicyPolicyDetailsEventSource"], result)

    @builtins.property
    def parameters(
        self,
    ) -> typing.Optional["DlmLifecyclePolicyPolicyDetailsParameters"]:
        '''parameters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#parameters DlmLifecyclePolicy#parameters}
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional["DlmLifecyclePolicyPolicyDetailsParameters"], result)

    @builtins.property
    def policy_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#policy_type DlmLifecyclePolicy#policy_type}.'''
        result = self._values.get("policy_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_locations(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#resource_locations DlmLifecyclePolicy#resource_locations}.'''
        result = self._values.get("resource_locations")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def resource_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#resource_types DlmLifecyclePolicy#resource_types}.'''
        result = self._values.get("resource_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def schedule(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DlmLifecyclePolicyPolicyDetailsSchedule"]]]:
        '''schedule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#schedule DlmLifecyclePolicy#schedule}
        '''
        result = self._values.get("schedule")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DlmLifecyclePolicyPolicyDetailsSchedule"]]], result)

    @builtins.property
    def target_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#target_tags DlmLifecyclePolicy#target_tags}.'''
        result = self._values.get("target_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DlmLifecyclePolicyPolicyDetails(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.dlmLifecyclePolicy.DlmLifecyclePolicyPolicyDetailsAction",
    jsii_struct_bases=[],
    name_mapping={"cross_region_copy": "crossRegionCopy", "name": "name"},
)
class DlmLifecyclePolicyPolicyDetailsAction:
    def __init__(
        self,
        *,
        cross_region_copy: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopy", typing.Dict[builtins.str, typing.Any]]]],
        name: builtins.str,
    ) -> None:
        '''
        :param cross_region_copy: cross_region_copy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#cross_region_copy DlmLifecyclePolicy#cross_region_copy}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#name DlmLifecyclePolicy#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c76b635fae27e8b463fdaf324ab8edfdfd9d4bad102dfe72a54c075a109c996)
            check_type(argname="argument cross_region_copy", value=cross_region_copy, expected_type=type_hints["cross_region_copy"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cross_region_copy": cross_region_copy,
            "name": name,
        }

    @builtins.property
    def cross_region_copy(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopy"]]:
        '''cross_region_copy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#cross_region_copy DlmLifecyclePolicy#cross_region_copy}
        '''
        result = self._values.get("cross_region_copy")
        assert result is not None, "Required property 'cross_region_copy' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopy"]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#name DlmLifecyclePolicy#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DlmLifecyclePolicyPolicyDetailsAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.dlmLifecyclePolicy.DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopy",
    jsii_struct_bases=[],
    name_mapping={
        "encryption_configuration": "encryptionConfiguration",
        "target": "target",
        "retain_rule": "retainRule",
    },
)
class DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopy:
    def __init__(
        self,
        *,
        encryption_configuration: typing.Union["DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyEncryptionConfiguration", typing.Dict[builtins.str, typing.Any]],
        target: builtins.str,
        retain_rule: typing.Optional[typing.Union["DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyRetainRule", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param encryption_configuration: encryption_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#encryption_configuration DlmLifecyclePolicy#encryption_configuration}
        :param target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#target DlmLifecyclePolicy#target}.
        :param retain_rule: retain_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#retain_rule DlmLifecyclePolicy#retain_rule}
        '''
        if isinstance(encryption_configuration, dict):
            encryption_configuration = DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyEncryptionConfiguration(**encryption_configuration)
        if isinstance(retain_rule, dict):
            retain_rule = DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyRetainRule(**retain_rule)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d12af520dd34fa3964de49a7a5c3382d766a667c3b04abecd8742357cdaf4b24)
            check_type(argname="argument encryption_configuration", value=encryption_configuration, expected_type=type_hints["encryption_configuration"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument retain_rule", value=retain_rule, expected_type=type_hints["retain_rule"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "encryption_configuration": encryption_configuration,
            "target": target,
        }
        if retain_rule is not None:
            self._values["retain_rule"] = retain_rule

    @builtins.property
    def encryption_configuration(
        self,
    ) -> "DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyEncryptionConfiguration":
        '''encryption_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#encryption_configuration DlmLifecyclePolicy#encryption_configuration}
        '''
        result = self._values.get("encryption_configuration")
        assert result is not None, "Required property 'encryption_configuration' is missing"
        return typing.cast("DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyEncryptionConfiguration", result)

    @builtins.property
    def target(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#target DlmLifecyclePolicy#target}.'''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def retain_rule(
        self,
    ) -> typing.Optional["DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyRetainRule"]:
        '''retain_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#retain_rule DlmLifecyclePolicy#retain_rule}
        '''
        result = self._values.get("retain_rule")
        return typing.cast(typing.Optional["DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyRetainRule"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.dlmLifecyclePolicy.DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyEncryptionConfiguration",
    jsii_struct_bases=[],
    name_mapping={"cmk_arn": "cmkArn", "encrypted": "encrypted"},
)
class DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyEncryptionConfiguration:
    def __init__(
        self,
        *,
        cmk_arn: typing.Optional[builtins.str] = None,
        encrypted: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param cmk_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#cmk_arn DlmLifecyclePolicy#cmk_arn}.
        :param encrypted: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#encrypted DlmLifecyclePolicy#encrypted}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e15a1c3b0d06cde048b58525a1c8aae1e82ffd0f1c0a515e15246619f4a83b7b)
            check_type(argname="argument cmk_arn", value=cmk_arn, expected_type=type_hints["cmk_arn"])
            check_type(argname="argument encrypted", value=encrypted, expected_type=type_hints["encrypted"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cmk_arn is not None:
            self._values["cmk_arn"] = cmk_arn
        if encrypted is not None:
            self._values["encrypted"] = encrypted

    @builtins.property
    def cmk_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#cmk_arn DlmLifecyclePolicy#cmk_arn}.'''
        result = self._values.get("cmk_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encrypted(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#encrypted DlmLifecyclePolicy#encrypted}.'''
        result = self._values.get("encrypted")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyEncryptionConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyEncryptionConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dlmLifecyclePolicy.DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyEncryptionConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f19293be56ab2aa65632832d6ba4f5ec59d1fefa286f1475c49e105815a7e529)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCmkArn")
    def reset_cmk_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCmkArn", []))

    @jsii.member(jsii_name="resetEncrypted")
    def reset_encrypted(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncrypted", []))

    @builtins.property
    @jsii.member(jsii_name="cmkArnInput")
    def cmk_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cmkArnInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptedInput")
    def encrypted_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "encryptedInput"))

    @builtins.property
    @jsii.member(jsii_name="cmkArn")
    def cmk_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cmkArn"))

    @cmk_arn.setter
    def cmk_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d419f8960f00950eded7b5be42018c9593657cc6dd6057acebc89f98b162489a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cmkArn", value)

    @builtins.property
    @jsii.member(jsii_name="encrypted")
    def encrypted(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "encrypted"))

    @encrypted.setter
    def encrypted(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6edb5569d521a4d10aa01b8b4e0a61666063d50a62afd477cc3590f04bb514f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encrypted", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyEncryptionConfiguration]:
        return typing.cast(typing.Optional[DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyEncryptionConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyEncryptionConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10b0523b4aaa5c942e0bfeea35d31ba466c6bdbc49d8b5a8c0120f9fc34a85a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dlmLifecyclePolicy.DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3a0768b061831184dbf4e7af743f723d713f182c06c0cb35900bb2c514a1017f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2a07016e38bb228d68cce2c12d7908e730c3f86e5a163807b7579d17e1ea94a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9dbd2bc3502714f85051e9d31030aac132252d26319213eb3be950eaa509f433)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c0d8dd813f3f84d6c7adad65f0d8a77e505d039546bad728d6786a9f754353d7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c46a06c3b5953c0d55f4c1cc12b7e2ff3b77a1baf7712092adbc194d75bcb78e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopy]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopy]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09aa4927ba40e4312c44681cc85b233dc2afa0dcdfdadc1a53121da21d23d1a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dlmLifecyclePolicy.DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__82e113c02addcd7b996f119f672625328e260861b09359225176a4ca6ba66de8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putEncryptionConfiguration")
    def put_encryption_configuration(
        self,
        *,
        cmk_arn: typing.Optional[builtins.str] = None,
        encrypted: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param cmk_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#cmk_arn DlmLifecyclePolicy#cmk_arn}.
        :param encrypted: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#encrypted DlmLifecyclePolicy#encrypted}.
        '''
        value = DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyEncryptionConfiguration(
            cmk_arn=cmk_arn, encrypted=encrypted
        )

        return typing.cast(None, jsii.invoke(self, "putEncryptionConfiguration", [value]))

    @jsii.member(jsii_name="putRetainRule")
    def put_retain_rule(
        self,
        *,
        interval: jsii.Number,
        interval_unit: builtins.str,
    ) -> None:
        '''
        :param interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#interval DlmLifecyclePolicy#interval}.
        :param interval_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#interval_unit DlmLifecyclePolicy#interval_unit}.
        '''
        value = DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyRetainRule(
            interval=interval, interval_unit=interval_unit
        )

        return typing.cast(None, jsii.invoke(self, "putRetainRule", [value]))

    @jsii.member(jsii_name="resetRetainRule")
    def reset_retain_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetainRule", []))

    @builtins.property
    @jsii.member(jsii_name="encryptionConfiguration")
    def encryption_configuration(
        self,
    ) -> DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyEncryptionConfigurationOutputReference:
        return typing.cast(DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyEncryptionConfigurationOutputReference, jsii.get(self, "encryptionConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="retainRule")
    def retain_rule(
        self,
    ) -> "DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyRetainRuleOutputReference":
        return typing.cast("DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyRetainRuleOutputReference", jsii.get(self, "retainRule"))

    @builtins.property
    @jsii.member(jsii_name="encryptionConfigurationInput")
    def encryption_configuration_input(
        self,
    ) -> typing.Optional[DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyEncryptionConfiguration]:
        return typing.cast(typing.Optional[DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyEncryptionConfiguration], jsii.get(self, "encryptionConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="retainRuleInput")
    def retain_rule_input(
        self,
    ) -> typing.Optional["DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyRetainRule"]:
        return typing.cast(typing.Optional["DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyRetainRule"], jsii.get(self, "retainRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5bb74111817787f476eb5eb122314dcdb7984b341666be0124aad08f47f6cf5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopy, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopy, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopy, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c17ea11d40a614ba4ae86e567c818598783cd0080a1ca3658b842d0c56878eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dlmLifecyclePolicy.DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyRetainRule",
    jsii_struct_bases=[],
    name_mapping={"interval": "interval", "interval_unit": "intervalUnit"},
)
class DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyRetainRule:
    def __init__(self, *, interval: jsii.Number, interval_unit: builtins.str) -> None:
        '''
        :param interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#interval DlmLifecyclePolicy#interval}.
        :param interval_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#interval_unit DlmLifecyclePolicy#interval_unit}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ca73aed3f37c9ff9adb7cba95823fd6743b9761b5f67bb2ebe6f17df0aa09a3)
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
            check_type(argname="argument interval_unit", value=interval_unit, expected_type=type_hints["interval_unit"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "interval": interval,
            "interval_unit": interval_unit,
        }

    @builtins.property
    def interval(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#interval DlmLifecyclePolicy#interval}.'''
        result = self._values.get("interval")
        assert result is not None, "Required property 'interval' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def interval_unit(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#interval_unit DlmLifecyclePolicy#interval_unit}.'''
        result = self._values.get("interval_unit")
        assert result is not None, "Required property 'interval_unit' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyRetainRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyRetainRuleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dlmLifecyclePolicy.DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyRetainRuleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3beb176077353192de7e2ddf4f7ebcbb87eef127d98e5bcaaee72d77fa96e7ff)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="intervalInput")
    def interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "intervalInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalUnitInput")
    def interval_unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "intervalUnitInput"))

    @builtins.property
    @jsii.member(jsii_name="interval")
    def interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "interval"))

    @interval.setter
    def interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb3e1343c30c9a6becbfad542e9a996171e5b1a486e35325b14985142677d723)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interval", value)

    @builtins.property
    @jsii.member(jsii_name="intervalUnit")
    def interval_unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "intervalUnit"))

    @interval_unit.setter
    def interval_unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a18a96c3fdf4d34accf0eb35a8fcfdc03d608379cf7f6e642cdde96854c8bef9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intervalUnit", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyRetainRule]:
        return typing.cast(typing.Optional[DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyRetainRule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyRetainRule],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4aee30f57bb3c708bc75c10bc26eee43a54cbc6eae2366d7899719bd4974c2c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DlmLifecyclePolicyPolicyDetailsActionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dlmLifecyclePolicy.DlmLifecyclePolicyPolicyDetailsActionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f7ddf03af3c199345a8dd19e22356f8fe7b745f6d0a54742f848525c6adb2f1d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCrossRegionCopy")
    def put_cross_region_copy(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopy, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd1d889d2e1e3a03543ac07db12859e3f8c9a4808fb8922e53fdd991a038acf2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCrossRegionCopy", [value]))

    @builtins.property
    @jsii.member(jsii_name="crossRegionCopy")
    def cross_region_copy(
        self,
    ) -> DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyList:
        return typing.cast(DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyList, jsii.get(self, "crossRegionCopy"))

    @builtins.property
    @jsii.member(jsii_name="crossRegionCopyInput")
    def cross_region_copy_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopy]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopy]]], jsii.get(self, "crossRegionCopyInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__d2f3182495cda418106f459a0cfbd103998c55a49c993b7e69a3734094d405a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DlmLifecyclePolicyPolicyDetailsAction]:
        return typing.cast(typing.Optional[DlmLifecyclePolicyPolicyDetailsAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DlmLifecyclePolicyPolicyDetailsAction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bf944708a74ef440d310d463936d788135f0836b3599e8578bb03f5620bb38b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dlmLifecyclePolicy.DlmLifecyclePolicyPolicyDetailsEventSource",
    jsii_struct_bases=[],
    name_mapping={"parameters": "parameters", "type": "type"},
)
class DlmLifecyclePolicyPolicyDetailsEventSource:
    def __init__(
        self,
        *,
        parameters: typing.Union["DlmLifecyclePolicyPolicyDetailsEventSourceParameters", typing.Dict[builtins.str, typing.Any]],
        type: builtins.str,
    ) -> None:
        '''
        :param parameters: parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#parameters DlmLifecyclePolicy#parameters}
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#type DlmLifecyclePolicy#type}.
        '''
        if isinstance(parameters, dict):
            parameters = DlmLifecyclePolicyPolicyDetailsEventSourceParameters(**parameters)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a01d91b26c3c792b6daf082b9602bedcf2cf83f48b40175f0ba46efda32ed11)
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "parameters": parameters,
            "type": type,
        }

    @builtins.property
    def parameters(self) -> "DlmLifecyclePolicyPolicyDetailsEventSourceParameters":
        '''parameters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#parameters DlmLifecyclePolicy#parameters}
        '''
        result = self._values.get("parameters")
        assert result is not None, "Required property 'parameters' is missing"
        return typing.cast("DlmLifecyclePolicyPolicyDetailsEventSourceParameters", result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#type DlmLifecyclePolicy#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DlmLifecyclePolicyPolicyDetailsEventSource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DlmLifecyclePolicyPolicyDetailsEventSourceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dlmLifecyclePolicy.DlmLifecyclePolicyPolicyDetailsEventSourceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c6ec49fde22df52720a5c88a95c343d98b0c0761b2e2c4d49b0900de38e41698)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putParameters")
    def put_parameters(
        self,
        *,
        description_regex: builtins.str,
        event_type: builtins.str,
        snapshot_owner: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param description_regex: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#description_regex DlmLifecyclePolicy#description_regex}.
        :param event_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#event_type DlmLifecyclePolicy#event_type}.
        :param snapshot_owner: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#snapshot_owner DlmLifecyclePolicy#snapshot_owner}.
        '''
        value = DlmLifecyclePolicyPolicyDetailsEventSourceParameters(
            description_regex=description_regex,
            event_type=event_type,
            snapshot_owner=snapshot_owner,
        )

        return typing.cast(None, jsii.invoke(self, "putParameters", [value]))

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(
        self,
    ) -> "DlmLifecyclePolicyPolicyDetailsEventSourceParametersOutputReference":
        return typing.cast("DlmLifecyclePolicyPolicyDetailsEventSourceParametersOutputReference", jsii.get(self, "parameters"))

    @builtins.property
    @jsii.member(jsii_name="parametersInput")
    def parameters_input(
        self,
    ) -> typing.Optional["DlmLifecyclePolicyPolicyDetailsEventSourceParameters"]:
        return typing.cast(typing.Optional["DlmLifecyclePolicyPolicyDetailsEventSourceParameters"], jsii.get(self, "parametersInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__e6e7cf49cd0429e1cb456932cc74656a302de893575040c836aea2fe1e986959)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DlmLifecyclePolicyPolicyDetailsEventSource]:
        return typing.cast(typing.Optional[DlmLifecyclePolicyPolicyDetailsEventSource], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DlmLifecyclePolicyPolicyDetailsEventSource],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5eb47f66c90cb849118dbaaad42c16b00f2e4190ce5608f5debbbdfe85160aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dlmLifecyclePolicy.DlmLifecyclePolicyPolicyDetailsEventSourceParameters",
    jsii_struct_bases=[],
    name_mapping={
        "description_regex": "descriptionRegex",
        "event_type": "eventType",
        "snapshot_owner": "snapshotOwner",
    },
)
class DlmLifecyclePolicyPolicyDetailsEventSourceParameters:
    def __init__(
        self,
        *,
        description_regex: builtins.str,
        event_type: builtins.str,
        snapshot_owner: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param description_regex: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#description_regex DlmLifecyclePolicy#description_regex}.
        :param event_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#event_type DlmLifecyclePolicy#event_type}.
        :param snapshot_owner: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#snapshot_owner DlmLifecyclePolicy#snapshot_owner}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55420e53e96bdbba6410a9d5b208b03f4a9b66cc7c2a50fed08d9f8afedfa1ad)
            check_type(argname="argument description_regex", value=description_regex, expected_type=type_hints["description_regex"])
            check_type(argname="argument event_type", value=event_type, expected_type=type_hints["event_type"])
            check_type(argname="argument snapshot_owner", value=snapshot_owner, expected_type=type_hints["snapshot_owner"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description_regex": description_regex,
            "event_type": event_type,
            "snapshot_owner": snapshot_owner,
        }

    @builtins.property
    def description_regex(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#description_regex DlmLifecyclePolicy#description_regex}.'''
        result = self._values.get("description_regex")
        assert result is not None, "Required property 'description_regex' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def event_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#event_type DlmLifecyclePolicy#event_type}.'''
        result = self._values.get("event_type")
        assert result is not None, "Required property 'event_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def snapshot_owner(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#snapshot_owner DlmLifecyclePolicy#snapshot_owner}.'''
        result = self._values.get("snapshot_owner")
        assert result is not None, "Required property 'snapshot_owner' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DlmLifecyclePolicyPolicyDetailsEventSourceParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DlmLifecyclePolicyPolicyDetailsEventSourceParametersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dlmLifecyclePolicy.DlmLifecyclePolicyPolicyDetailsEventSourceParametersOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2ea41bff7dceb806970197613213526b6ab5b597b83068d9aa0a192475a63c21)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="descriptionRegexInput")
    def description_regex_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionRegexInput"))

    @builtins.property
    @jsii.member(jsii_name="eventTypeInput")
    def event_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="snapshotOwnerInput")
    def snapshot_owner_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "snapshotOwnerInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionRegex")
    def description_regex(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "descriptionRegex"))

    @description_regex.setter
    def description_regex(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff3546c335bf4baa0fecd464062204a476c877637440cc241940ae15015ef33b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "descriptionRegex", value)

    @builtins.property
    @jsii.member(jsii_name="eventType")
    def event_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventType"))

    @event_type.setter
    def event_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5ce0f574e63239414d12c99de9a382b7bbcb025acd2c8e58535f4a97b9dcb7e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventType", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotOwner")
    def snapshot_owner(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "snapshotOwner"))

    @snapshot_owner.setter
    def snapshot_owner(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4907134970060bfde2bdcb572d6e43c03c17b38c36a103b568e41c8776dca32f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotOwner", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DlmLifecyclePolicyPolicyDetailsEventSourceParameters]:
        return typing.cast(typing.Optional[DlmLifecyclePolicyPolicyDetailsEventSourceParameters], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DlmLifecyclePolicyPolicyDetailsEventSourceParameters],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17a482ca0e9ec7091d327b692c12261b084c7bb001f57d82343415eee4f25928)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DlmLifecyclePolicyPolicyDetailsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dlmLifecyclePolicy.DlmLifecyclePolicyPolicyDetailsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ac5b0c171b6730345a24321844f45ec026d24e8f550b686de16d0b41fd7a184b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAction")
    def put_action(
        self,
        *,
        cross_region_copy: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopy, typing.Dict[builtins.str, typing.Any]]]],
        name: builtins.str,
    ) -> None:
        '''
        :param cross_region_copy: cross_region_copy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#cross_region_copy DlmLifecyclePolicy#cross_region_copy}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#name DlmLifecyclePolicy#name}.
        '''
        value = DlmLifecyclePolicyPolicyDetailsAction(
            cross_region_copy=cross_region_copy, name=name
        )

        return typing.cast(None, jsii.invoke(self, "putAction", [value]))

    @jsii.member(jsii_name="putEventSource")
    def put_event_source(
        self,
        *,
        parameters: typing.Union[DlmLifecyclePolicyPolicyDetailsEventSourceParameters, typing.Dict[builtins.str, typing.Any]],
        type: builtins.str,
    ) -> None:
        '''
        :param parameters: parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#parameters DlmLifecyclePolicy#parameters}
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#type DlmLifecyclePolicy#type}.
        '''
        value = DlmLifecyclePolicyPolicyDetailsEventSource(
            parameters=parameters, type=type
        )

        return typing.cast(None, jsii.invoke(self, "putEventSource", [value]))

    @jsii.member(jsii_name="putParameters")
    def put_parameters(
        self,
        *,
        exclude_boot_volume: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        no_reboot: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param exclude_boot_volume: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#exclude_boot_volume DlmLifecyclePolicy#exclude_boot_volume}.
        :param no_reboot: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#no_reboot DlmLifecyclePolicy#no_reboot}.
        '''
        value = DlmLifecyclePolicyPolicyDetailsParameters(
            exclude_boot_volume=exclude_boot_volume, no_reboot=no_reboot
        )

        return typing.cast(None, jsii.invoke(self, "putParameters", [value]))

    @jsii.member(jsii_name="putSchedule")
    def put_schedule(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DlmLifecyclePolicyPolicyDetailsSchedule", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e404fe6d137bd13801a94275bd290fe2a6e9690dc7b650fbc04bf74978096b21)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSchedule", [value]))

    @jsii.member(jsii_name="resetAction")
    def reset_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAction", []))

    @jsii.member(jsii_name="resetEventSource")
    def reset_event_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventSource", []))

    @jsii.member(jsii_name="resetParameters")
    def reset_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameters", []))

    @jsii.member(jsii_name="resetPolicyType")
    def reset_policy_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolicyType", []))

    @jsii.member(jsii_name="resetResourceLocations")
    def reset_resource_locations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceLocations", []))

    @jsii.member(jsii_name="resetResourceTypes")
    def reset_resource_types(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceTypes", []))

    @jsii.member(jsii_name="resetSchedule")
    def reset_schedule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchedule", []))

    @jsii.member(jsii_name="resetTargetTags")
    def reset_target_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetTags", []))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> DlmLifecyclePolicyPolicyDetailsActionOutputReference:
        return typing.cast(DlmLifecyclePolicyPolicyDetailsActionOutputReference, jsii.get(self, "action"))

    @builtins.property
    @jsii.member(jsii_name="eventSource")
    def event_source(self) -> DlmLifecyclePolicyPolicyDetailsEventSourceOutputReference:
        return typing.cast(DlmLifecyclePolicyPolicyDetailsEventSourceOutputReference, jsii.get(self, "eventSource"))

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> "DlmLifecyclePolicyPolicyDetailsParametersOutputReference":
        return typing.cast("DlmLifecyclePolicyPolicyDetailsParametersOutputReference", jsii.get(self, "parameters"))

    @builtins.property
    @jsii.member(jsii_name="schedule")
    def schedule(self) -> "DlmLifecyclePolicyPolicyDetailsScheduleList":
        return typing.cast("DlmLifecyclePolicyPolicyDetailsScheduleList", jsii.get(self, "schedule"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[DlmLifecyclePolicyPolicyDetailsAction]:
        return typing.cast(typing.Optional[DlmLifecyclePolicyPolicyDetailsAction], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="eventSourceInput")
    def event_source_input(
        self,
    ) -> typing.Optional[DlmLifecyclePolicyPolicyDetailsEventSource]:
        return typing.cast(typing.Optional[DlmLifecyclePolicyPolicyDetailsEventSource], jsii.get(self, "eventSourceInput"))

    @builtins.property
    @jsii.member(jsii_name="parametersInput")
    def parameters_input(
        self,
    ) -> typing.Optional["DlmLifecyclePolicyPolicyDetailsParameters"]:
        return typing.cast(typing.Optional["DlmLifecyclePolicyPolicyDetailsParameters"], jsii.get(self, "parametersInput"))

    @builtins.property
    @jsii.member(jsii_name="policyTypeInput")
    def policy_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policyTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceLocationsInput")
    def resource_locations_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourceLocationsInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceTypesInput")
    def resource_types_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourceTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduleInput")
    def schedule_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DlmLifecyclePolicyPolicyDetailsSchedule"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DlmLifecyclePolicyPolicyDetailsSchedule"]]], jsii.get(self, "scheduleInput"))

    @builtins.property
    @jsii.member(jsii_name="targetTagsInput")
    def target_tags_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "targetTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="policyType")
    def policy_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "policyType"))

    @policy_type.setter
    def policy_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36a847b455815f3717a59b606df405e92fd023b5a8ffbb5475bdd89a1b735792)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyType", value)

    @builtins.property
    @jsii.member(jsii_name="resourceLocations")
    def resource_locations(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "resourceLocations"))

    @resource_locations.setter
    def resource_locations(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df28a3700513e47607b48e8c725eb6eef6e62b4e51fba05712b35a496ffc5c02)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceLocations", value)

    @builtins.property
    @jsii.member(jsii_name="resourceTypes")
    def resource_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "resourceTypes"))

    @resource_types.setter
    def resource_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38d127fb71ee5d96b2ab4f26a1b1aefd9856dd5cd3b6c27ff702d29fd4690900)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceTypes", value)

    @builtins.property
    @jsii.member(jsii_name="targetTags")
    def target_tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "targetTags"))

    @target_tags.setter
    def target_tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd538b9cf214ae8b32c1d75d1b373ad1a18a71195cb126d8e8f3edbae1276105)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetTags", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DlmLifecyclePolicyPolicyDetails]:
        return typing.cast(typing.Optional[DlmLifecyclePolicyPolicyDetails], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DlmLifecyclePolicyPolicyDetails],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed4ed98106b6723b684b8bd4e94bf04cc4a506f5566254c77f566ec4fa4f7493)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dlmLifecyclePolicy.DlmLifecyclePolicyPolicyDetailsParameters",
    jsii_struct_bases=[],
    name_mapping={"exclude_boot_volume": "excludeBootVolume", "no_reboot": "noReboot"},
)
class DlmLifecyclePolicyPolicyDetailsParameters:
    def __init__(
        self,
        *,
        exclude_boot_volume: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        no_reboot: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param exclude_boot_volume: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#exclude_boot_volume DlmLifecyclePolicy#exclude_boot_volume}.
        :param no_reboot: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#no_reboot DlmLifecyclePolicy#no_reboot}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed76e802f67ec88739ebacbd4c8ed87c227bbd28f61e6b94a640f4e5a8fca9e3)
            check_type(argname="argument exclude_boot_volume", value=exclude_boot_volume, expected_type=type_hints["exclude_boot_volume"])
            check_type(argname="argument no_reboot", value=no_reboot, expected_type=type_hints["no_reboot"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if exclude_boot_volume is not None:
            self._values["exclude_boot_volume"] = exclude_boot_volume
        if no_reboot is not None:
            self._values["no_reboot"] = no_reboot

    @builtins.property
    def exclude_boot_volume(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#exclude_boot_volume DlmLifecyclePolicy#exclude_boot_volume}.'''
        result = self._values.get("exclude_boot_volume")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def no_reboot(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#no_reboot DlmLifecyclePolicy#no_reboot}.'''
        result = self._values.get("no_reboot")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DlmLifecyclePolicyPolicyDetailsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DlmLifecyclePolicyPolicyDetailsParametersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dlmLifecyclePolicy.DlmLifecyclePolicyPolicyDetailsParametersOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__40ebdcc912be19064eacc4f6e0d37382b3aaa58eb044ca27bae1682c656b4fab)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetExcludeBootVolume")
    def reset_exclude_boot_volume(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcludeBootVolume", []))

    @jsii.member(jsii_name="resetNoReboot")
    def reset_no_reboot(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNoReboot", []))

    @builtins.property
    @jsii.member(jsii_name="excludeBootVolumeInput")
    def exclude_boot_volume_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "excludeBootVolumeInput"))

    @builtins.property
    @jsii.member(jsii_name="noRebootInput")
    def no_reboot_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "noRebootInput"))

    @builtins.property
    @jsii.member(jsii_name="excludeBootVolume")
    def exclude_boot_volume(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "excludeBootVolume"))

    @exclude_boot_volume.setter
    def exclude_boot_volume(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a8d3b769c5a6feeffba32dbab7e1b222e9e7492a7b9ef5366827ee3d86e1390)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "excludeBootVolume", value)

    @builtins.property
    @jsii.member(jsii_name="noReboot")
    def no_reboot(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "noReboot"))

    @no_reboot.setter
    def no_reboot(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc7f45d5104604e2f4ed525e0c2208712a9b8636b18d385cf8bd555f02e504e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "noReboot", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DlmLifecyclePolicyPolicyDetailsParameters]:
        return typing.cast(typing.Optional[DlmLifecyclePolicyPolicyDetailsParameters], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DlmLifecyclePolicyPolicyDetailsParameters],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3df0052ef316123756cff06b9f954808eaa2666e1c78a406faa10359a0dd71a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dlmLifecyclePolicy.DlmLifecyclePolicyPolicyDetailsSchedule",
    jsii_struct_bases=[],
    name_mapping={
        "create_rule": "createRule",
        "name": "name",
        "retain_rule": "retainRule",
        "copy_tags": "copyTags",
        "cross_region_copy_rule": "crossRegionCopyRule",
        "deprecate_rule": "deprecateRule",
        "fast_restore_rule": "fastRestoreRule",
        "share_rule": "shareRule",
        "tags_to_add": "tagsToAdd",
        "variable_tags": "variableTags",
    },
)
class DlmLifecyclePolicyPolicyDetailsSchedule:
    def __init__(
        self,
        *,
        create_rule: typing.Union["DlmLifecyclePolicyPolicyDetailsScheduleCreateRule", typing.Dict[builtins.str, typing.Any]],
        name: builtins.str,
        retain_rule: typing.Union["DlmLifecyclePolicyPolicyDetailsScheduleRetainRule", typing.Dict[builtins.str, typing.Any]],
        copy_tags: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        cross_region_copy_rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRule", typing.Dict[builtins.str, typing.Any]]]]] = None,
        deprecate_rule: typing.Optional[typing.Union["DlmLifecyclePolicyPolicyDetailsScheduleDeprecateRule", typing.Dict[builtins.str, typing.Any]]] = None,
        fast_restore_rule: typing.Optional[typing.Union["DlmLifecyclePolicyPolicyDetailsScheduleFastRestoreRule", typing.Dict[builtins.str, typing.Any]]] = None,
        share_rule: typing.Optional[typing.Union["DlmLifecyclePolicyPolicyDetailsScheduleShareRule", typing.Dict[builtins.str, typing.Any]]] = None,
        tags_to_add: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        variable_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param create_rule: create_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#create_rule DlmLifecyclePolicy#create_rule}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#name DlmLifecyclePolicy#name}.
        :param retain_rule: retain_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#retain_rule DlmLifecyclePolicy#retain_rule}
        :param copy_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#copy_tags DlmLifecyclePolicy#copy_tags}.
        :param cross_region_copy_rule: cross_region_copy_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#cross_region_copy_rule DlmLifecyclePolicy#cross_region_copy_rule}
        :param deprecate_rule: deprecate_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#deprecate_rule DlmLifecyclePolicy#deprecate_rule}
        :param fast_restore_rule: fast_restore_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#fast_restore_rule DlmLifecyclePolicy#fast_restore_rule}
        :param share_rule: share_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#share_rule DlmLifecyclePolicy#share_rule}
        :param tags_to_add: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#tags_to_add DlmLifecyclePolicy#tags_to_add}.
        :param variable_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#variable_tags DlmLifecyclePolicy#variable_tags}.
        '''
        if isinstance(create_rule, dict):
            create_rule = DlmLifecyclePolicyPolicyDetailsScheduleCreateRule(**create_rule)
        if isinstance(retain_rule, dict):
            retain_rule = DlmLifecyclePolicyPolicyDetailsScheduleRetainRule(**retain_rule)
        if isinstance(deprecate_rule, dict):
            deprecate_rule = DlmLifecyclePolicyPolicyDetailsScheduleDeprecateRule(**deprecate_rule)
        if isinstance(fast_restore_rule, dict):
            fast_restore_rule = DlmLifecyclePolicyPolicyDetailsScheduleFastRestoreRule(**fast_restore_rule)
        if isinstance(share_rule, dict):
            share_rule = DlmLifecyclePolicyPolicyDetailsScheduleShareRule(**share_rule)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbd4f3ec6e6572a052d780f0e27c84842548eba3c08674e267ff5554227da734)
            check_type(argname="argument create_rule", value=create_rule, expected_type=type_hints["create_rule"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument retain_rule", value=retain_rule, expected_type=type_hints["retain_rule"])
            check_type(argname="argument copy_tags", value=copy_tags, expected_type=type_hints["copy_tags"])
            check_type(argname="argument cross_region_copy_rule", value=cross_region_copy_rule, expected_type=type_hints["cross_region_copy_rule"])
            check_type(argname="argument deprecate_rule", value=deprecate_rule, expected_type=type_hints["deprecate_rule"])
            check_type(argname="argument fast_restore_rule", value=fast_restore_rule, expected_type=type_hints["fast_restore_rule"])
            check_type(argname="argument share_rule", value=share_rule, expected_type=type_hints["share_rule"])
            check_type(argname="argument tags_to_add", value=tags_to_add, expected_type=type_hints["tags_to_add"])
            check_type(argname="argument variable_tags", value=variable_tags, expected_type=type_hints["variable_tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "create_rule": create_rule,
            "name": name,
            "retain_rule": retain_rule,
        }
        if copy_tags is not None:
            self._values["copy_tags"] = copy_tags
        if cross_region_copy_rule is not None:
            self._values["cross_region_copy_rule"] = cross_region_copy_rule
        if deprecate_rule is not None:
            self._values["deprecate_rule"] = deprecate_rule
        if fast_restore_rule is not None:
            self._values["fast_restore_rule"] = fast_restore_rule
        if share_rule is not None:
            self._values["share_rule"] = share_rule
        if tags_to_add is not None:
            self._values["tags_to_add"] = tags_to_add
        if variable_tags is not None:
            self._values["variable_tags"] = variable_tags

    @builtins.property
    def create_rule(self) -> "DlmLifecyclePolicyPolicyDetailsScheduleCreateRule":
        '''create_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#create_rule DlmLifecyclePolicy#create_rule}
        '''
        result = self._values.get("create_rule")
        assert result is not None, "Required property 'create_rule' is missing"
        return typing.cast("DlmLifecyclePolicyPolicyDetailsScheduleCreateRule", result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#name DlmLifecyclePolicy#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def retain_rule(self) -> "DlmLifecyclePolicyPolicyDetailsScheduleRetainRule":
        '''retain_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#retain_rule DlmLifecyclePolicy#retain_rule}
        '''
        result = self._values.get("retain_rule")
        assert result is not None, "Required property 'retain_rule' is missing"
        return typing.cast("DlmLifecyclePolicyPolicyDetailsScheduleRetainRule", result)

    @builtins.property
    def copy_tags(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#copy_tags DlmLifecyclePolicy#copy_tags}.'''
        result = self._values.get("copy_tags")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def cross_region_copy_rule(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRule"]]]:
        '''cross_region_copy_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#cross_region_copy_rule DlmLifecyclePolicy#cross_region_copy_rule}
        '''
        result = self._values.get("cross_region_copy_rule")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRule"]]], result)

    @builtins.property
    def deprecate_rule(
        self,
    ) -> typing.Optional["DlmLifecyclePolicyPolicyDetailsScheduleDeprecateRule"]:
        '''deprecate_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#deprecate_rule DlmLifecyclePolicy#deprecate_rule}
        '''
        result = self._values.get("deprecate_rule")
        return typing.cast(typing.Optional["DlmLifecyclePolicyPolicyDetailsScheduleDeprecateRule"], result)

    @builtins.property
    def fast_restore_rule(
        self,
    ) -> typing.Optional["DlmLifecyclePolicyPolicyDetailsScheduleFastRestoreRule"]:
        '''fast_restore_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#fast_restore_rule DlmLifecyclePolicy#fast_restore_rule}
        '''
        result = self._values.get("fast_restore_rule")
        return typing.cast(typing.Optional["DlmLifecyclePolicyPolicyDetailsScheduleFastRestoreRule"], result)

    @builtins.property
    def share_rule(
        self,
    ) -> typing.Optional["DlmLifecyclePolicyPolicyDetailsScheduleShareRule"]:
        '''share_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#share_rule DlmLifecyclePolicy#share_rule}
        '''
        result = self._values.get("share_rule")
        return typing.cast(typing.Optional["DlmLifecyclePolicyPolicyDetailsScheduleShareRule"], result)

    @builtins.property
    def tags_to_add(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#tags_to_add DlmLifecyclePolicy#tags_to_add}.'''
        result = self._values.get("tags_to_add")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def variable_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#variable_tags DlmLifecyclePolicy#variable_tags}.'''
        result = self._values.get("variable_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DlmLifecyclePolicyPolicyDetailsSchedule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.dlmLifecyclePolicy.DlmLifecyclePolicyPolicyDetailsScheduleCreateRule",
    jsii_struct_bases=[],
    name_mapping={
        "cron_expression": "cronExpression",
        "interval": "interval",
        "interval_unit": "intervalUnit",
        "location": "location",
        "times": "times",
    },
)
class DlmLifecyclePolicyPolicyDetailsScheduleCreateRule:
    def __init__(
        self,
        *,
        cron_expression: typing.Optional[builtins.str] = None,
        interval: typing.Optional[jsii.Number] = None,
        interval_unit: typing.Optional[builtins.str] = None,
        location: typing.Optional[builtins.str] = None,
        times: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param cron_expression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#cron_expression DlmLifecyclePolicy#cron_expression}.
        :param interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#interval DlmLifecyclePolicy#interval}.
        :param interval_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#interval_unit DlmLifecyclePolicy#interval_unit}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#location DlmLifecyclePolicy#location}.
        :param times: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#times DlmLifecyclePolicy#times}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e85bc714270af8309dba0098ff6117761ed203f05d649a90fa9ade08f660ff83)
            check_type(argname="argument cron_expression", value=cron_expression, expected_type=type_hints["cron_expression"])
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
            check_type(argname="argument interval_unit", value=interval_unit, expected_type=type_hints["interval_unit"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument times", value=times, expected_type=type_hints["times"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cron_expression is not None:
            self._values["cron_expression"] = cron_expression
        if interval is not None:
            self._values["interval"] = interval
        if interval_unit is not None:
            self._values["interval_unit"] = interval_unit
        if location is not None:
            self._values["location"] = location
        if times is not None:
            self._values["times"] = times

    @builtins.property
    def cron_expression(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#cron_expression DlmLifecyclePolicy#cron_expression}.'''
        result = self._values.get("cron_expression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def interval(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#interval DlmLifecyclePolicy#interval}.'''
        result = self._values.get("interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def interval_unit(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#interval_unit DlmLifecyclePolicy#interval_unit}.'''
        result = self._values.get("interval_unit")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def location(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#location DlmLifecyclePolicy#location}.'''
        result = self._values.get("location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def times(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#times DlmLifecyclePolicy#times}.'''
        result = self._values.get("times")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DlmLifecyclePolicyPolicyDetailsScheduleCreateRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DlmLifecyclePolicyPolicyDetailsScheduleCreateRuleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dlmLifecyclePolicy.DlmLifecyclePolicyPolicyDetailsScheduleCreateRuleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a9653b5823f3b20d8d8644a515bce1e9fe598d90055faa133e7bc1bf2e9cc7c4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCronExpression")
    def reset_cron_expression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCronExpression", []))

    @jsii.member(jsii_name="resetInterval")
    def reset_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInterval", []))

    @jsii.member(jsii_name="resetIntervalUnit")
    def reset_interval_unit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIntervalUnit", []))

    @jsii.member(jsii_name="resetLocation")
    def reset_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocation", []))

    @jsii.member(jsii_name="resetTimes")
    def reset_times(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimes", []))

    @builtins.property
    @jsii.member(jsii_name="cronExpressionInput")
    def cron_expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cronExpressionInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalInput")
    def interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "intervalInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalUnitInput")
    def interval_unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "intervalUnitInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="timesInput")
    def times_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "timesInput"))

    @builtins.property
    @jsii.member(jsii_name="cronExpression")
    def cron_expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cronExpression"))

    @cron_expression.setter
    def cron_expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b08ce8a22bc6117d172cd029f4ce92de07d467df878624213ee8b098eaf6633)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cronExpression", value)

    @builtins.property
    @jsii.member(jsii_name="interval")
    def interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "interval"))

    @interval.setter
    def interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5febae01135fe00c45be5b2e8360ae6068d1c321ca4be719d625856a0a7f3f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interval", value)

    @builtins.property
    @jsii.member(jsii_name="intervalUnit")
    def interval_unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "intervalUnit"))

    @interval_unit.setter
    def interval_unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d218638ad1919ebf5888934bc4114402cbdc9605887fe7026e151445e263ee07)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intervalUnit", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb996ef72baaea4a2cd151b11d89f316e492ce73ee87e54a407841bab553e6b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="times")
    def times(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "times"))

    @times.setter
    def times(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d322d8045cfbcca26c5d37d98800cc3396bf6bcc94f70a532f9690a0226d8b3c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "times", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DlmLifecyclePolicyPolicyDetailsScheduleCreateRule]:
        return typing.cast(typing.Optional[DlmLifecyclePolicyPolicyDetailsScheduleCreateRule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DlmLifecyclePolicyPolicyDetailsScheduleCreateRule],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e84753be706bc8ecdd2279f0210e8bcd5bdce3001e2ff7bb583f3d288ea92e5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dlmLifecyclePolicy.DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRule",
    jsii_struct_bases=[],
    name_mapping={
        "encrypted": "encrypted",
        "target": "target",
        "cmk_arn": "cmkArn",
        "copy_tags": "copyTags",
        "deprecate_rule": "deprecateRule",
        "retain_rule": "retainRule",
    },
)
class DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRule:
    def __init__(
        self,
        *,
        encrypted: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        target: builtins.str,
        cmk_arn: typing.Optional[builtins.str] = None,
        copy_tags: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        deprecate_rule: typing.Optional[typing.Union["DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleDeprecateRule", typing.Dict[builtins.str, typing.Any]]] = None,
        retain_rule: typing.Optional[typing.Union["DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleRetainRule", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param encrypted: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#encrypted DlmLifecyclePolicy#encrypted}.
        :param target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#target DlmLifecyclePolicy#target}.
        :param cmk_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#cmk_arn DlmLifecyclePolicy#cmk_arn}.
        :param copy_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#copy_tags DlmLifecyclePolicy#copy_tags}.
        :param deprecate_rule: deprecate_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#deprecate_rule DlmLifecyclePolicy#deprecate_rule}
        :param retain_rule: retain_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#retain_rule DlmLifecyclePolicy#retain_rule}
        '''
        if isinstance(deprecate_rule, dict):
            deprecate_rule = DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleDeprecateRule(**deprecate_rule)
        if isinstance(retain_rule, dict):
            retain_rule = DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleRetainRule(**retain_rule)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f8ad6449b2cf946c24973deefae1273f83f6d310326d8f601e44432d822ac19)
            check_type(argname="argument encrypted", value=encrypted, expected_type=type_hints["encrypted"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument cmk_arn", value=cmk_arn, expected_type=type_hints["cmk_arn"])
            check_type(argname="argument copy_tags", value=copy_tags, expected_type=type_hints["copy_tags"])
            check_type(argname="argument deprecate_rule", value=deprecate_rule, expected_type=type_hints["deprecate_rule"])
            check_type(argname="argument retain_rule", value=retain_rule, expected_type=type_hints["retain_rule"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "encrypted": encrypted,
            "target": target,
        }
        if cmk_arn is not None:
            self._values["cmk_arn"] = cmk_arn
        if copy_tags is not None:
            self._values["copy_tags"] = copy_tags
        if deprecate_rule is not None:
            self._values["deprecate_rule"] = deprecate_rule
        if retain_rule is not None:
            self._values["retain_rule"] = retain_rule

    @builtins.property
    def encrypted(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#encrypted DlmLifecyclePolicy#encrypted}.'''
        result = self._values.get("encrypted")
        assert result is not None, "Required property 'encrypted' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def target(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#target DlmLifecyclePolicy#target}.'''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cmk_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#cmk_arn DlmLifecyclePolicy#cmk_arn}.'''
        result = self._values.get("cmk_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def copy_tags(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#copy_tags DlmLifecyclePolicy#copy_tags}.'''
        result = self._values.get("copy_tags")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def deprecate_rule(
        self,
    ) -> typing.Optional["DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleDeprecateRule"]:
        '''deprecate_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#deprecate_rule DlmLifecyclePolicy#deprecate_rule}
        '''
        result = self._values.get("deprecate_rule")
        return typing.cast(typing.Optional["DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleDeprecateRule"], result)

    @builtins.property
    def retain_rule(
        self,
    ) -> typing.Optional["DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleRetainRule"]:
        '''retain_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#retain_rule DlmLifecyclePolicy#retain_rule}
        '''
        result = self._values.get("retain_rule")
        return typing.cast(typing.Optional["DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleRetainRule"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.dlmLifecyclePolicy.DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleDeprecateRule",
    jsii_struct_bases=[],
    name_mapping={"interval": "interval", "interval_unit": "intervalUnit"},
)
class DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleDeprecateRule:
    def __init__(self, *, interval: jsii.Number, interval_unit: builtins.str) -> None:
        '''
        :param interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#interval DlmLifecyclePolicy#interval}.
        :param interval_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#interval_unit DlmLifecyclePolicy#interval_unit}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c12a2f4f2da0c69acba25557587584fb58d74ca6b47a1782360d4612163745fe)
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
            check_type(argname="argument interval_unit", value=interval_unit, expected_type=type_hints["interval_unit"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "interval": interval,
            "interval_unit": interval_unit,
        }

    @builtins.property
    def interval(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#interval DlmLifecyclePolicy#interval}.'''
        result = self._values.get("interval")
        assert result is not None, "Required property 'interval' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def interval_unit(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#interval_unit DlmLifecyclePolicy#interval_unit}.'''
        result = self._values.get("interval_unit")
        assert result is not None, "Required property 'interval_unit' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleDeprecateRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleDeprecateRuleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dlmLifecyclePolicy.DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleDeprecateRuleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__26b057667ab085173a668e7b8f19133deaa71073d8262a5638ad192fe9bf3dd0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="intervalInput")
    def interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "intervalInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalUnitInput")
    def interval_unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "intervalUnitInput"))

    @builtins.property
    @jsii.member(jsii_name="interval")
    def interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "interval"))

    @interval.setter
    def interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08eb49d89c4756f31b691fb01695ff335c685b23eb5d8d3719bb328d0262bcc5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interval", value)

    @builtins.property
    @jsii.member(jsii_name="intervalUnit")
    def interval_unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "intervalUnit"))

    @interval_unit.setter
    def interval_unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae3851a9aa0d40d1757285f7a13c41ef74c9b6e75e11f06e5ae97bd3f2081237)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intervalUnit", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleDeprecateRule]:
        return typing.cast(typing.Optional[DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleDeprecateRule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleDeprecateRule],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7decadd0e8ce3a0df5b4259b3482ef3632627c1b13f40116a08d43c952dc11d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dlmLifecyclePolicy.DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__06e48b17ec8d3ce811010997f3d43f639dbad0ec397b47b4010029ccd3336c31)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db3a22eb4be79a05414bd8f590861fc14e327efabc021c01fecd18a88a574ebd)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1da5d71245392f45d3a690b67688ddc9106fe36e4884fafb2762032cf6b1ed2b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7ecda70d4fc9dd89ff3070e56895c804562a76d5014518c13490cd0fadc8f2f4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__eb049cadd1f8fdc9485671268a1ee6f3d810f0d0091fb48f4eb6f30a8d34c873)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRule]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b68c469022c1814d9acee2a6f674b2d4d3714433e74a6b55f706ec7ef3064eed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dlmLifecyclePolicy.DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e8288f2aa30d2f6e3ad0524397ed74185c667edf9384764b2e86e72934bcd233)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putDeprecateRule")
    def put_deprecate_rule(
        self,
        *,
        interval: jsii.Number,
        interval_unit: builtins.str,
    ) -> None:
        '''
        :param interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#interval DlmLifecyclePolicy#interval}.
        :param interval_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#interval_unit DlmLifecyclePolicy#interval_unit}.
        '''
        value = DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleDeprecateRule(
            interval=interval, interval_unit=interval_unit
        )

        return typing.cast(None, jsii.invoke(self, "putDeprecateRule", [value]))

    @jsii.member(jsii_name="putRetainRule")
    def put_retain_rule(
        self,
        *,
        interval: jsii.Number,
        interval_unit: builtins.str,
    ) -> None:
        '''
        :param interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#interval DlmLifecyclePolicy#interval}.
        :param interval_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#interval_unit DlmLifecyclePolicy#interval_unit}.
        '''
        value = DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleRetainRule(
            interval=interval, interval_unit=interval_unit
        )

        return typing.cast(None, jsii.invoke(self, "putRetainRule", [value]))

    @jsii.member(jsii_name="resetCmkArn")
    def reset_cmk_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCmkArn", []))

    @jsii.member(jsii_name="resetCopyTags")
    def reset_copy_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCopyTags", []))

    @jsii.member(jsii_name="resetDeprecateRule")
    def reset_deprecate_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeprecateRule", []))

    @jsii.member(jsii_name="resetRetainRule")
    def reset_retain_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetainRule", []))

    @builtins.property
    @jsii.member(jsii_name="deprecateRule")
    def deprecate_rule(
        self,
    ) -> DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleDeprecateRuleOutputReference:
        return typing.cast(DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleDeprecateRuleOutputReference, jsii.get(self, "deprecateRule"))

    @builtins.property
    @jsii.member(jsii_name="retainRule")
    def retain_rule(
        self,
    ) -> "DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleRetainRuleOutputReference":
        return typing.cast("DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleRetainRuleOutputReference", jsii.get(self, "retainRule"))

    @builtins.property
    @jsii.member(jsii_name="cmkArnInput")
    def cmk_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cmkArnInput"))

    @builtins.property
    @jsii.member(jsii_name="copyTagsInput")
    def copy_tags_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "copyTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="deprecateRuleInput")
    def deprecate_rule_input(
        self,
    ) -> typing.Optional[DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleDeprecateRule]:
        return typing.cast(typing.Optional[DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleDeprecateRule], jsii.get(self, "deprecateRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptedInput")
    def encrypted_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "encryptedInput"))

    @builtins.property
    @jsii.member(jsii_name="retainRuleInput")
    def retain_rule_input(
        self,
    ) -> typing.Optional["DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleRetainRule"]:
        return typing.cast(typing.Optional["DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleRetainRule"], jsii.get(self, "retainRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="cmkArn")
    def cmk_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cmkArn"))

    @cmk_arn.setter
    def cmk_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb84d1f3d7a8cc137f82453c34b355b41172d3b11c22a91ba80525a28d247cbb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cmkArn", value)

    @builtins.property
    @jsii.member(jsii_name="copyTags")
    def copy_tags(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "copyTags"))

    @copy_tags.setter
    def copy_tags(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7835335961db94763f8e768955fc2e170002cb1d6e6826f0846444173131c1e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "copyTags", value)

    @builtins.property
    @jsii.member(jsii_name="encrypted")
    def encrypted(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "encrypted"))

    @encrypted.setter
    def encrypted(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c8a63bfc37d38f0cd3f313c8b2aea3bfa363b6edd759f5ff14722e2ff49f8a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encrypted", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70a50bdebc50928377498c2a761db56e6a7ad16882e38cd9babd6892d2777ed9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRule, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRule, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRule, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d52da3fa37fed809e4dcd6154b14ce4ec7cbc0efe3e7de54c214fb3dd2a8f66)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dlmLifecyclePolicy.DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleRetainRule",
    jsii_struct_bases=[],
    name_mapping={"interval": "interval", "interval_unit": "intervalUnit"},
)
class DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleRetainRule:
    def __init__(self, *, interval: jsii.Number, interval_unit: builtins.str) -> None:
        '''
        :param interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#interval DlmLifecyclePolicy#interval}.
        :param interval_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#interval_unit DlmLifecyclePolicy#interval_unit}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__750984b021ec143fb796c7fd32651c59491f029ab7e920b3808e2bdbb8a7ba97)
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
            check_type(argname="argument interval_unit", value=interval_unit, expected_type=type_hints["interval_unit"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "interval": interval,
            "interval_unit": interval_unit,
        }

    @builtins.property
    def interval(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#interval DlmLifecyclePolicy#interval}.'''
        result = self._values.get("interval")
        assert result is not None, "Required property 'interval' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def interval_unit(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#interval_unit DlmLifecyclePolicy#interval_unit}.'''
        result = self._values.get("interval_unit")
        assert result is not None, "Required property 'interval_unit' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleRetainRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleRetainRuleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dlmLifecyclePolicy.DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleRetainRuleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9e6f87b8379b5a974c55f07a69467da597191baed7fc55a7a7e32e34990a7804)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="intervalInput")
    def interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "intervalInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalUnitInput")
    def interval_unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "intervalUnitInput"))

    @builtins.property
    @jsii.member(jsii_name="interval")
    def interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "interval"))

    @interval.setter
    def interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60dc99f9f1f26fb57a3567453ba166e4069f88015db0679d139fdf01078d0886)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interval", value)

    @builtins.property
    @jsii.member(jsii_name="intervalUnit")
    def interval_unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "intervalUnit"))

    @interval_unit.setter
    def interval_unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df2a03c268832edbab1f67fbfb33526b2a6c58f6f0d19f9230945f7058065a22)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intervalUnit", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleRetainRule]:
        return typing.cast(typing.Optional[DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleRetainRule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleRetainRule],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64b9bdf118cca4a033e247b125fa51ef39d6ebe90dd57a19fc24401f46aa3b1c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dlmLifecyclePolicy.DlmLifecyclePolicyPolicyDetailsScheduleDeprecateRule",
    jsii_struct_bases=[],
    name_mapping={
        "count": "count",
        "interval": "interval",
        "interval_unit": "intervalUnit",
    },
)
class DlmLifecyclePolicyPolicyDetailsScheduleDeprecateRule:
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        interval: typing.Optional[jsii.Number] = None,
        interval_unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#count DlmLifecyclePolicy#count}.
        :param interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#interval DlmLifecyclePolicy#interval}.
        :param interval_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#interval_unit DlmLifecyclePolicy#interval_unit}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d33b76c2a1a0c549d1f1b8e22b7b8274bc7f5c43ef5d140f3304a7028ee98ebc)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
            check_type(argname="argument interval_unit", value=interval_unit, expected_type=type_hints["interval_unit"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if count is not None:
            self._values["count"] = count
        if interval is not None:
            self._values["interval"] = interval
        if interval_unit is not None:
            self._values["interval_unit"] = interval_unit

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#count DlmLifecyclePolicy#count}.'''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def interval(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#interval DlmLifecyclePolicy#interval}.'''
        result = self._values.get("interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def interval_unit(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#interval_unit DlmLifecyclePolicy#interval_unit}.'''
        result = self._values.get("interval_unit")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DlmLifecyclePolicyPolicyDetailsScheduleDeprecateRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DlmLifecyclePolicyPolicyDetailsScheduleDeprecateRuleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dlmLifecyclePolicy.DlmLifecyclePolicyPolicyDetailsScheduleDeprecateRuleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__185cd91d95f95678060d183464a0c1fa95200576179825f33db70d3cf24002f2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCount")
    def reset_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCount", []))

    @jsii.member(jsii_name="resetInterval")
    def reset_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInterval", []))

    @jsii.member(jsii_name="resetIntervalUnit")
    def reset_interval_unit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIntervalUnit", []))

    @builtins.property
    @jsii.member(jsii_name="countInput")
    def count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "countInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalInput")
    def interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "intervalInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalUnitInput")
    def interval_unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "intervalUnitInput"))

    @builtins.property
    @jsii.member(jsii_name="count")
    def count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "count"))

    @count.setter
    def count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__840bb71371bf8c961ba25789c942148e0655797c872e7c2b40b964b73ed45623)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "count", value)

    @builtins.property
    @jsii.member(jsii_name="interval")
    def interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "interval"))

    @interval.setter
    def interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0621b7896e4fd76eb21a2907ae2ff1d7f6f91cf8a98daddc287e529755563ab1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interval", value)

    @builtins.property
    @jsii.member(jsii_name="intervalUnit")
    def interval_unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "intervalUnit"))

    @interval_unit.setter
    def interval_unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33a4ad4b5de97dd550388a2e6d0957e34ab29517ef6d7f6a4af9fbeab8d5912a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intervalUnit", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DlmLifecyclePolicyPolicyDetailsScheduleDeprecateRule]:
        return typing.cast(typing.Optional[DlmLifecyclePolicyPolicyDetailsScheduleDeprecateRule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DlmLifecyclePolicyPolicyDetailsScheduleDeprecateRule],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b6fb4c694a031cfd53fdfc6d03f53ed6eb00f5d3e031266cf897d29e5d79f90)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dlmLifecyclePolicy.DlmLifecyclePolicyPolicyDetailsScheduleFastRestoreRule",
    jsii_struct_bases=[],
    name_mapping={
        "availability_zones": "availabilityZones",
        "count": "count",
        "interval": "interval",
        "interval_unit": "intervalUnit",
    },
)
class DlmLifecyclePolicyPolicyDetailsScheduleFastRestoreRule:
    def __init__(
        self,
        *,
        availability_zones: typing.Sequence[builtins.str],
        count: typing.Optional[jsii.Number] = None,
        interval: typing.Optional[jsii.Number] = None,
        interval_unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param availability_zones: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#availability_zones DlmLifecyclePolicy#availability_zones}.
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#count DlmLifecyclePolicy#count}.
        :param interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#interval DlmLifecyclePolicy#interval}.
        :param interval_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#interval_unit DlmLifecyclePolicy#interval_unit}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__617277db96aa53b300a863eed26a22fccf28a2157e18641d561c0f6c3f26df37)
            check_type(argname="argument availability_zones", value=availability_zones, expected_type=type_hints["availability_zones"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
            check_type(argname="argument interval_unit", value=interval_unit, expected_type=type_hints["interval_unit"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "availability_zones": availability_zones,
        }
        if count is not None:
            self._values["count"] = count
        if interval is not None:
            self._values["interval"] = interval
        if interval_unit is not None:
            self._values["interval_unit"] = interval_unit

    @builtins.property
    def availability_zones(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#availability_zones DlmLifecyclePolicy#availability_zones}.'''
        result = self._values.get("availability_zones")
        assert result is not None, "Required property 'availability_zones' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#count DlmLifecyclePolicy#count}.'''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def interval(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#interval DlmLifecyclePolicy#interval}.'''
        result = self._values.get("interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def interval_unit(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#interval_unit DlmLifecyclePolicy#interval_unit}.'''
        result = self._values.get("interval_unit")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DlmLifecyclePolicyPolicyDetailsScheduleFastRestoreRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DlmLifecyclePolicyPolicyDetailsScheduleFastRestoreRuleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dlmLifecyclePolicy.DlmLifecyclePolicyPolicyDetailsScheduleFastRestoreRuleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fad53dcf086e1cdec6b3699c911c6eb42f7917041ad3c69744524fc340756fa2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCount")
    def reset_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCount", []))

    @jsii.member(jsii_name="resetInterval")
    def reset_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInterval", []))

    @jsii.member(jsii_name="resetIntervalUnit")
    def reset_interval_unit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIntervalUnit", []))

    @builtins.property
    @jsii.member(jsii_name="availabilityZonesInput")
    def availability_zones_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "availabilityZonesInput"))

    @builtins.property
    @jsii.member(jsii_name="countInput")
    def count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "countInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalInput")
    def interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "intervalInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalUnitInput")
    def interval_unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "intervalUnitInput"))

    @builtins.property
    @jsii.member(jsii_name="availabilityZones")
    def availability_zones(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "availabilityZones"))

    @availability_zones.setter
    def availability_zones(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f17f2a978b8f200916d7f4fd713a4659aefbe49679f5b12c871bb6c0dac4ae7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZones", value)

    @builtins.property
    @jsii.member(jsii_name="count")
    def count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "count"))

    @count.setter
    def count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24fc566d01f7466258b67fcb9847946db09c11cd23bfe841507a9659611eccf8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "count", value)

    @builtins.property
    @jsii.member(jsii_name="interval")
    def interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "interval"))

    @interval.setter
    def interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b3c6a1e77c2b6166a5713523908cf7f69cc2536c8544c7ade826f9efee28607)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interval", value)

    @builtins.property
    @jsii.member(jsii_name="intervalUnit")
    def interval_unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "intervalUnit"))

    @interval_unit.setter
    def interval_unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__adbd60de18acb3d9403f7d4a2cff89fd926f808afc0523d5cf0e27ad864b1e5c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intervalUnit", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DlmLifecyclePolicyPolicyDetailsScheduleFastRestoreRule]:
        return typing.cast(typing.Optional[DlmLifecyclePolicyPolicyDetailsScheduleFastRestoreRule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DlmLifecyclePolicyPolicyDetailsScheduleFastRestoreRule],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6b261d58efa085612c66a25d9ae79f2a3e2f590ab2e4e1904e911943eae2773)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DlmLifecyclePolicyPolicyDetailsScheduleList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dlmLifecyclePolicy.DlmLifecyclePolicyPolicyDetailsScheduleList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e33a6d652467177457bdc30edde62c85bd57d5f6d01785e3a7373df27ff13a5f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DlmLifecyclePolicyPolicyDetailsScheduleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2d88b6756a6f7182049e766335d6ff8f9a3ee673e8b55c50c50dcfc2eacdd74)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DlmLifecyclePolicyPolicyDetailsScheduleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33d772011850633498565f2946ae46e5c2aa5ab2e3aa97dc527770ab1e46daf3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0a80ed3a17704ad9dd7c712cbcba5fb985a980a4569b316be9005c46df918b47)
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
            type_hints = typing.get_type_hints(_typecheckingstub__db600a5048876df1ca3bc568910f403fce068178394dd78f100d0c1b4e0aec40)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DlmLifecyclePolicyPolicyDetailsSchedule]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DlmLifecyclePolicyPolicyDetailsSchedule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DlmLifecyclePolicyPolicyDetailsSchedule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efe469eeabb110571968f6122d03429ba65516575f6b165e100167dcaf1a7f89)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DlmLifecyclePolicyPolicyDetailsScheduleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dlmLifecyclePolicy.DlmLifecyclePolicyPolicyDetailsScheduleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__594366b0eb6621dfed908b25f1dabb9ea1df369a96164d9762677d1bc9fbec86)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putCreateRule")
    def put_create_rule(
        self,
        *,
        cron_expression: typing.Optional[builtins.str] = None,
        interval: typing.Optional[jsii.Number] = None,
        interval_unit: typing.Optional[builtins.str] = None,
        location: typing.Optional[builtins.str] = None,
        times: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param cron_expression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#cron_expression DlmLifecyclePolicy#cron_expression}.
        :param interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#interval DlmLifecyclePolicy#interval}.
        :param interval_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#interval_unit DlmLifecyclePolicy#interval_unit}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#location DlmLifecyclePolicy#location}.
        :param times: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#times DlmLifecyclePolicy#times}.
        '''
        value = DlmLifecyclePolicyPolicyDetailsScheduleCreateRule(
            cron_expression=cron_expression,
            interval=interval,
            interval_unit=interval_unit,
            location=location,
            times=times,
        )

        return typing.cast(None, jsii.invoke(self, "putCreateRule", [value]))

    @jsii.member(jsii_name="putCrossRegionCopyRule")
    def put_cross_region_copy_rule(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRule, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28322dcbe26eacdf890baef9f55883cd92a2b4a11f06229a5c4af100ff76c0c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCrossRegionCopyRule", [value]))

    @jsii.member(jsii_name="putDeprecateRule")
    def put_deprecate_rule(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        interval: typing.Optional[jsii.Number] = None,
        interval_unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#count DlmLifecyclePolicy#count}.
        :param interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#interval DlmLifecyclePolicy#interval}.
        :param interval_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#interval_unit DlmLifecyclePolicy#interval_unit}.
        '''
        value = DlmLifecyclePolicyPolicyDetailsScheduleDeprecateRule(
            count=count, interval=interval, interval_unit=interval_unit
        )

        return typing.cast(None, jsii.invoke(self, "putDeprecateRule", [value]))

    @jsii.member(jsii_name="putFastRestoreRule")
    def put_fast_restore_rule(
        self,
        *,
        availability_zones: typing.Sequence[builtins.str],
        count: typing.Optional[jsii.Number] = None,
        interval: typing.Optional[jsii.Number] = None,
        interval_unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param availability_zones: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#availability_zones DlmLifecyclePolicy#availability_zones}.
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#count DlmLifecyclePolicy#count}.
        :param interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#interval DlmLifecyclePolicy#interval}.
        :param interval_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#interval_unit DlmLifecyclePolicy#interval_unit}.
        '''
        value = DlmLifecyclePolicyPolicyDetailsScheduleFastRestoreRule(
            availability_zones=availability_zones,
            count=count,
            interval=interval,
            interval_unit=interval_unit,
        )

        return typing.cast(None, jsii.invoke(self, "putFastRestoreRule", [value]))

    @jsii.member(jsii_name="putRetainRule")
    def put_retain_rule(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        interval: typing.Optional[jsii.Number] = None,
        interval_unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#count DlmLifecyclePolicy#count}.
        :param interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#interval DlmLifecyclePolicy#interval}.
        :param interval_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#interval_unit DlmLifecyclePolicy#interval_unit}.
        '''
        value = DlmLifecyclePolicyPolicyDetailsScheduleRetainRule(
            count=count, interval=interval, interval_unit=interval_unit
        )

        return typing.cast(None, jsii.invoke(self, "putRetainRule", [value]))

    @jsii.member(jsii_name="putShareRule")
    def put_share_rule(
        self,
        *,
        target_accounts: typing.Sequence[builtins.str],
        unshare_interval: typing.Optional[jsii.Number] = None,
        unshare_interval_unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param target_accounts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#target_accounts DlmLifecyclePolicy#target_accounts}.
        :param unshare_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#unshare_interval DlmLifecyclePolicy#unshare_interval}.
        :param unshare_interval_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#unshare_interval_unit DlmLifecyclePolicy#unshare_interval_unit}.
        '''
        value = DlmLifecyclePolicyPolicyDetailsScheduleShareRule(
            target_accounts=target_accounts,
            unshare_interval=unshare_interval,
            unshare_interval_unit=unshare_interval_unit,
        )

        return typing.cast(None, jsii.invoke(self, "putShareRule", [value]))

    @jsii.member(jsii_name="resetCopyTags")
    def reset_copy_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCopyTags", []))

    @jsii.member(jsii_name="resetCrossRegionCopyRule")
    def reset_cross_region_copy_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCrossRegionCopyRule", []))

    @jsii.member(jsii_name="resetDeprecateRule")
    def reset_deprecate_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeprecateRule", []))

    @jsii.member(jsii_name="resetFastRestoreRule")
    def reset_fast_restore_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFastRestoreRule", []))

    @jsii.member(jsii_name="resetShareRule")
    def reset_share_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShareRule", []))

    @jsii.member(jsii_name="resetTagsToAdd")
    def reset_tags_to_add(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsToAdd", []))

    @jsii.member(jsii_name="resetVariableTags")
    def reset_variable_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVariableTags", []))

    @builtins.property
    @jsii.member(jsii_name="createRule")
    def create_rule(
        self,
    ) -> DlmLifecyclePolicyPolicyDetailsScheduleCreateRuleOutputReference:
        return typing.cast(DlmLifecyclePolicyPolicyDetailsScheduleCreateRuleOutputReference, jsii.get(self, "createRule"))

    @builtins.property
    @jsii.member(jsii_name="crossRegionCopyRule")
    def cross_region_copy_rule(
        self,
    ) -> DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleList:
        return typing.cast(DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleList, jsii.get(self, "crossRegionCopyRule"))

    @builtins.property
    @jsii.member(jsii_name="deprecateRule")
    def deprecate_rule(
        self,
    ) -> DlmLifecyclePolicyPolicyDetailsScheduleDeprecateRuleOutputReference:
        return typing.cast(DlmLifecyclePolicyPolicyDetailsScheduleDeprecateRuleOutputReference, jsii.get(self, "deprecateRule"))

    @builtins.property
    @jsii.member(jsii_name="fastRestoreRule")
    def fast_restore_rule(
        self,
    ) -> DlmLifecyclePolicyPolicyDetailsScheduleFastRestoreRuleOutputReference:
        return typing.cast(DlmLifecyclePolicyPolicyDetailsScheduleFastRestoreRuleOutputReference, jsii.get(self, "fastRestoreRule"))

    @builtins.property
    @jsii.member(jsii_name="retainRule")
    def retain_rule(
        self,
    ) -> "DlmLifecyclePolicyPolicyDetailsScheduleRetainRuleOutputReference":
        return typing.cast("DlmLifecyclePolicyPolicyDetailsScheduleRetainRuleOutputReference", jsii.get(self, "retainRule"))

    @builtins.property
    @jsii.member(jsii_name="shareRule")
    def share_rule(
        self,
    ) -> "DlmLifecyclePolicyPolicyDetailsScheduleShareRuleOutputReference":
        return typing.cast("DlmLifecyclePolicyPolicyDetailsScheduleShareRuleOutputReference", jsii.get(self, "shareRule"))

    @builtins.property
    @jsii.member(jsii_name="copyTagsInput")
    def copy_tags_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "copyTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="createRuleInput")
    def create_rule_input(
        self,
    ) -> typing.Optional[DlmLifecyclePolicyPolicyDetailsScheduleCreateRule]:
        return typing.cast(typing.Optional[DlmLifecyclePolicyPolicyDetailsScheduleCreateRule], jsii.get(self, "createRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="crossRegionCopyRuleInput")
    def cross_region_copy_rule_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRule]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRule]]], jsii.get(self, "crossRegionCopyRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="deprecateRuleInput")
    def deprecate_rule_input(
        self,
    ) -> typing.Optional[DlmLifecyclePolicyPolicyDetailsScheduleDeprecateRule]:
        return typing.cast(typing.Optional[DlmLifecyclePolicyPolicyDetailsScheduleDeprecateRule], jsii.get(self, "deprecateRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="fastRestoreRuleInput")
    def fast_restore_rule_input(
        self,
    ) -> typing.Optional[DlmLifecyclePolicyPolicyDetailsScheduleFastRestoreRule]:
        return typing.cast(typing.Optional[DlmLifecyclePolicyPolicyDetailsScheduleFastRestoreRule], jsii.get(self, "fastRestoreRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="retainRuleInput")
    def retain_rule_input(
        self,
    ) -> typing.Optional["DlmLifecyclePolicyPolicyDetailsScheduleRetainRule"]:
        return typing.cast(typing.Optional["DlmLifecyclePolicyPolicyDetailsScheduleRetainRule"], jsii.get(self, "retainRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="shareRuleInput")
    def share_rule_input(
        self,
    ) -> typing.Optional["DlmLifecyclePolicyPolicyDetailsScheduleShareRule"]:
        return typing.cast(typing.Optional["DlmLifecyclePolicyPolicyDetailsScheduleShareRule"], jsii.get(self, "shareRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsToAddInput")
    def tags_to_add_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsToAddInput"))

    @builtins.property
    @jsii.member(jsii_name="variableTagsInput")
    def variable_tags_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "variableTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="copyTags")
    def copy_tags(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "copyTags"))

    @copy_tags.setter
    def copy_tags(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93f94d79dedf4f9cf512138ba0dc5f7257eddebceed8b67dc96538006d34b600)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "copyTags", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad78bb3ee2392143b59c7db27637e3b4dd5f52901aab7dd76031ea3b83b1cd63)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tagsToAdd")
    def tags_to_add(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsToAdd"))

    @tags_to_add.setter
    def tags_to_add(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93f36ca573f4c4543af48a9aecb752377f356c3073d1c8b4695f41380aca024c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsToAdd", value)

    @builtins.property
    @jsii.member(jsii_name="variableTags")
    def variable_tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "variableTags"))

    @variable_tags.setter
    def variable_tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb13910d40b2d0a0c411425790bd35ed25dd1be0a74c055b1e3590e7d50659f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "variableTags", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DlmLifecyclePolicyPolicyDetailsSchedule, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DlmLifecyclePolicyPolicyDetailsSchedule, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DlmLifecyclePolicyPolicyDetailsSchedule, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__198c59112ccb1f8ce04ae9ceb749af51e0f3211f4738fe9d82b255ef432db876)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dlmLifecyclePolicy.DlmLifecyclePolicyPolicyDetailsScheduleRetainRule",
    jsii_struct_bases=[],
    name_mapping={
        "count": "count",
        "interval": "interval",
        "interval_unit": "intervalUnit",
    },
)
class DlmLifecyclePolicyPolicyDetailsScheduleRetainRule:
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        interval: typing.Optional[jsii.Number] = None,
        interval_unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#count DlmLifecyclePolicy#count}.
        :param interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#interval DlmLifecyclePolicy#interval}.
        :param interval_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#interval_unit DlmLifecyclePolicy#interval_unit}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e657a7b20d0a585443d900338b1b75531f470310b3c9bceb9bb7e72146168029)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
            check_type(argname="argument interval_unit", value=interval_unit, expected_type=type_hints["interval_unit"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if count is not None:
            self._values["count"] = count
        if interval is not None:
            self._values["interval"] = interval
        if interval_unit is not None:
            self._values["interval_unit"] = interval_unit

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#count DlmLifecyclePolicy#count}.'''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def interval(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#interval DlmLifecyclePolicy#interval}.'''
        result = self._values.get("interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def interval_unit(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#interval_unit DlmLifecyclePolicy#interval_unit}.'''
        result = self._values.get("interval_unit")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DlmLifecyclePolicyPolicyDetailsScheduleRetainRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DlmLifecyclePolicyPolicyDetailsScheduleRetainRuleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dlmLifecyclePolicy.DlmLifecyclePolicyPolicyDetailsScheduleRetainRuleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6841bbac9c53a6f12fc222913e280d911b59eceb632ceea3f90d17856a69f369)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCount")
    def reset_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCount", []))

    @jsii.member(jsii_name="resetInterval")
    def reset_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInterval", []))

    @jsii.member(jsii_name="resetIntervalUnit")
    def reset_interval_unit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIntervalUnit", []))

    @builtins.property
    @jsii.member(jsii_name="countInput")
    def count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "countInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalInput")
    def interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "intervalInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalUnitInput")
    def interval_unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "intervalUnitInput"))

    @builtins.property
    @jsii.member(jsii_name="count")
    def count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "count"))

    @count.setter
    def count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0562a7a86b565f1e516090df5e4e85bc6335b9e2daa812dc52983dba7fcac119)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "count", value)

    @builtins.property
    @jsii.member(jsii_name="interval")
    def interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "interval"))

    @interval.setter
    def interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e75816c36c553422847c66e0ff9492ae956d111f41044cbf36e2853c3459f15)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interval", value)

    @builtins.property
    @jsii.member(jsii_name="intervalUnit")
    def interval_unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "intervalUnit"))

    @interval_unit.setter
    def interval_unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e894ed680f591461bfa941a190e60a3b644f41ae73446f5657864dd151eea2a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intervalUnit", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DlmLifecyclePolicyPolicyDetailsScheduleRetainRule]:
        return typing.cast(typing.Optional[DlmLifecyclePolicyPolicyDetailsScheduleRetainRule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DlmLifecyclePolicyPolicyDetailsScheduleRetainRule],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__351855a0909572eb69c6327935430af7cec9faf32acc7ba863db49a65c66e12a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dlmLifecyclePolicy.DlmLifecyclePolicyPolicyDetailsScheduleShareRule",
    jsii_struct_bases=[],
    name_mapping={
        "target_accounts": "targetAccounts",
        "unshare_interval": "unshareInterval",
        "unshare_interval_unit": "unshareIntervalUnit",
    },
)
class DlmLifecyclePolicyPolicyDetailsScheduleShareRule:
    def __init__(
        self,
        *,
        target_accounts: typing.Sequence[builtins.str],
        unshare_interval: typing.Optional[jsii.Number] = None,
        unshare_interval_unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param target_accounts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#target_accounts DlmLifecyclePolicy#target_accounts}.
        :param unshare_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#unshare_interval DlmLifecyclePolicy#unshare_interval}.
        :param unshare_interval_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#unshare_interval_unit DlmLifecyclePolicy#unshare_interval_unit}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e56ee1b4df94d3c2939bcf1e953f88dc602b4c2c63922058012b718ce3090599)
            check_type(argname="argument target_accounts", value=target_accounts, expected_type=type_hints["target_accounts"])
            check_type(argname="argument unshare_interval", value=unshare_interval, expected_type=type_hints["unshare_interval"])
            check_type(argname="argument unshare_interval_unit", value=unshare_interval_unit, expected_type=type_hints["unshare_interval_unit"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "target_accounts": target_accounts,
        }
        if unshare_interval is not None:
            self._values["unshare_interval"] = unshare_interval
        if unshare_interval_unit is not None:
            self._values["unshare_interval_unit"] = unshare_interval_unit

    @builtins.property
    def target_accounts(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#target_accounts DlmLifecyclePolicy#target_accounts}.'''
        result = self._values.get("target_accounts")
        assert result is not None, "Required property 'target_accounts' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def unshare_interval(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#unshare_interval DlmLifecyclePolicy#unshare_interval}.'''
        result = self._values.get("unshare_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def unshare_interval_unit(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy#unshare_interval_unit DlmLifecyclePolicy#unshare_interval_unit}.'''
        result = self._values.get("unshare_interval_unit")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DlmLifecyclePolicyPolicyDetailsScheduleShareRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DlmLifecyclePolicyPolicyDetailsScheduleShareRuleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dlmLifecyclePolicy.DlmLifecyclePolicyPolicyDetailsScheduleShareRuleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7597ab8282e55191e833d1d5b508471977abf269d1878970ad159b14086562c6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetUnshareInterval")
    def reset_unshare_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnshareInterval", []))

    @jsii.member(jsii_name="resetUnshareIntervalUnit")
    def reset_unshare_interval_unit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnshareIntervalUnit", []))

    @builtins.property
    @jsii.member(jsii_name="targetAccountsInput")
    def target_accounts_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "targetAccountsInput"))

    @builtins.property
    @jsii.member(jsii_name="unshareIntervalInput")
    def unshare_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "unshareIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="unshareIntervalUnitInput")
    def unshare_interval_unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unshareIntervalUnitInput"))

    @builtins.property
    @jsii.member(jsii_name="targetAccounts")
    def target_accounts(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "targetAccounts"))

    @target_accounts.setter
    def target_accounts(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__911d8c649437bc19631201cb4fa8c2f56a5f525a3da10862a9253bd5aba5ec4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetAccounts", value)

    @builtins.property
    @jsii.member(jsii_name="unshareInterval")
    def unshare_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "unshareInterval"))

    @unshare_interval.setter
    def unshare_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4cc585202476dbb2f086f025b3c5351534b49bc2f9f189b8c4ec3775f2d6de8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unshareInterval", value)

    @builtins.property
    @jsii.member(jsii_name="unshareIntervalUnit")
    def unshare_interval_unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unshareIntervalUnit"))

    @unshare_interval_unit.setter
    def unshare_interval_unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89d0be0e8bb591f02144c431afb02849d49eb114d83380912d348a0cb8c2650d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unshareIntervalUnit", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DlmLifecyclePolicyPolicyDetailsScheduleShareRule]:
        return typing.cast(typing.Optional[DlmLifecyclePolicyPolicyDetailsScheduleShareRule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DlmLifecyclePolicyPolicyDetailsScheduleShareRule],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1a00de4b7293361ea385669941de45068c3ab87de7e58df00511245cfc6c459)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DlmLifecyclePolicy",
    "DlmLifecyclePolicyConfig",
    "DlmLifecyclePolicyPolicyDetails",
    "DlmLifecyclePolicyPolicyDetailsAction",
    "DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopy",
    "DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyEncryptionConfiguration",
    "DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyEncryptionConfigurationOutputReference",
    "DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyList",
    "DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyOutputReference",
    "DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyRetainRule",
    "DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyRetainRuleOutputReference",
    "DlmLifecyclePolicyPolicyDetailsActionOutputReference",
    "DlmLifecyclePolicyPolicyDetailsEventSource",
    "DlmLifecyclePolicyPolicyDetailsEventSourceOutputReference",
    "DlmLifecyclePolicyPolicyDetailsEventSourceParameters",
    "DlmLifecyclePolicyPolicyDetailsEventSourceParametersOutputReference",
    "DlmLifecyclePolicyPolicyDetailsOutputReference",
    "DlmLifecyclePolicyPolicyDetailsParameters",
    "DlmLifecyclePolicyPolicyDetailsParametersOutputReference",
    "DlmLifecyclePolicyPolicyDetailsSchedule",
    "DlmLifecyclePolicyPolicyDetailsScheduleCreateRule",
    "DlmLifecyclePolicyPolicyDetailsScheduleCreateRuleOutputReference",
    "DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRule",
    "DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleDeprecateRule",
    "DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleDeprecateRuleOutputReference",
    "DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleList",
    "DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleOutputReference",
    "DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleRetainRule",
    "DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleRetainRuleOutputReference",
    "DlmLifecyclePolicyPolicyDetailsScheduleDeprecateRule",
    "DlmLifecyclePolicyPolicyDetailsScheduleDeprecateRuleOutputReference",
    "DlmLifecyclePolicyPolicyDetailsScheduleFastRestoreRule",
    "DlmLifecyclePolicyPolicyDetailsScheduleFastRestoreRuleOutputReference",
    "DlmLifecyclePolicyPolicyDetailsScheduleList",
    "DlmLifecyclePolicyPolicyDetailsScheduleOutputReference",
    "DlmLifecyclePolicyPolicyDetailsScheduleRetainRule",
    "DlmLifecyclePolicyPolicyDetailsScheduleRetainRuleOutputReference",
    "DlmLifecyclePolicyPolicyDetailsScheduleShareRule",
    "DlmLifecyclePolicyPolicyDetailsScheduleShareRuleOutputReference",
]

publication.publish()

def _typecheckingstub__5a711b3694b2b58c3a2eafae18cca5fef5ec5b0cb85bf0b1d7c76d4ebe733345(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    description: builtins.str,
    execution_role_arn: builtins.str,
    policy_details: typing.Union[DlmLifecyclePolicyPolicyDetails, typing.Dict[builtins.str, typing.Any]],
    id: typing.Optional[builtins.str] = None,
    state: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__cb51c46523bc4dfa848063df9e12153b679169d0f52947ba5c35261d2324cc1d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8224ec627227a5ca04eda7fb4ddcd39613083201ad3f98a0f0ef2d25fd53f59(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__001fd7ce3bf9a783b2e59ba343e55a24f1483d393d226d648f092ce04c2ae071(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__711db73513a2e3feff3baa6d90e6bd0ae0ccf2a0afd7edc2e6d31fe7ab6e2ea1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb752cfabe1cd3871753b8b40c4dfbad9669060160beea013c594f12024f5a3f(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06f651a57513a0d108d4d0388e2e3bb4a5c8c616d800ccbd6c69702b1eb4dbce(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f5d54b72101466ce55a8b0c6568181b2a83ed98514f38e8b7eac7a35e8b2923(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    description: builtins.str,
    execution_role_arn: builtins.str,
    policy_details: typing.Union[DlmLifecyclePolicyPolicyDetails, typing.Dict[builtins.str, typing.Any]],
    id: typing.Optional[builtins.str] = None,
    state: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19c9abf860401b5a2a67ec8023fa0c4f5af72cd2befd2cb184798abb8ec97cd0(
    *,
    action: typing.Optional[typing.Union[DlmLifecyclePolicyPolicyDetailsAction, typing.Dict[builtins.str, typing.Any]]] = None,
    event_source: typing.Optional[typing.Union[DlmLifecyclePolicyPolicyDetailsEventSource, typing.Dict[builtins.str, typing.Any]]] = None,
    parameters: typing.Optional[typing.Union[DlmLifecyclePolicyPolicyDetailsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    policy_type: typing.Optional[builtins.str] = None,
    resource_locations: typing.Optional[typing.Sequence[builtins.str]] = None,
    resource_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    schedule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DlmLifecyclePolicyPolicyDetailsSchedule, typing.Dict[builtins.str, typing.Any]]]]] = None,
    target_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c76b635fae27e8b463fdaf324ab8edfdfd9d4bad102dfe72a54c075a109c996(
    *,
    cross_region_copy: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopy, typing.Dict[builtins.str, typing.Any]]]],
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d12af520dd34fa3964de49a7a5c3382d766a667c3b04abecd8742357cdaf4b24(
    *,
    encryption_configuration: typing.Union[DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyEncryptionConfiguration, typing.Dict[builtins.str, typing.Any]],
    target: builtins.str,
    retain_rule: typing.Optional[typing.Union[DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyRetainRule, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e15a1c3b0d06cde048b58525a1c8aae1e82ffd0f1c0a515e15246619f4a83b7b(
    *,
    cmk_arn: typing.Optional[builtins.str] = None,
    encrypted: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f19293be56ab2aa65632832d6ba4f5ec59d1fefa286f1475c49e105815a7e529(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d419f8960f00950eded7b5be42018c9593657cc6dd6057acebc89f98b162489a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6edb5569d521a4d10aa01b8b4e0a61666063d50a62afd477cc3590f04bb514f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10b0523b4aaa5c942e0bfeea35d31ba466c6bdbc49d8b5a8c0120f9fc34a85a6(
    value: typing.Optional[DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyEncryptionConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a0768b061831184dbf4e7af743f723d713f182c06c0cb35900bb2c514a1017f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2a07016e38bb228d68cce2c12d7908e730c3f86e5a163807b7579d17e1ea94a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9dbd2bc3502714f85051e9d31030aac132252d26319213eb3be950eaa509f433(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0d8dd813f3f84d6c7adad65f0d8a77e505d039546bad728d6786a9f754353d7(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c46a06c3b5953c0d55f4c1cc12b7e2ff3b77a1baf7712092adbc194d75bcb78e(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09aa4927ba40e4312c44681cc85b233dc2afa0dcdfdadc1a53121da21d23d1a3(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopy]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82e113c02addcd7b996f119f672625328e260861b09359225176a4ca6ba66de8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5bb74111817787f476eb5eb122314dcdb7984b341666be0124aad08f47f6cf5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c17ea11d40a614ba4ae86e567c818598783cd0080a1ca3658b842d0c56878eb(
    value: typing.Optional[typing.Union[DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopy, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ca73aed3f37c9ff9adb7cba95823fd6743b9761b5f67bb2ebe6f17df0aa09a3(
    *,
    interval: jsii.Number,
    interval_unit: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3beb176077353192de7e2ddf4f7ebcbb87eef127d98e5bcaaee72d77fa96e7ff(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb3e1343c30c9a6becbfad542e9a996171e5b1a486e35325b14985142677d723(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a18a96c3fdf4d34accf0eb35a8fcfdc03d608379cf7f6e642cdde96854c8bef9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4aee30f57bb3c708bc75c10bc26eee43a54cbc6eae2366d7899719bd4974c2c(
    value: typing.Optional[DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopyRetainRule],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7ddf03af3c199345a8dd19e22356f8fe7b745f6d0a54742f848525c6adb2f1d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd1d889d2e1e3a03543ac07db12859e3f8c9a4808fb8922e53fdd991a038acf2(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DlmLifecyclePolicyPolicyDetailsActionCrossRegionCopy, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2f3182495cda418106f459a0cfbd103998c55a49c993b7e69a3734094d405a3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bf944708a74ef440d310d463936d788135f0836b3599e8578bb03f5620bb38b(
    value: typing.Optional[DlmLifecyclePolicyPolicyDetailsAction],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a01d91b26c3c792b6daf082b9602bedcf2cf83f48b40175f0ba46efda32ed11(
    *,
    parameters: typing.Union[DlmLifecyclePolicyPolicyDetailsEventSourceParameters, typing.Dict[builtins.str, typing.Any]],
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6ec49fde22df52720a5c88a95c343d98b0c0761b2e2c4d49b0900de38e41698(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6e7cf49cd0429e1cb456932cc74656a302de893575040c836aea2fe1e986959(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5eb47f66c90cb849118dbaaad42c16b00f2e4190ce5608f5debbbdfe85160aa(
    value: typing.Optional[DlmLifecyclePolicyPolicyDetailsEventSource],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55420e53e96bdbba6410a9d5b208b03f4a9b66cc7c2a50fed08d9f8afedfa1ad(
    *,
    description_regex: builtins.str,
    event_type: builtins.str,
    snapshot_owner: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ea41bff7dceb806970197613213526b6ab5b597b83068d9aa0a192475a63c21(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff3546c335bf4baa0fecd464062204a476c877637440cc241940ae15015ef33b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5ce0f574e63239414d12c99de9a382b7bbcb025acd2c8e58535f4a97b9dcb7e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4907134970060bfde2bdcb572d6e43c03c17b38c36a103b568e41c8776dca32f(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17a482ca0e9ec7091d327b692c12261b084c7bb001f57d82343415eee4f25928(
    value: typing.Optional[DlmLifecyclePolicyPolicyDetailsEventSourceParameters],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac5b0c171b6730345a24321844f45ec026d24e8f550b686de16d0b41fd7a184b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e404fe6d137bd13801a94275bd290fe2a6e9690dc7b650fbc04bf74978096b21(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DlmLifecyclePolicyPolicyDetailsSchedule, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36a847b455815f3717a59b606df405e92fd023b5a8ffbb5475bdd89a1b735792(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df28a3700513e47607b48e8c725eb6eef6e62b4e51fba05712b35a496ffc5c02(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38d127fb71ee5d96b2ab4f26a1b1aefd9856dd5cd3b6c27ff702d29fd4690900(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd538b9cf214ae8b32c1d75d1b373ad1a18a71195cb126d8e8f3edbae1276105(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed4ed98106b6723b684b8bd4e94bf04cc4a506f5566254c77f566ec4fa4f7493(
    value: typing.Optional[DlmLifecyclePolicyPolicyDetails],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed76e802f67ec88739ebacbd4c8ed87c227bbd28f61e6b94a640f4e5a8fca9e3(
    *,
    exclude_boot_volume: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    no_reboot: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40ebdcc912be19064eacc4f6e0d37382b3aaa58eb044ca27bae1682c656b4fab(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a8d3b769c5a6feeffba32dbab7e1b222e9e7492a7b9ef5366827ee3d86e1390(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc7f45d5104604e2f4ed525e0c2208712a9b8636b18d385cf8bd555f02e504e1(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3df0052ef316123756cff06b9f954808eaa2666e1c78a406faa10359a0dd71a1(
    value: typing.Optional[DlmLifecyclePolicyPolicyDetailsParameters],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbd4f3ec6e6572a052d780f0e27c84842548eba3c08674e267ff5554227da734(
    *,
    create_rule: typing.Union[DlmLifecyclePolicyPolicyDetailsScheduleCreateRule, typing.Dict[builtins.str, typing.Any]],
    name: builtins.str,
    retain_rule: typing.Union[DlmLifecyclePolicyPolicyDetailsScheduleRetainRule, typing.Dict[builtins.str, typing.Any]],
    copy_tags: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    cross_region_copy_rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRule, typing.Dict[builtins.str, typing.Any]]]]] = None,
    deprecate_rule: typing.Optional[typing.Union[DlmLifecyclePolicyPolicyDetailsScheduleDeprecateRule, typing.Dict[builtins.str, typing.Any]]] = None,
    fast_restore_rule: typing.Optional[typing.Union[DlmLifecyclePolicyPolicyDetailsScheduleFastRestoreRule, typing.Dict[builtins.str, typing.Any]]] = None,
    share_rule: typing.Optional[typing.Union[DlmLifecyclePolicyPolicyDetailsScheduleShareRule, typing.Dict[builtins.str, typing.Any]]] = None,
    tags_to_add: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    variable_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e85bc714270af8309dba0098ff6117761ed203f05d649a90fa9ade08f660ff83(
    *,
    cron_expression: typing.Optional[builtins.str] = None,
    interval: typing.Optional[jsii.Number] = None,
    interval_unit: typing.Optional[builtins.str] = None,
    location: typing.Optional[builtins.str] = None,
    times: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9653b5823f3b20d8d8644a515bce1e9fe598d90055faa133e7bc1bf2e9cc7c4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b08ce8a22bc6117d172cd029f4ce92de07d467df878624213ee8b098eaf6633(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5febae01135fe00c45be5b2e8360ae6068d1c321ca4be719d625856a0a7f3f4(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d218638ad1919ebf5888934bc4114402cbdc9605887fe7026e151445e263ee07(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb996ef72baaea4a2cd151b11d89f316e492ce73ee87e54a407841bab553e6b0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d322d8045cfbcca26c5d37d98800cc3396bf6bcc94f70a532f9690a0226d8b3c(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e84753be706bc8ecdd2279f0210e8bcd5bdce3001e2ff7bb583f3d288ea92e5e(
    value: typing.Optional[DlmLifecyclePolicyPolicyDetailsScheduleCreateRule],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f8ad6449b2cf946c24973deefae1273f83f6d310326d8f601e44432d822ac19(
    *,
    encrypted: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    target: builtins.str,
    cmk_arn: typing.Optional[builtins.str] = None,
    copy_tags: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    deprecate_rule: typing.Optional[typing.Union[DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleDeprecateRule, typing.Dict[builtins.str, typing.Any]]] = None,
    retain_rule: typing.Optional[typing.Union[DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleRetainRule, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c12a2f4f2da0c69acba25557587584fb58d74ca6b47a1782360d4612163745fe(
    *,
    interval: jsii.Number,
    interval_unit: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26b057667ab085173a668e7b8f19133deaa71073d8262a5638ad192fe9bf3dd0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08eb49d89c4756f31b691fb01695ff335c685b23eb5d8d3719bb328d0262bcc5(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae3851a9aa0d40d1757285f7a13c41ef74c9b6e75e11f06e5ae97bd3f2081237(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7decadd0e8ce3a0df5b4259b3482ef3632627c1b13f40116a08d43c952dc11d7(
    value: typing.Optional[DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleDeprecateRule],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06e48b17ec8d3ce811010997f3d43f639dbad0ec397b47b4010029ccd3336c31(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db3a22eb4be79a05414bd8f590861fc14e327efabc021c01fecd18a88a574ebd(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1da5d71245392f45d3a690b67688ddc9106fe36e4884fafb2762032cf6b1ed2b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ecda70d4fc9dd89ff3070e56895c804562a76d5014518c13490cd0fadc8f2f4(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb049cadd1f8fdc9485671268a1ee6f3d810f0d0091fb48f4eb6f30a8d34c873(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b68c469022c1814d9acee2a6f674b2d4d3714433e74a6b55f706ec7ef3064eed(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRule]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8288f2aa30d2f6e3ad0524397ed74185c667edf9384764b2e86e72934bcd233(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb84d1f3d7a8cc137f82453c34b355b41172d3b11c22a91ba80525a28d247cbb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7835335961db94763f8e768955fc2e170002cb1d6e6826f0846444173131c1e3(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c8a63bfc37d38f0cd3f313c8b2aea3bfa363b6edd759f5ff14722e2ff49f8a6(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70a50bdebc50928377498c2a761db56e6a7ad16882e38cd9babd6892d2777ed9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d52da3fa37fed809e4dcd6154b14ce4ec7cbc0efe3e7de54c214fb3dd2a8f66(
    value: typing.Optional[typing.Union[DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRule, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__750984b021ec143fb796c7fd32651c59491f029ab7e920b3808e2bdbb8a7ba97(
    *,
    interval: jsii.Number,
    interval_unit: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e6f87b8379b5a974c55f07a69467da597191baed7fc55a7a7e32e34990a7804(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60dc99f9f1f26fb57a3567453ba166e4069f88015db0679d139fdf01078d0886(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df2a03c268832edbab1f67fbfb33526b2a6c58f6f0d19f9230945f7058065a22(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64b9bdf118cca4a033e247b125fa51ef39d6ebe90dd57a19fc24401f46aa3b1c(
    value: typing.Optional[DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleRetainRule],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d33b76c2a1a0c549d1f1b8e22b7b8274bc7f5c43ef5d140f3304a7028ee98ebc(
    *,
    count: typing.Optional[jsii.Number] = None,
    interval: typing.Optional[jsii.Number] = None,
    interval_unit: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__185cd91d95f95678060d183464a0c1fa95200576179825f33db70d3cf24002f2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__840bb71371bf8c961ba25789c942148e0655797c872e7c2b40b964b73ed45623(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0621b7896e4fd76eb21a2907ae2ff1d7f6f91cf8a98daddc287e529755563ab1(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33a4ad4b5de97dd550388a2e6d0957e34ab29517ef6d7f6a4af9fbeab8d5912a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b6fb4c694a031cfd53fdfc6d03f53ed6eb00f5d3e031266cf897d29e5d79f90(
    value: typing.Optional[DlmLifecyclePolicyPolicyDetailsScheduleDeprecateRule],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__617277db96aa53b300a863eed26a22fccf28a2157e18641d561c0f6c3f26df37(
    *,
    availability_zones: typing.Sequence[builtins.str],
    count: typing.Optional[jsii.Number] = None,
    interval: typing.Optional[jsii.Number] = None,
    interval_unit: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fad53dcf086e1cdec6b3699c911c6eb42f7917041ad3c69744524fc340756fa2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f17f2a978b8f200916d7f4fd713a4659aefbe49679f5b12c871bb6c0dac4ae7(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24fc566d01f7466258b67fcb9847946db09c11cd23bfe841507a9659611eccf8(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b3c6a1e77c2b6166a5713523908cf7f69cc2536c8544c7ade826f9efee28607(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adbd60de18acb3d9403f7d4a2cff89fd926f808afc0523d5cf0e27ad864b1e5c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6b261d58efa085612c66a25d9ae79f2a3e2f590ab2e4e1904e911943eae2773(
    value: typing.Optional[DlmLifecyclePolicyPolicyDetailsScheduleFastRestoreRule],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e33a6d652467177457bdc30edde62c85bd57d5f6d01785e3a7373df27ff13a5f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2d88b6756a6f7182049e766335d6ff8f9a3ee673e8b55c50c50dcfc2eacdd74(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33d772011850633498565f2946ae46e5c2aa5ab2e3aa97dc527770ab1e46daf3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a80ed3a17704ad9dd7c712cbcba5fb985a980a4569b316be9005c46df918b47(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db600a5048876df1ca3bc568910f403fce068178394dd78f100d0c1b4e0aec40(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efe469eeabb110571968f6122d03429ba65516575f6b165e100167dcaf1a7f89(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DlmLifecyclePolicyPolicyDetailsSchedule]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__594366b0eb6621dfed908b25f1dabb9ea1df369a96164d9762677d1bc9fbec86(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28322dcbe26eacdf890baef9f55883cd92a2b4a11f06229a5c4af100ff76c0c7(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DlmLifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRule, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93f94d79dedf4f9cf512138ba0dc5f7257eddebceed8b67dc96538006d34b600(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad78bb3ee2392143b59c7db27637e3b4dd5f52901aab7dd76031ea3b83b1cd63(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93f36ca573f4c4543af48a9aecb752377f356c3073d1c8b4695f41380aca024c(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb13910d40b2d0a0c411425790bd35ed25dd1be0a74c055b1e3590e7d50659f2(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__198c59112ccb1f8ce04ae9ceb749af51e0f3211f4738fe9d82b255ef432db876(
    value: typing.Optional[typing.Union[DlmLifecyclePolicyPolicyDetailsSchedule, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e657a7b20d0a585443d900338b1b75531f470310b3c9bceb9bb7e72146168029(
    *,
    count: typing.Optional[jsii.Number] = None,
    interval: typing.Optional[jsii.Number] = None,
    interval_unit: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6841bbac9c53a6f12fc222913e280d911b59eceb632ceea3f90d17856a69f369(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0562a7a86b565f1e516090df5e4e85bc6335b9e2daa812dc52983dba7fcac119(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e75816c36c553422847c66e0ff9492ae956d111f41044cbf36e2853c3459f15(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e894ed680f591461bfa941a190e60a3b644f41ae73446f5657864dd151eea2a7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__351855a0909572eb69c6327935430af7cec9faf32acc7ba863db49a65c66e12a(
    value: typing.Optional[DlmLifecyclePolicyPolicyDetailsScheduleRetainRule],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e56ee1b4df94d3c2939bcf1e953f88dc602b4c2c63922058012b718ce3090599(
    *,
    target_accounts: typing.Sequence[builtins.str],
    unshare_interval: typing.Optional[jsii.Number] = None,
    unshare_interval_unit: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7597ab8282e55191e833d1d5b508471977abf269d1878970ad159b14086562c6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__911d8c649437bc19631201cb4fa8c2f56a5f525a3da10862a9253bd5aba5ec4e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4cc585202476dbb2f086f025b3c5351534b49bc2f9f189b8c4ec3775f2d6de8(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89d0be0e8bb591f02144c431afb02849d49eb114d83380912d348a0cb8c2650d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1a00de4b7293361ea385669941de45068c3ab87de7e58df00511245cfc6c459(
    value: typing.Optional[DlmLifecyclePolicyPolicyDetailsScheduleShareRule],
) -> None:
    """Type checking stubs"""
    pass
