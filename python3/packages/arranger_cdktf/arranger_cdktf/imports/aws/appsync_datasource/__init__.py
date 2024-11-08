'''
# `aws_appsync_datasource`

Refer to the Terraform Registory for docs: [`aws_appsync_datasource`](https://www.terraform.io/docs/providers/aws/r/appsync_datasource).
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


class AppsyncDatasource(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appsyncDatasource.AppsyncDatasource",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource aws_appsync_datasource}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        api_id: builtins.str,
        name: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        dynamodb_config: typing.Optional[typing.Union["AppsyncDatasourceDynamodbConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        elasticsearch_config: typing.Optional[typing.Union["AppsyncDatasourceElasticsearchConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        http_config: typing.Optional[typing.Union["AppsyncDatasourceHttpConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        lambda_config: typing.Optional[typing.Union["AppsyncDatasourceLambdaConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        relational_database_config: typing.Optional[typing.Union["AppsyncDatasourceRelationalDatabaseConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        service_role_arn: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource aws_appsync_datasource} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param api_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#api_id AppsyncDatasource#api_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#name AppsyncDatasource#name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#type AppsyncDatasource#type}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#description AppsyncDatasource#description}.
        :param dynamodb_config: dynamodb_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#dynamodb_config AppsyncDatasource#dynamodb_config}
        :param elasticsearch_config: elasticsearch_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#elasticsearch_config AppsyncDatasource#elasticsearch_config}
        :param http_config: http_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#http_config AppsyncDatasource#http_config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#id AppsyncDatasource#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param lambda_config: lambda_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#lambda_config AppsyncDatasource#lambda_config}
        :param relational_database_config: relational_database_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#relational_database_config AppsyncDatasource#relational_database_config}
        :param service_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#service_role_arn AppsyncDatasource#service_role_arn}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a75711e528346865046793fbd1a3583fc51ab214f74b7ed6993e2f86027e910d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AppsyncDatasourceConfig(
            api_id=api_id,
            name=name,
            type=type,
            description=description,
            dynamodb_config=dynamodb_config,
            elasticsearch_config=elasticsearch_config,
            http_config=http_config,
            id=id,
            lambda_config=lambda_config,
            relational_database_config=relational_database_config,
            service_role_arn=service_role_arn,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putDynamodbConfig")
    def put_dynamodb_config(
        self,
        *,
        table_name: builtins.str,
        delta_sync_config: typing.Optional[typing.Union["AppsyncDatasourceDynamodbConfigDeltaSyncConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        region: typing.Optional[builtins.str] = None,
        use_caller_credentials: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        versioned: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param table_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#table_name AppsyncDatasource#table_name}.
        :param delta_sync_config: delta_sync_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#delta_sync_config AppsyncDatasource#delta_sync_config}
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#region AppsyncDatasource#region}.
        :param use_caller_credentials: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#use_caller_credentials AppsyncDatasource#use_caller_credentials}.
        :param versioned: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#versioned AppsyncDatasource#versioned}.
        '''
        value = AppsyncDatasourceDynamodbConfig(
            table_name=table_name,
            delta_sync_config=delta_sync_config,
            region=region,
            use_caller_credentials=use_caller_credentials,
            versioned=versioned,
        )

        return typing.cast(None, jsii.invoke(self, "putDynamodbConfig", [value]))

    @jsii.member(jsii_name="putElasticsearchConfig")
    def put_elasticsearch_config(
        self,
        *,
        endpoint: builtins.str,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#endpoint AppsyncDatasource#endpoint}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#region AppsyncDatasource#region}.
        '''
        value = AppsyncDatasourceElasticsearchConfig(endpoint=endpoint, region=region)

        return typing.cast(None, jsii.invoke(self, "putElasticsearchConfig", [value]))

    @jsii.member(jsii_name="putHttpConfig")
    def put_http_config(
        self,
        *,
        endpoint: builtins.str,
        authorization_config: typing.Optional[typing.Union["AppsyncDatasourceHttpConfigAuthorizationConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#endpoint AppsyncDatasource#endpoint}.
        :param authorization_config: authorization_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#authorization_config AppsyncDatasource#authorization_config}
        '''
        value = AppsyncDatasourceHttpConfig(
            endpoint=endpoint, authorization_config=authorization_config
        )

        return typing.cast(None, jsii.invoke(self, "putHttpConfig", [value]))

    @jsii.member(jsii_name="putLambdaConfig")
    def put_lambda_config(self, *, function_arn: builtins.str) -> None:
        '''
        :param function_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#function_arn AppsyncDatasource#function_arn}.
        '''
        value = AppsyncDatasourceLambdaConfig(function_arn=function_arn)

        return typing.cast(None, jsii.invoke(self, "putLambdaConfig", [value]))

    @jsii.member(jsii_name="putRelationalDatabaseConfig")
    def put_relational_database_config(
        self,
        *,
        http_endpoint_config: typing.Optional[typing.Union["AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        source_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param http_endpoint_config: http_endpoint_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#http_endpoint_config AppsyncDatasource#http_endpoint_config}
        :param source_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#source_type AppsyncDatasource#source_type}.
        '''
        value = AppsyncDatasourceRelationalDatabaseConfig(
            http_endpoint_config=http_endpoint_config, source_type=source_type
        )

        return typing.cast(None, jsii.invoke(self, "putRelationalDatabaseConfig", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDynamodbConfig")
    def reset_dynamodb_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDynamodbConfig", []))

    @jsii.member(jsii_name="resetElasticsearchConfig")
    def reset_elasticsearch_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetElasticsearchConfig", []))

    @jsii.member(jsii_name="resetHttpConfig")
    def reset_http_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpConfig", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLambdaConfig")
    def reset_lambda_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLambdaConfig", []))

    @jsii.member(jsii_name="resetRelationalDatabaseConfig")
    def reset_relational_database_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRelationalDatabaseConfig", []))

    @jsii.member(jsii_name="resetServiceRoleArn")
    def reset_service_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceRoleArn", []))

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
    @jsii.member(jsii_name="dynamodbConfig")
    def dynamodb_config(self) -> "AppsyncDatasourceDynamodbConfigOutputReference":
        return typing.cast("AppsyncDatasourceDynamodbConfigOutputReference", jsii.get(self, "dynamodbConfig"))

    @builtins.property
    @jsii.member(jsii_name="elasticsearchConfig")
    def elasticsearch_config(
        self,
    ) -> "AppsyncDatasourceElasticsearchConfigOutputReference":
        return typing.cast("AppsyncDatasourceElasticsearchConfigOutputReference", jsii.get(self, "elasticsearchConfig"))

    @builtins.property
    @jsii.member(jsii_name="httpConfig")
    def http_config(self) -> "AppsyncDatasourceHttpConfigOutputReference":
        return typing.cast("AppsyncDatasourceHttpConfigOutputReference", jsii.get(self, "httpConfig"))

    @builtins.property
    @jsii.member(jsii_name="lambdaConfig")
    def lambda_config(self) -> "AppsyncDatasourceLambdaConfigOutputReference":
        return typing.cast("AppsyncDatasourceLambdaConfigOutputReference", jsii.get(self, "lambdaConfig"))

    @builtins.property
    @jsii.member(jsii_name="relationalDatabaseConfig")
    def relational_database_config(
        self,
    ) -> "AppsyncDatasourceRelationalDatabaseConfigOutputReference":
        return typing.cast("AppsyncDatasourceRelationalDatabaseConfigOutputReference", jsii.get(self, "relationalDatabaseConfig"))

    @builtins.property
    @jsii.member(jsii_name="apiIdInput")
    def api_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiIdInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="dynamodbConfigInput")
    def dynamodb_config_input(
        self,
    ) -> typing.Optional["AppsyncDatasourceDynamodbConfig"]:
        return typing.cast(typing.Optional["AppsyncDatasourceDynamodbConfig"], jsii.get(self, "dynamodbConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="elasticsearchConfigInput")
    def elasticsearch_config_input(
        self,
    ) -> typing.Optional["AppsyncDatasourceElasticsearchConfig"]:
        return typing.cast(typing.Optional["AppsyncDatasourceElasticsearchConfig"], jsii.get(self, "elasticsearchConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="httpConfigInput")
    def http_config_input(self) -> typing.Optional["AppsyncDatasourceHttpConfig"]:
        return typing.cast(typing.Optional["AppsyncDatasourceHttpConfig"], jsii.get(self, "httpConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="lambdaConfigInput")
    def lambda_config_input(self) -> typing.Optional["AppsyncDatasourceLambdaConfig"]:
        return typing.cast(typing.Optional["AppsyncDatasourceLambdaConfig"], jsii.get(self, "lambdaConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="relationalDatabaseConfigInput")
    def relational_database_config_input(
        self,
    ) -> typing.Optional["AppsyncDatasourceRelationalDatabaseConfig"]:
        return typing.cast(typing.Optional["AppsyncDatasourceRelationalDatabaseConfig"], jsii.get(self, "relationalDatabaseConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceRoleArnInput")
    def service_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceRoleArnInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__d33a4e069651015c5c38c2507186d712c5e2abaa955cebfc0a7bd076fc7dab9b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2f0a52c09ebc2ae757e06cb235daef4da5c320ee9090cc48b0bb854c274a4e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9349031ce2736852e43ca1ef2a3d672cf3b56d142e4cab5c4d3f35c92162c8fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04fe807be50cb424c432536ec17ab753f341f522688ac6e8f7e43ebfc34696b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="serviceRoleArn")
    def service_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceRoleArn"))

    @service_role_arn.setter
    def service_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a428fd979f934136c07fa82f6d1d76f195dd4e74742e885379fa0c88c59f9c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b926b87f372f58a5b7a2cdb842bf760e57c8e282f8f210f101b53fb17abab806)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)


@jsii.data_type(
    jsii_type="aws.appsyncDatasource.AppsyncDatasourceConfig",
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
        "name": "name",
        "type": "type",
        "description": "description",
        "dynamodb_config": "dynamodbConfig",
        "elasticsearch_config": "elasticsearchConfig",
        "http_config": "httpConfig",
        "id": "id",
        "lambda_config": "lambdaConfig",
        "relational_database_config": "relationalDatabaseConfig",
        "service_role_arn": "serviceRoleArn",
    },
)
class AppsyncDatasourceConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        name: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        dynamodb_config: typing.Optional[typing.Union["AppsyncDatasourceDynamodbConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        elasticsearch_config: typing.Optional[typing.Union["AppsyncDatasourceElasticsearchConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        http_config: typing.Optional[typing.Union["AppsyncDatasourceHttpConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        lambda_config: typing.Optional[typing.Union["AppsyncDatasourceLambdaConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        relational_database_config: typing.Optional[typing.Union["AppsyncDatasourceRelationalDatabaseConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        service_role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param api_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#api_id AppsyncDatasource#api_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#name AppsyncDatasource#name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#type AppsyncDatasource#type}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#description AppsyncDatasource#description}.
        :param dynamodb_config: dynamodb_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#dynamodb_config AppsyncDatasource#dynamodb_config}
        :param elasticsearch_config: elasticsearch_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#elasticsearch_config AppsyncDatasource#elasticsearch_config}
        :param http_config: http_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#http_config AppsyncDatasource#http_config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#id AppsyncDatasource#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param lambda_config: lambda_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#lambda_config AppsyncDatasource#lambda_config}
        :param relational_database_config: relational_database_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#relational_database_config AppsyncDatasource#relational_database_config}
        :param service_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#service_role_arn AppsyncDatasource#service_role_arn}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(dynamodb_config, dict):
            dynamodb_config = AppsyncDatasourceDynamodbConfig(**dynamodb_config)
        if isinstance(elasticsearch_config, dict):
            elasticsearch_config = AppsyncDatasourceElasticsearchConfig(**elasticsearch_config)
        if isinstance(http_config, dict):
            http_config = AppsyncDatasourceHttpConfig(**http_config)
        if isinstance(lambda_config, dict):
            lambda_config = AppsyncDatasourceLambdaConfig(**lambda_config)
        if isinstance(relational_database_config, dict):
            relational_database_config = AppsyncDatasourceRelationalDatabaseConfig(**relational_database_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fbb4433154a45a7ce7cf44a17d94eb7d198a20a4f08c1333ec06a8d9a05c68f6)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument api_id", value=api_id, expected_type=type_hints["api_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument dynamodb_config", value=dynamodb_config, expected_type=type_hints["dynamodb_config"])
            check_type(argname="argument elasticsearch_config", value=elasticsearch_config, expected_type=type_hints["elasticsearch_config"])
            check_type(argname="argument http_config", value=http_config, expected_type=type_hints["http_config"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument lambda_config", value=lambda_config, expected_type=type_hints["lambda_config"])
            check_type(argname="argument relational_database_config", value=relational_database_config, expected_type=type_hints["relational_database_config"])
            check_type(argname="argument service_role_arn", value=service_role_arn, expected_type=type_hints["service_role_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_id": api_id,
            "name": name,
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
        if description is not None:
            self._values["description"] = description
        if dynamodb_config is not None:
            self._values["dynamodb_config"] = dynamodb_config
        if elasticsearch_config is not None:
            self._values["elasticsearch_config"] = elasticsearch_config
        if http_config is not None:
            self._values["http_config"] = http_config
        if id is not None:
            self._values["id"] = id
        if lambda_config is not None:
            self._values["lambda_config"] = lambda_config
        if relational_database_config is not None:
            self._values["relational_database_config"] = relational_database_config
        if service_role_arn is not None:
            self._values["service_role_arn"] = service_role_arn

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#api_id AppsyncDatasource#api_id}.'''
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#name AppsyncDatasource#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#type AppsyncDatasource#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#description AppsyncDatasource#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dynamodb_config(self) -> typing.Optional["AppsyncDatasourceDynamodbConfig"]:
        '''dynamodb_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#dynamodb_config AppsyncDatasource#dynamodb_config}
        '''
        result = self._values.get("dynamodb_config")
        return typing.cast(typing.Optional["AppsyncDatasourceDynamodbConfig"], result)

    @builtins.property
    def elasticsearch_config(
        self,
    ) -> typing.Optional["AppsyncDatasourceElasticsearchConfig"]:
        '''elasticsearch_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#elasticsearch_config AppsyncDatasource#elasticsearch_config}
        '''
        result = self._values.get("elasticsearch_config")
        return typing.cast(typing.Optional["AppsyncDatasourceElasticsearchConfig"], result)

    @builtins.property
    def http_config(self) -> typing.Optional["AppsyncDatasourceHttpConfig"]:
        '''http_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#http_config AppsyncDatasource#http_config}
        '''
        result = self._values.get("http_config")
        return typing.cast(typing.Optional["AppsyncDatasourceHttpConfig"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#id AppsyncDatasource#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lambda_config(self) -> typing.Optional["AppsyncDatasourceLambdaConfig"]:
        '''lambda_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#lambda_config AppsyncDatasource#lambda_config}
        '''
        result = self._values.get("lambda_config")
        return typing.cast(typing.Optional["AppsyncDatasourceLambdaConfig"], result)

    @builtins.property
    def relational_database_config(
        self,
    ) -> typing.Optional["AppsyncDatasourceRelationalDatabaseConfig"]:
        '''relational_database_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#relational_database_config AppsyncDatasource#relational_database_config}
        '''
        result = self._values.get("relational_database_config")
        return typing.cast(typing.Optional["AppsyncDatasourceRelationalDatabaseConfig"], result)

    @builtins.property
    def service_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#service_role_arn AppsyncDatasource#service_role_arn}.'''
        result = self._values.get("service_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncDatasourceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appsyncDatasource.AppsyncDatasourceDynamodbConfig",
    jsii_struct_bases=[],
    name_mapping={
        "table_name": "tableName",
        "delta_sync_config": "deltaSyncConfig",
        "region": "region",
        "use_caller_credentials": "useCallerCredentials",
        "versioned": "versioned",
    },
)
class AppsyncDatasourceDynamodbConfig:
    def __init__(
        self,
        *,
        table_name: builtins.str,
        delta_sync_config: typing.Optional[typing.Union["AppsyncDatasourceDynamodbConfigDeltaSyncConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        region: typing.Optional[builtins.str] = None,
        use_caller_credentials: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        versioned: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param table_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#table_name AppsyncDatasource#table_name}.
        :param delta_sync_config: delta_sync_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#delta_sync_config AppsyncDatasource#delta_sync_config}
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#region AppsyncDatasource#region}.
        :param use_caller_credentials: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#use_caller_credentials AppsyncDatasource#use_caller_credentials}.
        :param versioned: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#versioned AppsyncDatasource#versioned}.
        '''
        if isinstance(delta_sync_config, dict):
            delta_sync_config = AppsyncDatasourceDynamodbConfigDeltaSyncConfig(**delta_sync_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3696e384179f33c22300a704e6b17b2a76b3d72e4810502bcc433600fdcfdcbd)
            check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
            check_type(argname="argument delta_sync_config", value=delta_sync_config, expected_type=type_hints["delta_sync_config"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument use_caller_credentials", value=use_caller_credentials, expected_type=type_hints["use_caller_credentials"])
            check_type(argname="argument versioned", value=versioned, expected_type=type_hints["versioned"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "table_name": table_name,
        }
        if delta_sync_config is not None:
            self._values["delta_sync_config"] = delta_sync_config
        if region is not None:
            self._values["region"] = region
        if use_caller_credentials is not None:
            self._values["use_caller_credentials"] = use_caller_credentials
        if versioned is not None:
            self._values["versioned"] = versioned

    @builtins.property
    def table_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#table_name AppsyncDatasource#table_name}.'''
        result = self._values.get("table_name")
        assert result is not None, "Required property 'table_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def delta_sync_config(
        self,
    ) -> typing.Optional["AppsyncDatasourceDynamodbConfigDeltaSyncConfig"]:
        '''delta_sync_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#delta_sync_config AppsyncDatasource#delta_sync_config}
        '''
        result = self._values.get("delta_sync_config")
        return typing.cast(typing.Optional["AppsyncDatasourceDynamodbConfigDeltaSyncConfig"], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#region AppsyncDatasource#region}.'''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def use_caller_credentials(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#use_caller_credentials AppsyncDatasource#use_caller_credentials}.'''
        result = self._values.get("use_caller_credentials")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def versioned(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#versioned AppsyncDatasource#versioned}.'''
        result = self._values.get("versioned")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncDatasourceDynamodbConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appsyncDatasource.AppsyncDatasourceDynamodbConfigDeltaSyncConfig",
    jsii_struct_bases=[],
    name_mapping={
        "delta_sync_table_name": "deltaSyncTableName",
        "base_table_ttl": "baseTableTtl",
        "delta_sync_table_ttl": "deltaSyncTableTtl",
    },
)
class AppsyncDatasourceDynamodbConfigDeltaSyncConfig:
    def __init__(
        self,
        *,
        delta_sync_table_name: builtins.str,
        base_table_ttl: typing.Optional[jsii.Number] = None,
        delta_sync_table_ttl: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param delta_sync_table_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#delta_sync_table_name AppsyncDatasource#delta_sync_table_name}.
        :param base_table_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#base_table_ttl AppsyncDatasource#base_table_ttl}.
        :param delta_sync_table_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#delta_sync_table_ttl AppsyncDatasource#delta_sync_table_ttl}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e56a5b37016f1df1f689934e150fcd1382104eac70cb71e83a89e02c1de77d1a)
            check_type(argname="argument delta_sync_table_name", value=delta_sync_table_name, expected_type=type_hints["delta_sync_table_name"])
            check_type(argname="argument base_table_ttl", value=base_table_ttl, expected_type=type_hints["base_table_ttl"])
            check_type(argname="argument delta_sync_table_ttl", value=delta_sync_table_ttl, expected_type=type_hints["delta_sync_table_ttl"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "delta_sync_table_name": delta_sync_table_name,
        }
        if base_table_ttl is not None:
            self._values["base_table_ttl"] = base_table_ttl
        if delta_sync_table_ttl is not None:
            self._values["delta_sync_table_ttl"] = delta_sync_table_ttl

    @builtins.property
    def delta_sync_table_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#delta_sync_table_name AppsyncDatasource#delta_sync_table_name}.'''
        result = self._values.get("delta_sync_table_name")
        assert result is not None, "Required property 'delta_sync_table_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def base_table_ttl(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#base_table_ttl AppsyncDatasource#base_table_ttl}.'''
        result = self._values.get("base_table_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def delta_sync_table_ttl(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#delta_sync_table_ttl AppsyncDatasource#delta_sync_table_ttl}.'''
        result = self._values.get("delta_sync_table_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncDatasourceDynamodbConfigDeltaSyncConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppsyncDatasourceDynamodbConfigDeltaSyncConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appsyncDatasource.AppsyncDatasourceDynamodbConfigDeltaSyncConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3585a56dcaf9b65703128345b5f9a33338883ecade8770c2deae97fdcae4877c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBaseTableTtl")
    def reset_base_table_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBaseTableTtl", []))

    @jsii.member(jsii_name="resetDeltaSyncTableTtl")
    def reset_delta_sync_table_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeltaSyncTableTtl", []))

    @builtins.property
    @jsii.member(jsii_name="baseTableTtlInput")
    def base_table_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "baseTableTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="deltaSyncTableNameInput")
    def delta_sync_table_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deltaSyncTableNameInput"))

    @builtins.property
    @jsii.member(jsii_name="deltaSyncTableTtlInput")
    def delta_sync_table_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "deltaSyncTableTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="baseTableTtl")
    def base_table_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "baseTableTtl"))

    @base_table_ttl.setter
    def base_table_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0fea69fe90eb55cdad76c1abfcdb11aa7079aae65d240789b4166ad9e9d0c92)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "baseTableTtl", value)

    @builtins.property
    @jsii.member(jsii_name="deltaSyncTableName")
    def delta_sync_table_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deltaSyncTableName"))

    @delta_sync_table_name.setter
    def delta_sync_table_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47f458c5f96d0e8f04841a6f210e4e9074ea6751357a60b2d21c13194090f272)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deltaSyncTableName", value)

    @builtins.property
    @jsii.member(jsii_name="deltaSyncTableTtl")
    def delta_sync_table_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "deltaSyncTableTtl"))

    @delta_sync_table_ttl.setter
    def delta_sync_table_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca7a6955ce9100bc3ce01f6e42e57915c18e6ef9b8607cd2cf4fd1271b4e2aeb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deltaSyncTableTtl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppsyncDatasourceDynamodbConfigDeltaSyncConfig]:
        return typing.cast(typing.Optional[AppsyncDatasourceDynamodbConfigDeltaSyncConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppsyncDatasourceDynamodbConfigDeltaSyncConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfc90cdaca7b48ba7a9ba149e69606aae3c63590b7b6233cffdeec91d92c565d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppsyncDatasourceDynamodbConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appsyncDatasource.AppsyncDatasourceDynamodbConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b1d4b45a79950bbe59798eaf56468b339557bd6769ea08b5225ee9453278bdcb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDeltaSyncConfig")
    def put_delta_sync_config(
        self,
        *,
        delta_sync_table_name: builtins.str,
        base_table_ttl: typing.Optional[jsii.Number] = None,
        delta_sync_table_ttl: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param delta_sync_table_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#delta_sync_table_name AppsyncDatasource#delta_sync_table_name}.
        :param base_table_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#base_table_ttl AppsyncDatasource#base_table_ttl}.
        :param delta_sync_table_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#delta_sync_table_ttl AppsyncDatasource#delta_sync_table_ttl}.
        '''
        value = AppsyncDatasourceDynamodbConfigDeltaSyncConfig(
            delta_sync_table_name=delta_sync_table_name,
            base_table_ttl=base_table_ttl,
            delta_sync_table_ttl=delta_sync_table_ttl,
        )

        return typing.cast(None, jsii.invoke(self, "putDeltaSyncConfig", [value]))

    @jsii.member(jsii_name="resetDeltaSyncConfig")
    def reset_delta_sync_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeltaSyncConfig", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetUseCallerCredentials")
    def reset_use_caller_credentials(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseCallerCredentials", []))

    @jsii.member(jsii_name="resetVersioned")
    def reset_versioned(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersioned", []))

    @builtins.property
    @jsii.member(jsii_name="deltaSyncConfig")
    def delta_sync_config(
        self,
    ) -> AppsyncDatasourceDynamodbConfigDeltaSyncConfigOutputReference:
        return typing.cast(AppsyncDatasourceDynamodbConfigDeltaSyncConfigOutputReference, jsii.get(self, "deltaSyncConfig"))

    @builtins.property
    @jsii.member(jsii_name="deltaSyncConfigInput")
    def delta_sync_config_input(
        self,
    ) -> typing.Optional[AppsyncDatasourceDynamodbConfigDeltaSyncConfig]:
        return typing.cast(typing.Optional[AppsyncDatasourceDynamodbConfigDeltaSyncConfig], jsii.get(self, "deltaSyncConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="tableNameInput")
    def table_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableNameInput"))

    @builtins.property
    @jsii.member(jsii_name="useCallerCredentialsInput")
    def use_caller_credentials_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "useCallerCredentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="versionedInput")
    def versioned_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "versionedInput"))

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__565a5ce944ab65cabc1bf9ff3dd4884212b6477962043edafdd98541ee2c2eb5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="tableName")
    def table_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tableName"))

    @table_name.setter
    def table_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00376b153f4c75768d27a90e5156e9520c4c813e2426142bb63c8c944b875003)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableName", value)

    @builtins.property
    @jsii.member(jsii_name="useCallerCredentials")
    def use_caller_credentials(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "useCallerCredentials"))

    @use_caller_credentials.setter
    def use_caller_credentials(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a102f61e7ce4f99baa8000bde47fd471f19432f82472a7005df15f6c0bc8fe9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useCallerCredentials", value)

    @builtins.property
    @jsii.member(jsii_name="versioned")
    def versioned(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "versioned"))

    @versioned.setter
    def versioned(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eeba8e5120e14f090fc4c10cbcefa741f3dc7823c1e55320823afcc688a16984)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "versioned", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppsyncDatasourceDynamodbConfig]:
        return typing.cast(typing.Optional[AppsyncDatasourceDynamodbConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppsyncDatasourceDynamodbConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0af848ad029985d6455610ab3a3a95aa1f50946575e2cbab95fd2baed89816f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appsyncDatasource.AppsyncDatasourceElasticsearchConfig",
    jsii_struct_bases=[],
    name_mapping={"endpoint": "endpoint", "region": "region"},
)
class AppsyncDatasourceElasticsearchConfig:
    def __init__(
        self,
        *,
        endpoint: builtins.str,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#endpoint AppsyncDatasource#endpoint}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#region AppsyncDatasource#region}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cec811bc0f06bc111309e12cec711ece8d595920c985a15dc793a08482f5fbb9)
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "endpoint": endpoint,
        }
        if region is not None:
            self._values["region"] = region

    @builtins.property
    def endpoint(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#endpoint AppsyncDatasource#endpoint}.'''
        result = self._values.get("endpoint")
        assert result is not None, "Required property 'endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#region AppsyncDatasource#region}.'''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncDatasourceElasticsearchConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppsyncDatasourceElasticsearchConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appsyncDatasource.AppsyncDatasourceElasticsearchConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b81e2d6c26407c1bfef1b08ebc975ca81c56d12e2af505705d1259c14e259ed4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @builtins.property
    @jsii.member(jsii_name="endpointInput")
    def endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @endpoint.setter
    def endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__630ca0261145c9de9df2b0c9e55e199cb3a6b55bd0219549d62a1892a98c51b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpoint", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af7eb637b87b3813207aea3c819ff45bd78dee804a32fb35ae3a5b860c06b5d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppsyncDatasourceElasticsearchConfig]:
        return typing.cast(typing.Optional[AppsyncDatasourceElasticsearchConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppsyncDatasourceElasticsearchConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e627a757d2b8916339234630f8f6830a4f280af9c66955868976ba180f8c7aca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appsyncDatasource.AppsyncDatasourceHttpConfig",
    jsii_struct_bases=[],
    name_mapping={
        "endpoint": "endpoint",
        "authorization_config": "authorizationConfig",
    },
)
class AppsyncDatasourceHttpConfig:
    def __init__(
        self,
        *,
        endpoint: builtins.str,
        authorization_config: typing.Optional[typing.Union["AppsyncDatasourceHttpConfigAuthorizationConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#endpoint AppsyncDatasource#endpoint}.
        :param authorization_config: authorization_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#authorization_config AppsyncDatasource#authorization_config}
        '''
        if isinstance(authorization_config, dict):
            authorization_config = AppsyncDatasourceHttpConfigAuthorizationConfig(**authorization_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb5f8d417b8422cfe92780709533b00c14c9ab0ae7a889d74dca6b2225866e0a)
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            check_type(argname="argument authorization_config", value=authorization_config, expected_type=type_hints["authorization_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "endpoint": endpoint,
        }
        if authorization_config is not None:
            self._values["authorization_config"] = authorization_config

    @builtins.property
    def endpoint(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#endpoint AppsyncDatasource#endpoint}.'''
        result = self._values.get("endpoint")
        assert result is not None, "Required property 'endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authorization_config(
        self,
    ) -> typing.Optional["AppsyncDatasourceHttpConfigAuthorizationConfig"]:
        '''authorization_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#authorization_config AppsyncDatasource#authorization_config}
        '''
        result = self._values.get("authorization_config")
        return typing.cast(typing.Optional["AppsyncDatasourceHttpConfigAuthorizationConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncDatasourceHttpConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appsyncDatasource.AppsyncDatasourceHttpConfigAuthorizationConfig",
    jsii_struct_bases=[],
    name_mapping={
        "authorization_type": "authorizationType",
        "aws_iam_config": "awsIamConfig",
    },
)
class AppsyncDatasourceHttpConfigAuthorizationConfig:
    def __init__(
        self,
        *,
        authorization_type: typing.Optional[builtins.str] = None,
        aws_iam_config: typing.Optional[typing.Union["AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param authorization_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#authorization_type AppsyncDatasource#authorization_type}.
        :param aws_iam_config: aws_iam_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#aws_iam_config AppsyncDatasource#aws_iam_config}
        '''
        if isinstance(aws_iam_config, dict):
            aws_iam_config = AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfig(**aws_iam_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b69119e5e68488c250fe1828ddc2d419576df3674a6b52f58fe5b75787a0bb94)
            check_type(argname="argument authorization_type", value=authorization_type, expected_type=type_hints["authorization_type"])
            check_type(argname="argument aws_iam_config", value=aws_iam_config, expected_type=type_hints["aws_iam_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if authorization_type is not None:
            self._values["authorization_type"] = authorization_type
        if aws_iam_config is not None:
            self._values["aws_iam_config"] = aws_iam_config

    @builtins.property
    def authorization_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#authorization_type AppsyncDatasource#authorization_type}.'''
        result = self._values.get("authorization_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aws_iam_config(
        self,
    ) -> typing.Optional["AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfig"]:
        '''aws_iam_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#aws_iam_config AppsyncDatasource#aws_iam_config}
        '''
        result = self._values.get("aws_iam_config")
        return typing.cast(typing.Optional["AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncDatasourceHttpConfigAuthorizationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appsyncDatasource.AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfig",
    jsii_struct_bases=[],
    name_mapping={
        "signing_region": "signingRegion",
        "signing_service_name": "signingServiceName",
    },
)
class AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfig:
    def __init__(
        self,
        *,
        signing_region: typing.Optional[builtins.str] = None,
        signing_service_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param signing_region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#signing_region AppsyncDatasource#signing_region}.
        :param signing_service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#signing_service_name AppsyncDatasource#signing_service_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73440df39b4e47af8255915817d4bbb9813cc66a6c9cca75c1d715707c99446b)
            check_type(argname="argument signing_region", value=signing_region, expected_type=type_hints["signing_region"])
            check_type(argname="argument signing_service_name", value=signing_service_name, expected_type=type_hints["signing_service_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if signing_region is not None:
            self._values["signing_region"] = signing_region
        if signing_service_name is not None:
            self._values["signing_service_name"] = signing_service_name

    @builtins.property
    def signing_region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#signing_region AppsyncDatasource#signing_region}.'''
        result = self._values.get("signing_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def signing_service_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#signing_service_name AppsyncDatasource#signing_service_name}.'''
        result = self._values.get("signing_service_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appsyncDatasource.AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7a2acf4a61da9b32ee0b12adc023309d36ba7804d7ca34baeec69e4b9781744a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetSigningRegion")
    def reset_signing_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSigningRegion", []))

    @jsii.member(jsii_name="resetSigningServiceName")
    def reset_signing_service_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSigningServiceName", []))

    @builtins.property
    @jsii.member(jsii_name="signingRegionInput")
    def signing_region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "signingRegionInput"))

    @builtins.property
    @jsii.member(jsii_name="signingServiceNameInput")
    def signing_service_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "signingServiceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="signingRegion")
    def signing_region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "signingRegion"))

    @signing_region.setter
    def signing_region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd15707fd32089bddd1bc24454bd61c9ef05efe8f705e74020c0556b23d15368)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signingRegion", value)

    @builtins.property
    @jsii.member(jsii_name="signingServiceName")
    def signing_service_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "signingServiceName"))

    @signing_service_name.setter
    def signing_service_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0d1d855275fddd5b030f2b2f544d9a6c836e35beb6d1518ad1917854c7cd665)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signingServiceName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfig]:
        return typing.cast(typing.Optional[AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17cdd51d050b1b2e0bac937ff09886bf15fb7dd00228a7364589b79d12138195)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppsyncDatasourceHttpConfigAuthorizationConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appsyncDatasource.AppsyncDatasourceHttpConfigAuthorizationConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d9443d5c94246462f4bdddee99b3811a5a0ed84f3ad582a57f5a9959b0f62667)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAwsIamConfig")
    def put_aws_iam_config(
        self,
        *,
        signing_region: typing.Optional[builtins.str] = None,
        signing_service_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param signing_region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#signing_region AppsyncDatasource#signing_region}.
        :param signing_service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#signing_service_name AppsyncDatasource#signing_service_name}.
        '''
        value = AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfig(
            signing_region=signing_region, signing_service_name=signing_service_name
        )

        return typing.cast(None, jsii.invoke(self, "putAwsIamConfig", [value]))

    @jsii.member(jsii_name="resetAuthorizationType")
    def reset_authorization_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthorizationType", []))

    @jsii.member(jsii_name="resetAwsIamConfig")
    def reset_aws_iam_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsIamConfig", []))

    @builtins.property
    @jsii.member(jsii_name="awsIamConfig")
    def aws_iam_config(
        self,
    ) -> AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfigOutputReference:
        return typing.cast(AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfigOutputReference, jsii.get(self, "awsIamConfig"))

    @builtins.property
    @jsii.member(jsii_name="authorizationTypeInput")
    def authorization_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authorizationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="awsIamConfigInput")
    def aws_iam_config_input(
        self,
    ) -> typing.Optional[AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfig]:
        return typing.cast(typing.Optional[AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfig], jsii.get(self, "awsIamConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="authorizationType")
    def authorization_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authorizationType"))

    @authorization_type.setter
    def authorization_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e72eb98da845f90e589dff715df092af65a4f0d9713e900f282c6622d2cfbc71)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizationType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppsyncDatasourceHttpConfigAuthorizationConfig]:
        return typing.cast(typing.Optional[AppsyncDatasourceHttpConfigAuthorizationConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppsyncDatasourceHttpConfigAuthorizationConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85bfba08dc943074a86d3a84e119f8b265f377c89229cb1234eb6857674246a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppsyncDatasourceHttpConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appsyncDatasource.AppsyncDatasourceHttpConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__986efb10be74b69a4794f8280a3d17ade39b1e1b9feaf17abc128e8c260f5ebc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAuthorizationConfig")
    def put_authorization_config(
        self,
        *,
        authorization_type: typing.Optional[builtins.str] = None,
        aws_iam_config: typing.Optional[typing.Union[AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param authorization_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#authorization_type AppsyncDatasource#authorization_type}.
        :param aws_iam_config: aws_iam_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#aws_iam_config AppsyncDatasource#aws_iam_config}
        '''
        value = AppsyncDatasourceHttpConfigAuthorizationConfig(
            authorization_type=authorization_type, aws_iam_config=aws_iam_config
        )

        return typing.cast(None, jsii.invoke(self, "putAuthorizationConfig", [value]))

    @jsii.member(jsii_name="resetAuthorizationConfig")
    def reset_authorization_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthorizationConfig", []))

    @builtins.property
    @jsii.member(jsii_name="authorizationConfig")
    def authorization_config(
        self,
    ) -> AppsyncDatasourceHttpConfigAuthorizationConfigOutputReference:
        return typing.cast(AppsyncDatasourceHttpConfigAuthorizationConfigOutputReference, jsii.get(self, "authorizationConfig"))

    @builtins.property
    @jsii.member(jsii_name="authorizationConfigInput")
    def authorization_config_input(
        self,
    ) -> typing.Optional[AppsyncDatasourceHttpConfigAuthorizationConfig]:
        return typing.cast(typing.Optional[AppsyncDatasourceHttpConfigAuthorizationConfig], jsii.get(self, "authorizationConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointInput")
    def endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointInput"))

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @endpoint.setter
    def endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28cabfe07c83af919d4375a4a21f619467924e9bbf71c4b098a79457c352c403)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpoint", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppsyncDatasourceHttpConfig]:
        return typing.cast(typing.Optional[AppsyncDatasourceHttpConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppsyncDatasourceHttpConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70fd6e4db14f8e5aa5c9641221808ba66860ee6a45f35b55131920a6701357d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appsyncDatasource.AppsyncDatasourceLambdaConfig",
    jsii_struct_bases=[],
    name_mapping={"function_arn": "functionArn"},
)
class AppsyncDatasourceLambdaConfig:
    def __init__(self, *, function_arn: builtins.str) -> None:
        '''
        :param function_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#function_arn AppsyncDatasource#function_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58ad03e54216fc78ce2ed21e58f6ca46a6a54f08ed9410626205d42558df8942)
            check_type(argname="argument function_arn", value=function_arn, expected_type=type_hints["function_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "function_arn": function_arn,
        }

    @builtins.property
    def function_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#function_arn AppsyncDatasource#function_arn}.'''
        result = self._values.get("function_arn")
        assert result is not None, "Required property 'function_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncDatasourceLambdaConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppsyncDatasourceLambdaConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appsyncDatasource.AppsyncDatasourceLambdaConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__138dc0314c35c7707aa2532b98e396ebcfdf556ecdd90d6d177795fd0260eab8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="functionArnInput")
    def function_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "functionArnInput"))

    @builtins.property
    @jsii.member(jsii_name="functionArn")
    def function_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "functionArn"))

    @function_arn.setter
    def function_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9dfebf9ae07ba990bf4b3a0c09c2b535e5917a0f32cf9e87c9989ae0be62fa26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "functionArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppsyncDatasourceLambdaConfig]:
        return typing.cast(typing.Optional[AppsyncDatasourceLambdaConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppsyncDatasourceLambdaConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7cac99b6c246d6e50c4a7ef6e8afb92d854dfdd0bc18023d1dcec3a3a58b9bdc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appsyncDatasource.AppsyncDatasourceRelationalDatabaseConfig",
    jsii_struct_bases=[],
    name_mapping={
        "http_endpoint_config": "httpEndpointConfig",
        "source_type": "sourceType",
    },
)
class AppsyncDatasourceRelationalDatabaseConfig:
    def __init__(
        self,
        *,
        http_endpoint_config: typing.Optional[typing.Union["AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        source_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param http_endpoint_config: http_endpoint_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#http_endpoint_config AppsyncDatasource#http_endpoint_config}
        :param source_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#source_type AppsyncDatasource#source_type}.
        '''
        if isinstance(http_endpoint_config, dict):
            http_endpoint_config = AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfig(**http_endpoint_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6997ebcc47a7dd95c7c3fad51879a90f99c9391bab503b4344cfb23c97e8facd)
            check_type(argname="argument http_endpoint_config", value=http_endpoint_config, expected_type=type_hints["http_endpoint_config"])
            check_type(argname="argument source_type", value=source_type, expected_type=type_hints["source_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if http_endpoint_config is not None:
            self._values["http_endpoint_config"] = http_endpoint_config
        if source_type is not None:
            self._values["source_type"] = source_type

    @builtins.property
    def http_endpoint_config(
        self,
    ) -> typing.Optional["AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfig"]:
        '''http_endpoint_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#http_endpoint_config AppsyncDatasource#http_endpoint_config}
        '''
        result = self._values.get("http_endpoint_config")
        return typing.cast(typing.Optional["AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfig"], result)

    @builtins.property
    def source_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#source_type AppsyncDatasource#source_type}.'''
        result = self._values.get("source_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncDatasourceRelationalDatabaseConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appsyncDatasource.AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfig",
    jsii_struct_bases=[],
    name_mapping={
        "aws_secret_store_arn": "awsSecretStoreArn",
        "db_cluster_identifier": "dbClusterIdentifier",
        "database_name": "databaseName",
        "region": "region",
        "schema": "schema",
    },
)
class AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfig:
    def __init__(
        self,
        *,
        aws_secret_store_arn: builtins.str,
        db_cluster_identifier: builtins.str,
        database_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        schema: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_secret_store_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#aws_secret_store_arn AppsyncDatasource#aws_secret_store_arn}.
        :param db_cluster_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#db_cluster_identifier AppsyncDatasource#db_cluster_identifier}.
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#database_name AppsyncDatasource#database_name}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#region AppsyncDatasource#region}.
        :param schema: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#schema AppsyncDatasource#schema}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a0bd99aba87307b74f3f416c39c7a22f5ff7235d8cebf45c4574e05df876b5c)
            check_type(argname="argument aws_secret_store_arn", value=aws_secret_store_arn, expected_type=type_hints["aws_secret_store_arn"])
            check_type(argname="argument db_cluster_identifier", value=db_cluster_identifier, expected_type=type_hints["db_cluster_identifier"])
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "aws_secret_store_arn": aws_secret_store_arn,
            "db_cluster_identifier": db_cluster_identifier,
        }
        if database_name is not None:
            self._values["database_name"] = database_name
        if region is not None:
            self._values["region"] = region
        if schema is not None:
            self._values["schema"] = schema

    @builtins.property
    def aws_secret_store_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#aws_secret_store_arn AppsyncDatasource#aws_secret_store_arn}.'''
        result = self._values.get("aws_secret_store_arn")
        assert result is not None, "Required property 'aws_secret_store_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def db_cluster_identifier(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#db_cluster_identifier AppsyncDatasource#db_cluster_identifier}.'''
        result = self._values.get("db_cluster_identifier")
        assert result is not None, "Required property 'db_cluster_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def database_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#database_name AppsyncDatasource#database_name}.'''
        result = self._values.get("database_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#region AppsyncDatasource#region}.'''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schema(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#schema AppsyncDatasource#schema}.'''
        result = self._values.get("schema")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appsyncDatasource.AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__babd9102b979b09b65b12a226281a2e9e25afd484e9ce763adf68c47c8307dee)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDatabaseName")
    def reset_database_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatabaseName", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetSchema")
    def reset_schema(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchema", []))

    @builtins.property
    @jsii.member(jsii_name="awsSecretStoreArnInput")
    def aws_secret_store_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "awsSecretStoreArnInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseNameInput")
    def database_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseNameInput"))

    @builtins.property
    @jsii.member(jsii_name="dbClusterIdentifierInput")
    def db_cluster_identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dbClusterIdentifierInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaInput")
    def schema_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaInput"))

    @builtins.property
    @jsii.member(jsii_name="awsSecretStoreArn")
    def aws_secret_store_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "awsSecretStoreArn"))

    @aws_secret_store_arn.setter
    def aws_secret_store_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87bf1b9f47a4fafc9d14eee83a629186a181bb82f31053205d4572b8802cfcf1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsSecretStoreArn", value)

    @builtins.property
    @jsii.member(jsii_name="databaseName")
    def database_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseName"))

    @database_name.setter
    def database_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a2b1eb7dff4401fae8ddd308bc9365aa2465443216f5c3705819b3f158a5dbd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseName", value)

    @builtins.property
    @jsii.member(jsii_name="dbClusterIdentifier")
    def db_cluster_identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dbClusterIdentifier"))

    @db_cluster_identifier.setter
    def db_cluster_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c314856b9f6943093b71176b40b8fa10109da30eab645b33dbe84728d000683c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbClusterIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76102749ba63ca31ba20c7f0c2df058df3258ecd16c0d4883f50f36699495284)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="schema")
    def schema(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schema"))

    @schema.setter
    def schema(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96cb9c6fad6f34d2fb1588c614b7c38213b470ce09647f79adb9857c7bb50567)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schema", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfig]:
        return typing.cast(typing.Optional[AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45a31a0b1fee59fbc5e8d96521e61399a7b662af0a2c0e03d0ff51239f0c1a87)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppsyncDatasourceRelationalDatabaseConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appsyncDatasource.AppsyncDatasourceRelationalDatabaseConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8add3c84cfc5fd0b332bc5509f145c949c4212e9c465bd7b66c3b538f3dc4a55)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putHttpEndpointConfig")
    def put_http_endpoint_config(
        self,
        *,
        aws_secret_store_arn: builtins.str,
        db_cluster_identifier: builtins.str,
        database_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        schema: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_secret_store_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#aws_secret_store_arn AppsyncDatasource#aws_secret_store_arn}.
        :param db_cluster_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#db_cluster_identifier AppsyncDatasource#db_cluster_identifier}.
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#database_name AppsyncDatasource#database_name}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#region AppsyncDatasource#region}.
        :param schema: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#schema AppsyncDatasource#schema}.
        '''
        value = AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfig(
            aws_secret_store_arn=aws_secret_store_arn,
            db_cluster_identifier=db_cluster_identifier,
            database_name=database_name,
            region=region,
            schema=schema,
        )

        return typing.cast(None, jsii.invoke(self, "putHttpEndpointConfig", [value]))

    @jsii.member(jsii_name="resetHttpEndpointConfig")
    def reset_http_endpoint_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpEndpointConfig", []))

    @jsii.member(jsii_name="resetSourceType")
    def reset_source_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceType", []))

    @builtins.property
    @jsii.member(jsii_name="httpEndpointConfig")
    def http_endpoint_config(
        self,
    ) -> AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfigOutputReference:
        return typing.cast(AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfigOutputReference, jsii.get(self, "httpEndpointConfig"))

    @builtins.property
    @jsii.member(jsii_name="httpEndpointConfigInput")
    def http_endpoint_config_input(
        self,
    ) -> typing.Optional[AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfig]:
        return typing.cast(typing.Optional[AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfig], jsii.get(self, "httpEndpointConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceTypeInput")
    def source_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceType")
    def source_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceType"))

    @source_type.setter
    def source_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23b0f69f0c43d9e21e418d2e5cea250760e5a8aaba3dd90df251516347b7bff9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppsyncDatasourceRelationalDatabaseConfig]:
        return typing.cast(typing.Optional[AppsyncDatasourceRelationalDatabaseConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppsyncDatasourceRelationalDatabaseConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54e2bb1ce8cdef13277295446c132a7361ec81c1e1396733c9ec7f186e66b205)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "AppsyncDatasource",
    "AppsyncDatasourceConfig",
    "AppsyncDatasourceDynamodbConfig",
    "AppsyncDatasourceDynamodbConfigDeltaSyncConfig",
    "AppsyncDatasourceDynamodbConfigDeltaSyncConfigOutputReference",
    "AppsyncDatasourceDynamodbConfigOutputReference",
    "AppsyncDatasourceElasticsearchConfig",
    "AppsyncDatasourceElasticsearchConfigOutputReference",
    "AppsyncDatasourceHttpConfig",
    "AppsyncDatasourceHttpConfigAuthorizationConfig",
    "AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfig",
    "AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfigOutputReference",
    "AppsyncDatasourceHttpConfigAuthorizationConfigOutputReference",
    "AppsyncDatasourceHttpConfigOutputReference",
    "AppsyncDatasourceLambdaConfig",
    "AppsyncDatasourceLambdaConfigOutputReference",
    "AppsyncDatasourceRelationalDatabaseConfig",
    "AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfig",
    "AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfigOutputReference",
    "AppsyncDatasourceRelationalDatabaseConfigOutputReference",
]

publication.publish()

def _typecheckingstub__a75711e528346865046793fbd1a3583fc51ab214f74b7ed6993e2f86027e910d(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    api_id: builtins.str,
    name: builtins.str,
    type: builtins.str,
    description: typing.Optional[builtins.str] = None,
    dynamodb_config: typing.Optional[typing.Union[AppsyncDatasourceDynamodbConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    elasticsearch_config: typing.Optional[typing.Union[AppsyncDatasourceElasticsearchConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    http_config: typing.Optional[typing.Union[AppsyncDatasourceHttpConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    lambda_config: typing.Optional[typing.Union[AppsyncDatasourceLambdaConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    relational_database_config: typing.Optional[typing.Union[AppsyncDatasourceRelationalDatabaseConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    service_role_arn: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__d33a4e069651015c5c38c2507186d712c5e2abaa955cebfc0a7bd076fc7dab9b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2f0a52c09ebc2ae757e06cb235daef4da5c320ee9090cc48b0bb854c274a4e8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9349031ce2736852e43ca1ef2a3d672cf3b56d142e4cab5c4d3f35c92162c8fc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04fe807be50cb424c432536ec17ab753f341f522688ac6e8f7e43ebfc34696b2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a428fd979f934136c07fa82f6d1d76f195dd4e74742e885379fa0c88c59f9c0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b926b87f372f58a5b7a2cdb842bf760e57c8e282f8f210f101b53fb17abab806(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbb4433154a45a7ce7cf44a17d94eb7d198a20a4f08c1333ec06a8d9a05c68f6(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    api_id: builtins.str,
    name: builtins.str,
    type: builtins.str,
    description: typing.Optional[builtins.str] = None,
    dynamodb_config: typing.Optional[typing.Union[AppsyncDatasourceDynamodbConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    elasticsearch_config: typing.Optional[typing.Union[AppsyncDatasourceElasticsearchConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    http_config: typing.Optional[typing.Union[AppsyncDatasourceHttpConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    lambda_config: typing.Optional[typing.Union[AppsyncDatasourceLambdaConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    relational_database_config: typing.Optional[typing.Union[AppsyncDatasourceRelationalDatabaseConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    service_role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3696e384179f33c22300a704e6b17b2a76b3d72e4810502bcc433600fdcfdcbd(
    *,
    table_name: builtins.str,
    delta_sync_config: typing.Optional[typing.Union[AppsyncDatasourceDynamodbConfigDeltaSyncConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    region: typing.Optional[builtins.str] = None,
    use_caller_credentials: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    versioned: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e56a5b37016f1df1f689934e150fcd1382104eac70cb71e83a89e02c1de77d1a(
    *,
    delta_sync_table_name: builtins.str,
    base_table_ttl: typing.Optional[jsii.Number] = None,
    delta_sync_table_ttl: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3585a56dcaf9b65703128345b5f9a33338883ecade8770c2deae97fdcae4877c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0fea69fe90eb55cdad76c1abfcdb11aa7079aae65d240789b4166ad9e9d0c92(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47f458c5f96d0e8f04841a6f210e4e9074ea6751357a60b2d21c13194090f272(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca7a6955ce9100bc3ce01f6e42e57915c18e6ef9b8607cd2cf4fd1271b4e2aeb(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfc90cdaca7b48ba7a9ba149e69606aae3c63590b7b6233cffdeec91d92c565d(
    value: typing.Optional[AppsyncDatasourceDynamodbConfigDeltaSyncConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1d4b45a79950bbe59798eaf56468b339557bd6769ea08b5225ee9453278bdcb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__565a5ce944ab65cabc1bf9ff3dd4884212b6477962043edafdd98541ee2c2eb5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00376b153f4c75768d27a90e5156e9520c4c813e2426142bb63c8c944b875003(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a102f61e7ce4f99baa8000bde47fd471f19432f82472a7005df15f6c0bc8fe9(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eeba8e5120e14f090fc4c10cbcefa741f3dc7823c1e55320823afcc688a16984(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0af848ad029985d6455610ab3a3a95aa1f50946575e2cbab95fd2baed89816f(
    value: typing.Optional[AppsyncDatasourceDynamodbConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cec811bc0f06bc111309e12cec711ece8d595920c985a15dc793a08482f5fbb9(
    *,
    endpoint: builtins.str,
    region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b81e2d6c26407c1bfef1b08ebc975ca81c56d12e2af505705d1259c14e259ed4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__630ca0261145c9de9df2b0c9e55e199cb3a6b55bd0219549d62a1892a98c51b8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af7eb637b87b3813207aea3c819ff45bd78dee804a32fb35ae3a5b860c06b5d7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e627a757d2b8916339234630f8f6830a4f280af9c66955868976ba180f8c7aca(
    value: typing.Optional[AppsyncDatasourceElasticsearchConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb5f8d417b8422cfe92780709533b00c14c9ab0ae7a889d74dca6b2225866e0a(
    *,
    endpoint: builtins.str,
    authorization_config: typing.Optional[typing.Union[AppsyncDatasourceHttpConfigAuthorizationConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b69119e5e68488c250fe1828ddc2d419576df3674a6b52f58fe5b75787a0bb94(
    *,
    authorization_type: typing.Optional[builtins.str] = None,
    aws_iam_config: typing.Optional[typing.Union[AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73440df39b4e47af8255915817d4bbb9813cc66a6c9cca75c1d715707c99446b(
    *,
    signing_region: typing.Optional[builtins.str] = None,
    signing_service_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a2acf4a61da9b32ee0b12adc023309d36ba7804d7ca34baeec69e4b9781744a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd15707fd32089bddd1bc24454bd61c9ef05efe8f705e74020c0556b23d15368(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0d1d855275fddd5b030f2b2f544d9a6c836e35beb6d1518ad1917854c7cd665(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17cdd51d050b1b2e0bac937ff09886bf15fb7dd00228a7364589b79d12138195(
    value: typing.Optional[AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9443d5c94246462f4bdddee99b3811a5a0ed84f3ad582a57f5a9959b0f62667(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e72eb98da845f90e589dff715df092af65a4f0d9713e900f282c6622d2cfbc71(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85bfba08dc943074a86d3a84e119f8b265f377c89229cb1234eb6857674246a0(
    value: typing.Optional[AppsyncDatasourceHttpConfigAuthorizationConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__986efb10be74b69a4794f8280a3d17ade39b1e1b9feaf17abc128e8c260f5ebc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28cabfe07c83af919d4375a4a21f619467924e9bbf71c4b098a79457c352c403(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70fd6e4db14f8e5aa5c9641221808ba66860ee6a45f35b55131920a6701357d6(
    value: typing.Optional[AppsyncDatasourceHttpConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58ad03e54216fc78ce2ed21e58f6ca46a6a54f08ed9410626205d42558df8942(
    *,
    function_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__138dc0314c35c7707aa2532b98e396ebcfdf556ecdd90d6d177795fd0260eab8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9dfebf9ae07ba990bf4b3a0c09c2b535e5917a0f32cf9e87c9989ae0be62fa26(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7cac99b6c246d6e50c4a7ef6e8afb92d854dfdd0bc18023d1dcec3a3a58b9bdc(
    value: typing.Optional[AppsyncDatasourceLambdaConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6997ebcc47a7dd95c7c3fad51879a90f99c9391bab503b4344cfb23c97e8facd(
    *,
    http_endpoint_config: typing.Optional[typing.Union[AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    source_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a0bd99aba87307b74f3f416c39c7a22f5ff7235d8cebf45c4574e05df876b5c(
    *,
    aws_secret_store_arn: builtins.str,
    db_cluster_identifier: builtins.str,
    database_name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    schema: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__babd9102b979b09b65b12a226281a2e9e25afd484e9ce763adf68c47c8307dee(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87bf1b9f47a4fafc9d14eee83a629186a181bb82f31053205d4572b8802cfcf1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a2b1eb7dff4401fae8ddd308bc9365aa2465443216f5c3705819b3f158a5dbd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c314856b9f6943093b71176b40b8fa10109da30eab645b33dbe84728d000683c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76102749ba63ca31ba20c7f0c2df058df3258ecd16c0d4883f50f36699495284(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96cb9c6fad6f34d2fb1588c614b7c38213b470ce09647f79adb9857c7bb50567(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45a31a0b1fee59fbc5e8d96521e61399a7b662af0a2c0e03d0ff51239f0c1a87(
    value: typing.Optional[AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8add3c84cfc5fd0b332bc5509f145c949c4212e9c465bd7b66c3b538f3dc4a55(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23b0f69f0c43d9e21e418d2e5cea250760e5a8aaba3dd90df251516347b7bff9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54e2bb1ce8cdef13277295446c132a7361ec81c1e1396733c9ec7f186e66b205(
    value: typing.Optional[AppsyncDatasourceRelationalDatabaseConfig],
) -> None:
    """Type checking stubs"""
    pass
