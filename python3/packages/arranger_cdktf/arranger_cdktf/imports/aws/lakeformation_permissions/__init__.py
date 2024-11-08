'''
# `aws_lakeformation_permissions`

Refer to the Terraform Registory for docs: [`aws_lakeformation_permissions`](https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions).
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


class LakeformationPermissions(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lakeformationPermissions.LakeformationPermissions",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions aws_lakeformation_permissions}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        permissions: typing.Sequence[builtins.str],
        principal: builtins.str,
        catalog_id: typing.Optional[builtins.str] = None,
        catalog_resource: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        database: typing.Optional[typing.Union["LakeformationPermissionsDatabase", typing.Dict[builtins.str, typing.Any]]] = None,
        data_location: typing.Optional[typing.Union["LakeformationPermissionsDataLocation", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        lf_tag: typing.Optional[typing.Union["LakeformationPermissionsLfTag", typing.Dict[builtins.str, typing.Any]]] = None,
        lf_tag_policy: typing.Optional[typing.Union["LakeformationPermissionsLfTagPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        permissions_with_grant_option: typing.Optional[typing.Sequence[builtins.str]] = None,
        table: typing.Optional[typing.Union["LakeformationPermissionsTable", typing.Dict[builtins.str, typing.Any]]] = None,
        table_with_columns: typing.Optional[typing.Union["LakeformationPermissionsTableWithColumns", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions aws_lakeformation_permissions} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param permissions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#permissions LakeformationPermissions#permissions}.
        :param principal: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#principal LakeformationPermissions#principal}.
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#catalog_id LakeformationPermissions#catalog_id}.
        :param catalog_resource: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#catalog_resource LakeformationPermissions#catalog_resource}.
        :param database: database block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#database LakeformationPermissions#database}
        :param data_location: data_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#data_location LakeformationPermissions#data_location}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#id LakeformationPermissions#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param lf_tag: lf_tag block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#lf_tag LakeformationPermissions#lf_tag}
        :param lf_tag_policy: lf_tag_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#lf_tag_policy LakeformationPermissions#lf_tag_policy}
        :param permissions_with_grant_option: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#permissions_with_grant_option LakeformationPermissions#permissions_with_grant_option}.
        :param table: table block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#table LakeformationPermissions#table}
        :param table_with_columns: table_with_columns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#table_with_columns LakeformationPermissions#table_with_columns}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abc098ffcafe14bdec2dcc73d451f5e9a0139ea9e7750d83242392e8eefa3c64)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = LakeformationPermissionsConfig(
            permissions=permissions,
            principal=principal,
            catalog_id=catalog_id,
            catalog_resource=catalog_resource,
            database=database,
            data_location=data_location,
            id=id,
            lf_tag=lf_tag,
            lf_tag_policy=lf_tag_policy,
            permissions_with_grant_option=permissions_with_grant_option,
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
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#name LakeformationPermissions#name}.
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#catalog_id LakeformationPermissions#catalog_id}.
        '''
        value = LakeformationPermissionsDatabase(name=name, catalog_id=catalog_id)

        return typing.cast(None, jsii.invoke(self, "putDatabase", [value]))

    @jsii.member(jsii_name="putDataLocation")
    def put_data_location(
        self,
        *,
        arn: builtins.str,
        catalog_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#arn LakeformationPermissions#arn}.
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#catalog_id LakeformationPermissions#catalog_id}.
        '''
        value = LakeformationPermissionsDataLocation(arn=arn, catalog_id=catalog_id)

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
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#key LakeformationPermissions#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#values LakeformationPermissions#values}.
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#catalog_id LakeformationPermissions#catalog_id}.
        '''
        value = LakeformationPermissionsLfTag(
            key=key, values=values, catalog_id=catalog_id
        )

        return typing.cast(None, jsii.invoke(self, "putLfTag", [value]))

    @jsii.member(jsii_name="putLfTagPolicy")
    def put_lf_tag_policy(
        self,
        *,
        expression: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LakeformationPermissionsLfTagPolicyExpression", typing.Dict[builtins.str, typing.Any]]]],
        resource_type: builtins.str,
        catalog_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param expression: expression block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#expression LakeformationPermissions#expression}
        :param resource_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#resource_type LakeformationPermissions#resource_type}.
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#catalog_id LakeformationPermissions#catalog_id}.
        '''
        value = LakeformationPermissionsLfTagPolicy(
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
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#database_name LakeformationPermissions#database_name}.
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#catalog_id LakeformationPermissions#catalog_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#name LakeformationPermissions#name}.
        :param wildcard: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#wildcard LakeformationPermissions#wildcard}.
        '''
        value = LakeformationPermissionsTable(
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
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#database_name LakeformationPermissions#database_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#name LakeformationPermissions#name}.
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#catalog_id LakeformationPermissions#catalog_id}.
        :param column_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#column_names LakeformationPermissions#column_names}.
        :param excluded_column_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#excluded_column_names LakeformationPermissions#excluded_column_names}.
        :param wildcard: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#wildcard LakeformationPermissions#wildcard}.
        '''
        value = LakeformationPermissionsTableWithColumns(
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

    @jsii.member(jsii_name="resetPermissionsWithGrantOption")
    def reset_permissions_with_grant_option(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPermissionsWithGrantOption", []))

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
    def database(self) -> "LakeformationPermissionsDatabaseOutputReference":
        return typing.cast("LakeformationPermissionsDatabaseOutputReference", jsii.get(self, "database"))

    @builtins.property
    @jsii.member(jsii_name="dataLocation")
    def data_location(self) -> "LakeformationPermissionsDataLocationOutputReference":
        return typing.cast("LakeformationPermissionsDataLocationOutputReference", jsii.get(self, "dataLocation"))

    @builtins.property
    @jsii.member(jsii_name="lfTag")
    def lf_tag(self) -> "LakeformationPermissionsLfTagOutputReference":
        return typing.cast("LakeformationPermissionsLfTagOutputReference", jsii.get(self, "lfTag"))

    @builtins.property
    @jsii.member(jsii_name="lfTagPolicy")
    def lf_tag_policy(self) -> "LakeformationPermissionsLfTagPolicyOutputReference":
        return typing.cast("LakeformationPermissionsLfTagPolicyOutputReference", jsii.get(self, "lfTagPolicy"))

    @builtins.property
    @jsii.member(jsii_name="table")
    def table(self) -> "LakeformationPermissionsTableOutputReference":
        return typing.cast("LakeformationPermissionsTableOutputReference", jsii.get(self, "table"))

    @builtins.property
    @jsii.member(jsii_name="tableWithColumns")
    def table_with_columns(
        self,
    ) -> "LakeformationPermissionsTableWithColumnsOutputReference":
        return typing.cast("LakeformationPermissionsTableWithColumnsOutputReference", jsii.get(self, "tableWithColumns"))

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
    def database_input(self) -> typing.Optional["LakeformationPermissionsDatabase"]:
        return typing.cast(typing.Optional["LakeformationPermissionsDatabase"], jsii.get(self, "databaseInput"))

    @builtins.property
    @jsii.member(jsii_name="dataLocationInput")
    def data_location_input(
        self,
    ) -> typing.Optional["LakeformationPermissionsDataLocation"]:
        return typing.cast(typing.Optional["LakeformationPermissionsDataLocation"], jsii.get(self, "dataLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="lfTagInput")
    def lf_tag_input(self) -> typing.Optional["LakeformationPermissionsLfTag"]:
        return typing.cast(typing.Optional["LakeformationPermissionsLfTag"], jsii.get(self, "lfTagInput"))

    @builtins.property
    @jsii.member(jsii_name="lfTagPolicyInput")
    def lf_tag_policy_input(
        self,
    ) -> typing.Optional["LakeformationPermissionsLfTagPolicy"]:
        return typing.cast(typing.Optional["LakeformationPermissionsLfTagPolicy"], jsii.get(self, "lfTagPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="permissionsInput")
    def permissions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "permissionsInput"))

    @builtins.property
    @jsii.member(jsii_name="permissionsWithGrantOptionInput")
    def permissions_with_grant_option_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "permissionsWithGrantOptionInput"))

    @builtins.property
    @jsii.member(jsii_name="principalInput")
    def principal_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "principalInput"))

    @builtins.property
    @jsii.member(jsii_name="tableInput")
    def table_input(self) -> typing.Optional["LakeformationPermissionsTable"]:
        return typing.cast(typing.Optional["LakeformationPermissionsTable"], jsii.get(self, "tableInput"))

    @builtins.property
    @jsii.member(jsii_name="tableWithColumnsInput")
    def table_with_columns_input(
        self,
    ) -> typing.Optional["LakeformationPermissionsTableWithColumns"]:
        return typing.cast(typing.Optional["LakeformationPermissionsTableWithColumns"], jsii.get(self, "tableWithColumnsInput"))

    @builtins.property
    @jsii.member(jsii_name="catalogId")
    def catalog_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "catalogId"))

    @catalog_id.setter
    def catalog_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__928dd54c4d8d8a11c0904678adeaf4a171a5e9d3aa3927047bbffdb13a56f6d1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__53bbfe0dfbf99dfb3e8446ef4bd795a02db517bff851b1a5a9fd49b681798769)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "catalogResource", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed8293d696d18a9882c531e09759305338f2e19ed505f8a0a45ff50047fa0183)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="permissions")
    def permissions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "permissions"))

    @permissions.setter
    def permissions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f8425d026e46260199268d53b3f7a9bca2712e4ab19bf8998794d36e43ba3cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissions", value)

    @builtins.property
    @jsii.member(jsii_name="permissionsWithGrantOption")
    def permissions_with_grant_option(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "permissionsWithGrantOption"))

    @permissions_with_grant_option.setter
    def permissions_with_grant_option(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5319ee914919d0b4ea936d4ef2942c8f5fa7b91db1c5776dfdce4a54ffbacb67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissionsWithGrantOption", value)

    @builtins.property
    @jsii.member(jsii_name="principal")
    def principal(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "principal"))

    @principal.setter
    def principal(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efcab12f199415d7cebd5e6a096e952b18de222dc304541150f25c77ce6dd3ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "principal", value)


@jsii.data_type(
    jsii_type="aws.lakeformationPermissions.LakeformationPermissionsConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "permissions": "permissions",
        "principal": "principal",
        "catalog_id": "catalogId",
        "catalog_resource": "catalogResource",
        "database": "database",
        "data_location": "dataLocation",
        "id": "id",
        "lf_tag": "lfTag",
        "lf_tag_policy": "lfTagPolicy",
        "permissions_with_grant_option": "permissionsWithGrantOption",
        "table": "table",
        "table_with_columns": "tableWithColumns",
    },
)
class LakeformationPermissionsConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        permissions: typing.Sequence[builtins.str],
        principal: builtins.str,
        catalog_id: typing.Optional[builtins.str] = None,
        catalog_resource: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        database: typing.Optional[typing.Union["LakeformationPermissionsDatabase", typing.Dict[builtins.str, typing.Any]]] = None,
        data_location: typing.Optional[typing.Union["LakeformationPermissionsDataLocation", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        lf_tag: typing.Optional[typing.Union["LakeformationPermissionsLfTag", typing.Dict[builtins.str, typing.Any]]] = None,
        lf_tag_policy: typing.Optional[typing.Union["LakeformationPermissionsLfTagPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        permissions_with_grant_option: typing.Optional[typing.Sequence[builtins.str]] = None,
        table: typing.Optional[typing.Union["LakeformationPermissionsTable", typing.Dict[builtins.str, typing.Any]]] = None,
        table_with_columns: typing.Optional[typing.Union["LakeformationPermissionsTableWithColumns", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param permissions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#permissions LakeformationPermissions#permissions}.
        :param principal: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#principal LakeformationPermissions#principal}.
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#catalog_id LakeformationPermissions#catalog_id}.
        :param catalog_resource: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#catalog_resource LakeformationPermissions#catalog_resource}.
        :param database: database block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#database LakeformationPermissions#database}
        :param data_location: data_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#data_location LakeformationPermissions#data_location}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#id LakeformationPermissions#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param lf_tag: lf_tag block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#lf_tag LakeformationPermissions#lf_tag}
        :param lf_tag_policy: lf_tag_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#lf_tag_policy LakeformationPermissions#lf_tag_policy}
        :param permissions_with_grant_option: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#permissions_with_grant_option LakeformationPermissions#permissions_with_grant_option}.
        :param table: table block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#table LakeformationPermissions#table}
        :param table_with_columns: table_with_columns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#table_with_columns LakeformationPermissions#table_with_columns}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(database, dict):
            database = LakeformationPermissionsDatabase(**database)
        if isinstance(data_location, dict):
            data_location = LakeformationPermissionsDataLocation(**data_location)
        if isinstance(lf_tag, dict):
            lf_tag = LakeformationPermissionsLfTag(**lf_tag)
        if isinstance(lf_tag_policy, dict):
            lf_tag_policy = LakeformationPermissionsLfTagPolicy(**lf_tag_policy)
        if isinstance(table, dict):
            table = LakeformationPermissionsTable(**table)
        if isinstance(table_with_columns, dict):
            table_with_columns = LakeformationPermissionsTableWithColumns(**table_with_columns)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__348e75ae5680f7d11f8b1001c033752d8616b8ca2bfe2024cc49f4738a0ee31c)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument permissions", value=permissions, expected_type=type_hints["permissions"])
            check_type(argname="argument principal", value=principal, expected_type=type_hints["principal"])
            check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
            check_type(argname="argument catalog_resource", value=catalog_resource, expected_type=type_hints["catalog_resource"])
            check_type(argname="argument database", value=database, expected_type=type_hints["database"])
            check_type(argname="argument data_location", value=data_location, expected_type=type_hints["data_location"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument lf_tag", value=lf_tag, expected_type=type_hints["lf_tag"])
            check_type(argname="argument lf_tag_policy", value=lf_tag_policy, expected_type=type_hints["lf_tag_policy"])
            check_type(argname="argument permissions_with_grant_option", value=permissions_with_grant_option, expected_type=type_hints["permissions_with_grant_option"])
            check_type(argname="argument table", value=table, expected_type=type_hints["table"])
            check_type(argname="argument table_with_columns", value=table_with_columns, expected_type=type_hints["table_with_columns"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "permissions": permissions,
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
        if permissions_with_grant_option is not None:
            self._values["permissions_with_grant_option"] = permissions_with_grant_option
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
    def permissions(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#permissions LakeformationPermissions#permissions}.'''
        result = self._values.get("permissions")
        assert result is not None, "Required property 'permissions' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def principal(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#principal LakeformationPermissions#principal}.'''
        result = self._values.get("principal")
        assert result is not None, "Required property 'principal' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def catalog_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#catalog_id LakeformationPermissions#catalog_id}.'''
        result = self._values.get("catalog_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def catalog_resource(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#catalog_resource LakeformationPermissions#catalog_resource}.'''
        result = self._values.get("catalog_resource")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def database(self) -> typing.Optional["LakeformationPermissionsDatabase"]:
        '''database block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#database LakeformationPermissions#database}
        '''
        result = self._values.get("database")
        return typing.cast(typing.Optional["LakeformationPermissionsDatabase"], result)

    @builtins.property
    def data_location(self) -> typing.Optional["LakeformationPermissionsDataLocation"]:
        '''data_location block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#data_location LakeformationPermissions#data_location}
        '''
        result = self._values.get("data_location")
        return typing.cast(typing.Optional["LakeformationPermissionsDataLocation"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#id LakeformationPermissions#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lf_tag(self) -> typing.Optional["LakeformationPermissionsLfTag"]:
        '''lf_tag block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#lf_tag LakeformationPermissions#lf_tag}
        '''
        result = self._values.get("lf_tag")
        return typing.cast(typing.Optional["LakeformationPermissionsLfTag"], result)

    @builtins.property
    def lf_tag_policy(self) -> typing.Optional["LakeformationPermissionsLfTagPolicy"]:
        '''lf_tag_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#lf_tag_policy LakeformationPermissions#lf_tag_policy}
        '''
        result = self._values.get("lf_tag_policy")
        return typing.cast(typing.Optional["LakeformationPermissionsLfTagPolicy"], result)

    @builtins.property
    def permissions_with_grant_option(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#permissions_with_grant_option LakeformationPermissions#permissions_with_grant_option}.'''
        result = self._values.get("permissions_with_grant_option")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def table(self) -> typing.Optional["LakeformationPermissionsTable"]:
        '''table block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#table LakeformationPermissions#table}
        '''
        result = self._values.get("table")
        return typing.cast(typing.Optional["LakeformationPermissionsTable"], result)

    @builtins.property
    def table_with_columns(
        self,
    ) -> typing.Optional["LakeformationPermissionsTableWithColumns"]:
        '''table_with_columns block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#table_with_columns LakeformationPermissions#table_with_columns}
        '''
        result = self._values.get("table_with_columns")
        return typing.cast(typing.Optional["LakeformationPermissionsTableWithColumns"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LakeformationPermissionsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.lakeformationPermissions.LakeformationPermissionsDataLocation",
    jsii_struct_bases=[],
    name_mapping={"arn": "arn", "catalog_id": "catalogId"},
)
class LakeformationPermissionsDataLocation:
    def __init__(
        self,
        *,
        arn: builtins.str,
        catalog_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#arn LakeformationPermissions#arn}.
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#catalog_id LakeformationPermissions#catalog_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e636fe388e629cc8e12f7096d2f06edc9b4c56cac27836a867def0c63ae56469)
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "arn": arn,
        }
        if catalog_id is not None:
            self._values["catalog_id"] = catalog_id

    @builtins.property
    def arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#arn LakeformationPermissions#arn}.'''
        result = self._values.get("arn")
        assert result is not None, "Required property 'arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def catalog_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#catalog_id LakeformationPermissions#catalog_id}.'''
        result = self._values.get("catalog_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LakeformationPermissionsDataLocation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LakeformationPermissionsDataLocationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lakeformationPermissions.LakeformationPermissionsDataLocationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2e8285d8965b2074a7de510ccfa574b0a4320097dbab1b5fb3773c7797c2c54f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1d7147c878699c94564705c7aa5914f209e9e1bebe1472f994d5a10b68eda465)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "arn", value)

    @builtins.property
    @jsii.member(jsii_name="catalogId")
    def catalog_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "catalogId"))

    @catalog_id.setter
    def catalog_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddf00d9986d4f7a29eafa323d9fd256941b9e24d8ec3cbd01391bc23b9d116fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "catalogId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LakeformationPermissionsDataLocation]:
        return typing.cast(typing.Optional[LakeformationPermissionsDataLocation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LakeformationPermissionsDataLocation],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13abdeea232c48f883345d5c2e02084f6b2e8ec50af4c0721a65ea0660ebd9f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.lakeformationPermissions.LakeformationPermissionsDatabase",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "catalog_id": "catalogId"},
)
class LakeformationPermissionsDatabase:
    def __init__(
        self,
        *,
        name: builtins.str,
        catalog_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#name LakeformationPermissions#name}.
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#catalog_id LakeformationPermissions#catalog_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac60b38c6e8865a6c22ddad4bbc4c5bbe3928096ca5695291fce0ba5ef9b4b82)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if catalog_id is not None:
            self._values["catalog_id"] = catalog_id

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#name LakeformationPermissions#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def catalog_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#catalog_id LakeformationPermissions#catalog_id}.'''
        result = self._values.get("catalog_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LakeformationPermissionsDatabase(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LakeformationPermissionsDatabaseOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lakeformationPermissions.LakeformationPermissionsDatabaseOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cf120f91f4720655970df96de325dc6353eb8abd6497d8f681d01f33021ca8d4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5564e26b7cc01b6981fe8db7ef2c4407f421c575c73478160801fdee11ef397c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "catalogId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d59f7bccdfcbeff6f3343d46163126a9d5b73f8ba5d01a0487dff73f792311b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LakeformationPermissionsDatabase]:
        return typing.cast(typing.Optional[LakeformationPermissionsDatabase], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LakeformationPermissionsDatabase],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44decfdb4b277a7c3a5127f8a1215735143750e19053c356927b146d3acd1e90)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.lakeformationPermissions.LakeformationPermissionsLfTag",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "values": "values", "catalog_id": "catalogId"},
)
class LakeformationPermissionsLfTag:
    def __init__(
        self,
        *,
        key: builtins.str,
        values: typing.Sequence[builtins.str],
        catalog_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#key LakeformationPermissions#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#values LakeformationPermissions#values}.
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#catalog_id LakeformationPermissions#catalog_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22881cbe3e0cd2ff09b365c90c23083770ffb883b74178ae83cccdfe7e89e86d)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#key LakeformationPermissions#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#values LakeformationPermissions#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def catalog_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#catalog_id LakeformationPermissions#catalog_id}.'''
        result = self._values.get("catalog_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LakeformationPermissionsLfTag(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LakeformationPermissionsLfTagOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lakeformationPermissions.LakeformationPermissionsLfTagOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__09faba71abb08c158a74edabb0aa58ac87c5e9bdce819d6755563873995fe1c2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b5579d594d709af9b5f95ca870c35500ed03ee152bc5f07903c0c032cbc5a3fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "catalogId", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1ed4a1545962b7337ef947bfe7f5eaa8f13738b33f4042a2b03456450ab38d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2dbd3eba37bd4b2acb494c77e208fa53aef8ec3507d9dc90f88a378dc1d5772)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LakeformationPermissionsLfTag]:
        return typing.cast(typing.Optional[LakeformationPermissionsLfTag], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LakeformationPermissionsLfTag],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c07ea46ab97bdee5c075ae89fa0bf7cd701decf68d119d69125e03df1c9a8b60)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.lakeformationPermissions.LakeformationPermissionsLfTagPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "expression": "expression",
        "resource_type": "resourceType",
        "catalog_id": "catalogId",
    },
)
class LakeformationPermissionsLfTagPolicy:
    def __init__(
        self,
        *,
        expression: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LakeformationPermissionsLfTagPolicyExpression", typing.Dict[builtins.str, typing.Any]]]],
        resource_type: builtins.str,
        catalog_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param expression: expression block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#expression LakeformationPermissions#expression}
        :param resource_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#resource_type LakeformationPermissions#resource_type}.
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#catalog_id LakeformationPermissions#catalog_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__988641619689f85270f878a47cf16308551c63385374248aed79f507cc127379)
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
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LakeformationPermissionsLfTagPolicyExpression"]]:
        '''expression block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#expression LakeformationPermissions#expression}
        '''
        result = self._values.get("expression")
        assert result is not None, "Required property 'expression' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LakeformationPermissionsLfTagPolicyExpression"]], result)

    @builtins.property
    def resource_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#resource_type LakeformationPermissions#resource_type}.'''
        result = self._values.get("resource_type")
        assert result is not None, "Required property 'resource_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def catalog_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#catalog_id LakeformationPermissions#catalog_id}.'''
        result = self._values.get("catalog_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LakeformationPermissionsLfTagPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.lakeformationPermissions.LakeformationPermissionsLfTagPolicyExpression",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "values": "values"},
)
class LakeformationPermissionsLfTagPolicyExpression:
    def __init__(
        self,
        *,
        key: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#key LakeformationPermissions#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#values LakeformationPermissions#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ef28e7930fb684cf06d2571f3c111618fdd48f6caad23bb1b0aee0bfd39b703)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "values": values,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#key LakeformationPermissions#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#values LakeformationPermissions#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LakeformationPermissionsLfTagPolicyExpression(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LakeformationPermissionsLfTagPolicyExpressionList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lakeformationPermissions.LakeformationPermissionsLfTagPolicyExpressionList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a323aa70932068f27eaefd3da856219a7c4ce724d50a27d5aea75f72412b4ef7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LakeformationPermissionsLfTagPolicyExpressionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__932e8ad10ee0bf07028ed10a27dabbb80107495249903a7d6c6a761b42b3e64b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LakeformationPermissionsLfTagPolicyExpressionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f3efa41692f886af9dc75a17c9b79f8857e22866779b6c9c38c2dc4140bc023)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9e2fb030d492788b73042a99b0a141a2a8c2696efffba570b809b231960b68da)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a3f7b8161569cab0a78772ca44aa9ce66402880bf239ea455ddc63c662cb2121)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LakeformationPermissionsLfTagPolicyExpression]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LakeformationPermissionsLfTagPolicyExpression]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LakeformationPermissionsLfTagPolicyExpression]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a17dfeda1404535309487ef47cd8c7b40afc1cd8ee74c742100b83dd5c2ad462)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LakeformationPermissionsLfTagPolicyExpressionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lakeformationPermissions.LakeformationPermissionsLfTagPolicyExpressionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3f2555db1b137011420d68461300c0e59e7837ca4eb246f775e19fe80bec8e50)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a20aaed97607897d09203f1d6f267d72575ad8b42c6f8ccc97316cd07aabd2d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11c022e999a78af0db837d310320f116a037c1ea8d7527660889672b537560f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LakeformationPermissionsLfTagPolicyExpression, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LakeformationPermissionsLfTagPolicyExpression, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LakeformationPermissionsLfTagPolicyExpression, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fea36ca42f8b70c94cfa0cc9c83d3453e6809693ed00253f06dab3f48cdb6d64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LakeformationPermissionsLfTagPolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lakeformationPermissions.LakeformationPermissionsLfTagPolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__203a7ae45e61cd466486e680a339bd7e63b10a6d05ced0899797f836c36d6268)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putExpression")
    def put_expression(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LakeformationPermissionsLfTagPolicyExpression, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ffaf6c2cf7d06eda96d2cb81bdd7e6b92d9d06241650787fdcd8b4d28971cc6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putExpression", [value]))

    @jsii.member(jsii_name="resetCatalogId")
    def reset_catalog_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCatalogId", []))

    @builtins.property
    @jsii.member(jsii_name="expression")
    def expression(self) -> LakeformationPermissionsLfTagPolicyExpressionList:
        return typing.cast(LakeformationPermissionsLfTagPolicyExpressionList, jsii.get(self, "expression"))

    @builtins.property
    @jsii.member(jsii_name="catalogIdInput")
    def catalog_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "catalogIdInput"))

    @builtins.property
    @jsii.member(jsii_name="expressionInput")
    def expression_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LakeformationPermissionsLfTagPolicyExpression]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LakeformationPermissionsLfTagPolicyExpression]]], jsii.get(self, "expressionInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__5727688c87326caa5f4f5da4b292430e0522a80d5be0b1938d2d483b189ce162)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "catalogId", value)

    @builtins.property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceType"))

    @resource_type.setter
    def resource_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4423c10494446c60265cad2bf0bff80ad19676d2c7a4dd3e3d4e2990aa757482)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LakeformationPermissionsLfTagPolicy]:
        return typing.cast(typing.Optional[LakeformationPermissionsLfTagPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LakeformationPermissionsLfTagPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4415ed9a262bed4784f10505c79d60664caac1a455a43b29150c3488570dd9a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.lakeformationPermissions.LakeformationPermissionsTable",
    jsii_struct_bases=[],
    name_mapping={
        "database_name": "databaseName",
        "catalog_id": "catalogId",
        "name": "name",
        "wildcard": "wildcard",
    },
)
class LakeformationPermissionsTable:
    def __init__(
        self,
        *,
        database_name: builtins.str,
        catalog_id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        wildcard: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#database_name LakeformationPermissions#database_name}.
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#catalog_id LakeformationPermissions#catalog_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#name LakeformationPermissions#name}.
        :param wildcard: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#wildcard LakeformationPermissions#wildcard}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e93577b92c23a79a50ad3762197a29154d1b82483c29fb13a690e882cd4429c8)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#database_name LakeformationPermissions#database_name}.'''
        result = self._values.get("database_name")
        assert result is not None, "Required property 'database_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def catalog_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#catalog_id LakeformationPermissions#catalog_id}.'''
        result = self._values.get("catalog_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#name LakeformationPermissions#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def wildcard(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#wildcard LakeformationPermissions#wildcard}.'''
        result = self._values.get("wildcard")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LakeformationPermissionsTable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LakeformationPermissionsTableOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lakeformationPermissions.LakeformationPermissionsTableOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__39c653c1dc57be36be65001a9e3acefd114ac3c64790be93044c227153a7c244)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ec5d76a3aa25617254b90df2ce2a943f198753efd6476404abbe47925b248bf9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "catalogId", value)

    @builtins.property
    @jsii.member(jsii_name="databaseName")
    def database_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseName"))

    @database_name.setter
    def database_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65a05b478070a794169a172c871c75302c96895798d1cc730448fd2b9182a14e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseName", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec8c820eafdb31da098b50305098797418f5203c470cc479d8370c38c7f016ce)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1fe8cb220326e9d9377679ebe966df4cbb85a49f0508ea2336bc6fce46336f36)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wildcard", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LakeformationPermissionsTable]:
        return typing.cast(typing.Optional[LakeformationPermissionsTable], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LakeformationPermissionsTable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5af5ab7e38b615a71cd0f774eebcfb96e3d89dca7444546f2b1c8c18ee1a1708)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.lakeformationPermissions.LakeformationPermissionsTableWithColumns",
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
class LakeformationPermissionsTableWithColumns:
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
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#database_name LakeformationPermissions#database_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#name LakeformationPermissions#name}.
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#catalog_id LakeformationPermissions#catalog_id}.
        :param column_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#column_names LakeformationPermissions#column_names}.
        :param excluded_column_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#excluded_column_names LakeformationPermissions#excluded_column_names}.
        :param wildcard: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#wildcard LakeformationPermissions#wildcard}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebcb44c0780159b775afb8e0539522d0b1028c5abe42acfc62deadd25926f218)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#database_name LakeformationPermissions#database_name}.'''
        result = self._values.get("database_name")
        assert result is not None, "Required property 'database_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#name LakeformationPermissions#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def catalog_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#catalog_id LakeformationPermissions#catalog_id}.'''
        result = self._values.get("catalog_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def column_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#column_names LakeformationPermissions#column_names}.'''
        result = self._values.get("column_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def excluded_column_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#excluded_column_names LakeformationPermissions#excluded_column_names}.'''
        result = self._values.get("excluded_column_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def wildcard(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lakeformation_permissions#wildcard LakeformationPermissions#wildcard}.'''
        result = self._values.get("wildcard")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LakeformationPermissionsTableWithColumns(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LakeformationPermissionsTableWithColumnsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lakeformationPermissions.LakeformationPermissionsTableWithColumnsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__359c8859eea03f6b681553436cbad919fc9462db02b8a703cb1978a7dc1eb8fd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__94b6c35ff72c2a37239fd28c91c99ebbdb68e1e23f95c4e13bb033b2433c9b7e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "catalogId", value)

    @builtins.property
    @jsii.member(jsii_name="columnNames")
    def column_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "columnNames"))

    @column_names.setter
    def column_names(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6353ced93b9cba17e0f929a833d3e2133d98c1690c5b5d9a38b70f6cdd5295f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "columnNames", value)

    @builtins.property
    @jsii.member(jsii_name="databaseName")
    def database_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseName"))

    @database_name.setter
    def database_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bca1a593ed8f92b4ed90b095eac2bf97b7a436becc957a078283d89426981254)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseName", value)

    @builtins.property
    @jsii.member(jsii_name="excludedColumnNames")
    def excluded_column_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "excludedColumnNames"))

    @excluded_column_names.setter
    def excluded_column_names(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88b73856b76020e1c2800924fdec968088cd9002c435d5b3a03ba9f3c64068c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "excludedColumnNames", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__edb9f3a0d9304fcf17582cb3d962e5ecb8accd7efe74cd739b9a6ed6a7f0d7d9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__072f4ae7fd6e287c16a0d1a77ce6ef7a6fee0614cace0ae1e8ea1baa0dbffe1f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wildcard", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LakeformationPermissionsTableWithColumns]:
        return typing.cast(typing.Optional[LakeformationPermissionsTableWithColumns], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LakeformationPermissionsTableWithColumns],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85587db98fb8d03fdea04065b83bc329b65ee693fd25e4dd3c8ba59cf8922d83)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "LakeformationPermissions",
    "LakeformationPermissionsConfig",
    "LakeformationPermissionsDataLocation",
    "LakeformationPermissionsDataLocationOutputReference",
    "LakeformationPermissionsDatabase",
    "LakeformationPermissionsDatabaseOutputReference",
    "LakeformationPermissionsLfTag",
    "LakeformationPermissionsLfTagOutputReference",
    "LakeformationPermissionsLfTagPolicy",
    "LakeformationPermissionsLfTagPolicyExpression",
    "LakeformationPermissionsLfTagPolicyExpressionList",
    "LakeformationPermissionsLfTagPolicyExpressionOutputReference",
    "LakeformationPermissionsLfTagPolicyOutputReference",
    "LakeformationPermissionsTable",
    "LakeformationPermissionsTableOutputReference",
    "LakeformationPermissionsTableWithColumns",
    "LakeformationPermissionsTableWithColumnsOutputReference",
]

