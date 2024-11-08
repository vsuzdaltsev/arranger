'''
# `aws_glue_crawler`

Refer to the Terraform Registory for docs: [`aws_glue_crawler`](https://www.terraform.io/docs/providers/aws/r/glue_crawler).
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


class GlueCrawler(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.glueCrawler.GlueCrawler",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler aws_glue_crawler}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        database_name: builtins.str,
        name: builtins.str,
        role: builtins.str,
        catalog_target: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GlueCrawlerCatalogTarget", typing.Dict[builtins.str, typing.Any]]]]] = None,
        classifiers: typing.Optional[typing.Sequence[builtins.str]] = None,
        configuration: typing.Optional[builtins.str] = None,
        delta_target: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GlueCrawlerDeltaTarget", typing.Dict[builtins.str, typing.Any]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        dynamodb_target: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GlueCrawlerDynamodbTarget", typing.Dict[builtins.str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        jdbc_target: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GlueCrawlerJdbcTarget", typing.Dict[builtins.str, typing.Any]]]]] = None,
        lake_formation_configuration: typing.Optional[typing.Union["GlueCrawlerLakeFormationConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        lineage_configuration: typing.Optional[typing.Union["GlueCrawlerLineageConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        mongodb_target: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GlueCrawlerMongodbTarget", typing.Dict[builtins.str, typing.Any]]]]] = None,
        recrawl_policy: typing.Optional[typing.Union["GlueCrawlerRecrawlPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        s3_target: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GlueCrawlerS3Target", typing.Dict[builtins.str, typing.Any]]]]] = None,
        schedule: typing.Optional[builtins.str] = None,
        schema_change_policy: typing.Optional[typing.Union["GlueCrawlerSchemaChangePolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        security_configuration: typing.Optional[builtins.str] = None,
        table_prefix: typing.Optional[builtins.str] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler aws_glue_crawler} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#database_name GlueCrawler#database_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#name GlueCrawler#name}.
        :param role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#role GlueCrawler#role}.
        :param catalog_target: catalog_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#catalog_target GlueCrawler#catalog_target}
        :param classifiers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#classifiers GlueCrawler#classifiers}.
        :param configuration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#configuration GlueCrawler#configuration}.
        :param delta_target: delta_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#delta_target GlueCrawler#delta_target}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#description GlueCrawler#description}.
        :param dynamodb_target: dynamodb_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#dynamodb_target GlueCrawler#dynamodb_target}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#id GlueCrawler#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param jdbc_target: jdbc_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#jdbc_target GlueCrawler#jdbc_target}
        :param lake_formation_configuration: lake_formation_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#lake_formation_configuration GlueCrawler#lake_formation_configuration}
        :param lineage_configuration: lineage_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#lineage_configuration GlueCrawler#lineage_configuration}
        :param mongodb_target: mongodb_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#mongodb_target GlueCrawler#mongodb_target}
        :param recrawl_policy: recrawl_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#recrawl_policy GlueCrawler#recrawl_policy}
        :param s3_target: s3_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#s3_target GlueCrawler#s3_target}
        :param schedule: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#schedule GlueCrawler#schedule}.
        :param schema_change_policy: schema_change_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#schema_change_policy GlueCrawler#schema_change_policy}
        :param security_configuration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#security_configuration GlueCrawler#security_configuration}.
        :param table_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#table_prefix GlueCrawler#table_prefix}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#tags GlueCrawler#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#tags_all GlueCrawler#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce19d43400f8f2c340b8537e1962b744e7ab3ad3ad1020c9b53218ef2eefd69e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GlueCrawlerConfig(
            database_name=database_name,
            name=name,
            role=role,
            catalog_target=catalog_target,
            classifiers=classifiers,
            configuration=configuration,
            delta_target=delta_target,
            description=description,
            dynamodb_target=dynamodb_target,
            id=id,
            jdbc_target=jdbc_target,
            lake_formation_configuration=lake_formation_configuration,
            lineage_configuration=lineage_configuration,
            mongodb_target=mongodb_target,
            recrawl_policy=recrawl_policy,
            s3_target=s3_target,
            schedule=schedule,
            schema_change_policy=schema_change_policy,
            security_configuration=security_configuration,
            table_prefix=table_prefix,
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

    @jsii.member(jsii_name="putCatalogTarget")
    def put_catalog_target(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GlueCrawlerCatalogTarget", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7081833d391d3260585ef0b6fdac5528d2c1f728bb79b7ff956f9543308f131)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCatalogTarget", [value]))

    @jsii.member(jsii_name="putDeltaTarget")
    def put_delta_target(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GlueCrawlerDeltaTarget", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce99ce69110a761f2dcf77be0096035117a2a0c77cf89678d835897a32ba7b4d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDeltaTarget", [value]))

    @jsii.member(jsii_name="putDynamodbTarget")
    def put_dynamodb_target(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GlueCrawlerDynamodbTarget", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ed48fd33b0e73cce502ca07fa393095585ed0555394b88058ed008e794e2813)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDynamodbTarget", [value]))

    @jsii.member(jsii_name="putJdbcTarget")
    def put_jdbc_target(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GlueCrawlerJdbcTarget", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42d2b5bf68d492d19ac3f11a58fcc005df9a673b4ff35400612f8274f1f7662c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putJdbcTarget", [value]))

    @jsii.member(jsii_name="putLakeFormationConfiguration")
    def put_lake_formation_configuration(
        self,
        *,
        account_id: typing.Optional[builtins.str] = None,
        use_lake_formation_credentials: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#account_id GlueCrawler#account_id}.
        :param use_lake_formation_credentials: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#use_lake_formation_credentials GlueCrawler#use_lake_formation_credentials}.
        '''
        value = GlueCrawlerLakeFormationConfiguration(
            account_id=account_id,
            use_lake_formation_credentials=use_lake_formation_credentials,
        )

        return typing.cast(None, jsii.invoke(self, "putLakeFormationConfiguration", [value]))

    @jsii.member(jsii_name="putLineageConfiguration")
    def put_lineage_configuration(
        self,
        *,
        crawler_lineage_settings: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param crawler_lineage_settings: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#crawler_lineage_settings GlueCrawler#crawler_lineage_settings}.
        '''
        value = GlueCrawlerLineageConfiguration(
            crawler_lineage_settings=crawler_lineage_settings
        )

        return typing.cast(None, jsii.invoke(self, "putLineageConfiguration", [value]))

    @jsii.member(jsii_name="putMongodbTarget")
    def put_mongodb_target(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GlueCrawlerMongodbTarget", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4fa9487fe92a745d5d4504ba066bb31fc6812f6243c9c79e8b97c0729edcc1a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMongodbTarget", [value]))

    @jsii.member(jsii_name="putRecrawlPolicy")
    def put_recrawl_policy(
        self,
        *,
        recrawl_behavior: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param recrawl_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#recrawl_behavior GlueCrawler#recrawl_behavior}.
        '''
        value = GlueCrawlerRecrawlPolicy(recrawl_behavior=recrawl_behavior)

        return typing.cast(None, jsii.invoke(self, "putRecrawlPolicy", [value]))

    @jsii.member(jsii_name="putS3Target")
    def put_s3_target(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GlueCrawlerS3Target", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce2ea91807e3ab5ea57e2bf732974447c0f12f7e8a17a37c2a3bc716f1d307d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putS3Target", [value]))

    @jsii.member(jsii_name="putSchemaChangePolicy")
    def put_schema_change_policy(
        self,
        *,
        delete_behavior: typing.Optional[builtins.str] = None,
        update_behavior: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param delete_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#delete_behavior GlueCrawler#delete_behavior}.
        :param update_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#update_behavior GlueCrawler#update_behavior}.
        '''
        value = GlueCrawlerSchemaChangePolicy(
            delete_behavior=delete_behavior, update_behavior=update_behavior
        )

        return typing.cast(None, jsii.invoke(self, "putSchemaChangePolicy", [value]))

    @jsii.member(jsii_name="resetCatalogTarget")
    def reset_catalog_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCatalogTarget", []))

    @jsii.member(jsii_name="resetClassifiers")
    def reset_classifiers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClassifiers", []))

    @jsii.member(jsii_name="resetConfiguration")
    def reset_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfiguration", []))

    @jsii.member(jsii_name="resetDeltaTarget")
    def reset_delta_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeltaTarget", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDynamodbTarget")
    def reset_dynamodb_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDynamodbTarget", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetJdbcTarget")
    def reset_jdbc_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJdbcTarget", []))

    @jsii.member(jsii_name="resetLakeFormationConfiguration")
    def reset_lake_formation_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLakeFormationConfiguration", []))

    @jsii.member(jsii_name="resetLineageConfiguration")
    def reset_lineage_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLineageConfiguration", []))

    @jsii.member(jsii_name="resetMongodbTarget")
    def reset_mongodb_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMongodbTarget", []))

    @jsii.member(jsii_name="resetRecrawlPolicy")
    def reset_recrawl_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecrawlPolicy", []))

    @jsii.member(jsii_name="resetS3Target")
    def reset_s3_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3Target", []))

    @jsii.member(jsii_name="resetSchedule")
    def reset_schedule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchedule", []))

    @jsii.member(jsii_name="resetSchemaChangePolicy")
    def reset_schema_change_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchemaChangePolicy", []))

    @jsii.member(jsii_name="resetSecurityConfiguration")
    def reset_security_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityConfiguration", []))

    @jsii.member(jsii_name="resetTablePrefix")
    def reset_table_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTablePrefix", []))

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
    @jsii.member(jsii_name="catalogTarget")
    def catalog_target(self) -> "GlueCrawlerCatalogTargetList":
        return typing.cast("GlueCrawlerCatalogTargetList", jsii.get(self, "catalogTarget"))

    @builtins.property
    @jsii.member(jsii_name="deltaTarget")
    def delta_target(self) -> "GlueCrawlerDeltaTargetList":
        return typing.cast("GlueCrawlerDeltaTargetList", jsii.get(self, "deltaTarget"))

    @builtins.property
    @jsii.member(jsii_name="dynamodbTarget")
    def dynamodb_target(self) -> "GlueCrawlerDynamodbTargetList":
        return typing.cast("GlueCrawlerDynamodbTargetList", jsii.get(self, "dynamodbTarget"))

    @builtins.property
    @jsii.member(jsii_name="jdbcTarget")
    def jdbc_target(self) -> "GlueCrawlerJdbcTargetList":
        return typing.cast("GlueCrawlerJdbcTargetList", jsii.get(self, "jdbcTarget"))

    @builtins.property
    @jsii.member(jsii_name="lakeFormationConfiguration")
    def lake_formation_configuration(
        self,
    ) -> "GlueCrawlerLakeFormationConfigurationOutputReference":
        return typing.cast("GlueCrawlerLakeFormationConfigurationOutputReference", jsii.get(self, "lakeFormationConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="lineageConfiguration")
    def lineage_configuration(self) -> "GlueCrawlerLineageConfigurationOutputReference":
        return typing.cast("GlueCrawlerLineageConfigurationOutputReference", jsii.get(self, "lineageConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="mongodbTarget")
    def mongodb_target(self) -> "GlueCrawlerMongodbTargetList":
        return typing.cast("GlueCrawlerMongodbTargetList", jsii.get(self, "mongodbTarget"))

    @builtins.property
    @jsii.member(jsii_name="recrawlPolicy")
    def recrawl_policy(self) -> "GlueCrawlerRecrawlPolicyOutputReference":
        return typing.cast("GlueCrawlerRecrawlPolicyOutputReference", jsii.get(self, "recrawlPolicy"))

    @builtins.property
    @jsii.member(jsii_name="s3Target")
    def s3_target(self) -> "GlueCrawlerS3TargetList":
        return typing.cast("GlueCrawlerS3TargetList", jsii.get(self, "s3Target"))

    @builtins.property
    @jsii.member(jsii_name="schemaChangePolicy")
    def schema_change_policy(self) -> "GlueCrawlerSchemaChangePolicyOutputReference":
        return typing.cast("GlueCrawlerSchemaChangePolicyOutputReference", jsii.get(self, "schemaChangePolicy"))

    @builtins.property
    @jsii.member(jsii_name="catalogTargetInput")
    def catalog_target_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GlueCrawlerCatalogTarget"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GlueCrawlerCatalogTarget"]]], jsii.get(self, "catalogTargetInput"))

    @builtins.property
    @jsii.member(jsii_name="classifiersInput")
    def classifiers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "classifiersInput"))

    @builtins.property
    @jsii.member(jsii_name="configurationInput")
    def configuration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configurationInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseNameInput")
    def database_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseNameInput"))

    @builtins.property
    @jsii.member(jsii_name="deltaTargetInput")
    def delta_target_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GlueCrawlerDeltaTarget"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GlueCrawlerDeltaTarget"]]], jsii.get(self, "deltaTargetInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="dynamodbTargetInput")
    def dynamodb_target_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GlueCrawlerDynamodbTarget"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GlueCrawlerDynamodbTarget"]]], jsii.get(self, "dynamodbTargetInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="jdbcTargetInput")
    def jdbc_target_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GlueCrawlerJdbcTarget"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GlueCrawlerJdbcTarget"]]], jsii.get(self, "jdbcTargetInput"))

    @builtins.property
    @jsii.member(jsii_name="lakeFormationConfigurationInput")
    def lake_formation_configuration_input(
        self,
    ) -> typing.Optional["GlueCrawlerLakeFormationConfiguration"]:
        return typing.cast(typing.Optional["GlueCrawlerLakeFormationConfiguration"], jsii.get(self, "lakeFormationConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="lineageConfigurationInput")
    def lineage_configuration_input(
        self,
    ) -> typing.Optional["GlueCrawlerLineageConfiguration"]:
        return typing.cast(typing.Optional["GlueCrawlerLineageConfiguration"], jsii.get(self, "lineageConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="mongodbTargetInput")
    def mongodb_target_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GlueCrawlerMongodbTarget"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GlueCrawlerMongodbTarget"]]], jsii.get(self, "mongodbTargetInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="recrawlPolicyInput")
    def recrawl_policy_input(self) -> typing.Optional["GlueCrawlerRecrawlPolicy"]:
        return typing.cast(typing.Optional["GlueCrawlerRecrawlPolicy"], jsii.get(self, "recrawlPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="roleInput")
    def role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleInput"))

    @builtins.property
    @jsii.member(jsii_name="s3TargetInput")
    def s3_target_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GlueCrawlerS3Target"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GlueCrawlerS3Target"]]], jsii.get(self, "s3TargetInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduleInput")
    def schedule_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scheduleInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaChangePolicyInput")
    def schema_change_policy_input(
        self,
    ) -> typing.Optional["GlueCrawlerSchemaChangePolicy"]:
        return typing.cast(typing.Optional["GlueCrawlerSchemaChangePolicy"], jsii.get(self, "schemaChangePolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="securityConfigurationInput")
    def security_configuration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "securityConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="tablePrefixInput")
    def table_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tablePrefixInput"))

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
    @jsii.member(jsii_name="classifiers")
    def classifiers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "classifiers"))

    @classifiers.setter
    def classifiers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89545a88025c74ef184be49a1fbdb4f70d77520ca265573cc2e681ec7c8f4f4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "classifiers", value)

    @builtins.property
    @jsii.member(jsii_name="configuration")
    def configuration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "configuration"))

    @configuration.setter
    def configuration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28efc36cbab9e6879bc71f335d9ff87f94b927a9e16d7164013d65d7627c7610)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configuration", value)

    @builtins.property
    @jsii.member(jsii_name="databaseName")
    def database_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseName"))

    @database_name.setter
    def database_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da7e0eacef9c4c6560a8a349b56f1dc1519ad8e7965253b803530005fbb6d7d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseName", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e799792aa1e17016090eb7e7dfe3e74c9b4e3d235577286e24c91bf978725d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36cee85f7b881cd40881952f2e1d0472f960b65a500bb905cc923aaedfea17df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1385c671a92e9e0ec06cf636e957676aa3a167c1dc11204fce2d66c62a6c1d68)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "role"))

    @role.setter
    def role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ebc0dea20a029efeb1a4e862ff421cfc2feae27ae13e9c7963aca2242273c66)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "role", value)

    @builtins.property
    @jsii.member(jsii_name="schedule")
    def schedule(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schedule"))

    @schedule.setter
    def schedule(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f44e77768243d8de9f640d4fb5849d53c234b530bc8ff10da176541c5748db22)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schedule", value)

    @builtins.property
    @jsii.member(jsii_name="securityConfiguration")
    def security_configuration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "securityConfiguration"))

    @security_configuration.setter
    def security_configuration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e34483ecf993a0d672c6a59a19ab35f109558032e8f330f5b1276827bd904de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="tablePrefix")
    def table_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tablePrefix"))

    @table_prefix.setter
    def table_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9076732b52fa008945ac5d4a0ef1bd09e1b21093e53a157e2bbfb97265030083)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tablePrefix", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ab8adabfacef54b18f09be9b95a2e1825c0e070d73ad3c1d8d3c30e0298290e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb4e5f831c836b91c19925098ce14d66be3c7583e0ba73e8ea3ae5d3da78b5b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.glueCrawler.GlueCrawlerCatalogTarget",
    jsii_struct_bases=[],
    name_mapping={
        "database_name": "databaseName",
        "tables": "tables",
        "connection_name": "connectionName",
        "dlq_event_queue_arn": "dlqEventQueueArn",
        "event_queue_arn": "eventQueueArn",
    },
)
class GlueCrawlerCatalogTarget:
    def __init__(
        self,
        *,
        database_name: builtins.str,
        tables: typing.Sequence[builtins.str],
        connection_name: typing.Optional[builtins.str] = None,
        dlq_event_queue_arn: typing.Optional[builtins.str] = None,
        event_queue_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#database_name GlueCrawler#database_name}.
        :param tables: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#tables GlueCrawler#tables}.
        :param connection_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#connection_name GlueCrawler#connection_name}.
        :param dlq_event_queue_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#dlq_event_queue_arn GlueCrawler#dlq_event_queue_arn}.
        :param event_queue_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#event_queue_arn GlueCrawler#event_queue_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65d5a23fadffa9e10cac18e70d639c95394e890e074946687cbea7413e89cef1)
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument tables", value=tables, expected_type=type_hints["tables"])
            check_type(argname="argument connection_name", value=connection_name, expected_type=type_hints["connection_name"])
            check_type(argname="argument dlq_event_queue_arn", value=dlq_event_queue_arn, expected_type=type_hints["dlq_event_queue_arn"])
            check_type(argname="argument event_queue_arn", value=event_queue_arn, expected_type=type_hints["event_queue_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "database_name": database_name,
            "tables": tables,
        }
        if connection_name is not None:
            self._values["connection_name"] = connection_name
        if dlq_event_queue_arn is not None:
            self._values["dlq_event_queue_arn"] = dlq_event_queue_arn
        if event_queue_arn is not None:
            self._values["event_queue_arn"] = event_queue_arn

    @builtins.property
    def database_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#database_name GlueCrawler#database_name}.'''
        result = self._values.get("database_name")
        assert result is not None, "Required property 'database_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tables(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#tables GlueCrawler#tables}.'''
        result = self._values.get("tables")
        assert result is not None, "Required property 'tables' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def connection_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#connection_name GlueCrawler#connection_name}.'''
        result = self._values.get("connection_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dlq_event_queue_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#dlq_event_queue_arn GlueCrawler#dlq_event_queue_arn}.'''
        result = self._values.get("dlq_event_queue_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def event_queue_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#event_queue_arn GlueCrawler#event_queue_arn}.'''
        result = self._values.get("event_queue_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueCrawlerCatalogTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GlueCrawlerCatalogTargetList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.glueCrawler.GlueCrawlerCatalogTargetList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f316ad702459abd417897f1ddd561d72aa06de3a5c41ee8c255aa8c828b6fad1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "GlueCrawlerCatalogTargetOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b31edb056def6b5204ce8178aceb8a2575fe2c249ba5c2bc8a896a4ea4bd997b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GlueCrawlerCatalogTargetOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b62041ad69ba9fb854fbfe54f80855188f42840a037597b56c54e0542ff8170)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d9f4d615dadf1da014cb66ff4f551bfa00501f76d357cdff863ef83cdb5b626c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d415738c529ebd8597701338788892e1bb3d80da2b1bd290be35c061e9c17b94)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GlueCrawlerCatalogTarget]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GlueCrawlerCatalogTarget]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GlueCrawlerCatalogTarget]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cdac4b09b22b96c88029a515cdeaace1f1f3e8ef29d12f36ef76358b2c1f386)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GlueCrawlerCatalogTargetOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.glueCrawler.GlueCrawlerCatalogTargetOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__dd2ed339c1a5ce60da6faf1c3859114ab1db39ca09f8aaf0512e094e9e6b48f8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetConnectionName")
    def reset_connection_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionName", []))

    @jsii.member(jsii_name="resetDlqEventQueueArn")
    def reset_dlq_event_queue_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDlqEventQueueArn", []))

    @jsii.member(jsii_name="resetEventQueueArn")
    def reset_event_queue_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventQueueArn", []))

    @builtins.property
    @jsii.member(jsii_name="connectionNameInput")
    def connection_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionNameInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseNameInput")
    def database_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseNameInput"))

    @builtins.property
    @jsii.member(jsii_name="dlqEventQueueArnInput")
    def dlq_event_queue_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dlqEventQueueArnInput"))

    @builtins.property
    @jsii.member(jsii_name="eventQueueArnInput")
    def event_queue_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventQueueArnInput"))

    @builtins.property
    @jsii.member(jsii_name="tablesInput")
    def tables_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tablesInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionName")
    def connection_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionName"))

    @connection_name.setter
    def connection_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c733f6f764d2a94defafa3778162ec226babb04779dcd9b0564555e50d28d919)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionName", value)

    @builtins.property
    @jsii.member(jsii_name="databaseName")
    def database_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseName"))

    @database_name.setter
    def database_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d3a2342c19224d0d6e83303489f2d8d6f034463c43075b95418362bb80e4f59)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseName", value)

    @builtins.property
    @jsii.member(jsii_name="dlqEventQueueArn")
    def dlq_event_queue_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dlqEventQueueArn"))

    @dlq_event_queue_arn.setter
    def dlq_event_queue_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8be76ebce2b5f30e132064944289a6ffaf04deca3fc00c2f85dceccd1219a50e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dlqEventQueueArn", value)

    @builtins.property
    @jsii.member(jsii_name="eventQueueArn")
    def event_queue_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventQueueArn"))

    @event_queue_arn.setter
    def event_queue_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43fe746f6c06833b9a66500b0bcec32bfeb57b6b013cbc451d6f5695d6f70cb5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventQueueArn", value)

    @builtins.property
    @jsii.member(jsii_name="tables")
    def tables(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tables"))

    @tables.setter
    def tables(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d6cc4bea36083ba4af369019c53289c744fcc8b41c26e9f4affed33f9aebeda)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tables", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GlueCrawlerCatalogTarget, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GlueCrawlerCatalogTarget, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GlueCrawlerCatalogTarget, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae60bb75a6f4b3f2c1a9ee89b6db5768c8f32a80ca8c7781750a08decd2bc569)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.glueCrawler.GlueCrawlerConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "database_name": "databaseName",
        "name": "name",
        "role": "role",
        "catalog_target": "catalogTarget",
        "classifiers": "classifiers",
        "configuration": "configuration",
        "delta_target": "deltaTarget",
        "description": "description",
        "dynamodb_target": "dynamodbTarget",
        "id": "id",
        "jdbc_target": "jdbcTarget",
        "lake_formation_configuration": "lakeFormationConfiguration",
        "lineage_configuration": "lineageConfiguration",
        "mongodb_target": "mongodbTarget",
        "recrawl_policy": "recrawlPolicy",
        "s3_target": "s3Target",
        "schedule": "schedule",
        "schema_change_policy": "schemaChangePolicy",
        "security_configuration": "securityConfiguration",
        "table_prefix": "tablePrefix",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class GlueCrawlerConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        database_name: builtins.str,
        name: builtins.str,
        role: builtins.str,
        catalog_target: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GlueCrawlerCatalogTarget, typing.Dict[builtins.str, typing.Any]]]]] = None,
        classifiers: typing.Optional[typing.Sequence[builtins.str]] = None,
        configuration: typing.Optional[builtins.str] = None,
        delta_target: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GlueCrawlerDeltaTarget", typing.Dict[builtins.str, typing.Any]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        dynamodb_target: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GlueCrawlerDynamodbTarget", typing.Dict[builtins.str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        jdbc_target: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GlueCrawlerJdbcTarget", typing.Dict[builtins.str, typing.Any]]]]] = None,
        lake_formation_configuration: typing.Optional[typing.Union["GlueCrawlerLakeFormationConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        lineage_configuration: typing.Optional[typing.Union["GlueCrawlerLineageConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        mongodb_target: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GlueCrawlerMongodbTarget", typing.Dict[builtins.str, typing.Any]]]]] = None,
        recrawl_policy: typing.Optional[typing.Union["GlueCrawlerRecrawlPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        s3_target: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GlueCrawlerS3Target", typing.Dict[builtins.str, typing.Any]]]]] = None,
        schedule: typing.Optional[builtins.str] = None,
        schema_change_policy: typing.Optional[typing.Union["GlueCrawlerSchemaChangePolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        security_configuration: typing.Optional[builtins.str] = None,
        table_prefix: typing.Optional[builtins.str] = None,
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
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#database_name GlueCrawler#database_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#name GlueCrawler#name}.
        :param role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#role GlueCrawler#role}.
        :param catalog_target: catalog_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#catalog_target GlueCrawler#catalog_target}
        :param classifiers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#classifiers GlueCrawler#classifiers}.
        :param configuration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#configuration GlueCrawler#configuration}.
        :param delta_target: delta_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#delta_target GlueCrawler#delta_target}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#description GlueCrawler#description}.
        :param dynamodb_target: dynamodb_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#dynamodb_target GlueCrawler#dynamodb_target}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#id GlueCrawler#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param jdbc_target: jdbc_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#jdbc_target GlueCrawler#jdbc_target}
        :param lake_formation_configuration: lake_formation_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#lake_formation_configuration GlueCrawler#lake_formation_configuration}
        :param lineage_configuration: lineage_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#lineage_configuration GlueCrawler#lineage_configuration}
        :param mongodb_target: mongodb_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#mongodb_target GlueCrawler#mongodb_target}
        :param recrawl_policy: recrawl_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#recrawl_policy GlueCrawler#recrawl_policy}
        :param s3_target: s3_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#s3_target GlueCrawler#s3_target}
        :param schedule: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#schedule GlueCrawler#schedule}.
        :param schema_change_policy: schema_change_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#schema_change_policy GlueCrawler#schema_change_policy}
        :param security_configuration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#security_configuration GlueCrawler#security_configuration}.
        :param table_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#table_prefix GlueCrawler#table_prefix}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#tags GlueCrawler#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#tags_all GlueCrawler#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(lake_formation_configuration, dict):
            lake_formation_configuration = GlueCrawlerLakeFormationConfiguration(**lake_formation_configuration)
        if isinstance(lineage_configuration, dict):
            lineage_configuration = GlueCrawlerLineageConfiguration(**lineage_configuration)
        if isinstance(recrawl_policy, dict):
            recrawl_policy = GlueCrawlerRecrawlPolicy(**recrawl_policy)
        if isinstance(schema_change_policy, dict):
            schema_change_policy = GlueCrawlerSchemaChangePolicy(**schema_change_policy)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c2aad4d2e353612ebcdaf468d1f92fb5ae948341f7770501fdae277d968ca58)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument catalog_target", value=catalog_target, expected_type=type_hints["catalog_target"])
            check_type(argname="argument classifiers", value=classifiers, expected_type=type_hints["classifiers"])
            check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
            check_type(argname="argument delta_target", value=delta_target, expected_type=type_hints["delta_target"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument dynamodb_target", value=dynamodb_target, expected_type=type_hints["dynamodb_target"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument jdbc_target", value=jdbc_target, expected_type=type_hints["jdbc_target"])
            check_type(argname="argument lake_formation_configuration", value=lake_formation_configuration, expected_type=type_hints["lake_formation_configuration"])
            check_type(argname="argument lineage_configuration", value=lineage_configuration, expected_type=type_hints["lineage_configuration"])
            check_type(argname="argument mongodb_target", value=mongodb_target, expected_type=type_hints["mongodb_target"])
            check_type(argname="argument recrawl_policy", value=recrawl_policy, expected_type=type_hints["recrawl_policy"])
            check_type(argname="argument s3_target", value=s3_target, expected_type=type_hints["s3_target"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            check_type(argname="argument schema_change_policy", value=schema_change_policy, expected_type=type_hints["schema_change_policy"])
            check_type(argname="argument security_configuration", value=security_configuration, expected_type=type_hints["security_configuration"])
            check_type(argname="argument table_prefix", value=table_prefix, expected_type=type_hints["table_prefix"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "database_name": database_name,
            "name": name,
            "role": role,
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
        if catalog_target is not None:
            self._values["catalog_target"] = catalog_target
        if classifiers is not None:
            self._values["classifiers"] = classifiers
        if configuration is not None:
            self._values["configuration"] = configuration
        if delta_target is not None:
            self._values["delta_target"] = delta_target
        if description is not None:
            self._values["description"] = description
        if dynamodb_target is not None:
            self._values["dynamodb_target"] = dynamodb_target
        if id is not None:
            self._values["id"] = id
        if jdbc_target is not None:
            self._values["jdbc_target"] = jdbc_target
        if lake_formation_configuration is not None:
            self._values["lake_formation_configuration"] = lake_formation_configuration
        if lineage_configuration is not None:
            self._values["lineage_configuration"] = lineage_configuration
        if mongodb_target is not None:
            self._values["mongodb_target"] = mongodb_target
        if recrawl_policy is not None:
            self._values["recrawl_policy"] = recrawl_policy
        if s3_target is not None:
            self._values["s3_target"] = s3_target
        if schedule is not None:
            self._values["schedule"] = schedule
        if schema_change_policy is not None:
            self._values["schema_change_policy"] = schema_change_policy
        if security_configuration is not None:
            self._values["security_configuration"] = security_configuration
        if table_prefix is not None:
            self._values["table_prefix"] = table_prefix
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
    def database_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#database_name GlueCrawler#database_name}.'''
        result = self._values.get("database_name")
        assert result is not None, "Required property 'database_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#name GlueCrawler#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#role GlueCrawler#role}.'''
        result = self._values.get("role")
        assert result is not None, "Required property 'role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def catalog_target(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GlueCrawlerCatalogTarget]]]:
        '''catalog_target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#catalog_target GlueCrawler#catalog_target}
        '''
        result = self._values.get("catalog_target")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GlueCrawlerCatalogTarget]]], result)

    @builtins.property
    def classifiers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#classifiers GlueCrawler#classifiers}.'''
        result = self._values.get("classifiers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def configuration(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#configuration GlueCrawler#configuration}.'''
        result = self._values.get("configuration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delta_target(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GlueCrawlerDeltaTarget"]]]:
        '''delta_target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#delta_target GlueCrawler#delta_target}
        '''
        result = self._values.get("delta_target")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GlueCrawlerDeltaTarget"]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#description GlueCrawler#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dynamodb_target(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GlueCrawlerDynamodbTarget"]]]:
        '''dynamodb_target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#dynamodb_target GlueCrawler#dynamodb_target}
        '''
        result = self._values.get("dynamodb_target")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GlueCrawlerDynamodbTarget"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#id GlueCrawler#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def jdbc_target(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GlueCrawlerJdbcTarget"]]]:
        '''jdbc_target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#jdbc_target GlueCrawler#jdbc_target}
        '''
        result = self._values.get("jdbc_target")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GlueCrawlerJdbcTarget"]]], result)

    @builtins.property
    def lake_formation_configuration(
        self,
    ) -> typing.Optional["GlueCrawlerLakeFormationConfiguration"]:
        '''lake_formation_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#lake_formation_configuration GlueCrawler#lake_formation_configuration}
        '''
        result = self._values.get("lake_formation_configuration")
        return typing.cast(typing.Optional["GlueCrawlerLakeFormationConfiguration"], result)

    @builtins.property
    def lineage_configuration(
        self,
    ) -> typing.Optional["GlueCrawlerLineageConfiguration"]:
        '''lineage_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#lineage_configuration GlueCrawler#lineage_configuration}
        '''
        result = self._values.get("lineage_configuration")
        return typing.cast(typing.Optional["GlueCrawlerLineageConfiguration"], result)

    @builtins.property
    def mongodb_target(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GlueCrawlerMongodbTarget"]]]:
        '''mongodb_target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#mongodb_target GlueCrawler#mongodb_target}
        '''
        result = self._values.get("mongodb_target")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GlueCrawlerMongodbTarget"]]], result)

    @builtins.property
    def recrawl_policy(self) -> typing.Optional["GlueCrawlerRecrawlPolicy"]:
        '''recrawl_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#recrawl_policy GlueCrawler#recrawl_policy}
        '''
        result = self._values.get("recrawl_policy")
        return typing.cast(typing.Optional["GlueCrawlerRecrawlPolicy"], result)

    @builtins.property
    def s3_target(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GlueCrawlerS3Target"]]]:
        '''s3_target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#s3_target GlueCrawler#s3_target}
        '''
        result = self._values.get("s3_target")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GlueCrawlerS3Target"]]], result)

    @builtins.property
    def schedule(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#schedule GlueCrawler#schedule}.'''
        result = self._values.get("schedule")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schema_change_policy(self) -> typing.Optional["GlueCrawlerSchemaChangePolicy"]:
        '''schema_change_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#schema_change_policy GlueCrawler#schema_change_policy}
        '''
        result = self._values.get("schema_change_policy")
        return typing.cast(typing.Optional["GlueCrawlerSchemaChangePolicy"], result)

    @builtins.property
    def security_configuration(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#security_configuration GlueCrawler#security_configuration}.'''
        result = self._values.get("security_configuration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def table_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#table_prefix GlueCrawler#table_prefix}.'''
        result = self._values.get("table_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#tags GlueCrawler#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#tags_all GlueCrawler#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueCrawlerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.glueCrawler.GlueCrawlerDeltaTarget",
    jsii_struct_bases=[],
    name_mapping={
        "delta_tables": "deltaTables",
        "write_manifest": "writeManifest",
        "connection_name": "connectionName",
    },
)
class GlueCrawlerDeltaTarget:
    def __init__(
        self,
        *,
        delta_tables: typing.Sequence[builtins.str],
        write_manifest: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        connection_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param delta_tables: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#delta_tables GlueCrawler#delta_tables}.
        :param write_manifest: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#write_manifest GlueCrawler#write_manifest}.
        :param connection_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#connection_name GlueCrawler#connection_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60a1c43df90bd8f9ca084605db64a508ef2b43ccbce1c46304e96ef0102d5bd3)
            check_type(argname="argument delta_tables", value=delta_tables, expected_type=type_hints["delta_tables"])
            check_type(argname="argument write_manifest", value=write_manifest, expected_type=type_hints["write_manifest"])
            check_type(argname="argument connection_name", value=connection_name, expected_type=type_hints["connection_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "delta_tables": delta_tables,
            "write_manifest": write_manifest,
        }
        if connection_name is not None:
            self._values["connection_name"] = connection_name

    @builtins.property
    def delta_tables(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#delta_tables GlueCrawler#delta_tables}.'''
        result = self._values.get("delta_tables")
        assert result is not None, "Required property 'delta_tables' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def write_manifest(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#write_manifest GlueCrawler#write_manifest}.'''
        result = self._values.get("write_manifest")
        assert result is not None, "Required property 'write_manifest' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def connection_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#connection_name GlueCrawler#connection_name}.'''
        result = self._values.get("connection_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueCrawlerDeltaTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GlueCrawlerDeltaTargetList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.glueCrawler.GlueCrawlerDeltaTargetList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__89dfa48ff6e1a512dff2cceee925e7017c671c615f0788b05e8afcfc954eaf3c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "GlueCrawlerDeltaTargetOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90338d3d8ae86e31f69e0c807e0f6816d0c698db14ec7a7178f83fa9daca555b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GlueCrawlerDeltaTargetOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8780503df898d39d73477b121cbd4c71a1d957bd30cfb2b4eb6212a52b8b4298)
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
            type_hints = typing.get_type_hints(_typecheckingstub__370fc096c4eb6686eaaf8a5351bba00528afe45daa8fb5bf9c3b7b4c083b952c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f659f9615d4723ec2bafa326ba6d1f178fa19fd8530ebeb0b8154e3dd131930f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GlueCrawlerDeltaTarget]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GlueCrawlerDeltaTarget]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GlueCrawlerDeltaTarget]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__915b41cc15de5e951e222fe4ca1a9853ff41634fafed735bbabf23abbdb97485)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GlueCrawlerDeltaTargetOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.glueCrawler.GlueCrawlerDeltaTargetOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__418d8bc8bd295aae896fd2da1efdf2f2c983be8b79eeebe0837c03e2ee1c2ea5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetConnectionName")
    def reset_connection_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionName", []))

    @builtins.property
    @jsii.member(jsii_name="connectionNameInput")
    def connection_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionNameInput"))

    @builtins.property
    @jsii.member(jsii_name="deltaTablesInput")
    def delta_tables_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "deltaTablesInput"))

    @builtins.property
    @jsii.member(jsii_name="writeManifestInput")
    def write_manifest_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "writeManifestInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionName")
    def connection_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionName"))

    @connection_name.setter
    def connection_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d459c07fe7cccb18e7649ba749a0ec6f5c0e406df8c6fc8b16a8b2966907fc99)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionName", value)

    @builtins.property
    @jsii.member(jsii_name="deltaTables")
    def delta_tables(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "deltaTables"))

    @delta_tables.setter
    def delta_tables(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9788a4a64224c101052e9ba2f9be9e71c8d9ee45fb394786bb119923b612e15)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deltaTables", value)

    @builtins.property
    @jsii.member(jsii_name="writeManifest")
    def write_manifest(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "writeManifest"))

    @write_manifest.setter
    def write_manifest(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4acd8d098039fcb2ae0e90cc4a438069f937f6e26c437d2531e1297b973195ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "writeManifest", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GlueCrawlerDeltaTarget, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GlueCrawlerDeltaTarget, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GlueCrawlerDeltaTarget, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85edcc2f2fb925fa63d4f541beeb366d6a82b6318d2fb02e4d687da8fd2e5119)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.glueCrawler.GlueCrawlerDynamodbTarget",
    jsii_struct_bases=[],
    name_mapping={"path": "path", "scan_all": "scanAll", "scan_rate": "scanRate"},
)
class GlueCrawlerDynamodbTarget:
    def __init__(
        self,
        *,
        path: builtins.str,
        scan_all: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        scan_rate: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#path GlueCrawler#path}.
        :param scan_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#scan_all GlueCrawler#scan_all}.
        :param scan_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#scan_rate GlueCrawler#scan_rate}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31c22ee5235267ce4618620966d316aaaf6ff4c20feeb863ae878b9e288b3b77)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument scan_all", value=scan_all, expected_type=type_hints["scan_all"])
            check_type(argname="argument scan_rate", value=scan_rate, expected_type=type_hints["scan_rate"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "path": path,
        }
        if scan_all is not None:
            self._values["scan_all"] = scan_all
        if scan_rate is not None:
            self._values["scan_rate"] = scan_rate

    @builtins.property
    def path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#path GlueCrawler#path}.'''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def scan_all(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#scan_all GlueCrawler#scan_all}.'''
        result = self._values.get("scan_all")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def scan_rate(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#scan_rate GlueCrawler#scan_rate}.'''
        result = self._values.get("scan_rate")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueCrawlerDynamodbTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GlueCrawlerDynamodbTargetList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.glueCrawler.GlueCrawlerDynamodbTargetList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c7415f8adb83846fb6e5df60c234294a37cc2329c4b5574dfd3e9ec68adbd04e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "GlueCrawlerDynamodbTargetOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b61186d6494d888df7bcc672f28404357e151ce149fef138e7d1b13f5bc712a9)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GlueCrawlerDynamodbTargetOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d1c46506911d088bfe633ea74a0d99afd76b8a8a8d12064f980edda55a979f8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__32ae6d53aff7fd156ff9a6fe6faf02935bbfb84b1308119a7215b9a2b6fddeae)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b358001f8e6871665d7e79d219b0eab525c71492ed604467174e0aa80dcdb06e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GlueCrawlerDynamodbTarget]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GlueCrawlerDynamodbTarget]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GlueCrawlerDynamodbTarget]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b0da5522f9aef7105b0fc85127f32b4c28e1688ca193d8081c6b6428bb113c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GlueCrawlerDynamodbTargetOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.glueCrawler.GlueCrawlerDynamodbTargetOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__689e77dc9910e5024c41e0a6941e8e3e6148dca0cd851f1c07a5d109ae659331)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetScanAll")
    def reset_scan_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScanAll", []))

    @jsii.member(jsii_name="resetScanRate")
    def reset_scan_rate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScanRate", []))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="scanAllInput")
    def scan_all_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "scanAllInput"))

    @builtins.property
    @jsii.member(jsii_name="scanRateInput")
    def scan_rate_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "scanRateInput"))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b8a8f7ef26ba98e88f44fb34543f43c3e11a60efb6c3c363a10297cea972c9e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="scanAll")
    def scan_all(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "scanAll"))

    @scan_all.setter
    def scan_all(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__245b5f45470932c24924382f0f3999caad39a7883f464293f395b1100fc9c3e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scanAll", value)

    @builtins.property
    @jsii.member(jsii_name="scanRate")
    def scan_rate(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "scanRate"))

    @scan_rate.setter
    def scan_rate(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9ce0675137d76e1e85e87e2e42536f2d189eeeab87a3cdb74cf48dd5db9e538)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scanRate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GlueCrawlerDynamodbTarget, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GlueCrawlerDynamodbTarget, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GlueCrawlerDynamodbTarget, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09643d70b5582a7077471fa2a7cfa1280f4c857e3f7520bfedb4177bfd369348)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.glueCrawler.GlueCrawlerJdbcTarget",
    jsii_struct_bases=[],
    name_mapping={
        "connection_name": "connectionName",
        "path": "path",
        "enable_additional_metadata": "enableAdditionalMetadata",
        "exclusions": "exclusions",
    },
)
class GlueCrawlerJdbcTarget:
    def __init__(
        self,
        *,
        connection_name: builtins.str,
        path: builtins.str,
        enable_additional_metadata: typing.Optional[typing.Sequence[builtins.str]] = None,
        exclusions: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#connection_name GlueCrawler#connection_name}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#path GlueCrawler#path}.
        :param enable_additional_metadata: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#enable_additional_metadata GlueCrawler#enable_additional_metadata}.
        :param exclusions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#exclusions GlueCrawler#exclusions}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d427ce1b57e05685443dc8d3d4a34eb7b2a006ed4a5b9d3fc56a82a2ab6d04d0)
            check_type(argname="argument connection_name", value=connection_name, expected_type=type_hints["connection_name"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument enable_additional_metadata", value=enable_additional_metadata, expected_type=type_hints["enable_additional_metadata"])
            check_type(argname="argument exclusions", value=exclusions, expected_type=type_hints["exclusions"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "connection_name": connection_name,
            "path": path,
        }
        if enable_additional_metadata is not None:
            self._values["enable_additional_metadata"] = enable_additional_metadata
        if exclusions is not None:
            self._values["exclusions"] = exclusions

    @builtins.property
    def connection_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#connection_name GlueCrawler#connection_name}.'''
        result = self._values.get("connection_name")
        assert result is not None, "Required property 'connection_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#path GlueCrawler#path}.'''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enable_additional_metadata(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#enable_additional_metadata GlueCrawler#enable_additional_metadata}.'''
        result = self._values.get("enable_additional_metadata")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def exclusions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#exclusions GlueCrawler#exclusions}.'''
        result = self._values.get("exclusions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueCrawlerJdbcTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GlueCrawlerJdbcTargetList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.glueCrawler.GlueCrawlerJdbcTargetList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d0ac66af86449cc829ed3b696c6ab6333a548890c94d46a7971e3d0d66f10119)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "GlueCrawlerJdbcTargetOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8927848c722cd272d60f5d32b257bdad03d5963df2ec5ee537652640bb3a54a6)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GlueCrawlerJdbcTargetOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__252f10c0dd1a83a1327a445266a5abac9a538cbf35001e8cbeabe11547309988)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3d022137a44cb7c46352b15a9b7bdcf1101e2a7c0f5652fbc91e972e792fd8f9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__91ec8d30f779ff8eb4fe7af23ac35b4952d37a138d18f1009aa78d118dd9a92c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GlueCrawlerJdbcTarget]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GlueCrawlerJdbcTarget]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GlueCrawlerJdbcTarget]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__517590b5b63436422b9168eb9d18d972d095f10af6e013e99b2812e720b1c380)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GlueCrawlerJdbcTargetOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.glueCrawler.GlueCrawlerJdbcTargetOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__345e84cf3ae6e0c2f89f0abf93b537524c4a361b687c96c92fa2c04e43007dfa)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetEnableAdditionalMetadata")
    def reset_enable_additional_metadata(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableAdditionalMetadata", []))

    @jsii.member(jsii_name="resetExclusions")
    def reset_exclusions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExclusions", []))

    @builtins.property
    @jsii.member(jsii_name="connectionNameInput")
    def connection_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionNameInput"))

    @builtins.property
    @jsii.member(jsii_name="enableAdditionalMetadataInput")
    def enable_additional_metadata_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "enableAdditionalMetadataInput"))

    @builtins.property
    @jsii.member(jsii_name="exclusionsInput")
    def exclusions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "exclusionsInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionName")
    def connection_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionName"))

    @connection_name.setter
    def connection_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38fa945f6484a9e0ffbba8ed720bdede4cf86210ee4d16ddd259b72fcea35173)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionName", value)

    @builtins.property
    @jsii.member(jsii_name="enableAdditionalMetadata")
    def enable_additional_metadata(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "enableAdditionalMetadata"))

    @enable_additional_metadata.setter
    def enable_additional_metadata(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c827d24f69256268fbbdd4e3d6c021a2ae52e3e099201bc482c868f1ed3ff811)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableAdditionalMetadata", value)

    @builtins.property
    @jsii.member(jsii_name="exclusions")
    def exclusions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "exclusions"))

    @exclusions.setter
    def exclusions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66c05f3241f1111d423a4110501acddf95c969dd5e3bfdce9a49424e6a0b175d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exclusions", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7950cf1da8a88c98a6e05500ba7c63fb99de20c917a08540df1fe31665ac8806)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GlueCrawlerJdbcTarget, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GlueCrawlerJdbcTarget, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GlueCrawlerJdbcTarget, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68b018d599babe2557c8976e0f5092d566293a69b96d98b30a703a73649e997a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.glueCrawler.GlueCrawlerLakeFormationConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "account_id": "accountId",
        "use_lake_formation_credentials": "useLakeFormationCredentials",
    },
)
class GlueCrawlerLakeFormationConfiguration:
    def __init__(
        self,
        *,
        account_id: typing.Optional[builtins.str] = None,
        use_lake_formation_credentials: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#account_id GlueCrawler#account_id}.
        :param use_lake_formation_credentials: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#use_lake_formation_credentials GlueCrawler#use_lake_formation_credentials}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6d1794f1993e17ba17e00cb34e0b3a2b23630e06c0ccafd0d1ceb8339e69381)
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument use_lake_formation_credentials", value=use_lake_formation_credentials, expected_type=type_hints["use_lake_formation_credentials"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if account_id is not None:
            self._values["account_id"] = account_id
        if use_lake_formation_credentials is not None:
            self._values["use_lake_formation_credentials"] = use_lake_formation_credentials

    @builtins.property
    def account_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#account_id GlueCrawler#account_id}.'''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def use_lake_formation_credentials(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#use_lake_formation_credentials GlueCrawler#use_lake_formation_credentials}.'''
        result = self._values.get("use_lake_formation_credentials")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueCrawlerLakeFormationConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GlueCrawlerLakeFormationConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.glueCrawler.GlueCrawlerLakeFormationConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__daf7e2942db5c8961ee2b017232f7e17e2e78d619c76b5e2d2c8e808c17d3737)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAccountId")
    def reset_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountId", []))

    @jsii.member(jsii_name="resetUseLakeFormationCredentials")
    def reset_use_lake_formation_credentials(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseLakeFormationCredentials", []))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="useLakeFormationCredentialsInput")
    def use_lake_formation_credentials_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "useLakeFormationCredentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__533f6cc5eb83629113522b3963ff231402e4d03cc85aedcca08481956ced02bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="useLakeFormationCredentials")
    def use_lake_formation_credentials(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "useLakeFormationCredentials"))

    @use_lake_formation_credentials.setter
    def use_lake_formation_credentials(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae06e426a808828a2f5ff19e362fce52fe3b4f56f1b796f8fdef05253d32a93b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useLakeFormationCredentials", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GlueCrawlerLakeFormationConfiguration]:
        return typing.cast(typing.Optional[GlueCrawlerLakeFormationConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GlueCrawlerLakeFormationConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11cc3d140a43b607574af7d22e32a2619b84257e03654c0830a555d52ce1e40b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.glueCrawler.GlueCrawlerLineageConfiguration",
    jsii_struct_bases=[],
    name_mapping={"crawler_lineage_settings": "crawlerLineageSettings"},
)
class GlueCrawlerLineageConfiguration:
    def __init__(
        self,
        *,
        crawler_lineage_settings: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param crawler_lineage_settings: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#crawler_lineage_settings GlueCrawler#crawler_lineage_settings}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__833aaf5ead4bd4a2a7fb148411e00984748e5b0eca424728fd3816d444ffb8b8)
            check_type(argname="argument crawler_lineage_settings", value=crawler_lineage_settings, expected_type=type_hints["crawler_lineage_settings"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if crawler_lineage_settings is not None:
            self._values["crawler_lineage_settings"] = crawler_lineage_settings

    @builtins.property
    def crawler_lineage_settings(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#crawler_lineage_settings GlueCrawler#crawler_lineage_settings}.'''
        result = self._values.get("crawler_lineage_settings")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueCrawlerLineageConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GlueCrawlerLineageConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.glueCrawler.GlueCrawlerLineageConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6709ed731aecf6903b5973ef2e206a74ba31c8e0423eac9c3e73e57e1a115a78)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCrawlerLineageSettings")
    def reset_crawler_lineage_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCrawlerLineageSettings", []))

    @builtins.property
    @jsii.member(jsii_name="crawlerLineageSettingsInput")
    def crawler_lineage_settings_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "crawlerLineageSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="crawlerLineageSettings")
    def crawler_lineage_settings(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "crawlerLineageSettings"))

    @crawler_lineage_settings.setter
    def crawler_lineage_settings(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76d29edbc1ce2c06fa07060842098c11a1ad904f5e170dc555acd904479f01a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "crawlerLineageSettings", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GlueCrawlerLineageConfiguration]:
        return typing.cast(typing.Optional[GlueCrawlerLineageConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GlueCrawlerLineageConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5909147a5f6dd367f4a7817fdb4c304a765ceb074296b9c3d61a02a093692b6c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.glueCrawler.GlueCrawlerMongodbTarget",
    jsii_struct_bases=[],
    name_mapping={
        "connection_name": "connectionName",
        "path": "path",
        "scan_all": "scanAll",
    },
)
class GlueCrawlerMongodbTarget:
    def __init__(
        self,
        *,
        connection_name: builtins.str,
        path: builtins.str,
        scan_all: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param connection_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#connection_name GlueCrawler#connection_name}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#path GlueCrawler#path}.
        :param scan_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#scan_all GlueCrawler#scan_all}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf7188a6254237ff67f526e1632997b12459d77af7de2102c8371578b69ca13e)
            check_type(argname="argument connection_name", value=connection_name, expected_type=type_hints["connection_name"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument scan_all", value=scan_all, expected_type=type_hints["scan_all"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "connection_name": connection_name,
            "path": path,
        }
        if scan_all is not None:
            self._values["scan_all"] = scan_all

    @builtins.property
    def connection_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#connection_name GlueCrawler#connection_name}.'''
        result = self._values.get("connection_name")
        assert result is not None, "Required property 'connection_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#path GlueCrawler#path}.'''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def scan_all(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#scan_all GlueCrawler#scan_all}.'''
        result = self._values.get("scan_all")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueCrawlerMongodbTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GlueCrawlerMongodbTargetList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.glueCrawler.GlueCrawlerMongodbTargetList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3276c9ee7564120ed6936cbb1309e8a3e9da3962a7e71c800d8124e7d2dbdeaf)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "GlueCrawlerMongodbTargetOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__866a906675479f47472ac2f2be2da9eb4b29d146f74606a52abe0ccc890df9d6)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GlueCrawlerMongodbTargetOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4238bdd269523aab01946d42be9801f06541cfb984e238c69c9719d6a9c1fd4c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4fa2d1fd508a3918b380b3790148dd7537cb0cb013dfc450ad83497467236513)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5b01ef68908885c940ea1c9910ccd7b9e80a8997c02bcfbda6315855fd20f86f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GlueCrawlerMongodbTarget]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GlueCrawlerMongodbTarget]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GlueCrawlerMongodbTarget]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1a3b8e564329b18be839d1858f3f9b2ba14508600d3329a4a16feb4545926a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GlueCrawlerMongodbTargetOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.glueCrawler.GlueCrawlerMongodbTargetOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7a7b31eda44d9ad49598a4d17f13e131515327e2447576a1c85262475329b2ff)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetScanAll")
    def reset_scan_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScanAll", []))

    @builtins.property
    @jsii.member(jsii_name="connectionNameInput")
    def connection_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionNameInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="scanAllInput")
    def scan_all_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "scanAllInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionName")
    def connection_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionName"))

    @connection_name.setter
    def connection_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9d04f8e25499a885ae5f074175c14d1ede4e987d52e589e1142625f72fb3802)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionName", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2d1f046e87011a36c51c89d02c857b35d59dc5e35b81aba820b9f6b9a3c52ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="scanAll")
    def scan_all(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "scanAll"))

    @scan_all.setter
    def scan_all(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8cdf6ae63703fe8e7d2dd35599ed20f0efb15f3e178069611f7773480057a1c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scanAll", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GlueCrawlerMongodbTarget, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GlueCrawlerMongodbTarget, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GlueCrawlerMongodbTarget, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3de30de4dc7d5358bb642f211682c9f7005036a025d2806b9080126bfc6c6a58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.glueCrawler.GlueCrawlerRecrawlPolicy",
    jsii_struct_bases=[],
    name_mapping={"recrawl_behavior": "recrawlBehavior"},
)
class GlueCrawlerRecrawlPolicy:
    def __init__(
        self,
        *,
        recrawl_behavior: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param recrawl_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#recrawl_behavior GlueCrawler#recrawl_behavior}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d056f1793426cf87ecdeda4b472e782fa1100471da8f51d72c1a113616306aa6)
            check_type(argname="argument recrawl_behavior", value=recrawl_behavior, expected_type=type_hints["recrawl_behavior"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if recrawl_behavior is not None:
            self._values["recrawl_behavior"] = recrawl_behavior

    @builtins.property
    def recrawl_behavior(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#recrawl_behavior GlueCrawler#recrawl_behavior}.'''
        result = self._values.get("recrawl_behavior")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueCrawlerRecrawlPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GlueCrawlerRecrawlPolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.glueCrawler.GlueCrawlerRecrawlPolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__eaee970767f51e9764b0beea13ed0b490dd8cd8632f4b376373bf94d6d9c3d12)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetRecrawlBehavior")
    def reset_recrawl_behavior(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecrawlBehavior", []))

    @builtins.property
    @jsii.member(jsii_name="recrawlBehaviorInput")
    def recrawl_behavior_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recrawlBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="recrawlBehavior")
    def recrawl_behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recrawlBehavior"))

    @recrawl_behavior.setter
    def recrawl_behavior(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e71130c67d4eeedf131b990b82781ffc6d94ebc5dd2bf363e53e34951261fc9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recrawlBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GlueCrawlerRecrawlPolicy]:
        return typing.cast(typing.Optional[GlueCrawlerRecrawlPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[GlueCrawlerRecrawlPolicy]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e982c8689a651eb6bd1b31192602d1cd4704d5d9ac755fa56231b2021717e201)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.glueCrawler.GlueCrawlerS3Target",
    jsii_struct_bases=[],
    name_mapping={
        "path": "path",
        "connection_name": "connectionName",
        "dlq_event_queue_arn": "dlqEventQueueArn",
        "event_queue_arn": "eventQueueArn",
        "exclusions": "exclusions",
        "sample_size": "sampleSize",
    },
)
class GlueCrawlerS3Target:
    def __init__(
        self,
        *,
        path: builtins.str,
        connection_name: typing.Optional[builtins.str] = None,
        dlq_event_queue_arn: typing.Optional[builtins.str] = None,
        event_queue_arn: typing.Optional[builtins.str] = None,
        exclusions: typing.Optional[typing.Sequence[builtins.str]] = None,
        sample_size: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#path GlueCrawler#path}.
        :param connection_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#connection_name GlueCrawler#connection_name}.
        :param dlq_event_queue_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#dlq_event_queue_arn GlueCrawler#dlq_event_queue_arn}.
        :param event_queue_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#event_queue_arn GlueCrawler#event_queue_arn}.
        :param exclusions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#exclusions GlueCrawler#exclusions}.
        :param sample_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#sample_size GlueCrawler#sample_size}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b49122aebea569496570a2a8d08f2e1cf19e45c127760536880fefb34ce61cfb)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument connection_name", value=connection_name, expected_type=type_hints["connection_name"])
            check_type(argname="argument dlq_event_queue_arn", value=dlq_event_queue_arn, expected_type=type_hints["dlq_event_queue_arn"])
            check_type(argname="argument event_queue_arn", value=event_queue_arn, expected_type=type_hints["event_queue_arn"])
            check_type(argname="argument exclusions", value=exclusions, expected_type=type_hints["exclusions"])
            check_type(argname="argument sample_size", value=sample_size, expected_type=type_hints["sample_size"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "path": path,
        }
        if connection_name is not None:
            self._values["connection_name"] = connection_name
        if dlq_event_queue_arn is not None:
            self._values["dlq_event_queue_arn"] = dlq_event_queue_arn
        if event_queue_arn is not None:
            self._values["event_queue_arn"] = event_queue_arn
        if exclusions is not None:
            self._values["exclusions"] = exclusions
        if sample_size is not None:
            self._values["sample_size"] = sample_size

    @builtins.property
    def path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#path GlueCrawler#path}.'''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def connection_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#connection_name GlueCrawler#connection_name}.'''
        result = self._values.get("connection_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dlq_event_queue_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#dlq_event_queue_arn GlueCrawler#dlq_event_queue_arn}.'''
        result = self._values.get("dlq_event_queue_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def event_queue_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#event_queue_arn GlueCrawler#event_queue_arn}.'''
        result = self._values.get("event_queue_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def exclusions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#exclusions GlueCrawler#exclusions}.'''
        result = self._values.get("exclusions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def sample_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#sample_size GlueCrawler#sample_size}.'''
        result = self._values.get("sample_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueCrawlerS3Target(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GlueCrawlerS3TargetList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.glueCrawler.GlueCrawlerS3TargetList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__417c5fb662402182eac937b0cafb375acdd0aa7d45993b7d4fbbfe7cef98152f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "GlueCrawlerS3TargetOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07fe04c5d64f274cad9384f7cfb8278554cde85cb309b56c15d9dc60a5ff2c54)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GlueCrawlerS3TargetOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19c936b087419659ade040e1e2934ebd17d2a5e9f5bd514e46f4c6f321b24819)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1408deda4f58986d9767e3119dad78c87f550b12afa58ff0014374477b605b09)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ccafcdc68d2cf314d0266e51a5973faa7d9f8de9adc978421f089a3f985f0f25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GlueCrawlerS3Target]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GlueCrawlerS3Target]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GlueCrawlerS3Target]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__399231c291551f7f83ae45a7f70276c86ec9ada1098eeee46a07ee02a1d36b49)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GlueCrawlerS3TargetOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.glueCrawler.GlueCrawlerS3TargetOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e82f944b319586a890d79ea0e3f251ca82f38ca546db5c0c3dad2bacda8a0a51)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetConnectionName")
    def reset_connection_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionName", []))

    @jsii.member(jsii_name="resetDlqEventQueueArn")
    def reset_dlq_event_queue_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDlqEventQueueArn", []))

    @jsii.member(jsii_name="resetEventQueueArn")
    def reset_event_queue_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventQueueArn", []))

    @jsii.member(jsii_name="resetExclusions")
    def reset_exclusions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExclusions", []))

    @jsii.member(jsii_name="resetSampleSize")
    def reset_sample_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSampleSize", []))

    @builtins.property
    @jsii.member(jsii_name="connectionNameInput")
    def connection_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionNameInput"))

    @builtins.property
    @jsii.member(jsii_name="dlqEventQueueArnInput")
    def dlq_event_queue_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dlqEventQueueArnInput"))

    @builtins.property
    @jsii.member(jsii_name="eventQueueArnInput")
    def event_queue_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventQueueArnInput"))

    @builtins.property
    @jsii.member(jsii_name="exclusionsInput")
    def exclusions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "exclusionsInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="sampleSizeInput")
    def sample_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sampleSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionName")
    def connection_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionName"))

    @connection_name.setter
    def connection_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d431c21734418ef126e8cac9581e0e6f62f1beb679a5549c147b71fc8595d625)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionName", value)

    @builtins.property
    @jsii.member(jsii_name="dlqEventQueueArn")
    def dlq_event_queue_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dlqEventQueueArn"))

    @dlq_event_queue_arn.setter
    def dlq_event_queue_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4dad3755666e802385d056912d22ca129a3d975eb575fa0fe17365088ac27e8a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dlqEventQueueArn", value)

    @builtins.property
    @jsii.member(jsii_name="eventQueueArn")
    def event_queue_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventQueueArn"))

    @event_queue_arn.setter
    def event_queue_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3809553c872c66675bc99aaf57429b01a1e3992a36e0ad72b500d01bf299f62c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventQueueArn", value)

    @builtins.property
    @jsii.member(jsii_name="exclusions")
    def exclusions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "exclusions"))

    @exclusions.setter
    def exclusions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1062656edac034979a2f5f73f3db9c3a3a41bf90eacd013d75f7c75459504d45)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exclusions", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89d819108f960602c4b31e706ba9a8a000e1d7f9caef2b89142198dfc6955227)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="sampleSize")
    def sample_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sampleSize"))

    @sample_size.setter
    def sample_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af286f5c35a1bc9e89ba13de8a52c254012d6cd3db5c7eed15483b154ffccab4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sampleSize", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GlueCrawlerS3Target, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GlueCrawlerS3Target, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GlueCrawlerS3Target, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e778af59be91bede0646ab3868f6a8200f2028f09391431987357a0a019bfffe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.glueCrawler.GlueCrawlerSchemaChangePolicy",
    jsii_struct_bases=[],
    name_mapping={
        "delete_behavior": "deleteBehavior",
        "update_behavior": "updateBehavior",
    },
)
class GlueCrawlerSchemaChangePolicy:
    def __init__(
        self,
        *,
        delete_behavior: typing.Optional[builtins.str] = None,
        update_behavior: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param delete_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#delete_behavior GlueCrawler#delete_behavior}.
        :param update_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#update_behavior GlueCrawler#update_behavior}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc3d8b9f9531066dd5009d2d4f172ce1f7c74850a9cbfb885d89c9c43c1c99e5)
            check_type(argname="argument delete_behavior", value=delete_behavior, expected_type=type_hints["delete_behavior"])
            check_type(argname="argument update_behavior", value=update_behavior, expected_type=type_hints["update_behavior"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if delete_behavior is not None:
            self._values["delete_behavior"] = delete_behavior
        if update_behavior is not None:
            self._values["update_behavior"] = update_behavior

    @builtins.property
    def delete_behavior(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#delete_behavior GlueCrawler#delete_behavior}.'''
        result = self._values.get("delete_behavior")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update_behavior(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#update_behavior GlueCrawler#update_behavior}.'''
        result = self._values.get("update_behavior")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueCrawlerSchemaChangePolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GlueCrawlerSchemaChangePolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.glueCrawler.GlueCrawlerSchemaChangePolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f0613c41cae683f3331d998044b4da186d3b20be1fc7f63f38481c7ff5bfb5f9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDeleteBehavior")
    def reset_delete_behavior(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeleteBehavior", []))

    @jsii.member(jsii_name="resetUpdateBehavior")
    def reset_update_behavior(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdateBehavior", []))

    @builtins.property
    @jsii.member(jsii_name="deleteBehaviorInput")
    def delete_behavior_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="updateBehaviorInput")
    def update_behavior_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteBehavior")
    def delete_behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deleteBehavior"))

    @delete_behavior.setter
    def delete_behavior(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e963be25eb45bf47b566fbd8ae0319c3e1d19f80f2ef8a15a607bb993901150)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="updateBehavior")
    def update_behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "updateBehavior"))

    @update_behavior.setter
    def update_behavior(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bba42926c2b117459997f7dffe040a2d4edbe257128fd925baf67bba931c955d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "updateBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GlueCrawlerSchemaChangePolicy]:
        return typing.cast(typing.Optional[GlueCrawlerSchemaChangePolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GlueCrawlerSchemaChangePolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23d62666c93e69cd0a1d6f19c5b6d942651f8a3324c35f7285520b5e15a768a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GlueCrawler",
    "GlueCrawlerCatalogTarget",
    "GlueCrawlerCatalogTargetList",
    "GlueCrawlerCatalogTargetOutputReference",
    "GlueCrawlerConfig",
    "GlueCrawlerDeltaTarget",
    "GlueCrawlerDeltaTargetList",
    "GlueCrawlerDeltaTargetOutputReference",
    "GlueCrawlerDynamodbTarget",
    "GlueCrawlerDynamodbTargetList",
    "GlueCrawlerDynamodbTargetOutputReference",
    "GlueCrawlerJdbcTarget",
    "GlueCrawlerJdbcTargetList",
    "GlueCrawlerJdbcTargetOutputReference",
    "GlueCrawlerLakeFormationConfiguration",
    "GlueCrawlerLakeFormationConfigurationOutputReference",
    "GlueCrawlerLineageConfiguration",
    "GlueCrawlerLineageConfigurationOutputReference",
    "GlueCrawlerMongodbTarget",
    "GlueCrawlerMongodbTargetList",
    "GlueCrawlerMongodbTargetOutputReference",
    "GlueCrawlerRecrawlPolicy",
    "GlueCrawlerRecrawlPolicyOutputReference",
    "GlueCrawlerS3Target",
    "GlueCrawlerS3TargetList",
    "GlueCrawlerS3TargetOutputReference",
    "GlueCrawlerSchemaChangePolicy",
    "GlueCrawlerSchemaChangePolicyOutputReference",
]

publication.publish()

def _typecheckingstub__ce19d43400f8f2c340b8537e1962b744e7ab3ad3ad1020c9b53218ef2eefd69e(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    database_name: builtins.str,
    name: builtins.str,
    role: builtins.str,
    catalog_target: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GlueCrawlerCatalogTarget, typing.Dict[builtins.str, typing.Any]]]]] = None,
    classifiers: typing.Optional[typing.Sequence[builtins.str]] = None,
    configuration: typing.Optional[builtins.str] = None,
    delta_target: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GlueCrawlerDeltaTarget, typing.Dict[builtins.str, typing.Any]]]]] = None,
    description: typing.Optional[builtins.str] = None,
    dynamodb_target: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GlueCrawlerDynamodbTarget, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
    jdbc_target: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GlueCrawlerJdbcTarget, typing.Dict[builtins.str, typing.Any]]]]] = None,
    lake_formation_configuration: typing.Optional[typing.Union[GlueCrawlerLakeFormationConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    lineage_configuration: typing.Optional[typing.Union[GlueCrawlerLineageConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    mongodb_target: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GlueCrawlerMongodbTarget, typing.Dict[builtins.str, typing.Any]]]]] = None,
    recrawl_policy: typing.Optional[typing.Union[GlueCrawlerRecrawlPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    s3_target: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GlueCrawlerS3Target, typing.Dict[builtins.str, typing.Any]]]]] = None,
    schedule: typing.Optional[builtins.str] = None,
    schema_change_policy: typing.Optional[typing.Union[GlueCrawlerSchemaChangePolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    security_configuration: typing.Optional[builtins.str] = None,
    table_prefix: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__e7081833d391d3260585ef0b6fdac5528d2c1f728bb79b7ff956f9543308f131(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GlueCrawlerCatalogTarget, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce99ce69110a761f2dcf77be0096035117a2a0c77cf89678d835897a32ba7b4d(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GlueCrawlerDeltaTarget, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ed48fd33b0e73cce502ca07fa393095585ed0555394b88058ed008e794e2813(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GlueCrawlerDynamodbTarget, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42d2b5bf68d492d19ac3f11a58fcc005df9a673b4ff35400612f8274f1f7662c(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GlueCrawlerJdbcTarget, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fa9487fe92a745d5d4504ba066bb31fc6812f6243c9c79e8b97c0729edcc1a1(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GlueCrawlerMongodbTarget, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce2ea91807e3ab5ea57e2bf732974447c0f12f7e8a17a37c2a3bc716f1d307d1(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GlueCrawlerS3Target, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89545a88025c74ef184be49a1fbdb4f70d77520ca265573cc2e681ec7c8f4f4e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28efc36cbab9e6879bc71f335d9ff87f94b927a9e16d7164013d65d7627c7610(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da7e0eacef9c4c6560a8a349b56f1dc1519ad8e7965253b803530005fbb6d7d7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e799792aa1e17016090eb7e7dfe3e74c9b4e3d235577286e24c91bf978725d5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36cee85f7b881cd40881952f2e1d0472f960b65a500bb905cc923aaedfea17df(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1385c671a92e9e0ec06cf636e957676aa3a167c1dc11204fce2d66c62a6c1d68(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ebc0dea20a029efeb1a4e862ff421cfc2feae27ae13e9c7963aca2242273c66(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f44e77768243d8de9f640d4fb5849d53c234b530bc8ff10da176541c5748db22(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e34483ecf993a0d672c6a59a19ab35f109558032e8f330f5b1276827bd904de(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9076732b52fa008945ac5d4a0ef1bd09e1b21093e53a157e2bbfb97265030083(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ab8adabfacef54b18f09be9b95a2e1825c0e070d73ad3c1d8d3c30e0298290e(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb4e5f831c836b91c19925098ce14d66be3c7583e0ba73e8ea3ae5d3da78b5b0(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65d5a23fadffa9e10cac18e70d639c95394e890e074946687cbea7413e89cef1(
    *,
    database_name: builtins.str,
    tables: typing.Sequence[builtins.str],
    connection_name: typing.Optional[builtins.str] = None,
    dlq_event_queue_arn: typing.Optional[builtins.str] = None,
    event_queue_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f316ad702459abd417897f1ddd561d72aa06de3a5c41ee8c255aa8c828b6fad1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b31edb056def6b5204ce8178aceb8a2575fe2c249ba5c2bc8a896a4ea4bd997b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b62041ad69ba9fb854fbfe54f80855188f42840a037597b56c54e0542ff8170(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9f4d615dadf1da014cb66ff4f551bfa00501f76d357cdff863ef83cdb5b626c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d415738c529ebd8597701338788892e1bb3d80da2b1bd290be35c061e9c17b94(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cdac4b09b22b96c88029a515cdeaace1f1f3e8ef29d12f36ef76358b2c1f386(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GlueCrawlerCatalogTarget]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd2ed339c1a5ce60da6faf1c3859114ab1db39ca09f8aaf0512e094e9e6b48f8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c733f6f764d2a94defafa3778162ec226babb04779dcd9b0564555e50d28d919(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d3a2342c19224d0d6e83303489f2d8d6f034463c43075b95418362bb80e4f59(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8be76ebce2b5f30e132064944289a6ffaf04deca3fc00c2f85dceccd1219a50e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43fe746f6c06833b9a66500b0bcec32bfeb57b6b013cbc451d6f5695d6f70cb5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d6cc4bea36083ba4af369019c53289c744fcc8b41c26e9f4affed33f9aebeda(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae60bb75a6f4b3f2c1a9ee89b6db5768c8f32a80ca8c7781750a08decd2bc569(
    value: typing.Optional[typing.Union[GlueCrawlerCatalogTarget, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c2aad4d2e353612ebcdaf468d1f92fb5ae948341f7770501fdae277d968ca58(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    database_name: builtins.str,
    name: builtins.str,
    role: builtins.str,
    catalog_target: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GlueCrawlerCatalogTarget, typing.Dict[builtins.str, typing.Any]]]]] = None,
    classifiers: typing.Optional[typing.Sequence[builtins.str]] = None,
    configuration: typing.Optional[builtins.str] = None,
    delta_target: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GlueCrawlerDeltaTarget, typing.Dict[builtins.str, typing.Any]]]]] = None,
    description: typing.Optional[builtins.str] = None,
    dynamodb_target: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GlueCrawlerDynamodbTarget, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
    jdbc_target: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GlueCrawlerJdbcTarget, typing.Dict[builtins.str, typing.Any]]]]] = None,
    lake_formation_configuration: typing.Optional[typing.Union[GlueCrawlerLakeFormationConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    lineage_configuration: typing.Optional[typing.Union[GlueCrawlerLineageConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    mongodb_target: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GlueCrawlerMongodbTarget, typing.Dict[builtins.str, typing.Any]]]]] = None,
    recrawl_policy: typing.Optional[typing.Union[GlueCrawlerRecrawlPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    s3_target: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GlueCrawlerS3Target, typing.Dict[builtins.str, typing.Any]]]]] = None,
    schedule: typing.Optional[builtins.str] = None,
    schema_change_policy: typing.Optional[typing.Union[GlueCrawlerSchemaChangePolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    security_configuration: typing.Optional[builtins.str] = None,
    table_prefix: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60a1c43df90bd8f9ca084605db64a508ef2b43ccbce1c46304e96ef0102d5bd3(
    *,
    delta_tables: typing.Sequence[builtins.str],
    write_manifest: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    connection_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89dfa48ff6e1a512dff2cceee925e7017c671c615f0788b05e8afcfc954eaf3c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90338d3d8ae86e31f69e0c807e0f6816d0c698db14ec7a7178f83fa9daca555b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8780503df898d39d73477b121cbd4c71a1d957bd30cfb2b4eb6212a52b8b4298(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__370fc096c4eb6686eaaf8a5351bba00528afe45daa8fb5bf9c3b7b4c083b952c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f659f9615d4723ec2bafa326ba6d1f178fa19fd8530ebeb0b8154e3dd131930f(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__915b41cc15de5e951e222fe4ca1a9853ff41634fafed735bbabf23abbdb97485(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GlueCrawlerDeltaTarget]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__418d8bc8bd295aae896fd2da1efdf2f2c983be8b79eeebe0837c03e2ee1c2ea5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d459c07fe7cccb18e7649ba749a0ec6f5c0e406df8c6fc8b16a8b2966907fc99(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9788a4a64224c101052e9ba2f9be9e71c8d9ee45fb394786bb119923b612e15(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4acd8d098039fcb2ae0e90cc4a438069f937f6e26c437d2531e1297b973195ac(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85edcc2f2fb925fa63d4f541beeb366d6a82b6318d2fb02e4d687da8fd2e5119(
    value: typing.Optional[typing.Union[GlueCrawlerDeltaTarget, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31c22ee5235267ce4618620966d316aaaf6ff4c20feeb863ae878b9e288b3b77(
    *,
    path: builtins.str,
    scan_all: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    scan_rate: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7415f8adb83846fb6e5df60c234294a37cc2329c4b5574dfd3e9ec68adbd04e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b61186d6494d888df7bcc672f28404357e151ce149fef138e7d1b13f5bc712a9(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d1c46506911d088bfe633ea74a0d99afd76b8a8a8d12064f980edda55a979f8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32ae6d53aff7fd156ff9a6fe6faf02935bbfb84b1308119a7215b9a2b6fddeae(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b358001f8e6871665d7e79d219b0eab525c71492ed604467174e0aa80dcdb06e(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b0da5522f9aef7105b0fc85127f32b4c28e1688ca193d8081c6b6428bb113c1(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GlueCrawlerDynamodbTarget]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__689e77dc9910e5024c41e0a6941e8e3e6148dca0cd851f1c07a5d109ae659331(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b8a8f7ef26ba98e88f44fb34543f43c3e11a60efb6c3c363a10297cea972c9e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__245b5f45470932c24924382f0f3999caad39a7883f464293f395b1100fc9c3e2(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9ce0675137d76e1e85e87e2e42536f2d189eeeab87a3cdb74cf48dd5db9e538(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09643d70b5582a7077471fa2a7cfa1280f4c857e3f7520bfedb4177bfd369348(
    value: typing.Optional[typing.Union[GlueCrawlerDynamodbTarget, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d427ce1b57e05685443dc8d3d4a34eb7b2a006ed4a5b9d3fc56a82a2ab6d04d0(
    *,
    connection_name: builtins.str,
    path: builtins.str,
    enable_additional_metadata: typing.Optional[typing.Sequence[builtins.str]] = None,
    exclusions: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0ac66af86449cc829ed3b696c6ab6333a548890c94d46a7971e3d0d66f10119(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8927848c722cd272d60f5d32b257bdad03d5963df2ec5ee537652640bb3a54a6(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__252f10c0dd1a83a1327a445266a5abac9a538cbf35001e8cbeabe11547309988(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d022137a44cb7c46352b15a9b7bdcf1101e2a7c0f5652fbc91e972e792fd8f9(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91ec8d30f779ff8eb4fe7af23ac35b4952d37a138d18f1009aa78d118dd9a92c(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__517590b5b63436422b9168eb9d18d972d095f10af6e013e99b2812e720b1c380(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GlueCrawlerJdbcTarget]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__345e84cf3ae6e0c2f89f0abf93b537524c4a361b687c96c92fa2c04e43007dfa(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38fa945f6484a9e0ffbba8ed720bdede4cf86210ee4d16ddd259b72fcea35173(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c827d24f69256268fbbdd4e3d6c021a2ae52e3e099201bc482c868f1ed3ff811(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66c05f3241f1111d423a4110501acddf95c969dd5e3bfdce9a49424e6a0b175d(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7950cf1da8a88c98a6e05500ba7c63fb99de20c917a08540df1fe31665ac8806(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68b018d599babe2557c8976e0f5092d566293a69b96d98b30a703a73649e997a(
    value: typing.Optional[typing.Union[GlueCrawlerJdbcTarget, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6d1794f1993e17ba17e00cb34e0b3a2b23630e06c0ccafd0d1ceb8339e69381(
    *,
    account_id: typing.Optional[builtins.str] = None,
    use_lake_formation_credentials: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__daf7e2942db5c8961ee2b017232f7e17e2e78d619c76b5e2d2c8e808c17d3737(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__533f6cc5eb83629113522b3963ff231402e4d03cc85aedcca08481956ced02bd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae06e426a808828a2f5ff19e362fce52fe3b4f56f1b796f8fdef05253d32a93b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11cc3d140a43b607574af7d22e32a2619b84257e03654c0830a555d52ce1e40b(
    value: typing.Optional[GlueCrawlerLakeFormationConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__833aaf5ead4bd4a2a7fb148411e00984748e5b0eca424728fd3816d444ffb8b8(
    *,
    crawler_lineage_settings: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6709ed731aecf6903b5973ef2e206a74ba31c8e0423eac9c3e73e57e1a115a78(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76d29edbc1ce2c06fa07060842098c11a1ad904f5e170dc555acd904479f01a7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5909147a5f6dd367f4a7817fdb4c304a765ceb074296b9c3d61a02a093692b6c(
    value: typing.Optional[GlueCrawlerLineageConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf7188a6254237ff67f526e1632997b12459d77af7de2102c8371578b69ca13e(
    *,
    connection_name: builtins.str,
    path: builtins.str,
    scan_all: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3276c9ee7564120ed6936cbb1309e8a3e9da3962a7e71c800d8124e7d2dbdeaf(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__866a906675479f47472ac2f2be2da9eb4b29d146f74606a52abe0ccc890df9d6(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4238bdd269523aab01946d42be9801f06541cfb984e238c69c9719d6a9c1fd4c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fa2d1fd508a3918b380b3790148dd7537cb0cb013dfc450ad83497467236513(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b01ef68908885c940ea1c9910ccd7b9e80a8997c02bcfbda6315855fd20f86f(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1a3b8e564329b18be839d1858f3f9b2ba14508600d3329a4a16feb4545926a2(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GlueCrawlerMongodbTarget]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a7b31eda44d9ad49598a4d17f13e131515327e2447576a1c85262475329b2ff(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9d04f8e25499a885ae5f074175c14d1ede4e987d52e589e1142625f72fb3802(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2d1f046e87011a36c51c89d02c857b35d59dc5e35b81aba820b9f6b9a3c52ae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8cdf6ae63703fe8e7d2dd35599ed20f0efb15f3e178069611f7773480057a1c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3de30de4dc7d5358bb642f211682c9f7005036a025d2806b9080126bfc6c6a58(
    value: typing.Optional[typing.Union[GlueCrawlerMongodbTarget, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d056f1793426cf87ecdeda4b472e782fa1100471da8f51d72c1a113616306aa6(
    *,
    recrawl_behavior: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eaee970767f51e9764b0beea13ed0b490dd8cd8632f4b376373bf94d6d9c3d12(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e71130c67d4eeedf131b990b82781ffc6d94ebc5dd2bf363e53e34951261fc9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e982c8689a651eb6bd1b31192602d1cd4704d5d9ac755fa56231b2021717e201(
    value: typing.Optional[GlueCrawlerRecrawlPolicy],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b49122aebea569496570a2a8d08f2e1cf19e45c127760536880fefb34ce61cfb(
    *,
    path: builtins.str,
    connection_name: typing.Optional[builtins.str] = None,
    dlq_event_queue_arn: typing.Optional[builtins.str] = None,
    event_queue_arn: typing.Optional[builtins.str] = None,
    exclusions: typing.Optional[typing.Sequence[builtins.str]] = None,
    sample_size: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__417c5fb662402182eac937b0cafb375acdd0aa7d45993b7d4fbbfe7cef98152f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07fe04c5d64f274cad9384f7cfb8278554cde85cb309b56c15d9dc60a5ff2c54(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19c936b087419659ade040e1e2934ebd17d2a5e9f5bd514e46f4c6f321b24819(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1408deda4f58986d9767e3119dad78c87f550b12afa58ff0014374477b605b09(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccafcdc68d2cf314d0266e51a5973faa7d9f8de9adc978421f089a3f985f0f25(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__399231c291551f7f83ae45a7f70276c86ec9ada1098eeee46a07ee02a1d36b49(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GlueCrawlerS3Target]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e82f944b319586a890d79ea0e3f251ca82f38ca546db5c0c3dad2bacda8a0a51(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d431c21734418ef126e8cac9581e0e6f62f1beb679a5549c147b71fc8595d625(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4dad3755666e802385d056912d22ca129a3d975eb575fa0fe17365088ac27e8a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3809553c872c66675bc99aaf57429b01a1e3992a36e0ad72b500d01bf299f62c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1062656edac034979a2f5f73f3db9c3a3a41bf90eacd013d75f7c75459504d45(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89d819108f960602c4b31e706ba9a8a000e1d7f9caef2b89142198dfc6955227(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af286f5c35a1bc9e89ba13de8a52c254012d6cd3db5c7eed15483b154ffccab4(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e778af59be91bede0646ab3868f6a8200f2028f09391431987357a0a019bfffe(
    value: typing.Optional[typing.Union[GlueCrawlerS3Target, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc3d8b9f9531066dd5009d2d4f172ce1f7c74850a9cbfb885d89c9c43c1c99e5(
    *,
    delete_behavior: typing.Optional[builtins.str] = None,
    update_behavior: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0613c41cae683f3331d998044b4da186d3b20be1fc7f63f38481c7ff5bfb5f9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e963be25eb45bf47b566fbd8ae0319c3e1d19f80f2ef8a15a607bb993901150(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bba42926c2b117459997f7dffe040a2d4edbe257128fd925baf67bba931c955d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23d62666c93e69cd0a1d6f19c5b6d942651f8a3324c35f7285520b5e15a768a1(
    value: typing.Optional[GlueCrawlerSchemaChangePolicy],
) -> None:
    """Type checking stubs"""
    pass
