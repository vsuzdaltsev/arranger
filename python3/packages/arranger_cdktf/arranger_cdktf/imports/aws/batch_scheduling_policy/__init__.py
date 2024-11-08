'''
# `aws_batch_scheduling_policy`

Refer to the Terraform Registory for docs: [`aws_batch_scheduling_policy`](https://www.terraform.io/docs/providers/aws/r/batch_scheduling_policy).
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


class BatchSchedulingPolicy(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.batchSchedulingPolicy.BatchSchedulingPolicy",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/batch_scheduling_policy aws_batch_scheduling_policy}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        fair_share_policy: typing.Optional[typing.Union["BatchSchedulingPolicyFairSharePolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/batch_scheduling_policy aws_batch_scheduling_policy} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_scheduling_policy#name BatchSchedulingPolicy#name}.
        :param fair_share_policy: fair_share_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_scheduling_policy#fair_share_policy BatchSchedulingPolicy#fair_share_policy}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_scheduling_policy#id BatchSchedulingPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_scheduling_policy#tags BatchSchedulingPolicy#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_scheduling_policy#tags_all BatchSchedulingPolicy#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c23181835eaee9da3b86dd1fb2bf063d8f36326c9885cc5bdad191d2274c8de2)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = BatchSchedulingPolicyConfig(
            name=name,
            fair_share_policy=fair_share_policy,
            id=id,
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

    @jsii.member(jsii_name="putFairSharePolicy")
    def put_fair_share_policy(
        self,
        *,
        compute_reservation: typing.Optional[jsii.Number] = None,
        share_decay_seconds: typing.Optional[jsii.Number] = None,
        share_distribution: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["BatchSchedulingPolicyFairSharePolicyShareDistribution", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param compute_reservation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_scheduling_policy#compute_reservation BatchSchedulingPolicy#compute_reservation}.
        :param share_decay_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_scheduling_policy#share_decay_seconds BatchSchedulingPolicy#share_decay_seconds}.
        :param share_distribution: share_distribution block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_scheduling_policy#share_distribution BatchSchedulingPolicy#share_distribution}
        '''
        value = BatchSchedulingPolicyFairSharePolicy(
            compute_reservation=compute_reservation,
            share_decay_seconds=share_decay_seconds,
            share_distribution=share_distribution,
        )

        return typing.cast(None, jsii.invoke(self, "putFairSharePolicy", [value]))

    @jsii.member(jsii_name="resetFairSharePolicy")
    def reset_fair_share_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFairSharePolicy", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

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
    @jsii.member(jsii_name="fairSharePolicy")
    def fair_share_policy(
        self,
    ) -> "BatchSchedulingPolicyFairSharePolicyOutputReference":
        return typing.cast("BatchSchedulingPolicyFairSharePolicyOutputReference", jsii.get(self, "fairSharePolicy"))

    @builtins.property
    @jsii.member(jsii_name="fairSharePolicyInput")
    def fair_share_policy_input(
        self,
    ) -> typing.Optional["BatchSchedulingPolicyFairSharePolicy"]:
        return typing.cast(typing.Optional["BatchSchedulingPolicyFairSharePolicy"], jsii.get(self, "fairSharePolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

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
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d2eefd93c86b28cce38fc3de853893d444ebfd37f5d4c1572dc1ad90bab2f8b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cfe791332925806a1eca0249f8d25a2f858ef756bd3a78add71f1f3170bea08)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9216bcad1a32f691ab7d5ee189f935b05640beba76b83976bb955d15de3629e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__422aa5f9e3ba992357f02798fc665528f4c36af2b6b0eba7399030fba1a3b656)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.batchSchedulingPolicy.BatchSchedulingPolicyConfig",
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
        "fair_share_policy": "fairSharePolicy",
        "id": "id",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class BatchSchedulingPolicyConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        fair_share_policy: typing.Optional[typing.Union["BatchSchedulingPolicyFairSharePolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
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
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_scheduling_policy#name BatchSchedulingPolicy#name}.
        :param fair_share_policy: fair_share_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_scheduling_policy#fair_share_policy BatchSchedulingPolicy#fair_share_policy}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_scheduling_policy#id BatchSchedulingPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_scheduling_policy#tags BatchSchedulingPolicy#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_scheduling_policy#tags_all BatchSchedulingPolicy#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(fair_share_policy, dict):
            fair_share_policy = BatchSchedulingPolicyFairSharePolicy(**fair_share_policy)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1e3588e7680621dcb554196c931a1fd9e066617019ebbf134d9a9de4cac0de8)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument fair_share_policy", value=fair_share_policy, expected_type=type_hints["fair_share_policy"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
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
        if fair_share_policy is not None:
            self._values["fair_share_policy"] = fair_share_policy
        if id is not None:
            self._values["id"] = id
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
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_scheduling_policy#name BatchSchedulingPolicy#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fair_share_policy(
        self,
    ) -> typing.Optional["BatchSchedulingPolicyFairSharePolicy"]:
        '''fair_share_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_scheduling_policy#fair_share_policy BatchSchedulingPolicy#fair_share_policy}
        '''
        result = self._values.get("fair_share_policy")
        return typing.cast(typing.Optional["BatchSchedulingPolicyFairSharePolicy"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_scheduling_policy#id BatchSchedulingPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_scheduling_policy#tags BatchSchedulingPolicy#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_scheduling_policy#tags_all BatchSchedulingPolicy#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BatchSchedulingPolicyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.batchSchedulingPolicy.BatchSchedulingPolicyFairSharePolicy",
    jsii_struct_bases=[],
    name_mapping={
        "compute_reservation": "computeReservation",
        "share_decay_seconds": "shareDecaySeconds",
        "share_distribution": "shareDistribution",
    },
)
class BatchSchedulingPolicyFairSharePolicy:
    def __init__(
        self,
        *,
        compute_reservation: typing.Optional[jsii.Number] = None,
        share_decay_seconds: typing.Optional[jsii.Number] = None,
        share_distribution: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["BatchSchedulingPolicyFairSharePolicyShareDistribution", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param compute_reservation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_scheduling_policy#compute_reservation BatchSchedulingPolicy#compute_reservation}.
        :param share_decay_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_scheduling_policy#share_decay_seconds BatchSchedulingPolicy#share_decay_seconds}.
        :param share_distribution: share_distribution block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_scheduling_policy#share_distribution BatchSchedulingPolicy#share_distribution}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c192916655f4acb261809d98e8fcba2e323259c47c18b75d3d2f0d9cb9b71de)
            check_type(argname="argument compute_reservation", value=compute_reservation, expected_type=type_hints["compute_reservation"])
            check_type(argname="argument share_decay_seconds", value=share_decay_seconds, expected_type=type_hints["share_decay_seconds"])
            check_type(argname="argument share_distribution", value=share_distribution, expected_type=type_hints["share_distribution"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if compute_reservation is not None:
            self._values["compute_reservation"] = compute_reservation
        if share_decay_seconds is not None:
            self._values["share_decay_seconds"] = share_decay_seconds
        if share_distribution is not None:
            self._values["share_distribution"] = share_distribution

    @builtins.property
    def compute_reservation(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_scheduling_policy#compute_reservation BatchSchedulingPolicy#compute_reservation}.'''
        result = self._values.get("compute_reservation")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def share_decay_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_scheduling_policy#share_decay_seconds BatchSchedulingPolicy#share_decay_seconds}.'''
        result = self._values.get("share_decay_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def share_distribution(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["BatchSchedulingPolicyFairSharePolicyShareDistribution"]]]:
        '''share_distribution block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_scheduling_policy#share_distribution BatchSchedulingPolicy#share_distribution}
        '''
        result = self._values.get("share_distribution")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["BatchSchedulingPolicyFairSharePolicyShareDistribution"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BatchSchedulingPolicyFairSharePolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BatchSchedulingPolicyFairSharePolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.batchSchedulingPolicy.BatchSchedulingPolicyFairSharePolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fb9cb5de41588e77fa1e9c3b26fa8c81ca690202ef2d86962ff617321e935560)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putShareDistribution")
    def put_share_distribution(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["BatchSchedulingPolicyFairSharePolicyShareDistribution", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06f0604f69b39a82e7c42a6e35c4c152b208261aa6da89e064d038908af02c34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putShareDistribution", [value]))

    @jsii.member(jsii_name="resetComputeReservation")
    def reset_compute_reservation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComputeReservation", []))

    @jsii.member(jsii_name="resetShareDecaySeconds")
    def reset_share_decay_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShareDecaySeconds", []))

    @jsii.member(jsii_name="resetShareDistribution")
    def reset_share_distribution(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShareDistribution", []))

    @builtins.property
    @jsii.member(jsii_name="shareDistribution")
    def share_distribution(
        self,
    ) -> "BatchSchedulingPolicyFairSharePolicyShareDistributionList":
        return typing.cast("BatchSchedulingPolicyFairSharePolicyShareDistributionList", jsii.get(self, "shareDistribution"))

    @builtins.property
    @jsii.member(jsii_name="computeReservationInput")
    def compute_reservation_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "computeReservationInput"))

    @builtins.property
    @jsii.member(jsii_name="shareDecaySecondsInput")
    def share_decay_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "shareDecaySecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="shareDistributionInput")
    def share_distribution_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["BatchSchedulingPolicyFairSharePolicyShareDistribution"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["BatchSchedulingPolicyFairSharePolicyShareDistribution"]]], jsii.get(self, "shareDistributionInput"))

    @builtins.property
    @jsii.member(jsii_name="computeReservation")
    def compute_reservation(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "computeReservation"))

    @compute_reservation.setter
    def compute_reservation(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__acbeb9f504cfa0158f1425dfe838a6a64dc27119ef1ba3a8a6b0da7b71912732)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "computeReservation", value)

    @builtins.property
    @jsii.member(jsii_name="shareDecaySeconds")
    def share_decay_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "shareDecaySeconds"))

    @share_decay_seconds.setter
    def share_decay_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__677fd7681558a850ecfabbcda21e9ae1f2352930a7bade810ee13987aa4150e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shareDecaySeconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[BatchSchedulingPolicyFairSharePolicy]:
        return typing.cast(typing.Optional[BatchSchedulingPolicyFairSharePolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[BatchSchedulingPolicyFairSharePolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf0db97739014cbcde0fe6a63bbe9f79db2121fd167fb6d1e554b4f18b36a0b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.batchSchedulingPolicy.BatchSchedulingPolicyFairSharePolicyShareDistribution",
    jsii_struct_bases=[],
    name_mapping={
        "share_identifier": "shareIdentifier",
        "weight_factor": "weightFactor",
    },
)
class BatchSchedulingPolicyFairSharePolicyShareDistribution:
    def __init__(
        self,
        *,
        share_identifier: builtins.str,
        weight_factor: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param share_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_scheduling_policy#share_identifier BatchSchedulingPolicy#share_identifier}.
        :param weight_factor: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_scheduling_policy#weight_factor BatchSchedulingPolicy#weight_factor}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3bd787c3c037321c3161ab07e4bc6f9d85baf63e3d964c0d90137293c3ec8ef8)
            check_type(argname="argument share_identifier", value=share_identifier, expected_type=type_hints["share_identifier"])
            check_type(argname="argument weight_factor", value=weight_factor, expected_type=type_hints["weight_factor"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "share_identifier": share_identifier,
        }
        if weight_factor is not None:
            self._values["weight_factor"] = weight_factor

    @builtins.property
    def share_identifier(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_scheduling_policy#share_identifier BatchSchedulingPolicy#share_identifier}.'''
        result = self._values.get("share_identifier")
        assert result is not None, "Required property 'share_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def weight_factor(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_scheduling_policy#weight_factor BatchSchedulingPolicy#weight_factor}.'''
        result = self._values.get("weight_factor")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BatchSchedulingPolicyFairSharePolicyShareDistribution(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BatchSchedulingPolicyFairSharePolicyShareDistributionList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.batchSchedulingPolicy.BatchSchedulingPolicyFairSharePolicyShareDistributionList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__78111be4b3bfd6e20571f96316b45f5701a886a93d5a35d36148bb9888cebc26)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "BatchSchedulingPolicyFairSharePolicyShareDistributionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d80b3996075382c6f6013e96a29cfb91ac14dbe01b3f5e51d5ee9564a08470a3)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("BatchSchedulingPolicyFairSharePolicyShareDistributionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fcbb3e0fd4ade995e56212e74a17fb99e356526966baa9c9cb5ad13d0d7d07be)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a4a52ad0f3170504019be32ca0de11da20e9a7967bba7936049f6894d6e9deef)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6ede0c793e4a1ff91129dc671338e7e5c1b231d448acbb58c18b21586df8c8ca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[BatchSchedulingPolicyFairSharePolicyShareDistribution]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[BatchSchedulingPolicyFairSharePolicyShareDistribution]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[BatchSchedulingPolicyFairSharePolicyShareDistribution]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7172b4716f8992a7fc37eca4000962a8551b18f48f2a04a660b8475a4eec6e9e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class BatchSchedulingPolicyFairSharePolicyShareDistributionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.batchSchedulingPolicy.BatchSchedulingPolicyFairSharePolicyShareDistributionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d4397b870d4680f3102a504d085756a217efd74a47f161f26d34146505d39e5e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetWeightFactor")
    def reset_weight_factor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeightFactor", []))

    @builtins.property
    @jsii.member(jsii_name="shareIdentifierInput")
    def share_identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "shareIdentifierInput"))

    @builtins.property
    @jsii.member(jsii_name="weightFactorInput")
    def weight_factor_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "weightFactorInput"))

    @builtins.property
    @jsii.member(jsii_name="shareIdentifier")
    def share_identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "shareIdentifier"))

    @share_identifier.setter
    def share_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df3153985562db714a205fc879733212b2528562d86243dc808e5e558a34788c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shareIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="weightFactor")
    def weight_factor(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "weightFactor"))

    @weight_factor.setter
    def weight_factor(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2338c743dd835e4af2b43c6027a473b2496d3ef95b4a6c40670735ba96c68a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weightFactor", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[BatchSchedulingPolicyFairSharePolicyShareDistribution, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[BatchSchedulingPolicyFairSharePolicyShareDistribution, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[BatchSchedulingPolicyFairSharePolicyShareDistribution, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d277e905fe883b6697f078976cb4cbfde962adf20a464612bf8a4c2f67283c5b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "BatchSchedulingPolicy",
    "BatchSchedulingPolicyConfig",
    "BatchSchedulingPolicyFairSharePolicy",
    "BatchSchedulingPolicyFairSharePolicyOutputReference",
    "BatchSchedulingPolicyFairSharePolicyShareDistribution",
    "BatchSchedulingPolicyFairSharePolicyShareDistributionList",
    "BatchSchedulingPolicyFairSharePolicyShareDistributionOutputReference",
]