publication.publish()

def _typecheckingstub__abc098ffcafe14bdec2dcc73d451f5e9a0139ea9e7750d83242392e8eefa3c64(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    permissions: typing.Sequence[builtins.str],
    principal: builtins.str,
    catalog_id: typing.Optional[builtins.str] = None,
    catalog_resource: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    database: typing.Optional[typing.Union[LakeformationPermissionsDatabase, typing.Dict[builtins.str, typing.Any]]] = None,
    data_location: typing.Optional[typing.Union[LakeformationPermissionsDataLocation, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    lf_tag: typing.Optional[typing.Union[LakeformationPermissionsLfTag, typing.Dict[builtins.str, typing.Any]]] = None,
    lf_tag_policy: typing.Optional[typing.Union[LakeformationPermissionsLfTagPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    permissions_with_grant_option: typing.Optional[typing.Sequence[builtins.str]] = None,
    table: typing.Optional[typing.Union[LakeformationPermissionsTable, typing.Dict[builtins.str, typing.Any]]] = None,
    table_with_columns: typing.Optional[typing.Union[LakeformationPermissionsTableWithColumns, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__928dd54c4d8d8a11c0904678adeaf4a171a5e9d3aa3927047bbffdb13a56f6d1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53bbfe0dfbf99dfb3e8446ef4bd795a02db517bff851b1a5a9fd49b681798769(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed8293d696d18a9882c531e09759305338f2e19ed505f8a0a45ff50047fa0183(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f8425d026e46260199268d53b3f7a9bca2712e4ab19bf8998794d36e43ba3cd(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5319ee914919d0b4ea936d4ef2942c8f5fa7b91db1c5776dfdce4a54ffbacb67(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efcab12f199415d7cebd5e6a096e952b18de222dc304541150f25c77ce6dd3ce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__348e75ae5680f7d11f8b1001c033752d8616b8ca2bfe2024cc49f4738a0ee31c(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    permissions: typing.Sequence[builtins.str],
    principal: builtins.str,
    catalog_id: typing.Optional[builtins.str] = None,
    catalog_resource: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    database: typing.Optional[typing.Union[LakeformationPermissionsDatabase, typing.Dict[builtins.str, typing.Any]]] = None,
    data_location: typing.Optional[typing.Union[LakeformationPermissionsDataLocation, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    lf_tag: typing.Optional[typing.Union[LakeformationPermissionsLfTag, typing.Dict[builtins.str, typing.Any]]] = None,
    lf_tag_policy: typing.Optional[typing.Union[LakeformationPermissionsLfTagPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    permissions_with_grant_option: typing.Optional[typing.Sequence[builtins.str]] = None,
    table: typing.Optional[typing.Union[LakeformationPermissionsTable, typing.Dict[builtins.str, typing.Any]]] = None,
    table_with_columns: typing.Optional[typing.Union[LakeformationPermissionsTableWithColumns, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e636fe388e629cc8e12f7096d2f06edc9b4c56cac27836a867def0c63ae56469(
    *,
    arn: builtins.str,
    catalog_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e8285d8965b2074a7de510ccfa574b0a4320097dbab1b5fb3773c7797c2c54f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d7147c878699c94564705c7aa5914f209e9e1bebe1472f994d5a10b68eda465(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddf00d9986d4f7a29eafa323d9fd256941b9e24d8ec3cbd01391bc23b9d116fa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13abdeea232c48f883345d5c2e02084f6b2e8ec50af4c0721a65ea0660ebd9f0(
    value: typing.Optional[LakeformationPermissionsDataLocation],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac60b38c6e8865a6c22ddad4bbc4c5bbe3928096ca5695291fce0ba5ef9b4b82(
    *,
    name: builtins.str,
    catalog_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf120f91f4720655970df96de325dc6353eb8abd6497d8f681d01f33021ca8d4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5564e26b7cc01b6981fe8db7ef2c4407f421c575c73478160801fdee11ef397c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d59f7bccdfcbeff6f3343d46163126a9d5b73f8ba5d01a0487dff73f792311b5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44decfdb4b277a7c3a5127f8a1215735143750e19053c356927b146d3acd1e90(
    value: typing.Optional[LakeformationPermissionsDatabase],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22881cbe3e0cd2ff09b365c90c23083770ffb883b74178ae83cccdfe7e89e86d(
    *,
    key: builtins.str,
    values: typing.Sequence[builtins.str],
    catalog_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09faba71abb08c158a74edabb0aa58ac87c5e9bdce819d6755563873995fe1c2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5579d594d709af9b5f95ca870c35500ed03ee152bc5f07903c0c032cbc5a3fa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1ed4a1545962b7337ef947bfe7f5eaa8f13738b33f4042a2b03456450ab38d3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2dbd3eba37bd4b2acb494c77e208fa53aef8ec3507d9dc90f88a378dc1d5772(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c07ea46ab97bdee5c075ae89fa0bf7cd701decf68d119d69125e03df1c9a8b60(
    value: typing.Optional[LakeformationPermissionsLfTag],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__988641619689f85270f878a47cf16308551c63385374248aed79f507cc127379(
    *,
    expression: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LakeformationPermissionsLfTagPolicyExpression, typing.Dict[builtins.str, typing.Any]]]],
    resource_type: builtins.str,
    catalog_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ef28e7930fb684cf06d2571f3c111618fdd48f6caad23bb1b0aee0bfd39b703(
    *,
    key: builtins.str,
    values: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a323aa70932068f27eaefd3da856219a7c4ce724d50a27d5aea75f72412b4ef7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__932e8ad10ee0bf07028ed10a27dabbb80107495249903a7d6c6a761b42b3e64b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f3efa41692f886af9dc75a17c9b79f8857e22866779b6c9c38c2dc4140bc023(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e2fb030d492788b73042a99b0a141a2a8c2696efffba570b809b231960b68da(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3f7b8161569cab0a78772ca44aa9ce66402880bf239ea455ddc63c662cb2121(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a17dfeda1404535309487ef47cd8c7b40afc1cd8ee74c742100b83dd5c2ad462(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LakeformationPermissionsLfTagPolicyExpression]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f2555db1b137011420d68461300c0e59e7837ca4eb246f775e19fe80bec8e50(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a20aaed97607897d09203f1d6f267d72575ad8b42c6f8ccc97316cd07aabd2d5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11c022e999a78af0db837d310320f116a037c1ea8d7527660889672b537560f6(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fea36ca42f8b70c94cfa0cc9c83d3453e6809693ed00253f06dab3f48cdb6d64(
    value: typing.Optional[typing.Union[LakeformationPermissionsLfTagPolicyExpression, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__203a7ae45e61cd466486e680a339bd7e63b10a6d05ced0899797f836c36d6268(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ffaf6c2cf7d06eda96d2cb81bdd7e6b92d9d06241650787fdcd8b4d28971cc6(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LakeformationPermissionsLfTagPolicyExpression, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5727688c87326caa5f4f5da4b292430e0522a80d5be0b1938d2d483b189ce162(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4423c10494446c60265cad2bf0bff80ad19676d2c7a4dd3e3d4e2990aa757482(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4415ed9a262bed4784f10505c79d60664caac1a455a43b29150c3488570dd9a(
    value: typing.Optional[LakeformationPermissionsLfTagPolicy],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e93577b92c23a79a50ad3762197a29154d1b82483c29fb13a690e882cd4429c8(
    *,
    database_name: builtins.str,
    catalog_id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    wildcard: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39c653c1dc57be36be65001a9e3acefd114ac3c64790be93044c227153a7c244(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec5d76a3aa25617254b90df2ce2a943f198753efd6476404abbe47925b248bf9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65a05b478070a794169a172c871c75302c96895798d1cc730448fd2b9182a14e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec8c820eafdb31da098b50305098797418f5203c470cc479d8370c38c7f016ce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fe8cb220326e9d9377679ebe966df4cbb85a49f0508ea2336bc6fce46336f36(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5af5ab7e38b615a71cd0f774eebcfb96e3d89dca7444546f2b1c8c18ee1a1708(
    value: typing.Optional[LakeformationPermissionsTable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebcb44c0780159b775afb8e0539522d0b1028c5abe42acfc62deadd25926f218(
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

def _typecheckingstub__359c8859eea03f6b681553436cbad919fc9462db02b8a703cb1978a7dc1eb8fd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94b6c35ff72c2a37239fd28c91c99ebbdb68e1e23f95c4e13bb033b2433c9b7e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6353ced93b9cba17e0f929a833d3e2133d98c1690c5b5d9a38b70f6cdd5295f0(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bca1a593ed8f92b4ed90b095eac2bf97b7a436becc957a078283d89426981254(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88b73856b76020e1c2800924fdec968088cd9002c435d5b3a03ba9f3c64068c3(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__edb9f3a0d9304fcf17582cb3d962e5ecb8accd7efe74cd739b9a6ed6a7f0d7d9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__072f4ae7fd6e287c16a0d1a77ce6ef7a6fee0614cace0ae1e8ea1baa0dbffe1f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85587db98fb8d03fdea04065b83bc329b65ee693fd25e4dd3c8ba59cf8922d83(
    value: typing.Optional[LakeformationPermissionsTableWithColumns],
) -> None:
    """Type checking stubs"""
    pass
