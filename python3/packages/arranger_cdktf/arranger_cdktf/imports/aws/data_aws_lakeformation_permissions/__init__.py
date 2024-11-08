'''
# `data_aws_lakeformation_permissions`

Refer to the Terraform Registory for docs: [`data_aws_lakeformation_permissions`](https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions).
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


class DataAwsLakeformationPermissions(
    _cdktf_9a9027ec.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsLakeformationPermissions.DataAwsLakeformationPermissions",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions aws_lakeformation_permissions}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        principal: builtins.str,
        catalog_id: typing.Optional[builtins.str] = None,
        catalog_resource: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        database: typing.Optional[typing.Union["DataAwsLakeformationPermissionsDatabase", typing.Dict[builtins.str, typing.Any]]] = None,
        data_location: typing.Optional[typing.Union["DataAwsLakeformationPermissionsDataLocation", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        lf_tag: typing.Optional[typing.Union["DataAwsLakeformationPermissionsLfTag", typing.Dict[builtins.str, typing.Any]]] = None,
        lf_tag_policy: typing.Optional[typing.Union["DataAwsLakeformationPermissionsLfTagPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        table: typing.Optional[typing.Union["DataAwsLakeformationPermissionsTable", typing.Dict[builtins.str, typing.Any]]] = None,
        table_with_columns: typing.Optional[typing.Union["DataAwsLakeformationPermissionsTableWithColumns", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions aws_lakeformation_permissions} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param principal: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#principal DataAwsLakeformationPermissions#principal}.
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#catalog_id DataAwsLakeformationPermissions#catalog_id}.
        :param catalog_resource: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#catalog_resource DataAwsLakeformationPermissions#catalog_resource}.
        :param database: database block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#database DataAwsLakeformationPermissions#database}
        :param data_location: data_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#data_location DataAwsLakeformationPermissions#data_location}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#id DataAwsLakeformationPermissions#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param lf_tag: lf_tag block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#lf_tag DataAwsLakeformationPermissions#lf_tag}
        :param lf_tag_policy: lf_tag_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#lf_tag_policy DataAwsLakeformationPermissions#lf_tag_policy}
        :param table: table block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#table DataAwsLakeformationPermissions#table}
        :param table_with_columns: table_with_columns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#table_with_columns DataAwsLakeformationPermissions#table_with_columns}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fd8454cce1328fb5dbe9926364295f5d1f4867a4f84f172d518d8ed2719040c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataAwsLakeformationPermissionsConfig(
            principal=principal,
            catalog_id=catalog_id,
            catalog_resource=catalog_resource,
            database=database,
            data_location=data_location,
            id=id,
            lf_tag=lf_tag,
            lf_tag_policy=lf_tag_policy,
            table=table,
            table_with_columns=table_with_columns,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putDatabase")
    def put_database(
        self,
        *,
        name: builtins.str,
        catalog_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#name DataAwsLakeformationPermissions#name}.
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#catalog_id DataAwsLakeformationPermissions#catalog_id}.
        '''
        value = DataAwsLakeformationPermissionsDatabase(
            name=name, catalog_id=catalog_id
        )

        return typing.cast(None, jsii.invoke(self, "putDatabase", [value]))

    @jsii.member(jsii_name="putDataLocation")
    def put_data_location(
        self,
        *,
        arn: builtins.str,
        catalog_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#arn DataAwsLakeformationPermissions#arn}.
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#catalog_id DataAwsLakeformationPermissions#catalog_id}.
        '''
        value = DataAwsLakeformationPermissionsDataLocation(
            arn=arn, catalog_id=catalog_id
        )

        return typing.cast(None, jsii.invoke(self, "putDataLocation", [value]))

    @jsii.member(jsii_name="putLfTag")
    def put_lf_tag(
        self,
        *,
        key: builtins.str,
        values: typing.Sequence[builtins.str],
        catalog_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#key DataAwsLakeformationPermissions#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#values DataAwsLakeformationPermissions#values}.
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#catalog_id DataAwsLakeformationPermissions#catalog_id}.
        '''
        value = DataAwsLakeformationPermissionsLfTag(
            key=key, values=values, catalog_id=catalog_id
        )

        return typing.cast(None, jsii.invoke(self, "putLfTag", [value]))

    @jsii.member(jsii_name="putLfTagPolicy")
    def put_lf_tag_policy(
        self,
        *,
        expression: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAwsLakeformationPermissionsLfTagPolicyExpression", typing.Dict[builtins.str, typing.Any]]]],
        resource_type: builtins.str,
        catalog_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param expression: expression block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#expression DataAwsLakeformationPermissions#expression}
        :param resource_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#resource_type DataAwsLakeformationPermissions#resource_type}.
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#catalog_id DataAwsLakeformationPermissions#catalog_id}.
        '''
        value = DataAwsLakeformationPermissionsLfTagPolicy(
            expression=expression, resource_type=resource_type, catalog_id=catalog_id
        )

        return typing.cast(None, jsii.invoke(self, "putLfTagPolicy", [value]))

    @jsii.member(jsii_name="putTable")
    def put_table(
        self,
        *,
        database_name: builtins.str,
        catalog_id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        wildcard: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#database_name DataAwsLakeformationPermissions#database_name}.
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#catalog_id DataAwsLakeformationPermissions#catalog_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#name DataAwsLakeformationPermissions#name}.
        :param wildcard: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#wildcard DataAwsLakeformationPermissions#wildcard}.
        '''
        value = DataAwsLakeformationPermissionsTable(
            database_name=database_name,
            catalog_id=catalog_id,
            name=name,
            wildcard=wildcard,
        )

        return typing.cast(None, jsii.invoke(self, "putTable", [value]))

    @jsii.member(jsii_name="putTableWithColumns")
    def put_table_with_columns(
        self,
        *,
        database_name: builtins.str,
        name: builtins.str,
        catalog_id: typing.Optional[builtins.str] = None,
        column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        excluded_column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        wildcard: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#database_name DataAwsLakeformationPermissions#database_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#name DataAwsLakeformationPermissions#name}.
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#catalog_id DataAwsLakeformationPermissions#catalog_id}.
        :param column_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#column_names DataAwsLakeformationPermissions#column_names}.
        :param excluded_column_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#excluded_column_names DataAwsLakeformationPermissions#excluded_column_names}.
        :param wildcard: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#wildcard DataAwsLakeformationPermissions#wildcard}.
        '''
        value = DataAwsLakeformationPermissionsTableWithColumns(
            database_name=database_name,
            name=name,
            catalog_id=catalog_id,
            column_names=column_names,
            excluded_column_names=excluded_column_names,
            wildcard=wildcard,
        )

        return typing.cast(None, jsii.invoke(self, "putTableWithColumns", [value]))

    @jsii.member(jsii_name="resetCatalogId")
    def reset_catalog_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCatalogId", []))

    @jsii.member(jsii_name="resetCatalogResource")
    def reset_catalog_resource(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCatalogResource", []))

    @jsii.member(jsii_name="resetDatabase")
    def reset_database(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatabase", []))

    @jsii.member(jsii_name="resetDataLocation")
    def reset_data_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataLocation", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLfTag")
    def reset_lf_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLfTag", []))

    @jsii.member(jsii_name="resetLfTagPolicy")
    def reset_lf_tag_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLfTagPolicy", []))

    @jsii.member(jsii_name="resetTable")
    def reset_table(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTable", []))

    @jsii.member(jsii_name="resetTableWithColumns")
    def reset_table_with_columns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTableWithColumns", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="database")
    def database(self) -> "DataAwsLakeformationPermissionsDatabaseOutputReference":
        return typing.cast("DataAwsLakeformationPermissionsDatabaseOutputReference", jsii.get(self, "database"))

    @builtins.property
    @jsii.member(jsii_name="dataLocation")
    def data_location(
        self,
    ) -> "DataAwsLakeformationPermissionsDataLocationOutputReference":
        return typing.cast("DataAwsLakeformationPermissionsDataLocationOutputReference", jsii.get(self, "dataLocation"))

    @builtins.property
    @jsii.member(jsii_name="lfTag")
    def lf_tag(self) -> "DataAwsLakeformationPermissionsLfTagOutputReference":
        return typing.cast("DataAwsLakeformationPermissionsLfTagOutputReference", jsii.get(self, "lfTag"))

    @builtins.property
    @jsii.member(jsii_name="lfTagPolicy")
    def lf_tag_policy(
        self,
    ) -> "DataAwsLakeformationPermissionsLfTagPolicyOutputReference":
        return typing.cast("DataAwsLakeformationPermissionsLfTagPolicyOutputReference", jsii.get(self, "lfTagPolicy"))

    @builtins.property
    @jsii.member(jsii_name="permissions")
    def permissions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "permissions"))

    @builtins.property
    @jsii.member(jsii_name="permissionsWithGrantOption")
    def permissions_with_grant_option(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "permissionsWithGrantOption"))

    @builtins.property
    @jsii.member(jsii_name="table")
    def table(self) -> "DataAwsLakeformationPermissionsTableOutputReference":
        return typing.cast("DataAwsLakeformationPermissionsTableOutputReference", jsii.get(self, "table"))

    @builtins.property
    @jsii.member(jsii_name="tableWithColumns")
    def table_with_columns(
        self,
    ) -> "DataAwsLakeformationPermissionsTableWithColumnsOutputReference":
        return typing.cast("DataAwsLakeformationPermissionsTableWithColumnsOutputReference", jsii.get(self, "tableWithColumns"))

    @builtins.property
    @jsii.member(jsii_name="catalogIdInput")
    def catalog_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "catalogIdInput"))

    @builtins.property
    @jsii.member(jsii_name="catalogResourceInput")
    def catalog_resource_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "catalogResourceInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseInput")
    def database_input(
        self,
    ) -> typing.Optional["DataAwsLakeformationPermissionsDatabase"]:
        return typing.cast(typing.Optional["DataAwsLakeformationPermissionsDatabase"], jsii.get(self, "databaseInput"))

    @builtins.property
    @jsii.member(jsii_name="dataLocationInput")
    def data_location_input(
        self,
    ) -> typing.Optional["DataAwsLakeformationPermissionsDataLocation"]:
        return typing.cast(typing.Optional["DataAwsLakeformationPermissionsDataLocation"], jsii.get(self, "dataLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="lfTagInput")
    def lf_tag_input(self) -> typing.Optional["DataAwsLakeformationPermissionsLfTag"]:
        return typing.cast(typing.Optional["DataAwsLakeformationPermissionsLfTag"], jsii.get(self, "lfTagInput"))

    @builtins.property
    @jsii.member(jsii_name="lfTagPolicyInput")
    def lf_tag_policy_input(
        self,
    ) -> typing.Optional["DataAwsLakeformationPermissionsLfTagPolicy"]:
        return typing.cast(typing.Optional["DataAwsLakeformationPermissionsLfTagPolicy"], jsii.get(self, "lfTagPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="principalInput")
    def principal_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "principalInput"))

    @builtins.property
    @jsii.member(jsii_name="tableInput")
    def table_input(self) -> typing.Optional["DataAwsLakeformationPermissionsTable"]:
        return typing.cast(typing.Optional["DataAwsLakeformationPermissionsTable"], jsii.get(self, "tableInput"))

    @builtins.property
    @jsii.member(jsii_name="tableWithColumnsInput")
    def table_with_columns_input(
        self,
    ) -> typing.Optional["DataAwsLakeformationPermissionsTableWithColumns"]:
        return typing.cast(typing.Optional["DataAwsLakeformationPermissionsTableWithColumns"], jsii.get(self, "tableWithColumnsInput"))

    @builtins.property
    @jsii.member(jsii_name="catalogId")
    def catalog_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "catalogId"))

    @catalog_id.setter
    def catalog_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3b567cb714dacde5e7d3bc03df422c9a661c84a9bbb3b3280422d6c7d86c8b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "catalogId", value)

    @builtins.property
    @jsii.member(jsii_name="catalogResource")
    def catalog_resource(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "catalogResource"))

    @catalog_resource.setter
    def catalog_resource(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa9e226d8d6dfbc80679ffb882b239183f3b2ca0a78d44f8cb9b4e907f65630b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "catalogResource", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fedb48f178530c66224b1f3fa66ce7e9eb9ae0168efa98da032858aaa9dfb0da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="principal")
    def principal(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "principal"))

    @principal.setter
    def principal(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9262c08297d4e523847f67434bdf869589f7a658ff8a272e0ed709c8f46d949)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "principal", value)


@jsii.data_type(
    jsii_type="aws.dataAwsLakeformationPermissions.DataAwsLakeformationPermissionsConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "principal": "principal",
        "catalog_id": "catalogId",
        "catalog_resource": "catalogResource",
        "database": "database",
        "data_location": "dataLocation",
        "id": "id",
        "lf_tag": "lfTag",
        "lf_tag_policy": "lfTagPolicy",
        "table": "table",
        "table_with_columns": "tableWithColumns",
    },
)
class DataAwsLakeformationPermissionsConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        principal: builtins.str,
        catalog_id: typing.Optional[builtins.str] = None,
        catalog_resource: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        database: typing.Optional[typing.Union["DataAwsLakeformationPermissionsDatabase", typing.Dict[builtins.str, typing.Any]]] = None,
        data_location: typing.Optional[typing.Union["DataAwsLakeformationPermissionsDataLocation", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        lf_tag: typing.Optional[typing.Union["DataAwsLakeformationPermissionsLfTag", typing.Dict[builtins.str, typing.Any]]] = None,
        lf_tag_policy: typing.Optional[typing.Union["DataAwsLakeformationPermissionsLfTagPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        table: typing.Optional[typing.Union["DataAwsLakeformationPermissionsTable", typing.Dict[builtins.str, typing.Any]]] = None,
        table_with_columns: typing.Optional[typing.Union["DataAwsLakeformationPermissionsTableWithColumns", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param principal: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#principal DataAwsLakeformationPermissions#principal}.
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#catalog_id DataAwsLakeformationPermissions#catalog_id}.
        :param catalog_resource: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#catalog_resource DataAwsLakeformationPermissions#catalog_resource}.
        :param database: database block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#database DataAwsLakeformationPermissions#database}
        :param data_location: data_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#data_location DataAwsLakeformationPermissions#data_location}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#id DataAwsLakeformationPermissions#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param lf_tag: lf_tag block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#lf_tag DataAwsLakeformationPermissions#lf_tag}
        :param lf_tag_policy: lf_tag_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#lf_tag_policy DataAwsLakeformationPermissions#lf_tag_policy}
        :param table: table block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#table DataAwsLakeformationPermissions#table}
        :param table_with_columns: table_with_columns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#table_with_columns DataAwsLakeformationPermissions#table_with_columns}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(database, dict):
            database = DataAwsLakeformationPermissionsDatabase(**database)
        if isinstance(data_location, dict):
            data_location = DataAwsLakeformationPermissionsDataLocation(**data_location)
        if isinstance(lf_tag, dict):
            lf_tag = DataAwsLakeformationPermissionsLfTag(**lf_tag)
        if isinstance(lf_tag_policy, dict):
            lf_tag_policy = DataAwsLakeformationPermissionsLfTagPolicy(**lf_tag_policy)
        if isinstance(table, dict):
            table = DataAwsLakeformationPermissionsTable(**table)
        if isinstance(table_with_columns, dict):
            table_with_columns = DataAwsLakeformationPermissionsTableWithColumns(**table_with_columns)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25d0bda34847d686ad6a0b6b6194cf583ddbb0961869aec57456b053aaec989d)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument principal", value=principal, expected_type=type_hints["principal"])
            check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
            check_type(argname="argument catalog_resource", value=catalog_resource, expected_type=type_hints["catalog_resource"])
            check_type(argname="argument database", value=database, expected_type=type_hints["database"])
            check_type(argname="argument data_location", value=data_location, expected_type=type_hints["data_location"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument lf_tag", value=lf_tag, expected_type=type_hints["lf_tag"])
            check_type(argname="argument lf_tag_policy", value=lf_tag_policy, expected_type=type_hints["lf_tag_policy"])
            check_type(argname="argument table", value=table, expected_type=type_hints["table"])
            check_type(argname="argument table_with_columns", value=table_with_columns, expected_type=type_hints["table_with_columns"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "principal": principal,
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
        if catalog_id is not None:
            self._values["catalog_id"] = catalog_id
        if catalog_resource is not None:
            self._values["catalog_resource"] = catalog_resource
        if database is not None:
            self._values["database"] = database
        if data_location is not None:
            self._values["data_location"] = data_location
        if id is not None:
            self._values["id"] = id
        if lf_tag is not None:
            self._values["lf_tag"] = lf_tag
        if lf_tag_policy is not None:
            self._values["lf_tag_policy"] = lf_tag_policy
        if table is not None:
            self._values["table"] = table
        if table_with_columns is not None:
            self._values["table_with_columns"] = table_with_columns

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
    def principal(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#principal DataAwsLakeformationPermissions#principal}.'''
        result = self._values.get("principal")
        assert result is not None, "Required property 'principal' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def catalog_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#catalog_id DataAwsLakeformationPermissions#catalog_id}.'''
        result = self._values.get("catalog_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def catalog_resource(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#catalog_resource DataAwsLakeformationPermissions#catalog_resource}.'''
        result = self._values.get("catalog_resource")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def database(self) -> typing.Optional["DataAwsLakeformationPermissionsDatabase"]:
        '''database block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#database DataAwsLakeformationPermissions#database}
        '''
        result = self._values.get("database")
        return typing.cast(typing.Optional["DataAwsLakeformationPermissionsDatabase"], result)

    @builtins.property
    def data_location(
        self,
    ) -> typing.Optional["DataAwsLakeformationPermissionsDataLocation"]:
        '''data_location block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#data_location DataAwsLakeformationPermissions#data_location}
        '''
        result = self._values.get("data_location")
        return typing.cast(typing.Optional["DataAwsLakeformationPermissionsDataLocation"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#id DataAwsLakeformationPermissions#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lf_tag(self) -> typing.Optional["DataAwsLakeformationPermissionsLfTag"]:
        '''lf_tag block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#lf_tag DataAwsLakeformationPermissions#lf_tag}
        '''
        result = self._values.get("lf_tag")
        return typing.cast(typing.Optional["DataAwsLakeformationPermissionsLfTag"], result)

    @builtins.property
    def lf_tag_policy(
        self,
    ) -> typing.Optional["DataAwsLakeformationPermissionsLfTagPolicy"]:
        '''lf_tag_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#lf_tag_policy DataAwsLakeformationPermissions#lf_tag_policy}
        '''
        result = self._values.get("lf_tag_policy")
        return typing.cast(typing.Optional["DataAwsLakeformationPermissionsLfTagPolicy"], result)

    @builtins.property
    def table(self) -> typing.Optional["DataAwsLakeformationPermissionsTable"]:
        '''table block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#table DataAwsLakeformationPermissions#table}
        '''
        result = self._values.get("table")
        return typing.cast(typing.Optional["DataAwsLakeformationPermissionsTable"], result)

    @builtins.property
    def table_with_columns(
        self,
    ) -> typing.Optional["DataAwsLakeformationPermissionsTableWithColumns"]:
        '''table_with_columns block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#table_with_columns DataAwsLakeformationPermissions#table_with_columns}
        '''
        result = self._values.get("table_with_columns")
        return typing.cast(typing.Optional["DataAwsLakeformationPermissionsTableWithColumns"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsLakeformationPermissionsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.dataAwsLakeformationPermissions.DataAwsLakeformationPermissionsDataLocation",
    jsii_struct_bases=[],
    name_mapping={"arn": "arn", "catalog_id": "catalogId"},
)
class DataAwsLakeformationPermissionsDataLocation:
    def __init__(
        self,
        *,
        arn: builtins.str,
        catalog_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#arn DataAwsLakeformationPermissions#arn}.
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#catalog_id DataAwsLakeformationPermissions#catalog_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b79ab7278a7f86da9792ba7430a47ed226b20698429eca237396152546cccf5)
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "arn": arn,
        }
        if catalog_id is not None:
            self._values["catalog_id"] = catalog_id

    @builtins.property
    def arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#arn DataAwsLakeformationPermissions#arn}.'''
        result = self._values.get("arn")
        assert result is not None, "Required property 'arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def catalog_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#catalog_id DataAwsLakeformationPermissions#catalog_id}.'''
        result = self._values.get("catalog_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsLakeformationPermissionsDataLocation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsLakeformationPermissionsDataLocationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsLakeformationPermissions.DataAwsLakeformationPermissionsDataLocationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c351949d03604cd1e10a7fe510bbf671a448a8ff9ad2cdcdcffb9d474a058ef0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCatalogId")
    def reset_catalog_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCatalogId", []))

    @builtins.property
    @jsii.member(jsii_name="arnInput")
    def arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "arnInput"))

    @builtins.property
    @jsii.member(jsii_name="catalogIdInput")
    def catalog_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "catalogIdInput"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @arn.setter
    def arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77d950c5db5a9cdc5615157ad5ea8f9d5d8518f68e1d50a9b0459387cffb0d80)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "arn", value)

    @builtins.property
    @jsii.member(jsii_name="catalogId")
    def catalog_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "catalogId"))

    @catalog_id.setter
    def catalog_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98fe6cd4f02bbd57e344e9e01a70f11ecb59ea413827a9cd7fa1ccf8237172ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "catalogId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataAwsLakeformationPermissionsDataLocation]:
        return typing.cast(typing.Optional[DataAwsLakeformationPermissionsDataLocation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsLakeformationPermissionsDataLocation],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__229c74417d2dad308a7051122eae8582c222d47e39731a03842ebb0c380b4915)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dataAwsLakeformationPermissions.DataAwsLakeformationPermissionsDatabase",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "catalog_id": "catalogId"},
)
class DataAwsLakeformationPermissionsDatabase:
    def __init__(
        self,
        *,
        name: builtins.str,
        catalog_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#name DataAwsLakeformationPermissions#name}.
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#catalog_id DataAwsLakeformationPermissions#catalog_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcb42865737503f30655cb2c8d65acb381d57686c3337b71525dde8e9117d0fc)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if catalog_id is not None:
            self._values["catalog_id"] = catalog_id

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#name DataAwsLakeformationPermissions#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def catalog_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#catalog_id DataAwsLakeformationPermissions#catalog_id}.'''
        result = self._values.get("catalog_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsLakeformationPermissionsDatabase(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsLakeformationPermissionsDatabaseOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsLakeformationPermissions.DataAwsLakeformationPermissionsDatabaseOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__71955824e50c4ddc0b88481d1cc46b370cb5f7ee41b8ee9b66a381e2004cec3f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCatalogId")
    def reset_catalog_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCatalogId", []))

    @builtins.property
    @jsii.member(jsii_name="catalogIdInput")
    def catalog_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "catalogIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="catalogId")
    def catalog_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "catalogId"))

    @catalog_id.setter
    def catalog_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58eca998e5e134fdbed367df78cc2c2defcec2677780883c704cbd3854c0918c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "catalogId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dac8cccb0f70a23c6f67e979cde39c2b1550c6586df30319e0ca50809638a506)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataAwsLakeformationPermissionsDatabase]:
        return typing.cast(typing.Optional[DataAwsLakeformationPermissionsDatabase], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsLakeformationPermissionsDatabase],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c62cfba208732455aa33f05fbb048031f6a7acc5c5c42f66537204d8593c04b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dataAwsLakeformationPermissions.DataAwsLakeformationPermissionsLfTag",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "values": "values", "catalog_id": "catalogId"},
)
class DataAwsLakeformationPermissionsLfTag:
    def __init__(
        self,
        *,
        key: builtins.str,
        values: typing.Sequence[builtins.str],
        catalog_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#key DataAwsLakeformationPermissions#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#values DataAwsLakeformationPermissions#values}.
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#catalog_id DataAwsLakeformationPermissions#catalog_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbe8166527d3676b0682a2d45e2ae030e17366722351cdf5b0719bcd58b130fc)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
            check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "values": values,
        }
        if catalog_id is not None:
            self._values["catalog_id"] = catalog_id

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#key DataAwsLakeformationPermissions#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#values DataAwsLakeformationPermissions#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def catalog_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#catalog_id DataAwsLakeformationPermissions#catalog_id}.'''
        result = self._values.get("catalog_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsLakeformationPermissionsLfTag(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsLakeformationPermissionsLfTagOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsLakeformationPermissions.DataAwsLakeformationPermissionsLfTagOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5c49284193168f1b2bd62149628791a1dd8c5ba3b99e276ce297d900db901cde)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCatalogId")
    def reset_catalog_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCatalogId", []))

    @builtins.property
    @jsii.member(jsii_name="catalogIdInput")
    def catalog_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "catalogIdInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="catalogId")
    def catalog_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "catalogId"))

    @catalog_id.setter
    def catalog_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23a35820a26a6fc5721d43ede2959d507cdf50d3b858f060ce5a2cacd981ffd5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "catalogId", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5185b597d688ea072e21a37dfb65a0542a37d603c735d1a6d50908dd89b78e6d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f62f7834420eff11f698b2b016c37fb904e70aff9d9662004841754dfa6b2a35)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataAwsLakeformationPermissionsLfTag]:
        return typing.cast(typing.Optional[DataAwsLakeformationPermissionsLfTag], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsLakeformationPermissionsLfTag],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95c6a1a6abbeb0b3fcc1975812d1f2f7677d0b8b6c76da474e00607482bf6967)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dataAwsLakeformationPermissions.DataAwsLakeformationPermissionsLfTagPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "expression": "expression",
        "resource_type": "resourceType",
        "catalog_id": "catalogId",
    },
)
class DataAwsLakeformationPermissionsLfTagPolicy:
    def __init__(
        self,
        *,
        expression: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAwsLakeformationPermissionsLfTagPolicyExpression", typing.Dict[builtins.str, typing.Any]]]],
        resource_type: builtins.str,
        catalog_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param expression: expression block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#expression DataAwsLakeformationPermissions#expression}
        :param resource_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#resource_type DataAwsLakeformationPermissions#resource_type}.
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#catalog_id DataAwsLakeformationPermissions#catalog_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33b9b6894ae10fb2ae3f0ae8fa15fe01ebbc2f9d5f6c07f3b03a062f5f7e5a23)
            check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
            check_type(argname="argument resource_type", value=resource_type, expected_type=type_hints["resource_type"])
            check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "expression": expression,
            "resource_type": resource_type,
        }
        if catalog_id is not None:
            self._values["catalog_id"] = catalog_id

    @builtins.property
    def expression(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAwsLakeformationPermissionsLfTagPolicyExpression"]]:
        '''expression block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#expression DataAwsLakeformationPermissions#expression}
        '''
        result = self._values.get("expression")
        assert result is not None, "Required property 'expression' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAwsLakeformationPermissionsLfTagPolicyExpression"]], result)

    @builtins.property
    def resource_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#resource_type DataAwsLakeformationPermissions#resource_type}.'''
        result = self._values.get("resource_type")
        assert result is not None, "Required property 'resource_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def catalog_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#catalog_id DataAwsLakeformationPermissions#catalog_id}.'''
        result = self._values.get("catalog_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsLakeformationPermissionsLfTagPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.dataAwsLakeformationPermissions.DataAwsLakeformationPermissionsLfTagPolicyExpression",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "values": "values"},
)
class DataAwsLakeformationPermissionsLfTagPolicyExpression:
    def __init__(
        self,
        *,
        key: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#key DataAwsLakeformationPermissions#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#values DataAwsLakeformationPermissions#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a42a2224a167d23aef979bd3479e41f72120707401c84e623a76894185d5dd29)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "values": values,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#key DataAwsLakeformationPermissions#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#values DataAwsLakeformationPermissions#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsLakeformationPermissionsLfTagPolicyExpression(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsLakeformationPermissionsLfTagPolicyExpressionList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsLakeformationPermissions.DataAwsLakeformationPermissionsLfTagPolicyExpressionList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d16b8fe9cab11fa71b8b0da1334c20af96d73ff6935ce596c54c65e5cf0152c0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAwsLakeformationPermissionsLfTagPolicyExpressionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6195863d9b4cb36eda21d9f7d018ce2642a2a0809a08336aa03c8a01911a79df)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsLakeformationPermissionsLfTagPolicyExpressionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d053a2ab6e9bfdfd9ff2305c701710ac1e9ba7bfa3f2de04fd7654aebea8499b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b93c42f2c95a008db00ddbdc3448a358d9c316f0dba8e8c7ce51a9a0aad4ce94)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2e2efedceb611e894f7647282af1d47b9f57e4c339b58286f1ba30e0a345abd6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsLakeformationPermissionsLfTagPolicyExpression]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsLakeformationPermissionsLfTagPolicyExpression]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsLakeformationPermissionsLfTagPolicyExpression]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__634d1f8b1bea4ba808e739a299e7edea5b755741986c5c310c5ac893a125c76c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAwsLakeformationPermissionsLfTagPolicyExpressionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsLakeformationPermissions.DataAwsLakeformationPermissionsLfTagPolicyExpressionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__67b3567637b24f17743eca16ba64d38d6f6318c3e072e7148f6d9a8f8d7e54f8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__806b435f2413b0c7e962fbc010703ca699d0b97699501c8ecfd97a6e87dbc344)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b473c56657c54e79a117f6ee8d925073ed3e9b97e75478aa5fa00a9ab6b59743)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataAwsLakeformationPermissionsLfTagPolicyExpression, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataAwsLakeformationPermissionsLfTagPolicyExpression, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataAwsLakeformationPermissionsLfTagPolicyExpression, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0916b3239efbcf7c21f5a0a5d15a5b7e293483750daf8af400096df454666e81)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAwsLakeformationPermissionsLfTagPolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsLakeformationPermissions.DataAwsLakeformationPermissionsLfTagPolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0e3f06046c0836eecdcaac3d83df8618b78e06f0373c1095f0b8a002b038221e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putExpression")
    def put_expression(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAwsLakeformationPermissionsLfTagPolicyExpression, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94e956d5f5d0e9c8653c7b5b6de6015952d8f8050886209f126e0cb9193ad6e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putExpression", [value]))

    @jsii.member(jsii_name="resetCatalogId")
    def reset_catalog_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCatalogId", []))

    @builtins.property
    @jsii.member(jsii_name="expression")
    def expression(self) -> DataAwsLakeformationPermissionsLfTagPolicyExpressionList:
        return typing.cast(DataAwsLakeformationPermissionsLfTagPolicyExpressionList, jsii.get(self, "expression"))

    @builtins.property
    @jsii.member(jsii_name="catalogIdInput")
    def catalog_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "catalogIdInput"))

    @builtins.property
    @jsii.member(jsii_name="expressionInput")
    def expression_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsLakeformationPermissionsLfTagPolicyExpression]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsLakeformationPermissionsLfTagPolicyExpression]]], jsii.get(self, "expressionInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceTypeInput")
    def resource_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="catalogId")
    def catalog_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "catalogId"))

    @catalog_id.setter
    def catalog_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2132d9cb0c2cb465784ea3cf3aee55d28261790bd3db3855d5a9534bc2b631f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "catalogId", value)

    @builtins.property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceType"))

    @resource_type.setter
    def resource_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__988ec7c2fb9a6c6ab0be13c4f6d3dce29d285a989724c39dd2689399c82235d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataAwsLakeformationPermissionsLfTagPolicy]:
        return typing.cast(typing.Optional[DataAwsLakeformationPermissionsLfTagPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsLakeformationPermissionsLfTagPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d3d5ec39e5b0507c3a562d0edb5f1d43bbe476dba930550f0da209ebe0dd628)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dataAwsLakeformationPermissions.DataAwsLakeformationPermissionsTable",
    jsii_struct_bases=[],
    name_mapping={
        "database_name": "databaseName",
        "catalog_id": "catalogId",
        "name": "name",
        "wildcard": "wildcard",
    },
)
class DataAwsLakeformationPermissionsTable:
    def __init__(
        self,
        *,
        database_name: builtins.str,
        catalog_id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        wildcard: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#database_name DataAwsLakeformationPermissions#database_name}.
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#catalog_id DataAwsLakeformationPermissions#catalog_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#name DataAwsLakeformationPermissions#name}.
        :param wildcard: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#wildcard DataAwsLakeformationPermissions#wildcard}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d03971f3f2024ae3df3b1e4b631b333e0ba3de89414b6f08e969ccf9c52f7f9a)
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument wildcard", value=wildcard, expected_type=type_hints["wildcard"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "database_name": database_name,
        }
        if catalog_id is not None:
            self._values["catalog_id"] = catalog_id
        if name is not None:
            self._values["name"] = name
        if wildcard is not None:
            self._values["wildcard"] = wildcard

    @builtins.property
    def database_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#database_name DataAwsLakeformationPermissions#database_name}.'''
        result = self._values.get("database_name")
        assert result is not None, "Required property 'database_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def catalog_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#catalog_id DataAwsLakeformationPermissions#catalog_id}.'''
        result = self._values.get("catalog_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#name DataAwsLakeformationPermissions#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def wildcard(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#wildcard DataAwsLakeformationPermissions#wildcard}.'''
        result = self._values.get("wildcard")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsLakeformationPermissionsTable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsLakeformationPermissionsTableOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsLakeformationPermissions.DataAwsLakeformationPermissionsTableOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d3dd6838a6ad6d2451df1e1333a5730c695ac81ced3b5ab9e98c6265e184375b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCatalogId")
    def reset_catalog_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCatalogId", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetWildcard")
    def reset_wildcard(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWildcard", []))

    @builtins.property
    @jsii.member(jsii_name="catalogIdInput")
    def catalog_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "catalogIdInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseNameInput")
    def database_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseNameInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="wildcardInput")
    def wildcard_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "wildcardInput"))

    @builtins.property
    @jsii.member(jsii_name="catalogId")
    def catalog_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "catalogId"))

    @catalog_id.setter
    def catalog_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c709835ca9d3fe1b24c4966c227f6355604e94ecea23d64f641072f89aceb27c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "catalogId", value)

    @builtins.property
    @jsii.member(jsii_name="databaseName")
    def database_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseName"))

    @database_name.setter
    def database_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b916b2621c9ae47aba9bcf0d2fab2b601bdf246e806a087b1d17a9d1cea7e3e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseName", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__587a4a1339da491772cfa038ef07f479c72c2842a0d512844bd6648e4e5b9037)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="wildcard")
    def wildcard(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "wildcard"))

    @wildcard.setter
    def wildcard(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec7b3e838c35566a6b49529d7bd02161af653150a4cc09ddb3cf920f21442df8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wildcard", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataAwsLakeformationPermissionsTable]:
        return typing.cast(typing.Optional[DataAwsLakeformationPermissionsTable], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsLakeformationPermissionsTable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22d40897c2676a3b4b34c658482129e2b428e26b086a9327bb017aa97c9f3bd8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dataAwsLakeformationPermissions.DataAwsLakeformationPermissionsTableWithColumns",
    jsii_struct_bases=[],
    name_mapping={
        "database_name": "databaseName",
        "name": "name",
        "catalog_id": "catalogId",
        "column_names": "columnNames",
        "excluded_column_names": "excludedColumnNames",
        "wildcard": "wildcard",
    },
)
class DataAwsLakeformationPermissionsTableWithColumns:
    def __init__(
        self,
        *,
        database_name: builtins.str,
        name: builtins.str,
        catalog_id: typing.Optional[builtins.str] = None,
        column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        excluded_column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        wildcard: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#database_name DataAwsLakeformationPermissions#database_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#name DataAwsLakeformationPermissions#name}.
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#catalog_id DataAwsLakeformationPermissions#catalog_id}.
        :param column_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#column_names DataAwsLakeformationPermissions#column_names}.
        :param excluded_column_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#excluded_column_names DataAwsLakeformationPermissions#excluded_column_names}.
        :param wildcard: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#wildcard DataAwsLakeformationPermissions#wildcard}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ced8b901b023268c5b22e206cd2562d196a2ea62fdc3f0bd00419d1d611f5b74)
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
            check_type(argname="argument column_names", value=column_names, expected_type=type_hints["column_names"])
            check_type(argname="argument excluded_column_names", value=excluded_column_names, expected_type=type_hints["excluded_column_names"])
            check_type(argname="argument wildcard", value=wildcard, expected_type=type_hints["wildcard"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "database_name": database_name,
            "name": name,
        }
        if catalog_id is not None:
            self._values["catalog_id"] = catalog_id
        if column_names is not None:
            self._values["column_names"] = column_names
        if excluded_column_names is not None:
            self._values["excluded_column_names"] = excluded_column_names
        if wildcard is not None:
            self._values["wildcard"] = wildcard

    @builtins.property
    def database_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#database_name DataAwsLakeformationPermissions#database_name}.'''
        result = self._values.get("database_name")
        assert result is not None, "Required property 'database_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#name DataAwsLakeformationPermissions#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def catalog_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#catalog_id DataAwsLakeformationPermissions#catalog_id}.'''
        result = self._values.get("catalog_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def column_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#column_names DataAwsLakeformationPermissions#column_names}.'''
        result = self._values.get("column_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def excluded_column_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#excluded_column_names DataAwsLakeformationPermissions#excluded_column_names}.'''
        result = self._values.get("excluded_column_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def wildcard(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/lakeformation_permissions#wildcard DataAwsLakeformationPermissions#wildcard}.'''
        result = self._values.get("wildcard")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsLakeformationPermissionsTableWithColumns(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsLakeformationPermissionsTableWithColumnsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsLakeformationPermissions.DataAwsLakeformationPermissionsTableWithColumnsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8785fbfaa7e9db4dbe693e0feb2610bef65b25b8718399da787b96e018b9d95b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCatalogId")
    def reset_catalog_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCatalogId", []))

    @jsii.member(jsii_name="resetColumnNames")
    def reset_column_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetColumnNames", []))

    @jsii.member(jsii_name="resetExcludedColumnNames")
    def reset_excluded_column_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcludedColumnNames", []))

    @jsii.member(jsii_name="resetWildcard")
    def reset_wildcard(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWildcard", []))

    @builtins.property
    @jsii.member(jsii_name="catalogIdInput")
    def catalog_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "catalogIdInput"))

    @builtins.property
    @jsii.member(jsii_name="columnNamesInput")
    def column_names_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "columnNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseNameInput")
    def database_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseNameInput"))

    @builtins.property
    @jsii.member(jsii_name="excludedColumnNamesInput")
    def excluded_column_names_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "excludedColumnNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="wildcardInput")
    def wildcard_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "wildcardInput"))

    @builtins.property
    @jsii.member(jsii_name="catalogId")
    def catalog_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "catalogId"))

    @catalog_id.setter
    def catalog_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bf487ba05071bbfb3344d3a5130703ce0693187f75c3deb62c1f2b2627b5e5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "catalogId", value)

    @builtins.property
    @jsii.member(jsii_name="columnNames")
    def column_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "columnNames"))

    @column_names.setter
    def column_names(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9a77e69a91cbea511d59bcc49fe036e90cdb3e2014d3c78bc158594e4df1d39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "columnNames", value)

    @builtins.property
    @jsii.member(jsii_name="databaseName")
    def database_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseName"))

    @database_name.setter
    def database_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45d25fd8bb9a1bfef3fd21527d182425daf9081d83c82a7cdb23486ee2f260f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseName", value)

    @builtins.property
    @jsii.member(jsii_name="excludedColumnNames")
    def excluded_column_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "excludedColumnNames"))

    @excluded_column_names.setter
    def excluded_column_names(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3276a1525caec6a6c0d497c7d88a961106ecf3c9075ee164baedb9e30b9fb10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "excludedColumnNames", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af766098309980cc8102c4b0e493e5621b519c5754e5cb8a631e9da332d9dadf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="wildcard")
    def wildcard(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "wildcard"))

    @wildcard.setter
    def wildcard(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__598ea2e93db899ceac2601ee83c3a4ca8726aba2221dea4cfd4fdd1efa982cbf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wildcard", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataAwsLakeformationPermissionsTableWithColumns]:
        return typing.cast(typing.Optional[DataAwsLakeformationPermissionsTableWithColumns], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsLakeformationPermissionsTableWithColumns],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__184c6b8de80b0bcbec47a9090191533cbb18700e313e25948cc8f29d6f655abf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataAwsLakeformationPermissions",
    "DataAwsLakeformationPermissionsConfig",
    "DataAwsLakeformationPermissionsDataLocation",
    "DataAwsLakeformationPermissionsDataLocationOutputReference",
    "DataAwsLakeformationPermissionsDatabase",
    "DataAwsLakeformationPermissionsDatabaseOutputReference",
    "DataAwsLakeformationPermissionsLfTag",
    "DataAwsLakeformationPermissionsLfTagOutputReference",
    "DataAwsLakeformationPermissionsLfTagPolicy",
    "DataAwsLakeformationPermissionsLfTagPolicyExpression",
    "DataAwsLakeformationPermissionsLfTagPolicyExpressionList",
    "DataAwsLakeformationPermissionsLfTagPolicyExpressionOutputReference",
    "DataAwsLakeformationPermissionsLfTagPolicyOutputReference",
    "DataAwsLakeformationPermissionsTable",
    "DataAwsLakeformationPermissionsTableOutputReference",
    "DataAwsLakeformationPermissionsTableWithColumns",
    "DataAwsLakeformationPermissionsTableWithColumnsOutputReference",
]

