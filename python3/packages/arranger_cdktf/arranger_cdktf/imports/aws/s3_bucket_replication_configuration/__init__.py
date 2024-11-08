'''
# `aws_s3_bucket_replication_configuration`

Refer to the Terraform Registory for docs: [`aws_s3_bucket_replication_configuration`](https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration).
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


class S3BucketReplicationConfigurationA(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketReplicationConfiguration.S3BucketReplicationConfigurationA",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration aws_s3_bucket_replication_configuration}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        bucket: builtins.str,
        role: builtins.str,
        rule: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["S3BucketReplicationConfigurationRule", typing.Dict[builtins.str, typing.Any]]]],
        id: typing.Optional[builtins.str] = None,
        token: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration aws_s3_bucket_replication_configuration} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#bucket S3BucketReplicationConfigurationA#bucket}.
        :param role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#role S3BucketReplicationConfigurationA#role}.
        :param rule: rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#rule S3BucketReplicationConfigurationA#rule}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#id S3BucketReplicationConfigurationA#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#token S3BucketReplicationConfigurationA#token}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a00ef44dbf5e747ff466d1e10eb2784cf26f076275ada3d6721ef1eeac27053d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = S3BucketReplicationConfigurationAConfig(
            bucket=bucket,
            role=role,
            rule=rule,
            id=id,
            token=token,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putRule")
    def put_rule(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["S3BucketReplicationConfigurationRule", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74c8cdc0b0d06b4471ae0d7a45069dbda0d7f1344f6b65e05b71a5b93c6154b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRule", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetToken")
    def reset_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetToken", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> "S3BucketReplicationConfigurationRuleList":
        return typing.cast("S3BucketReplicationConfigurationRuleList", jsii.get(self, "rule"))

    @builtins.property
    @jsii.member(jsii_name="bucketInput")
    def bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="roleInput")
    def role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketReplicationConfigurationRule"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketReplicationConfigurationRule"]]], jsii.get(self, "ruleInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenInput")
    def token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenInput"))

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24ff2de8b3d6c594ec1b493980e7563f967a8774349dee14e338c49abedc3a86)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucket", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb6feb5a4177e6fb68c4e8570982b09ced1db991d1c2cca8a44cdaf5c39d296a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "role"))

    @role.setter
    def role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c23a9e111b0f6639579bf50e1495a171d131b4635ea551969391bfa701718fb6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "role", value)

    @builtins.property
    @jsii.member(jsii_name="token")
    def token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "token"))

    @token.setter
    def token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e692b9da2b9d1aaae8066674a83524b02b6d1008a0529eed18e340c22ab34855)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "token", value)


@jsii.data_type(
    jsii_type="aws.s3BucketReplicationConfiguration.S3BucketReplicationConfigurationAConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "bucket": "bucket",
        "role": "role",
        "rule": "rule",
        "id": "id",
        "token": "token",
    },
)
class S3BucketReplicationConfigurationAConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        bucket: builtins.str,
        role: builtins.str,
        rule: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["S3BucketReplicationConfigurationRule", typing.Dict[builtins.str, typing.Any]]]],
        id: typing.Optional[builtins.str] = None,
        token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#bucket S3BucketReplicationConfigurationA#bucket}.
        :param role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#role S3BucketReplicationConfigurationA#role}.
        :param rule: rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#rule S3BucketReplicationConfigurationA#rule}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#id S3BucketReplicationConfigurationA#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#token S3BucketReplicationConfigurationA#token}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24888e56a25a7324b58bb3b3d727793424f09925d02343b6eec175e101be1f5f)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument token", value=token, expected_type=type_hints["token"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket": bucket,
            "role": role,
            "rule": rule,
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
        if token is not None:
            self._values["token"] = token

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
    def bucket(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#bucket S3BucketReplicationConfigurationA#bucket}.'''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#role S3BucketReplicationConfigurationA#role}.'''
        result = self._values.get("role")
        assert result is not None, "Required property 'role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketReplicationConfigurationRule"]]:
        '''rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#rule S3BucketReplicationConfigurationA#rule}
        '''
        result = self._values.get("rule")
        assert result is not None, "Required property 'rule' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketReplicationConfigurationRule"]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#id S3BucketReplicationConfigurationA#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#token S3BucketReplicationConfigurationA#token}.'''
        result = self._values.get("token")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketReplicationConfigurationAConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.s3BucketReplicationConfiguration.S3BucketReplicationConfigurationRule",
    jsii_struct_bases=[],
    name_mapping={
        "destination": "destination",
        "status": "status",
        "delete_marker_replication": "deleteMarkerReplication",
        "existing_object_replication": "existingObjectReplication",
        "filter": "filter",
        "id": "id",
        "prefix": "prefix",
        "priority": "priority",
        "source_selection_criteria": "sourceSelectionCriteria",
    },
)
class S3BucketReplicationConfigurationRule:
    def __init__(
        self,
        *,
        destination: typing.Union["S3BucketReplicationConfigurationRuleDestination", typing.Dict[builtins.str, typing.Any]],
        status: builtins.str,
        delete_marker_replication: typing.Optional[typing.Union["S3BucketReplicationConfigurationRuleDeleteMarkerReplication", typing.Dict[builtins.str, typing.Any]]] = None,
        existing_object_replication: typing.Optional[typing.Union["S3BucketReplicationConfigurationRuleExistingObjectReplication", typing.Dict[builtins.str, typing.Any]]] = None,
        filter: typing.Optional[typing.Union["S3BucketReplicationConfigurationRuleFilter", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        priority: typing.Optional[jsii.Number] = None,
        source_selection_criteria: typing.Optional[typing.Union["S3BucketReplicationConfigurationRuleSourceSelectionCriteria", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param destination: destination block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#destination S3BucketReplicationConfigurationA#destination}
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#status S3BucketReplicationConfigurationA#status}.
        :param delete_marker_replication: delete_marker_replication block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#delete_marker_replication S3BucketReplicationConfigurationA#delete_marker_replication}
        :param existing_object_replication: existing_object_replication block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#existing_object_replication S3BucketReplicationConfigurationA#existing_object_replication}
        :param filter: filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#filter S3BucketReplicationConfigurationA#filter}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#id S3BucketReplicationConfigurationA#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#prefix S3BucketReplicationConfigurationA#prefix}.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#priority S3BucketReplicationConfigurationA#priority}.
        :param source_selection_criteria: source_selection_criteria block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#source_selection_criteria S3BucketReplicationConfigurationA#source_selection_criteria}
        '''
        if isinstance(destination, dict):
            destination = S3BucketReplicationConfigurationRuleDestination(**destination)
        if isinstance(delete_marker_replication, dict):
            delete_marker_replication = S3BucketReplicationConfigurationRuleDeleteMarkerReplication(**delete_marker_replication)
        if isinstance(existing_object_replication, dict):
            existing_object_replication = S3BucketReplicationConfigurationRuleExistingObjectReplication(**existing_object_replication)
        if isinstance(filter, dict):
            filter = S3BucketReplicationConfigurationRuleFilter(**filter)
        if isinstance(source_selection_criteria, dict):
            source_selection_criteria = S3BucketReplicationConfigurationRuleSourceSelectionCriteria(**source_selection_criteria)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39591452702cf49409a1719c3157143dfe7803e6e44ebf12bf841054dd860c17)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument delete_marker_replication", value=delete_marker_replication, expected_type=type_hints["delete_marker_replication"])
            check_type(argname="argument existing_object_replication", value=existing_object_replication, expected_type=type_hints["existing_object_replication"])
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument source_selection_criteria", value=source_selection_criteria, expected_type=type_hints["source_selection_criteria"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination": destination,
            "status": status,
        }
        if delete_marker_replication is not None:
            self._values["delete_marker_replication"] = delete_marker_replication
        if existing_object_replication is not None:
            self._values["existing_object_replication"] = existing_object_replication
        if filter is not None:
            self._values["filter"] = filter
        if id is not None:
            self._values["id"] = id
        if prefix is not None:
            self._values["prefix"] = prefix
        if priority is not None:
            self._values["priority"] = priority
        if source_selection_criteria is not None:
            self._values["source_selection_criteria"] = source_selection_criteria

    @builtins.property
    def destination(self) -> "S3BucketReplicationConfigurationRuleDestination":
        '''destination block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#destination S3BucketReplicationConfigurationA#destination}
        '''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast("S3BucketReplicationConfigurationRuleDestination", result)

    @builtins.property
    def status(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#status S3BucketReplicationConfigurationA#status}.'''
        result = self._values.get("status")
        assert result is not None, "Required property 'status' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def delete_marker_replication(
        self,
    ) -> typing.Optional["S3BucketReplicationConfigurationRuleDeleteMarkerReplication"]:
        '''delete_marker_replication block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#delete_marker_replication S3BucketReplicationConfigurationA#delete_marker_replication}
        '''
        result = self._values.get("delete_marker_replication")
        return typing.cast(typing.Optional["S3BucketReplicationConfigurationRuleDeleteMarkerReplication"], result)

    @builtins.property
    def existing_object_replication(
        self,
    ) -> typing.Optional["S3BucketReplicationConfigurationRuleExistingObjectReplication"]:
        '''existing_object_replication block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#existing_object_replication S3BucketReplicationConfigurationA#existing_object_replication}
        '''
        result = self._values.get("existing_object_replication")
        return typing.cast(typing.Optional["S3BucketReplicationConfigurationRuleExistingObjectReplication"], result)

    @builtins.property
    def filter(self) -> typing.Optional["S3BucketReplicationConfigurationRuleFilter"]:
        '''filter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#filter S3BucketReplicationConfigurationA#filter}
        '''
        result = self._values.get("filter")
        return typing.cast(typing.Optional["S3BucketReplicationConfigurationRuleFilter"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#id S3BucketReplicationConfigurationA#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#prefix S3BucketReplicationConfigurationA#prefix}.'''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#priority S3BucketReplicationConfigurationA#priority}.'''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def source_selection_criteria(
        self,
    ) -> typing.Optional["S3BucketReplicationConfigurationRuleSourceSelectionCriteria"]:
        '''source_selection_criteria block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#source_selection_criteria S3BucketReplicationConfigurationA#source_selection_criteria}
        '''
        result = self._values.get("source_selection_criteria")
        return typing.cast(typing.Optional["S3BucketReplicationConfigurationRuleSourceSelectionCriteria"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketReplicationConfigurationRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.s3BucketReplicationConfiguration.S3BucketReplicationConfigurationRuleDeleteMarkerReplication",
    jsii_struct_bases=[],
    name_mapping={"status": "status"},
)
class S3BucketReplicationConfigurationRuleDeleteMarkerReplication:
    def __init__(self, *, status: builtins.str) -> None:
        '''
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#status S3BucketReplicationConfigurationA#status}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a34bc6800b9efd934610f5d18213de007d98421c7ab0f9a2528f0f60a178d79f)
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "status": status,
        }

    @builtins.property
    def status(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#status S3BucketReplicationConfigurationA#status}.'''
        result = self._values.get("status")
        assert result is not None, "Required property 'status' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketReplicationConfigurationRuleDeleteMarkerReplication(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketReplicationConfigurationRuleDeleteMarkerReplicationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketReplicationConfiguration.S3BucketReplicationConfigurationRuleDeleteMarkerReplicationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a5af452fa57fc468533530db3a772be1a91aadd9785ac7ddf62c220b70dc408c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99f5de09097132dd587e03aa6b10970dd265f0b41e2b9cff9311b7a3efc79645)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketReplicationConfigurationRuleDeleteMarkerReplication]:
        return typing.cast(typing.Optional[S3BucketReplicationConfigurationRuleDeleteMarkerReplication], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketReplicationConfigurationRuleDeleteMarkerReplication],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__591b05213c3f9f6869720ba13b594e784ebb77a00005c499544392f84b5bcc92)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3BucketReplicationConfiguration.S3BucketReplicationConfigurationRuleDestination",
    jsii_struct_bases=[],
    name_mapping={
        "bucket": "bucket",
        "access_control_translation": "accessControlTranslation",
        "account": "account",
        "encryption_configuration": "encryptionConfiguration",
        "metrics": "metrics",
        "replication_time": "replicationTime",
        "storage_class": "storageClass",
    },
)
class S3BucketReplicationConfigurationRuleDestination:
    def __init__(
        self,
        *,
        bucket: builtins.str,
        access_control_translation: typing.Optional[typing.Union["S3BucketReplicationConfigurationRuleDestinationAccessControlTranslation", typing.Dict[builtins.str, typing.Any]]] = None,
        account: typing.Optional[builtins.str] = None,
        encryption_configuration: typing.Optional[typing.Union["S3BucketReplicationConfigurationRuleDestinationEncryptionConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        metrics: typing.Optional[typing.Union["S3BucketReplicationConfigurationRuleDestinationMetrics", typing.Dict[builtins.str, typing.Any]]] = None,
        replication_time: typing.Optional[typing.Union["S3BucketReplicationConfigurationRuleDestinationReplicationTime", typing.Dict[builtins.str, typing.Any]]] = None,
        storage_class: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#bucket S3BucketReplicationConfigurationA#bucket}.
        :param access_control_translation: access_control_translation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#access_control_translation S3BucketReplicationConfigurationA#access_control_translation}
        :param account: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#account S3BucketReplicationConfigurationA#account}.
        :param encryption_configuration: encryption_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#encryption_configuration S3BucketReplicationConfigurationA#encryption_configuration}
        :param metrics: metrics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#metrics S3BucketReplicationConfigurationA#metrics}
        :param replication_time: replication_time block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#replication_time S3BucketReplicationConfigurationA#replication_time}
        :param storage_class: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#storage_class S3BucketReplicationConfigurationA#storage_class}.
        '''
        if isinstance(access_control_translation, dict):
            access_control_translation = S3BucketReplicationConfigurationRuleDestinationAccessControlTranslation(**access_control_translation)
        if isinstance(encryption_configuration, dict):
            encryption_configuration = S3BucketReplicationConfigurationRuleDestinationEncryptionConfiguration(**encryption_configuration)
        if isinstance(metrics, dict):
            metrics = S3BucketReplicationConfigurationRuleDestinationMetrics(**metrics)
        if isinstance(replication_time, dict):
            replication_time = S3BucketReplicationConfigurationRuleDestinationReplicationTime(**replication_time)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55c565986b591cc6823d994fd950b1f4e48ccd93476f2fa6630e3aac91d96fdd)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument access_control_translation", value=access_control_translation, expected_type=type_hints["access_control_translation"])
            check_type(argname="argument account", value=account, expected_type=type_hints["account"])
            check_type(argname="argument encryption_configuration", value=encryption_configuration, expected_type=type_hints["encryption_configuration"])
            check_type(argname="argument metrics", value=metrics, expected_type=type_hints["metrics"])
            check_type(argname="argument replication_time", value=replication_time, expected_type=type_hints["replication_time"])
            check_type(argname="argument storage_class", value=storage_class, expected_type=type_hints["storage_class"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket": bucket,
        }
        if access_control_translation is not None:
            self._values["access_control_translation"] = access_control_translation
        if account is not None:
            self._values["account"] = account
        if encryption_configuration is not None:
            self._values["encryption_configuration"] = encryption_configuration
        if metrics is not None:
            self._values["metrics"] = metrics
        if replication_time is not None:
            self._values["replication_time"] = replication_time
        if storage_class is not None:
            self._values["storage_class"] = storage_class

    @builtins.property
    def bucket(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#bucket S3BucketReplicationConfigurationA#bucket}.'''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_control_translation(
        self,
    ) -> typing.Optional["S3BucketReplicationConfigurationRuleDestinationAccessControlTranslation"]:
        '''access_control_translation block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#access_control_translation S3BucketReplicationConfigurationA#access_control_translation}
        '''
        result = self._values.get("access_control_translation")
        return typing.cast(typing.Optional["S3BucketReplicationConfigurationRuleDestinationAccessControlTranslation"], result)

    @builtins.property
    def account(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#account S3BucketReplicationConfigurationA#account}.'''
        result = self._values.get("account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_configuration(
        self,
    ) -> typing.Optional["S3BucketReplicationConfigurationRuleDestinationEncryptionConfiguration"]:
        '''encryption_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#encryption_configuration S3BucketReplicationConfigurationA#encryption_configuration}
        '''
        result = self._values.get("encryption_configuration")
        return typing.cast(typing.Optional["S3BucketReplicationConfigurationRuleDestinationEncryptionConfiguration"], result)

    @builtins.property
    def metrics(
        self,
    ) -> typing.Optional["S3BucketReplicationConfigurationRuleDestinationMetrics"]:
        '''metrics block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#metrics S3BucketReplicationConfigurationA#metrics}
        '''
        result = self._values.get("metrics")
        return typing.cast(typing.Optional["S3BucketReplicationConfigurationRuleDestinationMetrics"], result)

    @builtins.property
    def replication_time(
        self,
    ) -> typing.Optional["S3BucketReplicationConfigurationRuleDestinationReplicationTime"]:
        '''replication_time block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#replication_time S3BucketReplicationConfigurationA#replication_time}
        '''
        result = self._values.get("replication_time")
        return typing.cast(typing.Optional["S3BucketReplicationConfigurationRuleDestinationReplicationTime"], result)

    @builtins.property
    def storage_class(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#storage_class S3BucketReplicationConfigurationA#storage_class}.'''
        result = self._values.get("storage_class")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketReplicationConfigurationRuleDestination(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.s3BucketReplicationConfiguration.S3BucketReplicationConfigurationRuleDestinationAccessControlTranslation",
    jsii_struct_bases=[],
    name_mapping={"owner": "owner"},
)
class S3BucketReplicationConfigurationRuleDestinationAccessControlTranslation:
    def __init__(self, *, owner: builtins.str) -> None:
        '''
        :param owner: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#owner S3BucketReplicationConfigurationA#owner}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc9c2053106a166f37068fc45d444968ae4bf04bc1a0b51119f848126c7836e9)
            check_type(argname="argument owner", value=owner, expected_type=type_hints["owner"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "owner": owner,
        }

    @builtins.property
    def owner(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#owner S3BucketReplicationConfigurationA#owner}.'''
        result = self._values.get("owner")
        assert result is not None, "Required property 'owner' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketReplicationConfigurationRuleDestinationAccessControlTranslation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketReplicationConfigurationRuleDestinationAccessControlTranslationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketReplicationConfiguration.S3BucketReplicationConfigurationRuleDestinationAccessControlTranslationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d9d5b344773f8360cc549ac261d22dbfacb8f4cd5189cab4d9364e9b2f60a808)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="ownerInput")
    def owner_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ownerInput"))

    @builtins.property
    @jsii.member(jsii_name="owner")
    def owner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "owner"))

    @owner.setter
    def owner(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f652c54c33735c267bff6f321b572d3fbee0c42f8c70144a32842040acaedb73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "owner", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketReplicationConfigurationRuleDestinationAccessControlTranslation]:
        return typing.cast(typing.Optional[S3BucketReplicationConfigurationRuleDestinationAccessControlTranslation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketReplicationConfigurationRuleDestinationAccessControlTranslation],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a508e532e3f5b854c002e272ecda63040aa154131d19ead8b3f4b04ab3627f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3BucketReplicationConfiguration.S3BucketReplicationConfigurationRuleDestinationEncryptionConfiguration",
    jsii_struct_bases=[],
    name_mapping={"replica_kms_key_id": "replicaKmsKeyId"},
)
class S3BucketReplicationConfigurationRuleDestinationEncryptionConfiguration:
    def __init__(self, *, replica_kms_key_id: builtins.str) -> None:
        '''
        :param replica_kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#replica_kms_key_id S3BucketReplicationConfigurationA#replica_kms_key_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd5bf09cb38b4fa857ad57db1c6723f795d1595b8893595de96aa019958dfcca)
            check_type(argname="argument replica_kms_key_id", value=replica_kms_key_id, expected_type=type_hints["replica_kms_key_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "replica_kms_key_id": replica_kms_key_id,
        }

    @builtins.property
    def replica_kms_key_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#replica_kms_key_id S3BucketReplicationConfigurationA#replica_kms_key_id}.'''
        result = self._values.get("replica_kms_key_id")
        assert result is not None, "Required property 'replica_kms_key_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketReplicationConfigurationRuleDestinationEncryptionConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketReplicationConfigurationRuleDestinationEncryptionConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketReplicationConfiguration.S3BucketReplicationConfigurationRuleDestinationEncryptionConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__586c0b2b1bca9a9a30a4b72fbf873b6bf1babb9fdac6d8d2fc841c9c6f42b566)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="replicaKmsKeyIdInput")
    def replica_kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "replicaKmsKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="replicaKmsKeyId")
    def replica_kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "replicaKmsKeyId"))

    @replica_kms_key_id.setter
    def replica_kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b4b587e04c987724d22c227a017c6bbc48182a1216ceaa5d042ad82272567b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicaKmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketReplicationConfigurationRuleDestinationEncryptionConfiguration]:
        return typing.cast(typing.Optional[S3BucketReplicationConfigurationRuleDestinationEncryptionConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketReplicationConfigurationRuleDestinationEncryptionConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__103e5a77d1ed7d3d9de217f38ca9b3d70f7d6f1859c26f53e638f9dec8449397)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3BucketReplicationConfiguration.S3BucketReplicationConfigurationRuleDestinationMetrics",
    jsii_struct_bases=[],
    name_mapping={"status": "status", "event_threshold": "eventThreshold"},
)
class S3BucketReplicationConfigurationRuleDestinationMetrics:
    def __init__(
        self,
        *,
        status: builtins.str,
        event_threshold: typing.Optional[typing.Union["S3BucketReplicationConfigurationRuleDestinationMetricsEventThreshold", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#status S3BucketReplicationConfigurationA#status}.
        :param event_threshold: event_threshold block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#event_threshold S3BucketReplicationConfigurationA#event_threshold}
        '''
        if isinstance(event_threshold, dict):
            event_threshold = S3BucketReplicationConfigurationRuleDestinationMetricsEventThreshold(**event_threshold)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb71a698938cfdf7d2fb4074db3675108c38c7377b6d67bdcfa7e9fb23e822c3)
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument event_threshold", value=event_threshold, expected_type=type_hints["event_threshold"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "status": status,
        }
        if event_threshold is not None:
            self._values["event_threshold"] = event_threshold

    @builtins.property
    def status(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#status S3BucketReplicationConfigurationA#status}.'''
        result = self._values.get("status")
        assert result is not None, "Required property 'status' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def event_threshold(
        self,
    ) -> typing.Optional["S3BucketReplicationConfigurationRuleDestinationMetricsEventThreshold"]:
        '''event_threshold block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#event_threshold S3BucketReplicationConfigurationA#event_threshold}
        '''
        result = self._values.get("event_threshold")
        return typing.cast(typing.Optional["S3BucketReplicationConfigurationRuleDestinationMetricsEventThreshold"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketReplicationConfigurationRuleDestinationMetrics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.s3BucketReplicationConfiguration.S3BucketReplicationConfigurationRuleDestinationMetricsEventThreshold",
    jsii_struct_bases=[],
    name_mapping={"minutes": "minutes"},
)
class S3BucketReplicationConfigurationRuleDestinationMetricsEventThreshold:
    def __init__(self, *, minutes: jsii.Number) -> None:
        '''
        :param minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#minutes S3BucketReplicationConfigurationA#minutes}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b3d424cd6de03e3ccb77dbb5c833e3d353d972a38f883fbbae5c47eeb64417e)
            check_type(argname="argument minutes", value=minutes, expected_type=type_hints["minutes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "minutes": minutes,
        }

    @builtins.property
    def minutes(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#minutes S3BucketReplicationConfigurationA#minutes}.'''
        result = self._values.get("minutes")
        assert result is not None, "Required property 'minutes' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketReplicationConfigurationRuleDestinationMetricsEventThreshold(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketReplicationConfigurationRuleDestinationMetricsEventThresholdOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketReplicationConfiguration.S3BucketReplicationConfigurationRuleDestinationMetricsEventThresholdOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0aa2f11ecf9238c70366e8f9799de64333a0ee2e792da46b3257993abefcdec6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="minutesInput")
    def minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minutesInput"))

    @builtins.property
    @jsii.member(jsii_name="minutes")
    def minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minutes"))

    @minutes.setter
    def minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63e1b31d5e65a0a4f85475cee63d7f07b170c49a68dcc5551e97c8b320b01030)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minutes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketReplicationConfigurationRuleDestinationMetricsEventThreshold]:
        return typing.cast(typing.Optional[S3BucketReplicationConfigurationRuleDestinationMetricsEventThreshold], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketReplicationConfigurationRuleDestinationMetricsEventThreshold],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f3f2325d4219c867872d7301cc713f170da1a4a72531ef580566f0a69ff4543)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3BucketReplicationConfigurationRuleDestinationMetricsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketReplicationConfiguration.S3BucketReplicationConfigurationRuleDestinationMetricsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__416166aa49964c253c9cbe5e18cdb09fb5453eb3928e7daf439eabd1ae4dc9cb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putEventThreshold")
    def put_event_threshold(self, *, minutes: jsii.Number) -> None:
        '''
        :param minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#minutes S3BucketReplicationConfigurationA#minutes}.
        '''
        value = S3BucketReplicationConfigurationRuleDestinationMetricsEventThreshold(
            minutes=minutes
        )

        return typing.cast(None, jsii.invoke(self, "putEventThreshold", [value]))

    @jsii.member(jsii_name="resetEventThreshold")
    def reset_event_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventThreshold", []))

    @builtins.property
    @jsii.member(jsii_name="eventThreshold")
    def event_threshold(
        self,
    ) -> S3BucketReplicationConfigurationRuleDestinationMetricsEventThresholdOutputReference:
        return typing.cast(S3BucketReplicationConfigurationRuleDestinationMetricsEventThresholdOutputReference, jsii.get(self, "eventThreshold"))

    @builtins.property
    @jsii.member(jsii_name="eventThresholdInput")
    def event_threshold_input(
        self,
    ) -> typing.Optional[S3BucketReplicationConfigurationRuleDestinationMetricsEventThreshold]:
        return typing.cast(typing.Optional[S3BucketReplicationConfigurationRuleDestinationMetricsEventThreshold], jsii.get(self, "eventThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e127956bcbdc3a3f30fc3104194f0cff53786984906dc56951aaf2e970ff8487)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketReplicationConfigurationRuleDestinationMetrics]:
        return typing.cast(typing.Optional[S3BucketReplicationConfigurationRuleDestinationMetrics], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketReplicationConfigurationRuleDestinationMetrics],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb842eb6e555aa9af2198c58e7efb2322ecfcdc32abf537ac7a45017dce30d66)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3BucketReplicationConfigurationRuleDestinationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketReplicationConfiguration.S3BucketReplicationConfigurationRuleDestinationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bd0c4a9f0dcf8601d14513712d695e213c42cb7d9ddfb04927a3ecf59fa09bc4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAccessControlTranslation")
    def put_access_control_translation(self, *, owner: builtins.str) -> None:
        '''
        :param owner: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#owner S3BucketReplicationConfigurationA#owner}.
        '''
        value = S3BucketReplicationConfigurationRuleDestinationAccessControlTranslation(
            owner=owner
        )

        return typing.cast(None, jsii.invoke(self, "putAccessControlTranslation", [value]))

    @jsii.member(jsii_name="putEncryptionConfiguration")
    def put_encryption_configuration(self, *, replica_kms_key_id: builtins.str) -> None:
        '''
        :param replica_kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#replica_kms_key_id S3BucketReplicationConfigurationA#replica_kms_key_id}.
        '''
        value = S3BucketReplicationConfigurationRuleDestinationEncryptionConfiguration(
            replica_kms_key_id=replica_kms_key_id
        )

        return typing.cast(None, jsii.invoke(self, "putEncryptionConfiguration", [value]))

    @jsii.member(jsii_name="putMetrics")
    def put_metrics(
        self,
        *,
        status: builtins.str,
        event_threshold: typing.Optional[typing.Union[S3BucketReplicationConfigurationRuleDestinationMetricsEventThreshold, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#status S3BucketReplicationConfigurationA#status}.
        :param event_threshold: event_threshold block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#event_threshold S3BucketReplicationConfigurationA#event_threshold}
        '''
        value = S3BucketReplicationConfigurationRuleDestinationMetrics(
            status=status, event_threshold=event_threshold
        )

        return typing.cast(None, jsii.invoke(self, "putMetrics", [value]))

    @jsii.member(jsii_name="putReplicationTime")
    def put_replication_time(
        self,
        *,
        status: builtins.str,
        time: typing.Union["S3BucketReplicationConfigurationRuleDestinationReplicationTimeTime", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#status S3BucketReplicationConfigurationA#status}.
        :param time: time block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#time S3BucketReplicationConfigurationA#time}
        '''
        value = S3BucketReplicationConfigurationRuleDestinationReplicationTime(
            status=status, time=time
        )

        return typing.cast(None, jsii.invoke(self, "putReplicationTime", [value]))

    @jsii.member(jsii_name="resetAccessControlTranslation")
    def reset_access_control_translation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessControlTranslation", []))

    @jsii.member(jsii_name="resetAccount")
    def reset_account(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccount", []))

    @jsii.member(jsii_name="resetEncryptionConfiguration")
    def reset_encryption_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionConfiguration", []))

    @jsii.member(jsii_name="resetMetrics")
    def reset_metrics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetrics", []))

    @jsii.member(jsii_name="resetReplicationTime")
    def reset_replication_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReplicationTime", []))

    @jsii.member(jsii_name="resetStorageClass")
    def reset_storage_class(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageClass", []))

    @builtins.property
    @jsii.member(jsii_name="accessControlTranslation")
    def access_control_translation(
        self,
    ) -> S3BucketReplicationConfigurationRuleDestinationAccessControlTranslationOutputReference:
        return typing.cast(S3BucketReplicationConfigurationRuleDestinationAccessControlTranslationOutputReference, jsii.get(self, "accessControlTranslation"))

    @builtins.property
    @jsii.member(jsii_name="encryptionConfiguration")
    def encryption_configuration(
        self,
    ) -> S3BucketReplicationConfigurationRuleDestinationEncryptionConfigurationOutputReference:
        return typing.cast(S3BucketReplicationConfigurationRuleDestinationEncryptionConfigurationOutputReference, jsii.get(self, "encryptionConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="metrics")
    def metrics(
        self,
    ) -> S3BucketReplicationConfigurationRuleDestinationMetricsOutputReference:
        return typing.cast(S3BucketReplicationConfigurationRuleDestinationMetricsOutputReference, jsii.get(self, "metrics"))

    @builtins.property
    @jsii.member(jsii_name="replicationTime")
    def replication_time(
        self,
    ) -> "S3BucketReplicationConfigurationRuleDestinationReplicationTimeOutputReference":
        return typing.cast("S3BucketReplicationConfigurationRuleDestinationReplicationTimeOutputReference", jsii.get(self, "replicationTime"))

    @builtins.property
    @jsii.member(jsii_name="accessControlTranslationInput")
    def access_control_translation_input(
        self,
    ) -> typing.Optional[S3BucketReplicationConfigurationRuleDestinationAccessControlTranslation]:
        return typing.cast(typing.Optional[S3BucketReplicationConfigurationRuleDestinationAccessControlTranslation], jsii.get(self, "accessControlTranslationInput"))

    @builtins.property
    @jsii.member(jsii_name="accountInput")
    def account_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketInput")
    def bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionConfigurationInput")
    def encryption_configuration_input(
        self,
    ) -> typing.Optional[S3BucketReplicationConfigurationRuleDestinationEncryptionConfiguration]:
        return typing.cast(typing.Optional[S3BucketReplicationConfigurationRuleDestinationEncryptionConfiguration], jsii.get(self, "encryptionConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsInput")
    def metrics_input(
        self,
    ) -> typing.Optional[S3BucketReplicationConfigurationRuleDestinationMetrics]:
        return typing.cast(typing.Optional[S3BucketReplicationConfigurationRuleDestinationMetrics], jsii.get(self, "metricsInput"))

    @builtins.property
    @jsii.member(jsii_name="replicationTimeInput")
    def replication_time_input(
        self,
    ) -> typing.Optional["S3BucketReplicationConfigurationRuleDestinationReplicationTime"]:
        return typing.cast(typing.Optional["S3BucketReplicationConfigurationRuleDestinationReplicationTime"], jsii.get(self, "replicationTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="storageClassInput")
    def storage_class_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageClassInput"))

    @builtins.property
    @jsii.member(jsii_name="account")
    def account(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "account"))

    @account.setter
    def account(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__673aa2bb7f5050d96e9468ecfa98d8fb10b877d0edca49d2db8ca74ddfc65080)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "account", value)

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__945bc0805f34b312bc1c391d95bc7211ca803086e6215d6816d0e006a2279097)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucket", value)

    @builtins.property
    @jsii.member(jsii_name="storageClass")
    def storage_class(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageClass"))

    @storage_class.setter
    def storage_class(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8849da212accb7dd4da8c7c7e83f3fd42da2313791b111a376a58e483f4fa3e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageClass", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketReplicationConfigurationRuleDestination]:
        return typing.cast(typing.Optional[S3BucketReplicationConfigurationRuleDestination], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketReplicationConfigurationRuleDestination],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e2b61ab01ed535eedd02c2fe26856bf9cbada5a7ea49e223f4f8397ed6cb84e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3BucketReplicationConfiguration.S3BucketReplicationConfigurationRuleDestinationReplicationTime",
    jsii_struct_bases=[],
    name_mapping={"status": "status", "time": "time"},
)
class S3BucketReplicationConfigurationRuleDestinationReplicationTime:
    def __init__(
        self,
        *,
        status: builtins.str,
        time: typing.Union["S3BucketReplicationConfigurationRuleDestinationReplicationTimeTime", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#status S3BucketReplicationConfigurationA#status}.
        :param time: time block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#time S3BucketReplicationConfigurationA#time}
        '''
        if isinstance(time, dict):
            time = S3BucketReplicationConfigurationRuleDestinationReplicationTimeTime(**time)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__598fcf6f4b963de700a6b21b47f404d22c63e931f3a58c6f50dc2675074e3ae9)
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument time", value=time, expected_type=type_hints["time"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "status": status,
            "time": time,
        }

    @builtins.property
    def status(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#status S3BucketReplicationConfigurationA#status}.'''
        result = self._values.get("status")
        assert result is not None, "Required property 'status' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def time(
        self,
    ) -> "S3BucketReplicationConfigurationRuleDestinationReplicationTimeTime":
        '''time block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#time S3BucketReplicationConfigurationA#time}
        '''
        result = self._values.get("time")
        assert result is not None, "Required property 'time' is missing"
        return typing.cast("S3BucketReplicationConfigurationRuleDestinationReplicationTimeTime", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketReplicationConfigurationRuleDestinationReplicationTime(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketReplicationConfigurationRuleDestinationReplicationTimeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketReplicationConfiguration.S3BucketReplicationConfigurationRuleDestinationReplicationTimeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ece32e6d87dd9634dc54f3d0a052fa2f686faf85857c2ee2d2eddec8cd42a2ce)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putTime")
    def put_time(self, *, minutes: jsii.Number) -> None:
        '''
        :param minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#minutes S3BucketReplicationConfigurationA#minutes}.
        '''
        value = S3BucketReplicationConfigurationRuleDestinationReplicationTimeTime(
            minutes=minutes
        )

        return typing.cast(None, jsii.invoke(self, "putTime", [value]))

    @builtins.property
    @jsii.member(jsii_name="time")
    def time(
        self,
    ) -> "S3BucketReplicationConfigurationRuleDestinationReplicationTimeTimeOutputReference":
        return typing.cast("S3BucketReplicationConfigurationRuleDestinationReplicationTimeTimeOutputReference", jsii.get(self, "time"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="timeInput")
    def time_input(
        self,
    ) -> typing.Optional["S3BucketReplicationConfigurationRuleDestinationReplicationTimeTime"]:
        return typing.cast(typing.Optional["S3BucketReplicationConfigurationRuleDestinationReplicationTimeTime"], jsii.get(self, "timeInput"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d70c6cd88a31553d2e26cf5c67d638877778d58be7045c3126e2ea90549896e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketReplicationConfigurationRuleDestinationReplicationTime]:
        return typing.cast(typing.Optional[S3BucketReplicationConfigurationRuleDestinationReplicationTime], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketReplicationConfigurationRuleDestinationReplicationTime],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c35e834041961524df481e3921a59a2970410d3b7af883b8f3245367126a0f87)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3BucketReplicationConfiguration.S3BucketReplicationConfigurationRuleDestinationReplicationTimeTime",
    jsii_struct_bases=[],
    name_mapping={"minutes": "minutes"},
)
class S3BucketReplicationConfigurationRuleDestinationReplicationTimeTime:
    def __init__(self, *, minutes: jsii.Number) -> None:
        '''
        :param minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#minutes S3BucketReplicationConfigurationA#minutes}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2659bbbb9feb3bdf32205f77abc19268c4156d3dc51b120e07d7c96e5a7e959)
            check_type(argname="argument minutes", value=minutes, expected_type=type_hints["minutes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "minutes": minutes,
        }

    @builtins.property
    def minutes(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#minutes S3BucketReplicationConfigurationA#minutes}.'''
        result = self._values.get("minutes")
        assert result is not None, "Required property 'minutes' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketReplicationConfigurationRuleDestinationReplicationTimeTime(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketReplicationConfigurationRuleDestinationReplicationTimeTimeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketReplicationConfiguration.S3BucketReplicationConfigurationRuleDestinationReplicationTimeTimeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__51056b2b9430ead5d93f94c739ea41e3295549501833eba5c32fc5ff06a0abed)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="minutesInput")
    def minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minutesInput"))

    @builtins.property
    @jsii.member(jsii_name="minutes")
    def minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minutes"))

    @minutes.setter
    def minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb544014dfab2992f4a8ee67d22c71b06e11273f143547e3d027be77aae5eba6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minutes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketReplicationConfigurationRuleDestinationReplicationTimeTime]:
        return typing.cast(typing.Optional[S3BucketReplicationConfigurationRuleDestinationReplicationTimeTime], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketReplicationConfigurationRuleDestinationReplicationTimeTime],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3647e90c29321b2c3e3d9c07d5a6a8efddca0f38effaaf68e88c1604cb2c2268)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3BucketReplicationConfiguration.S3BucketReplicationConfigurationRuleExistingObjectReplication",
    jsii_struct_bases=[],
    name_mapping={"status": "status"},
)
class S3BucketReplicationConfigurationRuleExistingObjectReplication:
    def __init__(self, *, status: builtins.str) -> None:
        '''
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#status S3BucketReplicationConfigurationA#status}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b3ba417eb7e7a96c6662a7c8f23f42179c9a3429b9252945537ce2576eed61f)
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "status": status,
        }

    @builtins.property
    def status(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#status S3BucketReplicationConfigurationA#status}.'''
        result = self._values.get("status")
        assert result is not None, "Required property 'status' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketReplicationConfigurationRuleExistingObjectReplication(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketReplicationConfigurationRuleExistingObjectReplicationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketReplicationConfiguration.S3BucketReplicationConfigurationRuleExistingObjectReplicationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d2607b756636c4e35b5d3a7b8cb4d8ca8462be67a8a56c832cf04c82801be13f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fede01a2aae12d1d4aa545a53c24a0f12d3442430f40d8da7f4e6bb699de05b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketReplicationConfigurationRuleExistingObjectReplication]:
        return typing.cast(typing.Optional[S3BucketReplicationConfigurationRuleExistingObjectReplication], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketReplicationConfigurationRuleExistingObjectReplication],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46505493cd8193b2d2ef1d6571674be89cd4f42daa64567afc61a3104d91e7ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3BucketReplicationConfiguration.S3BucketReplicationConfigurationRuleFilter",
    jsii_struct_bases=[],
    name_mapping={"and_": "and", "prefix": "prefix", "tag": "tag"},
)
class S3BucketReplicationConfigurationRuleFilter:
    def __init__(
        self,
        *,
        and_: typing.Optional[typing.Union["S3BucketReplicationConfigurationRuleFilterAnd", typing.Dict[builtins.str, typing.Any]]] = None,
        prefix: typing.Optional[builtins.str] = None,
        tag: typing.Optional[typing.Union["S3BucketReplicationConfigurationRuleFilterTag", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param and_: and block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#and S3BucketReplicationConfigurationA#and}
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#prefix S3BucketReplicationConfigurationA#prefix}.
        :param tag: tag block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#tag S3BucketReplicationConfigurationA#tag}
        '''
        if isinstance(and_, dict):
            and_ = S3BucketReplicationConfigurationRuleFilterAnd(**and_)
        if isinstance(tag, dict):
            tag = S3BucketReplicationConfigurationRuleFilterTag(**tag)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93cdab7d3241644cf52386c164f70fbffaebf252c672e924808a4775e8c937ae)
            check_type(argname="argument and_", value=and_, expected_type=type_hints["and_"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            check_type(argname="argument tag", value=tag, expected_type=type_hints["tag"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if and_ is not None:
            self._values["and_"] = and_
        if prefix is not None:
            self._values["prefix"] = prefix
        if tag is not None:
            self._values["tag"] = tag

    @builtins.property
    def and_(self) -> typing.Optional["S3BucketReplicationConfigurationRuleFilterAnd"]:
        '''and block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#and S3BucketReplicationConfigurationA#and}
        '''
        result = self._values.get("and_")
        return typing.cast(typing.Optional["S3BucketReplicationConfigurationRuleFilterAnd"], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#prefix S3BucketReplicationConfigurationA#prefix}.'''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag(self) -> typing.Optional["S3BucketReplicationConfigurationRuleFilterTag"]:
        '''tag block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#tag S3BucketReplicationConfigurationA#tag}
        '''
        result = self._values.get("tag")
        return typing.cast(typing.Optional["S3BucketReplicationConfigurationRuleFilterTag"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketReplicationConfigurationRuleFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.s3BucketReplicationConfiguration.S3BucketReplicationConfigurationRuleFilterAnd",
    jsii_struct_bases=[],
    name_mapping={"prefix": "prefix", "tags": "tags"},
)
class S3BucketReplicationConfigurationRuleFilterAnd:
    def __init__(
        self,
        *,
        prefix: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#prefix S3BucketReplicationConfigurationA#prefix}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#tags S3BucketReplicationConfigurationA#tags}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77a59486ef083a51639ecb31e70cb0e7a74a0414d2f647f8df412c3163ee36db)
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if prefix is not None:
            self._values["prefix"] = prefix
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#prefix S3BucketReplicationConfigurationA#prefix}.'''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#tags S3BucketReplicationConfigurationA#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketReplicationConfigurationRuleFilterAnd(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketReplicationConfigurationRuleFilterAndOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketReplicationConfiguration.S3BucketReplicationConfigurationRuleFilterAndOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f9f705333deebdbd81c830d40f47330c235b9a297bf27479a6a890c0e87843a8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPrefix")
    def reset_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefix", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51cbaf57ac8fc1ef57a47c74a30db816d2adb5ece25975b8dd82bf77d433b8e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c4ff5c2c7aad2edaedea1d98d1ee19cb531da992d460ef2c508fd28803bce49)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketReplicationConfigurationRuleFilterAnd]:
        return typing.cast(typing.Optional[S3BucketReplicationConfigurationRuleFilterAnd], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketReplicationConfigurationRuleFilterAnd],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11480e2f3d211e38936d8b64eeb947a862d75a9144065c08955f8da0f5deaae0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3BucketReplicationConfigurationRuleFilterOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketReplicationConfiguration.S3BucketReplicationConfigurationRuleFilterOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__72823ab035c9b6ac0635b66abefb728896d4d8c1ee729581951924ff0ec94591)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAnd")
    def put_and(
        self,
        *,
        prefix: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#prefix S3BucketReplicationConfigurationA#prefix}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#tags S3BucketReplicationConfigurationA#tags}.
        '''
        value = S3BucketReplicationConfigurationRuleFilterAnd(prefix=prefix, tags=tags)

        return typing.cast(None, jsii.invoke(self, "putAnd", [value]))

    @jsii.member(jsii_name="putTag")
    def put_tag(self, *, key: builtins.str, value: builtins.str) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#key S3BucketReplicationConfigurationA#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#value S3BucketReplicationConfigurationA#value}.
        '''
        value_ = S3BucketReplicationConfigurationRuleFilterTag(key=key, value=value)

        return typing.cast(None, jsii.invoke(self, "putTag", [value_]))

    @jsii.member(jsii_name="resetAnd")
    def reset_and(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnd", []))

    @jsii.member(jsii_name="resetPrefix")
    def reset_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefix", []))

    @jsii.member(jsii_name="resetTag")
    def reset_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTag", []))

    @builtins.property
    @jsii.member(jsii_name="and")
    def and_(self) -> S3BucketReplicationConfigurationRuleFilterAndOutputReference:
        return typing.cast(S3BucketReplicationConfigurationRuleFilterAndOutputReference, jsii.get(self, "and"))

    @builtins.property
    @jsii.member(jsii_name="tag")
    def tag(self) -> "S3BucketReplicationConfigurationRuleFilterTagOutputReference":
        return typing.cast("S3BucketReplicationConfigurationRuleFilterTagOutputReference", jsii.get(self, "tag"))

    @builtins.property
    @jsii.member(jsii_name="andInput")
    def and_input(
        self,
    ) -> typing.Optional[S3BucketReplicationConfigurationRuleFilterAnd]:
        return typing.cast(typing.Optional[S3BucketReplicationConfigurationRuleFilterAnd], jsii.get(self, "andInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="tagInput")
    def tag_input(
        self,
    ) -> typing.Optional["S3BucketReplicationConfigurationRuleFilterTag"]:
        return typing.cast(typing.Optional["S3BucketReplicationConfigurationRuleFilterTag"], jsii.get(self, "tagInput"))

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d2445d1b987520f61fb0a045da12120ddee6c36b61c14af01ebe3c42c472f0b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketReplicationConfigurationRuleFilter]:
        return typing.cast(typing.Optional[S3BucketReplicationConfigurationRuleFilter], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketReplicationConfigurationRuleFilter],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30c46cbbf30b67997dcb710ab10e570dac919327f9c1f669360e142c67bd247a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3BucketReplicationConfiguration.S3BucketReplicationConfigurationRuleFilterTag",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class S3BucketReplicationConfigurationRuleFilterTag:
    def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#key S3BucketReplicationConfigurationA#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#value S3BucketReplicationConfigurationA#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__281315d5bc1ab7eefc73f194e708aea44349c61d95f58bd1087e89929e6ef5c7)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#key S3BucketReplicationConfigurationA#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#value S3BucketReplicationConfigurationA#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketReplicationConfigurationRuleFilterTag(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketReplicationConfigurationRuleFilterTagOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketReplicationConfiguration.S3BucketReplicationConfigurationRuleFilterTagOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f02d22c88cc6ea6690c78255776e3fca35875f0b3e40c1d3ead3d13090c31074)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

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
            type_hints = typing.get_type_hints(_typecheckingstub__b12417c0be2e8af1b71724f9576b7a0731e6f06c772072e165ffe28a0175b500)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6470bcdc0086efd3cfa21fe35f7e2f595b04bc894cbdc61480f2ff9885f1b849)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketReplicationConfigurationRuleFilterTag]:
        return typing.cast(typing.Optional[S3BucketReplicationConfigurationRuleFilterTag], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketReplicationConfigurationRuleFilterTag],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42f09f43d177d2154734d5d3637df9f621409ac1345bf3e2953839ff125f5d0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3BucketReplicationConfigurationRuleList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketReplicationConfiguration.S3BucketReplicationConfigurationRuleList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__87a74b7c0ae2308b70e11c8a6670b9430f406f21d4a878142bbdc552ca11ba47)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "S3BucketReplicationConfigurationRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a1d695c84c22473cbd4b0eb66ebf180f5a0dfb20e58c5c2ec0f8dc870ee57db)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("S3BucketReplicationConfigurationRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a845b3d13671e306a16eeb39a4d4f254bb2ed3260475aaaf8ff4b1b1646a0f3f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__08e207068cad8f506469b5af0438e4e1aa99546a274c3fb56f9995b7c7aa51cb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__883aae6322aa460563ebce28441dd3af49849e2bbeaac03fe6189b75ecd2b4c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketReplicationConfigurationRule]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketReplicationConfigurationRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketReplicationConfigurationRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9b996f44bb9b4441c24fc4403ed80e958c5eba701293129e7d4d4184fbd83ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3BucketReplicationConfigurationRuleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketReplicationConfiguration.S3BucketReplicationConfigurationRuleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__924931fa82fc6915e0c68e34b1e824b7b56a3a086937a2532c8662f9f6e26674)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putDeleteMarkerReplication")
    def put_delete_marker_replication(self, *, status: builtins.str) -> None:
        '''
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#status S3BucketReplicationConfigurationA#status}.
        '''
        value = S3BucketReplicationConfigurationRuleDeleteMarkerReplication(
            status=status
        )

        return typing.cast(None, jsii.invoke(self, "putDeleteMarkerReplication", [value]))

    @jsii.member(jsii_name="putDestination")
    def put_destination(
        self,
        *,
        bucket: builtins.str,
        access_control_translation: typing.Optional[typing.Union[S3BucketReplicationConfigurationRuleDestinationAccessControlTranslation, typing.Dict[builtins.str, typing.Any]]] = None,
        account: typing.Optional[builtins.str] = None,
        encryption_configuration: typing.Optional[typing.Union[S3BucketReplicationConfigurationRuleDestinationEncryptionConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
        metrics: typing.Optional[typing.Union[S3BucketReplicationConfigurationRuleDestinationMetrics, typing.Dict[builtins.str, typing.Any]]] = None,
        replication_time: typing.Optional[typing.Union[S3BucketReplicationConfigurationRuleDestinationReplicationTime, typing.Dict[builtins.str, typing.Any]]] = None,
        storage_class: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#bucket S3BucketReplicationConfigurationA#bucket}.
        :param access_control_translation: access_control_translation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#access_control_translation S3BucketReplicationConfigurationA#access_control_translation}
        :param account: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#account S3BucketReplicationConfigurationA#account}.
        :param encryption_configuration: encryption_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#encryption_configuration S3BucketReplicationConfigurationA#encryption_configuration}
        :param metrics: metrics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#metrics S3BucketReplicationConfigurationA#metrics}
        :param replication_time: replication_time block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#replication_time S3BucketReplicationConfigurationA#replication_time}
        :param storage_class: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#storage_class S3BucketReplicationConfigurationA#storage_class}.
        '''
        value = S3BucketReplicationConfigurationRuleDestination(
            bucket=bucket,
            access_control_translation=access_control_translation,
            account=account,
            encryption_configuration=encryption_configuration,
            metrics=metrics,
            replication_time=replication_time,
            storage_class=storage_class,
        )

        return typing.cast(None, jsii.invoke(self, "putDestination", [value]))

    @jsii.member(jsii_name="putExistingObjectReplication")
    def put_existing_object_replication(self, *, status: builtins.str) -> None:
        '''
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#status S3BucketReplicationConfigurationA#status}.
        '''
        value = S3BucketReplicationConfigurationRuleExistingObjectReplication(
            status=status
        )

        return typing.cast(None, jsii.invoke(self, "putExistingObjectReplication", [value]))

    @jsii.member(jsii_name="putFilter")
    def put_filter(
        self,
        *,
        and_: typing.Optional[typing.Union[S3BucketReplicationConfigurationRuleFilterAnd, typing.Dict[builtins.str, typing.Any]]] = None,
        prefix: typing.Optional[builtins.str] = None,
        tag: typing.Optional[typing.Union[S3BucketReplicationConfigurationRuleFilterTag, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param and_: and block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#and S3BucketReplicationConfigurationA#and}
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#prefix S3BucketReplicationConfigurationA#prefix}.
        :param tag: tag block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#tag S3BucketReplicationConfigurationA#tag}
        '''
        value = S3BucketReplicationConfigurationRuleFilter(
            and_=and_, prefix=prefix, tag=tag
        )

        return typing.cast(None, jsii.invoke(self, "putFilter", [value]))

    @jsii.member(jsii_name="putSourceSelectionCriteria")
    def put_source_selection_criteria(
        self,
        *,
        replica_modifications: typing.Optional[typing.Union["S3BucketReplicationConfigurationRuleSourceSelectionCriteriaReplicaModifications", typing.Dict[builtins.str, typing.Any]]] = None,
        sse_kms_encrypted_objects: typing.Optional[typing.Union["S3BucketReplicationConfigurationRuleSourceSelectionCriteriaSseKmsEncryptedObjects", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param replica_modifications: replica_modifications block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#replica_modifications S3BucketReplicationConfigurationA#replica_modifications}
        :param sse_kms_encrypted_objects: sse_kms_encrypted_objects block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#sse_kms_encrypted_objects S3BucketReplicationConfigurationA#sse_kms_encrypted_objects}
        '''
        value = S3BucketReplicationConfigurationRuleSourceSelectionCriteria(
            replica_modifications=replica_modifications,
            sse_kms_encrypted_objects=sse_kms_encrypted_objects,
        )

        return typing.cast(None, jsii.invoke(self, "putSourceSelectionCriteria", [value]))

    @jsii.member(jsii_name="resetDeleteMarkerReplication")
    def reset_delete_marker_replication(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeleteMarkerReplication", []))

    @jsii.member(jsii_name="resetExistingObjectReplication")
    def reset_existing_object_replication(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExistingObjectReplication", []))

    @jsii.member(jsii_name="resetFilter")
    def reset_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilter", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPrefix")
    def reset_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefix", []))

    @jsii.member(jsii_name="resetPriority")
    def reset_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPriority", []))

    @jsii.member(jsii_name="resetSourceSelectionCriteria")
    def reset_source_selection_criteria(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceSelectionCriteria", []))

    @builtins.property
    @jsii.member(jsii_name="deleteMarkerReplication")
    def delete_marker_replication(
        self,
    ) -> S3BucketReplicationConfigurationRuleDeleteMarkerReplicationOutputReference:
        return typing.cast(S3BucketReplicationConfigurationRuleDeleteMarkerReplicationOutputReference, jsii.get(self, "deleteMarkerReplication"))

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(
        self,
    ) -> S3BucketReplicationConfigurationRuleDestinationOutputReference:
        return typing.cast(S3BucketReplicationConfigurationRuleDestinationOutputReference, jsii.get(self, "destination"))

    @builtins.property
    @jsii.member(jsii_name="existingObjectReplication")
    def existing_object_replication(
        self,
    ) -> S3BucketReplicationConfigurationRuleExistingObjectReplicationOutputReference:
        return typing.cast(S3BucketReplicationConfigurationRuleExistingObjectReplicationOutputReference, jsii.get(self, "existingObjectReplication"))

    @builtins.property
    @jsii.member(jsii_name="filter")
    def filter(self) -> S3BucketReplicationConfigurationRuleFilterOutputReference:
        return typing.cast(S3BucketReplicationConfigurationRuleFilterOutputReference, jsii.get(self, "filter"))

    @builtins.property
    @jsii.member(jsii_name="sourceSelectionCriteria")
    def source_selection_criteria(
        self,
    ) -> "S3BucketReplicationConfigurationRuleSourceSelectionCriteriaOutputReference":
        return typing.cast("S3BucketReplicationConfigurationRuleSourceSelectionCriteriaOutputReference", jsii.get(self, "sourceSelectionCriteria"))

    @builtins.property
    @jsii.member(jsii_name="deleteMarkerReplicationInput")
    def delete_marker_replication_input(
        self,
    ) -> typing.Optional[S3BucketReplicationConfigurationRuleDeleteMarkerReplication]:
        return typing.cast(typing.Optional[S3BucketReplicationConfigurationRuleDeleteMarkerReplication], jsii.get(self, "deleteMarkerReplicationInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationInput")
    def destination_input(
        self,
    ) -> typing.Optional[S3BucketReplicationConfigurationRuleDestination]:
        return typing.cast(typing.Optional[S3BucketReplicationConfigurationRuleDestination], jsii.get(self, "destinationInput"))

    @builtins.property
    @jsii.member(jsii_name="existingObjectReplicationInput")
    def existing_object_replication_input(
        self,
    ) -> typing.Optional[S3BucketReplicationConfigurationRuleExistingObjectReplication]:
        return typing.cast(typing.Optional[S3BucketReplicationConfigurationRuleExistingObjectReplication], jsii.get(self, "existingObjectReplicationInput"))

    @builtins.property
    @jsii.member(jsii_name="filterInput")
    def filter_input(
        self,
    ) -> typing.Optional[S3BucketReplicationConfigurationRuleFilter]:
        return typing.cast(typing.Optional[S3BucketReplicationConfigurationRuleFilter], jsii.get(self, "filterInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceSelectionCriteriaInput")
    def source_selection_criteria_input(
        self,
    ) -> typing.Optional["S3BucketReplicationConfigurationRuleSourceSelectionCriteria"]:
        return typing.cast(typing.Optional["S3BucketReplicationConfigurationRuleSourceSelectionCriteria"], jsii.get(self, "sourceSelectionCriteriaInput"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e097d79925b241d3f71874e834b974f7e5c07f27be60a1da0d1cb804d9ad188f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7372842742fbce6e91d0f8e0320c7c1ce19cbf5d355d6667244ace90651ccf6c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8349d47461be01a500fd5db39ed15cc03f24f40640f20d2a9f2d448cdc148f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cefb4d6759b4a9bf8ed5a0520b3a0934b8fc97c40e0e9fd566b50b82076ceb1d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[S3BucketReplicationConfigurationRule, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[S3BucketReplicationConfigurationRule, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[S3BucketReplicationConfigurationRule, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3bc5c137778e0cebb5d2798c9522a79c0c6b30ad9f95379bfb2467dcf1a5a34b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3BucketReplicationConfiguration.S3BucketReplicationConfigurationRuleSourceSelectionCriteria",
    jsii_struct_bases=[],
    name_mapping={
        "replica_modifications": "replicaModifications",
        "sse_kms_encrypted_objects": "sseKmsEncryptedObjects",
    },
)
class S3BucketReplicationConfigurationRuleSourceSelectionCriteria:
    def __init__(
        self,
        *,
        replica_modifications: typing.Optional[typing.Union["S3BucketReplicationConfigurationRuleSourceSelectionCriteriaReplicaModifications", typing.Dict[builtins.str, typing.Any]]] = None,
        sse_kms_encrypted_objects: typing.Optional[typing.Union["S3BucketReplicationConfigurationRuleSourceSelectionCriteriaSseKmsEncryptedObjects", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param replica_modifications: replica_modifications block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#replica_modifications S3BucketReplicationConfigurationA#replica_modifications}
        :param sse_kms_encrypted_objects: sse_kms_encrypted_objects block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#sse_kms_encrypted_objects S3BucketReplicationConfigurationA#sse_kms_encrypted_objects}
        '''
        if isinstance(replica_modifications, dict):
            replica_modifications = S3BucketReplicationConfigurationRuleSourceSelectionCriteriaReplicaModifications(**replica_modifications)
        if isinstance(sse_kms_encrypted_objects, dict):
            sse_kms_encrypted_objects = S3BucketReplicationConfigurationRuleSourceSelectionCriteriaSseKmsEncryptedObjects(**sse_kms_encrypted_objects)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba366e580942d3dc8e656bf8e09d8fc4dd4db4f3f1319caf3d766971b2dd2d87)
            check_type(argname="argument replica_modifications", value=replica_modifications, expected_type=type_hints["replica_modifications"])
            check_type(argname="argument sse_kms_encrypted_objects", value=sse_kms_encrypted_objects, expected_type=type_hints["sse_kms_encrypted_objects"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if replica_modifications is not None:
            self._values["replica_modifications"] = replica_modifications
        if sse_kms_encrypted_objects is not None:
            self._values["sse_kms_encrypted_objects"] = sse_kms_encrypted_objects

    @builtins.property
    def replica_modifications(
        self,
    ) -> typing.Optional["S3BucketReplicationConfigurationRuleSourceSelectionCriteriaReplicaModifications"]:
        '''replica_modifications block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#replica_modifications S3BucketReplicationConfigurationA#replica_modifications}
        '''
        result = self._values.get("replica_modifications")
        return typing.cast(typing.Optional["S3BucketReplicationConfigurationRuleSourceSelectionCriteriaReplicaModifications"], result)

    @builtins.property
    def sse_kms_encrypted_objects(
        self,
    ) -> typing.Optional["S3BucketReplicationConfigurationRuleSourceSelectionCriteriaSseKmsEncryptedObjects"]:
        '''sse_kms_encrypted_objects block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#sse_kms_encrypted_objects S3BucketReplicationConfigurationA#sse_kms_encrypted_objects}
        '''
        result = self._values.get("sse_kms_encrypted_objects")
        return typing.cast(typing.Optional["S3BucketReplicationConfigurationRuleSourceSelectionCriteriaSseKmsEncryptedObjects"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketReplicationConfigurationRuleSourceSelectionCriteria(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketReplicationConfigurationRuleSourceSelectionCriteriaOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketReplicationConfiguration.S3BucketReplicationConfigurationRuleSourceSelectionCriteriaOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ddf628a5b07a50d76a4a8117679132f232d0647438e5c4eb8ccc9d2c9c478290)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putReplicaModifications")
    def put_replica_modifications(self, *, status: builtins.str) -> None:
        '''
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#status S3BucketReplicationConfigurationA#status}.
        '''
        value = S3BucketReplicationConfigurationRuleSourceSelectionCriteriaReplicaModifications(
            status=status
        )

        return typing.cast(None, jsii.invoke(self, "putReplicaModifications", [value]))

    @jsii.member(jsii_name="putSseKmsEncryptedObjects")
    def put_sse_kms_encrypted_objects(self, *, status: builtins.str) -> None:
        '''
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#status S3BucketReplicationConfigurationA#status}.
        '''
        value = S3BucketReplicationConfigurationRuleSourceSelectionCriteriaSseKmsEncryptedObjects(
            status=status
        )

        return typing.cast(None, jsii.invoke(self, "putSseKmsEncryptedObjects", [value]))

    @jsii.member(jsii_name="resetReplicaModifications")
    def reset_replica_modifications(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReplicaModifications", []))

    @jsii.member(jsii_name="resetSseKmsEncryptedObjects")
    def reset_sse_kms_encrypted_objects(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSseKmsEncryptedObjects", []))

    @builtins.property
    @jsii.member(jsii_name="replicaModifications")
    def replica_modifications(
        self,
    ) -> "S3BucketReplicationConfigurationRuleSourceSelectionCriteriaReplicaModificationsOutputReference":
        return typing.cast("S3BucketReplicationConfigurationRuleSourceSelectionCriteriaReplicaModificationsOutputReference", jsii.get(self, "replicaModifications"))

    @builtins.property
    @jsii.member(jsii_name="sseKmsEncryptedObjects")
    def sse_kms_encrypted_objects(
        self,
    ) -> "S3BucketReplicationConfigurationRuleSourceSelectionCriteriaSseKmsEncryptedObjectsOutputReference":
        return typing.cast("S3BucketReplicationConfigurationRuleSourceSelectionCriteriaSseKmsEncryptedObjectsOutputReference", jsii.get(self, "sseKmsEncryptedObjects"))

    @builtins.property
    @jsii.member(jsii_name="replicaModificationsInput")
    def replica_modifications_input(
        self,
    ) -> typing.Optional["S3BucketReplicationConfigurationRuleSourceSelectionCriteriaReplicaModifications"]:
        return typing.cast(typing.Optional["S3BucketReplicationConfigurationRuleSourceSelectionCriteriaReplicaModifications"], jsii.get(self, "replicaModificationsInput"))

    @builtins.property
    @jsii.member(jsii_name="sseKmsEncryptedObjectsInput")
    def sse_kms_encrypted_objects_input(
        self,
    ) -> typing.Optional["S3BucketReplicationConfigurationRuleSourceSelectionCriteriaSseKmsEncryptedObjects"]:
        return typing.cast(typing.Optional["S3BucketReplicationConfigurationRuleSourceSelectionCriteriaSseKmsEncryptedObjects"], jsii.get(self, "sseKmsEncryptedObjectsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketReplicationConfigurationRuleSourceSelectionCriteria]:
        return typing.cast(typing.Optional[S3BucketReplicationConfigurationRuleSourceSelectionCriteria], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketReplicationConfigurationRuleSourceSelectionCriteria],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19c38476f2d2834ac2c81479ab6d8aeb0f5dc0c4c2e3fd63aee99594003329b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3BucketReplicationConfiguration.S3BucketReplicationConfigurationRuleSourceSelectionCriteriaReplicaModifications",
    jsii_struct_bases=[],
    name_mapping={"status": "status"},
)
class S3BucketReplicationConfigurationRuleSourceSelectionCriteriaReplicaModifications:
    def __init__(self, *, status: builtins.str) -> None:
        '''
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#status S3BucketReplicationConfigurationA#status}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5ef646c3e0c5a8ad776f2bd391d8424e88f0b84438aeff6264c74f04ac1fcdb)
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "status": status,
        }

    @builtins.property
    def status(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#status S3BucketReplicationConfigurationA#status}.'''
        result = self._values.get("status")
        assert result is not None, "Required property 'status' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketReplicationConfigurationRuleSourceSelectionCriteriaReplicaModifications(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketReplicationConfigurationRuleSourceSelectionCriteriaReplicaModificationsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketReplicationConfiguration.S3BucketReplicationConfigurationRuleSourceSelectionCriteriaReplicaModificationsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1542586021988a29360ce5631163c20180f02eceba10c42a92ae6201e0a16b0d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d7b2adfc13c3f3359b121d8200c979dcbe86c09d962a03933dd0ad69a233339)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketReplicationConfigurationRuleSourceSelectionCriteriaReplicaModifications]:
        return typing.cast(typing.Optional[S3BucketReplicationConfigurationRuleSourceSelectionCriteriaReplicaModifications], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketReplicationConfigurationRuleSourceSelectionCriteriaReplicaModifications],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d07ad10b81dcfc05b677a73e81db58045eeb9d74215ebb813f61ecd3b03e4f87)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3BucketReplicationConfiguration.S3BucketReplicationConfigurationRuleSourceSelectionCriteriaSseKmsEncryptedObjects",
    jsii_struct_bases=[],
    name_mapping={"status": "status"},
)
class S3BucketReplicationConfigurationRuleSourceSelectionCriteriaSseKmsEncryptedObjects:
    def __init__(self, *, status: builtins.str) -> None:
        '''
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#status S3BucketReplicationConfigurationA#status}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13e60a42984ce3d10b5a7d6a0138c1d10bb2b97207666fbff30291da81ea1f8b)
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "status": status,
        }

    @builtins.property
    def status(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_replication_configuration#status S3BucketReplicationConfigurationA#status}.'''
        result = self._values.get("status")
        assert result is not None, "Required property 'status' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketReplicationConfigurationRuleSourceSelectionCriteriaSseKmsEncryptedObjects(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketReplicationConfigurationRuleSourceSelectionCriteriaSseKmsEncryptedObjectsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketReplicationConfiguration.S3BucketReplicationConfigurationRuleSourceSelectionCriteriaSseKmsEncryptedObjectsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e98067ee3ffe8321bdb0cd1a83f6b0e35470380721382cc9c0b8892598c48b44)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a9ef95d71f51231099a0f41c49345d93f48579c663aed980356adbe79ffdb32)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketReplicationConfigurationRuleSourceSelectionCriteriaSseKmsEncryptedObjects]:
        return typing.cast(typing.Optional[S3BucketReplicationConfigurationRuleSourceSelectionCriteriaSseKmsEncryptedObjects], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketReplicationConfigurationRuleSourceSelectionCriteriaSseKmsEncryptedObjects],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9d91a9b809039f9c2c1e47029548aa6d51aaf9110f96350f9c019d45853f47c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "S3BucketReplicationConfigurationA",
    "S3BucketReplicationConfigurationAConfig",
    "S3BucketReplicationConfigurationRule",
    "S3BucketReplicationConfigurationRuleDeleteMarkerReplication",
    "S3BucketReplicationConfigurationRuleDeleteMarkerReplicationOutputReference",
    "S3BucketReplicationConfigurationRuleDestination",
    "S3BucketReplicationConfigurationRuleDestinationAccessControlTranslation",
    "S3BucketReplicationConfigurationRuleDestinationAccessControlTranslationOutputReference",
    "S3BucketReplicationConfigurationRuleDestinationEncryptionConfiguration",
    "S3BucketReplicationConfigurationRuleDestinationEncryptionConfigurationOutputReference",
    "S3BucketReplicationConfigurationRuleDestinationMetrics",
    "S3BucketReplicationConfigurationRuleDestinationMetricsEventThreshold",
    "S3BucketReplicationConfigurationRuleDestinationMetricsEventThresholdOutputReference",
    "S3BucketReplicationConfigurationRuleDestinationMetricsOutputReference",
    "S3BucketReplicationConfigurationRuleDestinationOutputReference",
    "S3BucketReplicationConfigurationRuleDestinationReplicationTime",
    "S3BucketReplicationConfigurationRuleDestinationReplicationTimeOutputReference",
    "S3BucketReplicationConfigurationRuleDestinationReplicationTimeTime",
    "S3BucketReplicationConfigurationRuleDestinationReplicationTimeTimeOutputReference",
    "S3BucketReplicationConfigurationRuleExistingObjectReplication",
    "S3BucketReplicationConfigurationRuleExistingObjectReplicationOutputReference",
    "S3BucketReplicationConfigurationRuleFilter",
    "S3BucketReplicationConfigurationRuleFilterAnd",
    "S3BucketReplicationConfigurationRuleFilterAndOutputReference",
    "S3BucketReplicationConfigurationRuleFilterOutputReference",
    "S3BucketReplicationConfigurationRuleFilterTag",
    "S3BucketReplicationConfigurationRuleFilterTagOutputReference",
    "S3BucketReplicationConfigurationRuleList",
    "S3BucketReplicationConfigurationRuleOutputReference",
    "S3BucketReplicationConfigurationRuleSourceSelectionCriteria",
    "S3BucketReplicationConfigurationRuleSourceSelectionCriteriaOutputReference",
    "S3BucketReplicationConfigurationRuleSourceSelectionCriteriaReplicaModifications",
    "S3BucketReplicationConfigurationRuleSourceSelectionCriteriaReplicaModificationsOutputReference",
    "S3BucketReplicationConfigurationRuleSourceSelectionCriteriaSseKmsEncryptedObjects",
    "S3BucketReplicationConfigurationRuleSourceSelectionCriteriaSseKmsEncryptedObjectsOutputReference",
]

publication.publish()

def _typecheckingstub__a00ef44dbf5e747ff466d1e10eb2784cf26f076275ada3d6721ef1eeac27053d(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    bucket: builtins.str,
    role: builtins.str,
    rule: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[S3BucketReplicationConfigurationRule, typing.Dict[builtins.str, typing.Any]]]],
    id: typing.Optional[builtins.str] = None,
    token: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__74c8cdc0b0d06b4471ae0d7a45069dbda0d7f1344f6b65e05b71a5b93c6154b2(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[S3BucketReplicationConfigurationRule, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24ff2de8b3d6c594ec1b493980e7563f967a8774349dee14e338c49abedc3a86(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb6feb5a4177e6fb68c4e8570982b09ced1db991d1c2cca8a44cdaf5c39d296a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c23a9e111b0f6639579bf50e1495a171d131b4635ea551969391bfa701718fb6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e692b9da2b9d1aaae8066674a83524b02b6d1008a0529eed18e340c22ab34855(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24888e56a25a7324b58bb3b3d727793424f09925d02343b6eec175e101be1f5f(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    bucket: builtins.str,
    role: builtins.str,
    rule: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[S3BucketReplicationConfigurationRule, typing.Dict[builtins.str, typing.Any]]]],
    id: typing.Optional[builtins.str] = None,
    token: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39591452702cf49409a1719c3157143dfe7803e6e44ebf12bf841054dd860c17(
    *,
    destination: typing.Union[S3BucketReplicationConfigurationRuleDestination, typing.Dict[builtins.str, typing.Any]],
    status: builtins.str,
    delete_marker_replication: typing.Optional[typing.Union[S3BucketReplicationConfigurationRuleDeleteMarkerReplication, typing.Dict[builtins.str, typing.Any]]] = None,
    existing_object_replication: typing.Optional[typing.Union[S3BucketReplicationConfigurationRuleExistingObjectReplication, typing.Dict[builtins.str, typing.Any]]] = None,
    filter: typing.Optional[typing.Union[S3BucketReplicationConfigurationRuleFilter, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    prefix: typing.Optional[builtins.str] = None,
    priority: typing.Optional[jsii.Number] = None,
    source_selection_criteria: typing.Optional[typing.Union[S3BucketReplicationConfigurationRuleSourceSelectionCriteria, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a34bc6800b9efd934610f5d18213de007d98421c7ab0f9a2528f0f60a178d79f(
    *,
    status: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5af452fa57fc468533530db3a772be1a91aadd9785ac7ddf62c220b70dc408c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99f5de09097132dd587e03aa6b10970dd265f0b41e2b9cff9311b7a3efc79645(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__591b05213c3f9f6869720ba13b594e784ebb77a00005c499544392f84b5bcc92(
    value: typing.Optional[S3BucketReplicationConfigurationRuleDeleteMarkerReplication],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55c565986b591cc6823d994fd950b1f4e48ccd93476f2fa6630e3aac91d96fdd(
    *,
    bucket: builtins.str,
    access_control_translation: typing.Optional[typing.Union[S3BucketReplicationConfigurationRuleDestinationAccessControlTranslation, typing.Dict[builtins.str, typing.Any]]] = None,
    account: typing.Optional[builtins.str] = None,
    encryption_configuration: typing.Optional[typing.Union[S3BucketReplicationConfigurationRuleDestinationEncryptionConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    metrics: typing.Optional[typing.Union[S3BucketReplicationConfigurationRuleDestinationMetrics, typing.Dict[builtins.str, typing.Any]]] = None,
    replication_time: typing.Optional[typing.Union[S3BucketReplicationConfigurationRuleDestinationReplicationTime, typing.Dict[builtins.str, typing.Any]]] = None,
    storage_class: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc9c2053106a166f37068fc45d444968ae4bf04bc1a0b51119f848126c7836e9(
    *,
    owner: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9d5b344773f8360cc549ac261d22dbfacb8f4cd5189cab4d9364e9b2f60a808(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f652c54c33735c267bff6f321b572d3fbee0c42f8c70144a32842040acaedb73(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a508e532e3f5b854c002e272ecda63040aa154131d19ead8b3f4b04ab3627f4(
    value: typing.Optional[S3BucketReplicationConfigurationRuleDestinationAccessControlTranslation],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd5bf09cb38b4fa857ad57db1c6723f795d1595b8893595de96aa019958dfcca(
    *,
    replica_kms_key_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__586c0b2b1bca9a9a30a4b72fbf873b6bf1babb9fdac6d8d2fc841c9c6f42b566(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b4b587e04c987724d22c227a017c6bbc48182a1216ceaa5d042ad82272567b4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__103e5a77d1ed7d3d9de217f38ca9b3d70f7d6f1859c26f53e638f9dec8449397(
    value: typing.Optional[S3BucketReplicationConfigurationRuleDestinationEncryptionConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb71a698938cfdf7d2fb4074db3675108c38c7377b6d67bdcfa7e9fb23e822c3(
    *,
    status: builtins.str,
    event_threshold: typing.Optional[typing.Union[S3BucketReplicationConfigurationRuleDestinationMetricsEventThreshold, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b3d424cd6de03e3ccb77dbb5c833e3d353d972a38f883fbbae5c47eeb64417e(
    *,
    minutes: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0aa2f11ecf9238c70366e8f9799de64333a0ee2e792da46b3257993abefcdec6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63e1b31d5e65a0a4f85475cee63d7f07b170c49a68dcc5551e97c8b320b01030(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f3f2325d4219c867872d7301cc713f170da1a4a72531ef580566f0a69ff4543(
    value: typing.Optional[S3BucketReplicationConfigurationRuleDestinationMetricsEventThreshold],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__416166aa49964c253c9cbe5e18cdb09fb5453eb3928e7daf439eabd1ae4dc9cb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e127956bcbdc3a3f30fc3104194f0cff53786984906dc56951aaf2e970ff8487(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb842eb6e555aa9af2198c58e7efb2322ecfcdc32abf537ac7a45017dce30d66(
    value: typing.Optional[S3BucketReplicationConfigurationRuleDestinationMetrics],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd0c4a9f0dcf8601d14513712d695e213c42cb7d9ddfb04927a3ecf59fa09bc4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__673aa2bb7f5050d96e9468ecfa98d8fb10b877d0edca49d2db8ca74ddfc65080(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__945bc0805f34b312bc1c391d95bc7211ca803086e6215d6816d0e006a2279097(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8849da212accb7dd4da8c7c7e83f3fd42da2313791b111a376a58e483f4fa3e9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e2b61ab01ed535eedd02c2fe26856bf9cbada5a7ea49e223f4f8397ed6cb84e(
    value: typing.Optional[S3BucketReplicationConfigurationRuleDestination],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__598fcf6f4b963de700a6b21b47f404d22c63e931f3a58c6f50dc2675074e3ae9(
    *,
    status: builtins.str,
    time: typing.Union[S3BucketReplicationConfigurationRuleDestinationReplicationTimeTime, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ece32e6d87dd9634dc54f3d0a052fa2f686faf85857c2ee2d2eddec8cd42a2ce(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d70c6cd88a31553d2e26cf5c67d638877778d58be7045c3126e2ea90549896e7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c35e834041961524df481e3921a59a2970410d3b7af883b8f3245367126a0f87(
    value: typing.Optional[S3BucketReplicationConfigurationRuleDestinationReplicationTime],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2659bbbb9feb3bdf32205f77abc19268c4156d3dc51b120e07d7c96e5a7e959(
    *,
    minutes: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51056b2b9430ead5d93f94c739ea41e3295549501833eba5c32fc5ff06a0abed(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb544014dfab2992f4a8ee67d22c71b06e11273f143547e3d027be77aae5eba6(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3647e90c29321b2c3e3d9c07d5a6a8efddca0f38effaaf68e88c1604cb2c2268(
    value: typing.Optional[S3BucketReplicationConfigurationRuleDestinationReplicationTimeTime],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b3ba417eb7e7a96c6662a7c8f23f42179c9a3429b9252945537ce2576eed61f(
    *,
    status: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2607b756636c4e35b5d3a7b8cb4d8ca8462be67a8a56c832cf04c82801be13f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fede01a2aae12d1d4aa545a53c24a0f12d3442430f40d8da7f4e6bb699de05b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46505493cd8193b2d2ef1d6571674be89cd4f42daa64567afc61a3104d91e7ec(
    value: typing.Optional[S3BucketReplicationConfigurationRuleExistingObjectReplication],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93cdab7d3241644cf52386c164f70fbffaebf252c672e924808a4775e8c937ae(
    *,
    and_: typing.Optional[typing.Union[S3BucketReplicationConfigurationRuleFilterAnd, typing.Dict[builtins.str, typing.Any]]] = None,
    prefix: typing.Optional[builtins.str] = None,
    tag: typing.Optional[typing.Union[S3BucketReplicationConfigurationRuleFilterTag, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77a59486ef083a51639ecb31e70cb0e7a74a0414d2f647f8df412c3163ee36db(
    *,
    prefix: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9f705333deebdbd81c830d40f47330c235b9a297bf27479a6a890c0e87843a8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51cbaf57ac8fc1ef57a47c74a30db816d2adb5ece25975b8dd82bf77d433b8e8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c4ff5c2c7aad2edaedea1d98d1ee19cb531da992d460ef2c508fd28803bce49(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11480e2f3d211e38936d8b64eeb947a862d75a9144065c08955f8da0f5deaae0(
    value: typing.Optional[S3BucketReplicationConfigurationRuleFilterAnd],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72823ab035c9b6ac0635b66abefb728896d4d8c1ee729581951924ff0ec94591(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d2445d1b987520f61fb0a045da12120ddee6c36b61c14af01ebe3c42c472f0b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30c46cbbf30b67997dcb710ab10e570dac919327f9c1f669360e142c67bd247a(
    value: typing.Optional[S3BucketReplicationConfigurationRuleFilter],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__281315d5bc1ab7eefc73f194e708aea44349c61d95f58bd1087e89929e6ef5c7(
    *,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f02d22c88cc6ea6690c78255776e3fca35875f0b3e40c1d3ead3d13090c31074(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b12417c0be2e8af1b71724f9576b7a0731e6f06c772072e165ffe28a0175b500(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6470bcdc0086efd3cfa21fe35f7e2f595b04bc894cbdc61480f2ff9885f1b849(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42f09f43d177d2154734d5d3637df9f621409ac1345bf3e2953839ff125f5d0c(
    value: typing.Optional[S3BucketReplicationConfigurationRuleFilterTag],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87a74b7c0ae2308b70e11c8a6670b9430f406f21d4a878142bbdc552ca11ba47(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a1d695c84c22473cbd4b0eb66ebf180f5a0dfb20e58c5c2ec0f8dc870ee57db(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a845b3d13671e306a16eeb39a4d4f254bb2ed3260475aaaf8ff4b1b1646a0f3f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08e207068cad8f506469b5af0438e4e1aa99546a274c3fb56f9995b7c7aa51cb(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__883aae6322aa460563ebce28441dd3af49849e2bbeaac03fe6189b75ecd2b4c3(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9b996f44bb9b4441c24fc4403ed80e958c5eba701293129e7d4d4184fbd83ae(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketReplicationConfigurationRule]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__924931fa82fc6915e0c68e34b1e824b7b56a3a086937a2532c8662f9f6e26674(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e097d79925b241d3f71874e834b974f7e5c07f27be60a1da0d1cb804d9ad188f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7372842742fbce6e91d0f8e0320c7c1ce19cbf5d355d6667244ace90651ccf6c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8349d47461be01a500fd5db39ed15cc03f24f40640f20d2a9f2d448cdc148f4(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cefb4d6759b4a9bf8ed5a0520b3a0934b8fc97c40e0e9fd566b50b82076ceb1d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bc5c137778e0cebb5d2798c9522a79c0c6b30ad9f95379bfb2467dcf1a5a34b(
    value: typing.Optional[typing.Union[S3BucketReplicationConfigurationRule, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba366e580942d3dc8e656bf8e09d8fc4dd4db4f3f1319caf3d766971b2dd2d87(
    *,
    replica_modifications: typing.Optional[typing.Union[S3BucketReplicationConfigurationRuleSourceSelectionCriteriaReplicaModifications, typing.Dict[builtins.str, typing.Any]]] = None,
    sse_kms_encrypted_objects: typing.Optional[typing.Union[S3BucketReplicationConfigurationRuleSourceSelectionCriteriaSseKmsEncryptedObjects, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddf628a5b07a50d76a4a8117679132f232d0647438e5c4eb8ccc9d2c9c478290(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19c38476f2d2834ac2c81479ab6d8aeb0f5dc0c4c2e3fd63aee99594003329b0(
    value: typing.Optional[S3BucketReplicationConfigurationRuleSourceSelectionCriteria],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5ef646c3e0c5a8ad776f2bd391d8424e88f0b84438aeff6264c74f04ac1fcdb(
    *,
    status: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1542586021988a29360ce5631163c20180f02eceba10c42a92ae6201e0a16b0d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d7b2adfc13c3f3359b121d8200c979dcbe86c09d962a03933dd0ad69a233339(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d07ad10b81dcfc05b677a73e81db58045eeb9d74215ebb813f61ecd3b03e4f87(
    value: typing.Optional[S3BucketReplicationConfigurationRuleSourceSelectionCriteriaReplicaModifications],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13e60a42984ce3d10b5a7d6a0138c1d10bb2b97207666fbff30291da81ea1f8b(
    *,
    status: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e98067ee3ffe8321bdb0cd1a83f6b0e35470380721382cc9c0b8892598c48b44(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a9ef95d71f51231099a0f41c49345d93f48579c663aed980356adbe79ffdb32(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9d91a9b809039f9c2c1e47029548aa6d51aaf9110f96350f9c019d45853f47c(
    value: typing.Optional[S3BucketReplicationConfigurationRuleSourceSelectionCriteriaSseKmsEncryptedObjects],
) -> None:
    """Type checking stubs"""
    pass
