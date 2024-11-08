'''
# `aws_quicksight_data_source`

Refer to the Terraform Registory for docs: [`aws_quicksight_data_source`](https://www.terraform.io/docs/providers/aws/r/quicksight_data_source).
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


class QuicksightDataSource(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.quicksightDataSource.QuicksightDataSource",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source aws_quicksight_data_source}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        data_source_id: builtins.str,
        name: builtins.str,
        parameters: typing.Union["QuicksightDataSourceParameters", typing.Dict[builtins.str, typing.Any]],
        type: builtins.str,
        aws_account_id: typing.Optional[builtins.str] = None,
        credentials: typing.Optional[typing.Union["QuicksightDataSourceCredentials", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        permission: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["QuicksightDataSourcePermission", typing.Dict[builtins.str, typing.Any]]]]] = None,
        ssl_properties: typing.Optional[typing.Union["QuicksightDataSourceSslProperties", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        vpc_connection_properties: typing.Optional[typing.Union["QuicksightDataSourceVpcConnectionProperties", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source aws_quicksight_data_source} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param data_source_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#data_source_id QuicksightDataSource#data_source_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#name QuicksightDataSource#name}.
        :param parameters: parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#parameters QuicksightDataSource#parameters}
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#type QuicksightDataSource#type}.
        :param aws_account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#aws_account_id QuicksightDataSource#aws_account_id}.
        :param credentials: credentials block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#credentials QuicksightDataSource#credentials}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#id QuicksightDataSource#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param permission: permission block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#permission QuicksightDataSource#permission}
        :param ssl_properties: ssl_properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#ssl_properties QuicksightDataSource#ssl_properties}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#tags QuicksightDataSource#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#tags_all QuicksightDataSource#tags_all}.
        :param vpc_connection_properties: vpc_connection_properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#vpc_connection_properties QuicksightDataSource#vpc_connection_properties}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72e28790189a2c109b007044db61c5065ff546eaf12e7583c61ce7b167e3828f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = QuicksightDataSourceConfig(
            data_source_id=data_source_id,
            name=name,
            parameters=parameters,
            type=type,
            aws_account_id=aws_account_id,
            credentials=credentials,
            id=id,
            permission=permission,
            ssl_properties=ssl_properties,
            tags=tags,
            tags_all=tags_all,
            vpc_connection_properties=vpc_connection_properties,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCredentials")
    def put_credentials(
        self,
        *,
        copy_source_arn: typing.Optional[builtins.str] = None,
        credential_pair: typing.Optional[typing.Union["QuicksightDataSourceCredentialsCredentialPair", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param copy_source_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#copy_source_arn QuicksightDataSource#copy_source_arn}.
        :param credential_pair: credential_pair block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#credential_pair QuicksightDataSource#credential_pair}
        '''
        value = QuicksightDataSourceCredentials(
            copy_source_arn=copy_source_arn, credential_pair=credential_pair
        )

        return typing.cast(None, jsii.invoke(self, "putCredentials", [value]))

    @jsii.member(jsii_name="putParameters")
    def put_parameters(
        self,
        *,
        amazon_elasticsearch: typing.Optional[typing.Union["QuicksightDataSourceParametersAmazonElasticsearch", typing.Dict[builtins.str, typing.Any]]] = None,
        athena: typing.Optional[typing.Union["QuicksightDataSourceParametersAthena", typing.Dict[builtins.str, typing.Any]]] = None,
        aurora: typing.Optional[typing.Union["QuicksightDataSourceParametersAurora", typing.Dict[builtins.str, typing.Any]]] = None,
        aurora_postgresql: typing.Optional[typing.Union["QuicksightDataSourceParametersAuroraPostgresql", typing.Dict[builtins.str, typing.Any]]] = None,
        aws_iot_analytics: typing.Optional[typing.Union["QuicksightDataSourceParametersAwsIotAnalytics", typing.Dict[builtins.str, typing.Any]]] = None,
        jira: typing.Optional[typing.Union["QuicksightDataSourceParametersJira", typing.Dict[builtins.str, typing.Any]]] = None,
        maria_db: typing.Optional[typing.Union["QuicksightDataSourceParametersMariaDb", typing.Dict[builtins.str, typing.Any]]] = None,
        mysql: typing.Optional[typing.Union["QuicksightDataSourceParametersMysql", typing.Dict[builtins.str, typing.Any]]] = None,
        oracle: typing.Optional[typing.Union["QuicksightDataSourceParametersOracle", typing.Dict[builtins.str, typing.Any]]] = None,
        postgresql: typing.Optional[typing.Union["QuicksightDataSourceParametersPostgresql", typing.Dict[builtins.str, typing.Any]]] = None,
        presto: typing.Optional[typing.Union["QuicksightDataSourceParametersPresto", typing.Dict[builtins.str, typing.Any]]] = None,
        rds: typing.Optional[typing.Union["QuicksightDataSourceParametersRds", typing.Dict[builtins.str, typing.Any]]] = None,
        redshift: typing.Optional[typing.Union["QuicksightDataSourceParametersRedshift", typing.Dict[builtins.str, typing.Any]]] = None,
        s3: typing.Optional[typing.Union["QuicksightDataSourceParametersS3", typing.Dict[builtins.str, typing.Any]]] = None,
        service_now: typing.Optional[typing.Union["QuicksightDataSourceParametersServiceNow", typing.Dict[builtins.str, typing.Any]]] = None,
        snowflake: typing.Optional[typing.Union["QuicksightDataSourceParametersSnowflake", typing.Dict[builtins.str, typing.Any]]] = None,
        spark: typing.Optional[typing.Union["QuicksightDataSourceParametersSpark", typing.Dict[builtins.str, typing.Any]]] = None,
        sql_server: typing.Optional[typing.Union["QuicksightDataSourceParametersSqlServer", typing.Dict[builtins.str, typing.Any]]] = None,
        teradata: typing.Optional[typing.Union["QuicksightDataSourceParametersTeradata", typing.Dict[builtins.str, typing.Any]]] = None,
        twitter: typing.Optional[typing.Union["QuicksightDataSourceParametersTwitter", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param amazon_elasticsearch: amazon_elasticsearch block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#amazon_elasticsearch QuicksightDataSource#amazon_elasticsearch}
        :param athena: athena block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#athena QuicksightDataSource#athena}
        :param aurora: aurora block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#aurora QuicksightDataSource#aurora}
        :param aurora_postgresql: aurora_postgresql block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#aurora_postgresql QuicksightDataSource#aurora_postgresql}
        :param aws_iot_analytics: aws_iot_analytics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#aws_iot_analytics QuicksightDataSource#aws_iot_analytics}
        :param jira: jira block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#jira QuicksightDataSource#jira}
        :param maria_db: maria_db block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#maria_db QuicksightDataSource#maria_db}
        :param mysql: mysql block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#mysql QuicksightDataSource#mysql}
        :param oracle: oracle block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#oracle QuicksightDataSource#oracle}
        :param postgresql: postgresql block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#postgresql QuicksightDataSource#postgresql}
        :param presto: presto block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#presto QuicksightDataSource#presto}
        :param rds: rds block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#rds QuicksightDataSource#rds}
        :param redshift: redshift block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#redshift QuicksightDataSource#redshift}
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#s3 QuicksightDataSource#s3}
        :param service_now: service_now block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#service_now QuicksightDataSource#service_now}
        :param snowflake: snowflake block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#snowflake QuicksightDataSource#snowflake}
        :param spark: spark block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#spark QuicksightDataSource#spark}
        :param sql_server: sql_server block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#sql_server QuicksightDataSource#sql_server}
        :param teradata: teradata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#teradata QuicksightDataSource#teradata}
        :param twitter: twitter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#twitter QuicksightDataSource#twitter}
        '''
        value = QuicksightDataSourceParameters(
            amazon_elasticsearch=amazon_elasticsearch,
            athena=athena,
            aurora=aurora,
            aurora_postgresql=aurora_postgresql,
            aws_iot_analytics=aws_iot_analytics,
            jira=jira,
            maria_db=maria_db,
            mysql=mysql,
            oracle=oracle,
            postgresql=postgresql,
            presto=presto,
            rds=rds,
            redshift=redshift,
            s3=s3,
            service_now=service_now,
            snowflake=snowflake,
            spark=spark,
            sql_server=sql_server,
            teradata=teradata,
            twitter=twitter,
        )

        return typing.cast(None, jsii.invoke(self, "putParameters", [value]))

    @jsii.member(jsii_name="putPermission")
    def put_permission(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["QuicksightDataSourcePermission", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7307edd673902d38b30b78d801b3aa97c64e8156cd37c4906d020e9e2d73789)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPermission", [value]))

    @jsii.member(jsii_name="putSslProperties")
    def put_ssl_properties(
        self,
        *,
        disable_ssl: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param disable_ssl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#disable_ssl QuicksightDataSource#disable_ssl}.
        '''
        value = QuicksightDataSourceSslProperties(disable_ssl=disable_ssl)

        return typing.cast(None, jsii.invoke(self, "putSslProperties", [value]))

    @jsii.member(jsii_name="putVpcConnectionProperties")
    def put_vpc_connection_properties(
        self,
        *,
        vpc_connection_arn: builtins.str,
    ) -> None:
        '''
        :param vpc_connection_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#vpc_connection_arn QuicksightDataSource#vpc_connection_arn}.
        '''
        value = QuicksightDataSourceVpcConnectionProperties(
            vpc_connection_arn=vpc_connection_arn
        )

        return typing.cast(None, jsii.invoke(self, "putVpcConnectionProperties", [value]))

    @jsii.member(jsii_name="resetAwsAccountId")
    def reset_aws_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsAccountId", []))

    @jsii.member(jsii_name="resetCredentials")
    def reset_credentials(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCredentials", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPermission")
    def reset_permission(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPermission", []))

    @jsii.member(jsii_name="resetSslProperties")
    def reset_ssl_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSslProperties", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetVpcConnectionProperties")
    def reset_vpc_connection_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpcConnectionProperties", []))

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
    @jsii.member(jsii_name="credentials")
    def credentials(self) -> "QuicksightDataSourceCredentialsOutputReference":
        return typing.cast("QuicksightDataSourceCredentialsOutputReference", jsii.get(self, "credentials"))

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> "QuicksightDataSourceParametersOutputReference":
        return typing.cast("QuicksightDataSourceParametersOutputReference", jsii.get(self, "parameters"))

    @builtins.property
    @jsii.member(jsii_name="permission")
    def permission(self) -> "QuicksightDataSourcePermissionList":
        return typing.cast("QuicksightDataSourcePermissionList", jsii.get(self, "permission"))

    @builtins.property
    @jsii.member(jsii_name="sslProperties")
    def ssl_properties(self) -> "QuicksightDataSourceSslPropertiesOutputReference":
        return typing.cast("QuicksightDataSourceSslPropertiesOutputReference", jsii.get(self, "sslProperties"))

    @builtins.property
    @jsii.member(jsii_name="vpcConnectionProperties")
    def vpc_connection_properties(
        self,
    ) -> "QuicksightDataSourceVpcConnectionPropertiesOutputReference":
        return typing.cast("QuicksightDataSourceVpcConnectionPropertiesOutputReference", jsii.get(self, "vpcConnectionProperties"))

    @builtins.property
    @jsii.member(jsii_name="awsAccountIdInput")
    def aws_account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "awsAccountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="credentialsInput")
    def credentials_input(self) -> typing.Optional["QuicksightDataSourceCredentials"]:
        return typing.cast(typing.Optional["QuicksightDataSourceCredentials"], jsii.get(self, "credentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="dataSourceIdInput")
    def data_source_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataSourceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="parametersInput")
    def parameters_input(self) -> typing.Optional["QuicksightDataSourceParameters"]:
        return typing.cast(typing.Optional["QuicksightDataSourceParameters"], jsii.get(self, "parametersInput"))

    @builtins.property
    @jsii.member(jsii_name="permissionInput")
    def permission_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["QuicksightDataSourcePermission"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["QuicksightDataSourcePermission"]]], jsii.get(self, "permissionInput"))

    @builtins.property
    @jsii.member(jsii_name="sslPropertiesInput")
    def ssl_properties_input(
        self,
    ) -> typing.Optional["QuicksightDataSourceSslProperties"]:
        return typing.cast(typing.Optional["QuicksightDataSourceSslProperties"], jsii.get(self, "sslPropertiesInput"))

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
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcConnectionPropertiesInput")
    def vpc_connection_properties_input(
        self,
    ) -> typing.Optional["QuicksightDataSourceVpcConnectionProperties"]:
        return typing.cast(typing.Optional["QuicksightDataSourceVpcConnectionProperties"], jsii.get(self, "vpcConnectionPropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="awsAccountId")
    def aws_account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "awsAccountId"))

    @aws_account_id.setter
    def aws_account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c14358f67eda0df9954ecc9a6267294487e7a749c27a049f03a08198cca15f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsAccountId", value)

    @builtins.property
    @jsii.member(jsii_name="dataSourceId")
    def data_source_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataSourceId"))

    @data_source_id.setter
    def data_source_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9db6bf0f3c5778c3c7df0d2d9dfb1c8728428f37369059b2c8f866820cd1e510)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataSourceId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5aa3eab1e9bb20ae0a21a5a6c9b8290ec10d623ce625c063b320f8fb9e6b4a2c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c645f2e41ec39d8cab0e5e1ade2e9adc86571579f9cb97478ef78c29762bc34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfbecee08b4c8730b868dda541b4f844a672c479d86f0ae6b2cf4e75ec7ed65c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__752935c282dfa553be31a6d84f2d3713bfdfdffa7a75d1926cf02658fbd90722)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df276f91c053b598c29105e41b4fab65e195571f48372348b10f7f4337be20dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)


