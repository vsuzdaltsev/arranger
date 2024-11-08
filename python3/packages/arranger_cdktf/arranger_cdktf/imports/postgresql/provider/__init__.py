'''
# `provider`

Refer to the Terraform Registory for docs: [`postgresql`](https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs).
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


class PostgresqlProvider(
    _cdktf_9a9027ec.TerraformProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="postgresql.provider.PostgresqlProvider",
):
    '''Represents a {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs postgresql}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        alias: typing.Optional[builtins.str] = None,
        aws_rds_iam_auth: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        aws_rds_iam_profile: typing.Optional[builtins.str] = None,
        aws_rds_iam_region: typing.Optional[builtins.str] = None,
        clientcert: typing.Optional[typing.Union["PostgresqlProviderClientcert", typing.Dict[builtins.str, typing.Any]]] = None,
        connect_timeout: typing.Optional[jsii.Number] = None,
        database: typing.Optional[builtins.str] = None,
        database_username: typing.Optional[builtins.str] = None,
        expected_version: typing.Optional[builtins.str] = None,
        host: typing.Optional[builtins.str] = None,
        max_connections: typing.Optional[jsii.Number] = None,
        password: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        scheme: typing.Optional[builtins.str] = None,
        sslmode: typing.Optional[builtins.str] = None,
        ssl_mode: typing.Optional[builtins.str] = None,
        sslrootcert: typing.Optional[builtins.str] = None,
        superuser: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs postgresql} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param alias: Alias name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#alias PostgresqlProvider#alias}
        :param aws_rds_iam_auth: Use rds_iam instead of password authentication (see: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.html). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#aws_rds_iam_auth PostgresqlProvider#aws_rds_iam_auth}
        :param aws_rds_iam_profile: AWS profile to use for IAM auth. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#aws_rds_iam_profile PostgresqlProvider#aws_rds_iam_profile}
        :param aws_rds_iam_region: AWS region to use for IAM auth. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#aws_rds_iam_region PostgresqlProvider#aws_rds_iam_region}
        :param clientcert: clientcert block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#clientcert PostgresqlProvider#clientcert}
        :param connect_timeout: Maximum wait for connection, in seconds. Zero or not specified means wait indefinitely. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#connect_timeout PostgresqlProvider#connect_timeout}
        :param database: The name of the database to connect to in order to conenct to (defaults to ``postgres``). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#database PostgresqlProvider#database}
        :param database_username: Database username associated to the connected user (for user name maps). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#database_username PostgresqlProvider#database_username}
        :param expected_version: Specify the expected version of PostgreSQL. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#expected_version PostgresqlProvider#expected_version}
        :param host: Name of PostgreSQL server address to connect to. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#host PostgresqlProvider#host}
        :param max_connections: Maximum number of connections to establish to the database. Zero means unlimited. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#max_connections PostgresqlProvider#max_connections}
        :param password: Password to be used if the PostgreSQL server demands password authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#password PostgresqlProvider#password}
        :param port: The PostgreSQL port number to connect to at the server host, or socket file name extension for Unix-domain connections. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#port PostgresqlProvider#port}
        :param scheme: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#scheme PostgresqlProvider#scheme}.
        :param sslmode: This option determines whether or with what priority a secure SSL TCP/IP connection will be negotiated with the PostgreSQL server. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#sslmode PostgresqlProvider#sslmode}
        :param ssl_mode: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#ssl_mode PostgresqlProvider#ssl_mode}.
        :param sslrootcert: The SSL server root certificate file path. The file must contain PEM encoded data. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#sslrootcert PostgresqlProvider#sslrootcert}
        :param superuser: Specify if the user to connect as is a Postgres superuser or not.If not, some feature might be disabled (e.g.: Refreshing state password from Postgres). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#superuser PostgresqlProvider#superuser}
        :param username: PostgreSQL user name to connect as. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#username PostgresqlProvider#username}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3126e5d844adf0ca29a4fb56e523a5fd4f66eddede8c1955acd80a64394a5ac4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = PostgresqlProviderConfig(
            alias=alias,
            aws_rds_iam_auth=aws_rds_iam_auth,
            aws_rds_iam_profile=aws_rds_iam_profile,
            aws_rds_iam_region=aws_rds_iam_region,
            clientcert=clientcert,
            connect_timeout=connect_timeout,
            database=database,
            database_username=database_username,
            expected_version=expected_version,
            host=host,
            max_connections=max_connections,
            password=password,
            port=port,
            scheme=scheme,
            sslmode=sslmode,
            ssl_mode=ssl_mode,
            sslrootcert=sslrootcert,
            superuser=superuser,
            username=username,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetAlias")
    def reset_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlias", []))

    @jsii.member(jsii_name="resetAwsRdsIamAuth")
    def reset_aws_rds_iam_auth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsRdsIamAuth", []))

    @jsii.member(jsii_name="resetAwsRdsIamProfile")
    def reset_aws_rds_iam_profile(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsRdsIamProfile", []))

    @jsii.member(jsii_name="resetAwsRdsIamRegion")
    def reset_aws_rds_iam_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsRdsIamRegion", []))

    @jsii.member(jsii_name="resetClientcert")
    def reset_clientcert(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientcert", []))

    @jsii.member(jsii_name="resetConnectTimeout")
    def reset_connect_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectTimeout", []))

    @jsii.member(jsii_name="resetDatabase")
    def reset_database(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatabase", []))

    @jsii.member(jsii_name="resetDatabaseUsername")
    def reset_database_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatabaseUsername", []))

    @jsii.member(jsii_name="resetExpectedVersion")
    def reset_expected_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpectedVersion", []))

    @jsii.member(jsii_name="resetHost")
    def reset_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHost", []))

    @jsii.member(jsii_name="resetMaxConnections")
    def reset_max_connections(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxConnections", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="resetScheme")
    def reset_scheme(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScheme", []))

    @jsii.member(jsii_name="resetSslmode")
    def reset_sslmode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSslmode", []))

    @jsii.member(jsii_name="resetSslMode")
    def reset_ssl_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSslMode", []))

    @jsii.member(jsii_name="resetSslrootcert")
    def reset_sslrootcert(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSslrootcert", []))

    @jsii.member(jsii_name="resetSuperuser")
    def reset_superuser(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSuperuser", []))

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="aliasInput")
    def alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aliasInput"))

    @builtins.property
    @jsii.member(jsii_name="awsRdsIamAuthInput")
    def aws_rds_iam_auth_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "awsRdsIamAuthInput"))

    @builtins.property
    @jsii.member(jsii_name="awsRdsIamProfileInput")
    def aws_rds_iam_profile_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "awsRdsIamProfileInput"))

    @builtins.property
    @jsii.member(jsii_name="awsRdsIamRegionInput")
    def aws_rds_iam_region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "awsRdsIamRegionInput"))

    @builtins.property
    @jsii.member(jsii_name="clientcertInput")
    def clientcert_input(self) -> typing.Optional["PostgresqlProviderClientcert"]:
        return typing.cast(typing.Optional["PostgresqlProviderClientcert"], jsii.get(self, "clientcertInput"))

    @builtins.property
    @jsii.member(jsii_name="connectTimeoutInput")
    def connect_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "connectTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseInput")
    def database_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseUsernameInput")
    def database_username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseUsernameInput"))

    @builtins.property
    @jsii.member(jsii_name="expectedVersionInput")
    def expected_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expectedVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="maxConnectionsInput")
    def max_connections_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxConnectionsInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="schemeInput")
    def scheme_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemeInput"))

    @builtins.property
    @jsii.member(jsii_name="sslmodeInput")
    def sslmode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sslmodeInput"))

    @builtins.property
    @jsii.member(jsii_name="sslModeInput")
    def ssl_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sslModeInput"))

    @builtins.property
    @jsii.member(jsii_name="sslrootcertInput")
    def sslrootcert_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sslrootcertInput"))

    @builtins.property
    @jsii.member(jsii_name="superuserInput")
    def superuser_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "superuserInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f3dfa4c957c323811e91e6424515481bf99cdd0a80eb0dcd326af9d815617ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="awsRdsIamAuth")
    def aws_rds_iam_auth(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "awsRdsIamAuth"))

    @aws_rds_iam_auth.setter
    def aws_rds_iam_auth(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e7064f8d15ea1ff82286d48d4894d87871e3d9d8b94ad6dd60dd686d66ce012)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRdsIamAuth", value)

    @builtins.property
    @jsii.member(jsii_name="awsRdsIamProfile")
    def aws_rds_iam_profile(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "awsRdsIamProfile"))

    @aws_rds_iam_profile.setter
    def aws_rds_iam_profile(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6775f66dd6312a6838b82839f9ab69cd2816e4ffef29d2074c74e40cb3169d53)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRdsIamProfile", value)

    @builtins.property
    @jsii.member(jsii_name="awsRdsIamRegion")
    def aws_rds_iam_region(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "awsRdsIamRegion"))

    @aws_rds_iam_region.setter
    def aws_rds_iam_region(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6895323f511b2a4d59c2bb5a3c9ad62b74c0d5437f57bf15a3643f257dd92c13)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRdsIamRegion", value)

    @builtins.property
    @jsii.member(jsii_name="clientcert")
    def clientcert(self) -> typing.Optional["PostgresqlProviderClientcert"]:
        return typing.cast(typing.Optional["PostgresqlProviderClientcert"], jsii.get(self, "clientcert"))

    @clientcert.setter
    def clientcert(
        self,
        value: typing.Optional["PostgresqlProviderClientcert"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75c1fae4de70ee2a0f9755d2dbc29b0b4414b406edc1abebfb3bd0432d37bd38)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientcert", value)

    @builtins.property
    @jsii.member(jsii_name="connectTimeout")
    def connect_timeout(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "connectTimeout"))

    @connect_timeout.setter
    def connect_timeout(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a374daa44be31fc2d738a2c0ec484965a93db204c0bb3493a52d0672c0e36918)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="database")
    def database(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "database"))

    @database.setter
    def database(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3714e1136e8008c1a9b0b44d0505e8a8c77fad412aa5ddc1c4e6f04472b7743)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "database", value)

    @builtins.property
    @jsii.member(jsii_name="databaseUsername")
    def database_username(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseUsername"))

    @database_username.setter
    def database_username(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e9d49a02cca0b81d739562bf024891cf6ba91012e4f7d46c818e5acf24965df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseUsername", value)

    @builtins.property
    @jsii.member(jsii_name="expectedVersion")
    def expected_version(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expectedVersion"))

    @expected_version.setter
    def expected_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0abc27874e6be915da9f8c0d91512a513194f10c51563c9d2c29e70da34f485e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expectedVersion", value)

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "host"))

    @host.setter
    def host(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d567081b44040cfb790b89999dbc189f171ad8f46c64d2686e772eb7de93b5f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="maxConnections")
    def max_connections(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxConnections"))

    @max_connections.setter
    def max_connections(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b289485a3fda19e4dcf5822ea2270261e4f7c6025c2cee393a0a7be5be9551a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConnections", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "password"))

    @password.setter
    def password(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88ed5fcb5a84bdb6f8b416ebe5c9a16e37d504dab60727c7f71e7c0c34226d94)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "port"))

    @port.setter
    def port(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f24ac66e7c97dbb48217a10aff68c14e691c446e0f89325023ae1c22309596a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="scheme")
    def scheme(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scheme"))

    @scheme.setter
    def scheme(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4abf825572fd652aec14063196a23d065cefda07cdd8a5b1469b3d58e314fa69)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheme", value)

    @builtins.property
    @jsii.member(jsii_name="sslmode")
    def sslmode(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sslmode"))

    @sslmode.setter
    def sslmode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__300e86fb9f5d33c61d8b067ed33a30cf9596e5e41e54d99c7fd4298e90261613)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sslmode", value)

    @builtins.property
    @jsii.member(jsii_name="sslMode")
    def ssl_mode(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sslMode"))

    @ssl_mode.setter
    def ssl_mode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__422efa72f00b6286c2f7a652cd37b733525735dfa05fc0b9940647a3b6355a0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sslMode", value)

    @builtins.property
    @jsii.member(jsii_name="sslrootcert")
    def sslrootcert(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sslrootcert"))

    @sslrootcert.setter
    def sslrootcert(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f2eb727deb092e855c18289a569a30b3e9c667c3bf03497e25a1f525fb41ee7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sslrootcert", value)

    @builtins.property
    @jsii.member(jsii_name="superuser")
    def superuser(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "superuser"))

    @superuser.setter
    def superuser(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__edb8a7f00d5c076266c5210afaebf0c3a94022557daba9a9130139547d3a47c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "superuser", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "username"))

    @username.setter
    def username(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49ef85144568bbdca8c30804f82fe4d9cd00d90e0446d1588311b0fc2e4ae220)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)


@jsii.data_type(
    jsii_type="postgresql.provider.PostgresqlProviderClientcert",
    jsii_struct_bases=[],
    name_mapping={"cert": "cert", "key": "key"},
)
class PostgresqlProviderClientcert:
    def __init__(self, *, cert: builtins.str, key: builtins.str) -> None:
        '''
        :param cert: The SSL client certificate file path. The file must contain PEM encoded data. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#cert PostgresqlProvider#cert}
        :param key: The SSL client certificate private key file path. The file must contain PEM encoded data. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#key PostgresqlProvider#key}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e59540b4be149b20803bb498895084207461094b99907e7632fcac7cfcaf6e50)
            check_type(argname="argument cert", value=cert, expected_type=type_hints["cert"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cert": cert,
            "key": key,
        }

    @builtins.property
    def cert(self) -> builtins.str:
        '''The SSL client certificate file path. The file must contain PEM encoded data.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#cert PostgresqlProvider#cert}
        '''
        result = self._values.get("cert")
        assert result is not None, "Required property 'cert' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key(self) -> builtins.str:
        '''The SSL client certificate private key file path. The file must contain PEM encoded data.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#key PostgresqlProvider#key}
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PostgresqlProviderClientcert(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="postgresql.provider.PostgresqlProviderConfig",
    jsii_struct_bases=[],
    name_mapping={
        "alias": "alias",
        "aws_rds_iam_auth": "awsRdsIamAuth",
        "aws_rds_iam_profile": "awsRdsIamProfile",
        "aws_rds_iam_region": "awsRdsIamRegion",
        "clientcert": "clientcert",
        "connect_timeout": "connectTimeout",
        "database": "database",
        "database_username": "databaseUsername",
        "expected_version": "expectedVersion",
        "host": "host",
        "max_connections": "maxConnections",
        "password": "password",
        "port": "port",
        "scheme": "scheme",
        "sslmode": "sslmode",
        "ssl_mode": "sslMode",
        "sslrootcert": "sslrootcert",
        "superuser": "superuser",
        "username": "username",
    },
)
class PostgresqlProviderConfig:
    def __init__(
        self,
        *,
        alias: typing.Optional[builtins.str] = None,
        aws_rds_iam_auth: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        aws_rds_iam_profile: typing.Optional[builtins.str] = None,
        aws_rds_iam_region: typing.Optional[builtins.str] = None,
        clientcert: typing.Optional[typing.Union[PostgresqlProviderClientcert, typing.Dict[builtins.str, typing.Any]]] = None,
        connect_timeout: typing.Optional[jsii.Number] = None,
        database: typing.Optional[builtins.str] = None,
        database_username: typing.Optional[builtins.str] = None,
        expected_version: typing.Optional[builtins.str] = None,
        host: typing.Optional[builtins.str] = None,
        max_connections: typing.Optional[jsii.Number] = None,
        password: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        scheme: typing.Optional[builtins.str] = None,
        sslmode: typing.Optional[builtins.str] = None,
        ssl_mode: typing.Optional[builtins.str] = None,
        sslrootcert: typing.Optional[builtins.str] = None,
        superuser: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param alias: Alias name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#alias PostgresqlProvider#alias}
        :param aws_rds_iam_auth: Use rds_iam instead of password authentication (see: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.html). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#aws_rds_iam_auth PostgresqlProvider#aws_rds_iam_auth}
        :param aws_rds_iam_profile: AWS profile to use for IAM auth. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#aws_rds_iam_profile PostgresqlProvider#aws_rds_iam_profile}
        :param aws_rds_iam_region: AWS region to use for IAM auth. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#aws_rds_iam_region PostgresqlProvider#aws_rds_iam_region}
        :param clientcert: clientcert block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#clientcert PostgresqlProvider#clientcert}
        :param connect_timeout: Maximum wait for connection, in seconds. Zero or not specified means wait indefinitely. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#connect_timeout PostgresqlProvider#connect_timeout}
        :param database: The name of the database to connect to in order to conenct to (defaults to ``postgres``). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#database PostgresqlProvider#database}
        :param database_username: Database username associated to the connected user (for user name maps). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#database_username PostgresqlProvider#database_username}
        :param expected_version: Specify the expected version of PostgreSQL. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#expected_version PostgresqlProvider#expected_version}
        :param host: Name of PostgreSQL server address to connect to. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#host PostgresqlProvider#host}
        :param max_connections: Maximum number of connections to establish to the database. Zero means unlimited. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#max_connections PostgresqlProvider#max_connections}
        :param password: Password to be used if the PostgreSQL server demands password authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#password PostgresqlProvider#password}
        :param port: The PostgreSQL port number to connect to at the server host, or socket file name extension for Unix-domain connections. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#port PostgresqlProvider#port}
        :param scheme: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#scheme PostgresqlProvider#scheme}.
        :param sslmode: This option determines whether or with what priority a secure SSL TCP/IP connection will be negotiated with the PostgreSQL server. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#sslmode PostgresqlProvider#sslmode}
        :param ssl_mode: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#ssl_mode PostgresqlProvider#ssl_mode}.
        :param sslrootcert: The SSL server root certificate file path. The file must contain PEM encoded data. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#sslrootcert PostgresqlProvider#sslrootcert}
        :param superuser: Specify if the user to connect as is a Postgres superuser or not.If not, some feature might be disabled (e.g.: Refreshing state password from Postgres). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#superuser PostgresqlProvider#superuser}
        :param username: PostgreSQL user name to connect as. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#username PostgresqlProvider#username}
        '''
        if isinstance(clientcert, dict):
            clientcert = PostgresqlProviderClientcert(**clientcert)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c154d164537c6f3abcc1e8383fe6885177ee212d3fb344d13f88c36090418229)
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument aws_rds_iam_auth", value=aws_rds_iam_auth, expected_type=type_hints["aws_rds_iam_auth"])
            check_type(argname="argument aws_rds_iam_profile", value=aws_rds_iam_profile, expected_type=type_hints["aws_rds_iam_profile"])
            check_type(argname="argument aws_rds_iam_region", value=aws_rds_iam_region, expected_type=type_hints["aws_rds_iam_region"])
            check_type(argname="argument clientcert", value=clientcert, expected_type=type_hints["clientcert"])
            check_type(argname="argument connect_timeout", value=connect_timeout, expected_type=type_hints["connect_timeout"])
            check_type(argname="argument database", value=database, expected_type=type_hints["database"])
            check_type(argname="argument database_username", value=database_username, expected_type=type_hints["database_username"])
            check_type(argname="argument expected_version", value=expected_version, expected_type=type_hints["expected_version"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument max_connections", value=max_connections, expected_type=type_hints["max_connections"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument scheme", value=scheme, expected_type=type_hints["scheme"])
            check_type(argname="argument sslmode", value=sslmode, expected_type=type_hints["sslmode"])
            check_type(argname="argument ssl_mode", value=ssl_mode, expected_type=type_hints["ssl_mode"])
            check_type(argname="argument sslrootcert", value=sslrootcert, expected_type=type_hints["sslrootcert"])
            check_type(argname="argument superuser", value=superuser, expected_type=type_hints["superuser"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if alias is not None:
            self._values["alias"] = alias
        if aws_rds_iam_auth is not None:
            self._values["aws_rds_iam_auth"] = aws_rds_iam_auth
        if aws_rds_iam_profile is not None:
            self._values["aws_rds_iam_profile"] = aws_rds_iam_profile
        if aws_rds_iam_region is not None:
            self._values["aws_rds_iam_region"] = aws_rds_iam_region
        if clientcert is not None:
            self._values["clientcert"] = clientcert
        if connect_timeout is not None:
            self._values["connect_timeout"] = connect_timeout
        if database is not None:
            self._values["database"] = database
        if database_username is not None:
            self._values["database_username"] = database_username
        if expected_version is not None:
            self._values["expected_version"] = expected_version
        if host is not None:
            self._values["host"] = host
        if max_connections is not None:
            self._values["max_connections"] = max_connections
        if password is not None:
            self._values["password"] = password
        if port is not None:
            self._values["port"] = port
        if scheme is not None:
            self._values["scheme"] = scheme
        if sslmode is not None:
            self._values["sslmode"] = sslmode
        if ssl_mode is not None:
            self._values["ssl_mode"] = ssl_mode
        if sslrootcert is not None:
            self._values["sslrootcert"] = sslrootcert
        if superuser is not None:
            self._values["superuser"] = superuser
        if username is not None:
            self._values["username"] = username

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''Alias name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#alias PostgresqlProvider#alias}
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aws_rds_iam_auth(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Use rds_iam instead of password authentication (see: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.html).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#aws_rds_iam_auth PostgresqlProvider#aws_rds_iam_auth}
        '''
        result = self._values.get("aws_rds_iam_auth")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def aws_rds_iam_profile(self) -> typing.Optional[builtins.str]:
        '''AWS profile to use for IAM auth.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#aws_rds_iam_profile PostgresqlProvider#aws_rds_iam_profile}
        '''
        result = self._values.get("aws_rds_iam_profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aws_rds_iam_region(self) -> typing.Optional[builtins.str]:
        '''AWS region to use for IAM auth.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#aws_rds_iam_region PostgresqlProvider#aws_rds_iam_region}
        '''
        result = self._values.get("aws_rds_iam_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def clientcert(self) -> typing.Optional[PostgresqlProviderClientcert]:
        '''clientcert block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#clientcert PostgresqlProvider#clientcert}
        '''
        result = self._values.get("clientcert")
        return typing.cast(typing.Optional[PostgresqlProviderClientcert], result)

    @builtins.property
    def connect_timeout(self) -> typing.Optional[jsii.Number]:
        '''Maximum wait for connection, in seconds. Zero or not specified means wait indefinitely.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#connect_timeout PostgresqlProvider#connect_timeout}
        '''
        result = self._values.get("connect_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def database(self) -> typing.Optional[builtins.str]:
        '''The name of the database to connect to in order to conenct to (defaults to ``postgres``).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#database PostgresqlProvider#database}
        '''
        result = self._values.get("database")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def database_username(self) -> typing.Optional[builtins.str]:
        '''Database username associated to the connected user (for user name maps).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#database_username PostgresqlProvider#database_username}
        '''
        result = self._values.get("database_username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def expected_version(self) -> typing.Optional[builtins.str]:
        '''Specify the expected version of PostgreSQL.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#expected_version PostgresqlProvider#expected_version}
        '''
        result = self._values.get("expected_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        '''Name of PostgreSQL server address to connect to.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#host PostgresqlProvider#host}
        '''
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_connections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of connections to establish to the database. Zero means unlimited.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#max_connections PostgresqlProvider#max_connections}
        '''
        result = self._values.get("max_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Password to be used if the PostgreSQL server demands password authentication.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#password PostgresqlProvider#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''The PostgreSQL port number to connect to at the server host, or socket file name extension for Unix-domain connections.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#port PostgresqlProvider#port}
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def scheme(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#scheme PostgresqlProvider#scheme}.'''
        result = self._values.get("scheme")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sslmode(self) -> typing.Optional[builtins.str]:
        '''This option determines whether or with what priority a secure SSL TCP/IP connection will be negotiated with the PostgreSQL server.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#sslmode PostgresqlProvider#sslmode}
        '''
        result = self._values.get("sslmode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssl_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#ssl_mode PostgresqlProvider#ssl_mode}.'''
        result = self._values.get("ssl_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sslrootcert(self) -> typing.Optional[builtins.str]:
        '''The SSL server root certificate file path. The file must contain PEM encoded data.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#sslrootcert PostgresqlProvider#sslrootcert}
        '''
        result = self._values.get("sslrootcert")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def superuser(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Specify if the user to connect as is a Postgres superuser or not.If not, some feature might be disabled (e.g.: Refreshing state password from Postgres).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#superuser PostgresqlProvider#superuser}
        '''
        result = self._values.get("superuser")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''PostgreSQL user name to connect as.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cyrilgdn/postgresql/1.19.0/docs#username PostgresqlProvider#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PostgresqlProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "PostgresqlProvider",
    "PostgresqlProviderClientcert",
    "PostgresqlProviderConfig",
]

publication.publish()

def _typecheckingstub__3126e5d844adf0ca29a4fb56e523a5fd4f66eddede8c1955acd80a64394a5ac4(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    alias: typing.Optional[builtins.str] = None,
    aws_rds_iam_auth: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    aws_rds_iam_profile: typing.Optional[builtins.str] = None,
    aws_rds_iam_region: typing.Optional[builtins.str] = None,
    clientcert: typing.Optional[typing.Union[PostgresqlProviderClientcert, typing.Dict[builtins.str, typing.Any]]] = None,
    connect_timeout: typing.Optional[jsii.Number] = None,
    database: typing.Optional[builtins.str] = None,
    database_username: typing.Optional[builtins.str] = None,
    expected_version: typing.Optional[builtins.str] = None,
    host: typing.Optional[builtins.str] = None,
    max_connections: typing.Optional[jsii.Number] = None,
    password: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    scheme: typing.Optional[builtins.str] = None,
    sslmode: typing.Optional[builtins.str] = None,
    ssl_mode: typing.Optional[builtins.str] = None,
    sslrootcert: typing.Optional[builtins.str] = None,
    superuser: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f3dfa4c957c323811e91e6424515481bf99cdd0a80eb0dcd326af9d815617ef(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e7064f8d15ea1ff82286d48d4894d87871e3d9d8b94ad6dd60dd686d66ce012(
    value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6775f66dd6312a6838b82839f9ab69cd2816e4ffef29d2074c74e40cb3169d53(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6895323f511b2a4d59c2bb5a3c9ad62b74c0d5437f57bf15a3643f257dd92c13(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75c1fae4de70ee2a0f9755d2dbc29b0b4414b406edc1abebfb3bd0432d37bd38(
    value: typing.Optional[PostgresqlProviderClientcert],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a374daa44be31fc2d738a2c0ec484965a93db204c0bb3493a52d0672c0e36918(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3714e1136e8008c1a9b0b44d0505e8a8c77fad412aa5ddc1c4e6f04472b7743(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e9d49a02cca0b81d739562bf024891cf6ba91012e4f7d46c818e5acf24965df(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0abc27874e6be915da9f8c0d91512a513194f10c51563c9d2c29e70da34f485e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d567081b44040cfb790b89999dbc189f171ad8f46c64d2686e772eb7de93b5f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b289485a3fda19e4dcf5822ea2270261e4f7c6025c2cee393a0a7be5be9551a(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88ed5fcb5a84bdb6f8b416ebe5c9a16e37d504dab60727c7f71e7c0c34226d94(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f24ac66e7c97dbb48217a10aff68c14e691c446e0f89325023ae1c22309596a8(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4abf825572fd652aec14063196a23d065cefda07cdd8a5b1469b3d58e314fa69(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__300e86fb9f5d33c61d8b067ed33a30cf9596e5e41e54d99c7fd4298e90261613(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__422efa72f00b6286c2f7a652cd37b733525735dfa05fc0b9940647a3b6355a0c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f2eb727deb092e855c18289a569a30b3e9c667c3bf03497e25a1f525fb41ee7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__edb8a7f00d5c076266c5210afaebf0c3a94022557daba9a9130139547d3a47c9(
    value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49ef85144568bbdca8c30804f82fe4d9cd00d90e0446d1588311b0fc2e4ae220(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e59540b4be149b20803bb498895084207461094b99907e7632fcac7cfcaf6e50(
    *,
    cert: builtins.str,
    key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c154d164537c6f3abcc1e8383fe6885177ee212d3fb344d13f88c36090418229(
    *,
    alias: typing.Optional[builtins.str] = None,
    aws_rds_iam_auth: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    aws_rds_iam_profile: typing.Optional[builtins.str] = None,
    aws_rds_iam_region: typing.Optional[builtins.str] = None,
    clientcert: typing.Optional[typing.Union[PostgresqlProviderClientcert, typing.Dict[builtins.str, typing.Any]]] = None,
    connect_timeout: typing.Optional[jsii.Number] = None,
    database: typing.Optional[builtins.str] = None,
    database_username: typing.Optional[builtins.str] = None,
    expected_version: typing.Optional[builtins.str] = None,
    host: typing.Optional[builtins.str] = None,
    max_connections: typing.Optional[jsii.Number] = None,
    password: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    scheme: typing.Optional[builtins.str] = None,
    sslmode: typing.Optional[builtins.str] = None,
    ssl_mode: typing.Optional[builtins.str] = None,
    sslrootcert: typing.Optional[builtins.str] = None,
    superuser: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
