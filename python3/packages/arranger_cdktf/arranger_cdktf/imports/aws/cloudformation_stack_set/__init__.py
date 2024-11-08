'''
# `aws_cloudformation_stack_set`

Refer to the Terraform Registory for docs: [`aws_cloudformation_stack_set`](https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set).
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


class CloudformationStackSet(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudformationStackSet.CloudformationStackSet",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set aws_cloudformation_stack_set}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        administration_role_arn: typing.Optional[builtins.str] = None,
        auto_deployment: typing.Optional[typing.Union["CloudformationStackSetAutoDeployment", typing.Dict[builtins.str, typing.Any]]] = None,
        call_as: typing.Optional[builtins.str] = None,
        capabilities: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        execution_role_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        operation_preferences: typing.Optional[typing.Union["CloudformationStackSetOperationPreferences", typing.Dict[builtins.str, typing.Any]]] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        permission_model: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        template_body: typing.Optional[builtins.str] = None,
        template_url: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["CloudformationStackSetTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set aws_cloudformation_stack_set} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#name CloudformationStackSet#name}.
        :param administration_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#administration_role_arn CloudformationStackSet#administration_role_arn}.
        :param auto_deployment: auto_deployment block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#auto_deployment CloudformationStackSet#auto_deployment}
        :param call_as: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#call_as CloudformationStackSet#call_as}.
        :param capabilities: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#capabilities CloudformationStackSet#capabilities}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#description CloudformationStackSet#description}.
        :param execution_role_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#execution_role_name CloudformationStackSet#execution_role_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#id CloudformationStackSet#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param operation_preferences: operation_preferences block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#operation_preferences CloudformationStackSet#operation_preferences}
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#parameters CloudformationStackSet#parameters}.
        :param permission_model: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#permission_model CloudformationStackSet#permission_model}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#tags CloudformationStackSet#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#tags_all CloudformationStackSet#tags_all}.
        :param template_body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#template_body CloudformationStackSet#template_body}.
        :param template_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#template_url CloudformationStackSet#template_url}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#timeouts CloudformationStackSet#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8aeebcc8d7381344fa2aef22570981f1eec38f027962a818c21d82fe0c72ea3c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CloudformationStackSetConfig(
            name=name,
            administration_role_arn=administration_role_arn,
            auto_deployment=auto_deployment,
            call_as=call_as,
            capabilities=capabilities,
            description=description,
            execution_role_name=execution_role_name,
            id=id,
            operation_preferences=operation_preferences,
            parameters=parameters,
            permission_model=permission_model,
            tags=tags,
            tags_all=tags_all,
            template_body=template_body,
            template_url=template_url,
            timeouts=timeouts,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAutoDeployment")
    def put_auto_deployment(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        retain_stacks_on_account_removal: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#enabled CloudformationStackSet#enabled}.
        :param retain_stacks_on_account_removal: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#retain_stacks_on_account_removal CloudformationStackSet#retain_stacks_on_account_removal}.
        '''
        value = CloudformationStackSetAutoDeployment(
            enabled=enabled,
            retain_stacks_on_account_removal=retain_stacks_on_account_removal,
        )

        return typing.cast(None, jsii.invoke(self, "putAutoDeployment", [value]))

    @jsii.member(jsii_name="putOperationPreferences")
    def put_operation_preferences(
        self,
        *,
        failure_tolerance_count: typing.Optional[jsii.Number] = None,
        failure_tolerance_percentage: typing.Optional[jsii.Number] = None,
        max_concurrent_count: typing.Optional[jsii.Number] = None,
        max_concurrent_percentage: typing.Optional[jsii.Number] = None,
        region_concurrency_type: typing.Optional[builtins.str] = None,
        region_order: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param failure_tolerance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#failure_tolerance_count CloudformationStackSet#failure_tolerance_count}.
        :param failure_tolerance_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#failure_tolerance_percentage CloudformationStackSet#failure_tolerance_percentage}.
        :param max_concurrent_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#max_concurrent_count CloudformationStackSet#max_concurrent_count}.
        :param max_concurrent_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#max_concurrent_percentage CloudformationStackSet#max_concurrent_percentage}.
        :param region_concurrency_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#region_concurrency_type CloudformationStackSet#region_concurrency_type}.
        :param region_order: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#region_order CloudformationStackSet#region_order}.
        '''
        value = CloudformationStackSetOperationPreferences(
            failure_tolerance_count=failure_tolerance_count,
            failure_tolerance_percentage=failure_tolerance_percentage,
            max_concurrent_count=max_concurrent_count,
            max_concurrent_percentage=max_concurrent_percentage,
            region_concurrency_type=region_concurrency_type,
            region_order=region_order,
        )

        return typing.cast(None, jsii.invoke(self, "putOperationPreferences", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(self, *, update: typing.Optional[builtins.str] = None) -> None:
        '''
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#update CloudformationStackSet#update}.
        '''
        value = CloudformationStackSetTimeouts(update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAdministrationRoleArn")
    def reset_administration_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdministrationRoleArn", []))

    @jsii.member(jsii_name="resetAutoDeployment")
    def reset_auto_deployment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoDeployment", []))

    @jsii.member(jsii_name="resetCallAs")
    def reset_call_as(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCallAs", []))

    @jsii.member(jsii_name="resetCapabilities")
    def reset_capabilities(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCapabilities", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetExecutionRoleName")
    def reset_execution_role_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExecutionRoleName", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetOperationPreferences")
    def reset_operation_preferences(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperationPreferences", []))

    @jsii.member(jsii_name="resetParameters")
    def reset_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameters", []))

    @jsii.member(jsii_name="resetPermissionModel")
    def reset_permission_model(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPermissionModel", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTemplateBody")
    def reset_template_body(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTemplateBody", []))

    @jsii.member(jsii_name="resetTemplateUrl")
    def reset_template_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTemplateUrl", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

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
    @jsii.member(jsii_name="autoDeployment")
    def auto_deployment(self) -> "CloudformationStackSetAutoDeploymentOutputReference":
        return typing.cast("CloudformationStackSetAutoDeploymentOutputReference", jsii.get(self, "autoDeployment"))

    @builtins.property
    @jsii.member(jsii_name="operationPreferences")
    def operation_preferences(
        self,
    ) -> "CloudformationStackSetOperationPreferencesOutputReference":
        return typing.cast("CloudformationStackSetOperationPreferencesOutputReference", jsii.get(self, "operationPreferences"))

    @builtins.property
    @jsii.member(jsii_name="stackSetId")
    def stack_set_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stackSetId"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "CloudformationStackSetTimeoutsOutputReference":
        return typing.cast("CloudformationStackSetTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="administrationRoleArnInput")
    def administration_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "administrationRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="autoDeploymentInput")
    def auto_deployment_input(
        self,
    ) -> typing.Optional["CloudformationStackSetAutoDeployment"]:
        return typing.cast(typing.Optional["CloudformationStackSetAutoDeployment"], jsii.get(self, "autoDeploymentInput"))

    @builtins.property
    @jsii.member(jsii_name="callAsInput")
    def call_as_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "callAsInput"))

    @builtins.property
    @jsii.member(jsii_name="capabilitiesInput")
    def capabilities_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "capabilitiesInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="executionRoleNameInput")
    def execution_role_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "executionRoleNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="operationPreferencesInput")
    def operation_preferences_input(
        self,
    ) -> typing.Optional["CloudformationStackSetOperationPreferences"]:
        return typing.cast(typing.Optional["CloudformationStackSetOperationPreferences"], jsii.get(self, "operationPreferencesInput"))

    @builtins.property
    @jsii.member(jsii_name="parametersInput")
    def parameters_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "parametersInput"))

    @builtins.property
    @jsii.member(jsii_name="permissionModelInput")
    def permission_model_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "permissionModelInput"))

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
    @jsii.member(jsii_name="templateBodyInput")
    def template_body_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateBodyInput"))

    @builtins.property
    @jsii.member(jsii_name="templateUrlInput")
    def template_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["CloudformationStackSetTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["CloudformationStackSetTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="administrationRoleArn")
    def administration_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "administrationRoleArn"))

    @administration_role_arn.setter
    def administration_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5117f19289e185224a08c7dab4e4286d050c9452d037dd6799d972337a74240)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "administrationRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="callAs")
    def call_as(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "callAs"))

    @call_as.setter
    def call_as(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26c2b610e5782b033a31c45f1842aff1fe736544dee08a3fadb8b0c8fa5e9003)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "callAs", value)

    @builtins.property
    @jsii.member(jsii_name="capabilities")
    def capabilities(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "capabilities"))

    @capabilities.setter
    def capabilities(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6054b6b6b1df6b8fbb58fcf014211d02b5b85eab8677aca100ec42bc4c3c4fa2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capabilities", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__101e6f26dcaacfefce006fc36ac8cd4596a62672ce15609d886c6cf88d64b05d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="executionRoleName")
    def execution_role_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "executionRoleName"))

    @execution_role_name.setter
    def execution_role_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf6a057358bcebd198d1fd3b5222bbaa5bc0413e4d4287dff4afac318e330e41)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionRoleName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9379f7fa652ec5e41ba21916e169d89812d17b7d96914ba24a2857ab586ae626)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d57c5869145454a7f20c981b254992b5ce40a161d02a05dede0b7288be9eda9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e61e3b2f025b14cc07435efb470df526db689d34bd5b936af6a302b4e68ac2ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="permissionModel")
    def permission_model(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "permissionModel"))

    @permission_model.setter
    def permission_model(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05dbfe647ee61396c6d942e9e82e22ce4e45f5bed18c6a59d02edc570411e1e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissionModel", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9d7bf5af7e51a301a5a862b5d1d0f59f08f562ebbf538af08847439271a25a5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__058578588ecc98fe16797930cc8f5543066313f7fd9402467be9033fe9cd3361)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="templateBody")
    def template_body(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "templateBody"))

    @template_body.setter
    def template_body(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63a8c8f03f5ab21e02f6ccd81d97cab18859e9977e29d646619be117599d4480)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateBody", value)

    @builtins.property
    @jsii.member(jsii_name="templateUrl")
    def template_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "templateUrl"))

    @template_url.setter
    def template_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26b82e0fcc9a2608091a9ffb2a9f56f5b203ebee9e74d1635a457e7fb2238a04)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateUrl", value)


@jsii.data_type(
    jsii_type="aws.cloudformationStackSet.CloudformationStackSetAutoDeployment",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "retain_stacks_on_account_removal": "retainStacksOnAccountRemoval",
    },
)
class CloudformationStackSetAutoDeployment:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        retain_stacks_on_account_removal: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#enabled CloudformationStackSet#enabled}.
        :param retain_stacks_on_account_removal: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#retain_stacks_on_account_removal CloudformationStackSet#retain_stacks_on_account_removal}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6759ced3d5d653e79e85f6919897a0c0b9b5ffb99fe8622bf42439d32cda9918)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument retain_stacks_on_account_removal", value=retain_stacks_on_account_removal, expected_type=type_hints["retain_stacks_on_account_removal"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if retain_stacks_on_account_removal is not None:
            self._values["retain_stacks_on_account_removal"] = retain_stacks_on_account_removal

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#enabled CloudformationStackSet#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def retain_stacks_on_account_removal(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#retain_stacks_on_account_removal CloudformationStackSet#retain_stacks_on_account_removal}.'''
        result = self._values.get("retain_stacks_on_account_removal")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudformationStackSetAutoDeployment(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudformationStackSetAutoDeploymentOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudformationStackSet.CloudformationStackSetAutoDeploymentOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bd200df17b1052fa9baf00fed6f411c12e172062ec3bc48ec2268f0c015ca3c7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetRetainStacksOnAccountRemoval")
    def reset_retain_stacks_on_account_removal(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetainStacksOnAccountRemoval", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="retainStacksOnAccountRemovalInput")
    def retain_stacks_on_account_removal_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "retainStacksOnAccountRemovalInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a7a52bbcdca71d8879d4fa8d0a217be7e14b1576c9bb56ba9b0124706aba744)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="retainStacksOnAccountRemoval")
    def retain_stacks_on_account_removal(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "retainStacksOnAccountRemoval"))

    @retain_stacks_on_account_removal.setter
    def retain_stacks_on_account_removal(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9e79609cb200f652039118247e1d7be92c0a74cd3f8357d006b231bc41a86dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retainStacksOnAccountRemoval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudformationStackSetAutoDeployment]:
        return typing.cast(typing.Optional[CloudformationStackSetAutoDeployment], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudformationStackSetAutoDeployment],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33b48ec4eea7255cdd76a1f088d360a22aedb9891d0e583c2d437dd5ebf86d10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cloudformationStackSet.CloudformationStackSetConfig",
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
        "administration_role_arn": "administrationRoleArn",
        "auto_deployment": "autoDeployment",
        "call_as": "callAs",
        "capabilities": "capabilities",
        "description": "description",
        "execution_role_name": "executionRoleName",
        "id": "id",
        "operation_preferences": "operationPreferences",
        "parameters": "parameters",
        "permission_model": "permissionModel",
        "tags": "tags",
        "tags_all": "tagsAll",
        "template_body": "templateBody",
        "template_url": "templateUrl",
        "timeouts": "timeouts",
    },
)
class CloudformationStackSetConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        administration_role_arn: typing.Optional[builtins.str] = None,
        auto_deployment: typing.Optional[typing.Union[CloudformationStackSetAutoDeployment, typing.Dict[builtins.str, typing.Any]]] = None,
        call_as: typing.Optional[builtins.str] = None,
        capabilities: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        execution_role_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        operation_preferences: typing.Optional[typing.Union["CloudformationStackSetOperationPreferences", typing.Dict[builtins.str, typing.Any]]] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        permission_model: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        template_body: typing.Optional[builtins.str] = None,
        template_url: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["CloudformationStackSetTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#name CloudformationStackSet#name}.
        :param administration_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#administration_role_arn CloudformationStackSet#administration_role_arn}.
        :param auto_deployment: auto_deployment block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#auto_deployment CloudformationStackSet#auto_deployment}
        :param call_as: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#call_as CloudformationStackSet#call_as}.
        :param capabilities: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#capabilities CloudformationStackSet#capabilities}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#description CloudformationStackSet#description}.
        :param execution_role_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#execution_role_name CloudformationStackSet#execution_role_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#id CloudformationStackSet#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param operation_preferences: operation_preferences block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#operation_preferences CloudformationStackSet#operation_preferences}
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#parameters CloudformationStackSet#parameters}.
        :param permission_model: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#permission_model CloudformationStackSet#permission_model}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#tags CloudformationStackSet#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#tags_all CloudformationStackSet#tags_all}.
        :param template_body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#template_body CloudformationStackSet#template_body}.
        :param template_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#template_url CloudformationStackSet#template_url}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#timeouts CloudformationStackSet#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(auto_deployment, dict):
            auto_deployment = CloudformationStackSetAutoDeployment(**auto_deployment)
        if isinstance(operation_preferences, dict):
            operation_preferences = CloudformationStackSetOperationPreferences(**operation_preferences)
        if isinstance(timeouts, dict):
            timeouts = CloudformationStackSetTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe1d4b699cee636623f436b549010fee4906e16883968f347ea6212c074163ea)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument administration_role_arn", value=administration_role_arn, expected_type=type_hints["administration_role_arn"])
            check_type(argname="argument auto_deployment", value=auto_deployment, expected_type=type_hints["auto_deployment"])
            check_type(argname="argument call_as", value=call_as, expected_type=type_hints["call_as"])
            check_type(argname="argument capabilities", value=capabilities, expected_type=type_hints["capabilities"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument execution_role_name", value=execution_role_name, expected_type=type_hints["execution_role_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument operation_preferences", value=operation_preferences, expected_type=type_hints["operation_preferences"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument permission_model", value=permission_model, expected_type=type_hints["permission_model"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument template_body", value=template_body, expected_type=type_hints["template_body"])
            check_type(argname="argument template_url", value=template_url, expected_type=type_hints["template_url"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
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
        if administration_role_arn is not None:
            self._values["administration_role_arn"] = administration_role_arn
        if auto_deployment is not None:
            self._values["auto_deployment"] = auto_deployment
        if call_as is not None:
            self._values["call_as"] = call_as
        if capabilities is not None:
            self._values["capabilities"] = capabilities
        if description is not None:
            self._values["description"] = description
        if execution_role_name is not None:
            self._values["execution_role_name"] = execution_role_name
        if id is not None:
            self._values["id"] = id
        if operation_preferences is not None:
            self._values["operation_preferences"] = operation_preferences
        if parameters is not None:
            self._values["parameters"] = parameters
        if permission_model is not None:
            self._values["permission_model"] = permission_model
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if template_body is not None:
            self._values["template_body"] = template_body
        if template_url is not None:
            self._values["template_url"] = template_url
        if timeouts is not None:
            self._values["timeouts"] = timeouts

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#name CloudformationStackSet#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def administration_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#administration_role_arn CloudformationStackSet#administration_role_arn}.'''
        result = self._values.get("administration_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auto_deployment(self) -> typing.Optional[CloudformationStackSetAutoDeployment]:
        '''auto_deployment block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#auto_deployment CloudformationStackSet#auto_deployment}
        '''
        result = self._values.get("auto_deployment")
        return typing.cast(typing.Optional[CloudformationStackSetAutoDeployment], result)

    @builtins.property
    def call_as(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#call_as CloudformationStackSet#call_as}.'''
        result = self._values.get("call_as")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def capabilities(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#capabilities CloudformationStackSet#capabilities}.'''
        result = self._values.get("capabilities")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#description CloudformationStackSet#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def execution_role_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#execution_role_name CloudformationStackSet#execution_role_name}.'''
        result = self._values.get("execution_role_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#id CloudformationStackSet#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operation_preferences(
        self,
    ) -> typing.Optional["CloudformationStackSetOperationPreferences"]:
        '''operation_preferences block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#operation_preferences CloudformationStackSet#operation_preferences}
        '''
        result = self._values.get("operation_preferences")
        return typing.cast(typing.Optional["CloudformationStackSetOperationPreferences"], result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#parameters CloudformationStackSet#parameters}.'''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def permission_model(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#permission_model CloudformationStackSet#permission_model}.'''
        result = self._values.get("permission_model")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#tags CloudformationStackSet#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#tags_all CloudformationStackSet#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def template_body(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#template_body CloudformationStackSet#template_body}.'''
        result = self._values.get("template_body")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def template_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#template_url CloudformationStackSet#template_url}.'''
        result = self._values.get("template_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["CloudformationStackSetTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#timeouts CloudformationStackSet#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["CloudformationStackSetTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudformationStackSetConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.cloudformationStackSet.CloudformationStackSetOperationPreferences",
    jsii_struct_bases=[],
    name_mapping={
        "failure_tolerance_count": "failureToleranceCount",
        "failure_tolerance_percentage": "failureTolerancePercentage",
        "max_concurrent_count": "maxConcurrentCount",
        "max_concurrent_percentage": "maxConcurrentPercentage",
        "region_concurrency_type": "regionConcurrencyType",
        "region_order": "regionOrder",
    },
)
class CloudformationStackSetOperationPreferences:
    def __init__(
        self,
        *,
        failure_tolerance_count: typing.Optional[jsii.Number] = None,
        failure_tolerance_percentage: typing.Optional[jsii.Number] = None,
        max_concurrent_count: typing.Optional[jsii.Number] = None,
        max_concurrent_percentage: typing.Optional[jsii.Number] = None,
        region_concurrency_type: typing.Optional[builtins.str] = None,
        region_order: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param failure_tolerance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#failure_tolerance_count CloudformationStackSet#failure_tolerance_count}.
        :param failure_tolerance_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#failure_tolerance_percentage CloudformationStackSet#failure_tolerance_percentage}.
        :param max_concurrent_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#max_concurrent_count CloudformationStackSet#max_concurrent_count}.
        :param max_concurrent_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#max_concurrent_percentage CloudformationStackSet#max_concurrent_percentage}.
        :param region_concurrency_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#region_concurrency_type CloudformationStackSet#region_concurrency_type}.
        :param region_order: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#region_order CloudformationStackSet#region_order}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab9d3a01d121f222f674174870b8b594f965ae2f3e4a4a0a5ae898fcb473cc28)
            check_type(argname="argument failure_tolerance_count", value=failure_tolerance_count, expected_type=type_hints["failure_tolerance_count"])
            check_type(argname="argument failure_tolerance_percentage", value=failure_tolerance_percentage, expected_type=type_hints["failure_tolerance_percentage"])
            check_type(argname="argument max_concurrent_count", value=max_concurrent_count, expected_type=type_hints["max_concurrent_count"])
            check_type(argname="argument max_concurrent_percentage", value=max_concurrent_percentage, expected_type=type_hints["max_concurrent_percentage"])
            check_type(argname="argument region_concurrency_type", value=region_concurrency_type, expected_type=type_hints["region_concurrency_type"])
            check_type(argname="argument region_order", value=region_order, expected_type=type_hints["region_order"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if failure_tolerance_count is not None:
            self._values["failure_tolerance_count"] = failure_tolerance_count
        if failure_tolerance_percentage is not None:
            self._values["failure_tolerance_percentage"] = failure_tolerance_percentage
        if max_concurrent_count is not None:
            self._values["max_concurrent_count"] = max_concurrent_count
        if max_concurrent_percentage is not None:
            self._values["max_concurrent_percentage"] = max_concurrent_percentage
        if region_concurrency_type is not None:
            self._values["region_concurrency_type"] = region_concurrency_type
        if region_order is not None:
            self._values["region_order"] = region_order

    @builtins.property
    def failure_tolerance_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#failure_tolerance_count CloudformationStackSet#failure_tolerance_count}.'''
        result = self._values.get("failure_tolerance_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def failure_tolerance_percentage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#failure_tolerance_percentage CloudformationStackSet#failure_tolerance_percentage}.'''
        result = self._values.get("failure_tolerance_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_concurrent_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#max_concurrent_count CloudformationStackSet#max_concurrent_count}.'''
        result = self._values.get("max_concurrent_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_concurrent_percentage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#max_concurrent_percentage CloudformationStackSet#max_concurrent_percentage}.'''
        result = self._values.get("max_concurrent_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def region_concurrency_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#region_concurrency_type CloudformationStackSet#region_concurrency_type}.'''
        result = self._values.get("region_concurrency_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region_order(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#region_order CloudformationStackSet#region_order}.'''
        result = self._values.get("region_order")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudformationStackSetOperationPreferences(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudformationStackSetOperationPreferencesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudformationStackSet.CloudformationStackSetOperationPreferencesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c0f5dfb903eb2de3fb9b2cec57bf3d5ca30ac0c1c12e8c3f64cda21410ca4540)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFailureToleranceCount")
    def reset_failure_tolerance_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailureToleranceCount", []))

    @jsii.member(jsii_name="resetFailureTolerancePercentage")
    def reset_failure_tolerance_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailureTolerancePercentage", []))

    @jsii.member(jsii_name="resetMaxConcurrentCount")
    def reset_max_concurrent_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxConcurrentCount", []))

    @jsii.member(jsii_name="resetMaxConcurrentPercentage")
    def reset_max_concurrent_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxConcurrentPercentage", []))

    @jsii.member(jsii_name="resetRegionConcurrencyType")
    def reset_region_concurrency_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegionConcurrencyType", []))

    @jsii.member(jsii_name="resetRegionOrder")
    def reset_region_order(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegionOrder", []))

    @builtins.property
    @jsii.member(jsii_name="failureToleranceCountInput")
    def failure_tolerance_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "failureToleranceCountInput"))

    @builtins.property
    @jsii.member(jsii_name="failureTolerancePercentageInput")
    def failure_tolerance_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "failureTolerancePercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="maxConcurrentCountInput")
    def max_concurrent_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxConcurrentCountInput"))

    @builtins.property
    @jsii.member(jsii_name="maxConcurrentPercentageInput")
    def max_concurrent_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxConcurrentPercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="regionConcurrencyTypeInput")
    def region_concurrency_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionConcurrencyTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="regionOrderInput")
    def region_order_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "regionOrderInput"))

    @builtins.property
    @jsii.member(jsii_name="failureToleranceCount")
    def failure_tolerance_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "failureToleranceCount"))

    @failure_tolerance_count.setter
    def failure_tolerance_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a8e94aae2481dc6efa689c0f7a1bfe33c6a2961b0377327cb6db640c2fbdb08)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failureToleranceCount", value)

    @builtins.property
    @jsii.member(jsii_name="failureTolerancePercentage")
    def failure_tolerance_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "failureTolerancePercentage"))

    @failure_tolerance_percentage.setter
    def failure_tolerance_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d191d5625eee028b16908f840306ba61b4590d355082b91e3f65881106df61a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failureTolerancePercentage", value)

    @builtins.property
    @jsii.member(jsii_name="maxConcurrentCount")
    def max_concurrent_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConcurrentCount"))

    @max_concurrent_count.setter
    def max_concurrent_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1621b4464f0a23eb8fcb0356687143fe877299d03ebecb780c9dde7b3eea1400)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConcurrentCount", value)

    @builtins.property
    @jsii.member(jsii_name="maxConcurrentPercentage")
    def max_concurrent_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConcurrentPercentage"))

    @max_concurrent_percentage.setter
    def max_concurrent_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e420e3e9b78fe6dd7c797751074dc4c9dc9f5017fd12009805993b8f6c614d85)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConcurrentPercentage", value)

    @builtins.property
    @jsii.member(jsii_name="regionConcurrencyType")
    def region_concurrency_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "regionConcurrencyType"))

    @region_concurrency_type.setter
    def region_concurrency_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06878e0e303124a29665477f06890392d59fa015f31ba788c3875a795c1008b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regionConcurrencyType", value)

    @builtins.property
    @jsii.member(jsii_name="regionOrder")
    def region_order(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "regionOrder"))

    @region_order.setter
    def region_order(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ab5e84f1cc553747312b52467f2ba731dc072d3a2d567bcf25e256856b9311f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regionOrder", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudformationStackSetOperationPreferences]:
        return typing.cast(typing.Optional[CloudformationStackSetOperationPreferences], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudformationStackSetOperationPreferences],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f31d148fb56b5186262324351401428c5a20876937f6317d2581271b4299eee2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cloudformationStackSet.CloudformationStackSetTimeouts",
    jsii_struct_bases=[],
    name_mapping={"update": "update"},
)
class CloudformationStackSetTimeouts:
    def __init__(self, *, update: typing.Optional[builtins.str] = None) -> None:
        '''
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#update CloudformationStackSet#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__608a9ee454168d8c20b60f92a5883243dc1cdf57152ac3baf388b7f8c6537ff8)
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#update CloudformationStackSet#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudformationStackSetTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudformationStackSetTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudformationStackSet.CloudformationStackSetTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b9b0715431f9c1d188abec26c97dceb04639c483dc81127a9a585d1bc77ab25d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2bc8384567917eebc8f5bdbfccbd8ac3124bd14c00671f7ee47c8e894e727a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CloudformationStackSetTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CloudformationStackSetTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CloudformationStackSetTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f830b6639e552c34965fdf7b3ada6ff7eca2522035ef2db88a3f2fc60b35a75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CloudformationStackSet",
    "CloudformationStackSetAutoDeployment",
    "CloudformationStackSetAutoDeploymentOutputReference",
    "CloudformationStackSetConfig",
    "CloudformationStackSetOperationPreferences",
    "CloudformationStackSetOperationPreferencesOutputReference",
    "CloudformationStackSetTimeouts",
    "CloudformationStackSetTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__8aeebcc8d7381344fa2aef22570981f1eec38f027962a818c21d82fe0c72ea3c(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    administration_role_arn: typing.Optional[builtins.str] = None,
    auto_deployment: typing.Optional[typing.Union[CloudformationStackSetAutoDeployment, typing.Dict[builtins.str, typing.Any]]] = None,
    call_as: typing.Optional[builtins.str] = None,
    capabilities: typing.Optional[typing.Sequence[builtins.str]] = None,
    description: typing.Optional[builtins.str] = None,
    execution_role_name: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    operation_preferences: typing.Optional[typing.Union[CloudformationStackSetOperationPreferences, typing.Dict[builtins.str, typing.Any]]] = None,
    parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    permission_model: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    template_body: typing.Optional[builtins.str] = None,
    template_url: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[CloudformationStackSetTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__e5117f19289e185224a08c7dab4e4286d050c9452d037dd6799d972337a74240(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26c2b610e5782b033a31c45f1842aff1fe736544dee08a3fadb8b0c8fa5e9003(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6054b6b6b1df6b8fbb58fcf014211d02b5b85eab8677aca100ec42bc4c3c4fa2(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__101e6f26dcaacfefce006fc36ac8cd4596a62672ce15609d886c6cf88d64b05d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf6a057358bcebd198d1fd3b5222bbaa5bc0413e4d4287dff4afac318e330e41(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9379f7fa652ec5e41ba21916e169d89812d17b7d96914ba24a2857ab586ae626(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d57c5869145454a7f20c981b254992b5ce40a161d02a05dede0b7288be9eda9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e61e3b2f025b14cc07435efb470df526db689d34bd5b936af6a302b4e68ac2ec(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05dbfe647ee61396c6d942e9e82e22ce4e45f5bed18c6a59d02edc570411e1e8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9d7bf5af7e51a301a5a862b5d1d0f59f08f562ebbf538af08847439271a25a5(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__058578588ecc98fe16797930cc8f5543066313f7fd9402467be9033fe9cd3361(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63a8c8f03f5ab21e02f6ccd81d97cab18859e9977e29d646619be117599d4480(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26b82e0fcc9a2608091a9ffb2a9f56f5b203ebee9e74d1635a457e7fb2238a04(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6759ced3d5d653e79e85f6919897a0c0b9b5ffb99fe8622bf42439d32cda9918(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    retain_stacks_on_account_removal: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd200df17b1052fa9baf00fed6f411c12e172062ec3bc48ec2268f0c015ca3c7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a7a52bbcdca71d8879d4fa8d0a217be7e14b1576c9bb56ba9b0124706aba744(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9e79609cb200f652039118247e1d7be92c0a74cd3f8357d006b231bc41a86dd(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33b48ec4eea7255cdd76a1f088d360a22aedb9891d0e583c2d437dd5ebf86d10(
    value: typing.Optional[CloudformationStackSetAutoDeployment],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe1d4b699cee636623f436b549010fee4906e16883968f347ea6212c074163ea(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    administration_role_arn: typing.Optional[builtins.str] = None,
    auto_deployment: typing.Optional[typing.Union[CloudformationStackSetAutoDeployment, typing.Dict[builtins.str, typing.Any]]] = None,
    call_as: typing.Optional[builtins.str] = None,
    capabilities: typing.Optional[typing.Sequence[builtins.str]] = None,
    description: typing.Optional[builtins.str] = None,
    execution_role_name: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    operation_preferences: typing.Optional[typing.Union[CloudformationStackSetOperationPreferences, typing.Dict[builtins.str, typing.Any]]] = None,
    parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    permission_model: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    template_body: typing.Optional[builtins.str] = None,
    template_url: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[CloudformationStackSetTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab9d3a01d121f222f674174870b8b594f965ae2f3e4a4a0a5ae898fcb473cc28(
    *,
    failure_tolerance_count: typing.Optional[jsii.Number] = None,
    failure_tolerance_percentage: typing.Optional[jsii.Number] = None,
    max_concurrent_count: typing.Optional[jsii.Number] = None,
    max_concurrent_percentage: typing.Optional[jsii.Number] = None,
    region_concurrency_type: typing.Optional[builtins.str] = None,
    region_order: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0f5dfb903eb2de3fb9b2cec57bf3d5ca30ac0c1c12e8c3f64cda21410ca4540(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a8e94aae2481dc6efa689c0f7a1bfe33c6a2961b0377327cb6db640c2fbdb08(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d191d5625eee028b16908f840306ba61b4590d355082b91e3f65881106df61a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1621b4464f0a23eb8fcb0356687143fe877299d03ebecb780c9dde7b3eea1400(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e420e3e9b78fe6dd7c797751074dc4c9dc9f5017fd12009805993b8f6c614d85(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06878e0e303124a29665477f06890392d59fa015f31ba788c3875a795c1008b9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ab5e84f1cc553747312b52467f2ba731dc072d3a2d567bcf25e256856b9311f(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f31d148fb56b5186262324351401428c5a20876937f6317d2581271b4299eee2(
    value: typing.Optional[CloudformationStackSetOperationPreferences],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__608a9ee454168d8c20b60f92a5883243dc1cdf57152ac3baf388b7f8c6537ff8(
    *,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9b0715431f9c1d188abec26c97dceb04639c483dc81127a9a585d1bc77ab25d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2bc8384567917eebc8f5bdbfccbd8ac3124bd14c00671f7ee47c8e894e727a2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f830b6639e552c34965fdf7b3ada6ff7eca2522035ef2db88a3f2fc60b35a75(
    value: typing.Optional[typing.Union[CloudformationStackSetTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