publication.publish()

def _typecheckingstub__c23181835eaee9da3b86dd1fb2bf063d8f36326c9885cc5bdad191d2274c8de2(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    fair_share_policy: typing.Optional[typing.Union[BatchSchedulingPolicyFairSharePolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__5d2eefd93c86b28cce38fc3de853893d444ebfd37f5d4c1572dc1ad90bab2f8b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cfe791332925806a1eca0249f8d25a2f858ef756bd3a78add71f1f3170bea08(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9216bcad1a32f691ab7d5ee189f935b05640beba76b83976bb955d15de3629e6(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__422aa5f9e3ba992357f02798fc665528f4c36af2b6b0eba7399030fba1a3b656(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1e3588e7680621dcb554196c931a1fd9e066617019ebbf134d9a9de4cac0de8(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    fair_share_policy: typing.Optional[typing.Union[BatchSchedulingPolicyFairSharePolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c192916655f4acb261809d98e8fcba2e323259c47c18b75d3d2f0d9cb9b71de(
    *,
    compute_reservation: typing.Optional[jsii.Number] = None,
    share_decay_seconds: typing.Optional[jsii.Number] = None,
    share_distribution: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[BatchSchedulingPolicyFairSharePolicyShareDistribution, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb9cb5de41588e77fa1e9c3b26fa8c81ca690202ef2d86962ff617321e935560(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06f0604f69b39a82e7c42a6e35c4c152b208261aa6da89e064d038908af02c34(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[BatchSchedulingPolicyFairSharePolicyShareDistribution, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acbeb9f504cfa0158f1425dfe838a6a64dc27119ef1ba3a8a6b0da7b71912732(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__677fd7681558a850ecfabbcda21e9ae1f2352930a7bade810ee13987aa4150e6(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf0db97739014cbcde0fe6a63bbe9f79db2121fd167fb6d1e554b4f18b36a0b5(
    value: typing.Optional[BatchSchedulingPolicyFairSharePolicy],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bd787c3c037321c3161ab07e4bc6f9d85baf63e3d964c0d90137293c3ec8ef8(
    *,
    share_identifier: builtins.str,
    weight_factor: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78111be4b3bfd6e20571f96316b45f5701a886a93d5a35d36148bb9888cebc26(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d80b3996075382c6f6013e96a29cfb91ac14dbe01b3f5e51d5ee9564a08470a3(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcbb3e0fd4ade995e56212e74a17fb99e356526966baa9c9cb5ad13d0d7d07be(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4a52ad0f3170504019be32ca0de11da20e9a7967bba7936049f6894d6e9deef(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ede0c793e4a1ff91129dc671338e7e5c1b231d448acbb58c18b21586df8c8ca(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7172b4716f8992a7fc37eca4000962a8551b18f48f2a04a660b8475a4eec6e9e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[BatchSchedulingPolicyFairSharePolicyShareDistribution]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4397b870d4680f3102a504d085756a217efd74a47f161f26d34146505d39e5e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df3153985562db714a205fc879733212b2528562d86243dc808e5e558a34788c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2338c743dd835e4af2b43c6027a473b2496d3ef95b4a6c40670735ba96c68a1(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d277e905fe883b6697f078976cb4cbfde962adf20a464612bf8a4c2f67283c5b(
    value: typing.Optional[typing.Union[BatchSchedulingPolicyFairSharePolicyShareDistribution, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
