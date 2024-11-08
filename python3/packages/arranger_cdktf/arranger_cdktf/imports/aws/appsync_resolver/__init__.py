'''
# `aws_appsync_resolver`

Refer to the Terraform Registory for docs: [`aws_appsync_resolver`](https://www.terraform.io/docs/providers/aws/r/appsync_resolver).
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


class AppsyncResolver(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appsyncResolver.AppsyncResolver",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver aws_appsync_resolver}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        api_id: builtins.str,
        field: builtins.str,
        type: builtins.str,
        caching_config: typing.Optional[typing.Union["AppsyncResolverCachingConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        code: typing.Optional[builtins.str] = None,
        data_source: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        kind: typing.Optional[builtins.str] = None,
        max_batch_size: typing.Optional[jsii.Number] = None,
        pipeline_config: typing.Optional[typing.Union["AppsyncResolverPipelineConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        request_template: typing.Optional[builtins.str] = None,
        response_template: typing.Optional[builtins.str] = None,
        runtime: typing.Optional[typing.Union["AppsyncResolverRuntime", typing.Dict[builtins.str, typing.Any]]] = None,
        sync_config: typing.Optional[typing.Union["AppsyncResolverSyncConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver aws_appsync_resolver} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param api_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#api_id AppsyncResolver#api_id}.
        :param field: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#field AppsyncResolver#field}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#type AppsyncResolver#type}.
        :param caching_config: caching_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#caching_config AppsyncResolver#caching_config}
        :param code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#code AppsyncResolver#code}.
        :param data_source: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#data_source AppsyncResolver#data_source}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#id AppsyncResolver#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kind: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#kind AppsyncResolver#kind}.
        :param max_batch_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#max_batch_size AppsyncResolver#max_batch_size}.
        :param pipeline_config: pipeline_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#pipeline_config AppsyncResolver#pipeline_config}
        :param request_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#request_template AppsyncResolver#request_template}.
        :param response_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#response_template AppsyncResolver#response_template}.
        :param runtime: runtime block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#runtime AppsyncResolver#runtime}
        :param sync_config: sync_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#sync_config AppsyncResolver#sync_config}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4ed28d6a885a3601cb8f5982651a0bc48d4a0ae2c8e51dea76434f9506a8469)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AppsyncResolverConfig(
            api_id=api_id,
            field=field,
            type=type,
            caching_config=caching_config,
            code=code,
            data_source=data_source,
            id=id,
            kind=kind,
            max_batch_size=max_batch_size,
            pipeline_config=pipeline_config,
            request_template=request_template,
            response_template=response_template,
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

    @jsii.member(jsii_name="putCachingConfig")
    def put_caching_config(
        self,
        *,
        caching_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        ttl: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param caching_keys: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#caching_keys AppsyncResolver#caching_keys}.
        :param ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#ttl AppsyncResolver#ttl}.
        '''
        value = AppsyncResolverCachingConfig(caching_keys=caching_keys, ttl=ttl)

        return typing.cast(None, jsii.invoke(self, "putCachingConfig", [value]))

    @jsii.member(jsii_name="putPipelineConfig")
    def put_pipeline_config(
        self,
        *,
        functions: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param functions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#functions AppsyncResolver#functions}.
        '''
        value = AppsyncResolverPipelineConfig(functions=functions)

        return typing.cast(None, jsii.invoke(self, "putPipelineConfig", [value]))

    @jsii.member(jsii_name="putRuntime")
    def put_runtime(self, *, name: builtins.str, runtime_version: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#name AppsyncResolver#name}.
        :param runtime_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#runtime_version AppsyncResolver#runtime_version}.
        '''
        value = AppsyncResolverRuntime(name=name, runtime_version=runtime_version)

        return typing.cast(None, jsii.invoke(self, "putRuntime", [value]))

    @jsii.member(jsii_name="putSyncConfig")
    def put_sync_config(
        self,
        *,
        conflict_detection: typing.Optional[builtins.str] = None,
        conflict_handler: typing.Optional[builtins.str] = None,
        lambda_conflict_handler_config: typing.Optional[typing.Union["AppsyncResolverSyncConfigLambdaConflictHandlerConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param conflict_detection: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#conflict_detection AppsyncResolver#conflict_detection}.
        :param conflict_handler: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#conflict_handler AppsyncResolver#conflict_handler}.
        :param lambda_conflict_handler_config: lambda_conflict_handler_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#lambda_conflict_handler_config AppsyncResolver#lambda_conflict_handler_config}
        '''
        value = AppsyncResolverSyncConfig(
            conflict_detection=conflict_detection,
            conflict_handler=conflict_handler,
            lambda_conflict_handler_config=lambda_conflict_handler_config,
        )

        return typing.cast(None, jsii.invoke(self, "putSyncConfig", [value]))

    @jsii.member(jsii_name="resetCachingConfig")
    def reset_caching_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCachingConfig", []))

    @jsii.member(jsii_name="resetCode")
    def reset_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCode", []))

    @jsii.member(jsii_name="resetDataSource")
    def reset_data_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataSource", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetKind")
    def reset_kind(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKind", []))

    @jsii.member(jsii_name="resetMaxBatchSize")
    def reset_max_batch_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxBatchSize", []))

    @jsii.member(jsii_name="resetPipelineConfig")
    def reset_pipeline_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPipelineConfig", []))

    @jsii.member(jsii_name="resetRequestTemplate")
    def reset_request_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestTemplate", []))

    @jsii.member(jsii_name="resetResponseTemplate")
    def reset_response_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseTemplate", []))

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
    @jsii.member(jsii_name="cachingConfig")
    def caching_config(self) -> "AppsyncResolverCachingConfigOutputReference":
        return typing.cast("AppsyncResolverCachingConfigOutputReference", jsii.get(self, "cachingConfig"))

    @builtins.property
    @jsii.member(jsii_name="pipelineConfig")
    def pipeline_config(self) -> "AppsyncResolverPipelineConfigOutputReference":
        return typing.cast("AppsyncResolverPipelineConfigOutputReference", jsii.get(self, "pipelineConfig"))

    @builtins.property
    @jsii.member(jsii_name="runtime")
    def runtime(self) -> "AppsyncResolverRuntimeOutputReference":
        return typing.cast("AppsyncResolverRuntimeOutputReference", jsii.get(self, "runtime"))

    @builtins.property
    @jsii.member(jsii_name="syncConfig")
    def sync_config(self) -> "AppsyncResolverSyncConfigOutputReference":
        return typing.cast("AppsyncResolverSyncConfigOutputReference", jsii.get(self, "syncConfig"))

    @builtins.property
    @jsii.member(jsii_name="apiIdInput")
    def api_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiIdInput"))

    @builtins.property
    @jsii.member(jsii_name="cachingConfigInput")
    def caching_config_input(self) -> typing.Optional["AppsyncResolverCachingConfig"]:
        return typing.cast(typing.Optional["AppsyncResolverCachingConfig"], jsii.get(self, "cachingConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="codeInput")
    def code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "codeInput"))

    @builtins.property
    @jsii.member(jsii_name="dataSourceInput")
    def data_source_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataSourceInput"))

    @builtins.property
    @jsii.member(jsii_name="fieldInput")
    def field_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fieldInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="kindInput")
    def kind_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kindInput"))

    @builtins.property
    @jsii.member(jsii_name="maxBatchSizeInput")
    def max_batch_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxBatchSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="pipelineConfigInput")
    def pipeline_config_input(self) -> typing.Optional["AppsyncResolverPipelineConfig"]:
        return typing.cast(typing.Optional["AppsyncResolverPipelineConfig"], jsii.get(self, "pipelineConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="requestTemplateInput")
    def request_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "requestTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="responseTemplateInput")
    def response_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "responseTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="runtimeInput")
    def runtime_input(self) -> typing.Optional["AppsyncResolverRuntime"]:
        return typing.cast(typing.Optional["AppsyncResolverRuntime"], jsii.get(self, "runtimeInput"))

    @builtins.property
    @jsii.member(jsii_name="syncConfigInput")
    def sync_config_input(self) -> typing.Optional["AppsyncResolverSyncConfig"]:
        return typing.cast(typing.Optional["AppsyncResolverSyncConfig"], jsii.get(self, "syncConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiId"))

    @api_id.setter
    def api_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ceb733a317341e43d463b118d20c538bf56665ce66fd99a464d59c08cb8fd12)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="code")
    def code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "code"))

    @code.setter
    def code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68c649dd587cfca7bcd53cadc69b628b2f389a271bb35a0e30c78a57f3f7f4f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "code", value)

    @builtins.property
    @jsii.member(jsii_name="dataSource")
    def data_source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataSource"))

    @data_source.setter
    def data_source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97c7e24621e6f996aba15f4694c6bec934b2719de68ac2f4dc9c1b7fced40c8e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataSource", value)

    @builtins.property
    @jsii.member(jsii_name="field")
    def field(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "field"))

    @field.setter
    def field(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90782a31b9995dbf07eef0c1dec97b9deed7580e53ed954821429d9cdc837f70)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "field", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f660ccfa81b6cb31de7e897828e63aac85a68997d86a387408dcff15497f9908)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @kind.setter
    def kind(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f79b8b7c932b7e3f51847002eae9ebe0cae8d9926dc8ce441c4bc2ecd83f899a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kind", value)

    @builtins.property
    @jsii.member(jsii_name="maxBatchSize")
    def max_batch_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxBatchSize"))

    @max_batch_size.setter
    def max_batch_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e195f4b4eb33c93014ea51ee23d55485895bb8e948ddb878dbad8efc312f4e67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxBatchSize", value)

    @builtins.property
    @jsii.member(jsii_name="requestTemplate")
    def request_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "requestTemplate"))

    @request_template.setter
    def request_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__892102b62e7d23e77594b64c90f1419982a3464ab485a6b932fd73601f7a58f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="responseTemplate")
    def response_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "responseTemplate"))

    @response_template.setter
    def response_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d7e0f783f7667f078a41063218b431c805b17a6216ce2790c3376806cf3569f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc78e4537682fb07de239fcc94a247b05d38e91cc5c431493a248a5e1c4a1406)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)


@jsii.data_type(
    jsii_type="aws.appsyncResolver.AppsyncResolverCachingConfig",
    jsii_struct_bases=[],
    name_mapping={"caching_keys": "cachingKeys", "ttl": "ttl"},
)
class AppsyncResolverCachingConfig:
    def __init__(
        self,
        *,
        caching_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        ttl: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param caching_keys: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#caching_keys AppsyncResolver#caching_keys}.
        :param ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#ttl AppsyncResolver#ttl}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e06bd335128a49570e4fe3b42942f689a57bcd193c30fd57401cad467462351c)
            check_type(argname="argument caching_keys", value=caching_keys, expected_type=type_hints["caching_keys"])
            check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if caching_keys is not None:
            self._values["caching_keys"] = caching_keys
        if ttl is not None:
            self._values["ttl"] = ttl

    @builtins.property
    def caching_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#caching_keys AppsyncResolver#caching_keys}.'''
        result = self._values.get("caching_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def ttl(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#ttl AppsyncResolver#ttl}.'''
        result = self._values.get("ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncResolverCachingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppsyncResolverCachingConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appsyncResolver.AppsyncResolverCachingConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__854e5b7ec06888a6f2080e031d4113c7be687bb8e0d57db95d988d786a8d031f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCachingKeys")
    def reset_caching_keys(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCachingKeys", []))

    @jsii.member(jsii_name="resetTtl")
    def reset_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTtl", []))

    @builtins.property
    @jsii.member(jsii_name="cachingKeysInput")
    def caching_keys_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "cachingKeysInput"))

    @builtins.property
    @jsii.member(jsii_name="ttlInput")
    def ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ttlInput"))

    @builtins.property
    @jsii.member(jsii_name="cachingKeys")
    def caching_keys(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "cachingKeys"))

    @caching_keys.setter
    def caching_keys(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5dffd2afea92cab6b70f0794925df45131ce2f2d82e93905eaf2747506501f8b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cachingKeys", value)

    @builtins.property
    @jsii.member(jsii_name="ttl")
    def ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ttl"))

    @ttl.setter
    def ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__191a04d407e301902ca195e35a8944817240a38e6958b1581eb4b6909f14d021)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ttl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppsyncResolverCachingConfig]:
        return typing.cast(typing.Optional[AppsyncResolverCachingConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppsyncResolverCachingConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7dd5935655a3df7b208161e2148de13d43f24053694dad18c7a98bdf009fc0e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appsyncResolver.AppsyncResolverConfig",
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
        "field": "field",
        "type": "type",
        "caching_config": "cachingConfig",
        "code": "code",
        "data_source": "dataSource",
        "id": "id",
        "kind": "kind",
        "max_batch_size": "maxBatchSize",
        "pipeline_config": "pipelineConfig",
        "request_template": "requestTemplate",
        "response_template": "responseTemplate",
        "runtime": "runtime",
        "sync_config": "syncConfig",
    },
)
class AppsyncResolverConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        field: builtins.str,
        type: builtins.str,
        caching_config: typing.Optional[typing.Union[AppsyncResolverCachingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        code: typing.Optional[builtins.str] = None,
        data_source: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        kind: typing.Optional[builtins.str] = None,
        max_batch_size: typing.Optional[jsii.Number] = None,
        pipeline_config: typing.Optional[typing.Union["AppsyncResolverPipelineConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        request_template: typing.Optional[builtins.str] = None,
        response_template: typing.Optional[builtins.str] = None,
        runtime: typing.Optional[typing.Union["AppsyncResolverRuntime", typing.Dict[builtins.str, typing.Any]]] = None,
        sync_config: typing.Optional[typing.Union["AppsyncResolverSyncConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param api_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#api_id AppsyncResolver#api_id}.
        :param field: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#field AppsyncResolver#field}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#type AppsyncResolver#type}.
        :param caching_config: caching_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#caching_config AppsyncResolver#caching_config}
        :param code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#code AppsyncResolver#code}.
        :param data_source: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#data_source AppsyncResolver#data_source}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#id AppsyncResolver#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kind: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#kind AppsyncResolver#kind}.
        :param max_batch_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#max_batch_size AppsyncResolver#max_batch_size}.
        :param pipeline_config: pipeline_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#pipeline_config AppsyncResolver#pipeline_config}
        :param request_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#request_template AppsyncResolver#request_template}.
        :param response_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#response_template AppsyncResolver#response_template}.
        :param runtime: runtime block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#runtime AppsyncResolver#runtime}
        :param sync_config: sync_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#sync_config AppsyncResolver#sync_config}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(caching_config, dict):
            caching_config = AppsyncResolverCachingConfig(**caching_config)
        if isinstance(pipeline_config, dict):
            pipeline_config = AppsyncResolverPipelineConfig(**pipeline_config)
        if isinstance(runtime, dict):
            runtime = AppsyncResolverRuntime(**runtime)
        if isinstance(sync_config, dict):
            sync_config = AppsyncResolverSyncConfig(**sync_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5d3acf94b6265cb78db8db611dc7c194d1a95c346e934fc221eacef5e277029)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument api_id", value=api_id, expected_type=type_hints["api_id"])
            check_type(argname="argument field", value=field, expected_type=type_hints["field"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument caching_config", value=caching_config, expected_type=type_hints["caching_config"])
            check_type(argname="argument code", value=code, expected_type=type_hints["code"])
            check_type(argname="argument data_source", value=data_source, expected_type=type_hints["data_source"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
            check_type(argname="argument max_batch_size", value=max_batch_size, expected_type=type_hints["max_batch_size"])
            check_type(argname="argument pipeline_config", value=pipeline_config, expected_type=type_hints["pipeline_config"])
            check_type(argname="argument request_template", value=request_template, expected_type=type_hints["request_template"])
            check_type(argname="argument response_template", value=response_template, expected_type=type_hints["response_template"])
            check_type(argname="argument runtime", value=runtime, expected_type=type_hints["runtime"])
            check_type(argname="argument sync_config", value=sync_config, expected_type=type_hints["sync_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_id": api_id,
            "field": field,
            "type": type,
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
        if caching_config is not None:
            self._values["caching_config"] = caching_config
        if code is not None:
            self._values["code"] = code
        if data_source is not None:
            self._values["data_source"] = data_source
        if id is not None:
            self._values["id"] = id
        if kind is not None:
            self._values["kind"] = kind
        if max_batch_size is not None:
            self._values["max_batch_size"] = max_batch_size
        if pipeline_config is not None:
            self._values["pipeline_config"] = pipeline_config
        if request_template is not None:
            self._values["request_template"] = request_template
        if response_template is not None:
            self._values["response_template"] = response_template
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#api_id AppsyncResolver#api_id}.'''
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def field(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#field AppsyncResolver#field}.'''
        result = self._values.get("field")
        assert result is not None, "Required property 'field' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#type AppsyncResolver#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def caching_config(self) -> typing.Optional[AppsyncResolverCachingConfig]:
        '''caching_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#caching_config AppsyncResolver#caching_config}
        '''
        result = self._values.get("caching_config")
        return typing.cast(typing.Optional[AppsyncResolverCachingConfig], result)

    @builtins.property
    def code(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#code AppsyncResolver#code}.'''
        result = self._values.get("code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_source(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#data_source AppsyncResolver#data_source}.'''
        result = self._values.get("data_source")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#id AppsyncResolver#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kind(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#kind AppsyncResolver#kind}.'''
        result = self._values.get("kind")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_batch_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#max_batch_size AppsyncResolver#max_batch_size}.'''
        result = self._values.get("max_batch_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def pipeline_config(self) -> typing.Optional["AppsyncResolverPipelineConfig"]:
        '''pipeline_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#pipeline_config AppsyncResolver#pipeline_config}
        '''
        result = self._values.get("pipeline_config")
        return typing.cast(typing.Optional["AppsyncResolverPipelineConfig"], result)

    @builtins.property
    def request_template(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#request_template AppsyncResolver#request_template}.'''
        result = self._values.get("request_template")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def response_template(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#response_template AppsyncResolver#response_template}.'''
        result = self._values.get("response_template")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def runtime(self) -> typing.Optional["AppsyncResolverRuntime"]:
        '''runtime block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#runtime AppsyncResolver#runtime}
        '''
        result = self._values.get("runtime")
        return typing.cast(typing.Optional["AppsyncResolverRuntime"], result)

    @builtins.property
    def sync_config(self) -> typing.Optional["AppsyncResolverSyncConfig"]:
        '''sync_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#sync_config AppsyncResolver#sync_config}
        '''
        result = self._values.get("sync_config")
        return typing.cast(typing.Optional["AppsyncResolverSyncConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncResolverConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appsyncResolver.AppsyncResolverPipelineConfig",
    jsii_struct_bases=[],
    name_mapping={"functions": "functions"},
)
class AppsyncResolverPipelineConfig:
    def __init__(
        self,
        *,
        functions: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param functions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#functions AppsyncResolver#functions}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93e0d8e439b834b7ba679310941fe827fee15ab3c7d641f3582d92d7be25a77f)
            check_type(argname="argument functions", value=functions, expected_type=type_hints["functions"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if functions is not None:
            self._values["functions"] = functions

    @builtins.property
    def functions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#functions AppsyncResolver#functions}.'''
        result = self._values.get("functions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncResolverPipelineConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppsyncResolverPipelineConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appsyncResolver.AppsyncResolverPipelineConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__083764a6b1c30b3e637208bee83f8c2de77c03ddbb1db1a17b69752575261293)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFunctions")
    def reset_functions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFunctions", []))

    @builtins.property
    @jsii.member(jsii_name="functionsInput")
    def functions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "functionsInput"))

    @builtins.property
    @jsii.member(jsii_name="functions")
    def functions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "functions"))

    @functions.setter
    def functions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a95247fa999e7d412429a44400ccf88ea766a6824e7aaaab0382966ac48c53b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "functions", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppsyncResolverPipelineConfig]:
        return typing.cast(typing.Optional[AppsyncResolverPipelineConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppsyncResolverPipelineConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c504887dd8fa189a6a6d92b944fd578f5911154f4332a82893638061feebc17)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appsyncResolver.AppsyncResolverRuntime",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "runtime_version": "runtimeVersion"},
)
class AppsyncResolverRuntime:
    def __init__(self, *, name: builtins.str, runtime_version: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#name AppsyncResolver#name}.
        :param runtime_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#runtime_version AppsyncResolver#runtime_version}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85b409c65fb41b17d14f7e713508ede54e055fc0a7c82d7eac08f9fa71d88d37)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument runtime_version", value=runtime_version, expected_type=type_hints["runtime_version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "runtime_version": runtime_version,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#name AppsyncResolver#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def runtime_version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#runtime_version AppsyncResolver#runtime_version}.'''
        result = self._values.get("runtime_version")
        assert result is not None, "Required property 'runtime_version' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncResolverRuntime(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppsyncResolverRuntimeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appsyncResolver.AppsyncResolverRuntimeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a71650524c433d59a0100c1ca28ac446822f0dcbfc7a841ff6f61d5096f52a9f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7e904b125a1c6b70ca33304c0c914d3fa54ee61543ac96f1f294a157d4e938d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="runtimeVersion")
    def runtime_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "runtimeVersion"))

    @runtime_version.setter
    def runtime_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1610d40e39c12e4fd586a966efdb765c6efdee43b932d37be4e926d98b012b33)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runtimeVersion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppsyncResolverRuntime]:
        return typing.cast(typing.Optional[AppsyncResolverRuntime], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[AppsyncResolverRuntime]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87c2baa1a1de3a83cd6d95a1bfd6582867cd69af5735858490c290741e65cfa9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appsyncResolver.AppsyncResolverSyncConfig",
    jsii_struct_bases=[],
    name_mapping={
        "conflict_detection": "conflictDetection",
        "conflict_handler": "conflictHandler",
        "lambda_conflict_handler_config": "lambdaConflictHandlerConfig",
    },
)
class AppsyncResolverSyncConfig:
    def __init__(
        self,
        *,
        conflict_detection: typing.Optional[builtins.str] = None,
        conflict_handler: typing.Optional[builtins.str] = None,
        lambda_conflict_handler_config: typing.Optional[typing.Union["AppsyncResolverSyncConfigLambdaConflictHandlerConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param conflict_detection: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#conflict_detection AppsyncResolver#conflict_detection}.
        :param conflict_handler: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#conflict_handler AppsyncResolver#conflict_handler}.
        :param lambda_conflict_handler_config: lambda_conflict_handler_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#lambda_conflict_handler_config AppsyncResolver#lambda_conflict_handler_config}
        '''
        if isinstance(lambda_conflict_handler_config, dict):
            lambda_conflict_handler_config = AppsyncResolverSyncConfigLambdaConflictHandlerConfig(**lambda_conflict_handler_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__265bb6964b48178fefca8e4282d4d9c10a4449cf41761c960d262519f95dfd74)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#conflict_detection AppsyncResolver#conflict_detection}.'''
        result = self._values.get("conflict_detection")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def conflict_handler(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#conflict_handler AppsyncResolver#conflict_handler}.'''
        result = self._values.get("conflict_handler")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lambda_conflict_handler_config(
        self,
    ) -> typing.Optional["AppsyncResolverSyncConfigLambdaConflictHandlerConfig"]:
        '''lambda_conflict_handler_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#lambda_conflict_handler_config AppsyncResolver#lambda_conflict_handler_config}
        '''
        result = self._values.get("lambda_conflict_handler_config")
        return typing.cast(typing.Optional["AppsyncResolverSyncConfigLambdaConflictHandlerConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncResolverSyncConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appsyncResolver.AppsyncResolverSyncConfigLambdaConflictHandlerConfig",
    jsii_struct_bases=[],
    name_mapping={"lambda_conflict_handler_arn": "lambdaConflictHandlerArn"},
)
class AppsyncResolverSyncConfigLambdaConflictHandlerConfig:
    def __init__(
        self,
        *,
        lambda_conflict_handler_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param lambda_conflict_handler_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#lambda_conflict_handler_arn AppsyncResolver#lambda_conflict_handler_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5cf825d3a2dce38f00d00a9ffc27bf6470d03f14eee39e91e8e7f17675cf4f7)
            check_type(argname="argument lambda_conflict_handler_arn", value=lambda_conflict_handler_arn, expected_type=type_hints["lambda_conflict_handler_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if lambda_conflict_handler_arn is not None:
            self._values["lambda_conflict_handler_arn"] = lambda_conflict_handler_arn

    @builtins.property
    def lambda_conflict_handler_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#lambda_conflict_handler_arn AppsyncResolver#lambda_conflict_handler_arn}.'''
        result = self._values.get("lambda_conflict_handler_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncResolverSyncConfigLambdaConflictHandlerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppsyncResolverSyncConfigLambdaConflictHandlerConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appsyncResolver.AppsyncResolverSyncConfigLambdaConflictHandlerConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9dc44fe425d04e947d67d36dc57d22019b8e44e0ff823e61b06362f6d91e4bed)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ec14e0e3197fef9c3037b95490c5af1244ccc58d993ddfc78fb2a1393d81b2b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lambdaConflictHandlerArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppsyncResolverSyncConfigLambdaConflictHandlerConfig]:
        return typing.cast(typing.Optional[AppsyncResolverSyncConfigLambdaConflictHandlerConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppsyncResolverSyncConfigLambdaConflictHandlerConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4f926dc221f05af74cf567c1f50bdb7bd311f13d93f7939fe35ac083eeb6e50)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppsyncResolverSyncConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appsyncResolver.AppsyncResolverSyncConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9cbaaf092299f34fc1a5afa19840bf5b2e9ae1b05448cc34754ccae220abbb94)
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
        :param lambda_conflict_handler_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_resolver#lambda_conflict_handler_arn AppsyncResolver#lambda_conflict_handler_arn}.
        '''
        value = AppsyncResolverSyncConfigLambdaConflictHandlerConfig(
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
    ) -> AppsyncResolverSyncConfigLambdaConflictHandlerConfigOutputReference:
        return typing.cast(AppsyncResolverSyncConfigLambdaConflictHandlerConfigOutputReference, jsii.get(self, "lambdaConflictHandlerConfig"))

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
    ) -> typing.Optional[AppsyncResolverSyncConfigLambdaConflictHandlerConfig]:
        return typing.cast(typing.Optional[AppsyncResolverSyncConfigLambdaConflictHandlerConfig], jsii.get(self, "lambdaConflictHandlerConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="conflictDetection")
    def conflict_detection(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "conflictDetection"))

    @conflict_detection.setter
    def conflict_detection(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c21440c79e2338101940e2395a7e1fea91d9c5614ef3dbe78b9005ca279d6e91)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "conflictDetection", value)

    @builtins.property
    @jsii.member(jsii_name="conflictHandler")
    def conflict_handler(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "conflictHandler"))

    @conflict_handler.setter
    def conflict_handler(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9cc14ab0095216366af8bb2ece1951cf706057a57ba5d70244c5ec3d91406330)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "conflictHandler", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppsyncResolverSyncConfig]:
        return typing.cast(typing.Optional[AppsyncResolverSyncConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[AppsyncResolverSyncConfig]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb56b131f75fb2db42cd186050b28819877f92f55d68ed198dd8516a43217df9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "AppsyncResolver",
    "AppsyncResolverCachingConfig",
    "AppsyncResolverCachingConfigOutputReference",
    "AppsyncResolverConfig",
    "AppsyncResolverPipelineConfig",
    "AppsyncResolverPipelineConfigOutputReference",
    "AppsyncResolverRuntime",
    "AppsyncResolverRuntimeOutputReference",
    "AppsyncResolverSyncConfig",
    "AppsyncResolverSyncConfigLambdaConflictHandlerConfig",
    "AppsyncResolverSyncConfigLambdaConflictHandlerConfigOutputReference",
    "AppsyncResolverSyncConfigOutputReference",
]

publication.publish()

def _typecheckingstub__a4ed28d6a885a3601cb8f5982651a0bc48d4a0ae2c8e51dea76434f9506a8469(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    api_id: builtins.str,
    field: builtins.str,
    type: builtins.str,
    caching_config: typing.Optional[typing.Union[AppsyncResolverCachingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    code: typing.Optional[builtins.str] = None,
    data_source: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    kind: typing.Optional[builtins.str] = None,
    max_batch_size: typing.Optional[jsii.Number] = None,
    pipeline_config: typing.Optional[typing.Union[AppsyncResolverPipelineConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    request_template: typing.Optional[builtins.str] = None,
    response_template: typing.Optional[builtins.str] = None,
    runtime: typing.Optional[typing.Union[AppsyncResolverRuntime, typing.Dict[builtins.str, typing.Any]]] = None,
    sync_config: typing.Optional[typing.Union[AppsyncResolverSyncConfig, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__9ceb733a317341e43d463b118d20c538bf56665ce66fd99a464d59c08cb8fd12(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68c649dd587cfca7bcd53cadc69b628b2f389a271bb35a0e30c78a57f3f7f4f1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97c7e24621e6f996aba15f4694c6bec934b2719de68ac2f4dc9c1b7fced40c8e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90782a31b9995dbf07eef0c1dec97b9deed7580e53ed954821429d9cdc837f70(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f660ccfa81b6cb31de7e897828e63aac85a68997d86a387408dcff15497f9908(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f79b8b7c932b7e3f51847002eae9ebe0cae8d9926dc8ce441c4bc2ecd83f899a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e195f4b4eb33c93014ea51ee23d55485895bb8e948ddb878dbad8efc312f4e67(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__892102b62e7d23e77594b64c90f1419982a3464ab485a6b932fd73601f7a58f6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d7e0f783f7667f078a41063218b431c805b17a6216ce2790c3376806cf3569f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc78e4537682fb07de239fcc94a247b05d38e91cc5c431493a248a5e1c4a1406(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e06bd335128a49570e4fe3b42942f689a57bcd193c30fd57401cad467462351c(
    *,
    caching_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    ttl: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__854e5b7ec06888a6f2080e031d4113c7be687bb8e0d57db95d988d786a8d031f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dffd2afea92cab6b70f0794925df45131ce2f2d82e93905eaf2747506501f8b(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__191a04d407e301902ca195e35a8944817240a38e6958b1581eb4b6909f14d021(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7dd5935655a3df7b208161e2148de13d43f24053694dad18c7a98bdf009fc0e(
    value: typing.Optional[AppsyncResolverCachingConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5d3acf94b6265cb78db8db611dc7c194d1a95c346e934fc221eacef5e277029(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    api_id: builtins.str,
    field: builtins.str,
    type: builtins.str,
    caching_config: typing.Optional[typing.Union[AppsyncResolverCachingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    code: typing.Optional[builtins.str] = None,
    data_source: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    kind: typing.Optional[builtins.str] = None,
    max_batch_size: typing.Optional[jsii.Number] = None,
    pipeline_config: typing.Optional[typing.Union[AppsyncResolverPipelineConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    request_template: typing.Optional[builtins.str] = None,
    response_template: typing.Optional[builtins.str] = None,
    runtime: typing.Optional[typing.Union[AppsyncResolverRuntime, typing.Dict[builtins.str, typing.Any]]] = None,
    sync_config: typing.Optional[typing.Union[AppsyncResolverSyncConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93e0d8e439b834b7ba679310941fe827fee15ab3c7d641f3582d92d7be25a77f(
    *,
    functions: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__083764a6b1c30b3e637208bee83f8c2de77c03ddbb1db1a17b69752575261293(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a95247fa999e7d412429a44400ccf88ea766a6824e7aaaab0382966ac48c53b0(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c504887dd8fa189a6a6d92b944fd578f5911154f4332a82893638061feebc17(
    value: typing.Optional[AppsyncResolverPipelineConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85b409c65fb41b17d14f7e713508ede54e055fc0a7c82d7eac08f9fa71d88d37(
    *,
    name: builtins.str,
    runtime_version: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a71650524c433d59a0100c1ca28ac446822f0dcbfc7a841ff6f61d5096f52a9f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e904b125a1c6b70ca33304c0c914d3fa54ee61543ac96f1f294a157d4e938d7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1610d40e39c12e4fd586a966efdb765c6efdee43b932d37be4e926d98b012b33(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87c2baa1a1de3a83cd6d95a1bfd6582867cd69af5735858490c290741e65cfa9(
    value: typing.Optional[AppsyncResolverRuntime],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__265bb6964b48178fefca8e4282d4d9c10a4449cf41761c960d262519f95dfd74(
    *,
    conflict_detection: typing.Optional[builtins.str] = None,
    conflict_handler: typing.Optional[builtins.str] = None,
    lambda_conflict_handler_config: typing.Optional[typing.Union[AppsyncResolverSyncConfigLambdaConflictHandlerConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5cf825d3a2dce38f00d00a9ffc27bf6470d03f14eee39e91e8e7f17675cf4f7(
    *,
    lambda_conflict_handler_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9dc44fe425d04e947d67d36dc57d22019b8e44e0ff823e61b06362f6d91e4bed(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec14e0e3197fef9c3037b95490c5af1244ccc58d993ddfc78fb2a1393d81b2b1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4f926dc221f05af74cf567c1f50bdb7bd311f13d93f7939fe35ac083eeb6e50(
    value: typing.Optional[AppsyncResolverSyncConfigLambdaConflictHandlerConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cbaaf092299f34fc1a5afa19840bf5b2e9ae1b05448cc34754ccae220abbb94(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c21440c79e2338101940e2395a7e1fea91d9c5614ef3dbe78b9005ca279d6e91(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cc14ab0095216366af8bb2ece1951cf706057a57ba5d70244c5ec3d91406330(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb56b131f75fb2db42cd186050b28819877f92f55d68ed198dd8516a43217df9(
    value: typing.Optional[AppsyncResolverSyncConfig],
) -> None:
    """Type checking stubs"""
    pass
