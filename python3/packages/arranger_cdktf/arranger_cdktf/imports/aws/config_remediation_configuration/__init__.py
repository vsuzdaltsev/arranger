'''
# `aws_config_remediation_configuration`

Refer to the Terraform Registory for docs: [`aws_config_remediation_configuration`](https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration).
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


class ConfigRemediationConfiguration(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.configRemediationConfiguration.ConfigRemediationConfiguration",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration aws_config_remediation_configuration}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        config_rule_name: builtins.str,
        target_id: builtins.str,
        target_type: builtins.str,
        automatic: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        execution_controls: typing.Optional[typing.Union["ConfigRemediationConfigurationExecutionControls", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        maximum_automatic_attempts: typing.Optional[jsii.Number] = None,
        parameter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ConfigRemediationConfigurationParameter", typing.Dict[builtins.str, typing.Any]]]]] = None,
        resource_type: typing.Optional[builtins.str] = None,
        retry_attempt_seconds: typing.Optional[jsii.Number] = None,
        target_version: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration aws_config_remediation_configuration} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param config_rule_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration#config_rule_name ConfigRemediationConfiguration#config_rule_name}.
        :param target_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration#target_id ConfigRemediationConfiguration#target_id}.
        :param target_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration#target_type ConfigRemediationConfiguration#target_type}.
        :param automatic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration#automatic ConfigRemediationConfiguration#automatic}.
        :param execution_controls: execution_controls block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration#execution_controls ConfigRemediationConfiguration#execution_controls}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration#id ConfigRemediationConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param maximum_automatic_attempts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration#maximum_automatic_attempts ConfigRemediationConfiguration#maximum_automatic_attempts}.
        :param parameter: parameter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration#parameter ConfigRemediationConfiguration#parameter}
        :param resource_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration#resource_type ConfigRemediationConfiguration#resource_type}.
        :param retry_attempt_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration#retry_attempt_seconds ConfigRemediationConfiguration#retry_attempt_seconds}.
        :param target_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration#target_version ConfigRemediationConfiguration#target_version}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93dc5c9227edfa06526086f25905c8c7bbe819b68f8423e4e988bf1fb0194a76)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ConfigRemediationConfigurationConfig(
            config_rule_name=config_rule_name,
            target_id=target_id,
            target_type=target_type,
            automatic=automatic,
            execution_controls=execution_controls,
            id=id,
            maximum_automatic_attempts=maximum_automatic_attempts,
            parameter=parameter,
            resource_type=resource_type,
            retry_attempt_seconds=retry_attempt_seconds,
            target_version=target_version,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putExecutionControls")
    def put_execution_controls(
        self,
        *,
        ssm_controls: typing.Optional[typing.Union["ConfigRemediationConfigurationExecutionControlsSsmControls", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param ssm_controls: ssm_controls block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration#ssm_controls ConfigRemediationConfiguration#ssm_controls}
        '''
        value = ConfigRemediationConfigurationExecutionControls(
            ssm_controls=ssm_controls
        )

        return typing.cast(None, jsii.invoke(self, "putExecutionControls", [value]))

    @jsii.member(jsii_name="putParameter")
    def put_parameter(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ConfigRemediationConfigurationParameter", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f58116e83e8536b93816fa3dd33169c589a69c035d63d77c5a0789cc18de20a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putParameter", [value]))

    @jsii.member(jsii_name="resetAutomatic")
    def reset_automatic(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutomatic", []))

    @jsii.member(jsii_name="resetExecutionControls")
    def reset_execution_controls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExecutionControls", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMaximumAutomaticAttempts")
    def reset_maximum_automatic_attempts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaximumAutomaticAttempts", []))

    @jsii.member(jsii_name="resetParameter")
    def reset_parameter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameter", []))

    @jsii.member(jsii_name="resetResourceType")
    def reset_resource_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceType", []))

    @jsii.member(jsii_name="resetRetryAttemptSeconds")
    def reset_retry_attempt_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetryAttemptSeconds", []))

    @jsii.member(jsii_name="resetTargetVersion")
    def reset_target_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetVersion", []))

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
    @jsii.member(jsii_name="executionControls")
    def execution_controls(
        self,
    ) -> "ConfigRemediationConfigurationExecutionControlsOutputReference":
        return typing.cast("ConfigRemediationConfigurationExecutionControlsOutputReference", jsii.get(self, "executionControls"))

    @builtins.property
    @jsii.member(jsii_name="parameter")
    def parameter(self) -> "ConfigRemediationConfigurationParameterList":
        return typing.cast("ConfigRemediationConfigurationParameterList", jsii.get(self, "parameter"))

    @builtins.property
    @jsii.member(jsii_name="automaticInput")
    def automatic_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "automaticInput"))

    @builtins.property
    @jsii.member(jsii_name="configRuleNameInput")
    def config_rule_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configRuleNameInput"))

    @builtins.property
    @jsii.member(jsii_name="executionControlsInput")
    def execution_controls_input(
        self,
    ) -> typing.Optional["ConfigRemediationConfigurationExecutionControls"]:
        return typing.cast(typing.Optional["ConfigRemediationConfigurationExecutionControls"], jsii.get(self, "executionControlsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumAutomaticAttemptsInput")
    def maximum_automatic_attempts_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maximumAutomaticAttemptsInput"))

    @builtins.property
    @jsii.member(jsii_name="parameterInput")
    def parameter_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ConfigRemediationConfigurationParameter"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ConfigRemediationConfigurationParameter"]]], jsii.get(self, "parameterInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceTypeInput")
    def resource_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="retryAttemptSecondsInput")
    def retry_attempt_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retryAttemptSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="targetIdInput")
    def target_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="targetTypeInput")
    def target_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="targetVersionInput")
    def target_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="automatic")
    def automatic(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "automatic"))

    @automatic.setter
    def automatic(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3557fc4c146556fa5391065afffe922dab8ebbd359e1ad9b9ded7994d786e85b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "automatic", value)

    @builtins.property
    @jsii.member(jsii_name="configRuleName")
    def config_rule_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "configRuleName"))

    @config_rule_name.setter
    def config_rule_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__325179d4b20798b92d1e041c2c53c0eb5c61aa24847e9516f9c5a6d53791782f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configRuleName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29e6f2c30287cb1ef0280e5c835cbb7f0c47a4ad4b9dd232541dae2842b68baf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="maximumAutomaticAttempts")
    def maximum_automatic_attempts(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maximumAutomaticAttempts"))

    @maximum_automatic_attempts.setter
    def maximum_automatic_attempts(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f42cded71fb465770f9c850592ffcee62a3d5bb6f480bd39aaa6c3f1e713833)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumAutomaticAttempts", value)

    @builtins.property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceType"))

    @resource_type.setter
    def resource_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c00d0a205c732723a2472e30d1f321f23f3cd3d98a4dd98253a5c027e6cf6839)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceType", value)

    @builtins.property
    @jsii.member(jsii_name="retryAttemptSeconds")
    def retry_attempt_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retryAttemptSeconds"))

    @retry_attempt_seconds.setter
    def retry_attempt_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5e368965768169447e109f2f9367e7430c4ab54154685de5dc03c9ab6246d57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retryAttemptSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="targetId")
    def target_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetId"))

    @target_id.setter
    def target_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc5e129a31e28213287c53b00707f92694f45a5058daa16b7d5c22174930543f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetId", value)

    @builtins.property
    @jsii.member(jsii_name="targetType")
    def target_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetType"))

    @target_type.setter
    def target_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fcc6cfb04c631e237716da64ea9033598053ae15b6d4e19f31407bb76d97bcf7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetType", value)

    @builtins.property
    @jsii.member(jsii_name="targetVersion")
    def target_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetVersion"))

    @target_version.setter
    def target_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e92c28c4472604eefd575db5af7bd1651428bd451573b6f0712a36d24909f5f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetVersion", value)


