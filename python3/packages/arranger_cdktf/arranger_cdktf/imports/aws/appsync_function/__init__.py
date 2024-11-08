'''
# `aws_appsync_function`

Refer to the Terraform Registory for docs: [`aws_appsync_function`](https://www.terraform.io/docs/providers/aws/r/appsync_function).
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


class AppsyncFunction(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appsyncFunction.AppsyncFunction",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/appsync_function aws_appsync_function}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        api_id: builtins.str,
        data_source: builtins.str,
        name: builtins.str,
        code: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        function_version: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        max_batch_size: typing.Optional[jsii.Number] = None,
        request_mapping_template: typing.Optional[builtins.str] = None,
        response_mapping_template: typing.Optional[builtins.str] = None,
        runtime: typing.Optional[typing.Union["AppsyncFunctionRuntime", typing.Dict[builtins.str, typing.Any]]] = None,
        sync_config: typing.Optional[typing.Union["AppsyncFunctionSyncConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/appsync_function aws_appsync_function} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param api_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#api_id AppsyncFunction#api_id}.
        :param data_source: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#data_source AppsyncFunction#data_source}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#name AppsyncFunction#name}.
        :param code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#code AppsyncFunction#code}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#description AppsyncFunction#description}.
        :param function_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#function_version AppsyncFunction#function_version}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#id AppsyncFunction#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param max_batch_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#max_batch_size AppsyncFunction#max_batch_size}.
        :param request_mapping_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#request_mapping_template AppsyncFunction#request_mapping_template}.
        :param response_mapping_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#response_mapping_template AppsyncFunction#response_mapping_template}.
        :param runtime: runtime block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#runtime AppsyncFunction#runtime}
        :param sync_config: sync_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#sync_config AppsyncFunction#sync_config}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a965e81a9c3f5c5dad09403ba0166bbbbe0fd9a4eae37a51fc52326d5ac9892)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AppsyncFunctionConfig(
            api_id=api_id,
            data_source=data_source,
            name=name,
            code=code,
            description=description,
            function_version=function_version,
            id=id,
            max_batch_size=max_batch_size,
            request_mapping_template=request_mapping_template,
            response_mapping_template=response_mapping_template,
            runtime=runtime,
            sync_config=sync_config,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putRuntime")
    def put_runtime(self, *, name: builtins.str, runtime_version: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#name AppsyncFunction#name}.
        :param runtime_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#runtime_version AppsyncFunction#runtime_version}.
        '''
        value = AppsyncFunctionRuntime(name=name, runtime_version=runtime_version)

        return typing.cast(None, jsii.invoke(self, "putRuntime", [value]))

    @jsii.member(jsii_name="putSyncConfig")
    def put_sync_config(
        self,
        *,
        conflict_detection: typing.Optional[builtins.str] = None,
        conflict_handler: typing.Optional[builtins.str] = None,
        lambda_conflict_handler_config: typing.Optional[typing.Union["AppsyncFunctionSyncConfigLambdaConflictHandlerConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param conflict_detection: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#conflict_detection AppsyncFunction#conflict_detection}.
        :param conflict_handler: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#conflict_handler AppsyncFunction#conflict_handler}.
        :param lambda_conflict_handler_config: lambda_conflict_handler_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#lambda_conflict_handler_config AppsyncFunction#lambda_conflict_handler_config}
        '''
        value = AppsyncFunctionSyncConfig(
            conflict_detection=conflict_detection,
            conflict_handler=conflict_handler,
            lambda_conflict_handler_config=lambda_conflict_handler_config,
        )

        return typing.cast(None, jsii.invoke(self, "putSyncConfig", [value]))

    @jsii.member(jsii_name="resetCode")
    def reset_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCode", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetFunctionVersion")
    def reset_function_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFunctionVersion", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMaxBatchSize")
    def reset_max_batch_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxBatchSize", []))

    @jsii.member(jsii_name="resetRequestMappingTemplate")
    def reset_request_mapping_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestMappingTemplate", []))

    @jsii.member(jsii_name="resetResponseMappingTemplate")
    def reset_response_mapping_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseMappingTemplate", []))

    @jsii.member(jsii_name="resetRuntime")
    def reset_runtime(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRuntime", []))

    @jsii.member(jsii_name="resetSyncConfig")
    def reset_sync_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSyncConfig", []))

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
    @jsii.member(jsii_name="functionId")
    def function_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "functionId"))

    @builtins.property
    @jsii.member(jsii_name="runtime")
    def runtime(self) -> "AppsyncFunctionRuntimeOutputReference":
        return typing.cast("AppsyncFunctionRuntimeOutputReference", jsii.get(self, "runtime"))

    @builtins.property
    @jsii.member(jsii_name="syncConfig")
    def sync_config(self) -> "AppsyncFunctionSyncConfigOutputReference":
        return typing.cast("AppsyncFunctionSyncConfigOutputReference", jsii.get(self, "syncConfig"))

    @builtins.property
    @jsii.member(jsii_name="apiIdInput")
    def api_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiIdInput"))

    @builtins.property
    @jsii.member(jsii_name="codeInput")
    def code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "codeInput"))

    @builtins.property
    @jsii.member(jsii_name="dataSourceInput")
    def data_source_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataSourceInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="functionVersionInput")
    def function_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "functionVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="maxBatchSizeInput")
    def max_batch_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxBatchSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="requestMappingTemplateInput")
    def request_mapping_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "requestMappingTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="responseMappingTemplateInput")
    def response_mapping_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "responseMappingTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="runtimeInput")
    def runtime_input(self) -> typing.Optional["AppsyncFunctionRuntime"]:
        return typing.cast(typing.Optional["AppsyncFunctionRuntime"], jsii.get(self, "runtimeInput"))

    @builtins.property
    @jsii.member(jsii_name="syncConfigInput")
    def sync_config_input(self) -> typing.Optional["AppsyncFunctionSyncConfig"]:
        return typing.cast(typing.Optional["AppsyncFunctionSyncConfig"], jsii.get(self, "syncConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiId"))

    @api_id.setter
    def api_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79eb4b5008dc9db0c51cd0bfb8c3bc792e6f507f3dc38e3eb57d2dad28b5c23e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="code")
    def code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "code"))

    @code.setter
    def code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95272da1fffdc01b5cd529a4b055e2840d423a0aafff0dd85798fc9de6b6bb1b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "code", value)

    @builtins.property
    @jsii.member(jsii_name="dataSource")
    def data_source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataSource"))

    @data_source.setter
    def data_source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__671cac51c517d442aeefd72ae225fe85abbbdcb37be67b5494ca44837c1be19a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataSource", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fd3558354e4f4ec6bf7370d4aa62b1f5f47ce6dc10121681369c9e51e5fb08b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="functionVersion")
    def function_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "functionVersion"))

    @function_version.setter
    def function_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94994cad0b830850f6686e35967d2d2d94685b734eb2708e7814db3b59fc4e03)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "functionVersion", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccbfc0e3208d8917e18dff4f5910f27d8326bbeb8cc603dd0494a6d076ba1a89)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="maxBatchSize")
    def max_batch_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxBatchSize"))

    @max_batch_size.setter
    def max_batch_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b2f1e2c46408b251e8508c72b819476ab0360592de576562fd248c0300457f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxBatchSize", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__590fdaec36bb9cd7aa8c33a95adaa176e8b68ff4b075898bd7ba90cef9575455)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="requestMappingTemplate")
    def request_mapping_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "requestMappingTemplate"))

    @request_mapping_template.setter
    def request_mapping_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64fc1fdb39086a754b85161a736fd333e823239082796fab44bf2f405ec419d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestMappingTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="responseMappingTemplate")
    def response_mapping_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "responseMappingTemplate"))

    @response_mapping_template.setter
    def response_mapping_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62d3cd534bb3d54c2134569b7edb1e17f8f2aa7ae0bfe5a49fcf873aafde50bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseMappingTemplate", value)


@jsii.data_type(
    jsii_type="aws.appsyncFunction.AppsyncFunctionConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "api_id": "apiId",
        "data_source": "dataSource",
        "name": "name",
        "code": "code",
        "description": "description",
        "function_version": "functionVersion",
        "id": "id",
        "max_batch_size": "maxBatchSize",
        "request_mapping_template": "requestMappingTemplate",
        "response_mapping_template": "responseMappingTemplate",
        "runtime": "runtime",
        "sync_config": "syncConfig",
    },
)
class AppsyncFunctionConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        api_id: builtins.str,
        data_source: builtins.str,
        name: builtins.str,
        code: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        function_version: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        max_batch_size: typing.Optional[jsii.Number] = None,
        request_mapping_template: typing.Optional[builtins.str] = None,
        response_mapping_template: typing.Optional[builtins.str] = None,
        runtime: typing.Optional[typing.Union["AppsyncFunctionRuntime", typing.Dict[builtins.str, typing.Any]]] = None,
        sync_config: typing.Optional[typing.Union["AppsyncFunctionSyncConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param api_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#api_id AppsyncFunction#api_id}.
        :param data_source: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#data_source AppsyncFunction#data_source}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#name AppsyncFunction#name}.
        :param code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#code AppsyncFunction#code}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#description AppsyncFunction#description}.
        :param function_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#function_version AppsyncFunction#function_version}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#id AppsyncFunction#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param max_batch_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#max_batch_size AppsyncFunction#max_batch_size}.
        :param request_mapping_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#request_mapping_template AppsyncFunction#request_mapping_template}.
        :param response_mapping_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#response_mapping_template AppsyncFunction#response_mapping_template}.
        :param runtime: runtime block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#runtime AppsyncFunction#runtime}
        :param sync_config: sync_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#sync_config AppsyncFunction#sync_config}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(runtime, dict):
            runtime = AppsyncFunctionRuntime(**runtime)
        if isinstance(sync_config, dict):
            sync_config = AppsyncFunctionSyncConfig(**sync_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b1dbe93e8f36bc4a5cb06ad83972c98473e53d08e802ce6bc8b427ef4cc3616)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument api_id", value=api_id, expected_type=type_hints["api_id"])
            check_type(argname="argument data_source", value=data_source, expected_type=type_hints["data_source"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument code", value=code, expected_type=type_hints["code"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument function_version", value=function_version, expected_type=type_hints["function_version"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument max_batch_size", value=max_batch_size, expected_type=type_hints["max_batch_size"])
            check_type(argname="argument request_mapping_template", value=request_mapping_template, expected_type=type_hints["request_mapping_template"])
            check_type(argname="argument response_mapping_template", value=response_mapping_template, expected_type=type_hints["response_mapping_template"])
            check_type(argname="argument runtime", value=runtime, expected_type=type_hints["runtime"])
            check_type(argname="argument sync_config", value=sync_config, expected_type=type_hints["sync_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_id": api_id,
            "data_source": data_source,
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
        if code is not None:
            self._values["code"] = code
        if description is not None:
            self._values["description"] = description
        if function_version is not None:
            self._values["function_version"] = function_version
        if id is not None:
            self._values["id"] = id
        if max_batch_size is not None:
            self._values["max_batch_size"] = max_batch_size
        if request_mapping_template is not None:
            self._values["request_mapping_template"] = request_mapping_template
        if response_mapping_template is not None:
            self._values["response_mapping_template"] = response_mapping_template
        if runtime is not None:
            self._values["runtime"] = runtime
        if sync_config is not None:
            self._values["sync_config"] = sync_config

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
    def api_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#api_id AppsyncFunction#api_id}.'''
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_source(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#data_source AppsyncFunction#data_source}.'''
        result = self._values.get("data_source")
        assert result is not None, "Required property 'data_source' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#name AppsyncFunction#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def code(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#code AppsyncFunction#code}.'''
        result = self._values.get("code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#description AppsyncFunction#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def function_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#function_version AppsyncFunction#function_version}.'''
        result = self._values.get("function_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#id AppsyncFunction#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_batch_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#max_batch_size AppsyncFunction#max_batch_size}.'''
        result = self._values.get("max_batch_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def request_mapping_template(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#request_mapping_template AppsyncFunction#request_mapping_template}.'''
        result = self._values.get("request_mapping_template")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def response_mapping_template(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#response_mapping_template AppsyncFunction#response_mapping_template}.'''
        result = self._values.get("response_mapping_template")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def runtime(self) -> typing.Optional["AppsyncFunctionRuntime"]:
        '''runtime block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#runtime AppsyncFunction#runtime}
        '''
        result = self._values.get("runtime")
        return typing.cast(typing.Optional["AppsyncFunctionRuntime"], result)

    @builtins.property
    def sync_config(self) -> typing.Optional["AppsyncFunctionSyncConfig"]:
        '''sync_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#sync_config AppsyncFunction#sync_config}
        '''
        result = self._values.get("sync_config")
        return typing.cast(typing.Optional["AppsyncFunctionSyncConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncFunctionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appsyncFunction.AppsyncFunctionRuntime",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "runtime_version": "runtimeVersion"},
)
class AppsyncFunctionRuntime:
    def __init__(self, *, name: builtins.str, runtime_version: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#name AppsyncFunction#name}.
        :param runtime_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#runtime_version AppsyncFunction#runtime_version}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d30a06c8e63d63c3db5ec61d90538c5bf45d2fc6b5143f396ea70cffccc5b84e)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument runtime_version", value=runtime_version, expected_type=type_hints["runtime_version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "runtime_version": runtime_version,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#name AppsyncFunction#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def runtime_version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#runtime_version AppsyncFunction#runtime_version}.'''
        result = self._values.get("runtime_version")
        assert result is not None, "Required property 'runtime_version' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncFunctionRuntime(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppsyncFunctionRuntimeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appsyncFunction.AppsyncFunctionRuntimeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e6a61448ae21cf431e808acb270748983a58fd7d27ecd6b35a67128f51516e3e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="runtimeVersionInput")
    def runtime_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "runtimeVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e3d9b4e6d3c9b09f3ccc5d9b3166a22b1984c743a011e96e0f6653bc0623955)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="runtimeVersion")
    def runtime_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "runtimeVersion"))

    @runtime_version.setter
    def runtime_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cabb0c199e3fb7a3115559a70be8ade439a929fe309aacbd9634f7499a3862f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runtimeVersion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppsyncFunctionRuntime]:
        return typing.cast(typing.Optional[AppsyncFunctionRuntime], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[AppsyncFunctionRuntime]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2990156d440dbc446a00f84b957b40b2bde287a1e93c5c469c3c887f0ae4cd84)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appsyncFunction.AppsyncFunctionSyncConfig",
    jsii_struct_bases=[],
    name_mapping={
        "conflict_detection": "conflictDetection",
        "conflict_handler": "conflictHandler",
        "lambda_conflict_handler_config": "lambdaConflictHandlerConfig",
    },
)
class AppsyncFunctionSyncConfig:
    def __init__(
        self,
        *,
        conflict_detection: typing.Optional[builtins.str] = None,
        conflict_handler: typing.Optional[builtins.str] = None,
        lambda_conflict_handler_config: typing.Optional[typing.Union["AppsyncFunctionSyncConfigLambdaConflictHandlerConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param conflict_detection: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#conflict_detection AppsyncFunction#conflict_detection}.
        :param conflict_handler: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#conflict_handler AppsyncFunction#conflict_handler}.
        :param lambda_conflict_handler_config: lambda_conflict_handler_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#lambda_conflict_handler_config AppsyncFunction#lambda_conflict_handler_config}
        '''
        if isinstance(lambda_conflict_handler_config, dict):
            lambda_conflict_handler_config = AppsyncFunctionSyncConfigLambdaConflictHandlerConfig(**lambda_conflict_handler_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__350a50a22280e4ff99ba2c56a38d4f7bf54ccef656024b4153027acf5a549345)
            check_type(argname="argument conflict_detection", value=conflict_detection, expected_type=type_hints["conflict_detection"])
            check_type(argname="argument conflict_handler", value=conflict_handler, expected_type=type_hints["conflict_handler"])
            check_type(argname="argument lambda_conflict_handler_config", value=lambda_conflict_handler_config, expected_type=type_hints["lambda_conflict_handler_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if conflict_detection is not None:
            self._values["conflict_detection"] = conflict_detection
        if conflict_handler is not None:
            self._values["conflict_handler"] = conflict_handler
        if lambda_conflict_handler_config is not None:
            self._values["lambda_conflict_handler_config"] = lambda_conflict_handler_config

    @builtins.property
    def conflict_detection(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#conflict_detection AppsyncFunction#conflict_detection}.'''
        result = self._values.get("conflict_detection")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def conflict_handler(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#conflict_handler AppsyncFunction#conflict_handler}.'''
        result = self._values.get("conflict_handler")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lambda_conflict_handler_config(
        self,
    ) -> typing.Optional["AppsyncFunctionSyncConfigLambdaConflictHandlerConfig"]:
        '''lambda_conflict_handler_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#lambda_conflict_handler_config AppsyncFunction#lambda_conflict_handler_config}
        '''
        result = self._values.get("lambda_conflict_handler_config")
        return typing.cast(typing.Optional["AppsyncFunctionSyncConfigLambdaConflictHandlerConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncFunctionSyncConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appsyncFunction.AppsyncFunctionSyncConfigLambdaConflictHandlerConfig",
    jsii_struct_bases=[],
    name_mapping={"lambda_conflict_handler_arn": "lambdaConflictHandlerArn"},
)
class AppsyncFunctionSyncConfigLambdaConflictHandlerConfig:
    def __init__(
        self,
        *,
        lambda_conflict_handler_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param lambda_conflict_handler_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#lambda_conflict_handler_arn AppsyncFunction#lambda_conflict_handler_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a15df30ce0c6c4c65bcc01c2642dc352f9df1636c499396f869ec6771e8585a)
            check_type(argname="argument lambda_conflict_handler_arn", value=lambda_conflict_handler_arn, expected_type=type_hints["lambda_conflict_handler_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if lambda_conflict_handler_arn is not None:
            self._values["lambda_conflict_handler_arn"] = lambda_conflict_handler_arn

    @builtins.property
    def lambda_conflict_handler_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#lambda_conflict_handler_arn AppsyncFunction#lambda_conflict_handler_arn}.'''
        result = self._values.get("lambda_conflict_handler_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncFunctionSyncConfigLambdaConflictHandlerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppsyncFunctionSyncConfigLambdaConflictHandlerConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appsyncFunction.AppsyncFunctionSyncConfigLambdaConflictHandlerConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d78171693153e6f9ba65dd8081cbdc174babd45bda3b4e3f46904feffb1bfe92)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetLambdaConflictHandlerArn")
    def reset_lambda_conflict_handler_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLambdaConflictHandlerArn", []))

    @builtins.property
    @jsii.member(jsii_name="lambdaConflictHandlerArnInput")
    def lambda_conflict_handler_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lambdaConflictHandlerArnInput"))

    @builtins.property
    @jsii.member(jsii_name="lambdaConflictHandlerArn")
    def lambda_conflict_handler_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lambdaConflictHandlerArn"))

    @lambda_conflict_handler_arn.setter
    def lambda_conflict_handler_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9eb3818087faa7ee96128117d872ad081f26a6bba46be3589d86be9aa45d594d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lambdaConflictHandlerArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppsyncFunctionSyncConfigLambdaConflictHandlerConfig]:
        return typing.cast(typing.Optional[AppsyncFunctionSyncConfigLambdaConflictHandlerConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppsyncFunctionSyncConfigLambdaConflictHandlerConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3fb76176ad8a1f6af57a35fd419fffed052a88946ef67dbce9c216478fc1d5f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppsyncFunctionSyncConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appsyncFunction.AppsyncFunctionSyncConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8b0bec52e29fa9264d91acab044dee2d28719c5f478745f2ee4346960ad7f32f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putLambdaConflictHandlerConfig")
    def put_lambda_conflict_handler_config(
        self,
        *,
        lambda_conflict_handler_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param lambda_conflict_handler_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_function#lambda_conflict_handler_arn AppsyncFunction#lambda_conflict_handler_arn}.
        '''
        value = AppsyncFunctionSyncConfigLambdaConflictHandlerConfig(
            lambda_conflict_handler_arn=lambda_conflict_handler_arn
        )

        return typing.cast(None, jsii.invoke(self, "putLambdaConflictHandlerConfig", [value]))

    @jsii.member(jsii_name="resetConflictDetection")
    def reset_conflict_detection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConflictDetection", []))

    @jsii.member(jsii_name="resetConflictHandler")
    def reset_conflict_handler(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConflictHandler", []))

    @jsii.member(jsii_name="resetLambdaConflictHandlerConfig")
    def reset_lambda_conflict_handler_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLambdaConflictHandlerConfig", []))

    @builtins.property
    @jsii.member(jsii_name="lambdaConflictHandlerConfig")
    def lambda_conflict_handler_config(
        self,
    ) -> AppsyncFunctionSyncConfigLambdaConflictHandlerConfigOutputReference:
        return typing.cast(AppsyncFunctionSyncConfigLambdaConflictHandlerConfigOutputReference, jsii.get(self, "lambdaConflictHandlerConfig"))

    @builtins.property
    @jsii.member(jsii_name="conflictDetectionInput")
    def conflict_detection_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "conflictDetectionInput"))

    @builtins.property
    @jsii.member(jsii_name="conflictHandlerInput")
    def conflict_handler_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "conflictHandlerInput"))

    @builtins.property
    @jsii.member(jsii_name="lambdaConflictHandlerConfigInput")
    def lambda_conflict_handler_config_input(
        self,
    ) -> typing.Optional[AppsyncFunctionSyncConfigLambdaConflictHandlerConfig]:
        return typing.cast(typing.Optional[AppsyncFunctionSyncConfigLambdaConflictHandlerConfig], jsii.get(self, "lambdaConflictHandlerConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="conflictDetection")
    def conflict_detection(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "conflictDetection"))

    @conflict_detection.setter
    def conflict_detection(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8379e6bf550c8e38852626509eb8ffa6584b53830e3456299bc2551dd8469778)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "conflictDetection", value)

    @builtins.property
    @jsii.member(jsii_name="conflictHandler")
    def conflict_handler(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "conflictHandler"))

    @conflict_handler.setter
    def conflict_handler(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddfb18df3db4fb2724caccc34ff2fcf45dc6ae064659c5c56029e48d791a182c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "conflictHandler", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppsyncFunctionSyncConfig]:
        return typing.cast(typing.Optional[AppsyncFunctionSyncConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[AppsyncFunctionSyncConfig]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89c6946e37eb6423c8b602b2d4d6da2d716b01225ff4455374acaae06e8a45cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "AppsyncFunction",
    "AppsyncFunctionConfig",
    "AppsyncFunctionRuntime",
    "AppsyncFunctionRuntimeOutputReference",
    "AppsyncFunctionSyncConfig",
    "AppsyncFunctionSyncConfigLambdaConflictHandlerConfig",
    "AppsyncFunctionSyncConfigLambdaConflictHandlerConfigOutputReference",
    "AppsyncFunctionSyncConfigOutputReference",
]

publication.publish()

def _typecheckingstub__4a965e81a9c3f5c5dad09403ba0166bbbbe0fd9a4eae37a51fc52326d5ac9892(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    api_id: builtins.str,
    data_source: builtins.str,
    name: builtins.str,
    code: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    function_version: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    max_batch_size: typing.Optional[jsii.Number] = None,
    request_mapping_template: typing.Optional[builtins.str] = None,
    response_mapping_template: typing.Optional[builtins.str] = None,
    runtime: typing.Optional[typing.Union[AppsyncFunctionRuntime, typing.Dict[builtins.str, typing.Any]]] = None,
    sync_config: typing.Optional[typing.Union[AppsyncFunctionSyncConfig, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__79eb4b5008dc9db0c51cd0bfb8c3bc792e6f507f3dc38e3eb57d2dad28b5c23e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95272da1fffdc01b5cd529a4b055e2840d423a0aafff0dd85798fc9de6b6bb1b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__671cac51c517d442aeefd72ae225fe85abbbdcb37be67b5494ca44837c1be19a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fd3558354e4f4ec6bf7370d4aa62b1f5f47ce6dc10121681369c9e51e5fb08b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94994cad0b830850f6686e35967d2d2d94685b734eb2708e7814db3b59fc4e03(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccbfc0e3208d8917e18dff4f5910f27d8326bbeb8cc603dd0494a6d076ba1a89(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b2f1e2c46408b251e8508c72b819476ab0360592de576562fd248c0300457f7(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__590fdaec36bb9cd7aa8c33a95adaa176e8b68ff4b075898bd7ba90cef9575455(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64fc1fdb39086a754b85161a736fd333e823239082796fab44bf2f405ec419d4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62d3cd534bb3d54c2134569b7edb1e17f8f2aa7ae0bfe5a49fcf873aafde50bb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b1dbe93e8f36bc4a5cb06ad83972c98473e53d08e802ce6bc8b427ef4cc3616(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    api_id: builtins.str,
    data_source: builtins.str,
    name: builtins.str,
    code: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    function_version: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    max_batch_size: typing.Optional[jsii.Number] = None,
    request_mapping_template: typing.Optional[builtins.str] = None,
    response_mapping_template: typing.Optional[builtins.str] = None,
    runtime: typing.Optional[typing.Union[AppsyncFunctionRuntime, typing.Dict[builtins.str, typing.Any]]] = None,
    sync_config: typing.Optional[typing.Union[AppsyncFunctionSyncConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d30a06c8e63d63c3db5ec61d90538c5bf45d2fc6b5143f396ea70cffccc5b84e(
    *,
    name: builtins.str,
    runtime_version: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6a61448ae21cf431e808acb270748983a58fd7d27ecd6b35a67128f51516e3e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e3d9b4e6d3c9b09f3ccc5d9b3166a22b1984c743a011e96e0f6653bc0623955(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cabb0c199e3fb7a3115559a70be8ade439a929fe309aacbd9634f7499a3862f4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2990156d440dbc446a00f84b957b40b2bde287a1e93c5c469c3c887f0ae4cd84(
    value: typing.Optional[AppsyncFunctionRuntime],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__350a50a22280e4ff99ba2c56a38d4f7bf54ccef656024b4153027acf5a549345(
    *,
    conflict_detection: typing.Optional[builtins.str] = None,
    conflict_handler: typing.Optional[builtins.str] = None,
    lambda_conflict_handler_config: typing.Optional[typing.Union[AppsyncFunctionSyncConfigLambdaConflictHandlerConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a15df30ce0c6c4c65bcc01c2642dc352f9df1636c499396f869ec6771e8585a(
    *,
    lambda_conflict_handler_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d78171693153e6f9ba65dd8081cbdc174babd45bda3b4e3f46904feffb1bfe92(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9eb3818087faa7ee96128117d872ad081f26a6bba46be3589d86be9aa45d594d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3fb76176ad8a1f6af57a35fd419fffed052a88946ef67dbce9c216478fc1d5f(
    value: typing.Optional[AppsyncFunctionSyncConfigLambdaConflictHandlerConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b0bec52e29fa9264d91acab044dee2d28719c5f478745f2ee4346960ad7f32f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8379e6bf550c8e38852626509eb8ffa6584b53830e3456299bc2551dd8469778(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddfb18df3db4fb2724caccc34ff2fcf45dc6ae064659c5c56029e48d791a182c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89c6946e37eb6423c8b602b2d4d6da2d716b01225ff4455374acaae06e8a45cb(
    value: typing.Optional[AppsyncFunctionSyncConfig],
) -> None:
    """Type checking stubs"""
    pass
