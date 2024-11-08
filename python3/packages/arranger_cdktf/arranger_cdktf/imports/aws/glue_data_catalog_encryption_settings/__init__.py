'''
# `aws_glue_data_catalog_encryption_settings`

Refer to the Terraform Registory for docs: [`aws_glue_data_catalog_encryption_settings`](https://www.terraform.io/docs/providers/aws/r/glue_data_catalog_encryption_settings).
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


class GlueDataCatalogEncryptionSettings(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.glueDataCatalogEncryptionSettings.GlueDataCatalogEncryptionSettings",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/glue_data_catalog_encryption_settings aws_glue_data_catalog_encryption_settings}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        data_catalog_encryption_settings: typing.Union["GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettings", typing.Dict[builtins.str, typing.Any]],
        catalog_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/glue_data_catalog_encryption_settings aws_glue_data_catalog_encryption_settings} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param data_catalog_encryption_settings: data_catalog_encryption_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_data_catalog_encryption_settings#data_catalog_encryption_settings GlueDataCatalogEncryptionSettings#data_catalog_encryption_settings}
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_data_catalog_encryption_settings#catalog_id GlueDataCatalogEncryptionSettings#catalog_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_data_catalog_encryption_settings#id GlueDataCatalogEncryptionSettings#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b177e85dea02e539b4667bdadc40ff13a607c3cde2b331cb1a3edda620a9ea94)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GlueDataCatalogEncryptionSettingsConfig(
            data_catalog_encryption_settings=data_catalog_encryption_settings,
            catalog_id=catalog_id,
            id=id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putDataCatalogEncryptionSettings")
    def put_data_catalog_encryption_settings(
        self,
        *,
        connection_password_encryption: typing.Union["GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsConnectionPasswordEncryption", typing.Dict[builtins.str, typing.Any]],
        encryption_at_rest: typing.Union["GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsEncryptionAtRest", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param connection_password_encryption: connection_password_encryption block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_data_catalog_encryption_settings#connection_password_encryption GlueDataCatalogEncryptionSettings#connection_password_encryption}
        :param encryption_at_rest: encryption_at_rest block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_data_catalog_encryption_settings#encryption_at_rest GlueDataCatalogEncryptionSettings#encryption_at_rest}
        '''
        value = GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettings(
            connection_password_encryption=connection_password_encryption,
            encryption_at_rest=encryption_at_rest,
        )

        return typing.cast(None, jsii.invoke(self, "putDataCatalogEncryptionSettings", [value]))

    @jsii.member(jsii_name="resetCatalogId")
    def reset_catalog_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCatalogId", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="dataCatalogEncryptionSettings")
    def data_catalog_encryption_settings(
        self,
    ) -> "GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsOutputReference":
        return typing.cast("GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsOutputReference", jsii.get(self, "dataCatalogEncryptionSettings"))

    @builtins.property
    @jsii.member(jsii_name="catalogIdInput")
    def catalog_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "catalogIdInput"))

    @builtins.property
    @jsii.member(jsii_name="dataCatalogEncryptionSettingsInput")
    def data_catalog_encryption_settings_input(
        self,
    ) -> typing.Optional["GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettings"]:
        return typing.cast(typing.Optional["GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettings"], jsii.get(self, "dataCatalogEncryptionSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="catalogId")
    def catalog_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "catalogId"))

    @catalog_id.setter
    def catalog_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8d60e2537b3223ac739dd60662d438851366b8804e8e81f30af3926280889ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "catalogId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13d4f165a7466dca413b5ef1100949321b1d231b6893bf002637ca81a4d1adde)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="aws.glueDataCatalogEncryptionSettings.GlueDataCatalogEncryptionSettingsConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "data_catalog_encryption_settings": "dataCatalogEncryptionSettings",
        "catalog_id": "catalogId",
        "id": "id",
    },
)
class GlueDataCatalogEncryptionSettingsConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        data_catalog_encryption_settings: typing.Union["GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettings", typing.Dict[builtins.str, typing.Any]],
        catalog_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param data_catalog_encryption_settings: data_catalog_encryption_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_data_catalog_encryption_settings#data_catalog_encryption_settings GlueDataCatalogEncryptionSettings#data_catalog_encryption_settings}
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_data_catalog_encryption_settings#catalog_id GlueDataCatalogEncryptionSettings#catalog_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_data_catalog_encryption_settings#id GlueDataCatalogEncryptionSettings#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(data_catalog_encryption_settings, dict):
            data_catalog_encryption_settings = GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettings(**data_catalog_encryption_settings)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d031bbced2ff872cba46612a1a7f1290d6a0ce2445b2f07a0ba92937ba0c6d59)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument data_catalog_encryption_settings", value=data_catalog_encryption_settings, expected_type=type_hints["data_catalog_encryption_settings"])
            check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "data_catalog_encryption_settings": data_catalog_encryption_settings,
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
        if id is not None:
            self._values["id"] = id

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
    def data_catalog_encryption_settings(
        self,
    ) -> "GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettings":
        '''data_catalog_encryption_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_data_catalog_encryption_settings#data_catalog_encryption_settings GlueDataCatalogEncryptionSettings#data_catalog_encryption_settings}
        '''
        result = self._values.get("data_catalog_encryption_settings")
        assert result is not None, "Required property 'data_catalog_encryption_settings' is missing"
        return typing.cast("GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettings", result)

    @builtins.property
    def catalog_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_data_catalog_encryption_settings#catalog_id GlueDataCatalogEncryptionSettings#catalog_id}.'''
        result = self._values.get("catalog_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_data_catalog_encryption_settings#id GlueDataCatalogEncryptionSettings#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueDataCatalogEncryptionSettingsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.glueDataCatalogEncryptionSettings.GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettings",
    jsii_struct_bases=[],
    name_mapping={
        "connection_password_encryption": "connectionPasswordEncryption",
        "encryption_at_rest": "encryptionAtRest",
    },
)
class GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettings:
    def __init__(
        self,
        *,
        connection_password_encryption: typing.Union["GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsConnectionPasswordEncryption", typing.Dict[builtins.str, typing.Any]],
        encryption_at_rest: typing.Union["GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsEncryptionAtRest", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param connection_password_encryption: connection_password_encryption block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_data_catalog_encryption_settings#connection_password_encryption GlueDataCatalogEncryptionSettings#connection_password_encryption}
        :param encryption_at_rest: encryption_at_rest block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_data_catalog_encryption_settings#encryption_at_rest GlueDataCatalogEncryptionSettings#encryption_at_rest}
        '''
        if isinstance(connection_password_encryption, dict):
            connection_password_encryption = GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsConnectionPasswordEncryption(**connection_password_encryption)
        if isinstance(encryption_at_rest, dict):
            encryption_at_rest = GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsEncryptionAtRest(**encryption_at_rest)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0f6a5185370772e39b671952f3f0324297c43aa66d247bdc7155fac8dc1b94c)
            check_type(argname="argument connection_password_encryption", value=connection_password_encryption, expected_type=type_hints["connection_password_encryption"])
            check_type(argname="argument encryption_at_rest", value=encryption_at_rest, expected_type=type_hints["encryption_at_rest"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "connection_password_encryption": connection_password_encryption,
            "encryption_at_rest": encryption_at_rest,
        }

    @builtins.property
    def connection_password_encryption(
        self,
    ) -> "GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsConnectionPasswordEncryption":
        '''connection_password_encryption block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_data_catalog_encryption_settings#connection_password_encryption GlueDataCatalogEncryptionSettings#connection_password_encryption}
        '''
        result = self._values.get("connection_password_encryption")
        assert result is not None, "Required property 'connection_password_encryption' is missing"
        return typing.cast("GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsConnectionPasswordEncryption", result)

    @builtins.property
    def encryption_at_rest(
        self,
    ) -> "GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsEncryptionAtRest":
        '''encryption_at_rest block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_data_catalog_encryption_settings#encryption_at_rest GlueDataCatalogEncryptionSettings#encryption_at_rest}
        '''
        result = self._values.get("encryption_at_rest")
        assert result is not None, "Required property 'encryption_at_rest' is missing"
        return typing.cast("GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsEncryptionAtRest", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.glueDataCatalogEncryptionSettings.GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsConnectionPasswordEncryption",
    jsii_struct_bases=[],
    name_mapping={
        "return_connection_password_encrypted": "returnConnectionPasswordEncrypted",
        "aws_kms_key_id": "awsKmsKeyId",
    },
)
class GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsConnectionPasswordEncryption:
    def __init__(
        self,
        *,
        return_connection_password_encrypted: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        aws_kms_key_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param return_connection_password_encrypted: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_data_catalog_encryption_settings#return_connection_password_encrypted GlueDataCatalogEncryptionSettings#return_connection_password_encrypted}.
        :param aws_kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_data_catalog_encryption_settings#aws_kms_key_id GlueDataCatalogEncryptionSettings#aws_kms_key_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a28f873e619f4612c248e2195c185291aa88447867484f65e71ef8c6783854c)
            check_type(argname="argument return_connection_password_encrypted", value=return_connection_password_encrypted, expected_type=type_hints["return_connection_password_encrypted"])
            check_type(argname="argument aws_kms_key_id", value=aws_kms_key_id, expected_type=type_hints["aws_kms_key_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "return_connection_password_encrypted": return_connection_password_encrypted,
        }
        if aws_kms_key_id is not None:
            self._values["aws_kms_key_id"] = aws_kms_key_id

    @builtins.property
    def return_connection_password_encrypted(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_data_catalog_encryption_settings#return_connection_password_encrypted GlueDataCatalogEncryptionSettings#return_connection_password_encrypted}.'''
        result = self._values.get("return_connection_password_encrypted")
        assert result is not None, "Required property 'return_connection_password_encrypted' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def aws_kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_data_catalog_encryption_settings#aws_kms_key_id GlueDataCatalogEncryptionSettings#aws_kms_key_id}.'''
        result = self._values.get("aws_kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsConnectionPasswordEncryption(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsConnectionPasswordEncryptionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.glueDataCatalogEncryptionSettings.GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsConnectionPasswordEncryptionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4b33c90016cca48ef32f06e16eeaa224de8fd6ed84ff825183a58ad893ff8207)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAwsKmsKeyId")
    def reset_aws_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsKmsKeyId", []))

    @builtins.property
    @jsii.member(jsii_name="awsKmsKeyIdInput")
    def aws_kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "awsKmsKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="returnConnectionPasswordEncryptedInput")
    def return_connection_password_encrypted_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "returnConnectionPasswordEncryptedInput"))

    @builtins.property
    @jsii.member(jsii_name="awsKmsKeyId")
    def aws_kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "awsKmsKeyId"))

    @aws_kms_key_id.setter
    def aws_kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74ca4cccdfe7150cd1d2f93b409105e0472ae366aba060457d6c22f53a451396)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsKmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="returnConnectionPasswordEncrypted")
    def return_connection_password_encrypted(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "returnConnectionPasswordEncrypted"))

    @return_connection_password_encrypted.setter
    def return_connection_password_encrypted(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__521209b14077aa2c62522c69ae46d1187a1299426597d015f18a77884af35848)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "returnConnectionPasswordEncrypted", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsConnectionPasswordEncryption]:
        return typing.cast(typing.Optional[GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsConnectionPasswordEncryption], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsConnectionPasswordEncryption],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e437dd9b4797c5ba702190923fc656ba94959016bae7956a287b68d46256798a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.glueDataCatalogEncryptionSettings.GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsEncryptionAtRest",
    jsii_struct_bases=[],
    name_mapping={
        "catalog_encryption_mode": "catalogEncryptionMode",
        "sse_aws_kms_key_id": "sseAwsKmsKeyId",
    },
)
class GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsEncryptionAtRest:
    def __init__(
        self,
        *,
        catalog_encryption_mode: builtins.str,
        sse_aws_kms_key_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param catalog_encryption_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_data_catalog_encryption_settings#catalog_encryption_mode GlueDataCatalogEncryptionSettings#catalog_encryption_mode}.
        :param sse_aws_kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_data_catalog_encryption_settings#sse_aws_kms_key_id GlueDataCatalogEncryptionSettings#sse_aws_kms_key_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66760b9d9c30544241229ab2a9409e83e12626b2a326df1cca3e498f784f4438)
            check_type(argname="argument catalog_encryption_mode", value=catalog_encryption_mode, expected_type=type_hints["catalog_encryption_mode"])
            check_type(argname="argument sse_aws_kms_key_id", value=sse_aws_kms_key_id, expected_type=type_hints["sse_aws_kms_key_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "catalog_encryption_mode": catalog_encryption_mode,
        }
        if sse_aws_kms_key_id is not None:
            self._values["sse_aws_kms_key_id"] = sse_aws_kms_key_id

    @builtins.property
    def catalog_encryption_mode(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_data_catalog_encryption_settings#catalog_encryption_mode GlueDataCatalogEncryptionSettings#catalog_encryption_mode}.'''
        result = self._values.get("catalog_encryption_mode")
        assert result is not None, "Required property 'catalog_encryption_mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sse_aws_kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_data_catalog_encryption_settings#sse_aws_kms_key_id GlueDataCatalogEncryptionSettings#sse_aws_kms_key_id}.'''
        result = self._values.get("sse_aws_kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsEncryptionAtRest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsEncryptionAtRestOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.glueDataCatalogEncryptionSettings.GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsEncryptionAtRestOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9620dbc4da3ebc09e7838922081f8eaca09abeccb76fba4e9ce1e7fd66e1cb45)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetSseAwsKmsKeyId")
    def reset_sse_aws_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSseAwsKmsKeyId", []))

    @builtins.property
    @jsii.member(jsii_name="catalogEncryptionModeInput")
    def catalog_encryption_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "catalogEncryptionModeInput"))

    @builtins.property
    @jsii.member(jsii_name="sseAwsKmsKeyIdInput")
    def sse_aws_kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sseAwsKmsKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="catalogEncryptionMode")
    def catalog_encryption_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "catalogEncryptionMode"))

    @catalog_encryption_mode.setter
    def catalog_encryption_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36538951ad316bf36e814aefc7b661630d60dff9cd387dd9011fb283b545fb9f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "catalogEncryptionMode", value)

    @builtins.property
    @jsii.member(jsii_name="sseAwsKmsKeyId")
    def sse_aws_kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sseAwsKmsKeyId"))

    @sse_aws_kms_key_id.setter
    def sse_aws_kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3437490bee8f75a1d4f0d77c03427c162de55fac4b0036194e1aa25675f0c693)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sseAwsKmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsEncryptionAtRest]:
        return typing.cast(typing.Optional[GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsEncryptionAtRest], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsEncryptionAtRest],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51a586ad3cda3d1da061cb5c804e6cc3e91264311d905c1b95947a43eeec65a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.glueDataCatalogEncryptionSettings.GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8d043025ff3c266011b2ed7e556bfc81eee68a3e45f8d3036eb0a73f3345b534)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putConnectionPasswordEncryption")
    def put_connection_password_encryption(
        self,
        *,
        return_connection_password_encrypted: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        aws_kms_key_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param return_connection_password_encrypted: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_data_catalog_encryption_settings#return_connection_password_encrypted GlueDataCatalogEncryptionSettings#return_connection_password_encrypted}.
        :param aws_kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_data_catalog_encryption_settings#aws_kms_key_id GlueDataCatalogEncryptionSettings#aws_kms_key_id}.
        '''
        value = GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsConnectionPasswordEncryption(
            return_connection_password_encrypted=return_connection_password_encrypted,
            aws_kms_key_id=aws_kms_key_id,
        )

        return typing.cast(None, jsii.invoke(self, "putConnectionPasswordEncryption", [value]))

    @jsii.member(jsii_name="putEncryptionAtRest")
    def put_encryption_at_rest(
        self,
        *,
        catalog_encryption_mode: builtins.str,
        sse_aws_kms_key_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param catalog_encryption_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_data_catalog_encryption_settings#catalog_encryption_mode GlueDataCatalogEncryptionSettings#catalog_encryption_mode}.
        :param sse_aws_kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_data_catalog_encryption_settings#sse_aws_kms_key_id GlueDataCatalogEncryptionSettings#sse_aws_kms_key_id}.
        '''
        value = GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsEncryptionAtRest(
            catalog_encryption_mode=catalog_encryption_mode,
            sse_aws_kms_key_id=sse_aws_kms_key_id,
        )

        return typing.cast(None, jsii.invoke(self, "putEncryptionAtRest", [value]))

    @builtins.property
    @jsii.member(jsii_name="connectionPasswordEncryption")
    def connection_password_encryption(
        self,
    ) -> GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsConnectionPasswordEncryptionOutputReference:
        return typing.cast(GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsConnectionPasswordEncryptionOutputReference, jsii.get(self, "connectionPasswordEncryption"))

    @builtins.property
    @jsii.member(jsii_name="encryptionAtRest")
    def encryption_at_rest(
        self,
    ) -> GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsEncryptionAtRestOutputReference:
        return typing.cast(GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsEncryptionAtRestOutputReference, jsii.get(self, "encryptionAtRest"))

    @builtins.property
    @jsii.member(jsii_name="connectionPasswordEncryptionInput")
    def connection_password_encryption_input(
        self,
    ) -> typing.Optional[GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsConnectionPasswordEncryption]:
        return typing.cast(typing.Optional[GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsConnectionPasswordEncryption], jsii.get(self, "connectionPasswordEncryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionAtRestInput")
    def encryption_at_rest_input(
        self,
    ) -> typing.Optional[GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsEncryptionAtRest]:
        return typing.cast(typing.Optional[GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsEncryptionAtRest], jsii.get(self, "encryptionAtRestInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettings]:
        return typing.cast(typing.Optional[GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2a6ce131766b2ca4e395fd38c3c305402e620d529f9d7f80b6f4f235e16f698)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GlueDataCatalogEncryptionSettings",
    "GlueDataCatalogEncryptionSettingsConfig",
    "GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettings",
    "GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsConnectionPasswordEncryption",
    "GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsConnectionPasswordEncryptionOutputReference",
    "GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsEncryptionAtRest",
    "GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsEncryptionAtRestOutputReference",
    "GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsOutputReference",
]

publication.publish()

def _typecheckingstub__b177e85dea02e539b4667bdadc40ff13a607c3cde2b331cb1a3edda620a9ea94(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    data_catalog_encryption_settings: typing.Union[GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettings, typing.Dict[builtins.str, typing.Any]],
    catalog_id: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__e8d60e2537b3223ac739dd60662d438851366b8804e8e81f30af3926280889ce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13d4f165a7466dca413b5ef1100949321b1d231b6893bf002637ca81a4d1adde(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d031bbced2ff872cba46612a1a7f1290d6a0ce2445b2f07a0ba92937ba0c6d59(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    data_catalog_encryption_settings: typing.Union[GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettings, typing.Dict[builtins.str, typing.Any]],
    catalog_id: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0f6a5185370772e39b671952f3f0324297c43aa66d247bdc7155fac8dc1b94c(
    *,
    connection_password_encryption: typing.Union[GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsConnectionPasswordEncryption, typing.Dict[builtins.str, typing.Any]],
    encryption_at_rest: typing.Union[GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsEncryptionAtRest, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a28f873e619f4612c248e2195c185291aa88447867484f65e71ef8c6783854c(
    *,
    return_connection_password_encrypted: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    aws_kms_key_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b33c90016cca48ef32f06e16eeaa224de8fd6ed84ff825183a58ad893ff8207(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74ca4cccdfe7150cd1d2f93b409105e0472ae366aba060457d6c22f53a451396(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__521209b14077aa2c62522c69ae46d1187a1299426597d015f18a77884af35848(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e437dd9b4797c5ba702190923fc656ba94959016bae7956a287b68d46256798a(
    value: typing.Optional[GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsConnectionPasswordEncryption],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66760b9d9c30544241229ab2a9409e83e12626b2a326df1cca3e498f784f4438(
    *,
    catalog_encryption_mode: builtins.str,
    sse_aws_kms_key_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9620dbc4da3ebc09e7838922081f8eaca09abeccb76fba4e9ce1e7fd66e1cb45(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36538951ad316bf36e814aefc7b661630d60dff9cd387dd9011fb283b545fb9f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3437490bee8f75a1d4f0d77c03427c162de55fac4b0036194e1aa25675f0c693(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51a586ad3cda3d1da061cb5c804e6cc3e91264311d905c1b95947a43eeec65a4(
    value: typing.Optional[GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsEncryptionAtRest],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d043025ff3c266011b2ed7e556bfc81eee68a3e45f8d3036eb0a73f3345b534(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2a6ce131766b2ca4e395fd38c3c305402e620d529f9d7f80b6f4f235e16f698(
    value: typing.Optional[GlueDataCatalogEncryptionSettingsDataCatalogEncryptionSettings],
) -> None:
    """Type checking stubs"""
    pass
