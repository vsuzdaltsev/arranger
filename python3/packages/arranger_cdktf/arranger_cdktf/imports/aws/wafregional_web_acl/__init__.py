'''
# `aws_wafregional_web_acl`

Refer to the Terraform Registory for docs: [`aws_wafregional_web_acl`](https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl).
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


class WafregionalWebAcl(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.wafregionalWebAcl.WafregionalWebAcl",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl aws_wafregional_web_acl}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        default_action: typing.Union["WafregionalWebAclDefaultAction", typing.Dict[builtins.str, typing.Any]],
        metric_name: builtins.str,
        name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        logging_configuration: typing.Optional[typing.Union["WafregionalWebAclLoggingConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WafregionalWebAclRule", typing.Dict[builtins.str, typing.Any]]]]] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl aws_wafregional_web_acl} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param default_action: default_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#default_action WafregionalWebAcl#default_action}
        :param metric_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#metric_name WafregionalWebAcl#metric_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#name WafregionalWebAcl#name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#id WafregionalWebAcl#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param logging_configuration: logging_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#logging_configuration WafregionalWebAcl#logging_configuration}
        :param rule: rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#rule WafregionalWebAcl#rule}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#tags WafregionalWebAcl#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#tags_all WafregionalWebAcl#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__135bad191b2b5f79f840059c059793d08a523197218a2ca16ddc83530026dd5b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = WafregionalWebAclConfig(
            default_action=default_action,
            metric_name=metric_name,
            name=name,
            id=id,
            logging_configuration=logging_configuration,
            rule=rule,
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

    @jsii.member(jsii_name="putDefaultAction")
    def put_default_action(self, *, type: builtins.str) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#type WafregionalWebAcl#type}.
        '''
        value = WafregionalWebAclDefaultAction(type=type)

        return typing.cast(None, jsii.invoke(self, "putDefaultAction", [value]))

    @jsii.member(jsii_name="putLoggingConfiguration")
    def put_logging_configuration(
        self,
        *,
        log_destination: builtins.str,
        redacted_fields: typing.Optional[typing.Union["WafregionalWebAclLoggingConfigurationRedactedFields", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param log_destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#log_destination WafregionalWebAcl#log_destination}.
        :param redacted_fields: redacted_fields block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#redacted_fields WafregionalWebAcl#redacted_fields}
        '''
        value = WafregionalWebAclLoggingConfiguration(
            log_destination=log_destination, redacted_fields=redacted_fields
        )

        return typing.cast(None, jsii.invoke(self, "putLoggingConfiguration", [value]))

    @jsii.member(jsii_name="putRule")
    def put_rule(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WafregionalWebAclRule", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__727fc6862273319ae07013d0fff3d4c413fdf367412abc7e03a3644c827c684b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRule", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLoggingConfiguration")
    def reset_logging_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoggingConfiguration", []))

    @jsii.member(jsii_name="resetRule")
    def reset_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRule", []))

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
    @jsii.member(jsii_name="defaultAction")
    def default_action(self) -> "WafregionalWebAclDefaultActionOutputReference":
        return typing.cast("WafregionalWebAclDefaultActionOutputReference", jsii.get(self, "defaultAction"))

    @builtins.property
    @jsii.member(jsii_name="loggingConfiguration")
    def logging_configuration(
        self,
    ) -> "WafregionalWebAclLoggingConfigurationOutputReference":
        return typing.cast("WafregionalWebAclLoggingConfigurationOutputReference", jsii.get(self, "loggingConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> "WafregionalWebAclRuleList":
        return typing.cast("WafregionalWebAclRuleList", jsii.get(self, "rule"))

    @builtins.property
    @jsii.member(jsii_name="defaultActionInput")
    def default_action_input(self) -> typing.Optional["WafregionalWebAclDefaultAction"]:
        return typing.cast(typing.Optional["WafregionalWebAclDefaultAction"], jsii.get(self, "defaultActionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="loggingConfigurationInput")
    def logging_configuration_input(
        self,
    ) -> typing.Optional["WafregionalWebAclLoggingConfiguration"]:
        return typing.cast(typing.Optional["WafregionalWebAclLoggingConfiguration"], jsii.get(self, "loggingConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="metricNameInput")
    def metric_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricNameInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WafregionalWebAclRule"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WafregionalWebAclRule"]]], jsii.get(self, "ruleInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__06783766af99297a736c770c41ac037e2915cb7df4c7f8b49a1075c0239fc35d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="metricName")
    def metric_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricName"))

    @metric_name.setter
    def metric_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e852d410fc6858bfcecbf4dd24f1cf1abfda64b39338204ab407d3d30ce6bbd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricName", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fea5408ce9c0fd45f4ad076292b9a040d00e7fb4ef21cd07afb61e5b004b125d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af2ce43e7b7340dff533be4061d07760cb1d954259c70fc3f3e4dee0b6a38936)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f67231310b712ffcce8907103016f1955bb7f96198c89605374b1215d295064)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.wafregionalWebAcl.WafregionalWebAclConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "default_action": "defaultAction",
        "metric_name": "metricName",
        "name": "name",
        "id": "id",
        "logging_configuration": "loggingConfiguration",
        "rule": "rule",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class WafregionalWebAclConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        default_action: typing.Union["WafregionalWebAclDefaultAction", typing.Dict[builtins.str, typing.Any]],
        metric_name: builtins.str,
        name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        logging_configuration: typing.Optional[typing.Union["WafregionalWebAclLoggingConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WafregionalWebAclRule", typing.Dict[builtins.str, typing.Any]]]]] = None,
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
        :param default_action: default_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#default_action WafregionalWebAcl#default_action}
        :param metric_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#metric_name WafregionalWebAcl#metric_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#name WafregionalWebAcl#name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#id WafregionalWebAcl#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param logging_configuration: logging_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#logging_configuration WafregionalWebAcl#logging_configuration}
        :param rule: rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#rule WafregionalWebAcl#rule}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#tags WafregionalWebAcl#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#tags_all WafregionalWebAcl#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(default_action, dict):
            default_action = WafregionalWebAclDefaultAction(**default_action)
        if isinstance(logging_configuration, dict):
            logging_configuration = WafregionalWebAclLoggingConfiguration(**logging_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ffd579b53c365bfbe19ed4300b93d154a1332598ffc3a08a38d5818136bb72c)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument default_action", value=default_action, expected_type=type_hints["default_action"])
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument logging_configuration", value=logging_configuration, expected_type=type_hints["logging_configuration"])
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "default_action": default_action,
            "metric_name": metric_name,
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
        if id is not None:
            self._values["id"] = id
        if logging_configuration is not None:
            self._values["logging_configuration"] = logging_configuration
        if rule is not None:
            self._values["rule"] = rule
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
    def default_action(self) -> "WafregionalWebAclDefaultAction":
        '''default_action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#default_action WafregionalWebAcl#default_action}
        '''
        result = self._values.get("default_action")
        assert result is not None, "Required property 'default_action' is missing"
        return typing.cast("WafregionalWebAclDefaultAction", result)

    @builtins.property
    def metric_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#metric_name WafregionalWebAcl#metric_name}.'''
        result = self._values.get("metric_name")
        assert result is not None, "Required property 'metric_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#name WafregionalWebAcl#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#id WafregionalWebAcl#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logging_configuration(
        self,
    ) -> typing.Optional["WafregionalWebAclLoggingConfiguration"]:
        '''logging_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#logging_configuration WafregionalWebAcl#logging_configuration}
        '''
        result = self._values.get("logging_configuration")
        return typing.cast(typing.Optional["WafregionalWebAclLoggingConfiguration"], result)

    @builtins.property
    def rule(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WafregionalWebAclRule"]]]:
        '''rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#rule WafregionalWebAcl#rule}
        '''
        result = self._values.get("rule")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WafregionalWebAclRule"]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#tags WafregionalWebAcl#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#tags_all WafregionalWebAcl#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WafregionalWebAclConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.wafregionalWebAcl.WafregionalWebAclDefaultAction",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class WafregionalWebAclDefaultAction:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#type WafregionalWebAcl#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fef8b62597b176b0026a845f7aaf8f6b37f1cfea1f4b2a3d4eb4eb748c2f34a1)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#type WafregionalWebAcl#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WafregionalWebAclDefaultAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WafregionalWebAclDefaultActionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.wafregionalWebAcl.WafregionalWebAclDefaultActionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ddf41d9d11a086579c05d4a5a6841d271e04064b2905a62081b4f8096dc8b379)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

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
            type_hints = typing.get_type_hints(_typecheckingstub__7410b463d251945d3d58eee11a368dfd419d8124a6eed5550497c5c5517a2a8f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[WafregionalWebAclDefaultAction]:
        return typing.cast(typing.Optional[WafregionalWebAclDefaultAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WafregionalWebAclDefaultAction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42cc515034fc831884abd4d797b7ac9a642ef9bb07dd4fc074cfd67006c20223)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.wafregionalWebAcl.WafregionalWebAclLoggingConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "log_destination": "logDestination",
        "redacted_fields": "redactedFields",
    },
)
class WafregionalWebAclLoggingConfiguration:
    def __init__(
        self,
        *,
        log_destination: builtins.str,
        redacted_fields: typing.Optional[typing.Union["WafregionalWebAclLoggingConfigurationRedactedFields", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param log_destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#log_destination WafregionalWebAcl#log_destination}.
        :param redacted_fields: redacted_fields block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#redacted_fields WafregionalWebAcl#redacted_fields}
        '''
        if isinstance(redacted_fields, dict):
            redacted_fields = WafregionalWebAclLoggingConfigurationRedactedFields(**redacted_fields)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84269a91d01b065ca3783524dd3e6df956d5b4f42af5ec87a695c21a66cd3f2b)
            check_type(argname="argument log_destination", value=log_destination, expected_type=type_hints["log_destination"])
            check_type(argname="argument redacted_fields", value=redacted_fields, expected_type=type_hints["redacted_fields"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "log_destination": log_destination,
        }
        if redacted_fields is not None:
            self._values["redacted_fields"] = redacted_fields

    @builtins.property
    def log_destination(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#log_destination WafregionalWebAcl#log_destination}.'''
        result = self._values.get("log_destination")
        assert result is not None, "Required property 'log_destination' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def redacted_fields(
        self,
    ) -> typing.Optional["WafregionalWebAclLoggingConfigurationRedactedFields"]:
        '''redacted_fields block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#redacted_fields WafregionalWebAcl#redacted_fields}
        '''
        result = self._values.get("redacted_fields")
        return typing.cast(typing.Optional["WafregionalWebAclLoggingConfigurationRedactedFields"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WafregionalWebAclLoggingConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WafregionalWebAclLoggingConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.wafregionalWebAcl.WafregionalWebAclLoggingConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f405da297aa7396e8c79cc96d9ddf3c63146aeb0b014447042456f3382b8e731)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRedactedFields")
    def put_redacted_fields(
        self,
        *,
        field_to_match: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WafregionalWebAclLoggingConfigurationRedactedFieldsFieldToMatch", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param field_to_match: field_to_match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#field_to_match WafregionalWebAcl#field_to_match}
        '''
        value = WafregionalWebAclLoggingConfigurationRedactedFields(
            field_to_match=field_to_match
        )

        return typing.cast(None, jsii.invoke(self, "putRedactedFields", [value]))

    @jsii.member(jsii_name="resetRedactedFields")
    def reset_redacted_fields(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedactedFields", []))

    @builtins.property
    @jsii.member(jsii_name="redactedFields")
    def redacted_fields(
        self,
    ) -> "WafregionalWebAclLoggingConfigurationRedactedFieldsOutputReference":
        return typing.cast("WafregionalWebAclLoggingConfigurationRedactedFieldsOutputReference", jsii.get(self, "redactedFields"))

    @builtins.property
    @jsii.member(jsii_name="logDestinationInput")
    def log_destination_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logDestinationInput"))

    @builtins.property
    @jsii.member(jsii_name="redactedFieldsInput")
    def redacted_fields_input(
        self,
    ) -> typing.Optional["WafregionalWebAclLoggingConfigurationRedactedFields"]:
        return typing.cast(typing.Optional["WafregionalWebAclLoggingConfigurationRedactedFields"], jsii.get(self, "redactedFieldsInput"))

    @builtins.property
    @jsii.member(jsii_name="logDestination")
    def log_destination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logDestination"))

    @log_destination.setter
    def log_destination(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__801c46fd61374cc59f214088b9f6307e1c9f64c05087eef45287aff87564c536)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logDestination", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[WafregionalWebAclLoggingConfiguration]:
        return typing.cast(typing.Optional[WafregionalWebAclLoggingConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WafregionalWebAclLoggingConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39b14421c085aa7ecbc759ca1faef43a8aa2555118151a15d953a9bf72d79c7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.wafregionalWebAcl.WafregionalWebAclLoggingConfigurationRedactedFields",
    jsii_struct_bases=[],
    name_mapping={"field_to_match": "fieldToMatch"},
)
class WafregionalWebAclLoggingConfigurationRedactedFields:
    def __init__(
        self,
        *,
        field_to_match: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WafregionalWebAclLoggingConfigurationRedactedFieldsFieldToMatch", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param field_to_match: field_to_match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#field_to_match WafregionalWebAcl#field_to_match}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c0136c15b1f119e78120b4b3fea486445e9a395877e813f4a45f55f6adab091)
            check_type(argname="argument field_to_match", value=field_to_match, expected_type=type_hints["field_to_match"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "field_to_match": field_to_match,
        }

    @builtins.property
    def field_to_match(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WafregionalWebAclLoggingConfigurationRedactedFieldsFieldToMatch"]]:
        '''field_to_match block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#field_to_match WafregionalWebAcl#field_to_match}
        '''
        result = self._values.get("field_to_match")
        assert result is not None, "Required property 'field_to_match' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WafregionalWebAclLoggingConfigurationRedactedFieldsFieldToMatch"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WafregionalWebAclLoggingConfigurationRedactedFields(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.wafregionalWebAcl.WafregionalWebAclLoggingConfigurationRedactedFieldsFieldToMatch",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "data": "data"},
)
class WafregionalWebAclLoggingConfigurationRedactedFieldsFieldToMatch:
    def __init__(
        self,
        *,
        type: builtins.str,
        data: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#type WafregionalWebAcl#type}.
        :param data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#data WafregionalWebAcl#data}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90a2020c103cae2011d741bffdab29ab5f27219d51345cdeb9e5a28a56f37095)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if data is not None:
            self._values["data"] = data

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#type WafregionalWebAcl#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#data WafregionalWebAcl#data}.'''
        result = self._values.get("data")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WafregionalWebAclLoggingConfigurationRedactedFieldsFieldToMatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WafregionalWebAclLoggingConfigurationRedactedFieldsFieldToMatchList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.wafregionalWebAcl.WafregionalWebAclLoggingConfigurationRedactedFieldsFieldToMatchList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__86c8620d9c34c9df916d9842c9ea15bbfbff97b740172f1fff293f9836c25155)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "WafregionalWebAclLoggingConfigurationRedactedFieldsFieldToMatchOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5090fc25aa35aefc10eb0298d38e4db18a385109c630a7066b1f746cc6ba03c)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WafregionalWebAclLoggingConfigurationRedactedFieldsFieldToMatchOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29e495f0063fc3e9d79fcb159e6d5f64f3eedfb557062e9e00520d646e36ecf0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__88418b603a34b44a9c84d20272d5f61230a6a10b634e0d40fd0fdd30b27d4b8f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c0784a9c90cf2782ee1f85a734ef439ecac10589a47e9cbec203aa9ecad715d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WafregionalWebAclLoggingConfigurationRedactedFieldsFieldToMatch]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WafregionalWebAclLoggingConfigurationRedactedFieldsFieldToMatch]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WafregionalWebAclLoggingConfigurationRedactedFieldsFieldToMatch]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6868d0ada77732aa86a1dddd9f3b268ea7d3397605776d28ff3f5b628350e42)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WafregionalWebAclLoggingConfigurationRedactedFieldsFieldToMatchOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.wafregionalWebAcl.WafregionalWebAclLoggingConfigurationRedactedFieldsFieldToMatchOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b930d75f696c296b28538cf16fc750feca7dfe29747e7fdaf0532d2f237ea33a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

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
            type_hints = typing.get_type_hints(_typecheckingstub__6b4dccb4f3321e2bd8ebf26eb93002380f7d723f2148197ed3650958b5ab8d15)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "data", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61dfccf954615ec8a5d8a0bbed5c7171a05312dec8f42e17b1f961698a336141)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WafregionalWebAclLoggingConfigurationRedactedFieldsFieldToMatch, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WafregionalWebAclLoggingConfigurationRedactedFieldsFieldToMatch, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WafregionalWebAclLoggingConfigurationRedactedFieldsFieldToMatch, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b95a9239d6bd047d9eaee5c6931e7a3072b50eac859ba3ada30d2c654fff48f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WafregionalWebAclLoggingConfigurationRedactedFieldsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.wafregionalWebAcl.WafregionalWebAclLoggingConfigurationRedactedFieldsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6a723e80821c7484feb606a46d96346f0944970cc3474a3c928bc1625d9448fc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putFieldToMatch")
    def put_field_to_match(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WafregionalWebAclLoggingConfigurationRedactedFieldsFieldToMatch, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d58737af3e5edcb6b21ad367282e597a2908510b0b19b6514a8a0cbec029d55a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFieldToMatch", [value]))

    @builtins.property
    @jsii.member(jsii_name="fieldToMatch")
    def field_to_match(
        self,
    ) -> WafregionalWebAclLoggingConfigurationRedactedFieldsFieldToMatchList:
        return typing.cast(WafregionalWebAclLoggingConfigurationRedactedFieldsFieldToMatchList, jsii.get(self, "fieldToMatch"))

    @builtins.property
    @jsii.member(jsii_name="fieldToMatchInput")
    def field_to_match_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WafregionalWebAclLoggingConfigurationRedactedFieldsFieldToMatch]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WafregionalWebAclLoggingConfigurationRedactedFieldsFieldToMatch]]], jsii.get(self, "fieldToMatchInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WafregionalWebAclLoggingConfigurationRedactedFields]:
        return typing.cast(typing.Optional[WafregionalWebAclLoggingConfigurationRedactedFields], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WafregionalWebAclLoggingConfigurationRedactedFields],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d7b6550cab2eb7253e6e271ccf1dc722b1a39a328e1e23bfd91c6f9076f6285)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.wafregionalWebAcl.WafregionalWebAclRule",
    jsii_struct_bases=[],
    name_mapping={
        "priority": "priority",
        "rule_id": "ruleId",
        "action": "action",
        "override_action": "overrideAction",
        "type": "type",
    },
)
class WafregionalWebAclRule:
    def __init__(
        self,
        *,
        priority: jsii.Number,
        rule_id: builtins.str,
        action: typing.Optional[typing.Union["WafregionalWebAclRuleAction", typing.Dict[builtins.str, typing.Any]]] = None,
        override_action: typing.Optional[typing.Union["WafregionalWebAclRuleOverrideAction", typing.Dict[builtins.str, typing.Any]]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#priority WafregionalWebAcl#priority}.
        :param rule_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#rule_id WafregionalWebAcl#rule_id}.
        :param action: action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#action WafregionalWebAcl#action}
        :param override_action: override_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#override_action WafregionalWebAcl#override_action}
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#type WafregionalWebAcl#type}.
        '''
        if isinstance(action, dict):
            action = WafregionalWebAclRuleAction(**action)
        if isinstance(override_action, dict):
            override_action = WafregionalWebAclRuleOverrideAction(**override_action)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__447b58b3c5c12a2a95c70bb0a98b06d51675753d41931db37977911b6b48a772)
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument rule_id", value=rule_id, expected_type=type_hints["rule_id"])
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument override_action", value=override_action, expected_type=type_hints["override_action"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "priority": priority,
            "rule_id": rule_id,
        }
        if action is not None:
            self._values["action"] = action
        if override_action is not None:
            self._values["override_action"] = override_action
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def priority(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#priority WafregionalWebAcl#priority}.'''
        result = self._values.get("priority")
        assert result is not None, "Required property 'priority' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def rule_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#rule_id WafregionalWebAcl#rule_id}.'''
        result = self._values.get("rule_id")
        assert result is not None, "Required property 'rule_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def action(self) -> typing.Optional["WafregionalWebAclRuleAction"]:
        '''action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#action WafregionalWebAcl#action}
        '''
        result = self._values.get("action")
        return typing.cast(typing.Optional["WafregionalWebAclRuleAction"], result)

    @builtins.property
    def override_action(self) -> typing.Optional["WafregionalWebAclRuleOverrideAction"]:
        '''override_action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#override_action WafregionalWebAcl#override_action}
        '''
        result = self._values.get("override_action")
        return typing.cast(typing.Optional["WafregionalWebAclRuleOverrideAction"], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#type WafregionalWebAcl#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WafregionalWebAclRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.wafregionalWebAcl.WafregionalWebAclRuleAction",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class WafregionalWebAclRuleAction:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#type WafregionalWebAcl#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e51bf4cfaf176bb8e0c98750b7aa9f27bc223d4b384fb6a1237bfc4ddbbe3cc9)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#type WafregionalWebAcl#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WafregionalWebAclRuleAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WafregionalWebAclRuleActionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.wafregionalWebAcl.WafregionalWebAclRuleActionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d53c0d63d097b3178cea1c9342a232a383ac1c1e28f2b6ea2951f7cd90b94ef9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

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
            type_hints = typing.get_type_hints(_typecheckingstub__2025ee8600ec530208ff823c5a581513cc5fd5b0da945d9cec8c4a0c32f505f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[WafregionalWebAclRuleAction]:
        return typing.cast(typing.Optional[WafregionalWebAclRuleAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WafregionalWebAclRuleAction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c82ad8e770c4bcb068264e783a5c7fd69954d6fad4f87f3a128477f8adcad30)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WafregionalWebAclRuleList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.wafregionalWebAcl.WafregionalWebAclRuleList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8dd0c5d58323dd8bf511515cc8dcf6275b890199deb95b1765383d050092734a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "WafregionalWebAclRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95c2304e67e5a86da2eba0293432b4fdc1c935c1241949f35c3b94cad94e0d80)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WafregionalWebAclRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a844cb87a55270258d11b88cf7e8af73d114604b97fda8a1aaeafd744b07310)
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
            type_hints = typing.get_type_hints(_typecheckingstub__974f19c45030e6f96e76b56d3dbcdeb841b6cc51df5ad58912f431ffce97ffcc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6f708ecd27f1f79e942c776e36dbf759b96a8aec3df448c9183f90c775e2f042)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WafregionalWebAclRule]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WafregionalWebAclRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WafregionalWebAclRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2b329f5918465d7bff8809483e9940db4367e6a1b6cff1eaaf3cb552e443af3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WafregionalWebAclRuleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.wafregionalWebAcl.WafregionalWebAclRuleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8bda1f841d744e3bdd377a925cf4d5be74fc5cc4b067cc7b332f6a95c052836c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAction")
    def put_action(self, *, type: builtins.str) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#type WafregionalWebAcl#type}.
        '''
        value = WafregionalWebAclRuleAction(type=type)

        return typing.cast(None, jsii.invoke(self, "putAction", [value]))

    @jsii.member(jsii_name="putOverrideAction")
    def put_override_action(self, *, type: builtins.str) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#type WafregionalWebAcl#type}.
        '''
        value = WafregionalWebAclRuleOverrideAction(type=type)

        return typing.cast(None, jsii.invoke(self, "putOverrideAction", [value]))

    @jsii.member(jsii_name="resetAction")
    def reset_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAction", []))

    @jsii.member(jsii_name="resetOverrideAction")
    def reset_override_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOverrideAction", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> WafregionalWebAclRuleActionOutputReference:
        return typing.cast(WafregionalWebAclRuleActionOutputReference, jsii.get(self, "action"))

    @builtins.property
    @jsii.member(jsii_name="overrideAction")
    def override_action(self) -> "WafregionalWebAclRuleOverrideActionOutputReference":
        return typing.cast("WafregionalWebAclRuleOverrideActionOutputReference", jsii.get(self, "overrideAction"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[WafregionalWebAclRuleAction]:
        return typing.cast(typing.Optional[WafregionalWebAclRuleAction], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="overrideActionInput")
    def override_action_input(
        self,
    ) -> typing.Optional["WafregionalWebAclRuleOverrideAction"]:
        return typing.cast(typing.Optional["WafregionalWebAclRuleOverrideAction"], jsii.get(self, "overrideActionInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleIdInput")
    def rule_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleIdInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82c7bdb875d560c9a8afe287856264b01682ee4dcf8d5a57285c45b686c8b21b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="ruleId")
    def rule_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ruleId"))

    @rule_id.setter
    def rule_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__325340bc78cf5ce6ddf5e29615c44731c71eaf5e986821b5892720881b5782ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleId", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce9a915788f1a4a7eca07ccf2486e79f42d331118bd455f6552e2119a12e9289)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WafregionalWebAclRule, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WafregionalWebAclRule, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WafregionalWebAclRule, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c398892d399f1789c05c0a617534145cf3eb29ce134ed71b5f6cd722f25b196)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.wafregionalWebAcl.WafregionalWebAclRuleOverrideAction",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class WafregionalWebAclRuleOverrideAction:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#type WafregionalWebAcl#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f5c96555de12624ae6cc45fed2acb8ab8b28df59b1269365a7c3fe98d3a9646)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl#type WafregionalWebAcl#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WafregionalWebAclRuleOverrideAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WafregionalWebAclRuleOverrideActionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.wafregionalWebAcl.WafregionalWebAclRuleOverrideActionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e554954cabf7c6eff2b963ce052614e0a890d9dd7f05e6cc8563129c14612cd3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

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
            type_hints = typing.get_type_hints(_typecheckingstub__c2f5676ee4640abf2911857ed4bb83b65b5563b68f143bb4be10f79d4dfad39a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[WafregionalWebAclRuleOverrideAction]:
        return typing.cast(typing.Optional[WafregionalWebAclRuleOverrideAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WafregionalWebAclRuleOverrideAction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__baaa63891e9e274aa7ae47d38d684588aafa3bb5fdd0dc555942069def45683a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "WafregionalWebAcl",
    "WafregionalWebAclConfig",
    "WafregionalWebAclDefaultAction",
    "WafregionalWebAclDefaultActionOutputReference",
    "WafregionalWebAclLoggingConfiguration",
    "WafregionalWebAclLoggingConfigurationOutputReference",
    "WafregionalWebAclLoggingConfigurationRedactedFields",
    "WafregionalWebAclLoggingConfigurationRedactedFieldsFieldToMatch",
    "WafregionalWebAclLoggingConfigurationRedactedFieldsFieldToMatchList",
    "WafregionalWebAclLoggingConfigurationRedactedFieldsFieldToMatchOutputReference",
    "WafregionalWebAclLoggingConfigurationRedactedFieldsOutputReference",
    "WafregionalWebAclRule",
    "WafregionalWebAclRuleAction",
    "WafregionalWebAclRuleActionOutputReference",
    "WafregionalWebAclRuleList",
    "WafregionalWebAclRuleOutputReference",
    "WafregionalWebAclRuleOverrideAction",
    "WafregionalWebAclRuleOverrideActionOutputReference",
]

publication.publish()

def _typecheckingstub__135bad191b2b5f79f840059c059793d08a523197218a2ca16ddc83530026dd5b(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    default_action: typing.Union[WafregionalWebAclDefaultAction, typing.Dict[builtins.str, typing.Any]],
    metric_name: builtins.str,
    name: builtins.str,
    id: typing.Optional[builtins.str] = None,
    logging_configuration: typing.Optional[typing.Union[WafregionalWebAclLoggingConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WafregionalWebAclRule, typing.Dict[builtins.str, typing.Any]]]]] = None,
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

def _typecheckingstub__727fc6862273319ae07013d0fff3d4c413fdf367412abc7e03a3644c827c684b(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WafregionalWebAclRule, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06783766af99297a736c770c41ac037e2915cb7df4c7f8b49a1075c0239fc35d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e852d410fc6858bfcecbf4dd24f1cf1abfda64b39338204ab407d3d30ce6bbd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fea5408ce9c0fd45f4ad076292b9a040d00e7fb4ef21cd07afb61e5b004b125d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af2ce43e7b7340dff533be4061d07760cb1d954259c70fc3f3e4dee0b6a38936(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f67231310b712ffcce8907103016f1955bb7f96198c89605374b1215d295064(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ffd579b53c365bfbe19ed4300b93d154a1332598ffc3a08a38d5818136bb72c(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    default_action: typing.Union[WafregionalWebAclDefaultAction, typing.Dict[builtins.str, typing.Any]],
    metric_name: builtins.str,
    name: builtins.str,
    id: typing.Optional[builtins.str] = None,
    logging_configuration: typing.Optional[typing.Union[WafregionalWebAclLoggingConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WafregionalWebAclRule, typing.Dict[builtins.str, typing.Any]]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fef8b62597b176b0026a845f7aaf8f6b37f1cfea1f4b2a3d4eb4eb748c2f34a1(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddf41d9d11a086579c05d4a5a6841d271e04064b2905a62081b4f8096dc8b379(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7410b463d251945d3d58eee11a368dfd419d8124a6eed5550497c5c5517a2a8f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42cc515034fc831884abd4d797b7ac9a642ef9bb07dd4fc074cfd67006c20223(
    value: typing.Optional[WafregionalWebAclDefaultAction],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84269a91d01b065ca3783524dd3e6df956d5b4f42af5ec87a695c21a66cd3f2b(
    *,
    log_destination: builtins.str,
    redacted_fields: typing.Optional[typing.Union[WafregionalWebAclLoggingConfigurationRedactedFields, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f405da297aa7396e8c79cc96d9ddf3c63146aeb0b014447042456f3382b8e731(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__801c46fd61374cc59f214088b9f6307e1c9f64c05087eef45287aff87564c536(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39b14421c085aa7ecbc759ca1faef43a8aa2555118151a15d953a9bf72d79c7b(
    value: typing.Optional[WafregionalWebAclLoggingConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c0136c15b1f119e78120b4b3fea486445e9a395877e813f4a45f55f6adab091(
    *,
    field_to_match: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WafregionalWebAclLoggingConfigurationRedactedFieldsFieldToMatch, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90a2020c103cae2011d741bffdab29ab5f27219d51345cdeb9e5a28a56f37095(
    *,
    type: builtins.str,
    data: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86c8620d9c34c9df916d9842c9ea15bbfbff97b740172f1fff293f9836c25155(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5090fc25aa35aefc10eb0298d38e4db18a385109c630a7066b1f746cc6ba03c(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29e495f0063fc3e9d79fcb159e6d5f64f3eedfb557062e9e00520d646e36ecf0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88418b603a34b44a9c84d20272d5f61230a6a10b634e0d40fd0fdd30b27d4b8f(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0784a9c90cf2782ee1f85a734ef439ecac10589a47e9cbec203aa9ecad715d2(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6868d0ada77732aa86a1dddd9f3b268ea7d3397605776d28ff3f5b628350e42(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WafregionalWebAclLoggingConfigurationRedactedFieldsFieldToMatch]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b930d75f696c296b28538cf16fc750feca7dfe29747e7fdaf0532d2f237ea33a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b4dccb4f3321e2bd8ebf26eb93002380f7d723f2148197ed3650958b5ab8d15(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61dfccf954615ec8a5d8a0bbed5c7171a05312dec8f42e17b1f961698a336141(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b95a9239d6bd047d9eaee5c6931e7a3072b50eac859ba3ada30d2c654fff48f(
    value: typing.Optional[typing.Union[WafregionalWebAclLoggingConfigurationRedactedFieldsFieldToMatch, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a723e80821c7484feb606a46d96346f0944970cc3474a3c928bc1625d9448fc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d58737af3e5edcb6b21ad367282e597a2908510b0b19b6514a8a0cbec029d55a(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WafregionalWebAclLoggingConfigurationRedactedFieldsFieldToMatch, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d7b6550cab2eb7253e6e271ccf1dc722b1a39a328e1e23bfd91c6f9076f6285(
    value: typing.Optional[WafregionalWebAclLoggingConfigurationRedactedFields],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__447b58b3c5c12a2a95c70bb0a98b06d51675753d41931db37977911b6b48a772(
    *,
    priority: jsii.Number,
    rule_id: builtins.str,
    action: typing.Optional[typing.Union[WafregionalWebAclRuleAction, typing.Dict[builtins.str, typing.Any]]] = None,
    override_action: typing.Optional[typing.Union[WafregionalWebAclRuleOverrideAction, typing.Dict[builtins.str, typing.Any]]] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e51bf4cfaf176bb8e0c98750b7aa9f27bc223d4b384fb6a1237bfc4ddbbe3cc9(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d53c0d63d097b3178cea1c9342a232a383ac1c1e28f2b6ea2951f7cd90b94ef9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2025ee8600ec530208ff823c5a581513cc5fd5b0da945d9cec8c4a0c32f505f7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c82ad8e770c4bcb068264e783a5c7fd69954d6fad4f87f3a128477f8adcad30(
    value: typing.Optional[WafregionalWebAclRuleAction],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8dd0c5d58323dd8bf511515cc8dcf6275b890199deb95b1765383d050092734a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95c2304e67e5a86da2eba0293432b4fdc1c935c1241949f35c3b94cad94e0d80(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a844cb87a55270258d11b88cf7e8af73d114604b97fda8a1aaeafd744b07310(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__974f19c45030e6f96e76b56d3dbcdeb841b6cc51df5ad58912f431ffce97ffcc(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f708ecd27f1f79e942c776e36dbf759b96a8aec3df448c9183f90c775e2f042(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2b329f5918465d7bff8809483e9940db4367e6a1b6cff1eaaf3cb552e443af3(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WafregionalWebAclRule]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8bda1f841d744e3bdd377a925cf4d5be74fc5cc4b067cc7b332f6a95c052836c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82c7bdb875d560c9a8afe287856264b01682ee4dcf8d5a57285c45b686c8b21b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__325340bc78cf5ce6ddf5e29615c44731c71eaf5e986821b5892720881b5782ef(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce9a915788f1a4a7eca07ccf2486e79f42d331118bd455f6552e2119a12e9289(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c398892d399f1789c05c0a617534145cf3eb29ce134ed71b5f6cd722f25b196(
    value: typing.Optional[typing.Union[WafregionalWebAclRule, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f5c96555de12624ae6cc45fed2acb8ab8b28df59b1269365a7c3fe98d3a9646(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e554954cabf7c6eff2b963ce052614e0a890d9dd7f05e6cc8563129c14612cd3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2f5676ee4640abf2911857ed4bb83b65b5563b68f143bb4be10f79d4dfad39a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__baaa63891e9e274aa7ae47d38d684588aafa3bb5fdd0dc555942069def45683a(
    value: typing.Optional[WafregionalWebAclRuleOverrideAction],
) -> None:
    """Type checking stubs"""
    pass
