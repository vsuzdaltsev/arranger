'''
# `data_aws_route53_traffic_policy_document`

Refer to the Terraform Registory for docs: [`data_aws_route53_traffic_policy_document`](https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document).
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


class DataAwsRoute53TrafficPolicyDocument(
    _cdktf_9a9027ec.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsRoute53TrafficPolicyDocument.DataAwsRoute53TrafficPolicyDocument",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document aws_route53_traffic_policy_document}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        endpoint: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAwsRoute53TrafficPolicyDocumentEndpoint", typing.Dict[builtins.str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        record_type: typing.Optional[builtins.str] = None,
        rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAwsRoute53TrafficPolicyDocumentRule", typing.Dict[builtins.str, typing.Any]]]]] = None,
        start_endpoint: typing.Optional[builtins.str] = None,
        start_rule: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document aws_route53_traffic_policy_document} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param endpoint: endpoint block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#endpoint DataAwsRoute53TrafficPolicyDocument#endpoint}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#id DataAwsRoute53TrafficPolicyDocument#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param record_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#record_type DataAwsRoute53TrafficPolicyDocument#record_type}.
        :param rule: rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#rule DataAwsRoute53TrafficPolicyDocument#rule}
        :param start_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#start_endpoint DataAwsRoute53TrafficPolicyDocument#start_endpoint}.
        :param start_rule: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#start_rule DataAwsRoute53TrafficPolicyDocument#start_rule}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#version DataAwsRoute53TrafficPolicyDocument#version}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d48e72b418e7a7f5063db6316c8a8a4004e66203a6481abbe5dd4f9a9f24278f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataAwsRoute53TrafficPolicyDocumentConfig(
            endpoint=endpoint,
            id=id,
            record_type=record_type,
            rule=rule,
            start_endpoint=start_endpoint,
            start_rule=start_rule,
            version=version,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putEndpoint")
    def put_endpoint(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAwsRoute53TrafficPolicyDocumentEndpoint", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e77d05da1791f609edce33c6ba3e3b4a5951fb71f5a2df3a21e15eb906662f3b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEndpoint", [value]))

    @jsii.member(jsii_name="putRule")
    def put_rule(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAwsRoute53TrafficPolicyDocumentRule", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82ccaac1123f6547004a0141500bb522ac5a9262c2878659dfeab71b0788ffb9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRule", [value]))

    @jsii.member(jsii_name="resetEndpoint")
    def reset_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndpoint", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetRecordType")
    def reset_record_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecordType", []))

    @jsii.member(jsii_name="resetRule")
    def reset_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRule", []))

    @jsii.member(jsii_name="resetStartEndpoint")
    def reset_start_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartEndpoint", []))

    @jsii.member(jsii_name="resetStartRule")
    def reset_start_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartRule", []))

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> "DataAwsRoute53TrafficPolicyDocumentEndpointList":
        return typing.cast("DataAwsRoute53TrafficPolicyDocumentEndpointList", jsii.get(self, "endpoint"))

    @builtins.property
    @jsii.member(jsii_name="json")
    def json(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "json"))

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> "DataAwsRoute53TrafficPolicyDocumentRuleList":
        return typing.cast("DataAwsRoute53TrafficPolicyDocumentRuleList", jsii.get(self, "rule"))

    @builtins.property
    @jsii.member(jsii_name="endpointInput")
    def endpoint_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAwsRoute53TrafficPolicyDocumentEndpoint"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAwsRoute53TrafficPolicyDocumentEndpoint"]]], jsii.get(self, "endpointInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="recordTypeInput")
    def record_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recordTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAwsRoute53TrafficPolicyDocumentRule"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAwsRoute53TrafficPolicyDocumentRule"]]], jsii.get(self, "ruleInput"))

    @builtins.property
    @jsii.member(jsii_name="startEndpointInput")
    def start_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="startRuleInput")
    def start_rule_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__996212dbe341ce1d1d7521f4270f381dd61dc4d789714440546cb292584b907a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="recordType")
    def record_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recordType"))

    @record_type.setter
    def record_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b50ca844576cacfda3324a0633e1a4d4455d3da6975b87be1f604068a73c5a44)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordType", value)

    @builtins.property
    @jsii.member(jsii_name="startEndpoint")
    def start_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startEndpoint"))

    @start_endpoint.setter
    def start_endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28fcfbbb7eb3d1f6c3d21f73a4ab757f05350c08816c4a778f789a53d990937e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="startRule")
    def start_rule(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startRule"))

    @start_rule.setter
    def start_rule(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00f3ddbd0b4b062f446c109ff69592488a203c81dc2fee13c9f54151a96faefb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startRule", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0db052b00a7ae5a9721ce8d12005c7cc51b72a0d87c2ebb7dcd7f27370d14f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)


@jsii.data_type(
    jsii_type="aws.dataAwsRoute53TrafficPolicyDocument.DataAwsRoute53TrafficPolicyDocumentConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "endpoint": "endpoint",
        "id": "id",
        "record_type": "recordType",
        "rule": "rule",
        "start_endpoint": "startEndpoint",
        "start_rule": "startRule",
        "version": "version",
    },
)
class DataAwsRoute53TrafficPolicyDocumentConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        endpoint: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAwsRoute53TrafficPolicyDocumentEndpoint", typing.Dict[builtins.str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        record_type: typing.Optional[builtins.str] = None,
        rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAwsRoute53TrafficPolicyDocumentRule", typing.Dict[builtins.str, typing.Any]]]]] = None,
        start_endpoint: typing.Optional[builtins.str] = None,
        start_rule: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param endpoint: endpoint block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#endpoint DataAwsRoute53TrafficPolicyDocument#endpoint}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#id DataAwsRoute53TrafficPolicyDocument#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param record_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#record_type DataAwsRoute53TrafficPolicyDocument#record_type}.
        :param rule: rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#rule DataAwsRoute53TrafficPolicyDocument#rule}
        :param start_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#start_endpoint DataAwsRoute53TrafficPolicyDocument#start_endpoint}.
        :param start_rule: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#start_rule DataAwsRoute53TrafficPolicyDocument#start_rule}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#version DataAwsRoute53TrafficPolicyDocument#version}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c624bc1f93272d22113873c8ad7a050090cc8d5af033a2d0c71a033bbe2e19a)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument record_type", value=record_type, expected_type=type_hints["record_type"])
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument start_endpoint", value=start_endpoint, expected_type=type_hints["start_endpoint"])
            check_type(argname="argument start_rule", value=start_rule, expected_type=type_hints["start_rule"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
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
        if endpoint is not None:
            self._values["endpoint"] = endpoint
        if id is not None:
            self._values["id"] = id
        if record_type is not None:
            self._values["record_type"] = record_type
        if rule is not None:
            self._values["rule"] = rule
        if start_endpoint is not None:
            self._values["start_endpoint"] = start_endpoint
        if start_rule is not None:
            self._values["start_rule"] = start_rule
        if version is not None:
            self._values["version"] = version

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
    def endpoint(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAwsRoute53TrafficPolicyDocumentEndpoint"]]]:
        '''endpoint block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#endpoint DataAwsRoute53TrafficPolicyDocument#endpoint}
        '''
        result = self._values.get("endpoint")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAwsRoute53TrafficPolicyDocumentEndpoint"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#id DataAwsRoute53TrafficPolicyDocument#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def record_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#record_type DataAwsRoute53TrafficPolicyDocument#record_type}.'''
        result = self._values.get("record_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rule(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAwsRoute53TrafficPolicyDocumentRule"]]]:
        '''rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#rule DataAwsRoute53TrafficPolicyDocument#rule}
        '''
        result = self._values.get("rule")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAwsRoute53TrafficPolicyDocumentRule"]]], result)

    @builtins.property
    def start_endpoint(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#start_endpoint DataAwsRoute53TrafficPolicyDocument#start_endpoint}.'''
        result = self._values.get("start_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start_rule(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#start_rule DataAwsRoute53TrafficPolicyDocument#start_rule}.'''
        result = self._values.get("start_rule")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#version DataAwsRoute53TrafficPolicyDocument#version}.'''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsRoute53TrafficPolicyDocumentConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.dataAwsRoute53TrafficPolicyDocument.DataAwsRoute53TrafficPolicyDocumentEndpoint",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "region": "region", "type": "type", "value": "value"},
)
class DataAwsRoute53TrafficPolicyDocumentEndpoint:
    def __init__(
        self,
        *,
        id: builtins.str,
        region: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#id DataAwsRoute53TrafficPolicyDocument#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#region DataAwsRoute53TrafficPolicyDocument#region}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#type DataAwsRoute53TrafficPolicyDocument#type}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#value DataAwsRoute53TrafficPolicyDocument#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__929b31c22f3d006046203acecaaf878d22a62ae5a91ad7dc3cf9da50aca75183)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "id": id,
        }
        if region is not None:
            self._values["region"] = region
        if type is not None:
            self._values["type"] = type
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#id DataAwsRoute53TrafficPolicyDocument#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#region DataAwsRoute53TrafficPolicyDocument#region}.'''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#type DataAwsRoute53TrafficPolicyDocument#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#value DataAwsRoute53TrafficPolicyDocument#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsRoute53TrafficPolicyDocumentEndpoint(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsRoute53TrafficPolicyDocumentEndpointList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsRoute53TrafficPolicyDocument.DataAwsRoute53TrafficPolicyDocumentEndpointList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0d476e55ffeb1f2960c70b00a2fc20e2b5bc6469543d3b58eb31bfa036c2f3f2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAwsRoute53TrafficPolicyDocumentEndpointOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbcc0f67b3f856d823d8255cc3eecedf4902c0acecc9a4ef944eb891c46ae7d0)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsRoute53TrafficPolicyDocumentEndpointOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51aac8f3fd8dc17604d88db5f621f78bec0d937c910a76a3b9f26b1948a75bc1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__de8c22b8444df58373a799db4d166fea3b580ece4754c0c7ae5821511b1d9014)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f32a6dea06cf668874055432ff32c40b22061c3188d8ba4890529812e285630a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentEndpoint]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentEndpoint]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentEndpoint]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3cfaf8a0a334c4664ccd3ad00edb9bf547f96ca41da7940918c508ba171a59b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAwsRoute53TrafficPolicyDocumentEndpointOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsRoute53TrafficPolicyDocument.DataAwsRoute53TrafficPolicyDocumentEndpointOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ea1a4b61639af922d2892e89e15f09a3c226a79f08ead76673861d518df544e3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21de70a313339e3c573d54830aebc7d337489d5409f0ad7f471dc4212aaf156a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35f6e85cd0f97d8c1e2f8877f82e01f605c8dae222e692f0f05ef5bed02668c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29a52f0fb448c41260916bb164041624f003c7bd8598923db87761e142e4ce82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58c4e05fa8dbe56acd2e4d3d34944848b9565301d8230e0e59d5162bf660b9ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentEndpoint, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentEndpoint, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentEndpoint, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4b333b74589f110fdfe23cc590d4f7fa0d7cde39eb2d398e6eb25d1d474262d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dataAwsRoute53TrafficPolicyDocument.DataAwsRoute53TrafficPolicyDocumentRule",
    jsii_struct_bases=[],
    name_mapping={
        "id": "id",
        "geo_proximity_location": "geoProximityLocation",
        "items": "items",
        "location": "location",
        "primary": "primary",
        "region": "region",
        "secondary": "secondary",
        "type": "type",
    },
)
class DataAwsRoute53TrafficPolicyDocumentRule:
    def __init__(
        self,
        *,
        id: builtins.str,
        geo_proximity_location: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocation", typing.Dict[builtins.str, typing.Any]]]]] = None,
        items: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAwsRoute53TrafficPolicyDocumentRuleItems", typing.Dict[builtins.str, typing.Any]]]]] = None,
        location: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAwsRoute53TrafficPolicyDocumentRuleLocation", typing.Dict[builtins.str, typing.Any]]]]] = None,
        primary: typing.Optional[typing.Union["DataAwsRoute53TrafficPolicyDocumentRulePrimary", typing.Dict[builtins.str, typing.Any]]] = None,
        region: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAwsRoute53TrafficPolicyDocumentRuleRegion", typing.Dict[builtins.str, typing.Any]]]]] = None,
        secondary: typing.Optional[typing.Union["DataAwsRoute53TrafficPolicyDocumentRuleSecondary", typing.Dict[builtins.str, typing.Any]]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#id DataAwsRoute53TrafficPolicyDocument#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param geo_proximity_location: geo_proximity_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#geo_proximity_location DataAwsRoute53TrafficPolicyDocument#geo_proximity_location}
        :param items: items block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#items DataAwsRoute53TrafficPolicyDocument#items}
        :param location: location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#location DataAwsRoute53TrafficPolicyDocument#location}
        :param primary: primary block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#primary DataAwsRoute53TrafficPolicyDocument#primary}
        :param region: region block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#region DataAwsRoute53TrafficPolicyDocument#region}
        :param secondary: secondary block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#secondary DataAwsRoute53TrafficPolicyDocument#secondary}
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#type DataAwsRoute53TrafficPolicyDocument#type}.
        '''
        if isinstance(primary, dict):
            primary = DataAwsRoute53TrafficPolicyDocumentRulePrimary(**primary)
        if isinstance(secondary, dict):
            secondary = DataAwsRoute53TrafficPolicyDocumentRuleSecondary(**secondary)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee0a9e7452eba07e239c78ecbef581d90f2e0a53dcf1d19c99eaba6c39de6e57)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument geo_proximity_location", value=geo_proximity_location, expected_type=type_hints["geo_proximity_location"])
            check_type(argname="argument items", value=items, expected_type=type_hints["items"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument primary", value=primary, expected_type=type_hints["primary"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument secondary", value=secondary, expected_type=type_hints["secondary"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "id": id,
        }
        if geo_proximity_location is not None:
            self._values["geo_proximity_location"] = geo_proximity_location
        if items is not None:
            self._values["items"] = items
        if location is not None:
            self._values["location"] = location
        if primary is not None:
            self._values["primary"] = primary
        if region is not None:
            self._values["region"] = region
        if secondary is not None:
            self._values["secondary"] = secondary
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#id DataAwsRoute53TrafficPolicyDocument#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def geo_proximity_location(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocation"]]]:
        '''geo_proximity_location block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#geo_proximity_location DataAwsRoute53TrafficPolicyDocument#geo_proximity_location}
        '''
        result = self._values.get("geo_proximity_location")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocation"]]], result)

    @builtins.property
    def items(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAwsRoute53TrafficPolicyDocumentRuleItems"]]]:
        '''items block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#items DataAwsRoute53TrafficPolicyDocument#items}
        '''
        result = self._values.get("items")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAwsRoute53TrafficPolicyDocumentRuleItems"]]], result)

    @builtins.property
    def location(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAwsRoute53TrafficPolicyDocumentRuleLocation"]]]:
        '''location block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#location DataAwsRoute53TrafficPolicyDocument#location}
        '''
        result = self._values.get("location")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAwsRoute53TrafficPolicyDocumentRuleLocation"]]], result)

    @builtins.property
    def primary(
        self,
    ) -> typing.Optional["DataAwsRoute53TrafficPolicyDocumentRulePrimary"]:
        '''primary block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#primary DataAwsRoute53TrafficPolicyDocument#primary}
        '''
        result = self._values.get("primary")
        return typing.cast(typing.Optional["DataAwsRoute53TrafficPolicyDocumentRulePrimary"], result)

    @builtins.property
    def region(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAwsRoute53TrafficPolicyDocumentRuleRegion"]]]:
        '''region block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#region DataAwsRoute53TrafficPolicyDocument#region}
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAwsRoute53TrafficPolicyDocumentRuleRegion"]]], result)

    @builtins.property
    def secondary(
        self,
    ) -> typing.Optional["DataAwsRoute53TrafficPolicyDocumentRuleSecondary"]:
        '''secondary block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#secondary DataAwsRoute53TrafficPolicyDocument#secondary}
        '''
        result = self._values.get("secondary")
        return typing.cast(typing.Optional["DataAwsRoute53TrafficPolicyDocumentRuleSecondary"], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#type DataAwsRoute53TrafficPolicyDocument#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsRoute53TrafficPolicyDocumentRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.dataAwsRoute53TrafficPolicyDocument.DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocation",
    jsii_struct_bases=[],
    name_mapping={
        "bias": "bias",
        "endpoint_reference": "endpointReference",
        "evaluate_target_health": "evaluateTargetHealth",
        "health_check": "healthCheck",
        "latitude": "latitude",
        "longitude": "longitude",
        "region": "region",
        "rule_reference": "ruleReference",
    },
)
class DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocation:
    def __init__(
        self,
        *,
        bias: typing.Optional[builtins.str] = None,
        endpoint_reference: typing.Optional[builtins.str] = None,
        evaluate_target_health: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        health_check: typing.Optional[builtins.str] = None,
        latitude: typing.Optional[builtins.str] = None,
        longitude: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        rule_reference: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bias: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#bias DataAwsRoute53TrafficPolicyDocument#bias}.
        :param endpoint_reference: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#endpoint_reference DataAwsRoute53TrafficPolicyDocument#endpoint_reference}.
        :param evaluate_target_health: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#evaluate_target_health DataAwsRoute53TrafficPolicyDocument#evaluate_target_health}.
        :param health_check: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#health_check DataAwsRoute53TrafficPolicyDocument#health_check}.
        :param latitude: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#latitude DataAwsRoute53TrafficPolicyDocument#latitude}.
        :param longitude: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#longitude DataAwsRoute53TrafficPolicyDocument#longitude}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#region DataAwsRoute53TrafficPolicyDocument#region}.
        :param rule_reference: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#rule_reference DataAwsRoute53TrafficPolicyDocument#rule_reference}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1b5791f89a54630a8b22d4fc76b15f0383490770f1b281f278934fb725c3509)
            check_type(argname="argument bias", value=bias, expected_type=type_hints["bias"])
            check_type(argname="argument endpoint_reference", value=endpoint_reference, expected_type=type_hints["endpoint_reference"])
            check_type(argname="argument evaluate_target_health", value=evaluate_target_health, expected_type=type_hints["evaluate_target_health"])
            check_type(argname="argument health_check", value=health_check, expected_type=type_hints["health_check"])
            check_type(argname="argument latitude", value=latitude, expected_type=type_hints["latitude"])
            check_type(argname="argument longitude", value=longitude, expected_type=type_hints["longitude"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument rule_reference", value=rule_reference, expected_type=type_hints["rule_reference"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if bias is not None:
            self._values["bias"] = bias
        if endpoint_reference is not None:
            self._values["endpoint_reference"] = endpoint_reference
        if evaluate_target_health is not None:
            self._values["evaluate_target_health"] = evaluate_target_health
        if health_check is not None:
            self._values["health_check"] = health_check
        if latitude is not None:
            self._values["latitude"] = latitude
        if longitude is not None:
            self._values["longitude"] = longitude
        if region is not None:
            self._values["region"] = region
        if rule_reference is not None:
            self._values["rule_reference"] = rule_reference

    @builtins.property
    def bias(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#bias DataAwsRoute53TrafficPolicyDocument#bias}.'''
        result = self._values.get("bias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def endpoint_reference(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#endpoint_reference DataAwsRoute53TrafficPolicyDocument#endpoint_reference}.'''
        result = self._values.get("endpoint_reference")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def evaluate_target_health(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#evaluate_target_health DataAwsRoute53TrafficPolicyDocument#evaluate_target_health}.'''
        result = self._values.get("evaluate_target_health")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def health_check(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#health_check DataAwsRoute53TrafficPolicyDocument#health_check}.'''
        result = self._values.get("health_check")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def latitude(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#latitude DataAwsRoute53TrafficPolicyDocument#latitude}.'''
        result = self._values.get("latitude")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def longitude(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#longitude DataAwsRoute53TrafficPolicyDocument#longitude}.'''
        result = self._values.get("longitude")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#region DataAwsRoute53TrafficPolicyDocument#region}.'''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rule_reference(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#rule_reference DataAwsRoute53TrafficPolicyDocument#rule_reference}.'''
        result = self._values.get("rule_reference")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocationList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsRoute53TrafficPolicyDocument.DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocationList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9e1f1edbd81627c746ae850624c9b8d52a879797476e3bc6dcd0d92cd754cb3a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10cae2a0de7404cd016012efc862272bf25639217ac80eb28ad9e57c5b03acd4)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf77bbe65cbb14b8d2c647411c2d577d3a5bc9c8f3d1947304b438143a2c2745)
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
            type_hints = typing.get_type_hints(_typecheckingstub__eb93db689c1e3cc6967aea84fa3e6fa4ed53e4b7e271b75dc10a7a313cf66b89)
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
            type_hints = typing.get_type_hints(_typecheckingstub__438cf4bd18b6a2814225d3c6647a59512df51bb10b93f7ab2e0b7fe1d302be62)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocation]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocation]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocation]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf97a2383724692039c51c6a9efedee5f00512a8c190ee8c2e112c18e29a8c4c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsRoute53TrafficPolicyDocument.DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__74c5290503d4cce73eecc2bb3656863a511d1a505e148934d3f6c891bb8fa9c7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetBias")
    def reset_bias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBias", []))

    @jsii.member(jsii_name="resetEndpointReference")
    def reset_endpoint_reference(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndpointReference", []))

    @jsii.member(jsii_name="resetEvaluateTargetHealth")
    def reset_evaluate_target_health(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEvaluateTargetHealth", []))

    @jsii.member(jsii_name="resetHealthCheck")
    def reset_health_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheck", []))

    @jsii.member(jsii_name="resetLatitude")
    def reset_latitude(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLatitude", []))

    @jsii.member(jsii_name="resetLongitude")
    def reset_longitude(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLongitude", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetRuleReference")
    def reset_rule_reference(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRuleReference", []))

    @builtins.property
    @jsii.member(jsii_name="biasInput")
    def bias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "biasInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointReferenceInput")
    def endpoint_reference_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointReferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="evaluateTargetHealthInput")
    def evaluate_target_health_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "evaluateTargetHealthInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckInput")
    def health_check_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "healthCheckInput"))

    @builtins.property
    @jsii.member(jsii_name="latitudeInput")
    def latitude_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "latitudeInput"))

    @builtins.property
    @jsii.member(jsii_name="longitudeInput")
    def longitude_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "longitudeInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleReferenceInput")
    def rule_reference_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleReferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="bias")
    def bias(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bias"))

    @bias.setter
    def bias(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e92cac29ee9a311d557895e99d25ffa9dda73ff3bdeb21c7710eff6d066d988)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bias", value)

    @builtins.property
    @jsii.member(jsii_name="endpointReference")
    def endpoint_reference(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpointReference"))

    @endpoint_reference.setter
    def endpoint_reference(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7ecfc60c8b359d8a51cf5b4913cacd668562423a3d495c44b71d473484c1bbf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointReference", value)

    @builtins.property
    @jsii.member(jsii_name="evaluateTargetHealth")
    def evaluate_target_health(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "evaluateTargetHealth"))

    @evaluate_target_health.setter
    def evaluate_target_health(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e355f0f97c54bf5f29c951384924ac66894b636dfd693b9b9a3e2422dcd0cd9a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluateTargetHealth", value)

    @builtins.property
    @jsii.member(jsii_name="healthCheck")
    def health_check(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "healthCheck"))

    @health_check.setter
    def health_check(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0d747fe7737a0187d6ce0a06b9063a0ae1d71b7a710b8ecca4f3882a4173044)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthCheck", value)

    @builtins.property
    @jsii.member(jsii_name="latitude")
    def latitude(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "latitude"))

    @latitude.setter
    def latitude(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f75a217353731f29849770ffc9147724dd1ba4a0833a2eae6e9724a1ae1b8c12)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "latitude", value)

    @builtins.property
    @jsii.member(jsii_name="longitude")
    def longitude(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "longitude"))

    @longitude.setter
    def longitude(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04359a8061664a8b9e7ec6b0b027592be48fa6a057a32ca303c0ff33d6fec367)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "longitude", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21283b41d6857091da823d8dd00a04e31cd92ca76713a39d4f63683d5f5b27e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="ruleReference")
    def rule_reference(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ruleReference"))

    @rule_reference.setter
    def rule_reference(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__621c514e531523b5d043e2d2027be397ab781dfbdfa319ee3af60d8f3659b4c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleReference", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocation, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocation, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocation, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd4e718362896805021693049924d7f305bedce055e864894314f2f8af2ef8aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dataAwsRoute53TrafficPolicyDocument.DataAwsRoute53TrafficPolicyDocumentRuleItems",
    jsii_struct_bases=[],
    name_mapping={
        "endpoint_reference": "endpointReference",
        "health_check": "healthCheck",
    },
)
class DataAwsRoute53TrafficPolicyDocumentRuleItems:
    def __init__(
        self,
        *,
        endpoint_reference: typing.Optional[builtins.str] = None,
        health_check: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param endpoint_reference: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#endpoint_reference DataAwsRoute53TrafficPolicyDocument#endpoint_reference}.
        :param health_check: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#health_check DataAwsRoute53TrafficPolicyDocument#health_check}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bd7c427ee14bd3b866a9c8b3543c527ce42c514de6e2929854c1eb2d957944c)
            check_type(argname="argument endpoint_reference", value=endpoint_reference, expected_type=type_hints["endpoint_reference"])
            check_type(argname="argument health_check", value=health_check, expected_type=type_hints["health_check"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if endpoint_reference is not None:
            self._values["endpoint_reference"] = endpoint_reference
        if health_check is not None:
            self._values["health_check"] = health_check

    @builtins.property
    def endpoint_reference(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#endpoint_reference DataAwsRoute53TrafficPolicyDocument#endpoint_reference}.'''
        result = self._values.get("endpoint_reference")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def health_check(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#health_check DataAwsRoute53TrafficPolicyDocument#health_check}.'''
        result = self._values.get("health_check")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsRoute53TrafficPolicyDocumentRuleItems(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsRoute53TrafficPolicyDocumentRuleItemsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsRoute53TrafficPolicyDocument.DataAwsRoute53TrafficPolicyDocumentRuleItemsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c098158a7e9a941595c515ad569e45389a5af38276292f2523c51b4e42c62830)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAwsRoute53TrafficPolicyDocumentRuleItemsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82f2b43eb1ab99170e65f014384e953649b68bc2a63bf0a7cfe0af8c3b503466)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsRoute53TrafficPolicyDocumentRuleItemsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d11e11a3584a696a422e8a722a856bb5daf26481794375e39e5c29dfd215519)
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
            type_hints = typing.get_type_hints(_typecheckingstub__016a35242308a22fef532169cf08d71fb654509fd55175cc200ce622565feecf)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3105bb182e89a537658f0a21af7a5a39e4be4c190b7bca1ad5d0b0f6592d0145)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRuleItems]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRuleItems]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRuleItems]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__832e80b7d04e44fca96589337460626532711ca02d35d029cea6cc7525a35406)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAwsRoute53TrafficPolicyDocumentRuleItemsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsRoute53TrafficPolicyDocument.DataAwsRoute53TrafficPolicyDocumentRuleItemsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cd8b83228f0d22a22090e1263fe63a6854e81c7908a679bbbae9a8e839911e2d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetEndpointReference")
    def reset_endpoint_reference(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndpointReference", []))

    @jsii.member(jsii_name="resetHealthCheck")
    def reset_health_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheck", []))

    @builtins.property
    @jsii.member(jsii_name="endpointReferenceInput")
    def endpoint_reference_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointReferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckInput")
    def health_check_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "healthCheckInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointReference")
    def endpoint_reference(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpointReference"))

    @endpoint_reference.setter
    def endpoint_reference(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b8c0fd9dd354654d357d17f9204297d779bf326055af01a1d3a21348fb12128)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointReference", value)

    @builtins.property
    @jsii.member(jsii_name="healthCheck")
    def health_check(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "healthCheck"))

    @health_check.setter
    def health_check(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db25f982925fccc109293202f7caccd14e2e94e89c4adff0245352ab5fda0009)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthCheck", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleItems, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleItems, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleItems, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f1172d2a70a8d66bc6de11fc67ce080799e4f18e7c434e1e42cc9ed7a7ff964)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAwsRoute53TrafficPolicyDocumentRuleList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsRoute53TrafficPolicyDocument.DataAwsRoute53TrafficPolicyDocumentRuleList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__794b1f0c7238ff0c0e503516a715635363431bf3742177cadba9c676a100a429)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAwsRoute53TrafficPolicyDocumentRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__417a42119e1d636443ccaaf40fe0f937b2f67b0f2c5c1476b8f3c554837cf9cb)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsRoute53TrafficPolicyDocumentRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__075dff35f02dcf316dae79a4726bf1cb0b623b12c7ae9260ffe56793414b328b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__08fc93853405dd41fd2ac0b8db92e774ac2fa84959be5cc3e333c4411323f939)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0cac7e09e82dbf65fbe7037959cfb536f9d3e5485b33d7c302856834e7acf2ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRule]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ffe22c0a30455244e36ce37bbdab3834ed5bd5046e1a3ba030f800b740abf64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dataAwsRoute53TrafficPolicyDocument.DataAwsRoute53TrafficPolicyDocumentRuleLocation",
    jsii_struct_bases=[],
    name_mapping={
        "continent": "continent",
        "country": "country",
        "endpoint_reference": "endpointReference",
        "evaluate_target_health": "evaluateTargetHealth",
        "health_check": "healthCheck",
        "is_default": "isDefault",
        "rule_reference": "ruleReference",
        "subdivision": "subdivision",
    },
)
class DataAwsRoute53TrafficPolicyDocumentRuleLocation:
    def __init__(
        self,
        *,
        continent: typing.Optional[builtins.str] = None,
        country: typing.Optional[builtins.str] = None,
        endpoint_reference: typing.Optional[builtins.str] = None,
        evaluate_target_health: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        health_check: typing.Optional[builtins.str] = None,
        is_default: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        rule_reference: typing.Optional[builtins.str] = None,
        subdivision: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param continent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#continent DataAwsRoute53TrafficPolicyDocument#continent}.
        :param country: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#country DataAwsRoute53TrafficPolicyDocument#country}.
        :param endpoint_reference: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#endpoint_reference DataAwsRoute53TrafficPolicyDocument#endpoint_reference}.
        :param evaluate_target_health: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#evaluate_target_health DataAwsRoute53TrafficPolicyDocument#evaluate_target_health}.
        :param health_check: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#health_check DataAwsRoute53TrafficPolicyDocument#health_check}.
        :param is_default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#is_default DataAwsRoute53TrafficPolicyDocument#is_default}.
        :param rule_reference: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#rule_reference DataAwsRoute53TrafficPolicyDocument#rule_reference}.
        :param subdivision: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#subdivision DataAwsRoute53TrafficPolicyDocument#subdivision}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c9a3f9db233e132f7ef8ac28b7d46d8a3e96605dbdd8be2a423b3c0fc7c3484)
            check_type(argname="argument continent", value=continent, expected_type=type_hints["continent"])
            check_type(argname="argument country", value=country, expected_type=type_hints["country"])
            check_type(argname="argument endpoint_reference", value=endpoint_reference, expected_type=type_hints["endpoint_reference"])
            check_type(argname="argument evaluate_target_health", value=evaluate_target_health, expected_type=type_hints["evaluate_target_health"])
            check_type(argname="argument health_check", value=health_check, expected_type=type_hints["health_check"])
            check_type(argname="argument is_default", value=is_default, expected_type=type_hints["is_default"])
            check_type(argname="argument rule_reference", value=rule_reference, expected_type=type_hints["rule_reference"])
            check_type(argname="argument subdivision", value=subdivision, expected_type=type_hints["subdivision"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if continent is not None:
            self._values["continent"] = continent
        if country is not None:
            self._values["country"] = country
        if endpoint_reference is not None:
            self._values["endpoint_reference"] = endpoint_reference
        if evaluate_target_health is not None:
            self._values["evaluate_target_health"] = evaluate_target_health
        if health_check is not None:
            self._values["health_check"] = health_check
        if is_default is not None:
            self._values["is_default"] = is_default
        if rule_reference is not None:
            self._values["rule_reference"] = rule_reference
        if subdivision is not None:
            self._values["subdivision"] = subdivision

    @builtins.property
    def continent(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#continent DataAwsRoute53TrafficPolicyDocument#continent}.'''
        result = self._values.get("continent")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def country(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#country DataAwsRoute53TrafficPolicyDocument#country}.'''
        result = self._values.get("country")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def endpoint_reference(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#endpoint_reference DataAwsRoute53TrafficPolicyDocument#endpoint_reference}.'''
        result = self._values.get("endpoint_reference")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def evaluate_target_health(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#evaluate_target_health DataAwsRoute53TrafficPolicyDocument#evaluate_target_health}.'''
        result = self._values.get("evaluate_target_health")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def health_check(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#health_check DataAwsRoute53TrafficPolicyDocument#health_check}.'''
        result = self._values.get("health_check")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def is_default(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#is_default DataAwsRoute53TrafficPolicyDocument#is_default}.'''
        result = self._values.get("is_default")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def rule_reference(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#rule_reference DataAwsRoute53TrafficPolicyDocument#rule_reference}.'''
        result = self._values.get("rule_reference")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subdivision(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#subdivision DataAwsRoute53TrafficPolicyDocument#subdivision}.'''
        result = self._values.get("subdivision")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsRoute53TrafficPolicyDocumentRuleLocation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsRoute53TrafficPolicyDocumentRuleLocationList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsRoute53TrafficPolicyDocument.DataAwsRoute53TrafficPolicyDocumentRuleLocationList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a3f7ef9bd3dedbcbb697fb331fccfdf554281bd651a827bd33056d567c29f15f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAwsRoute53TrafficPolicyDocumentRuleLocationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa16f6515970c9e0e0dbc0ecbdb4e43bb85d2ff9c3b0d7990286eb4d77527196)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsRoute53TrafficPolicyDocumentRuleLocationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df08db3272b2e55e3694f76fb5f85f1aa53e5c81789e011152fe90968ed1bbd2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__45d97bc4a47e9cec9fcfe232bf5c0478d794df8ece423977a3647895fa04f56d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8a775f604c18c73a87e0ba2b9cc97d43e4df422c82c532fdd50d8e62fbc9d8f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRuleLocation]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRuleLocation]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRuleLocation]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b32752ae962f8c18cf65c10ed78bc15fa95c2af73d8457bde3ea4999732c18d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAwsRoute53TrafficPolicyDocumentRuleLocationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsRoute53TrafficPolicyDocument.DataAwsRoute53TrafficPolicyDocumentRuleLocationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__36d9d6a1ebb131b2df78337efd93713cabda9d648ab2bc7cf6bca2e81ac0a179)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetContinent")
    def reset_continent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContinent", []))

    @jsii.member(jsii_name="resetCountry")
    def reset_country(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCountry", []))

    @jsii.member(jsii_name="resetEndpointReference")
    def reset_endpoint_reference(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndpointReference", []))

    @jsii.member(jsii_name="resetEvaluateTargetHealth")
    def reset_evaluate_target_health(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEvaluateTargetHealth", []))

    @jsii.member(jsii_name="resetHealthCheck")
    def reset_health_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheck", []))

    @jsii.member(jsii_name="resetIsDefault")
    def reset_is_default(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsDefault", []))

    @jsii.member(jsii_name="resetRuleReference")
    def reset_rule_reference(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRuleReference", []))

    @jsii.member(jsii_name="resetSubdivision")
    def reset_subdivision(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubdivision", []))

    @builtins.property
    @jsii.member(jsii_name="continentInput")
    def continent_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "continentInput"))

    @builtins.property
    @jsii.member(jsii_name="countryInput")
    def country_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "countryInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointReferenceInput")
    def endpoint_reference_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointReferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="evaluateTargetHealthInput")
    def evaluate_target_health_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "evaluateTargetHealthInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckInput")
    def health_check_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "healthCheckInput"))

    @builtins.property
    @jsii.member(jsii_name="isDefaultInput")
    def is_default_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "isDefaultInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleReferenceInput")
    def rule_reference_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleReferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="subdivisionInput")
    def subdivision_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subdivisionInput"))

    @builtins.property
    @jsii.member(jsii_name="continent")
    def continent(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "continent"))

    @continent.setter
    def continent(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db957784a85ce8e91731115b9b12eb886a63c8f6cc784f979994c4219c65838c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "continent", value)

    @builtins.property
    @jsii.member(jsii_name="country")
    def country(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "country"))

    @country.setter
    def country(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1ec11d873e417be285ff6dbafcdbbb6cff62a3d215a931c3845a45ec8d540e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "country", value)

    @builtins.property
    @jsii.member(jsii_name="endpointReference")
    def endpoint_reference(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpointReference"))

    @endpoint_reference.setter
    def endpoint_reference(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f01ca62a5037dc10348d9fcf2bf059da2bb4795908beb454e74d3b6eb700a014)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointReference", value)

    @builtins.property
    @jsii.member(jsii_name="evaluateTargetHealth")
    def evaluate_target_health(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "evaluateTargetHealth"))

    @evaluate_target_health.setter
    def evaluate_target_health(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3aeec8033dccf363e785b89eaed2f13e223ac603a82498bec51c62f462a1fc1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluateTargetHealth", value)

    @builtins.property
    @jsii.member(jsii_name="healthCheck")
    def health_check(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "healthCheck"))

    @health_check.setter
    def health_check(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__225342ffd16aecf2ed56ba4ac1bd4dd021cb943000f474ee1ea0a56acd7609ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthCheck", value)

    @builtins.property
    @jsii.member(jsii_name="isDefault")
    def is_default(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "isDefault"))

    @is_default.setter
    def is_default(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fab5a7c43ee22e8deba4d13bacba9b0df58107d8c65493f01a5cd3097334cc5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isDefault", value)

    @builtins.property
    @jsii.member(jsii_name="ruleReference")
    def rule_reference(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ruleReference"))

    @rule_reference.setter
    def rule_reference(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e41b4ccd5680ed2329d8a7a09cdd8cda18572da339c02da4858886ee52bcf099)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleReference", value)

    @builtins.property
    @jsii.member(jsii_name="subdivision")
    def subdivision(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subdivision"))

    @subdivision.setter
    def subdivision(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c655a568cd925113fe2d4ad2fa226678a05f3ffd7c58f5a627006478da717788)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subdivision", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleLocation, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleLocation, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleLocation, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee4b9dbfaa438a85dfaf48aa1f76325b880bed8a8225c90de178bc6c777de86b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAwsRoute53TrafficPolicyDocumentRuleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsRoute53TrafficPolicyDocument.DataAwsRoute53TrafficPolicyDocumentRuleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7789022304d42581ef4bff1c7d4d641fc031b01690465cb166075ac992fa202c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putGeoProximityLocation")
    def put_geo_proximity_location(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocation, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34476b434e966bd549c85b186470c8794d205ebda400b2538a638c6910abf4bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putGeoProximityLocation", [value]))

    @jsii.member(jsii_name="putItems")
    def put_items(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleItems, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__181622b9ee30ba8d4a8545eb61579124a1e9ce0acc191da6be30f9ae10eb3869)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putItems", [value]))

    @jsii.member(jsii_name="putLocation")
    def put_location(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleLocation, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2c616fd7aefc251f555eac3313036ee080cd6f44ce97fb64aedd1434f670ee6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLocation", [value]))

    @jsii.member(jsii_name="putPrimary")
    def put_primary(
        self,
        *,
        endpoint_reference: typing.Optional[builtins.str] = None,
        evaluate_target_health: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        health_check: typing.Optional[builtins.str] = None,
        rule_reference: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param endpoint_reference: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#endpoint_reference DataAwsRoute53TrafficPolicyDocument#endpoint_reference}.
        :param evaluate_target_health: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#evaluate_target_health DataAwsRoute53TrafficPolicyDocument#evaluate_target_health}.
        :param health_check: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#health_check DataAwsRoute53TrafficPolicyDocument#health_check}.
        :param rule_reference: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#rule_reference DataAwsRoute53TrafficPolicyDocument#rule_reference}.
        '''
        value = DataAwsRoute53TrafficPolicyDocumentRulePrimary(
            endpoint_reference=endpoint_reference,
            evaluate_target_health=evaluate_target_health,
            health_check=health_check,
            rule_reference=rule_reference,
        )

        return typing.cast(None, jsii.invoke(self, "putPrimary", [value]))

    @jsii.member(jsii_name="putRegion")
    def put_region(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAwsRoute53TrafficPolicyDocumentRuleRegion", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65e4546d64000d18d0084d5e1e63a20e7662ec19074f916c627b8e69b88a9052)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRegion", [value]))

    @jsii.member(jsii_name="putSecondary")
    def put_secondary(
        self,
        *,
        endpoint_reference: typing.Optional[builtins.str] = None,
        evaluate_target_health: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        health_check: typing.Optional[builtins.str] = None,
        rule_reference: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param endpoint_reference: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#endpoint_reference DataAwsRoute53TrafficPolicyDocument#endpoint_reference}.
        :param evaluate_target_health: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#evaluate_target_health DataAwsRoute53TrafficPolicyDocument#evaluate_target_health}.
        :param health_check: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#health_check DataAwsRoute53TrafficPolicyDocument#health_check}.
        :param rule_reference: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#rule_reference DataAwsRoute53TrafficPolicyDocument#rule_reference}.
        '''
        value = DataAwsRoute53TrafficPolicyDocumentRuleSecondary(
            endpoint_reference=endpoint_reference,
            evaluate_target_health=evaluate_target_health,
            health_check=health_check,
            rule_reference=rule_reference,
        )

        return typing.cast(None, jsii.invoke(self, "putSecondary", [value]))

    @jsii.member(jsii_name="resetGeoProximityLocation")
    def reset_geo_proximity_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGeoProximityLocation", []))

    @jsii.member(jsii_name="resetItems")
    def reset_items(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetItems", []))

    @jsii.member(jsii_name="resetLocation")
    def reset_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocation", []))

    @jsii.member(jsii_name="resetPrimary")
    def reset_primary(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrimary", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetSecondary")
    def reset_secondary(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecondary", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="geoProximityLocation")
    def geo_proximity_location(
        self,
    ) -> DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocationList:
        return typing.cast(DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocationList, jsii.get(self, "geoProximityLocation"))

    @builtins.property
    @jsii.member(jsii_name="items")
    def items(self) -> DataAwsRoute53TrafficPolicyDocumentRuleItemsList:
        return typing.cast(DataAwsRoute53TrafficPolicyDocumentRuleItemsList, jsii.get(self, "items"))

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> DataAwsRoute53TrafficPolicyDocumentRuleLocationList:
        return typing.cast(DataAwsRoute53TrafficPolicyDocumentRuleLocationList, jsii.get(self, "location"))

    @builtins.property
    @jsii.member(jsii_name="primary")
    def primary(
        self,
    ) -> "DataAwsRoute53TrafficPolicyDocumentRulePrimaryOutputReference":
        return typing.cast("DataAwsRoute53TrafficPolicyDocumentRulePrimaryOutputReference", jsii.get(self, "primary"))

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> "DataAwsRoute53TrafficPolicyDocumentRuleRegionList":
        return typing.cast("DataAwsRoute53TrafficPolicyDocumentRuleRegionList", jsii.get(self, "region"))

    @builtins.property
    @jsii.member(jsii_name="secondary")
    def secondary(
        self,
    ) -> "DataAwsRoute53TrafficPolicyDocumentRuleSecondaryOutputReference":
        return typing.cast("DataAwsRoute53TrafficPolicyDocumentRuleSecondaryOutputReference", jsii.get(self, "secondary"))

    @builtins.property
    @jsii.member(jsii_name="geoProximityLocationInput")
    def geo_proximity_location_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocation]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocation]]], jsii.get(self, "geoProximityLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="itemsInput")
    def items_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRuleItems]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRuleItems]]], jsii.get(self, "itemsInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRuleLocation]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRuleLocation]]], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="primaryInput")
    def primary_input(
        self,
    ) -> typing.Optional["DataAwsRoute53TrafficPolicyDocumentRulePrimary"]:
        return typing.cast(typing.Optional["DataAwsRoute53TrafficPolicyDocumentRulePrimary"], jsii.get(self, "primaryInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAwsRoute53TrafficPolicyDocumentRuleRegion"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAwsRoute53TrafficPolicyDocumentRuleRegion"]]], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="secondaryInput")
    def secondary_input(
        self,
    ) -> typing.Optional["DataAwsRoute53TrafficPolicyDocumentRuleSecondary"]:
        return typing.cast(typing.Optional["DataAwsRoute53TrafficPolicyDocumentRuleSecondary"], jsii.get(self, "secondaryInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06983f2d16abb6e00b6068c380cf0c52a5639e2ac6ef5a9e537d831f97c7474f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__def1eac342f6d668e0ab5aefc21265c9c089caa3098def9b3acaf279bc50587f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentRule, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentRule, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentRule, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__300158ad59d5501c47ebf8ad1450f91c46864ff176c62604316687bf4ab843d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dataAwsRoute53TrafficPolicyDocument.DataAwsRoute53TrafficPolicyDocumentRulePrimary",
    jsii_struct_bases=[],
    name_mapping={
        "endpoint_reference": "endpointReference",
        "evaluate_target_health": "evaluateTargetHealth",
        "health_check": "healthCheck",
        "rule_reference": "ruleReference",
    },
)
class DataAwsRoute53TrafficPolicyDocumentRulePrimary:
    def __init__(
        self,
        *,
        endpoint_reference: typing.Optional[builtins.str] = None,
        evaluate_target_health: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        health_check: typing.Optional[builtins.str] = None,
        rule_reference: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param endpoint_reference: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#endpoint_reference DataAwsRoute53TrafficPolicyDocument#endpoint_reference}.
        :param evaluate_target_health: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#evaluate_target_health DataAwsRoute53TrafficPolicyDocument#evaluate_target_health}.
        :param health_check: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#health_check DataAwsRoute53TrafficPolicyDocument#health_check}.
        :param rule_reference: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#rule_reference DataAwsRoute53TrafficPolicyDocument#rule_reference}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6c38d10fea5f0395c51215d9d68d6b86c8dda4d2c59e89ad08be847da10bc7d)
            check_type(argname="argument endpoint_reference", value=endpoint_reference, expected_type=type_hints["endpoint_reference"])
            check_type(argname="argument evaluate_target_health", value=evaluate_target_health, expected_type=type_hints["evaluate_target_health"])
            check_type(argname="argument health_check", value=health_check, expected_type=type_hints["health_check"])
            check_type(argname="argument rule_reference", value=rule_reference, expected_type=type_hints["rule_reference"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if endpoint_reference is not None:
            self._values["endpoint_reference"] = endpoint_reference
        if evaluate_target_health is not None:
            self._values["evaluate_target_health"] = evaluate_target_health
        if health_check is not None:
            self._values["health_check"] = health_check
        if rule_reference is not None:
            self._values["rule_reference"] = rule_reference

    @builtins.property
    def endpoint_reference(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#endpoint_reference DataAwsRoute53TrafficPolicyDocument#endpoint_reference}.'''
        result = self._values.get("endpoint_reference")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def evaluate_target_health(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#evaluate_target_health DataAwsRoute53TrafficPolicyDocument#evaluate_target_health}.'''
        result = self._values.get("evaluate_target_health")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def health_check(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#health_check DataAwsRoute53TrafficPolicyDocument#health_check}.'''
        result = self._values.get("health_check")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rule_reference(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#rule_reference DataAwsRoute53TrafficPolicyDocument#rule_reference}.'''
        result = self._values.get("rule_reference")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsRoute53TrafficPolicyDocumentRulePrimary(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsRoute53TrafficPolicyDocumentRulePrimaryOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsRoute53TrafficPolicyDocument.DataAwsRoute53TrafficPolicyDocumentRulePrimaryOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__67bbd2eccd794b704b4ade9071adca5adb3b4e4db34dadef02b8c267e90e7070)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEndpointReference")
    def reset_endpoint_reference(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndpointReference", []))

    @jsii.member(jsii_name="resetEvaluateTargetHealth")
    def reset_evaluate_target_health(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEvaluateTargetHealth", []))

    @jsii.member(jsii_name="resetHealthCheck")
    def reset_health_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheck", []))

    @jsii.member(jsii_name="resetRuleReference")
    def reset_rule_reference(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRuleReference", []))

    @builtins.property
    @jsii.member(jsii_name="endpointReferenceInput")
    def endpoint_reference_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointReferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="evaluateTargetHealthInput")
    def evaluate_target_health_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "evaluateTargetHealthInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckInput")
    def health_check_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "healthCheckInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleReferenceInput")
    def rule_reference_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleReferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointReference")
    def endpoint_reference(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpointReference"))

    @endpoint_reference.setter
    def endpoint_reference(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee646207be266f915969592da2e7d6c69c00ee79d756e1c98ec4c372dff758a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointReference", value)

    @builtins.property
    @jsii.member(jsii_name="evaluateTargetHealth")
    def evaluate_target_health(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "evaluateTargetHealth"))

    @evaluate_target_health.setter
    def evaluate_target_health(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06be12a8aeaab2253b920419ed3626d094877656782476321436b0b189a032de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluateTargetHealth", value)

    @builtins.property
    @jsii.member(jsii_name="healthCheck")
    def health_check(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "healthCheck"))

    @health_check.setter
    def health_check(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09a8ed2f2b0f10f1fe24240fb91002932e090362d53db4b4a29f791bfb960daf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthCheck", value)

    @builtins.property
    @jsii.member(jsii_name="ruleReference")
    def rule_reference(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ruleReference"))

    @rule_reference.setter
    def rule_reference(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72c2f62576707296ea9ed213c91238702f860ed45a475bdaeca1d86bb14204e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleReference", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataAwsRoute53TrafficPolicyDocumentRulePrimary]:
        return typing.cast(typing.Optional[DataAwsRoute53TrafficPolicyDocumentRulePrimary], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsRoute53TrafficPolicyDocumentRulePrimary],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11191eec36bc3cc5c189076442a188758e23cae839dcfb1db6df0bea695eee7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dataAwsRoute53TrafficPolicyDocument.DataAwsRoute53TrafficPolicyDocumentRuleRegion",
    jsii_struct_bases=[],
    name_mapping={
        "endpoint_reference": "endpointReference",
        "evaluate_target_health": "evaluateTargetHealth",
        "health_check": "healthCheck",
        "region": "region",
        "rule_reference": "ruleReference",
    },
)
class DataAwsRoute53TrafficPolicyDocumentRuleRegion:
    def __init__(
        self,
        *,
        endpoint_reference: typing.Optional[builtins.str] = None,
        evaluate_target_health: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        health_check: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        rule_reference: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param endpoint_reference: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#endpoint_reference DataAwsRoute53TrafficPolicyDocument#endpoint_reference}.
        :param evaluate_target_health: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#evaluate_target_health DataAwsRoute53TrafficPolicyDocument#evaluate_target_health}.
        :param health_check: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#health_check DataAwsRoute53TrafficPolicyDocument#health_check}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#region DataAwsRoute53TrafficPolicyDocument#region}.
        :param rule_reference: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#rule_reference DataAwsRoute53TrafficPolicyDocument#rule_reference}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b47213b714adbf2a8946c80105b7d9005b4fadf0c37a4b530a851f3406f15781)
            check_type(argname="argument endpoint_reference", value=endpoint_reference, expected_type=type_hints["endpoint_reference"])
            check_type(argname="argument evaluate_target_health", value=evaluate_target_health, expected_type=type_hints["evaluate_target_health"])
            check_type(argname="argument health_check", value=health_check, expected_type=type_hints["health_check"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument rule_reference", value=rule_reference, expected_type=type_hints["rule_reference"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if endpoint_reference is not None:
            self._values["endpoint_reference"] = endpoint_reference
        if evaluate_target_health is not None:
            self._values["evaluate_target_health"] = evaluate_target_health
        if health_check is not None:
            self._values["health_check"] = health_check
        if region is not None:
            self._values["region"] = region
        if rule_reference is not None:
            self._values["rule_reference"] = rule_reference

    @builtins.property
    def endpoint_reference(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#endpoint_reference DataAwsRoute53TrafficPolicyDocument#endpoint_reference}.'''
        result = self._values.get("endpoint_reference")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def evaluate_target_health(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#evaluate_target_health DataAwsRoute53TrafficPolicyDocument#evaluate_target_health}.'''
        result = self._values.get("evaluate_target_health")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def health_check(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#health_check DataAwsRoute53TrafficPolicyDocument#health_check}.'''
        result = self._values.get("health_check")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#region DataAwsRoute53TrafficPolicyDocument#region}.'''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rule_reference(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#rule_reference DataAwsRoute53TrafficPolicyDocument#rule_reference}.'''
        result = self._values.get("rule_reference")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsRoute53TrafficPolicyDocumentRuleRegion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsRoute53TrafficPolicyDocumentRuleRegionList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsRoute53TrafficPolicyDocument.DataAwsRoute53TrafficPolicyDocumentRuleRegionList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1e8245b3b2af449bf4eadc7e15de091c938dd68c4baf0a5a8906840bfd8c0818)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAwsRoute53TrafficPolicyDocumentRuleRegionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b49bdbe2f2ea911b5c965d8257dd5ff1f58a0fe32b608e1f95fc06239de360ae)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsRoute53TrafficPolicyDocumentRuleRegionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c25b2d3ac22c15202c449876e67232a4268081efd280f52582768bce1ccd55f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cdee584ccd82642b0de62d7c86bbd2433399ec3ad6094c7220180fef9d1e80a1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4a63c985380741a9f7e1e8ac658a74cac5796fbe00a9001459611dd8a6c16753)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRuleRegion]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRuleRegion]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRuleRegion]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27a1dda0e91d8ec824440829e2fd6016394ef0e5628f019d8e089ef19e0c73b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAwsRoute53TrafficPolicyDocumentRuleRegionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsRoute53TrafficPolicyDocument.DataAwsRoute53TrafficPolicyDocumentRuleRegionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__69b943c301b3c2be697ffb3dc128f18804adc9948d44e91d256e6304e9da22c2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetEndpointReference")
    def reset_endpoint_reference(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndpointReference", []))

    @jsii.member(jsii_name="resetEvaluateTargetHealth")
    def reset_evaluate_target_health(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEvaluateTargetHealth", []))

    @jsii.member(jsii_name="resetHealthCheck")
    def reset_health_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheck", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetRuleReference")
    def reset_rule_reference(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRuleReference", []))

    @builtins.property
    @jsii.member(jsii_name="endpointReferenceInput")
    def endpoint_reference_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointReferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="evaluateTargetHealthInput")
    def evaluate_target_health_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "evaluateTargetHealthInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckInput")
    def health_check_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "healthCheckInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleReferenceInput")
    def rule_reference_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleReferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointReference")
    def endpoint_reference(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpointReference"))

    @endpoint_reference.setter
    def endpoint_reference(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3844963672f97bd58576a795bd63703e5b5f3114b9f38117bc26c7d8fa5168e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointReference", value)

    @builtins.property
    @jsii.member(jsii_name="evaluateTargetHealth")
    def evaluate_target_health(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "evaluateTargetHealth"))

    @evaluate_target_health.setter
    def evaluate_target_health(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3810d128a2f8e41107b97579bcace69cbf2e3c8fd35b0d7b0b544d351890375)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluateTargetHealth", value)

    @builtins.property
    @jsii.member(jsii_name="healthCheck")
    def health_check(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "healthCheck"))

    @health_check.setter
    def health_check(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14961ffc0d13c982208927b13086a0e0f3b89b53ca1f3bfebf8d5b740e3031f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthCheck", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db91680867994f133e91674d3ac007386f0a4d00a75b82af965fff20d7721e0e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="ruleReference")
    def rule_reference(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ruleReference"))

    @rule_reference.setter
    def rule_reference(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__948a747b752c980b7180a83548c7443e6e423d0dd28ca042d660be363e12b588)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleReference", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleRegion, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleRegion, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleRegion, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4dbc8b0500e73ba8ff07119363012e1388bc3f565f8ecd3fe7f4c8b996c49d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dataAwsRoute53TrafficPolicyDocument.DataAwsRoute53TrafficPolicyDocumentRuleSecondary",
    jsii_struct_bases=[],
    name_mapping={
        "endpoint_reference": "endpointReference",
        "evaluate_target_health": "evaluateTargetHealth",
        "health_check": "healthCheck",
        "rule_reference": "ruleReference",
    },
)
class DataAwsRoute53TrafficPolicyDocumentRuleSecondary:
    def __init__(
        self,
        *,
        endpoint_reference: typing.Optional[builtins.str] = None,
        evaluate_target_health: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        health_check: typing.Optional[builtins.str] = None,
        rule_reference: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param endpoint_reference: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#endpoint_reference DataAwsRoute53TrafficPolicyDocument#endpoint_reference}.
        :param evaluate_target_health: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#evaluate_target_health DataAwsRoute53TrafficPolicyDocument#evaluate_target_health}.
        :param health_check: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#health_check DataAwsRoute53TrafficPolicyDocument#health_check}.
        :param rule_reference: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#rule_reference DataAwsRoute53TrafficPolicyDocument#rule_reference}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fde2432e0ddd4e3344df03812ce2f8029096a7518d894f4ea753728474a7668)
            check_type(argname="argument endpoint_reference", value=endpoint_reference, expected_type=type_hints["endpoint_reference"])
            check_type(argname="argument evaluate_target_health", value=evaluate_target_health, expected_type=type_hints["evaluate_target_health"])
            check_type(argname="argument health_check", value=health_check, expected_type=type_hints["health_check"])
            check_type(argname="argument rule_reference", value=rule_reference, expected_type=type_hints["rule_reference"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if endpoint_reference is not None:
            self._values["endpoint_reference"] = endpoint_reference
        if evaluate_target_health is not None:
            self._values["evaluate_target_health"] = evaluate_target_health
        if health_check is not None:
            self._values["health_check"] = health_check
        if rule_reference is not None:
            self._values["rule_reference"] = rule_reference

    @builtins.property
    def endpoint_reference(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#endpoint_reference DataAwsRoute53TrafficPolicyDocument#endpoint_reference}.'''
        result = self._values.get("endpoint_reference")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def evaluate_target_health(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#evaluate_target_health DataAwsRoute53TrafficPolicyDocument#evaluate_target_health}.'''
        result = self._values.get("evaluate_target_health")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def health_check(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#health_check DataAwsRoute53TrafficPolicyDocument#health_check}.'''
        result = self._values.get("health_check")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rule_reference(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#rule_reference DataAwsRoute53TrafficPolicyDocument#rule_reference}.'''
        result = self._values.get("rule_reference")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsRoute53TrafficPolicyDocumentRuleSecondary(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsRoute53TrafficPolicyDocumentRuleSecondaryOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsRoute53TrafficPolicyDocument.DataAwsRoute53TrafficPolicyDocumentRuleSecondaryOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b44afd0d2a362a007b66743d5b258ea1c469491b762058fc9aeba1a71cf31b8e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEndpointReference")
    def reset_endpoint_reference(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndpointReference", []))

    @jsii.member(jsii_name="resetEvaluateTargetHealth")
    def reset_evaluate_target_health(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEvaluateTargetHealth", []))

    @jsii.member(jsii_name="resetHealthCheck")
    def reset_health_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheck", []))

    @jsii.member(jsii_name="resetRuleReference")
    def reset_rule_reference(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRuleReference", []))

    @builtins.property
    @jsii.member(jsii_name="endpointReferenceInput")
    def endpoint_reference_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointReferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="evaluateTargetHealthInput")
    def evaluate_target_health_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "evaluateTargetHealthInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckInput")
    def health_check_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "healthCheckInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleReferenceInput")
    def rule_reference_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleReferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointReference")
    def endpoint_reference(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpointReference"))

    @endpoint_reference.setter
    def endpoint_reference(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__879a8a606104fc502c30a6886351a31a42615d6902ccf9b4bd7d250c9db2eb6a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointReference", value)

    @builtins.property
    @jsii.member(jsii_name="evaluateTargetHealth")
    def evaluate_target_health(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "evaluateTargetHealth"))

    @evaluate_target_health.setter
    def evaluate_target_health(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9531523c5d62c7468f9c361af37daad610d2eafc016a5ff56f9073e3469229ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluateTargetHealth", value)

    @builtins.property
    @jsii.member(jsii_name="healthCheck")
    def health_check(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "healthCheck"))

    @health_check.setter
    def health_check(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d122e2fb24fd9c0ac1faec1f3baecba73883af67c2a8ba973777e035ad3e52f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthCheck", value)

    @builtins.property
    @jsii.member(jsii_name="ruleReference")
    def rule_reference(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ruleReference"))

    @rule_reference.setter
    def rule_reference(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16197771fe680cf056d512feef6d60553766d17446207c9e56224c890407c2b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleReference", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataAwsRoute53TrafficPolicyDocumentRuleSecondary]:
        return typing.cast(typing.Optional[DataAwsRoute53TrafficPolicyDocumentRuleSecondary], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsRoute53TrafficPolicyDocumentRuleSecondary],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac556c6c1bfb34126c1ace7896524cd7fdb501b0cf064d44df46f26006a714f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataAwsRoute53TrafficPolicyDocument",
    "DataAwsRoute53TrafficPolicyDocumentConfig",
    "DataAwsRoute53TrafficPolicyDocumentEndpoint",
    "DataAwsRoute53TrafficPolicyDocumentEndpointList",
    "DataAwsRoute53TrafficPolicyDocumentEndpointOutputReference",
    "DataAwsRoute53TrafficPolicyDocumentRule",
    "DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocation",
    "DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocationList",
    "DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocationOutputReference",
    "DataAwsRoute53TrafficPolicyDocumentRuleItems",
    "DataAwsRoute53TrafficPolicyDocumentRuleItemsList",
    "DataAwsRoute53TrafficPolicyDocumentRuleItemsOutputReference",
    "DataAwsRoute53TrafficPolicyDocumentRuleList",
    "DataAwsRoute53TrafficPolicyDocumentRuleLocation",
    "DataAwsRoute53TrafficPolicyDocumentRuleLocationList",
    "DataAwsRoute53TrafficPolicyDocumentRuleLocationOutputReference",
    "DataAwsRoute53TrafficPolicyDocumentRuleOutputReference",
    "DataAwsRoute53TrafficPolicyDocumentRulePrimary",
    "DataAwsRoute53TrafficPolicyDocumentRulePrimaryOutputReference",
    "DataAwsRoute53TrafficPolicyDocumentRuleRegion",
    "DataAwsRoute53TrafficPolicyDocumentRuleRegionList",
    "DataAwsRoute53TrafficPolicyDocumentRuleRegionOutputReference",
    "DataAwsRoute53TrafficPolicyDocumentRuleSecondary",
    "DataAwsRoute53TrafficPolicyDocumentRuleSecondaryOutputReference",
]

publication.publish()

def _typecheckingstub__d48e72b418e7a7f5063db6316c8a8a4004e66203a6481abbe5dd4f9a9f24278f(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    endpoint: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAwsRoute53TrafficPolicyDocumentEndpoint, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
    record_type: typing.Optional[builtins.str] = None,
    rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAwsRoute53TrafficPolicyDocumentRule, typing.Dict[builtins.str, typing.Any]]]]] = None,
    start_endpoint: typing.Optional[builtins.str] = None,
    start_rule: typing.Optional[builtins.str] = None,
    version: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__e77d05da1791f609edce33c6ba3e3b4a5951fb71f5a2df3a21e15eb906662f3b(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAwsRoute53TrafficPolicyDocumentEndpoint, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82ccaac1123f6547004a0141500bb522ac5a9262c2878659dfeab71b0788ffb9(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAwsRoute53TrafficPolicyDocumentRule, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__996212dbe341ce1d1d7521f4270f381dd61dc4d789714440546cb292584b907a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b50ca844576cacfda3324a0633e1a4d4455d3da6975b87be1f604068a73c5a44(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28fcfbbb7eb3d1f6c3d21f73a4ab757f05350c08816c4a778f789a53d990937e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00f3ddbd0b4b062f446c109ff69592488a203c81dc2fee13c9f54151a96faefb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0db052b00a7ae5a9721ce8d12005c7cc51b72a0d87c2ebb7dcd7f27370d14f1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c624bc1f93272d22113873c8ad7a050090cc8d5af033a2d0c71a033bbe2e19a(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    endpoint: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAwsRoute53TrafficPolicyDocumentEndpoint, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
    record_type: typing.Optional[builtins.str] = None,
    rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAwsRoute53TrafficPolicyDocumentRule, typing.Dict[builtins.str, typing.Any]]]]] = None,
    start_endpoint: typing.Optional[builtins.str] = None,
    start_rule: typing.Optional[builtins.str] = None,
    version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__929b31c22f3d006046203acecaaf878d22a62ae5a91ad7dc3cf9da50aca75183(
    *,
    id: builtins.str,
    region: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d476e55ffeb1f2960c70b00a2fc20e2b5bc6469543d3b58eb31bfa036c2f3f2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbcc0f67b3f856d823d8255cc3eecedf4902c0acecc9a4ef944eb891c46ae7d0(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51aac8f3fd8dc17604d88db5f621f78bec0d937c910a76a3b9f26b1948a75bc1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de8c22b8444df58373a799db4d166fea3b580ece4754c0c7ae5821511b1d9014(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f32a6dea06cf668874055432ff32c40b22061c3188d8ba4890529812e285630a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3cfaf8a0a334c4664ccd3ad00edb9bf547f96ca41da7940918c508ba171a59b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentEndpoint]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea1a4b61639af922d2892e89e15f09a3c226a79f08ead76673861d518df544e3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21de70a313339e3c573d54830aebc7d337489d5409f0ad7f471dc4212aaf156a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35f6e85cd0f97d8c1e2f8877f82e01f605c8dae222e692f0f05ef5bed02668c2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29a52f0fb448c41260916bb164041624f003c7bd8598923db87761e142e4ce82(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58c4e05fa8dbe56acd2e4d3d34944848b9565301d8230e0e59d5162bf660b9ec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4b333b74589f110fdfe23cc590d4f7fa0d7cde39eb2d398e6eb25d1d474262d(
    value: typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentEndpoint, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee0a9e7452eba07e239c78ecbef581d90f2e0a53dcf1d19c99eaba6c39de6e57(
    *,
    id: builtins.str,
    geo_proximity_location: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocation, typing.Dict[builtins.str, typing.Any]]]]] = None,
    items: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleItems, typing.Dict[builtins.str, typing.Any]]]]] = None,
    location: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleLocation, typing.Dict[builtins.str, typing.Any]]]]] = None,
    primary: typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentRulePrimary, typing.Dict[builtins.str, typing.Any]]] = None,
    region: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleRegion, typing.Dict[builtins.str, typing.Any]]]]] = None,
    secondary: typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleSecondary, typing.Dict[builtins.str, typing.Any]]] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1b5791f89a54630a8b22d4fc76b15f0383490770f1b281f278934fb725c3509(
    *,
    bias: typing.Optional[builtins.str] = None,
    endpoint_reference: typing.Optional[builtins.str] = None,
    evaluate_target_health: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    health_check: typing.Optional[builtins.str] = None,
    latitude: typing.Optional[builtins.str] = None,
    longitude: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    rule_reference: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e1f1edbd81627c746ae850624c9b8d52a879797476e3bc6dcd0d92cd754cb3a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10cae2a0de7404cd016012efc862272bf25639217ac80eb28ad9e57c5b03acd4(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf77bbe65cbb14b8d2c647411c2d577d3a5bc9c8f3d1947304b438143a2c2745(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb93db689c1e3cc6967aea84fa3e6fa4ed53e4b7e271b75dc10a7a313cf66b89(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__438cf4bd18b6a2814225d3c6647a59512df51bb10b93f7ab2e0b7fe1d302be62(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf97a2383724692039c51c6a9efedee5f00512a8c190ee8c2e112c18e29a8c4c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocation]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74c5290503d4cce73eecc2bb3656863a511d1a505e148934d3f6c891bb8fa9c7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e92cac29ee9a311d557895e99d25ffa9dda73ff3bdeb21c7710eff6d066d988(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7ecfc60c8b359d8a51cf5b4913cacd668562423a3d495c44b71d473484c1bbf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e355f0f97c54bf5f29c951384924ac66894b636dfd693b9b9a3e2422dcd0cd9a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0d747fe7737a0187d6ce0a06b9063a0ae1d71b7a710b8ecca4f3882a4173044(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f75a217353731f29849770ffc9147724dd1ba4a0833a2eae6e9724a1ae1b8c12(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04359a8061664a8b9e7ec6b0b027592be48fa6a057a32ca303c0ff33d6fec367(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21283b41d6857091da823d8dd00a04e31cd92ca76713a39d4f63683d5f5b27e1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__621c514e531523b5d043e2d2027be397ab781dfbdfa319ee3af60d8f3659b4c6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd4e718362896805021693049924d7f305bedce055e864894314f2f8af2ef8aa(
    value: typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocation, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bd7c427ee14bd3b866a9c8b3543c527ce42c514de6e2929854c1eb2d957944c(
    *,
    endpoint_reference: typing.Optional[builtins.str] = None,
    health_check: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c098158a7e9a941595c515ad569e45389a5af38276292f2523c51b4e42c62830(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82f2b43eb1ab99170e65f014384e953649b68bc2a63bf0a7cfe0af8c3b503466(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d11e11a3584a696a422e8a722a856bb5daf26481794375e39e5c29dfd215519(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__016a35242308a22fef532169cf08d71fb654509fd55175cc200ce622565feecf(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3105bb182e89a537658f0a21af7a5a39e4be4c190b7bca1ad5d0b0f6592d0145(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__832e80b7d04e44fca96589337460626532711ca02d35d029cea6cc7525a35406(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRuleItems]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd8b83228f0d22a22090e1263fe63a6854e81c7908a679bbbae9a8e839911e2d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b8c0fd9dd354654d357d17f9204297d779bf326055af01a1d3a21348fb12128(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db25f982925fccc109293202f7caccd14e2e94e89c4adff0245352ab5fda0009(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f1172d2a70a8d66bc6de11fc67ce080799e4f18e7c434e1e42cc9ed7a7ff964(
    value: typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleItems, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__794b1f0c7238ff0c0e503516a715635363431bf3742177cadba9c676a100a429(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__417a42119e1d636443ccaaf40fe0f937b2f67b0f2c5c1476b8f3c554837cf9cb(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__075dff35f02dcf316dae79a4726bf1cb0b623b12c7ae9260ffe56793414b328b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08fc93853405dd41fd2ac0b8db92e774ac2fa84959be5cc3e333c4411323f939(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cac7e09e82dbf65fbe7037959cfb536f9d3e5485b33d7c302856834e7acf2ce(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ffe22c0a30455244e36ce37bbdab3834ed5bd5046e1a3ba030f800b740abf64(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRule]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c9a3f9db233e132f7ef8ac28b7d46d8a3e96605dbdd8be2a423b3c0fc7c3484(
    *,
    continent: typing.Optional[builtins.str] = None,
    country: typing.Optional[builtins.str] = None,
    endpoint_reference: typing.Optional[builtins.str] = None,
    evaluate_target_health: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    health_check: typing.Optional[builtins.str] = None,
    is_default: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    rule_reference: typing.Optional[builtins.str] = None,
    subdivision: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3f7ef9bd3dedbcbb697fb331fccfdf554281bd651a827bd33056d567c29f15f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa16f6515970c9e0e0dbc0ecbdb4e43bb85d2ff9c3b0d7990286eb4d77527196(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df08db3272b2e55e3694f76fb5f85f1aa53e5c81789e011152fe90968ed1bbd2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45d97bc4a47e9cec9fcfe232bf5c0478d794df8ece423977a3647895fa04f56d(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a775f604c18c73a87e0ba2b9cc97d43e4df422c82c532fdd50d8e62fbc9d8f7(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b32752ae962f8c18cf65c10ed78bc15fa95c2af73d8457bde3ea4999732c18d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRuleLocation]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36d9d6a1ebb131b2df78337efd93713cabda9d648ab2bc7cf6bca2e81ac0a179(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db957784a85ce8e91731115b9b12eb886a63c8f6cc784f979994c4219c65838c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1ec11d873e417be285ff6dbafcdbbb6cff62a3d215a931c3845a45ec8d540e6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f01ca62a5037dc10348d9fcf2bf059da2bb4795908beb454e74d3b6eb700a014(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3aeec8033dccf363e785b89eaed2f13e223ac603a82498bec51c62f462a1fc1(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__225342ffd16aecf2ed56ba4ac1bd4dd021cb943000f474ee1ea0a56acd7609ae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fab5a7c43ee22e8deba4d13bacba9b0df58107d8c65493f01a5cd3097334cc5(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e41b4ccd5680ed2329d8a7a09cdd8cda18572da339c02da4858886ee52bcf099(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c655a568cd925113fe2d4ad2fa226678a05f3ffd7c58f5a627006478da717788(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee4b9dbfaa438a85dfaf48aa1f76325b880bed8a8225c90de178bc6c777de86b(
    value: typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleLocation, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7789022304d42581ef4bff1c7d4d641fc031b01690465cb166075ac992fa202c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34476b434e966bd549c85b186470c8794d205ebda400b2538a638c6910abf4bb(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocation, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__181622b9ee30ba8d4a8545eb61579124a1e9ce0acc191da6be30f9ae10eb3869(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleItems, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2c616fd7aefc251f555eac3313036ee080cd6f44ce97fb64aedd1434f670ee6(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleLocation, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65e4546d64000d18d0084d5e1e63a20e7662ec19074f916c627b8e69b88a9052(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleRegion, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06983f2d16abb6e00b6068c380cf0c52a5639e2ac6ef5a9e537d831f97c7474f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__def1eac342f6d668e0ab5aefc21265c9c089caa3098def9b3acaf279bc50587f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__300158ad59d5501c47ebf8ad1450f91c46864ff176c62604316687bf4ab843d3(
    value: typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentRule, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6c38d10fea5f0395c51215d9d68d6b86c8dda4d2c59e89ad08be847da10bc7d(
    *,
    endpoint_reference: typing.Optional[builtins.str] = None,
    evaluate_target_health: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    health_check: typing.Optional[builtins.str] = None,
    rule_reference: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67bbd2eccd794b704b4ade9071adca5adb3b4e4db34dadef02b8c267e90e7070(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee646207be266f915969592da2e7d6c69c00ee79d756e1c98ec4c372dff758a2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06be12a8aeaab2253b920419ed3626d094877656782476321436b0b189a032de(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09a8ed2f2b0f10f1fe24240fb91002932e090362d53db4b4a29f791bfb960daf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72c2f62576707296ea9ed213c91238702f860ed45a475bdaeca1d86bb14204e2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11191eec36bc3cc5c189076442a188758e23cae839dcfb1db6df0bea695eee7b(
    value: typing.Optional[DataAwsRoute53TrafficPolicyDocumentRulePrimary],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b47213b714adbf2a8946c80105b7d9005b4fadf0c37a4b530a851f3406f15781(
    *,
    endpoint_reference: typing.Optional[builtins.str] = None,
    evaluate_target_health: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    health_check: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    rule_reference: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e8245b3b2af449bf4eadc7e15de091c938dd68c4baf0a5a8906840bfd8c0818(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b49bdbe2f2ea911b5c965d8257dd5ff1f58a0fe32b608e1f95fc06239de360ae(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c25b2d3ac22c15202c449876e67232a4268081efd280f52582768bce1ccd55f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdee584ccd82642b0de62d7c86bbd2433399ec3ad6094c7220180fef9d1e80a1(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a63c985380741a9f7e1e8ac658a74cac5796fbe00a9001459611dd8a6c16753(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27a1dda0e91d8ec824440829e2fd6016394ef0e5628f019d8e089ef19e0c73b6(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRuleRegion]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69b943c301b3c2be697ffb3dc128f18804adc9948d44e91d256e6304e9da22c2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3844963672f97bd58576a795bd63703e5b5f3114b9f38117bc26c7d8fa5168e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3810d128a2f8e41107b97579bcace69cbf2e3c8fd35b0d7b0b544d351890375(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14961ffc0d13c982208927b13086a0e0f3b89b53ca1f3bfebf8d5b740e3031f5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db91680867994f133e91674d3ac007386f0a4d00a75b82af965fff20d7721e0e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__948a747b752c980b7180a83548c7443e6e423d0dd28ca042d660be363e12b588(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4dbc8b0500e73ba8ff07119363012e1388bc3f565f8ecd3fe7f4c8b996c49d4(
    value: typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleRegion, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fde2432e0ddd4e3344df03812ce2f8029096a7518d894f4ea753728474a7668(
    *,
    endpoint_reference: typing.Optional[builtins.str] = None,
    evaluate_target_health: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    health_check: typing.Optional[builtins.str] = None,
    rule_reference: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b44afd0d2a362a007b66743d5b258ea1c469491b762058fc9aeba1a71cf31b8e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__879a8a606104fc502c30a6886351a31a42615d6902ccf9b4bd7d250c9db2eb6a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9531523c5d62c7468f9c361af37daad610d2eafc016a5ff56f9073e3469229ba(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d122e2fb24fd9c0ac1faec1f3baecba73883af67c2a8ba973777e035ad3e52f9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16197771fe680cf056d512feef6d60553766d17446207c9e56224c890407c2b1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac556c6c1bfb34126c1ace7896524cd7fdb501b0cf064d44df46f26006a714f4(
    value: typing.Optional[DataAwsRoute53TrafficPolicyDocumentRuleSecondary],
) -> None:
    """Type checking stubs"""
    pass