@jsii.data_type(
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "data_source_id": "dataSourceId",
        "name": "name",
        "parameters": "parameters",
        "type": "type",
        "aws_account_id": "awsAccountId",
        "credentials": "credentials",
        "id": "id",
        "permission": "permission",
        "ssl_properties": "sslProperties",
        "tags": "tags",
        "tags_all": "tagsAll",
        "vpc_connection_properties": "vpcConnectionProperties",
    },
)
class QuicksightDataSourceConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        data_source_id: builtins.str,
        name: builtins.str,
        parameters: typing.Union["QuicksightDataSourceParameters", typing.Dict[builtins.str, typing.Any]],
        type: builtins.str,
        aws_account_id: typing.Optional[builtins.str] = None,
        credentials: typing.Optional[typing.Union["QuicksightDataSourceCredentials", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        permission: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["QuicksightDataSourcePermission", typing.Dict[builtins.str, typing.Any]]]]] = None,
        ssl_properties: typing.Optional[typing.Union["QuicksightDataSourceSslProperties", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        vpc_connection_properties: typing.Optional[typing.Union["QuicksightDataSourceVpcConnectionProperties", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param data_source_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#data_source_id QuicksightDataSource#data_source_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#name QuicksightDataSource#name}.
        :param parameters: parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#parameters QuicksightDataSource#parameters}
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#type QuicksightDataSource#type}.
        :param aws_account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#aws_account_id QuicksightDataSource#aws_account_id}.
        :param credentials: credentials block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#credentials QuicksightDataSource#credentials}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#id QuicksightDataSource#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param permission: permission block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#permission QuicksightDataSource#permission}
        :param ssl_properties: ssl_properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#ssl_properties QuicksightDataSource#ssl_properties}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#tags QuicksightDataSource#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#tags_all QuicksightDataSource#tags_all}.
        :param vpc_connection_properties: vpc_connection_properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#vpc_connection_properties QuicksightDataSource#vpc_connection_properties}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(parameters, dict):
            parameters = QuicksightDataSourceParameters(**parameters)
        if isinstance(credentials, dict):
            credentials = QuicksightDataSourceCredentials(**credentials)
        if isinstance(ssl_properties, dict):
            ssl_properties = QuicksightDataSourceSslProperties(**ssl_properties)
        if isinstance(vpc_connection_properties, dict):
            vpc_connection_properties = QuicksightDataSourceVpcConnectionProperties(**vpc_connection_properties)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a40668f6757d0e4e76b6b34c27e5f8701af0a89a869004f8b409fe443e9461c)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument data_source_id", value=data_source_id, expected_type=type_hints["data_source_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument aws_account_id", value=aws_account_id, expected_type=type_hints["aws_account_id"])
            check_type(argname="argument credentials", value=credentials, expected_type=type_hints["credentials"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument permission", value=permission, expected_type=type_hints["permission"])
            check_type(argname="argument ssl_properties", value=ssl_properties, expected_type=type_hints["ssl_properties"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument vpc_connection_properties", value=vpc_connection_properties, expected_type=type_hints["vpc_connection_properties"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "data_source_id": data_source_id,
            "name": name,
            "parameters": parameters,
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
        if aws_account_id is not None:
            self._values["aws_account_id"] = aws_account_id
        if credentials is not None:
            self._values["credentials"] = credentials
        if id is not None:
            self._values["id"] = id
        if permission is not None:
            self._values["permission"] = permission
        if ssl_properties is not None:
            self._values["ssl_properties"] = ssl_properties
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if vpc_connection_properties is not None:
            self._values["vpc_connection_properties"] = vpc_connection_properties

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
    def data_source_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#data_source_id QuicksightDataSource#data_source_id}.'''
        result = self._values.get("data_source_id")
        assert result is not None, "Required property 'data_source_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#name QuicksightDataSource#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameters(self) -> "QuicksightDataSourceParameters":
        '''parameters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#parameters QuicksightDataSource#parameters}
        '''
        result = self._values.get("parameters")
        assert result is not None, "Required property 'parameters' is missing"
        return typing.cast("QuicksightDataSourceParameters", result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#type QuicksightDataSource#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aws_account_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#aws_account_id QuicksightDataSource#aws_account_id}.'''
        result = self._values.get("aws_account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def credentials(self) -> typing.Optional["QuicksightDataSourceCredentials"]:
        '''credentials block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#credentials QuicksightDataSource#credentials}
        '''
        result = self._values.get("credentials")
        return typing.cast(typing.Optional["QuicksightDataSourceCredentials"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#id QuicksightDataSource#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def permission(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["QuicksightDataSourcePermission"]]]:
        '''permission block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#permission QuicksightDataSource#permission}
        '''
        result = self._values.get("permission")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["QuicksightDataSourcePermission"]]], result)

    @builtins.property
    def ssl_properties(self) -> typing.Optional["QuicksightDataSourceSslProperties"]:
        '''ssl_properties block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#ssl_properties QuicksightDataSource#ssl_properties}
        '''
        result = self._values.get("ssl_properties")
        return typing.cast(typing.Optional["QuicksightDataSourceSslProperties"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#tags QuicksightDataSource#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#tags_all QuicksightDataSource#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def vpc_connection_properties(
        self,
    ) -> typing.Optional["QuicksightDataSourceVpcConnectionProperties"]:
        '''vpc_connection_properties block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#vpc_connection_properties QuicksightDataSource#vpc_connection_properties}
        '''
        result = self._values.get("vpc_connection_properties")
        return typing.cast(typing.Optional["QuicksightDataSourceVpcConnectionProperties"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QuicksightDataSourceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceCredentials",
    jsii_struct_bases=[],
    name_mapping={
        "copy_source_arn": "copySourceArn",
        "credential_pair": "credentialPair",
    },
)
class QuicksightDataSourceCredentials:
    def __init__(
        self,
        *,
        copy_source_arn: typing.Optional[builtins.str] = None,
        credential_pair: typing.Optional[typing.Union["QuicksightDataSourceCredentialsCredentialPair", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param copy_source_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#copy_source_arn QuicksightDataSource#copy_source_arn}.
        :param credential_pair: credential_pair block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#credential_pair QuicksightDataSource#credential_pair}
        '''
        if isinstance(credential_pair, dict):
            credential_pair = QuicksightDataSourceCredentialsCredentialPair(**credential_pair)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5864b8f45e78d7d4bf5f4933fa63d6d1b3184a783d3b997e8d55a193441f57c3)
            check_type(argname="argument copy_source_arn", value=copy_source_arn, expected_type=type_hints["copy_source_arn"])
            check_type(argname="argument credential_pair", value=credential_pair, expected_type=type_hints["credential_pair"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if copy_source_arn is not None:
            self._values["copy_source_arn"] = copy_source_arn
        if credential_pair is not None:
            self._values["credential_pair"] = credential_pair

    @builtins.property
    def copy_source_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#copy_source_arn QuicksightDataSource#copy_source_arn}.'''
        result = self._values.get("copy_source_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def credential_pair(
        self,
    ) -> typing.Optional["QuicksightDataSourceCredentialsCredentialPair"]:
        '''credential_pair block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#credential_pair QuicksightDataSource#credential_pair}
        '''
        result = self._values.get("credential_pair")
        return typing.cast(typing.Optional["QuicksightDataSourceCredentialsCredentialPair"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QuicksightDataSourceCredentials(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceCredentialsCredentialPair",
    jsii_struct_bases=[],
    name_mapping={"password": "password", "username": "username"},
)
class QuicksightDataSourceCredentialsCredentialPair:
    def __init__(self, *, password: builtins.str, username: builtins.str) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#password QuicksightDataSource#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#username QuicksightDataSource#username}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e37f8582a190aa480fd8ddeac589f7ae4ed0030b172181f1234d1f240bc44792)
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "password": password,
            "username": username,
        }

    @builtins.property
    def password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#password QuicksightDataSource#password}.'''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#username QuicksightDataSource#username}.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QuicksightDataSourceCredentialsCredentialPair(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class QuicksightDataSourceCredentialsCredentialPairOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceCredentialsCredentialPairOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__887fb705aedbde41e9aa5d9e7ab7b1308b1ed62c7a1db7da4e56ac5b58b53267)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6cc1fb0b7a565b231ce8024dae61467515b6387b9708035a86d3071721eb4fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13a37559f894599c20b760862c249ca22218d853d8fffa3480443e2177facb34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[QuicksightDataSourceCredentialsCredentialPair]:
        return typing.cast(typing.Optional[QuicksightDataSourceCredentialsCredentialPair], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[QuicksightDataSourceCredentialsCredentialPair],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aaf33667223d4bad574b9401d00b5a4805bdca91ce6eba4a473cc0046d38af84)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class QuicksightDataSourceCredentialsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceCredentialsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__903f2a6bcd0985088fb8683510e4c39f0b9f96edf3fa86e7242f2c8402ac1068)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCredentialPair")
    def put_credential_pair(
        self,
        *,
        password: builtins.str,
        username: builtins.str,
    ) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#password QuicksightDataSource#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#username QuicksightDataSource#username}.
        '''
        value = QuicksightDataSourceCredentialsCredentialPair(
            password=password, username=username
        )

        return typing.cast(None, jsii.invoke(self, "putCredentialPair", [value]))

    @jsii.member(jsii_name="resetCopySourceArn")
    def reset_copy_source_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCopySourceArn", []))

    @jsii.member(jsii_name="resetCredentialPair")
    def reset_credential_pair(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCredentialPair", []))

    @builtins.property
    @jsii.member(jsii_name="credentialPair")
    def credential_pair(
        self,
    ) -> QuicksightDataSourceCredentialsCredentialPairOutputReference:
        return typing.cast(QuicksightDataSourceCredentialsCredentialPairOutputReference, jsii.get(self, "credentialPair"))

    @builtins.property
    @jsii.member(jsii_name="copySourceArnInput")
    def copy_source_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "copySourceArnInput"))

    @builtins.property
    @jsii.member(jsii_name="credentialPairInput")
    def credential_pair_input(
        self,
    ) -> typing.Optional[QuicksightDataSourceCredentialsCredentialPair]:
        return typing.cast(typing.Optional[QuicksightDataSourceCredentialsCredentialPair], jsii.get(self, "credentialPairInput"))

    @builtins.property
    @jsii.member(jsii_name="copySourceArn")
    def copy_source_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "copySourceArn"))

    @copy_source_arn.setter
    def copy_source_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e08a8d0b802c31dd6b812f1f6350ec1860fe1c29f9758742e71baf930738a69)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "copySourceArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[QuicksightDataSourceCredentials]:
        return typing.cast(typing.Optional[QuicksightDataSourceCredentials], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[QuicksightDataSourceCredentials],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__174161bfed92558d4765b1bc7fb581c508db2ed8ad12048ef49724f6172a2a95)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceParameters",
    jsii_struct_bases=[],
    name_mapping={
        "amazon_elasticsearch": "amazonElasticsearch",
        "athena": "athena",
        "aurora": "aurora",
        "aurora_postgresql": "auroraPostgresql",
        "aws_iot_analytics": "awsIotAnalytics",
        "jira": "jira",
        "maria_db": "mariaDb",
        "mysql": "mysql",
        "oracle": "oracle",
        "postgresql": "postgresql",
        "presto": "presto",
        "rds": "rds",
        "redshift": "redshift",
        "s3": "s3",
        "service_now": "serviceNow",
        "snowflake": "snowflake",
        "spark": "spark",
        "sql_server": "sqlServer",
        "teradata": "teradata",
        "twitter": "twitter",
    },
)
class QuicksightDataSourceParameters:
    def __init__(
        self,
        *,
        amazon_elasticsearch: typing.Optional[typing.Union["QuicksightDataSourceParametersAmazonElasticsearch", typing.Dict[builtins.str, typing.Any]]] = None,
        athena: typing.Optional[typing.Union["QuicksightDataSourceParametersAthena", typing.Dict[builtins.str, typing.Any]]] = None,
        aurora: typing.Optional[typing.Union["QuicksightDataSourceParametersAurora", typing.Dict[builtins.str, typing.Any]]] = None,
        aurora_postgresql: typing.Optional[typing.Union["QuicksightDataSourceParametersAuroraPostgresql", typing.Dict[builtins.str, typing.Any]]] = None,
        aws_iot_analytics: typing.Optional[typing.Union["QuicksightDataSourceParametersAwsIotAnalytics", typing.Dict[builtins.str, typing.Any]]] = None,
        jira: typing.Optional[typing.Union["QuicksightDataSourceParametersJira", typing.Dict[builtins.str, typing.Any]]] = None,
        maria_db: typing.Optional[typing.Union["QuicksightDataSourceParametersMariaDb", typing.Dict[builtins.str, typing.Any]]] = None,
        mysql: typing.Optional[typing.Union["QuicksightDataSourceParametersMysql", typing.Dict[builtins.str, typing.Any]]] = None,
        oracle: typing.Optional[typing.Union["QuicksightDataSourceParametersOracle", typing.Dict[builtins.str, typing.Any]]] = None,
        postgresql: typing.Optional[typing.Union["QuicksightDataSourceParametersPostgresql", typing.Dict[builtins.str, typing.Any]]] = None,
        presto: typing.Optional[typing.Union["QuicksightDataSourceParametersPresto", typing.Dict[builtins.str, typing.Any]]] = None,
        rds: typing.Optional[typing.Union["QuicksightDataSourceParametersRds", typing.Dict[builtins.str, typing.Any]]] = None,
        redshift: typing.Optional[typing.Union["QuicksightDataSourceParametersRedshift", typing.Dict[builtins.str, typing.Any]]] = None,
        s3: typing.Optional[typing.Union["QuicksightDataSourceParametersS3", typing.Dict[builtins.str, typing.Any]]] = None,
        service_now: typing.Optional[typing.Union["QuicksightDataSourceParametersServiceNow", typing.Dict[builtins.str, typing.Any]]] = None,
        snowflake: typing.Optional[typing.Union["QuicksightDataSourceParametersSnowflake", typing.Dict[builtins.str, typing.Any]]] = None,
        spark: typing.Optional[typing.Union["QuicksightDataSourceParametersSpark", typing.Dict[builtins.str, typing.Any]]] = None,
        sql_server: typing.Optional[typing.Union["QuicksightDataSourceParametersSqlServer", typing.Dict[builtins.str, typing.Any]]] = None,
        teradata: typing.Optional[typing.Union["QuicksightDataSourceParametersTeradata", typing.Dict[builtins.str, typing.Any]]] = None,
        twitter: typing.Optional[typing.Union["QuicksightDataSourceParametersTwitter", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param amazon_elasticsearch: amazon_elasticsearch block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#amazon_elasticsearch QuicksightDataSource#amazon_elasticsearch}
        :param athena: athena block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#athena QuicksightDataSource#athena}
        :param aurora: aurora block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#aurora QuicksightDataSource#aurora}
        :param aurora_postgresql: aurora_postgresql block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#aurora_postgresql QuicksightDataSource#aurora_postgresql}
        :param aws_iot_analytics: aws_iot_analytics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#aws_iot_analytics QuicksightDataSource#aws_iot_analytics}
        :param jira: jira block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#jira QuicksightDataSource#jira}
        :param maria_db: maria_db block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#maria_db QuicksightDataSource#maria_db}
        :param mysql: mysql block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#mysql QuicksightDataSource#mysql}
        :param oracle: oracle block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#oracle QuicksightDataSource#oracle}
        :param postgresql: postgresql block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#postgresql QuicksightDataSource#postgresql}
        :param presto: presto block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#presto QuicksightDataSource#presto}
        :param rds: rds block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#rds QuicksightDataSource#rds}
        :param redshift: redshift block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#redshift QuicksightDataSource#redshift}
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#s3 QuicksightDataSource#s3}
        :param service_now: service_now block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#service_now QuicksightDataSource#service_now}
        :param snowflake: snowflake block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#snowflake QuicksightDataSource#snowflake}
        :param spark: spark block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#spark QuicksightDataSource#spark}
        :param sql_server: sql_server block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#sql_server QuicksightDataSource#sql_server}
        :param teradata: teradata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#teradata QuicksightDataSource#teradata}
        :param twitter: twitter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#twitter QuicksightDataSource#twitter}
        '''
        if isinstance(amazon_elasticsearch, dict):
            amazon_elasticsearch = QuicksightDataSourceParametersAmazonElasticsearch(**amazon_elasticsearch)
        if isinstance(athena, dict):
            athena = QuicksightDataSourceParametersAthena(**athena)
        if isinstance(aurora, dict):
            aurora = QuicksightDataSourceParametersAurora(**aurora)
        if isinstance(aurora_postgresql, dict):
            aurora_postgresql = QuicksightDataSourceParametersAuroraPostgresql(**aurora_postgresql)
        if isinstance(aws_iot_analytics, dict):
            aws_iot_analytics = QuicksightDataSourceParametersAwsIotAnalytics(**aws_iot_analytics)
        if isinstance(jira, dict):
            jira = QuicksightDataSourceParametersJira(**jira)
        if isinstance(maria_db, dict):
            maria_db = QuicksightDataSourceParametersMariaDb(**maria_db)
        if isinstance(mysql, dict):
            mysql = QuicksightDataSourceParametersMysql(**mysql)
        if isinstance(oracle, dict):
            oracle = QuicksightDataSourceParametersOracle(**oracle)
        if isinstance(postgresql, dict):
            postgresql = QuicksightDataSourceParametersPostgresql(**postgresql)
        if isinstance(presto, dict):
            presto = QuicksightDataSourceParametersPresto(**presto)
        if isinstance(rds, dict):
            rds = QuicksightDataSourceParametersRds(**rds)
        if isinstance(redshift, dict):
            redshift = QuicksightDataSourceParametersRedshift(**redshift)
        if isinstance(s3, dict):
            s3 = QuicksightDataSourceParametersS3(**s3)
        if isinstance(service_now, dict):
            service_now = QuicksightDataSourceParametersServiceNow(**service_now)
        if isinstance(snowflake, dict):
            snowflake = QuicksightDataSourceParametersSnowflake(**snowflake)
        if isinstance(spark, dict):
            spark = QuicksightDataSourceParametersSpark(**spark)
        if isinstance(sql_server, dict):
            sql_server = QuicksightDataSourceParametersSqlServer(**sql_server)
        if isinstance(teradata, dict):
            teradata = QuicksightDataSourceParametersTeradata(**teradata)
        if isinstance(twitter, dict):
            twitter = QuicksightDataSourceParametersTwitter(**twitter)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__925ab8f8230fb66c0e16b8767004032b2a21abdf01754cf6a98c55af5b0b49cc)
            check_type(argname="argument amazon_elasticsearch", value=amazon_elasticsearch, expected_type=type_hints["amazon_elasticsearch"])
            check_type(argname="argument athena", value=athena, expected_type=type_hints["athena"])
            check_type(argname="argument aurora", value=aurora, expected_type=type_hints["aurora"])
            check_type(argname="argument aurora_postgresql", value=aurora_postgresql, expected_type=type_hints["aurora_postgresql"])
            check_type(argname="argument aws_iot_analytics", value=aws_iot_analytics, expected_type=type_hints["aws_iot_analytics"])
            check_type(argname="argument jira", value=jira, expected_type=type_hints["jira"])
            check_type(argname="argument maria_db", value=maria_db, expected_type=type_hints["maria_db"])
            check_type(argname="argument mysql", value=mysql, expected_type=type_hints["mysql"])
            check_type(argname="argument oracle", value=oracle, expected_type=type_hints["oracle"])
            check_type(argname="argument postgresql", value=postgresql, expected_type=type_hints["postgresql"])
            check_type(argname="argument presto", value=presto, expected_type=type_hints["presto"])
            check_type(argname="argument rds", value=rds, expected_type=type_hints["rds"])
            check_type(argname="argument redshift", value=redshift, expected_type=type_hints["redshift"])
            check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
            check_type(argname="argument service_now", value=service_now, expected_type=type_hints["service_now"])
            check_type(argname="argument snowflake", value=snowflake, expected_type=type_hints["snowflake"])
            check_type(argname="argument spark", value=spark, expected_type=type_hints["spark"])
            check_type(argname="argument sql_server", value=sql_server, expected_type=type_hints["sql_server"])
            check_type(argname="argument teradata", value=teradata, expected_type=type_hints["teradata"])
            check_type(argname="argument twitter", value=twitter, expected_type=type_hints["twitter"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if amazon_elasticsearch is not None:
            self._values["amazon_elasticsearch"] = amazon_elasticsearch
        if athena is not None:
            self._values["athena"] = athena
        if aurora is not None:
            self._values["aurora"] = aurora
        if aurora_postgresql is not None:
            self._values["aurora_postgresql"] = aurora_postgresql
        if aws_iot_analytics is not None:
            self._values["aws_iot_analytics"] = aws_iot_analytics
        if jira is not None:
            self._values["jira"] = jira
        if maria_db is not None:
            self._values["maria_db"] = maria_db
        if mysql is not None:
            self._values["mysql"] = mysql
        if oracle is not None:
            self._values["oracle"] = oracle
        if postgresql is not None:
            self._values["postgresql"] = postgresql
        if presto is not None:
            self._values["presto"] = presto
        if rds is not None:
            self._values["rds"] = rds
        if redshift is not None:
            self._values["redshift"] = redshift
        if s3 is not None:
            self._values["s3"] = s3
        if service_now is not None:
            self._values["service_now"] = service_now
        if snowflake is not None:
            self._values["snowflake"] = snowflake
        if spark is not None:
            self._values["spark"] = spark
        if sql_server is not None:
            self._values["sql_server"] = sql_server
        if teradata is not None:
            self._values["teradata"] = teradata
        if twitter is not None:
            self._values["twitter"] = twitter

    @builtins.property
    def amazon_elasticsearch(
        self,
    ) -> typing.Optional["QuicksightDataSourceParametersAmazonElasticsearch"]:
        '''amazon_elasticsearch block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#amazon_elasticsearch QuicksightDataSource#amazon_elasticsearch}
        '''
        result = self._values.get("amazon_elasticsearch")
        return typing.cast(typing.Optional["QuicksightDataSourceParametersAmazonElasticsearch"], result)

    @builtins.property
    def athena(self) -> typing.Optional["QuicksightDataSourceParametersAthena"]:
        '''athena block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#athena QuicksightDataSource#athena}
        '''
        result = self._values.get("athena")
        return typing.cast(typing.Optional["QuicksightDataSourceParametersAthena"], result)

    @builtins.property
    def aurora(self) -> typing.Optional["QuicksightDataSourceParametersAurora"]:
        '''aurora block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#aurora QuicksightDataSource#aurora}
        '''
        result = self._values.get("aurora")
        return typing.cast(typing.Optional["QuicksightDataSourceParametersAurora"], result)

    @builtins.property
    def aurora_postgresql(
        self,
    ) -> typing.Optional["QuicksightDataSourceParametersAuroraPostgresql"]:
        '''aurora_postgresql block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#aurora_postgresql QuicksightDataSource#aurora_postgresql}
        '''
        result = self._values.get("aurora_postgresql")
        return typing.cast(typing.Optional["QuicksightDataSourceParametersAuroraPostgresql"], result)

    @builtins.property
    def aws_iot_analytics(
        self,
    ) -> typing.Optional["QuicksightDataSourceParametersAwsIotAnalytics"]:
        '''aws_iot_analytics block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#aws_iot_analytics QuicksightDataSource#aws_iot_analytics}
        '''
        result = self._values.get("aws_iot_analytics")
        return typing.cast(typing.Optional["QuicksightDataSourceParametersAwsIotAnalytics"], result)

    @builtins.property
    def jira(self) -> typing.Optional["QuicksightDataSourceParametersJira"]:
        '''jira block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#jira QuicksightDataSource#jira}
        '''
        result = self._values.get("jira")
        return typing.cast(typing.Optional["QuicksightDataSourceParametersJira"], result)

    @builtins.property
    def maria_db(self) -> typing.Optional["QuicksightDataSourceParametersMariaDb"]:
        '''maria_db block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#maria_db QuicksightDataSource#maria_db}
        '''
        result = self._values.get("maria_db")
        return typing.cast(typing.Optional["QuicksightDataSourceParametersMariaDb"], result)

    @builtins.property
    def mysql(self) -> typing.Optional["QuicksightDataSourceParametersMysql"]:
        '''mysql block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#mysql QuicksightDataSource#mysql}
        '''
        result = self._values.get("mysql")
        return typing.cast(typing.Optional["QuicksightDataSourceParametersMysql"], result)

    @builtins.property
    def oracle(self) -> typing.Optional["QuicksightDataSourceParametersOracle"]:
        '''oracle block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#oracle QuicksightDataSource#oracle}
        '''
        result = self._values.get("oracle")
        return typing.cast(typing.Optional["QuicksightDataSourceParametersOracle"], result)

    @builtins.property
    def postgresql(self) -> typing.Optional["QuicksightDataSourceParametersPostgresql"]:
        '''postgresql block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#postgresql QuicksightDataSource#postgresql}
        '''
        result = self._values.get("postgresql")
        return typing.cast(typing.Optional["QuicksightDataSourceParametersPostgresql"], result)

    @builtins.property
    def presto(self) -> typing.Optional["QuicksightDataSourceParametersPresto"]:
        '''presto block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#presto QuicksightDataSource#presto}
        '''
        result = self._values.get("presto")
        return typing.cast(typing.Optional["QuicksightDataSourceParametersPresto"], result)

    @builtins.property
    def rds(self) -> typing.Optional["QuicksightDataSourceParametersRds"]:
        '''rds block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#rds QuicksightDataSource#rds}
        '''
        result = self._values.get("rds")
        return typing.cast(typing.Optional["QuicksightDataSourceParametersRds"], result)

    @builtins.property
    def redshift(self) -> typing.Optional["QuicksightDataSourceParametersRedshift"]:
        '''redshift block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#redshift QuicksightDataSource#redshift}
        '''
        result = self._values.get("redshift")
        return typing.cast(typing.Optional["QuicksightDataSourceParametersRedshift"], result)

    @builtins.property
    def s3(self) -> typing.Optional["QuicksightDataSourceParametersS3"]:
        '''s3 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#s3 QuicksightDataSource#s3}
        '''
        result = self._values.get("s3")
        return typing.cast(typing.Optional["QuicksightDataSourceParametersS3"], result)

    @builtins.property
    def service_now(
        self,
    ) -> typing.Optional["QuicksightDataSourceParametersServiceNow"]:
        '''service_now block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#service_now QuicksightDataSource#service_now}
        '''
        result = self._values.get("service_now")
        return typing.cast(typing.Optional["QuicksightDataSourceParametersServiceNow"], result)

    @builtins.property
    def snowflake(self) -> typing.Optional["QuicksightDataSourceParametersSnowflake"]:
        '''snowflake block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#snowflake QuicksightDataSource#snowflake}
        '''
        result = self._values.get("snowflake")
        return typing.cast(typing.Optional["QuicksightDataSourceParametersSnowflake"], result)

    @builtins.property
    def spark(self) -> typing.Optional["QuicksightDataSourceParametersSpark"]:
        '''spark block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#spark QuicksightDataSource#spark}
        '''
        result = self._values.get("spark")
        return typing.cast(typing.Optional["QuicksightDataSourceParametersSpark"], result)

    @builtins.property
    def sql_server(self) -> typing.Optional["QuicksightDataSourceParametersSqlServer"]:
        '''sql_server block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#sql_server QuicksightDataSource#sql_server}
        '''
        result = self._values.get("sql_server")
        return typing.cast(typing.Optional["QuicksightDataSourceParametersSqlServer"], result)

    @builtins.property
    def teradata(self) -> typing.Optional["QuicksightDataSourceParametersTeradata"]:
        '''teradata block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#teradata QuicksightDataSource#teradata}
        '''
        result = self._values.get("teradata")
        return typing.cast(typing.Optional["QuicksightDataSourceParametersTeradata"], result)

    @builtins.property
    def twitter(self) -> typing.Optional["QuicksightDataSourceParametersTwitter"]:
        '''twitter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#twitter QuicksightDataSource#twitter}
        '''
        result = self._values.get("twitter")
        return typing.cast(typing.Optional["QuicksightDataSourceParametersTwitter"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QuicksightDataSourceParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceParametersAmazonElasticsearch",
    jsii_struct_bases=[],
    name_mapping={"domain": "domain"},
)
class QuicksightDataSourceParametersAmazonElasticsearch:
    def __init__(self, *, domain: builtins.str) -> None:
        '''
        :param domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#domain QuicksightDataSource#domain}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e2517cc485bcb7581b51f080f4133f80f336b16c02f7453ec6b7af8e3c29ec3)
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain": domain,
        }

    @builtins.property
    def domain(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#domain QuicksightDataSource#domain}.'''
        result = self._values.get("domain")
        assert result is not None, "Required property 'domain' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QuicksightDataSourceParametersAmazonElasticsearch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class QuicksightDataSourceParametersAmazonElasticsearchOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceParametersAmazonElasticsearchOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6bc8e387c101c39804061d7816a8973c2008aaa41b10e020d5aebe236a403ed7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="domainInput")
    def domain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainInput"))

    @builtins.property
    @jsii.member(jsii_name="domain")
    def domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domain"))

    @domain.setter
    def domain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51c5c08acbd64d8053b10ea67851ae1ee2451af593e8730d540ed09adb1d58f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domain", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[QuicksightDataSourceParametersAmazonElasticsearch]:
        return typing.cast(typing.Optional[QuicksightDataSourceParametersAmazonElasticsearch], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[QuicksightDataSourceParametersAmazonElasticsearch],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6035852fd4c8c2213640fae1261be2a47358b3e17d18d48f57e123025a2bed64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceParametersAthena",
    jsii_struct_bases=[],
    name_mapping={"work_group": "workGroup"},
)
class QuicksightDataSourceParametersAthena:
    def __init__(self, *, work_group: typing.Optional[builtins.str] = None) -> None:
        '''
        :param work_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#work_group QuicksightDataSource#work_group}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe93641b80b55ddd24b379306f3a2d6211ef46d5a23a136226953824d0843bd8)
            check_type(argname="argument work_group", value=work_group, expected_type=type_hints["work_group"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if work_group is not None:
            self._values["work_group"] = work_group

    @builtins.property
    def work_group(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#work_group QuicksightDataSource#work_group}.'''
        result = self._values.get("work_group")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QuicksightDataSourceParametersAthena(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class QuicksightDataSourceParametersAthenaOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceParametersAthenaOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6e7a1ef3f1984f55407c09fadecb0acef4482912c70dbc38f9cefc897e27f21a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetWorkGroup")
    def reset_work_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkGroup", []))

    @builtins.property
    @jsii.member(jsii_name="workGroupInput")
    def work_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="workGroup")
    def work_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "workGroup"))

    @work_group.setter
    def work_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__489319fe507cc2a84f57c89cb9941d0ce363302863130008262d621b9917aa65)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workGroup", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[QuicksightDataSourceParametersAthena]:
        return typing.cast(typing.Optional[QuicksightDataSourceParametersAthena], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[QuicksightDataSourceParametersAthena],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d0de4ff52f58cd9a4cbed490377ce0d171f0d0f4d7873647d97e07da13df5bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceParametersAurora",
    jsii_struct_bases=[],
    name_mapping={"database": "database", "host": "host", "port": "port"},
)
class QuicksightDataSourceParametersAurora:
    def __init__(
        self,
        *,
        database: builtins.str,
        host: builtins.str,
        port: jsii.Number,
    ) -> None:
        '''
        :param database: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#database QuicksightDataSource#database}.
        :param host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#host QuicksightDataSource#host}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#port QuicksightDataSource#port}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c82b4771e4ffacf3c65fb4a8822d55d1361706ed3f6d9f1a62c9804ed8324772)
            check_type(argname="argument database", value=database, expected_type=type_hints["database"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "database": database,
            "host": host,
            "port": port,
        }

    @builtins.property
    def database(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#database QuicksightDataSource#database}.'''
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def host(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#host QuicksightDataSource#host}.'''
        result = self._values.get("host")
        assert result is not None, "Required property 'host' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#port QuicksightDataSource#port}.'''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QuicksightDataSourceParametersAurora(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class QuicksightDataSourceParametersAuroraOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceParametersAuroraOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__16f1a4226b4425f75a0713df99c17555cdcd7beeebc683d881fc97ab45a4e57a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="databaseInput")
    def database_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseInput"))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="database")
    def database(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "database"))

    @database.setter
    def database(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81fb029c5d53bb89ed9fec95f2bfeb82b04cf5b6904b97fe70e43842efd2c443)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "database", value)

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @host.setter
    def host(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c56e3cd3186c632f6b23d3cc2b4ea14614aacd92e40a484747731222db6ee77)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32801290b83f8c40215d4c2d0f2e79c9c841df92c9e217885f4c6821603c5392)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[QuicksightDataSourceParametersAurora]:
        return typing.cast(typing.Optional[QuicksightDataSourceParametersAurora], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[QuicksightDataSourceParametersAurora],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57fe3fc4a62fbff9e04cbc2db9f341b6afd2073bc0744cc965cade31b5e00557)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceParametersAuroraPostgresql",
    jsii_struct_bases=[],
    name_mapping={"database": "database", "host": "host", "port": "port"},
)
class QuicksightDataSourceParametersAuroraPostgresql:
    def __init__(
        self,
        *,
        database: builtins.str,
        host: builtins.str,
        port: jsii.Number,
    ) -> None:
        '''
        :param database: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#database QuicksightDataSource#database}.
        :param host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#host QuicksightDataSource#host}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#port QuicksightDataSource#port}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__936d6fadf7702fae63ecefaab868dd1451c0ef61f9152f66e024dce1ffabeb8c)
            check_type(argname="argument database", value=database, expected_type=type_hints["database"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "database": database,
            "host": host,
            "port": port,
        }

    @builtins.property
    def database(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#database QuicksightDataSource#database}.'''
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def host(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#host QuicksightDataSource#host}.'''
        result = self._values.get("host")
        assert result is not None, "Required property 'host' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#port QuicksightDataSource#port}.'''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QuicksightDataSourceParametersAuroraPostgresql(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class QuicksightDataSourceParametersAuroraPostgresqlOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceParametersAuroraPostgresqlOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6e4fa259c0da42ec1731d3538c89df88cbd6342009e6dfb79441739ddf0ac862)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="databaseInput")
    def database_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseInput"))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="database")
    def database(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "database"))

    @database.setter
    def database(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30136dc3b3a16287ef52092de8df04ae232b6799b0872180f04e4a4612d5b474)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "database", value)

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @host.setter
    def host(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__054862547266c7a4f7248c51c22464fc57aab388222b8017ad2c6eb5e7c9f465)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e452798bd35b9859b9e1d9a280a545af4a4d739e9bc1d7d21becf57930a6ee74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[QuicksightDataSourceParametersAuroraPostgresql]:
        return typing.cast(typing.Optional[QuicksightDataSourceParametersAuroraPostgresql], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[QuicksightDataSourceParametersAuroraPostgresql],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97f5d53dc69fe692e5277c9914c15ca27fb27dbaf31c7b26f19d434e551f125d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceParametersAwsIotAnalytics",
    jsii_struct_bases=[],
    name_mapping={"data_set_name": "dataSetName"},
)
class QuicksightDataSourceParametersAwsIotAnalytics:
    def __init__(self, *, data_set_name: builtins.str) -> None:
        '''
        :param data_set_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#data_set_name QuicksightDataSource#data_set_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da635401732a08064ae10f0da7d46861a69092dce05117387aa0545a653e4c38)
            check_type(argname="argument data_set_name", value=data_set_name, expected_type=type_hints["data_set_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "data_set_name": data_set_name,
        }

    @builtins.property
    def data_set_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#data_set_name QuicksightDataSource#data_set_name}.'''
        result = self._values.get("data_set_name")
        assert result is not None, "Required property 'data_set_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QuicksightDataSourceParametersAwsIotAnalytics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class QuicksightDataSourceParametersAwsIotAnalyticsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceParametersAwsIotAnalyticsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__400e34548984e41132d374a3abcf0513def0dce56518fe17565519565f9734fe)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="dataSetNameInput")
    def data_set_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataSetNameInput"))

    @builtins.property
    @jsii.member(jsii_name="dataSetName")
    def data_set_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataSetName"))

    @data_set_name.setter
    def data_set_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae76ff275070d0a51ca7954323877ee252e54cf677d1328693b55d58c641b9a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataSetName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[QuicksightDataSourceParametersAwsIotAnalytics]:
        return typing.cast(typing.Optional[QuicksightDataSourceParametersAwsIotAnalytics], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[QuicksightDataSourceParametersAwsIotAnalytics],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8ef553d3f942244ba224d37a5d129d654ba1118cb4fac01b54798d623008fe8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceParametersJira",
    jsii_struct_bases=[],
    name_mapping={"site_base_url": "siteBaseUrl"},
)
class QuicksightDataSourceParametersJira:
    def __init__(self, *, site_base_url: builtins.str) -> None:
        '''
        :param site_base_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#site_base_url QuicksightDataSource#site_base_url}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f5d8044730d4247663475164d616ab0e9ec98ab2105ae34620c7f4ea7e0b764)
            check_type(argname="argument site_base_url", value=site_base_url, expected_type=type_hints["site_base_url"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "site_base_url": site_base_url,
        }

    @builtins.property
    def site_base_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#site_base_url QuicksightDataSource#site_base_url}.'''
        result = self._values.get("site_base_url")
        assert result is not None, "Required property 'site_base_url' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QuicksightDataSourceParametersJira(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class QuicksightDataSourceParametersJiraOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceParametersJiraOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3b513ac64aa35e62588e347e14b4b9c5440b9e112e786ed7d39454eb733801de)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="siteBaseUrlInput")
    def site_base_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "siteBaseUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="siteBaseUrl")
    def site_base_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "siteBaseUrl"))

    @site_base_url.setter
    def site_base_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__513ba5a520c5dd7f099e1cd1ede6edade11df83872f5b55692098b86f305efb2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "siteBaseUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[QuicksightDataSourceParametersJira]:
        return typing.cast(typing.Optional[QuicksightDataSourceParametersJira], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[QuicksightDataSourceParametersJira],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25a389b2c5b1c092f7a743debb30f6bf1abfb686061aaec3b4a9016f1503f81e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceParametersMariaDb",
    jsii_struct_bases=[],
    name_mapping={"database": "database", "host": "host", "port": "port"},
)
class QuicksightDataSourceParametersMariaDb:
    def __init__(
        self,
        *,
        database: builtins.str,
        host: builtins.str,
        port: jsii.Number,
    ) -> None:
        '''
        :param database: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#database QuicksightDataSource#database}.
        :param host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#host QuicksightDataSource#host}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#port QuicksightDataSource#port}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25f6a25c8d26db8cccc6d0a0a7750426cc302bbc0e70706dce736f0d5fcddaa1)
            check_type(argname="argument database", value=database, expected_type=type_hints["database"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "database": database,
            "host": host,
            "port": port,
        }

    @builtins.property
    def database(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#database QuicksightDataSource#database}.'''
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def host(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#host QuicksightDataSource#host}.'''
        result = self._values.get("host")
        assert result is not None, "Required property 'host' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#port QuicksightDataSource#port}.'''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QuicksightDataSourceParametersMariaDb(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class QuicksightDataSourceParametersMariaDbOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceParametersMariaDbOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ec519a22efdeb7c05cfc1f83d211568dfb2d59957580065b17581e2b0d62e55f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="databaseInput")
    def database_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseInput"))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="database")
    def database(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "database"))

    @database.setter
    def database(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4335b39d4495a3ea74e563db9d4fb26a1ccc759e975814fbd7ffac2ac52209fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "database", value)

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @host.setter
    def host(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf1ed3c0bb1731424b7068372653e9025319546580645f0b8e1a17e6a2526b74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afed2ef271d785b445b9f0fa5ea9b311dc92e63c216ef4ef32e5d946b27107a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[QuicksightDataSourceParametersMariaDb]:
        return typing.cast(typing.Optional[QuicksightDataSourceParametersMariaDb], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[QuicksightDataSourceParametersMariaDb],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3cd9510c1454bcd907a3485202518ca90617aa157be47cb6230e2dae5dffea86)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceParametersMysql",
    jsii_struct_bases=[],
    name_mapping={"database": "database", "host": "host", "port": "port"},
)
class QuicksightDataSourceParametersMysql:
    def __init__(
        self,
        *,
        database: builtins.str,
        host: builtins.str,
        port: jsii.Number,
    ) -> None:
        '''
        :param database: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#database QuicksightDataSource#database}.
        :param host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#host QuicksightDataSource#host}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#port QuicksightDataSource#port}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e06d73b9bdd3a865d2d2afddf174794e2601d2822b89766a394d72961015c662)
            check_type(argname="argument database", value=database, expected_type=type_hints["database"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "database": database,
            "host": host,
            "port": port,
        }

    @builtins.property
    def database(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#database QuicksightDataSource#database}.'''
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def host(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#host QuicksightDataSource#host}.'''
        result = self._values.get("host")
        assert result is not None, "Required property 'host' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#port QuicksightDataSource#port}.'''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QuicksightDataSourceParametersMysql(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class QuicksightDataSourceParametersMysqlOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceParametersMysqlOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__23f76f46eea15628e721a81df1406e8cebc4f357fa47bedda4c7e4b6c5df20cf)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="databaseInput")
    def database_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseInput"))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="database")
    def database(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "database"))

    @database.setter
    def database(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e34a64b436f0fb6fb1acb078364814d208253346b487ff2ee3f9d1f2e4348f0e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "database", value)

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @host.setter
    def host(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f175e13e7616fff1d001d75ebe556b64de8df12763019188cea25b1f15f8b6f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9c6176639e17bf86dd08b1dc1032f3e30f050bbe830660a8e4848cec780bfb6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[QuicksightDataSourceParametersMysql]:
        return typing.cast(typing.Optional[QuicksightDataSourceParametersMysql], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[QuicksightDataSourceParametersMysql],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce5e4ca2fa02cc9511aa3ddb758b7af6332e622c977dc6d334b90c8200797224)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceParametersOracle",
    jsii_struct_bases=[],
    name_mapping={"database": "database", "host": "host", "port": "port"},
)
class QuicksightDataSourceParametersOracle:
    def __init__(
        self,
        *,
        database: builtins.str,
        host: builtins.str,
        port: jsii.Number,
    ) -> None:
        '''
        :param database: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#database QuicksightDataSource#database}.
        :param host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#host QuicksightDataSource#host}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#port QuicksightDataSource#port}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__289a267a77d1484a96704835efb3fde5fc64638095d0428c8d2e1fd4e384ecfd)
            check_type(argname="argument database", value=database, expected_type=type_hints["database"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "database": database,
            "host": host,
            "port": port,
        }

    @builtins.property
    def database(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#database QuicksightDataSource#database}.'''
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def host(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#host QuicksightDataSource#host}.'''
        result = self._values.get("host")
        assert result is not None, "Required property 'host' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#port QuicksightDataSource#port}.'''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QuicksightDataSourceParametersOracle(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class QuicksightDataSourceParametersOracleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceParametersOracleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a1e0d5f370b3836884ca2bdfe705402e9d420086ffc6660a4e6a3092f7e13458)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="databaseInput")
    def database_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseInput"))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="database")
    def database(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "database"))

    @database.setter
    def database(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d276032e00ce65679ad022ef71fef2f4659ac89940b615f0829ab989c512943)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "database", value)

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @host.setter
    def host(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9635ba4743c38c7928cb612a0b3f21c624c975101712e588fb1822a76c78c09e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c220bee505e3027846f3491ab891db33a725c4c337d06cae5f3c642d673b9234)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[QuicksightDataSourceParametersOracle]:
        return typing.cast(typing.Optional[QuicksightDataSourceParametersOracle], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[QuicksightDataSourceParametersOracle],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04ebe71fe160012cb664edc9581c928eb7587d20b16a745f45817a90f1f339ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class QuicksightDataSourceParametersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceParametersOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d256e91e25c85f7677c1ee49c7dc1d187d2a3e9029b65a3f7b20b9dbe23b885a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAmazonElasticsearch")
    def put_amazon_elasticsearch(self, *, domain: builtins.str) -> None:
        '''
        :param domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#domain QuicksightDataSource#domain}.
        '''
        value = QuicksightDataSourceParametersAmazonElasticsearch(domain=domain)

        return typing.cast(None, jsii.invoke(self, "putAmazonElasticsearch", [value]))

    @jsii.member(jsii_name="putAthena")
    def put_athena(self, *, work_group: typing.Optional[builtins.str] = None) -> None:
        '''
        :param work_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#work_group QuicksightDataSource#work_group}.
        '''
        value = QuicksightDataSourceParametersAthena(work_group=work_group)

        return typing.cast(None, jsii.invoke(self, "putAthena", [value]))

    @jsii.member(jsii_name="putAurora")
    def put_aurora(
        self,
        *,
        database: builtins.str,
        host: builtins.str,
        port: jsii.Number,
    ) -> None:
        '''
        :param database: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#database QuicksightDataSource#database}.
        :param host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#host QuicksightDataSource#host}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#port QuicksightDataSource#port}.
        '''
        value = QuicksightDataSourceParametersAurora(
            database=database, host=host, port=port
        )

        return typing.cast(None, jsii.invoke(self, "putAurora", [value]))

    @jsii.member(jsii_name="putAuroraPostgresql")
    def put_aurora_postgresql(
        self,
        *,
        database: builtins.str,
        host: builtins.str,
        port: jsii.Number,
    ) -> None:
        '''
        :param database: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#database QuicksightDataSource#database}.
        :param host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#host QuicksightDataSource#host}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#port QuicksightDataSource#port}.
        '''
        value = QuicksightDataSourceParametersAuroraPostgresql(
            database=database, host=host, port=port
        )

        return typing.cast(None, jsii.invoke(self, "putAuroraPostgresql", [value]))

    @jsii.member(jsii_name="putAwsIotAnalytics")
    def put_aws_iot_analytics(self, *, data_set_name: builtins.str) -> None:
        '''
        :param data_set_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#data_set_name QuicksightDataSource#data_set_name}.
        '''
        value = QuicksightDataSourceParametersAwsIotAnalytics(
            data_set_name=data_set_name
        )

        return typing.cast(None, jsii.invoke(self, "putAwsIotAnalytics", [value]))

    @jsii.member(jsii_name="putJira")
    def put_jira(self, *, site_base_url: builtins.str) -> None:
        '''
        :param site_base_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#site_base_url QuicksightDataSource#site_base_url}.
        '''
        value = QuicksightDataSourceParametersJira(site_base_url=site_base_url)

        return typing.cast(None, jsii.invoke(self, "putJira", [value]))

    @jsii.member(jsii_name="putMariaDb")
    def put_maria_db(
        self,
        *,
        database: builtins.str,
        host: builtins.str,
        port: jsii.Number,
    ) -> None:
        '''
        :param database: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#database QuicksightDataSource#database}.
        :param host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#host QuicksightDataSource#host}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#port QuicksightDataSource#port}.
        '''
        value = QuicksightDataSourceParametersMariaDb(
            database=database, host=host, port=port
        )

        return typing.cast(None, jsii.invoke(self, "putMariaDb", [value]))

    @jsii.member(jsii_name="putMysql")
    def put_mysql(
        self,
        *,
        database: builtins.str,
        host: builtins.str,
        port: jsii.Number,
    ) -> None:
        '''
        :param database: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#database QuicksightDataSource#database}.
        :param host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#host QuicksightDataSource#host}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#port QuicksightDataSource#port}.
        '''
        value = QuicksightDataSourceParametersMysql(
            database=database, host=host, port=port
        )

        return typing.cast(None, jsii.invoke(self, "putMysql", [value]))

    @jsii.member(jsii_name="putOracle")
    def put_oracle(
        self,
        *,
        database: builtins.str,
        host: builtins.str,
        port: jsii.Number,
    ) -> None:
        '''
        :param database: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#database QuicksightDataSource#database}.
        :param host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#host QuicksightDataSource#host}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#port QuicksightDataSource#port}.
        '''
        value = QuicksightDataSourceParametersOracle(
            database=database, host=host, port=port
        )

        return typing.cast(None, jsii.invoke(self, "putOracle", [value]))

    @jsii.member(jsii_name="putPostgresql")
    def put_postgresql(
        self,
        *,
        database: builtins.str,
        host: builtins.str,
        port: jsii.Number,
    ) -> None:
        '''
        :param database: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#database QuicksightDataSource#database}.
        :param host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#host QuicksightDataSource#host}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#port QuicksightDataSource#port}.
        '''
        value = QuicksightDataSourceParametersPostgresql(
            database=database, host=host, port=port
        )

        return typing.cast(None, jsii.invoke(self, "putPostgresql", [value]))

    @jsii.member(jsii_name="putPresto")
    def put_presto(
        self,
        *,
        catalog: builtins.str,
        host: builtins.str,
        port: jsii.Number,
    ) -> None:
        '''
        :param catalog: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#catalog QuicksightDataSource#catalog}.
        :param host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#host QuicksightDataSource#host}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#port QuicksightDataSource#port}.
        '''
        value = QuicksightDataSourceParametersPresto(
            catalog=catalog, host=host, port=port
        )

        return typing.cast(None, jsii.invoke(self, "putPresto", [value]))

    @jsii.member(jsii_name="putRds")
    def put_rds(self, *, database: builtins.str, instance_id: builtins.str) -> None:
        '''
        :param database: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#database QuicksightDataSource#database}.
        :param instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#instance_id QuicksightDataSource#instance_id}.
        '''
        value = QuicksightDataSourceParametersRds(
            database=database, instance_id=instance_id
        )

        return typing.cast(None, jsii.invoke(self, "putRds", [value]))

    @jsii.member(jsii_name="putRedshift")
    def put_redshift(
        self,
        *,
        database: builtins.str,
        cluster_id: typing.Optional[builtins.str] = None,
        host: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param database: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#database QuicksightDataSource#database}.
        :param cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#cluster_id QuicksightDataSource#cluster_id}.
        :param host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#host QuicksightDataSource#host}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#port QuicksightDataSource#port}.
        '''
        value = QuicksightDataSourceParametersRedshift(
            database=database, cluster_id=cluster_id, host=host, port=port
        )

        return typing.cast(None, jsii.invoke(self, "putRedshift", [value]))

    @jsii.member(jsii_name="putS3")
    def put_s3(
        self,
        *,
        manifest_file_location: typing.Union["QuicksightDataSourceParametersS3ManifestFileLocation", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param manifest_file_location: manifest_file_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#manifest_file_location QuicksightDataSource#manifest_file_location}
        '''
        value = QuicksightDataSourceParametersS3(
            manifest_file_location=manifest_file_location
        )

        return typing.cast(None, jsii.invoke(self, "putS3", [value]))

    @jsii.member(jsii_name="putServiceNow")
    def put_service_now(self, *, site_base_url: builtins.str) -> None:
        '''
        :param site_base_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#site_base_url QuicksightDataSource#site_base_url}.
        '''
        value = QuicksightDataSourceParametersServiceNow(site_base_url=site_base_url)

        return typing.cast(None, jsii.invoke(self, "putServiceNow", [value]))

    @jsii.member(jsii_name="putSnowflake")
    def put_snowflake(
        self,
        *,
        database: builtins.str,
        host: builtins.str,
        warehouse: builtins.str,
    ) -> None:
        '''
        :param database: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#database QuicksightDataSource#database}.
        :param host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#host QuicksightDataSource#host}.
        :param warehouse: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#warehouse QuicksightDataSource#warehouse}.
        '''
        value = QuicksightDataSourceParametersSnowflake(
            database=database, host=host, warehouse=warehouse
        )

        return typing.cast(None, jsii.invoke(self, "putSnowflake", [value]))

    @jsii.member(jsii_name="putSpark")
    def put_spark(self, *, host: builtins.str, port: jsii.Number) -> None:
        '''
        :param host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#host QuicksightDataSource#host}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#port QuicksightDataSource#port}.
        '''
        value = QuicksightDataSourceParametersSpark(host=host, port=port)

        return typing.cast(None, jsii.invoke(self, "putSpark", [value]))

    @jsii.member(jsii_name="putSqlServer")
    def put_sql_server(
        self,
        *,
        database: builtins.str,
        host: builtins.str,
        port: jsii.Number,
    ) -> None:
        '''
        :param database: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#database QuicksightDataSource#database}.
        :param host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#host QuicksightDataSource#host}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#port QuicksightDataSource#port}.
        '''
        value = QuicksightDataSourceParametersSqlServer(
            database=database, host=host, port=port
        )

        return typing.cast(None, jsii.invoke(self, "putSqlServer", [value]))

    @jsii.member(jsii_name="putTeradata")
    def put_teradata(
        self,
        *,
        database: builtins.str,
        host: builtins.str,
        port: jsii.Number,
    ) -> None:
        '''
        :param database: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#database QuicksightDataSource#database}.
        :param host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#host QuicksightDataSource#host}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#port QuicksightDataSource#port}.
        '''
        value = QuicksightDataSourceParametersTeradata(
            database=database, host=host, port=port
        )

        return typing.cast(None, jsii.invoke(self, "putTeradata", [value]))

    @jsii.member(jsii_name="putTwitter")
    def put_twitter(self, *, max_rows: jsii.Number, query: builtins.str) -> None:
        '''
        :param max_rows: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#max_rows QuicksightDataSource#max_rows}.
        :param query: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#query QuicksightDataSource#query}.
        '''
        value = QuicksightDataSourceParametersTwitter(max_rows=max_rows, query=query)

        return typing.cast(None, jsii.invoke(self, "putTwitter", [value]))

    @jsii.member(jsii_name="resetAmazonElasticsearch")
    def reset_amazon_elasticsearch(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAmazonElasticsearch", []))

    @jsii.member(jsii_name="resetAthena")
    def reset_athena(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAthena", []))

    @jsii.member(jsii_name="resetAurora")
    def reset_aurora(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAurora", []))

    @jsii.member(jsii_name="resetAuroraPostgresql")
    def reset_aurora_postgresql(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuroraPostgresql", []))

    @jsii.member(jsii_name="resetAwsIotAnalytics")
    def reset_aws_iot_analytics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsIotAnalytics", []))

    @jsii.member(jsii_name="resetJira")
    def reset_jira(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJira", []))

    @jsii.member(jsii_name="resetMariaDb")
    def reset_maria_db(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMariaDb", []))

    @jsii.member(jsii_name="resetMysql")
    def reset_mysql(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMysql", []))

    @jsii.member(jsii_name="resetOracle")
    def reset_oracle(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOracle", []))

    @jsii.member(jsii_name="resetPostgresql")
    def reset_postgresql(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPostgresql", []))

    @jsii.member(jsii_name="resetPresto")
    def reset_presto(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPresto", []))

    @jsii.member(jsii_name="resetRds")
    def reset_rds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRds", []))

    @jsii.member(jsii_name="resetRedshift")
    def reset_redshift(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedshift", []))

    @jsii.member(jsii_name="resetS3")
    def reset_s3(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3", []))

    @jsii.member(jsii_name="resetServiceNow")
    def reset_service_now(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceNow", []))

    @jsii.member(jsii_name="resetSnowflake")
    def reset_snowflake(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSnowflake", []))

    @jsii.member(jsii_name="resetSpark")
    def reset_spark(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpark", []))

    @jsii.member(jsii_name="resetSqlServer")
    def reset_sql_server(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSqlServer", []))

    @jsii.member(jsii_name="resetTeradata")
    def reset_teradata(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTeradata", []))

    @jsii.member(jsii_name="resetTwitter")
    def reset_twitter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTwitter", []))

    @builtins.property
    @jsii.member(jsii_name="amazonElasticsearch")
    def amazon_elasticsearch(
        self,
    ) -> QuicksightDataSourceParametersAmazonElasticsearchOutputReference:
        return typing.cast(QuicksightDataSourceParametersAmazonElasticsearchOutputReference, jsii.get(self, "amazonElasticsearch"))

    @builtins.property
    @jsii.member(jsii_name="athena")
    def athena(self) -> QuicksightDataSourceParametersAthenaOutputReference:
        return typing.cast(QuicksightDataSourceParametersAthenaOutputReference, jsii.get(self, "athena"))

    @builtins.property
    @jsii.member(jsii_name="aurora")
    def aurora(self) -> QuicksightDataSourceParametersAuroraOutputReference:
        return typing.cast(QuicksightDataSourceParametersAuroraOutputReference, jsii.get(self, "aurora"))

    @builtins.property
    @jsii.member(jsii_name="auroraPostgresql")
    def aurora_postgresql(
        self,
    ) -> QuicksightDataSourceParametersAuroraPostgresqlOutputReference:
        return typing.cast(QuicksightDataSourceParametersAuroraPostgresqlOutputReference, jsii.get(self, "auroraPostgresql"))

    @builtins.property
    @jsii.member(jsii_name="awsIotAnalytics")
    def aws_iot_analytics(
        self,
    ) -> QuicksightDataSourceParametersAwsIotAnalyticsOutputReference:
        return typing.cast(QuicksightDataSourceParametersAwsIotAnalyticsOutputReference, jsii.get(self, "awsIotAnalytics"))

    @builtins.property
    @jsii.member(jsii_name="jira")
    def jira(self) -> QuicksightDataSourceParametersJiraOutputReference:
        return typing.cast(QuicksightDataSourceParametersJiraOutputReference, jsii.get(self, "jira"))

    @builtins.property
    @jsii.member(jsii_name="mariaDb")
    def maria_db(self) -> QuicksightDataSourceParametersMariaDbOutputReference:
        return typing.cast(QuicksightDataSourceParametersMariaDbOutputReference, jsii.get(self, "mariaDb"))

    @builtins.property
    @jsii.member(jsii_name="mysql")
    def mysql(self) -> QuicksightDataSourceParametersMysqlOutputReference:
        return typing.cast(QuicksightDataSourceParametersMysqlOutputReference, jsii.get(self, "mysql"))

    @builtins.property
    @jsii.member(jsii_name="oracle")
    def oracle(self) -> QuicksightDataSourceParametersOracleOutputReference:
        return typing.cast(QuicksightDataSourceParametersOracleOutputReference, jsii.get(self, "oracle"))

    @builtins.property
    @jsii.member(jsii_name="postgresql")
    def postgresql(self) -> "QuicksightDataSourceParametersPostgresqlOutputReference":
        return typing.cast("QuicksightDataSourceParametersPostgresqlOutputReference", jsii.get(self, "postgresql"))

    @builtins.property
    @jsii.member(jsii_name="presto")
    def presto(self) -> "QuicksightDataSourceParametersPrestoOutputReference":
        return typing.cast("QuicksightDataSourceParametersPrestoOutputReference", jsii.get(self, "presto"))

    @builtins.property
    @jsii.member(jsii_name="rds")
    def rds(self) -> "QuicksightDataSourceParametersRdsOutputReference":
        return typing.cast("QuicksightDataSourceParametersRdsOutputReference", jsii.get(self, "rds"))

    @builtins.property
    @jsii.member(jsii_name="redshift")
    def redshift(self) -> "QuicksightDataSourceParametersRedshiftOutputReference":
        return typing.cast("QuicksightDataSourceParametersRedshiftOutputReference", jsii.get(self, "redshift"))

    @builtins.property
    @jsii.member(jsii_name="s3")
    def s3(self) -> "QuicksightDataSourceParametersS3OutputReference":
        return typing.cast("QuicksightDataSourceParametersS3OutputReference", jsii.get(self, "s3"))

    @builtins.property
    @jsii.member(jsii_name="serviceNow")
    def service_now(self) -> "QuicksightDataSourceParametersServiceNowOutputReference":
        return typing.cast("QuicksightDataSourceParametersServiceNowOutputReference", jsii.get(self, "serviceNow"))

    @builtins.property
    @jsii.member(jsii_name="snowflake")
    def snowflake(self) -> "QuicksightDataSourceParametersSnowflakeOutputReference":
        return typing.cast("QuicksightDataSourceParametersSnowflakeOutputReference", jsii.get(self, "snowflake"))

    @builtins.property
    @jsii.member(jsii_name="spark")
    def spark(self) -> "QuicksightDataSourceParametersSparkOutputReference":
        return typing.cast("QuicksightDataSourceParametersSparkOutputReference", jsii.get(self, "spark"))

    @builtins.property
    @jsii.member(jsii_name="sqlServer")
    def sql_server(self) -> "QuicksightDataSourceParametersSqlServerOutputReference":
        return typing.cast("QuicksightDataSourceParametersSqlServerOutputReference", jsii.get(self, "sqlServer"))

    @builtins.property
    @jsii.member(jsii_name="teradata")
    def teradata(self) -> "QuicksightDataSourceParametersTeradataOutputReference":
        return typing.cast("QuicksightDataSourceParametersTeradataOutputReference", jsii.get(self, "teradata"))

    @builtins.property
    @jsii.member(jsii_name="twitter")
    def twitter(self) -> "QuicksightDataSourceParametersTwitterOutputReference":
        return typing.cast("QuicksightDataSourceParametersTwitterOutputReference", jsii.get(self, "twitter"))

    @builtins.property
    @jsii.member(jsii_name="amazonElasticsearchInput")
    def amazon_elasticsearch_input(
        self,
    ) -> typing.Optional[QuicksightDataSourceParametersAmazonElasticsearch]:
        return typing.cast(typing.Optional[QuicksightDataSourceParametersAmazonElasticsearch], jsii.get(self, "amazonElasticsearchInput"))

    @builtins.property
    @jsii.member(jsii_name="athenaInput")
    def athena_input(self) -> typing.Optional[QuicksightDataSourceParametersAthena]:
        return typing.cast(typing.Optional[QuicksightDataSourceParametersAthena], jsii.get(self, "athenaInput"))

    @builtins.property
    @jsii.member(jsii_name="auroraInput")
    def aurora_input(self) -> typing.Optional[QuicksightDataSourceParametersAurora]:
        return typing.cast(typing.Optional[QuicksightDataSourceParametersAurora], jsii.get(self, "auroraInput"))

    @builtins.property
    @jsii.member(jsii_name="auroraPostgresqlInput")
    def aurora_postgresql_input(
        self,
    ) -> typing.Optional[QuicksightDataSourceParametersAuroraPostgresql]:
        return typing.cast(typing.Optional[QuicksightDataSourceParametersAuroraPostgresql], jsii.get(self, "auroraPostgresqlInput"))

    @builtins.property
    @jsii.member(jsii_name="awsIotAnalyticsInput")
    def aws_iot_analytics_input(
        self,
    ) -> typing.Optional[QuicksightDataSourceParametersAwsIotAnalytics]:
        return typing.cast(typing.Optional[QuicksightDataSourceParametersAwsIotAnalytics], jsii.get(self, "awsIotAnalyticsInput"))

    @builtins.property
    @jsii.member(jsii_name="jiraInput")
    def jira_input(self) -> typing.Optional[QuicksightDataSourceParametersJira]:
        return typing.cast(typing.Optional[QuicksightDataSourceParametersJira], jsii.get(self, "jiraInput"))

    @builtins.property
    @jsii.member(jsii_name="mariaDbInput")
    def maria_db_input(self) -> typing.Optional[QuicksightDataSourceParametersMariaDb]:
        return typing.cast(typing.Optional[QuicksightDataSourceParametersMariaDb], jsii.get(self, "mariaDbInput"))

    @builtins.property
    @jsii.member(jsii_name="mysqlInput")
    def mysql_input(self) -> typing.Optional[QuicksightDataSourceParametersMysql]:
        return typing.cast(typing.Optional[QuicksightDataSourceParametersMysql], jsii.get(self, "mysqlInput"))

    @builtins.property
    @jsii.member(jsii_name="oracleInput")
    def oracle_input(self) -> typing.Optional[QuicksightDataSourceParametersOracle]:
        return typing.cast(typing.Optional[QuicksightDataSourceParametersOracle], jsii.get(self, "oracleInput"))

    @builtins.property
    @jsii.member(jsii_name="postgresqlInput")
    def postgresql_input(
        self,
    ) -> typing.Optional["QuicksightDataSourceParametersPostgresql"]:
        return typing.cast(typing.Optional["QuicksightDataSourceParametersPostgresql"], jsii.get(self, "postgresqlInput"))

    @builtins.property
    @jsii.member(jsii_name="prestoInput")
    def presto_input(self) -> typing.Optional["QuicksightDataSourceParametersPresto"]:
        return typing.cast(typing.Optional["QuicksightDataSourceParametersPresto"], jsii.get(self, "prestoInput"))

    @builtins.property
    @jsii.member(jsii_name="rdsInput")
    def rds_input(self) -> typing.Optional["QuicksightDataSourceParametersRds"]:
        return typing.cast(typing.Optional["QuicksightDataSourceParametersRds"], jsii.get(self, "rdsInput"))

    @builtins.property
    @jsii.member(jsii_name="redshiftInput")
    def redshift_input(
        self,
    ) -> typing.Optional["QuicksightDataSourceParametersRedshift"]:
        return typing.cast(typing.Optional["QuicksightDataSourceParametersRedshift"], jsii.get(self, "redshiftInput"))

    @builtins.property
    @jsii.member(jsii_name="s3Input")
    def s3_input(self) -> typing.Optional["QuicksightDataSourceParametersS3"]:
        return typing.cast(typing.Optional["QuicksightDataSourceParametersS3"], jsii.get(self, "s3Input"))

    @builtins.property
    @jsii.member(jsii_name="serviceNowInput")
    def service_now_input(
        self,
    ) -> typing.Optional["QuicksightDataSourceParametersServiceNow"]:
        return typing.cast(typing.Optional["QuicksightDataSourceParametersServiceNow"], jsii.get(self, "serviceNowInput"))

    @builtins.property
    @jsii.member(jsii_name="snowflakeInput")
    def snowflake_input(
        self,
    ) -> typing.Optional["QuicksightDataSourceParametersSnowflake"]:
        return typing.cast(typing.Optional["QuicksightDataSourceParametersSnowflake"], jsii.get(self, "snowflakeInput"))

    @builtins.property
    @jsii.member(jsii_name="sparkInput")
    def spark_input(self) -> typing.Optional["QuicksightDataSourceParametersSpark"]:
        return typing.cast(typing.Optional["QuicksightDataSourceParametersSpark"], jsii.get(self, "sparkInput"))

    @builtins.property
    @jsii.member(jsii_name="sqlServerInput")
    def sql_server_input(
        self,
    ) -> typing.Optional["QuicksightDataSourceParametersSqlServer"]:
        return typing.cast(typing.Optional["QuicksightDataSourceParametersSqlServer"], jsii.get(self, "sqlServerInput"))

    @builtins.property
    @jsii.member(jsii_name="teradataInput")
    def teradata_input(
        self,
    ) -> typing.Optional["QuicksightDataSourceParametersTeradata"]:
        return typing.cast(typing.Optional["QuicksightDataSourceParametersTeradata"], jsii.get(self, "teradataInput"))

    @builtins.property
    @jsii.member(jsii_name="twitterInput")
    def twitter_input(self) -> typing.Optional["QuicksightDataSourceParametersTwitter"]:
        return typing.cast(typing.Optional["QuicksightDataSourceParametersTwitter"], jsii.get(self, "twitterInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[QuicksightDataSourceParameters]:
        return typing.cast(typing.Optional[QuicksightDataSourceParameters], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[QuicksightDataSourceParameters],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8964d037d31c131064fd1a24ed9858103c0ee0513785cf015e523c07cb7730a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceParametersPostgresql",
    jsii_struct_bases=[],
    name_mapping={"database": "database", "host": "host", "port": "port"},
)
class QuicksightDataSourceParametersPostgresql:
    def __init__(
        self,
        *,
        database: builtins.str,
        host: builtins.str,
        port: jsii.Number,
    ) -> None:
        '''
        :param database: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#database QuicksightDataSource#database}.
        :param host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#host QuicksightDataSource#host}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#port QuicksightDataSource#port}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c60a37250b6f168d915bffed76c5d6030e05c9a3c9a22ae2e5839943d90cf20)
            check_type(argname="argument database", value=database, expected_type=type_hints["database"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "database": database,
            "host": host,
            "port": port,
        }

    @builtins.property
    def database(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#database QuicksightDataSource#database}.'''
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def host(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#host QuicksightDataSource#host}.'''
        result = self._values.get("host")
        assert result is not None, "Required property 'host' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#port QuicksightDataSource#port}.'''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QuicksightDataSourceParametersPostgresql(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class QuicksightDataSourceParametersPostgresqlOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceParametersPostgresqlOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__eae803b0c3a881ea40e30ea52220d495c42bb7dd11730bdf2992054aa44fc9af)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="databaseInput")
    def database_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseInput"))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="database")
    def database(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "database"))

    @database.setter
    def database(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8822e3eb6c083a364e2e408160e6e93d659c6430bfe66f737fb2baf3f27e274f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "database", value)

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @host.setter
    def host(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f2ebc3e5f05f3fa508da55bcce7ac9dea6578921d076def4a35a747ca09736b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aeab011955051f7528f0bd958d2e48b5ead4fd4436f113d902b6088f13e407b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[QuicksightDataSourceParametersPostgresql]:
        return typing.cast(typing.Optional[QuicksightDataSourceParametersPostgresql], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[QuicksightDataSourceParametersPostgresql],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ba7ecdd402716ff8ca4d3f8f75b0967551849b54a01086d35bfef7d24fd3005)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceParametersPresto",
    jsii_struct_bases=[],
    name_mapping={"catalog": "catalog", "host": "host", "port": "port"},
)
class QuicksightDataSourceParametersPresto:
    def __init__(
        self,
        *,
        catalog: builtins.str,
        host: builtins.str,
        port: jsii.Number,
    ) -> None:
        '''
        :param catalog: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#catalog QuicksightDataSource#catalog}.
        :param host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#host QuicksightDataSource#host}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#port QuicksightDataSource#port}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a275bbf8fc74883ab0feb0d072a30daf180644a04f1e0dd6ee5762efb76465da)
            check_type(argname="argument catalog", value=catalog, expected_type=type_hints["catalog"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "catalog": catalog,
            "host": host,
            "port": port,
        }

    @builtins.property
    def catalog(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#catalog QuicksightDataSource#catalog}.'''
        result = self._values.get("catalog")
        assert result is not None, "Required property 'catalog' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def host(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#host QuicksightDataSource#host}.'''
        result = self._values.get("host")
        assert result is not None, "Required property 'host' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#port QuicksightDataSource#port}.'''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QuicksightDataSourceParametersPresto(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class QuicksightDataSourceParametersPrestoOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceParametersPrestoOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ae45ef469f120e0d8e844cc0be047e6a1c9e2897d94483f96fd3507340d46bad)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="catalogInput")
    def catalog_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "catalogInput"))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="catalog")
    def catalog(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "catalog"))

    @catalog.setter
    def catalog(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d039332f8ea02ba4f7f03ca28ce8f9fcb84c7f1db33038a8547fc15a4e38519f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "catalog", value)

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @host.setter
    def host(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9557ddc7a0343351d051d28508a46690e0dc43f2083a7cb84558dc47aaee11d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3848a3e984b71598e5849f978549a8475b8cbcd8272d754029c183de20a6ddb6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[QuicksightDataSourceParametersPresto]:
        return typing.cast(typing.Optional[QuicksightDataSourceParametersPresto], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[QuicksightDataSourceParametersPresto],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed2b36b955374de5ae6a17f946a961403ba001f87f0a94bf1a5130fcfab961b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceParametersRds",
    jsii_struct_bases=[],
    name_mapping={"database": "database", "instance_id": "instanceId"},
)
class QuicksightDataSourceParametersRds:
    def __init__(self, *, database: builtins.str, instance_id: builtins.str) -> None:
        '''
        :param database: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#database QuicksightDataSource#database}.
        :param instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#instance_id QuicksightDataSource#instance_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__821b4385ff78925e4f11b2a2e17ec5fbb816d8248eac73e6dc2eb5efc5a87a52)
            check_type(argname="argument database", value=database, expected_type=type_hints["database"])
            check_type(argname="argument instance_id", value=instance_id, expected_type=type_hints["instance_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "database": database,
            "instance_id": instance_id,
        }

    @builtins.property
    def database(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#database QuicksightDataSource#database}.'''
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#instance_id QuicksightDataSource#instance_id}.'''
        result = self._values.get("instance_id")
        assert result is not None, "Required property 'instance_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QuicksightDataSourceParametersRds(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class QuicksightDataSourceParametersRdsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceParametersRdsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8ea1131f0327041e6d723d51ac8528a64f393883719a78bc9eced62cf38d9195)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="databaseInput")
    def database_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceIdInput")
    def instance_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="database")
    def database(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "database"))

    @database.setter
    def database(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74258ee5273afc332e64a034bd01fce0bb18b1b77f32e8370ebf5867ecfcec3d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "database", value)

    @builtins.property
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceId"))

    @instance_id.setter
    def instance_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2cd88ef8f3e73b6ec5ccbc4c1b03c7d273be389021a1b1cf4b96752e85aad70)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[QuicksightDataSourceParametersRds]:
        return typing.cast(typing.Optional[QuicksightDataSourceParametersRds], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[QuicksightDataSourceParametersRds],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__913e2f204aa0afdc73fa1b1d0f39033ec568e43c45bc97ecb60d77901ad1311f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceParametersRedshift",
    jsii_struct_bases=[],
    name_mapping={
        "database": "database",
        "cluster_id": "clusterId",
        "host": "host",
        "port": "port",
    },
)
class QuicksightDataSourceParametersRedshift:
    def __init__(
        self,
        *,
        database: builtins.str,
        cluster_id: typing.Optional[builtins.str] = None,
        host: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param database: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#database QuicksightDataSource#database}.
        :param cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#cluster_id QuicksightDataSource#cluster_id}.
        :param host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#host QuicksightDataSource#host}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#port QuicksightDataSource#port}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__377b5d266dd186abcd65e7d1abadf3541948a757048c5d9e0aba08cdc2ca84d0)
            check_type(argname="argument database", value=database, expected_type=type_hints["database"])
            check_type(argname="argument cluster_id", value=cluster_id, expected_type=type_hints["cluster_id"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "database": database,
        }
        if cluster_id is not None:
            self._values["cluster_id"] = cluster_id
        if host is not None:
            self._values["host"] = host
        if port is not None:
            self._values["port"] = port

    @builtins.property
    def database(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#database QuicksightDataSource#database}.'''
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cluster_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#cluster_id QuicksightDataSource#cluster_id}.'''
        result = self._values.get("cluster_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#host QuicksightDataSource#host}.'''
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#port QuicksightDataSource#port}.'''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QuicksightDataSourceParametersRedshift(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class QuicksightDataSourceParametersRedshiftOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceParametersRedshiftOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a32aaee60783b6a88201e39194e69f8b162be869e16c6064218fbc39706fce7d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetClusterId")
    def reset_cluster_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterId", []))

    @jsii.member(jsii_name="resetHost")
    def reset_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHost", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @builtins.property
    @jsii.member(jsii_name="clusterIdInput")
    def cluster_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterIdInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseInput")
    def database_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseInput"))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterId")
    def cluster_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterId"))

    @cluster_id.setter
    def cluster_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8335a2c7f7b2526c9db081773b46003d3fa3a601a29444113340e8d988e8a956)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterId", value)

    @builtins.property
    @jsii.member(jsii_name="database")
    def database(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "database"))

    @database.setter
    def database(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a1575689b936b026640f79474d06f52f4ee342988d8e5379c5d0662d59da8fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "database", value)

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @host.setter
    def host(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c9ff4506191acdd22511429d64efa810ac75100f838c299d17265518016fe58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9f391d98548c6848950b5115066ccb437d64a91169a94d5f3f1993e72202ba9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[QuicksightDataSourceParametersRedshift]:
        return typing.cast(typing.Optional[QuicksightDataSourceParametersRedshift], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[QuicksightDataSourceParametersRedshift],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0811a59927b0ac8a8d16a89c970525e52a790710cf50937334378f4ac7da3ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceParametersS3",
    jsii_struct_bases=[],
    name_mapping={"manifest_file_location": "manifestFileLocation"},
)
class QuicksightDataSourceParametersS3:
    def __init__(
        self,
        *,
        manifest_file_location: typing.Union["QuicksightDataSourceParametersS3ManifestFileLocation", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param manifest_file_location: manifest_file_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#manifest_file_location QuicksightDataSource#manifest_file_location}
        '''
        if isinstance(manifest_file_location, dict):
            manifest_file_location = QuicksightDataSourceParametersS3ManifestFileLocation(**manifest_file_location)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0755232c53887364728ac31016244692fc32917e7eb8912eed08ec57ec65946)
            check_type(argname="argument manifest_file_location", value=manifest_file_location, expected_type=type_hints["manifest_file_location"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "manifest_file_location": manifest_file_location,
        }

    @builtins.property
    def manifest_file_location(
        self,
    ) -> "QuicksightDataSourceParametersS3ManifestFileLocation":
        '''manifest_file_location block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#manifest_file_location QuicksightDataSource#manifest_file_location}
        '''
        result = self._values.get("manifest_file_location")
        assert result is not None, "Required property 'manifest_file_location' is missing"
        return typing.cast("QuicksightDataSourceParametersS3ManifestFileLocation", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QuicksightDataSourceParametersS3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceParametersS3ManifestFileLocation",
    jsii_struct_bases=[],
    name_mapping={"bucket": "bucket", "key": "key"},
)
class QuicksightDataSourceParametersS3ManifestFileLocation:
    def __init__(self, *, bucket: builtins.str, key: builtins.str) -> None:
        '''
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#bucket QuicksightDataSource#bucket}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#key QuicksightDataSource#key}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5aacf00da87a67d3cd11d576991c1ef410453ced31da3052098a21d7e866a07)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket": bucket,
            "key": key,
        }

    @builtins.property
    def bucket(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#bucket QuicksightDataSource#bucket}.'''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#key QuicksightDataSource#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QuicksightDataSourceParametersS3ManifestFileLocation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class QuicksightDataSourceParametersS3ManifestFileLocationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceParametersS3ManifestFileLocationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b384ca77d02fb5cf7f7e71b0218a52cd088e1dbdceeb0c89a7029ce914fef963)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="bucketInput")
    def bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0d23cb40bd85aa0ce7f74a0ec2bc9f11e492c673783efd357beed35f92bf11a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucket", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c13505e741d27a34bf83a99de09119c3992a978d74cfc0cf7a1131111ea3c595)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[QuicksightDataSourceParametersS3ManifestFileLocation]:
        return typing.cast(typing.Optional[QuicksightDataSourceParametersS3ManifestFileLocation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[QuicksightDataSourceParametersS3ManifestFileLocation],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3fdf552f1c71ce4f9587d28ecc170c594d7a62afbccebfd8f16f943eaaace18)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class QuicksightDataSourceParametersS3OutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceParametersS3OutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__564409363099b6c2c65063b6a3b873340233da669b21639fe75eeef59025da7a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putManifestFileLocation")
    def put_manifest_file_location(
        self,
        *,
        bucket: builtins.str,
        key: builtins.str,
    ) -> None:
        '''
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#bucket QuicksightDataSource#bucket}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#key QuicksightDataSource#key}.
        '''
        value = QuicksightDataSourceParametersS3ManifestFileLocation(
            bucket=bucket, key=key
        )

        return typing.cast(None, jsii.invoke(self, "putManifestFileLocation", [value]))

    @builtins.property
    @jsii.member(jsii_name="manifestFileLocation")
    def manifest_file_location(
        self,
    ) -> QuicksightDataSourceParametersS3ManifestFileLocationOutputReference:
        return typing.cast(QuicksightDataSourceParametersS3ManifestFileLocationOutputReference, jsii.get(self, "manifestFileLocation"))

    @builtins.property
    @jsii.member(jsii_name="manifestFileLocationInput")
    def manifest_file_location_input(
        self,
    ) -> typing.Optional[QuicksightDataSourceParametersS3ManifestFileLocation]:
        return typing.cast(typing.Optional[QuicksightDataSourceParametersS3ManifestFileLocation], jsii.get(self, "manifestFileLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[QuicksightDataSourceParametersS3]:
        return typing.cast(typing.Optional[QuicksightDataSourceParametersS3], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[QuicksightDataSourceParametersS3],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fc9cd0b0a2b24d99f461372e847cecfd9c8539b2686fe9d242e188cd2f8b5d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceParametersServiceNow",
    jsii_struct_bases=[],
    name_mapping={"site_base_url": "siteBaseUrl"},
)
class QuicksightDataSourceParametersServiceNow:
    def __init__(self, *, site_base_url: builtins.str) -> None:
        '''
        :param site_base_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#site_base_url QuicksightDataSource#site_base_url}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83ee293b07905cb493005a923f0985999aff6d8f7827ecb7d7281188ccc46966)
            check_type(argname="argument site_base_url", value=site_base_url, expected_type=type_hints["site_base_url"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "site_base_url": site_base_url,
        }

    @builtins.property
    def site_base_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#site_base_url QuicksightDataSource#site_base_url}.'''
        result = self._values.get("site_base_url")
        assert result is not None, "Required property 'site_base_url' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QuicksightDataSourceParametersServiceNow(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class QuicksightDataSourceParametersServiceNowOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceParametersServiceNowOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__224f48d3e59ed11679a859f8ed22ef12cffdf94c504884665896fe5f946c645d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="siteBaseUrlInput")
    def site_base_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "siteBaseUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="siteBaseUrl")
    def site_base_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "siteBaseUrl"))

    @site_base_url.setter
    def site_base_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91984e170c145e3110832a8f7cd651aa85e15eb4e9989eb9496dbcf783cd2c81)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "siteBaseUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[QuicksightDataSourceParametersServiceNow]:
        return typing.cast(typing.Optional[QuicksightDataSourceParametersServiceNow], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[QuicksightDataSourceParametersServiceNow],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ecc8e130123885871512f4a0a1fec19b907f2194ae69a277b32841804f4a84f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceParametersSnowflake",
    jsii_struct_bases=[],
    name_mapping={"database": "database", "host": "host", "warehouse": "warehouse"},
)
class QuicksightDataSourceParametersSnowflake:
    def __init__(
        self,
        *,
        database: builtins.str,
        host: builtins.str,
        warehouse: builtins.str,
    ) -> None:
        '''
        :param database: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#database QuicksightDataSource#database}.
        :param host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#host QuicksightDataSource#host}.
        :param warehouse: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#warehouse QuicksightDataSource#warehouse}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1c9818258f2a13c9f331abc749e495c80765be0138f40a235139c07f10ffdf5)
            check_type(argname="argument database", value=database, expected_type=type_hints["database"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument warehouse", value=warehouse, expected_type=type_hints["warehouse"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "database": database,
            "host": host,
            "warehouse": warehouse,
        }

    @builtins.property
    def database(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#database QuicksightDataSource#database}.'''
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def host(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#host QuicksightDataSource#host}.'''
        result = self._values.get("host")
        assert result is not None, "Required property 'host' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def warehouse(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#warehouse QuicksightDataSource#warehouse}.'''
        result = self._values.get("warehouse")
        assert result is not None, "Required property 'warehouse' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QuicksightDataSourceParametersSnowflake(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class QuicksightDataSourceParametersSnowflakeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceParametersSnowflakeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ade90c50de7a4f118a0a5c981157273812b58d4a7ccadbab9e908748b8f1313e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="databaseInput")
    def database_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseInput"))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="warehouseInput")
    def warehouse_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "warehouseInput"))

    @builtins.property
    @jsii.member(jsii_name="database")
    def database(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "database"))

    @database.setter
    def database(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7fa1ac12c58f2a54b6069336ea46ac60f3c95b4c0d86516e5f6631f52501f358)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "database", value)

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @host.setter
    def host(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__345fa1fbefd7c5a7c47b09e6c4187ac79ea32767b923bee8e9451207e7a436c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="warehouse")
    def warehouse(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "warehouse"))

    @warehouse.setter
    def warehouse(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3cb49acb0bda4743b35800512378b0a88d37d3efbaeee22dd472ae6364c9139a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "warehouse", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[QuicksightDataSourceParametersSnowflake]:
        return typing.cast(typing.Optional[QuicksightDataSourceParametersSnowflake], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[QuicksightDataSourceParametersSnowflake],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2871af9351fa38651301dfac42c30a0a11c73196ad414d75aa44656bc7fda7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceParametersSpark",
    jsii_struct_bases=[],
    name_mapping={"host": "host", "port": "port"},
)
class QuicksightDataSourceParametersSpark:
    def __init__(self, *, host: builtins.str, port: jsii.Number) -> None:
        '''
        :param host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#host QuicksightDataSource#host}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#port QuicksightDataSource#port}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfc4f932e247327e70c0aa168ac4cc1aa4c4194ddaa2815d274bd053bc56f6bf)
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "host": host,
            "port": port,
        }

    @builtins.property
    def host(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#host QuicksightDataSource#host}.'''
        result = self._values.get("host")
        assert result is not None, "Required property 'host' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#port QuicksightDataSource#port}.'''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QuicksightDataSourceParametersSpark(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class QuicksightDataSourceParametersSparkOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceParametersSparkOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f854e3c3d34078b1f2ac17d694410dc11f476faa33563f3786db8c2530bc2f37)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @host.setter
    def host(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e4b6d457c4b00a3e85f2d188d15ed42d9ce76509ee645ac7c4e6e41f9db85fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e17b65aef720a707288cfaa37210f0488ea418d9753a879080889a5c0be1bae0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[QuicksightDataSourceParametersSpark]:
        return typing.cast(typing.Optional[QuicksightDataSourceParametersSpark], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[QuicksightDataSourceParametersSpark],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7bc436077e9aa7af11c1198e8e0f746a0043197975e3301df9fa386c48b8f9a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceParametersSqlServer",
    jsii_struct_bases=[],
    name_mapping={"database": "database", "host": "host", "port": "port"},
)
class QuicksightDataSourceParametersSqlServer:
    def __init__(
        self,
        *,
        database: builtins.str,
        host: builtins.str,
        port: jsii.Number,
    ) -> None:
        '''
        :param database: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#database QuicksightDataSource#database}.
        :param host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#host QuicksightDataSource#host}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#port QuicksightDataSource#port}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1aae51c0cf1ab4748d304e5756b7bfab63be5a0442da7221bfd0aba3acc5f8c2)
            check_type(argname="argument database", value=database, expected_type=type_hints["database"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "database": database,
            "host": host,
            "port": port,
        }

    @builtins.property
    def database(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#database QuicksightDataSource#database}.'''
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def host(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#host QuicksightDataSource#host}.'''
        result = self._values.get("host")
        assert result is not None, "Required property 'host' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#port QuicksightDataSource#port}.'''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QuicksightDataSourceParametersSqlServer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class QuicksightDataSourceParametersSqlServerOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceParametersSqlServerOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d7417909729173f774eeb05dbb45c29b4f1508824e69ed237c50d56c7a265045)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="databaseInput")
    def database_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseInput"))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="database")
    def database(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "database"))

    @database.setter
    def database(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25d5203fcdb5e0aa81c8f44a6890c88c19cba43ef625efea3b50914ef35ccc8c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "database", value)

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @host.setter
    def host(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__deb1f63256741eda6a8d93d1c074f46e837e5eb20cbc9d1f21efa2f0e3c25dce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6a4596394c7d15fd4f87e0e50b056a1591448883a453f26463c4b531094cbd2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[QuicksightDataSourceParametersSqlServer]:
        return typing.cast(typing.Optional[QuicksightDataSourceParametersSqlServer], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[QuicksightDataSourceParametersSqlServer],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__028f82d2b862a64daee9f38b4c2dedc3b0426db6d83df28561211a53769ef3dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceParametersTeradata",
    jsii_struct_bases=[],
    name_mapping={"database": "database", "host": "host", "port": "port"},
)
class QuicksightDataSourceParametersTeradata:
    def __init__(
        self,
        *,
        database: builtins.str,
        host: builtins.str,
        port: jsii.Number,
    ) -> None:
        '''
        :param database: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#database QuicksightDataSource#database}.
        :param host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#host QuicksightDataSource#host}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#port QuicksightDataSource#port}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7321f53be6b7afe57a0a4a44730177d211084f4e021ae3d573bf5db48ba75f62)
            check_type(argname="argument database", value=database, expected_type=type_hints["database"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "database": database,
            "host": host,
            "port": port,
        }

    @builtins.property
    def database(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#database QuicksightDataSource#database}.'''
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def host(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#host QuicksightDataSource#host}.'''
        result = self._values.get("host")
        assert result is not None, "Required property 'host' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#port QuicksightDataSource#port}.'''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QuicksightDataSourceParametersTeradata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class QuicksightDataSourceParametersTeradataOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceParametersTeradataOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__197f9567c1d2ef25651212f327bfcddf08a08b5d1a5c8ffb973143bb7f3927f8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="databaseInput")
    def database_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseInput"))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="database")
    def database(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "database"))

    @database.setter
    def database(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__750d9471711335403c1a50389d468f3ac639fafe30c200a48c2f4b53c936e65e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "database", value)

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @host.setter
    def host(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53211a9094eeebf7897bcbf610fbf1317e7c970f007affcbdd4547beb9055d7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__346f2d704df145df2d79b8fcf21f08d67171a4f06475260e284df484ff7c8afe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[QuicksightDataSourceParametersTeradata]:
        return typing.cast(typing.Optional[QuicksightDataSourceParametersTeradata], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[QuicksightDataSourceParametersTeradata],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__240a41babc16df609f27f888245c6fb9e205f0688173f7544ecbbaae4565fa39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceParametersTwitter",
    jsii_struct_bases=[],
    name_mapping={"max_rows": "maxRows", "query": "query"},
)
class QuicksightDataSourceParametersTwitter:
    def __init__(self, *, max_rows: jsii.Number, query: builtins.str) -> None:
        '''
        :param max_rows: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#max_rows QuicksightDataSource#max_rows}.
        :param query: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#query QuicksightDataSource#query}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0be6a17f5863fa16f49831b112972628e3aa2ef6556a6512ba7a118fdc5f4f0)
            check_type(argname="argument max_rows", value=max_rows, expected_type=type_hints["max_rows"])
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "max_rows": max_rows,
            "query": query,
        }

    @builtins.property
    def max_rows(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#max_rows QuicksightDataSource#max_rows}.'''
        result = self._values.get("max_rows")
        assert result is not None, "Required property 'max_rows' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def query(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#query QuicksightDataSource#query}.'''
        result = self._values.get("query")
        assert result is not None, "Required property 'query' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QuicksightDataSourceParametersTwitter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class QuicksightDataSourceParametersTwitterOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceParametersTwitterOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5e1a12dac4ecc8ed7f65c375eb52786b1610dead0e1956fa19bb79b2278ab2ea)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="maxRowsInput")
    def max_rows_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxRowsInput"))

    @builtins.property
    @jsii.member(jsii_name="queryInput")
    def query_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="maxRows")
    def max_rows(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxRows"))

    @max_rows.setter
    def max_rows(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2fc0111e1a34b9a189f024feedefc038e481d2d08c4f59f73be354d254ef235)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxRows", value)

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "query"))

    @query.setter
    def query(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6adcce46c5bf147b69574610daee2b145b9488b704f578af2ab26b51e3aea3eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "query", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[QuicksightDataSourceParametersTwitter]:
        return typing.cast(typing.Optional[QuicksightDataSourceParametersTwitter], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[QuicksightDataSourceParametersTwitter],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e1f12c44aea2db0edf1fa4dcba6b78462eb9d926a271de61e34889ac5424d06)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.quicksightDataSource.QuicksightDataSourcePermission",
    jsii_struct_bases=[],
    name_mapping={"actions": "actions", "principal": "principal"},
)
class QuicksightDataSourcePermission:
    def __init__(
        self,
        *,
        actions: typing.Sequence[builtins.str],
        principal: builtins.str,
    ) -> None:
        '''
        :param actions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#actions QuicksightDataSource#actions}.
        :param principal: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#principal QuicksightDataSource#principal}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b803cac9313c3c70b91d8a2303a8c801408e7d6678b0a44c2b4912435de2473)
            check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
            check_type(argname="argument principal", value=principal, expected_type=type_hints["principal"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "actions": actions,
            "principal": principal,
        }

    @builtins.property
    def actions(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#actions QuicksightDataSource#actions}.'''
        result = self._values.get("actions")
        assert result is not None, "Required property 'actions' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def principal(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#principal QuicksightDataSource#principal}.'''
        result = self._values.get("principal")
        assert result is not None, "Required property 'principal' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QuicksightDataSourcePermission(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class QuicksightDataSourcePermissionList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.quicksightDataSource.QuicksightDataSourcePermissionList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5f142915611ab0bc25cd3fc30fd082e46e9bafd791d43f582250d1083bec76e7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "QuicksightDataSourcePermissionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c57989305627e366a27e47843cf145c311d61ce11bccd6e6151a4e51e4afc862)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("QuicksightDataSourcePermissionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aef130e1d28f76a88e5d2c3a4650e4820314eea1123d74bae0afecab48a97306)
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
            type_hints = typing.get_type_hints(_typecheckingstub__826708b544cd01593cb4be7c22a27ec73ee4fbd9d3d1ae97ac81d96145aed10c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__33a27dd82a74a92648bdb5322e9ecdbf5c983b4b034a9f2a69988583afa3489e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[QuicksightDataSourcePermission]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[QuicksightDataSourcePermission]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[QuicksightDataSourcePermission]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c773c6146fa1db88f14c1d7e8f4334d4ea171e75b8a0d75d444f2d5093c709ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class QuicksightDataSourcePermissionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.quicksightDataSource.QuicksightDataSourcePermissionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__44f9b6c05dc99a8d147ea53187f9d14d1ad543ab703db564b0463124611aab60)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="actionsInput")
    def actions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "actionsInput"))

    @builtins.property
    @jsii.member(jsii_name="principalInput")
    def principal_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "principalInput"))

    @builtins.property
    @jsii.member(jsii_name="actions")
    def actions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "actions"))

    @actions.setter
    def actions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abf83d92fa93efd5dc11a5dc23069176413b1e081bec30bafbd782eefa6643c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actions", value)

    @builtins.property
    @jsii.member(jsii_name="principal")
    def principal(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "principal"))

    @principal.setter
    def principal(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50a992bfe4725d1131fe5515b0db56aab0246b91ea379f4c2419fb2127439234)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "principal", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[QuicksightDataSourcePermission, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[QuicksightDataSourcePermission, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[QuicksightDataSourcePermission, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4f78918b171029a13e6ba89aca4c00ecf0bc3bdcf55540513a912bf44d74cf2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceSslProperties",
    jsii_struct_bases=[],
    name_mapping={"disable_ssl": "disableSsl"},
)
class QuicksightDataSourceSslProperties:
    def __init__(
        self,
        *,
        disable_ssl: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param disable_ssl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#disable_ssl QuicksightDataSource#disable_ssl}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f791c3d60fa6a5f9f23b589bc44de28a1b1717b1b99895ca408f58de29d0dc0a)
            check_type(argname="argument disable_ssl", value=disable_ssl, expected_type=type_hints["disable_ssl"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "disable_ssl": disable_ssl,
        }

    @builtins.property
    def disable_ssl(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#disable_ssl QuicksightDataSource#disable_ssl}.'''
        result = self._values.get("disable_ssl")
        assert result is not None, "Required property 'disable_ssl' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QuicksightDataSourceSslProperties(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class QuicksightDataSourceSslPropertiesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceSslPropertiesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__24eee20839d1173aa574fb7f4d9ab8cf1485189902000ba0a2cb38964675e168)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="disableSslInput")
    def disable_ssl_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disableSslInput"))

    @builtins.property
    @jsii.member(jsii_name="disableSsl")
    def disable_ssl(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "disableSsl"))

    @disable_ssl.setter
    def disable_ssl(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b44f5545e138c468891ee24603e819d550ae590099797adb566ad2772a611a13)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableSsl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[QuicksightDataSourceSslProperties]:
        return typing.cast(typing.Optional[QuicksightDataSourceSslProperties], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[QuicksightDataSourceSslProperties],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00c64d9bcf755fb3320204b2cb969b6de05c98f700a55efb1d35aa7a6335897d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceVpcConnectionProperties",
    jsii_struct_bases=[],
    name_mapping={"vpc_connection_arn": "vpcConnectionArn"},
)
class QuicksightDataSourceVpcConnectionProperties:
    def __init__(self, *, vpc_connection_arn: builtins.str) -> None:
        '''
        :param vpc_connection_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#vpc_connection_arn QuicksightDataSource#vpc_connection_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3785a15b60637d36496cd972f5b9b61b825da4e4d970fe6d168ed900048d6800)
            check_type(argname="argument vpc_connection_arn", value=vpc_connection_arn, expected_type=type_hints["vpc_connection_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "vpc_connection_arn": vpc_connection_arn,
        }

    @builtins.property
    def vpc_connection_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/quicksight_data_source#vpc_connection_arn QuicksightDataSource#vpc_connection_arn}.'''
        result = self._values.get("vpc_connection_arn")
        assert result is not None, "Required property 'vpc_connection_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QuicksightDataSourceVpcConnectionProperties(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class QuicksightDataSourceVpcConnectionPropertiesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.quicksightDataSource.QuicksightDataSourceVpcConnectionPropertiesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ac47d16817fef8cdc4bac4059261e2d9db74c979d22d096109717e5dacaae9d7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="vpcConnectionArnInput")
    def vpc_connection_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpcConnectionArnInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcConnectionArn")
    def vpc_connection_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcConnectionArn"))

    @vpc_connection_arn.setter
    def vpc_connection_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__383de5c05363d05d7cbd2f400936397bc286f9da459976d16d63e664780b1d1c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcConnectionArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[QuicksightDataSourceVpcConnectionProperties]:
        return typing.cast(typing.Optional[QuicksightDataSourceVpcConnectionProperties], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[QuicksightDataSourceVpcConnectionProperties],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0abbd00a62f2b369b19f028246ea25bd08528ab34c95cf23731aee472432ea8a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "QuicksightDataSource",
    "QuicksightDataSourceConfig",
    "QuicksightDataSourceCredentials",
    "QuicksightDataSourceCredentialsCredentialPair",
    "QuicksightDataSourceCredentialsCredentialPairOutputReference",
    "QuicksightDataSourceCredentialsOutputReference",
    "QuicksightDataSourceParameters",
    "QuicksightDataSourceParametersAmazonElasticsearch",
    "QuicksightDataSourceParametersAmazonElasticsearchOutputReference",
    "QuicksightDataSourceParametersAthena",
    "QuicksightDataSourceParametersAthenaOutputReference",
    "QuicksightDataSourceParametersAurora",
    "QuicksightDataSourceParametersAuroraOutputReference",
    "QuicksightDataSourceParametersAuroraPostgresql",
    "QuicksightDataSourceParametersAuroraPostgresqlOutputReference",
    "QuicksightDataSourceParametersAwsIotAnalytics",
    "QuicksightDataSourceParametersAwsIotAnalyticsOutputReference",
    "QuicksightDataSourceParametersJira",
    "QuicksightDataSourceParametersJiraOutputReference",
    "QuicksightDataSourceParametersMariaDb",
    "QuicksightDataSourceParametersMariaDbOutputReference",
    "QuicksightDataSourceParametersMysql",
    "QuicksightDataSourceParametersMysqlOutputReference",
    "QuicksightDataSourceParametersOracle",
    "QuicksightDataSourceParametersOracleOutputReference",
    "QuicksightDataSourceParametersOutputReference",
    "QuicksightDataSourceParametersPostgresql",
    "QuicksightDataSourceParametersPostgresqlOutputReference",
    "QuicksightDataSourceParametersPresto",
    "QuicksightDataSourceParametersPrestoOutputReference",
    "QuicksightDataSourceParametersRds",
    "QuicksightDataSourceParametersRdsOutputReference",
    "QuicksightDataSourceParametersRedshift",
    "QuicksightDataSourceParametersRedshiftOutputReference",
    "QuicksightDataSourceParametersS3",
    "QuicksightDataSourceParametersS3ManifestFileLocation",
    "QuicksightDataSourceParametersS3ManifestFileLocationOutputReference",
    "QuicksightDataSourceParametersS3OutputReference",
    "QuicksightDataSourceParametersServiceNow",
    "QuicksightDataSourceParametersServiceNowOutputReference",
    "QuicksightDataSourceParametersSnowflake",
    "QuicksightDataSourceParametersSnowflakeOutputReference",
    "QuicksightDataSourceParametersSpark",
    "QuicksightDataSourceParametersSparkOutputReference",
    "QuicksightDataSourceParametersSqlServer",
    "QuicksightDataSourceParametersSqlServerOutputReference",
    "QuicksightDataSourceParametersTeradata",
    "QuicksightDataSourceParametersTeradataOutputReference",
    "QuicksightDataSourceParametersTwitter",
    "QuicksightDataSourceParametersTwitterOutputReference",
    "QuicksightDataSourcePermission",
    "QuicksightDataSourcePermissionList",
    "QuicksightDataSourcePermissionOutputReference",
    "QuicksightDataSourceSslProperties",
    "QuicksightDataSourceSslPropertiesOutputReference",
    "QuicksightDataSourceVpcConnectionProperties",
    "QuicksightDataSourceVpcConnectionPropertiesOutputReference",
]

publication.publish()

def _typecheckingstub__72e28790189a2c109b007044db61c5065ff546eaf12e7583c61ce7b167e3828f(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    data_source_id: builtins.str,
    name: builtins.str,
    parameters: typing.Union[QuicksightDataSourceParameters, typing.Dict[builtins.str, typing.Any]],
    type: builtins.str,
    aws_account_id: typing.Optional[builtins.str] = None,
    credentials: typing.Optional[typing.Union[QuicksightDataSourceCredentials, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    permission: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[QuicksightDataSourcePermission, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ssl_properties: typing.Optional[typing.Union[QuicksightDataSourceSslProperties, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    vpc_connection_properties: typing.Optional[typing.Union[QuicksightDataSourceVpcConnectionProperties, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__e7307edd673902d38b30b78d801b3aa97c64e8156cd37c4906d020e9e2d73789(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[QuicksightDataSourcePermission, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c14358f67eda0df9954ecc9a6267294487e7a749c27a049f03a08198cca15f9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9db6bf0f3c5778c3c7df0d2d9dfb1c8728428f37369059b2c8f866820cd1e510(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5aa3eab1e9bb20ae0a21a5a6c9b8290ec10d623ce625c063b320f8fb9e6b4a2c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c645f2e41ec39d8cab0e5e1ade2e9adc86571579f9cb97478ef78c29762bc34(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfbecee08b4c8730b868dda541b4f844a672c479d86f0ae6b2cf4e75ec7ed65c(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__752935c282dfa553be31a6d84f2d3713bfdfdffa7a75d1926cf02658fbd90722(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df276f91c053b598c29105e41b4fab65e195571f48372348b10f7f4337be20dd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a40668f6757d0e4e76b6b34c27e5f8701af0a89a869004f8b409fe443e9461c(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    data_source_id: builtins.str,
    name: builtins.str,
    parameters: typing.Union[QuicksightDataSourceParameters, typing.Dict[builtins.str, typing.Any]],
    type: builtins.str,
    aws_account_id: typing.Optional[builtins.str] = None,
    credentials: typing.Optional[typing.Union[QuicksightDataSourceCredentials, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    permission: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[QuicksightDataSourcePermission, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ssl_properties: typing.Optional[typing.Union[QuicksightDataSourceSslProperties, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    vpc_connection_properties: typing.Optional[typing.Union[QuicksightDataSourceVpcConnectionProperties, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5864b8f45e78d7d4bf5f4933fa63d6d1b3184a783d3b997e8d55a193441f57c3(
    *,
    copy_source_arn: typing.Optional[builtins.str] = None,
    credential_pair: typing.Optional[typing.Union[QuicksightDataSourceCredentialsCredentialPair, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e37f8582a190aa480fd8ddeac589f7ae4ed0030b172181f1234d1f240bc44792(
    *,
    password: builtins.str,
    username: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__887fb705aedbde41e9aa5d9e7ab7b1308b1ed62c7a1db7da4e56ac5b58b53267(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6cc1fb0b7a565b231ce8024dae61467515b6387b9708035a86d3071721eb4fc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13a37559f894599c20b760862c249ca22218d853d8fffa3480443e2177facb34(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aaf33667223d4bad574b9401d00b5a4805bdca91ce6eba4a473cc0046d38af84(
    value: typing.Optional[QuicksightDataSourceCredentialsCredentialPair],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__903f2a6bcd0985088fb8683510e4c39f0b9f96edf3fa86e7242f2c8402ac1068(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e08a8d0b802c31dd6b812f1f6350ec1860fe1c29f9758742e71baf930738a69(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__174161bfed92558d4765b1bc7fb581c508db2ed8ad12048ef49724f6172a2a95(
    value: typing.Optional[QuicksightDataSourceCredentials],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__925ab8f8230fb66c0e16b8767004032b2a21abdf01754cf6a98c55af5b0b49cc(
    *,
    amazon_elasticsearch: typing.Optional[typing.Union[QuicksightDataSourceParametersAmazonElasticsearch, typing.Dict[builtins.str, typing.Any]]] = None,
    athena: typing.Optional[typing.Union[QuicksightDataSourceParametersAthena, typing.Dict[builtins.str, typing.Any]]] = None,
    aurora: typing.Optional[typing.Union[QuicksightDataSourceParametersAurora, typing.Dict[builtins.str, typing.Any]]] = None,
    aurora_postgresql: typing.Optional[typing.Union[QuicksightDataSourceParametersAuroraPostgresql, typing.Dict[builtins.str, typing.Any]]] = None,
    aws_iot_analytics: typing.Optional[typing.Union[QuicksightDataSourceParametersAwsIotAnalytics, typing.Dict[builtins.str, typing.Any]]] = None,
    jira: typing.Optional[typing.Union[QuicksightDataSourceParametersJira, typing.Dict[builtins.str, typing.Any]]] = None,
    maria_db: typing.Optional[typing.Union[QuicksightDataSourceParametersMariaDb, typing.Dict[builtins.str, typing.Any]]] = None,
    mysql: typing.Optional[typing.Union[QuicksightDataSourceParametersMysql, typing.Dict[builtins.str, typing.Any]]] = None,
    oracle: typing.Optional[typing.Union[QuicksightDataSourceParametersOracle, typing.Dict[builtins.str, typing.Any]]] = None,
    postgresql: typing.Optional[typing.Union[QuicksightDataSourceParametersPostgresql, typing.Dict[builtins.str, typing.Any]]] = None,
    presto: typing.Optional[typing.Union[QuicksightDataSourceParametersPresto, typing.Dict[builtins.str, typing.Any]]] = None,
    rds: typing.Optional[typing.Union[QuicksightDataSourceParametersRds, typing.Dict[builtins.str, typing.Any]]] = None,
    redshift: typing.Optional[typing.Union[QuicksightDataSourceParametersRedshift, typing.Dict[builtins.str, typing.Any]]] = None,
    s3: typing.Optional[typing.Union[QuicksightDataSourceParametersS3, typing.Dict[builtins.str, typing.Any]]] = None,
    service_now: typing.Optional[typing.Union[QuicksightDataSourceParametersServiceNow, typing.Dict[builtins.str, typing.Any]]] = None,
    snowflake: typing.Optional[typing.Union[QuicksightDataSourceParametersSnowflake, typing.Dict[builtins.str, typing.Any]]] = None,
    spark: typing.Optional[typing.Union[QuicksightDataSourceParametersSpark, typing.Dict[builtins.str, typing.Any]]] = None,
    sql_server: typing.Optional[typing.Union[QuicksightDataSourceParametersSqlServer, typing.Dict[builtins.str, typing.Any]]] = None,
    teradata: typing.Optional[typing.Union[QuicksightDataSourceParametersTeradata, typing.Dict[builtins.str, typing.Any]]] = None,
    twitter: typing.Optional[typing.Union[QuicksightDataSourceParametersTwitter, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e2517cc485bcb7581b51f080f4133f80f336b16c02f7453ec6b7af8e3c29ec3(
    *,
    domain: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bc8e387c101c39804061d7816a8973c2008aaa41b10e020d5aebe236a403ed7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51c5c08acbd64d8053b10ea67851ae1ee2451af593e8730d540ed09adb1d58f7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6035852fd4c8c2213640fae1261be2a47358b3e17d18d48f57e123025a2bed64(
    value: typing.Optional[QuicksightDataSourceParametersAmazonElasticsearch],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe93641b80b55ddd24b379306f3a2d6211ef46d5a23a136226953824d0843bd8(
    *,
    work_group: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e7a1ef3f1984f55407c09fadecb0acef4482912c70dbc38f9cefc897e27f21a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__489319fe507cc2a84f57c89cb9941d0ce363302863130008262d621b9917aa65(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d0de4ff52f58cd9a4cbed490377ce0d171f0d0f4d7873647d97e07da13df5bf(
    value: typing.Optional[QuicksightDataSourceParametersAthena],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c82b4771e4ffacf3c65fb4a8822d55d1361706ed3f6d9f1a62c9804ed8324772(
    *,
    database: builtins.str,
    host: builtins.str,
    port: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16f1a4226b4425f75a0713df99c17555cdcd7beeebc683d881fc97ab45a4e57a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81fb029c5d53bb89ed9fec95f2bfeb82b04cf5b6904b97fe70e43842efd2c443(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c56e3cd3186c632f6b23d3cc2b4ea14614aacd92e40a484747731222db6ee77(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32801290b83f8c40215d4c2d0f2e79c9c841df92c9e217885f4c6821603c5392(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57fe3fc4a62fbff9e04cbc2db9f341b6afd2073bc0744cc965cade31b5e00557(
    value: typing.Optional[QuicksightDataSourceParametersAurora],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__936d6fadf7702fae63ecefaab868dd1451c0ef61f9152f66e024dce1ffabeb8c(
    *,
    database: builtins.str,
    host: builtins.str,
    port: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e4fa259c0da42ec1731d3538c89df88cbd6342009e6dfb79441739ddf0ac862(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30136dc3b3a16287ef52092de8df04ae232b6799b0872180f04e4a4612d5b474(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__054862547266c7a4f7248c51c22464fc57aab388222b8017ad2c6eb5e7c9f465(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e452798bd35b9859b9e1d9a280a545af4a4d739e9bc1d7d21becf57930a6ee74(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97f5d53dc69fe692e5277c9914c15ca27fb27dbaf31c7b26f19d434e551f125d(
    value: typing.Optional[QuicksightDataSourceParametersAuroraPostgresql],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da635401732a08064ae10f0da7d46861a69092dce05117387aa0545a653e4c38(
    *,
    data_set_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__400e34548984e41132d374a3abcf0513def0dce56518fe17565519565f9734fe(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae76ff275070d0a51ca7954323877ee252e54cf677d1328693b55d58c641b9a8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8ef553d3f942244ba224d37a5d129d654ba1118cb4fac01b54798d623008fe8(
    value: typing.Optional[QuicksightDataSourceParametersAwsIotAnalytics],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f5d8044730d4247663475164d616ab0e9ec98ab2105ae34620c7f4ea7e0b764(
    *,
    site_base_url: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b513ac64aa35e62588e347e14b4b9c5440b9e112e786ed7d39454eb733801de(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__513ba5a520c5dd7f099e1cd1ede6edade11df83872f5b55692098b86f305efb2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25a389b2c5b1c092f7a743debb30f6bf1abfb686061aaec3b4a9016f1503f81e(
    value: typing.Optional[QuicksightDataSourceParametersJira],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25f6a25c8d26db8cccc6d0a0a7750426cc302bbc0e70706dce736f0d5fcddaa1(
    *,
    database: builtins.str,
    host: builtins.str,
    port: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec519a22efdeb7c05cfc1f83d211568dfb2d59957580065b17581e2b0d62e55f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4335b39d4495a3ea74e563db9d4fb26a1ccc759e975814fbd7ffac2ac52209fb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf1ed3c0bb1731424b7068372653e9025319546580645f0b8e1a17e6a2526b74(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afed2ef271d785b445b9f0fa5ea9b311dc92e63c216ef4ef32e5d946b27107a3(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cd9510c1454bcd907a3485202518ca90617aa157be47cb6230e2dae5dffea86(
    value: typing.Optional[QuicksightDataSourceParametersMariaDb],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e06d73b9bdd3a865d2d2afddf174794e2601d2822b89766a394d72961015c662(
    *,
    database: builtins.str,
    host: builtins.str,
    port: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23f76f46eea15628e721a81df1406e8cebc4f357fa47bedda4c7e4b6c5df20cf(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e34a64b436f0fb6fb1acb078364814d208253346b487ff2ee3f9d1f2e4348f0e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f175e13e7616fff1d001d75ebe556b64de8df12763019188cea25b1f15f8b6f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9c6176639e17bf86dd08b1dc1032f3e30f050bbe830660a8e4848cec780bfb6(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce5e4ca2fa02cc9511aa3ddb758b7af6332e622c977dc6d334b90c8200797224(
    value: typing.Optional[QuicksightDataSourceParametersMysql],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__289a267a77d1484a96704835efb3fde5fc64638095d0428c8d2e1fd4e384ecfd(
    *,
    database: builtins.str,
    host: builtins.str,
    port: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1e0d5f370b3836884ca2bdfe705402e9d420086ffc6660a4e6a3092f7e13458(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d276032e00ce65679ad022ef71fef2f4659ac89940b615f0829ab989c512943(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9635ba4743c38c7928cb612a0b3f21c624c975101712e588fb1822a76c78c09e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c220bee505e3027846f3491ab891db33a725c4c337d06cae5f3c642d673b9234(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04ebe71fe160012cb664edc9581c928eb7587d20b16a745f45817a90f1f339ea(
    value: typing.Optional[QuicksightDataSourceParametersOracle],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d256e91e25c85f7677c1ee49c7dc1d187d2a3e9029b65a3f7b20b9dbe23b885a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8964d037d31c131064fd1a24ed9858103c0ee0513785cf015e523c07cb7730a7(
    value: typing.Optional[QuicksightDataSourceParameters],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c60a37250b6f168d915bffed76c5d6030e05c9a3c9a22ae2e5839943d90cf20(
    *,
    database: builtins.str,
    host: builtins.str,
    port: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eae803b0c3a881ea40e30ea52220d495c42bb7dd11730bdf2992054aa44fc9af(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8822e3eb6c083a364e2e408160e6e93d659c6430bfe66f737fb2baf3f27e274f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f2ebc3e5f05f3fa508da55bcce7ac9dea6578921d076def4a35a747ca09736b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aeab011955051f7528f0bd958d2e48b5ead4fd4436f113d902b6088f13e407b1(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ba7ecdd402716ff8ca4d3f8f75b0967551849b54a01086d35bfef7d24fd3005(
    value: typing.Optional[QuicksightDataSourceParametersPostgresql],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a275bbf8fc74883ab0feb0d072a30daf180644a04f1e0dd6ee5762efb76465da(
    *,
    catalog: builtins.str,
    host: builtins.str,
    port: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae45ef469f120e0d8e844cc0be047e6a1c9e2897d94483f96fd3507340d46bad(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d039332f8ea02ba4f7f03ca28ce8f9fcb84c7f1db33038a8547fc15a4e38519f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9557ddc7a0343351d051d28508a46690e0dc43f2083a7cb84558dc47aaee11d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3848a3e984b71598e5849f978549a8475b8cbcd8272d754029c183de20a6ddb6(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed2b36b955374de5ae6a17f946a961403ba001f87f0a94bf1a5130fcfab961b4(
    value: typing.Optional[QuicksightDataSourceParametersPresto],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__821b4385ff78925e4f11b2a2e17ec5fbb816d8248eac73e6dc2eb5efc5a87a52(
    *,
    database: builtins.str,
    instance_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ea1131f0327041e6d723d51ac8528a64f393883719a78bc9eced62cf38d9195(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74258ee5273afc332e64a034bd01fce0bb18b1b77f32e8370ebf5867ecfcec3d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2cd88ef8f3e73b6ec5ccbc4c1b03c7d273be389021a1b1cf4b96752e85aad70(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__913e2f204aa0afdc73fa1b1d0f39033ec568e43c45bc97ecb60d77901ad1311f(
    value: typing.Optional[QuicksightDataSourceParametersRds],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__377b5d266dd186abcd65e7d1abadf3541948a757048c5d9e0aba08cdc2ca84d0(
    *,
    database: builtins.str,
    cluster_id: typing.Optional[builtins.str] = None,
    host: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a32aaee60783b6a88201e39194e69f8b162be869e16c6064218fbc39706fce7d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8335a2c7f7b2526c9db081773b46003d3fa3a601a29444113340e8d988e8a956(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a1575689b936b026640f79474d06f52f4ee342988d8e5379c5d0662d59da8fd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c9ff4506191acdd22511429d64efa810ac75100f838c299d17265518016fe58(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9f391d98548c6848950b5115066ccb437d64a91169a94d5f3f1993e72202ba9(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0811a59927b0ac8a8d16a89c970525e52a790710cf50937334378f4ac7da3ae(
    value: typing.Optional[QuicksightDataSourceParametersRedshift],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0755232c53887364728ac31016244692fc32917e7eb8912eed08ec57ec65946(
    *,
    manifest_file_location: typing.Union[QuicksightDataSourceParametersS3ManifestFileLocation, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5aacf00da87a67d3cd11d576991c1ef410453ced31da3052098a21d7e866a07(
    *,
    bucket: builtins.str,
    key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b384ca77d02fb5cf7f7e71b0218a52cd088e1dbdceeb0c89a7029ce914fef963(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0d23cb40bd85aa0ce7f74a0ec2bc9f11e492c673783efd357beed35f92bf11a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c13505e741d27a34bf83a99de09119c3992a978d74cfc0cf7a1131111ea3c595(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3fdf552f1c71ce4f9587d28ecc170c594d7a62afbccebfd8f16f943eaaace18(
    value: typing.Optional[QuicksightDataSourceParametersS3ManifestFileLocation],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__564409363099b6c2c65063b6a3b873340233da669b21639fe75eeef59025da7a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fc9cd0b0a2b24d99f461372e847cecfd9c8539b2686fe9d242e188cd2f8b5d7(
    value: typing.Optional[QuicksightDataSourceParametersS3],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83ee293b07905cb493005a923f0985999aff6d8f7827ecb7d7281188ccc46966(
    *,
    site_base_url: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__224f48d3e59ed11679a859f8ed22ef12cffdf94c504884665896fe5f946c645d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91984e170c145e3110832a8f7cd651aa85e15eb4e9989eb9496dbcf783cd2c81(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecc8e130123885871512f4a0a1fec19b907f2194ae69a277b32841804f4a84f1(
    value: typing.Optional[QuicksightDataSourceParametersServiceNow],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1c9818258f2a13c9f331abc749e495c80765be0138f40a235139c07f10ffdf5(
    *,
    database: builtins.str,
    host: builtins.str,
    warehouse: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ade90c50de7a4f118a0a5c981157273812b58d4a7ccadbab9e908748b8f1313e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fa1ac12c58f2a54b6069336ea46ac60f3c95b4c0d86516e5f6631f52501f358(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__345fa1fbefd7c5a7c47b09e6c4187ac79ea32767b923bee8e9451207e7a436c5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cb49acb0bda4743b35800512378b0a88d37d3efbaeee22dd472ae6364c9139a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2871af9351fa38651301dfac42c30a0a11c73196ad414d75aa44656bc7fda7d(
    value: typing.Optional[QuicksightDataSourceParametersSnowflake],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfc4f932e247327e70c0aa168ac4cc1aa4c4194ddaa2815d274bd053bc56f6bf(
    *,
    host: builtins.str,
    port: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f854e3c3d34078b1f2ac17d694410dc11f476faa33563f3786db8c2530bc2f37(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e4b6d457c4b00a3e85f2d188d15ed42d9ce76509ee645ac7c4e6e41f9db85fa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e17b65aef720a707288cfaa37210f0488ea418d9753a879080889a5c0be1bae0(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7bc436077e9aa7af11c1198e8e0f746a0043197975e3301df9fa386c48b8f9a(
    value: typing.Optional[QuicksightDataSourceParametersSpark],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1aae51c0cf1ab4748d304e5756b7bfab63be5a0442da7221bfd0aba3acc5f8c2(
    *,
    database: builtins.str,
    host: builtins.str,
    port: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7417909729173f774eeb05dbb45c29b4f1508824e69ed237c50d56c7a265045(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25d5203fcdb5e0aa81c8f44a6890c88c19cba43ef625efea3b50914ef35ccc8c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__deb1f63256741eda6a8d93d1c074f46e837e5eb20cbc9d1f21efa2f0e3c25dce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6a4596394c7d15fd4f87e0e50b056a1591448883a453f26463c4b531094cbd2(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__028f82d2b862a64daee9f38b4c2dedc3b0426db6d83df28561211a53769ef3dd(
    value: typing.Optional[QuicksightDataSourceParametersSqlServer],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7321f53be6b7afe57a0a4a44730177d211084f4e021ae3d573bf5db48ba75f62(
    *,
    database: builtins.str,
    host: builtins.str,
    port: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__197f9567c1d2ef25651212f327bfcddf08a08b5d1a5c8ffb973143bb7f3927f8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__750d9471711335403c1a50389d468f3ac639fafe30c200a48c2f4b53c936e65e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53211a9094eeebf7897bcbf610fbf1317e7c970f007affcbdd4547beb9055d7b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__346f2d704df145df2d79b8fcf21f08d67171a4f06475260e284df484ff7c8afe(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__240a41babc16df609f27f888245c6fb9e205f0688173f7544ecbbaae4565fa39(
    value: typing.Optional[QuicksightDataSourceParametersTeradata],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0be6a17f5863fa16f49831b112972628e3aa2ef6556a6512ba7a118fdc5f4f0(
    *,
    max_rows: jsii.Number,
    query: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e1a12dac4ecc8ed7f65c375eb52786b1610dead0e1956fa19bb79b2278ab2ea(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2fc0111e1a34b9a189f024feedefc038e481d2d08c4f59f73be354d254ef235(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6adcce46c5bf147b69574610daee2b145b9488b704f578af2ab26b51e3aea3eb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e1f12c44aea2db0edf1fa4dcba6b78462eb9d926a271de61e34889ac5424d06(
    value: typing.Optional[QuicksightDataSourceParametersTwitter],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b803cac9313c3c70b91d8a2303a8c801408e7d6678b0a44c2b4912435de2473(
    *,
    actions: typing.Sequence[builtins.str],
    principal: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f142915611ab0bc25cd3fc30fd082e46e9bafd791d43f582250d1083bec76e7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c57989305627e366a27e47843cf145c311d61ce11bccd6e6151a4e51e4afc862(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aef130e1d28f76a88e5d2c3a4650e4820314eea1123d74bae0afecab48a97306(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__826708b544cd01593cb4be7c22a27ec73ee4fbd9d3d1ae97ac81d96145aed10c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33a27dd82a74a92648bdb5322e9ecdbf5c983b4b034a9f2a69988583afa3489e(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c773c6146fa1db88f14c1d7e8f4334d4ea171e75b8a0d75d444f2d5093c709ab(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[QuicksightDataSourcePermission]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44f9b6c05dc99a8d147ea53187f9d14d1ad543ab703db564b0463124611aab60(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abf83d92fa93efd5dc11a5dc23069176413b1e081bec30bafbd782eefa6643c6(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50a992bfe4725d1131fe5515b0db56aab0246b91ea379f4c2419fb2127439234(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4f78918b171029a13e6ba89aca4c00ecf0bc3bdcf55540513a912bf44d74cf2(
    value: typing.Optional[typing.Union[QuicksightDataSourcePermission, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f791c3d60fa6a5f9f23b589bc44de28a1b1717b1b99895ca408f58de29d0dc0a(
    *,
    disable_ssl: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24eee20839d1173aa574fb7f4d9ab8cf1485189902000ba0a2cb38964675e168(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b44f5545e138c468891ee24603e819d550ae590099797adb566ad2772a611a13(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00c64d9bcf755fb3320204b2cb969b6de05c98f700a55efb1d35aa7a6335897d(
    value: typing.Optional[QuicksightDataSourceSslProperties],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3785a15b60637d36496cd972f5b9b61b825da4e4d970fe6d168ed900048d6800(
    *,
    vpc_connection_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac47d16817fef8cdc4bac4059261e2d9db74c979d22d096109717e5dacaae9d7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__383de5c05363d05d7cbd2f400936397bc286f9da459976d16d63e664780b1d1c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0abbd00a62f2b369b19f028246ea25bd08528ab34c95cf23731aee472432ea8a(
    value: typing.Optional[QuicksightDataSourceVpcConnectionProperties],
) -> None:
    """Type checking stubs"""
    pass