@jsii.data_type(
    jsii_type="aws.configRemediationConfiguration.ConfigRemediationConfigurationConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "config_rule_name": "configRuleName",
        "target_id": "targetId",
        "target_type": "targetType",
        "automatic": "automatic",
        "execution_controls": "executionControls",
        "id": "id",
        "maximum_automatic_attempts": "maximumAutomaticAttempts",
        "parameter": "parameter",
        "resource_type": "resourceType",
        "retry_attempt_seconds": "retryAttemptSeconds",
        "target_version": "targetVersion",
    },
)
class ConfigRemediationConfigurationConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        config_rule_name: builtins.str,
        target_id: builtins.str,
        target_type: builtins.str,
        automatic: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        execution_controls: typing.Optional[typing.Union["ConfigRemediationConfigurationExecutionControls", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        maximum_automatic_attempts: typing.Optional[jsii.Number] = None,
        parameter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ConfigRemediationConfigurationParameter", typing.Dict[builtins.str, typing.Any]]]]] = None,
        resource_type: typing.Optional[builtins.str] = None,
        retry_attempt_seconds: typing.Optional[jsii.Number] = None,
        target_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param config_rule_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration#config_rule_name ConfigRemediationConfiguration#config_rule_name}.
        :param target_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration#target_id ConfigRemediationConfiguration#target_id}.
        :param target_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration#target_type ConfigRemediationConfiguration#target_type}.
        :param automatic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration#automatic ConfigRemediationConfiguration#automatic}.
        :param execution_controls: execution_controls block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration#execution_controls ConfigRemediationConfiguration#execution_controls}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration#id ConfigRemediationConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param maximum_automatic_attempts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration#maximum_automatic_attempts ConfigRemediationConfiguration#maximum_automatic_attempts}.
        :param parameter: parameter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration#parameter ConfigRemediationConfiguration#parameter}
        :param resource_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration#resource_type ConfigRemediationConfiguration#resource_type}.
        :param retry_attempt_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration#retry_attempt_seconds ConfigRemediationConfiguration#retry_attempt_seconds}.
        :param target_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration#target_version ConfigRemediationConfiguration#target_version}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(execution_controls, dict):
            execution_controls = ConfigRemediationConfigurationExecutionControls(**execution_controls)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a43d521021f788c8b8e0e565d24415b436cc10c3fbfe853c321776c23d94a038)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument config_rule_name", value=config_rule_name, expected_type=type_hints["config_rule_name"])
            check_type(argname="argument target_id", value=target_id, expected_type=type_hints["target_id"])
            check_type(argname="argument target_type", value=target_type, expected_type=type_hints["target_type"])
            check_type(argname="argument automatic", value=automatic, expected_type=type_hints["automatic"])
            check_type(argname="argument execution_controls", value=execution_controls, expected_type=type_hints["execution_controls"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument maximum_automatic_attempts", value=maximum_automatic_attempts, expected_type=type_hints["maximum_automatic_attempts"])
            check_type(argname="argument parameter", value=parameter, expected_type=type_hints["parameter"])
            check_type(argname="argument resource_type", value=resource_type, expected_type=type_hints["resource_type"])
            check_type(argname="argument retry_attempt_seconds", value=retry_attempt_seconds, expected_type=type_hints["retry_attempt_seconds"])
            check_type(argname="argument target_version", value=target_version, expected_type=type_hints["target_version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "config_rule_name": config_rule_name,
            "target_id": target_id,
            "target_type": target_type,
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
        if automatic is not None:
            self._values["automatic"] = automatic
        if execution_controls is not None:
            self._values["execution_controls"] = execution_controls
        if id is not None:
            self._values["id"] = id
        if maximum_automatic_attempts is not None:
            self._values["maximum_automatic_attempts"] = maximum_automatic_attempts
        if parameter is not None:
            self._values["parameter"] = parameter
        if resource_type is not None:
            self._values["resource_type"] = resource_type
        if retry_attempt_seconds is not None:
            self._values["retry_attempt_seconds"] = retry_attempt_seconds
        if target_version is not None:
            self._values["target_version"] = target_version

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
    def config_rule_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration#config_rule_name ConfigRemediationConfiguration#config_rule_name}.'''
        result = self._values.get("config_rule_name")
        assert result is not None, "Required property 'config_rule_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration#target_id ConfigRemediationConfiguration#target_id}.'''
        result = self._values.get("target_id")
        assert result is not None, "Required property 'target_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration#target_type ConfigRemediationConfiguration#target_type}.'''
        result = self._values.get("target_type")
        assert result is not None, "Required property 'target_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def automatic(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration#automatic ConfigRemediationConfiguration#automatic}.'''
        result = self._values.get("automatic")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def execution_controls(
        self,
    ) -> typing.Optional["ConfigRemediationConfigurationExecutionControls"]:
        '''execution_controls block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration#execution_controls ConfigRemediationConfiguration#execution_controls}
        '''
        result = self._values.get("execution_controls")
        return typing.cast(typing.Optional["ConfigRemediationConfigurationExecutionControls"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration#id ConfigRemediationConfiguration#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def maximum_automatic_attempts(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration#maximum_automatic_attempts ConfigRemediationConfiguration#maximum_automatic_attempts}.'''
        result = self._values.get("maximum_automatic_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def parameter(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ConfigRemediationConfigurationParameter"]]]:
        '''parameter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration#parameter ConfigRemediationConfiguration#parameter}
        '''
        result = self._values.get("parameter")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ConfigRemediationConfigurationParameter"]]], result)

    @builtins.property
    def resource_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration#resource_type ConfigRemediationConfiguration#resource_type}.'''
        result = self._values.get("resource_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def retry_attempt_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration#retry_attempt_seconds ConfigRemediationConfiguration#retry_attempt_seconds}.'''
        result = self._values.get("retry_attempt_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def target_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration#target_version ConfigRemediationConfiguration#target_version}.'''
        result = self._values.get("target_version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConfigRemediationConfigurationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.configRemediationConfiguration.ConfigRemediationConfigurationExecutionControls",
    jsii_struct_bases=[],
    name_mapping={"ssm_controls": "ssmControls"},
)
class ConfigRemediationConfigurationExecutionControls:
    def __init__(
        self,
        *,
        ssm_controls: typing.Optional[typing.Union["ConfigRemediationConfigurationExecutionControlsSsmControls", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param ssm_controls: ssm_controls block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration#ssm_controls ConfigRemediationConfiguration#ssm_controls}
        '''
        if isinstance(ssm_controls, dict):
            ssm_controls = ConfigRemediationConfigurationExecutionControlsSsmControls(**ssm_controls)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cc8ef947a266994c8bf0494fbd8cd9b8f4cff7db0a90926c7799e185bb2cf06)
            check_type(argname="argument ssm_controls", value=ssm_controls, expected_type=type_hints["ssm_controls"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if ssm_controls is not None:
            self._values["ssm_controls"] = ssm_controls

    @builtins.property
    def ssm_controls(
        self,
    ) -> typing.Optional["ConfigRemediationConfigurationExecutionControlsSsmControls"]:
        '''ssm_controls block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration#ssm_controls ConfigRemediationConfiguration#ssm_controls}
        '''
        result = self._values.get("ssm_controls")
        return typing.cast(typing.Optional["ConfigRemediationConfigurationExecutionControlsSsmControls"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConfigRemediationConfigurationExecutionControls(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ConfigRemediationConfigurationExecutionControlsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.configRemediationConfiguration.ConfigRemediationConfigurationExecutionControlsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9502e2b8ca6e01535b058b3e28c97b150ac2dbb06a2875a31d2ad7c2e6ef92f1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSsmControls")
    def put_ssm_controls(
        self,
        *,
        concurrent_execution_rate_percentage: typing.Optional[jsii.Number] = None,
        error_percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param concurrent_execution_rate_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration#concurrent_execution_rate_percentage ConfigRemediationConfiguration#concurrent_execution_rate_percentage}.
        :param error_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration#error_percentage ConfigRemediationConfiguration#error_percentage}.
        '''
        value = ConfigRemediationConfigurationExecutionControlsSsmControls(
            concurrent_execution_rate_percentage=concurrent_execution_rate_percentage,
            error_percentage=error_percentage,
        )

        return typing.cast(None, jsii.invoke(self, "putSsmControls", [value]))

    @jsii.member(jsii_name="resetSsmControls")
    def reset_ssm_controls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSsmControls", []))

    @builtins.property
    @jsii.member(jsii_name="ssmControls")
    def ssm_controls(
        self,
    ) -> "ConfigRemediationConfigurationExecutionControlsSsmControlsOutputReference":
        return typing.cast("ConfigRemediationConfigurationExecutionControlsSsmControlsOutputReference", jsii.get(self, "ssmControls"))

    @builtins.property
    @jsii.member(jsii_name="ssmControlsInput")
    def ssm_controls_input(
        self,
    ) -> typing.Optional["ConfigRemediationConfigurationExecutionControlsSsmControls"]:
        return typing.cast(typing.Optional["ConfigRemediationConfigurationExecutionControlsSsmControls"], jsii.get(self, "ssmControlsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ConfigRemediationConfigurationExecutionControls]:
        return typing.cast(typing.Optional[ConfigRemediationConfigurationExecutionControls], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ConfigRemediationConfigurationExecutionControls],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ecd7638dfe8debf298e82b07261a30524646d64886ca6b8da50a0c4544be4ae9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.configRemediationConfiguration.ConfigRemediationConfigurationExecutionControlsSsmControls",
    jsii_struct_bases=[],
    name_mapping={
        "concurrent_execution_rate_percentage": "concurrentExecutionRatePercentage",
        "error_percentage": "errorPercentage",
    },
)
class ConfigRemediationConfigurationExecutionControlsSsmControls:
    def __init__(
        self,
        *,
        concurrent_execution_rate_percentage: typing.Optional[jsii.Number] = None,
        error_percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param concurrent_execution_rate_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration#concurrent_execution_rate_percentage ConfigRemediationConfiguration#concurrent_execution_rate_percentage}.
        :param error_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration#error_percentage ConfigRemediationConfiguration#error_percentage}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6826ba4bf014f6fbbfa7227291aeac0a6a11c84a2b6ebda6f1a3c753f17d8eeb)
            check_type(argname="argument concurrent_execution_rate_percentage", value=concurrent_execution_rate_percentage, expected_type=type_hints["concurrent_execution_rate_percentage"])
            check_type(argname="argument error_percentage", value=error_percentage, expected_type=type_hints["error_percentage"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if concurrent_execution_rate_percentage is not None:
            self._values["concurrent_execution_rate_percentage"] = concurrent_execution_rate_percentage
        if error_percentage is not None:
            self._values["error_percentage"] = error_percentage

    @builtins.property
    def concurrent_execution_rate_percentage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration#concurrent_execution_rate_percentage ConfigRemediationConfiguration#concurrent_execution_rate_percentage}.'''
        result = self._values.get("concurrent_execution_rate_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def error_percentage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration#error_percentage ConfigRemediationConfiguration#error_percentage}.'''
        result = self._values.get("error_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConfigRemediationConfigurationExecutionControlsSsmControls(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ConfigRemediationConfigurationExecutionControlsSsmControlsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.configRemediationConfiguration.ConfigRemediationConfigurationExecutionControlsSsmControlsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7bc3e15acbccaf14c9d2f317dcd63809701920b76c68e96ec1fa5e068154ebb9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetConcurrentExecutionRatePercentage")
    def reset_concurrent_execution_rate_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConcurrentExecutionRatePercentage", []))

    @jsii.member(jsii_name="resetErrorPercentage")
    def reset_error_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetErrorPercentage", []))

    @builtins.property
    @jsii.member(jsii_name="concurrentExecutionRatePercentageInput")
    def concurrent_execution_rate_percentage_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "concurrentExecutionRatePercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="errorPercentageInput")
    def error_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "errorPercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="concurrentExecutionRatePercentage")
    def concurrent_execution_rate_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "concurrentExecutionRatePercentage"))

    @concurrent_execution_rate_percentage.setter
    def concurrent_execution_rate_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9edf27ec3d9c267b89a7c7367aacec3cc0a5be5a620e6ce8d58334eee420eb6d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "concurrentExecutionRatePercentage", value)

    @builtins.property
    @jsii.member(jsii_name="errorPercentage")
    def error_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "errorPercentage"))

    @error_percentage.setter
    def error_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b9dbc8420d43725ae042851a1bb351647168df9b758ce8f5d7826f44cb55885)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "errorPercentage", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ConfigRemediationConfigurationExecutionControlsSsmControls]:
        return typing.cast(typing.Optional[ConfigRemediationConfigurationExecutionControlsSsmControls], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ConfigRemediationConfigurationExecutionControlsSsmControls],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28473d01bf2de34dbb621b5ef130f266dc2a80e898c4641931f23113c318550a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.configRemediationConfiguration.ConfigRemediationConfigurationParameter",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "resource_value": "resourceValue",
        "static_value": "staticValue",
        "static_values": "staticValues",
    },
)
class ConfigRemediationConfigurationParameter:
    def __init__(
        self,
        *,
        name: builtins.str,
        resource_value: typing.Optional[builtins.str] = None,
        static_value: typing.Optional[builtins.str] = None,
        static_values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration#name ConfigRemediationConfiguration#name}.
        :param resource_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration#resource_value ConfigRemediationConfiguration#resource_value}.
        :param static_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration#static_value ConfigRemediationConfiguration#static_value}.
        :param static_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration#static_values ConfigRemediationConfiguration#static_values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6d3fa113827f4a8b8e97f404fe234862430184d55f8f9ed92817c60ddb4f7d2)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_value", value=resource_value, expected_type=type_hints["resource_value"])
            check_type(argname="argument static_value", value=static_value, expected_type=type_hints["static_value"])
            check_type(argname="argument static_values", value=static_values, expected_type=type_hints["static_values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if resource_value is not None:
            self._values["resource_value"] = resource_value
        if static_value is not None:
            self._values["static_value"] = static_value
        if static_values is not None:
            self._values["static_values"] = static_values

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration#name ConfigRemediationConfiguration#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration#resource_value ConfigRemediationConfiguration#resource_value}.'''
        result = self._values.get("resource_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def static_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration#static_value ConfigRemediationConfiguration#static_value}.'''
        result = self._values.get("static_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def static_values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/config_remediation_configuration#static_values ConfigRemediationConfiguration#static_values}.'''
        result = self._values.get("static_values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConfigRemediationConfigurationParameter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ConfigRemediationConfigurationParameterList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.configRemediationConfiguration.ConfigRemediationConfigurationParameterList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ae6114c1ac4b22d8a64b9f5aa3037c5b4965a828eee8399b0e131f58f726e32d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ConfigRemediationConfigurationParameterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcc2d8fc4a26ea2debb6f48e87b458c5a705149429b1c6001f55907147811eaa)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ConfigRemediationConfigurationParameterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5900bd8b82aa553cf4edcabac991f512990e7008d46329c12d0e7c92389a5e7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__69a4295cf7deb1f77fc2ed26594bc0b8bf2335697b6d2e68c51149b30460a5fb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3a2a863e6724e95f727d16ff6618237dee0ca42cd2771507c895e68b0a4fee18)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ConfigRemediationConfigurationParameter]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ConfigRemediationConfigurationParameter]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ConfigRemediationConfigurationParameter]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12359e99562a5d1e7c688069e06c57e49ba5488181d9609d9507dd013cb97cd6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ConfigRemediationConfigurationParameterOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.configRemediationConfiguration.ConfigRemediationConfigurationParameterOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__03c4bb4bc115f6f4e716bee3373345a5438c93a493a50e99e0d089a0ef1bc43e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetResourceValue")
    def reset_resource_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceValue", []))

    @jsii.member(jsii_name="resetStaticValue")
    def reset_static_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStaticValue", []))

    @jsii.member(jsii_name="resetStaticValues")
    def reset_static_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStaticValues", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceValueInput")
    def resource_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceValueInput"))

    @builtins.property
    @jsii.member(jsii_name="staticValueInput")
    def static_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "staticValueInput"))

    @builtins.property
    @jsii.member(jsii_name="staticValuesInput")
    def static_values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "staticValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bfb65fda44d7956c1ffa85923e2207fe1ec1627d0c6a4269e3d0fe6626a2a94)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceValue")
    def resource_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceValue"))

    @resource_value.setter
    def resource_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7357138b25cd7f663be1165629775666cb4f982580f5a5087709f1277a10e0f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceValue", value)

    @builtins.property
    @jsii.member(jsii_name="staticValue")
    def static_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "staticValue"))

    @static_value.setter
    def static_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa15fd3cb34b9c2fcb7f040fe2776c8eaf780513a0bde8ee68e7f16ec07e26a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "staticValue", value)

    @builtins.property
    @jsii.member(jsii_name="staticValues")
    def static_values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "staticValues"))

    @static_values.setter
    def static_values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30eb3f85ae80144ad93c6f3e97f81f9774749d66fe96f054ca2642395dcccf5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "staticValues", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ConfigRemediationConfigurationParameter, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ConfigRemediationConfigurationParameter, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ConfigRemediationConfigurationParameter, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59a0aa8bbfb1ed169442988d999f79f6a60ada4f182007807875cd08ff6a11b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ConfigRemediationConfiguration",
    "ConfigRemediationConfigurationConfig",
    "ConfigRemediationConfigurationExecutionControls",
    "ConfigRemediationConfigurationExecutionControlsOutputReference",
    "ConfigRemediationConfigurationExecutionControlsSsmControls",
    "ConfigRemediationConfigurationExecutionControlsSsmControlsOutputReference",
    "ConfigRemediationConfigurationParameter",
    "ConfigRemediationConfigurationParameterList",
    "ConfigRemediationConfigurationParameterOutputReference",
]

publication.publish()

def _typecheckingstub__93dc5c9227edfa06526086f25905c8c7bbe819b68f8423e4e988bf1fb0194a76(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    config_rule_name: builtins.str,
    target_id: builtins.str,
    target_type: builtins.str,
    automatic: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    execution_controls: typing.Optional[typing.Union[ConfigRemediationConfigurationExecutionControls, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    maximum_automatic_attempts: typing.Optional[jsii.Number] = None,
    parameter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ConfigRemediationConfigurationParameter, typing.Dict[builtins.str, typing.Any]]]]] = None,
    resource_type: typing.Optional[builtins.str] = None,
    retry_attempt_seconds: typing.Optional[jsii.Number] = None,
    target_version: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__2f58116e83e8536b93816fa3dd33169c589a69c035d63d77c5a0789cc18de20a(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ConfigRemediationConfigurationParameter, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3557fc4c146556fa5391065afffe922dab8ebbd359e1ad9b9ded7994d786e85b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__325179d4b20798b92d1e041c2c53c0eb5c61aa24847e9516f9c5a6d53791782f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29e6f2c30287cb1ef0280e5c835cbb7f0c47a4ad4b9dd232541dae2842b68baf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f42cded71fb465770f9c850592ffcee62a3d5bb6f480bd39aaa6c3f1e713833(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c00d0a205c732723a2472e30d1f321f23f3cd3d98a4dd98253a5c027e6cf6839(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5e368965768169447e109f2f9367e7430c4ab54154685de5dc03c9ab6246d57(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc5e129a31e28213287c53b00707f92694f45a5058daa16b7d5c22174930543f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcc6cfb04c631e237716da64ea9033598053ae15b6d4e19f31407bb76d97bcf7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e92c28c4472604eefd575db5af7bd1651428bd451573b6f0712a36d24909f5f5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a43d521021f788c8b8e0e565d24415b436cc10c3fbfe853c321776c23d94a038(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    config_rule_name: builtins.str,
    target_id: builtins.str,
    target_type: builtins.str,
    automatic: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    execution_controls: typing.Optional[typing.Union[ConfigRemediationConfigurationExecutionControls, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    maximum_automatic_attempts: typing.Optional[jsii.Number] = None,
    parameter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ConfigRemediationConfigurationParameter, typing.Dict[builtins.str, typing.Any]]]]] = None,
    resource_type: typing.Optional[builtins.str] = None,
    retry_attempt_seconds: typing.Optional[jsii.Number] = None,
    target_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cc8ef947a266994c8bf0494fbd8cd9b8f4cff7db0a90926c7799e185bb2cf06(
    *,
    ssm_controls: typing.Optional[typing.Union[ConfigRemediationConfigurationExecutionControlsSsmControls, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9502e2b8ca6e01535b058b3e28c97b150ac2dbb06a2875a31d2ad7c2e6ef92f1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecd7638dfe8debf298e82b07261a30524646d64886ca6b8da50a0c4544be4ae9(
    value: typing.Optional[ConfigRemediationConfigurationExecutionControls],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6826ba4bf014f6fbbfa7227291aeac0a6a11c84a2b6ebda6f1a3c753f17d8eeb(
    *,
    concurrent_execution_rate_percentage: typing.Optional[jsii.Number] = None,
    error_percentage: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7bc3e15acbccaf14c9d2f317dcd63809701920b76c68e96ec1fa5e068154ebb9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9edf27ec3d9c267b89a7c7367aacec3cc0a5be5a620e6ce8d58334eee420eb6d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b9dbc8420d43725ae042851a1bb351647168df9b758ce8f5d7826f44cb55885(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28473d01bf2de34dbb621b5ef130f266dc2a80e898c4641931f23113c318550a(
    value: typing.Optional[ConfigRemediationConfigurationExecutionControlsSsmControls],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6d3fa113827f4a8b8e97f404fe234862430184d55f8f9ed92817c60ddb4f7d2(
    *,
    name: builtins.str,
    resource_value: typing.Optional[builtins.str] = None,
    static_value: typing.Optional[builtins.str] = None,
    static_values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae6114c1ac4b22d8a64b9f5aa3037c5b4965a828eee8399b0e131f58f726e32d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcc2d8fc4a26ea2debb6f48e87b458c5a705149429b1c6001f55907147811eaa(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5900bd8b82aa553cf4edcabac991f512990e7008d46329c12d0e7c92389a5e7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69a4295cf7deb1f77fc2ed26594bc0b8bf2335697b6d2e68c51149b30460a5fb(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a2a863e6724e95f727d16ff6618237dee0ca42cd2771507c895e68b0a4fee18(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12359e99562a5d1e7c688069e06c57e49ba5488181d9609d9507dd013cb97cd6(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ConfigRemediationConfigurationParameter]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03c4bb4bc115f6f4e716bee3373345a5438c93a493a50e99e0d089a0ef1bc43e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bfb65fda44d7956c1ffa85923e2207fe1ec1627d0c6a4269e3d0fe6626a2a94(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7357138b25cd7f663be1165629775666cb4f982580f5a5087709f1277a10e0f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa15fd3cb34b9c2fcb7f040fe2776c8eaf780513a0bde8ee68e7f16ec07e26a0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30eb3f85ae80144ad93c6f3e97f81f9774749d66fe96f054ca2642395dcccf5e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59a0aa8bbfb1ed169442988d999f79f6a60ada4f182007807875cd08ff6a11b2(
    value: typing.Optional[typing.Union[ConfigRemediationConfigurationParameter, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