publication.publish()

def _typecheckingstub__0fd8454cce1328fb5dbe9926364295f5d1f4867a4f84f172d518d8ed2719040c(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    principal: builtins.str,
    catalog_id: typing.Optional[builtins.str] = None,
    catalog_resource: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    database: typing.Optional[typing.Union[DataAwsLakeformationPermissionsDatabase, typing.Dict[builtins.str, typing.Any]]] = None,
    data_location: typing.Optional[typing.Union[DataAwsLakeformationPermissionsDataLocation, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    lf_tag: typing.Optional[typing.Union[DataAwsLakeformationPermissionsLfTag, typing.Dict[builtins.str, typing.Any]]] = None,
    lf_tag_policy: typing.Optional[typing.Union[DataAwsLakeformationPermissionsLfTagPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    table: typing.Optional[typing.Union[DataAwsLakeformationPermissionsTable, typing.Dict[builtins.str, typing.Any]]] = None,
    table_with_columns: typing.Optional[typing.Union[DataAwsLakeformationPermissionsTableWithColumns, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__b3b567cb714dacde5e7d3bc03df422c9a661c84a9bbb3b3280422d6c7d86c8b4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa9e226d8d6dfbc80679ffb882b239183f3b2ca0a78d44f8cb9b4e907f65630b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fedb48f178530c66224b1f3fa66ce7e9eb9ae0168efa98da032858aaa9dfb0da(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9262c08297d4e523847f67434bdf869589f7a658ff8a272e0ed709c8f46d949(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25d0bda34847d686ad6a0b6b6194cf583ddbb0961869aec57456b053aaec989d(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    principal: builtins.str,
    catalog_id: typing.Optional[builtins.str] = None,
    catalog_resource: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    database: typing.Optional[typing.Union[DataAwsLakeformationPermissionsDatabase, typing.Dict[builtins.str, typing.Any]]] = None,
    data_location: typing.Optional[typing.Union[DataAwsLakeformationPermissionsDataLocation, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    lf_tag: typing.Optional[typing.Union[DataAwsLakeformationPermissionsLfTag, typing.Dict[builtins.str, typing.Any]]] = None,
    lf_tag_policy: typing.Optional[typing.Union[DataAwsLakeformationPermissionsLfTagPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    table: typing.Optional[typing.Union[DataAwsLakeformationPermissionsTable, typing.Dict[builtins.str, typing.Any]]] = None,
    table_with_columns: typing.Optional[typing.Union[DataAwsLakeformationPermissionsTableWithColumns, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b79ab7278a7f86da9792ba7430a47ed226b20698429eca237396152546cccf5(
    *,
    arn: builtins.str,
    catalog_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c351949d03604cd1e10a7fe510bbf671a448a8ff9ad2cdcdcffb9d474a058ef0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77d950c5db5a9cdc5615157ad5ea8f9d5d8518f68e1d50a9b0459387cffb0d80(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98fe6cd4f02bbd57e344e9e01a70f11ecb59ea413827a9cd7fa1ccf8237172ac(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__229c74417d2dad308a7051122eae8582c222d47e39731a03842ebb0c380b4915(
    value: typing.Optional[DataAwsLakeformationPermissionsDataLocation],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcb42865737503f30655cb2c8d65acb381d57686c3337b71525dde8e9117d0fc(
    *,
    name: builtins.str,
    catalog_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71955824e50c4ddc0b88481d1cc46b370cb5f7ee41b8ee9b66a381e2004cec3f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58eca998e5e134fdbed367df78cc2c2defcec2677780883c704cbd3854c0918c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dac8cccb0f70a23c6f67e979cde39c2b1550c6586df30319e0ca50809638a506(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c62cfba208732455aa33f05fbb048031f6a7acc5c5c42f66537204d8593c04b(
    value: typing.Optional[DataAwsLakeformationPermissionsDatabase],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbe8166527d3676b0682a2d45e2ae030e17366722351cdf5b0719bcd58b130fc(
    *,
    key: builtins.str,
    values: typing.Sequence[builtins.str],
    catalog_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c49284193168f1b2bd62149628791a1dd8c5ba3b99e276ce297d900db901cde(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23a35820a26a6fc5721d43ede2959d507cdf50d3b858f060ce5a2cacd981ffd5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5185b597d688ea072e21a37dfb65a0542a37d603c735d1a6d50908dd89b78e6d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f62f7834420eff11f698b2b016c37fb904e70aff9d9662004841754dfa6b2a35(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95c6a1a6abbeb0b3fcc1975812d1f2f7677d0b8b6c76da474e00607482bf6967(
    value: typing.Optional[DataAwsLakeformationPermissionsLfTag],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33b9b6894ae10fb2ae3f0ae8fa15fe01ebbc2f9d5f6c07f3b03a062f5f7e5a23(
    *,
    expression: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAwsLakeformationPermissionsLfTagPolicyExpression, typing.Dict[builtins.str, typing.Any]]]],
    resource_type: builtins.str,
    catalog_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a42a2224a167d23aef979bd3479e41f72120707401c84e623a76894185d5dd29(
    *,
    key: builtins.str,
    values: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d16b8fe9cab11fa71b8b0da1334c20af96d73ff6935ce596c54c65e5cf0152c0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6195863d9b4cb36eda21d9f7d018ce2642a2a0809a08336aa03c8a01911a79df(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d053a2ab6e9bfdfd9ff2305c701710ac1e9ba7bfa3f2de04fd7654aebea8499b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b93c42f2c95a008db00ddbdc3448a358d9c316f0dba8e8c7ce51a9a0aad4ce94(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e2efedceb611e894f7647282af1d47b9f57e4c339b58286f1ba30e0a345abd6(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__634d1f8b1bea4ba808e739a299e7edea5b755741986c5c310c5ac893a125c76c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsLakeformationPermissionsLfTagPolicyExpression]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67b3567637b24f17743eca16ba64d38d6f6318c3e072e7148f6d9a8f8d7e54f8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__806b435f2413b0c7e962fbc010703ca699d0b97699501c8ecfd97a6e87dbc344(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b473c56657c54e79a117f6ee8d925073ed3e9b97e75478aa5fa00a9ab6b59743(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0916b3239efbcf7c21f5a0a5d15a5b7e293483750daf8af400096df454666e81(
    value: typing.Optional[typing.Union[DataAwsLakeformationPermissionsLfTagPolicyExpression, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e3f06046c0836eecdcaac3d83df8618b78e06f0373c1095f0b8a002b038221e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94e956d5f5d0e9c8653c7b5b6de6015952d8f8050886209f126e0cb9193ad6e3(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAwsLakeformationPermissionsLfTagPolicyExpression, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2132d9cb0c2cb465784ea3cf3aee55d28261790bd3db3855d5a9534bc2b631f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__988ec7c2fb9a6c6ab0be13c4f6d3dce29d285a989724c39dd2689399c82235d6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d3d5ec39e5b0507c3a562d0edb5f1d43bbe476dba930550f0da209ebe0dd628(
    value: typing.Optional[DataAwsLakeformationPermissionsLfTagPolicy],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d03971f3f2024ae3df3b1e4b631b333e0ba3de89414b6f08e969ccf9c52f7f9a(
    *,
    database_name: builtins.str,
    catalog_id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    wildcard: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3dd6838a6ad6d2451df1e1333a5730c695ac81ced3b5ab9e98c6265e184375b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c709835ca9d3fe1b24c4966c227f6355604e94ecea23d64f641072f89aceb27c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b916b2621c9ae47aba9bcf0d2fab2b601bdf246e806a087b1d17a9d1cea7e3e2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__587a4a1339da491772cfa038ef07f479c72c2842a0d512844bd6648e4e5b9037(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec7b3e838c35566a6b49529d7bd02161af653150a4cc09ddb3cf920f21442df8(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22d40897c2676a3b4b34c658482129e2b428e26b086a9327bb017aa97c9f3bd8(
    value: typing.Optional[DataAwsLakeformationPermissionsTable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ced8b901b023268c5b22e206cd2562d196a2ea62fdc3f0bd00419d1d611f5b74(
    *,
    database_name: builtins.str,
    name: builtins.str,
    catalog_id: typing.Optional[builtins.str] = None,
    column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    excluded_column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    wildcard: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8785fbfaa7e9db4dbe693e0feb2610bef65b25b8718399da787b96e018b9d95b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bf487ba05071bbfb3344d3a5130703ce0693187f75c3deb62c1f2b2627b5e5a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9a77e69a91cbea511d59bcc49fe036e90cdb3e2014d3c78bc158594e4df1d39(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45d25fd8bb9a1bfef3fd21527d182425daf9081d83c82a7cdb23486ee2f260f5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3276a1525caec6a6c0d497c7d88a961106ecf3c9075ee164baedb9e30b9fb10(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af766098309980cc8102c4b0e493e5621b519c5754e5cb8a631e9da332d9dadf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__598ea2e93db899ceac2601ee83c3a4ca8726aba2221dea4cfd4fdd1efa982cbf(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__184c6b8de80b0bcbec47a9090191533cbb18700e313e25948cc8f29d6f655abf(
    value: typing.Optional[DataAwsLakeformationPermissionsTableWithColumns],
) -> None:
    """Type checking stubs"""
    pass
