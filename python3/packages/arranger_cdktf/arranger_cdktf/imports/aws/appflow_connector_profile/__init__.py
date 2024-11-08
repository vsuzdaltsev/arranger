'''
# `aws_appflow_connector_profile`

Refer to the Terraform Registory for docs: [`aws_appflow_connector_profile`](https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile).
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


class AppflowConnectorProfile(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfile",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile aws_appflow_connector_profile}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        connection_mode: builtins.str,
        connector_profile_config: typing.Union["AppflowConnectorProfileConnectorProfileConfig", typing.Dict[builtins.str, typing.Any]],
        connector_type: builtins.str,
        name: builtins.str,
        connector_label: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        kms_arn: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile aws_appflow_connector_profile} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param connection_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#connection_mode AppflowConnectorProfile#connection_mode}.
        :param connector_profile_config: connector_profile_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#connector_profile_config AppflowConnectorProfile#connector_profile_config}
        :param connector_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#connector_type AppflowConnectorProfile#connector_type}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#name AppflowConnectorProfile#name}.
        :param connector_label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#connector_label AppflowConnectorProfile#connector_label}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#id AppflowConnectorProfile#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kms_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#kms_arn AppflowConnectorProfile#kms_arn}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__467d06a6c034038a3200e65f379a2c2642aff6f0cb2d8b9acdee2f4c137bc6e9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AppflowConnectorProfileConfig(
            connection_mode=connection_mode,
            connector_profile_config=connector_profile_config,
            connector_type=connector_type,
            name=name,
            connector_label=connector_label,
            id=id,
            kms_arn=kms_arn,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putConnectorProfileConfig")
    def put_connector_profile_config(
        self,
        *,
        connector_profile_credentials: typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentials", typing.Dict[builtins.str, typing.Any]],
        connector_profile_properties: typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileProperties", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param connector_profile_credentials: connector_profile_credentials block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#connector_profile_credentials AppflowConnectorProfile#connector_profile_credentials}
        :param connector_profile_properties: connector_profile_properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#connector_profile_properties AppflowConnectorProfile#connector_profile_properties}
        '''
        value = AppflowConnectorProfileConnectorProfileConfig(
            connector_profile_credentials=connector_profile_credentials,
            connector_profile_properties=connector_profile_properties,
        )

        return typing.cast(None, jsii.invoke(self, "putConnectorProfileConfig", [value]))

    @jsii.member(jsii_name="resetConnectorLabel")
    def reset_connector_label(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectorLabel", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetKmsArn")
    def reset_kms_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsArn", []))

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
    @jsii.member(jsii_name="connectorProfileConfig")
    def connector_profile_config(
        self,
    ) -> "AppflowConnectorProfileConnectorProfileConfigOutputReference":
        return typing.cast("AppflowConnectorProfileConnectorProfileConfigOutputReference", jsii.get(self, "connectorProfileConfig"))

    @builtins.property
    @jsii.member(jsii_name="credentialsArn")
    def credentials_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "credentialsArn"))

    @builtins.property
    @jsii.member(jsii_name="connectionModeInput")
    def connection_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionModeInput"))

    @builtins.property
    @jsii.member(jsii_name="connectorLabelInput")
    def connector_label_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectorLabelInput"))

    @builtins.property
    @jsii.member(jsii_name="connectorProfileConfigInput")
    def connector_profile_config_input(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfig"]:
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfig"], jsii.get(self, "connectorProfileConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="connectorTypeInput")
    def connector_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectorTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsArnInput")
    def kms_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsArnInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionMode")
    def connection_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionMode"))

    @connection_mode.setter
    def connection_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7cc9dad6f882df50531a264399a3516926eebaadf513e236079a07b51c363322)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionMode", value)

    @builtins.property
    @jsii.member(jsii_name="connectorLabel")
    def connector_label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectorLabel"))

    @connector_label.setter
    def connector_label(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c85b96dd9f746ee3ec96f47733b7533ece6b7ac1f0ce5852e4295975ad54752)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectorLabel", value)

    @builtins.property
    @jsii.member(jsii_name="connectorType")
    def connector_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectorType"))

    @connector_type.setter
    def connector_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b98b72d8a3796a31081ddb1fedd031297745ca53ce775166902fed1e27c2791)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectorType", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d8b80377bbc42cf1f08b9bb65421d4cf86b1a99ba2e2308a04318dd90ef3475)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="kmsArn")
    def kms_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsArn"))

    @kms_arn.setter
    def kms_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__becdf48c4096ee1be7f9bc532ce34c77a2aaebcf0f527c9f96774d6124a1639c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsArn", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__138e14335d269f31264505cb3ea26174c6f40b50817fbe2572da24792eadd118)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "connection_mode": "connectionMode",
        "connector_profile_config": "connectorProfileConfig",
        "connector_type": "connectorType",
        "name": "name",
        "connector_label": "connectorLabel",
        "id": "id",
        "kms_arn": "kmsArn",
    },
)
class AppflowConnectorProfileConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        connection_mode: builtins.str,
        connector_profile_config: typing.Union["AppflowConnectorProfileConnectorProfileConfig", typing.Dict[builtins.str, typing.Any]],
        connector_type: builtins.str,
        name: builtins.str,
        connector_label: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        kms_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param connection_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#connection_mode AppflowConnectorProfile#connection_mode}.
        :param connector_profile_config: connector_profile_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#connector_profile_config AppflowConnectorProfile#connector_profile_config}
        :param connector_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#connector_type AppflowConnectorProfile#connector_type}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#name AppflowConnectorProfile#name}.
        :param connector_label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#connector_label AppflowConnectorProfile#connector_label}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#id AppflowConnectorProfile#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kms_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#kms_arn AppflowConnectorProfile#kms_arn}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(connector_profile_config, dict):
            connector_profile_config = AppflowConnectorProfileConnectorProfileConfig(**connector_profile_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54e8cda6287b9fffb8989744b68315dcd075e93b7cfd087fd73de262fb7fc5e3)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument connection_mode", value=connection_mode, expected_type=type_hints["connection_mode"])
            check_type(argname="argument connector_profile_config", value=connector_profile_config, expected_type=type_hints["connector_profile_config"])
            check_type(argname="argument connector_type", value=connector_type, expected_type=type_hints["connector_type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument connector_label", value=connector_label, expected_type=type_hints["connector_label"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument kms_arn", value=kms_arn, expected_type=type_hints["kms_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "connection_mode": connection_mode,
            "connector_profile_config": connector_profile_config,
            "connector_type": connector_type,
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
        if connector_label is not None:
            self._values["connector_label"] = connector_label
        if id is not None:
            self._values["id"] = id
        if kms_arn is not None:
            self._values["kms_arn"] = kms_arn

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
    def connection_mode(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#connection_mode AppflowConnectorProfile#connection_mode}.'''
        result = self._values.get("connection_mode")
        assert result is not None, "Required property 'connection_mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def connector_profile_config(
        self,
    ) -> "AppflowConnectorProfileConnectorProfileConfig":
        '''connector_profile_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#connector_profile_config AppflowConnectorProfile#connector_profile_config}
        '''
        result = self._values.get("connector_profile_config")
        assert result is not None, "Required property 'connector_profile_config' is missing"
        return typing.cast("AppflowConnectorProfileConnectorProfileConfig", result)

    @builtins.property
    def connector_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#connector_type AppflowConnectorProfile#connector_type}.'''
        result = self._values.get("connector_type")
        assert result is not None, "Required property 'connector_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#name AppflowConnectorProfile#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def connector_label(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#connector_label AppflowConnectorProfile#connector_label}.'''
        result = self._values.get("connector_label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#id AppflowConnectorProfile#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#kms_arn AppflowConnectorProfile#kms_arn}.'''
        result = self._values.get("kms_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfig",
    jsii_struct_bases=[],
    name_mapping={
        "connector_profile_credentials": "connectorProfileCredentials",
        "connector_profile_properties": "connectorProfileProperties",
    },
)
class AppflowConnectorProfileConnectorProfileConfig:
    def __init__(
        self,
        *,
        connector_profile_credentials: typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentials", typing.Dict[builtins.str, typing.Any]],
        connector_profile_properties: typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileProperties", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param connector_profile_credentials: connector_profile_credentials block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#connector_profile_credentials AppflowConnectorProfile#connector_profile_credentials}
        :param connector_profile_properties: connector_profile_properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#connector_profile_properties AppflowConnectorProfile#connector_profile_properties}
        '''
        if isinstance(connector_profile_credentials, dict):
            connector_profile_credentials = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentials(**connector_profile_credentials)
        if isinstance(connector_profile_properties, dict):
            connector_profile_properties = AppflowConnectorProfileConnectorProfileConfigConnectorProfileProperties(**connector_profile_properties)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__258944cd6bb6d386c7d2a1f0fa509fda676023bbeea260fe98cf931c61011b78)
            check_type(argname="argument connector_profile_credentials", value=connector_profile_credentials, expected_type=type_hints["connector_profile_credentials"])
            check_type(argname="argument connector_profile_properties", value=connector_profile_properties, expected_type=type_hints["connector_profile_properties"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "connector_profile_credentials": connector_profile_credentials,
            "connector_profile_properties": connector_profile_properties,
        }

    @builtins.property
    def connector_profile_credentials(
        self,
    ) -> "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentials":
        '''connector_profile_credentials block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#connector_profile_credentials AppflowConnectorProfile#connector_profile_credentials}
        '''
        result = self._values.get("connector_profile_credentials")
        assert result is not None, "Required property 'connector_profile_credentials' is missing"
        return typing.cast("AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentials", result)

    @builtins.property
    def connector_profile_properties(
        self,
    ) -> "AppflowConnectorProfileConnectorProfileConfigConnectorProfileProperties":
        '''connector_profile_properties block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#connector_profile_properties AppflowConnectorProfile#connector_profile_properties}
        '''
        result = self._values.get("connector_profile_properties")
        assert result is not None, "Required property 'connector_profile_properties' is missing"
        return typing.cast("AppflowConnectorProfileConnectorProfileConfigConnectorProfileProperties", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentials",
    jsii_struct_bases=[],
    name_mapping={
        "amplitude": "amplitude",
        "custom_connector": "customConnector",
        "datadog": "datadog",
        "dynatrace": "dynatrace",
        "google_analytics": "googleAnalytics",
        "honeycode": "honeycode",
        "infor_nexus": "inforNexus",
        "marketo": "marketo",
        "redshift": "redshift",
        "salesforce": "salesforce",
        "sapo_data": "sapoData",
        "service_now": "serviceNow",
        "singular": "singular",
        "slack": "slack",
        "snowflake": "snowflake",
        "trendmicro": "trendmicro",
        "veeva": "veeva",
        "zendesk": "zendesk",
    },
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentials:
    def __init__(
        self,
        *,
        amplitude: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitude", typing.Dict[builtins.str, typing.Any]]] = None,
        custom_connector: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnector", typing.Dict[builtins.str, typing.Any]]] = None,
        datadog: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadog", typing.Dict[builtins.str, typing.Any]]] = None,
        dynatrace: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatrace", typing.Dict[builtins.str, typing.Any]]] = None,
        google_analytics: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalytics", typing.Dict[builtins.str, typing.Any]]] = None,
        honeycode: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycode", typing.Dict[builtins.str, typing.Any]]] = None,
        infor_nexus: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexus", typing.Dict[builtins.str, typing.Any]]] = None,
        marketo: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketo", typing.Dict[builtins.str, typing.Any]]] = None,
        redshift: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshift", typing.Dict[builtins.str, typing.Any]]] = None,
        salesforce: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforce", typing.Dict[builtins.str, typing.Any]]] = None,
        sapo_data: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoData", typing.Dict[builtins.str, typing.Any]]] = None,
        service_now: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNow", typing.Dict[builtins.str, typing.Any]]] = None,
        singular: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingular", typing.Dict[builtins.str, typing.Any]]] = None,
        slack: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlack", typing.Dict[builtins.str, typing.Any]]] = None,
        snowflake: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflake", typing.Dict[builtins.str, typing.Any]]] = None,
        trendmicro: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicro", typing.Dict[builtins.str, typing.Any]]] = None,
        veeva: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeeva", typing.Dict[builtins.str, typing.Any]]] = None,
        zendesk: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendesk", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param amplitude: amplitude block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#amplitude AppflowConnectorProfile#amplitude}
        :param custom_connector: custom_connector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#custom_connector AppflowConnectorProfile#custom_connector}
        :param datadog: datadog block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#datadog AppflowConnectorProfile#datadog}
        :param dynatrace: dynatrace block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#dynatrace AppflowConnectorProfile#dynatrace}
        :param google_analytics: google_analytics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#google_analytics AppflowConnectorProfile#google_analytics}
        :param honeycode: honeycode block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#honeycode AppflowConnectorProfile#honeycode}
        :param infor_nexus: infor_nexus block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#infor_nexus AppflowConnectorProfile#infor_nexus}
        :param marketo: marketo block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#marketo AppflowConnectorProfile#marketo}
        :param redshift: redshift block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redshift AppflowConnectorProfile#redshift}
        :param salesforce: salesforce block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#salesforce AppflowConnectorProfile#salesforce}
        :param sapo_data: sapo_data block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#sapo_data AppflowConnectorProfile#sapo_data}
        :param service_now: service_now block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#service_now AppflowConnectorProfile#service_now}
        :param singular: singular block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#singular AppflowConnectorProfile#singular}
        :param slack: slack block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#slack AppflowConnectorProfile#slack}
        :param snowflake: snowflake block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#snowflake AppflowConnectorProfile#snowflake}
        :param trendmicro: trendmicro block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#trendmicro AppflowConnectorProfile#trendmicro}
        :param veeva: veeva block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#veeva AppflowConnectorProfile#veeva}
        :param zendesk: zendesk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#zendesk AppflowConnectorProfile#zendesk}
        '''
        if isinstance(amplitude, dict):
            amplitude = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitude(**amplitude)
        if isinstance(custom_connector, dict):
            custom_connector = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnector(**custom_connector)
        if isinstance(datadog, dict):
            datadog = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadog(**datadog)
        if isinstance(dynatrace, dict):
            dynatrace = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatrace(**dynatrace)
        if isinstance(google_analytics, dict):
            google_analytics = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalytics(**google_analytics)
        if isinstance(honeycode, dict):
            honeycode = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycode(**honeycode)
        if isinstance(infor_nexus, dict):
            infor_nexus = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexus(**infor_nexus)
        if isinstance(marketo, dict):
            marketo = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketo(**marketo)
        if isinstance(redshift, dict):
            redshift = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshift(**redshift)
        if isinstance(salesforce, dict):
            salesforce = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforce(**salesforce)
        if isinstance(sapo_data, dict):
            sapo_data = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoData(**sapo_data)
        if isinstance(service_now, dict):
            service_now = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNow(**service_now)
        if isinstance(singular, dict):
            singular = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingular(**singular)
        if isinstance(slack, dict):
            slack = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlack(**slack)
        if isinstance(snowflake, dict):
            snowflake = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflake(**snowflake)
        if isinstance(trendmicro, dict):
            trendmicro = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicro(**trendmicro)
        if isinstance(veeva, dict):
            veeva = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeeva(**veeva)
        if isinstance(zendesk, dict):
            zendesk = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendesk(**zendesk)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b8482bdacb35fce0c59fc8a0887304b209695f7230bec55e3b5d7fb9ee5e0de)
            check_type(argname="argument amplitude", value=amplitude, expected_type=type_hints["amplitude"])
            check_type(argname="argument custom_connector", value=custom_connector, expected_type=type_hints["custom_connector"])
            check_type(argname="argument datadog", value=datadog, expected_type=type_hints["datadog"])
            check_type(argname="argument dynatrace", value=dynatrace, expected_type=type_hints["dynatrace"])
            check_type(argname="argument google_analytics", value=google_analytics, expected_type=type_hints["google_analytics"])
            check_type(argname="argument honeycode", value=honeycode, expected_type=type_hints["honeycode"])
            check_type(argname="argument infor_nexus", value=infor_nexus, expected_type=type_hints["infor_nexus"])
            check_type(argname="argument marketo", value=marketo, expected_type=type_hints["marketo"])
            check_type(argname="argument redshift", value=redshift, expected_type=type_hints["redshift"])
            check_type(argname="argument salesforce", value=salesforce, expected_type=type_hints["salesforce"])
            check_type(argname="argument sapo_data", value=sapo_data, expected_type=type_hints["sapo_data"])
            check_type(argname="argument service_now", value=service_now, expected_type=type_hints["service_now"])
            check_type(argname="argument singular", value=singular, expected_type=type_hints["singular"])
            check_type(argname="argument slack", value=slack, expected_type=type_hints["slack"])
            check_type(argname="argument snowflake", value=snowflake, expected_type=type_hints["snowflake"])
            check_type(argname="argument trendmicro", value=trendmicro, expected_type=type_hints["trendmicro"])
            check_type(argname="argument veeva", value=veeva, expected_type=type_hints["veeva"])
            check_type(argname="argument zendesk", value=zendesk, expected_type=type_hints["zendesk"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if amplitude is not None:
            self._values["amplitude"] = amplitude
        if custom_connector is not None:
            self._values["custom_connector"] = custom_connector
        if datadog is not None:
            self._values["datadog"] = datadog
        if dynatrace is not None:
            self._values["dynatrace"] = dynatrace
        if google_analytics is not None:
            self._values["google_analytics"] = google_analytics
        if honeycode is not None:
            self._values["honeycode"] = honeycode
        if infor_nexus is not None:
            self._values["infor_nexus"] = infor_nexus
        if marketo is not None:
            self._values["marketo"] = marketo
        if redshift is not None:
            self._values["redshift"] = redshift
        if salesforce is not None:
            self._values["salesforce"] = salesforce
        if sapo_data is not None:
            self._values["sapo_data"] = sapo_data
        if service_now is not None:
            self._values["service_now"] = service_now
        if singular is not None:
            self._values["singular"] = singular
        if slack is not None:
            self._values["slack"] = slack
        if snowflake is not None:
            self._values["snowflake"] = snowflake
        if trendmicro is not None:
            self._values["trendmicro"] = trendmicro
        if veeva is not None:
            self._values["veeva"] = veeva
        if zendesk is not None:
            self._values["zendesk"] = zendesk

    @builtins.property
    def amplitude(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitude"]:
        '''amplitude block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#amplitude AppflowConnectorProfile#amplitude}
        '''
        result = self._values.get("amplitude")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitude"], result)

    @builtins.property
    def custom_connector(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnector"]:
        '''custom_connector block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#custom_connector AppflowConnectorProfile#custom_connector}
        '''
        result = self._values.get("custom_connector")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnector"], result)

    @builtins.property
    def datadog(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadog"]:
        '''datadog block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#datadog AppflowConnectorProfile#datadog}
        '''
        result = self._values.get("datadog")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadog"], result)

    @builtins.property
    def dynatrace(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatrace"]:
        '''dynatrace block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#dynatrace AppflowConnectorProfile#dynatrace}
        '''
        result = self._values.get("dynatrace")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatrace"], result)

    @builtins.property
    def google_analytics(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalytics"]:
        '''google_analytics block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#google_analytics AppflowConnectorProfile#google_analytics}
        '''
        result = self._values.get("google_analytics")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalytics"], result)

    @builtins.property
    def honeycode(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycode"]:
        '''honeycode block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#honeycode AppflowConnectorProfile#honeycode}
        '''
        result = self._values.get("honeycode")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycode"], result)

    @builtins.property
    def infor_nexus(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexus"]:
        '''infor_nexus block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#infor_nexus AppflowConnectorProfile#infor_nexus}
        '''
        result = self._values.get("infor_nexus")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexus"], result)

    @builtins.property
    def marketo(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketo"]:
        '''marketo block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#marketo AppflowConnectorProfile#marketo}
        '''
        result = self._values.get("marketo")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketo"], result)

    @builtins.property
    def redshift(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshift"]:
        '''redshift block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redshift AppflowConnectorProfile#redshift}
        '''
        result = self._values.get("redshift")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshift"], result)

    @builtins.property
    def salesforce(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforce"]:
        '''salesforce block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#salesforce AppflowConnectorProfile#salesforce}
        '''
        result = self._values.get("salesforce")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforce"], result)

    @builtins.property
    def sapo_data(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoData"]:
        '''sapo_data block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#sapo_data AppflowConnectorProfile#sapo_data}
        '''
        result = self._values.get("sapo_data")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoData"], result)

    @builtins.property
    def service_now(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNow"]:
        '''service_now block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#service_now AppflowConnectorProfile#service_now}
        '''
        result = self._values.get("service_now")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNow"], result)

    @builtins.property
    def singular(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingular"]:
        '''singular block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#singular AppflowConnectorProfile#singular}
        '''
        result = self._values.get("singular")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingular"], result)

    @builtins.property
    def slack(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlack"]:
        '''slack block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#slack AppflowConnectorProfile#slack}
        '''
        result = self._values.get("slack")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlack"], result)

    @builtins.property
    def snowflake(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflake"]:
        '''snowflake block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#snowflake AppflowConnectorProfile#snowflake}
        '''
        result = self._values.get("snowflake")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflake"], result)

    @builtins.property
    def trendmicro(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicro"]:
        '''trendmicro block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#trendmicro AppflowConnectorProfile#trendmicro}
        '''
        result = self._values.get("trendmicro")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicro"], result)

    @builtins.property
    def veeva(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeeva"]:
        '''veeva block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#veeva AppflowConnectorProfile#veeva}
        '''
        result = self._values.get("veeva")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeeva"], result)

    @builtins.property
    def zendesk(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendesk"]:
        '''zendesk block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#zendesk AppflowConnectorProfile#zendesk}
        '''
        result = self._values.get("zendesk")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendesk"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentials(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitude",
    jsii_struct_bases=[],
    name_mapping={"api_key": "apiKey", "secret_key": "secretKey"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitude:
    def __init__(self, *, api_key: builtins.str, secret_key: builtins.str) -> None:
        '''
        :param api_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#api_key AppflowConnectorProfile#api_key}.
        :param secret_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#secret_key AppflowConnectorProfile#secret_key}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80dc6355640dc7b28d3589f2161d3b2e8f9d57786fbacf9ab6778cc9ac099b00)
            check_type(argname="argument api_key", value=api_key, expected_type=type_hints["api_key"])
            check_type(argname="argument secret_key", value=secret_key, expected_type=type_hints["secret_key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_key": api_key,
            "secret_key": secret_key,
        }

    @builtins.property
    def api_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#api_key AppflowConnectorProfile#api_key}.'''
        result = self._values.get("api_key")
        assert result is not None, "Required property 'api_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def secret_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#secret_key AppflowConnectorProfile#secret_key}.'''
        result = self._values.get("secret_key")
        assert result is not None, "Required property 'secret_key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitude(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitudeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitudeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__30b2a831eff9499a5dde409e1b7b77ed0511cdb95061d60f4cd4b1bee95291b6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="apiKeyInput")
    def api_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="secretKeyInput")
    def secret_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="apiKey")
    def api_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiKey"))

    @api_key.setter
    def api_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b954fca3a1ba6234a0230cc40af7b2a343c326a94b7372742a8c3f8533576920)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiKey", value)

    @builtins.property
    @jsii.member(jsii_name="secretKey")
    def secret_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretKey"))

    @secret_key.setter
    def secret_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2d1ef5dc9d1324e5bca694a2db9a56d2e412efd2ae782954467d666e66cd06f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitude]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitude], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitude],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36de010b0d6b2b3267c1e77ea835dec7a7e16f7612c8adb760c3aaea28c2f0a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnector",
    jsii_struct_bases=[],
    name_mapping={
        "authentication_type": "authenticationType",
        "api_key": "apiKey",
        "basic": "basic",
        "custom": "custom",
        "oauth2": "oauth2",
    },
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnector:
    def __init__(
        self,
        *,
        authentication_type: builtins.str,
        api_key: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKey", typing.Dict[builtins.str, typing.Any]]] = None,
        basic: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasic", typing.Dict[builtins.str, typing.Any]]] = None,
        custom: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustom", typing.Dict[builtins.str, typing.Any]]] = None,
        oauth2: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param authentication_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#authentication_type AppflowConnectorProfile#authentication_type}.
        :param api_key: api_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#api_key AppflowConnectorProfile#api_key}
        :param basic: basic block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#basic AppflowConnectorProfile#basic}
        :param custom: custom block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#custom AppflowConnectorProfile#custom}
        :param oauth2: oauth2 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth2 AppflowConnectorProfile#oauth2}
        '''
        if isinstance(api_key, dict):
            api_key = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKey(**api_key)
        if isinstance(basic, dict):
            basic = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasic(**basic)
        if isinstance(custom, dict):
            custom = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustom(**custom)
        if isinstance(oauth2, dict):
            oauth2 = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2(**oauth2)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2e1f157108fbcbf97a52e272c3faa4c969a6ce4b673b6e3055a467386438a59)
            check_type(argname="argument authentication_type", value=authentication_type, expected_type=type_hints["authentication_type"])
            check_type(argname="argument api_key", value=api_key, expected_type=type_hints["api_key"])
            check_type(argname="argument basic", value=basic, expected_type=type_hints["basic"])
            check_type(argname="argument custom", value=custom, expected_type=type_hints["custom"])
            check_type(argname="argument oauth2", value=oauth2, expected_type=type_hints["oauth2"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "authentication_type": authentication_type,
        }
        if api_key is not None:
            self._values["api_key"] = api_key
        if basic is not None:
            self._values["basic"] = basic
        if custom is not None:
            self._values["custom"] = custom
        if oauth2 is not None:
            self._values["oauth2"] = oauth2

    @builtins.property
    def authentication_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#authentication_type AppflowConnectorProfile#authentication_type}.'''
        result = self._values.get("authentication_type")
        assert result is not None, "Required property 'authentication_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def api_key(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKey"]:
        '''api_key block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#api_key AppflowConnectorProfile#api_key}
        '''
        result = self._values.get("api_key")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKey"], result)

    @builtins.property
    def basic(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasic"]:
        '''basic block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#basic AppflowConnectorProfile#basic}
        '''
        result = self._values.get("basic")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasic"], result)

    @builtins.property
    def custom(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustom"]:
        '''custom block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#custom AppflowConnectorProfile#custom}
        '''
        result = self._values.get("custom")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustom"], result)

    @builtins.property
    def oauth2(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2"]:
        '''oauth2 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth2 AppflowConnectorProfile#oauth2}
        '''
        result = self._values.get("oauth2")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKey",
    jsii_struct_bases=[],
    name_mapping={"api_key": "apiKey", "api_secret_key": "apiSecretKey"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKey:
    def __init__(
        self,
        *,
        api_key: builtins.str,
        api_secret_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param api_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#api_key AppflowConnectorProfile#api_key}.
        :param api_secret_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#api_secret_key AppflowConnectorProfile#api_secret_key}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9cbd7a8c0343b3065d53c4331b2a421fb528545de1d166649e6b55a05ece2b9a)
            check_type(argname="argument api_key", value=api_key, expected_type=type_hints["api_key"])
            check_type(argname="argument api_secret_key", value=api_secret_key, expected_type=type_hints["api_secret_key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_key": api_key,
        }
        if api_secret_key is not None:
            self._values["api_secret_key"] = api_secret_key

    @builtins.property
    def api_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#api_key AppflowConnectorProfile#api_key}.'''
        result = self._values.get("api_key")
        assert result is not None, "Required property 'api_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def api_secret_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#api_secret_key AppflowConnectorProfile#api_secret_key}.'''
        result = self._values.get("api_secret_key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKeyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKeyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7f86fc09f574869766b1c468dbfe70aac2eb601611c399479f13df06a6bc779a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetApiSecretKey")
    def reset_api_secret_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiSecretKey", []))

    @builtins.property
    @jsii.member(jsii_name="apiKeyInput")
    def api_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="apiSecretKeyInput")
    def api_secret_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiSecretKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="apiKey")
    def api_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiKey"))

    @api_key.setter
    def api_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__552b3a8c60115ab9c655c7d4be8e137e2f0cb5532cc5b7530e1e80adf8332d24)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiKey", value)

    @builtins.property
    @jsii.member(jsii_name="apiSecretKey")
    def api_secret_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiSecretKey"))

    @api_secret_key.setter
    def api_secret_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24ac690f4063c8b9fb71f1c9d54d50ee26d74131f06dd06f01a4f9cb3b5e0eb8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiSecretKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKey]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKey], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKey],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd59fe929ad04e61dc16a5ba09d1cacb52edd16be0e8ccbf0315cc5dd7c772a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasic",
    jsii_struct_bases=[],
    name_mapping={"password": "password", "username": "username"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasic:
    def __init__(self, *, password: builtins.str, username: builtins.str) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#password AppflowConnectorProfile#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#username AppflowConnectorProfile#username}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d4b2d2ef86af0a51a9a518549a33921c93923394213a80c55dd989713e62e4b)
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "password": password,
            "username": username,
        }

    @builtins.property
    def password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#password AppflowConnectorProfile#password}.'''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#username AppflowConnectorProfile#username}.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasic(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasicOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasicOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5c2318212120443d9cc650795f04cb86f935806720681a036c0ccd4ef54ef716)
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
            type_hints = typing.get_type_hints(_typecheckingstub__aba4dd4bb587f70db19e55176395c2386c00d8a1bc7285c26772fec053168cce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7c78864dab2ef39a9b7d8876d8ce917d45d7985cf4c3f3ee4603b7878af842e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasic]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasic], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasic],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__022045c0cb00c1dc959cd7f4fcafe0194808e2e7fb71099a57fb30a1bf3e8be9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustom",
    jsii_struct_bases=[],
    name_mapping={
        "custom_authentication_type": "customAuthenticationType",
        "credentials_map": "credentialsMap",
    },
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustom:
    def __init__(
        self,
        *,
        custom_authentication_type: builtins.str,
        credentials_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param custom_authentication_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#custom_authentication_type AppflowConnectorProfile#custom_authentication_type}.
        :param credentials_map: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#credentials_map AppflowConnectorProfile#credentials_map}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94afd2390fb7351382086adb0166647abd98d648536688e00a92c76b68b4b0ab)
            check_type(argname="argument custom_authentication_type", value=custom_authentication_type, expected_type=type_hints["custom_authentication_type"])
            check_type(argname="argument credentials_map", value=credentials_map, expected_type=type_hints["credentials_map"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "custom_authentication_type": custom_authentication_type,
        }
        if credentials_map is not None:
            self._values["credentials_map"] = credentials_map

    @builtins.property
    def custom_authentication_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#custom_authentication_type AppflowConnectorProfile#custom_authentication_type}.'''
        result = self._values.get("custom_authentication_type")
        assert result is not None, "Required property 'custom_authentication_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def credentials_map(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#credentials_map AppflowConnectorProfile#credentials_map}.'''
        result = self._values.get("credentials_map")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustom(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustomOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustomOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7e1c7c66cccd4475cedfc818fd35ac791f7cfffc109f5607795a158db4b48341)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCredentialsMap")
    def reset_credentials_map(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCredentialsMap", []))

    @builtins.property
    @jsii.member(jsii_name="credentialsMapInput")
    def credentials_map_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "credentialsMapInput"))

    @builtins.property
    @jsii.member(jsii_name="customAuthenticationTypeInput")
    def custom_authentication_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customAuthenticationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="credentialsMap")
    def credentials_map(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "credentialsMap"))

    @credentials_map.setter
    def credentials_map(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9402c95209d848ad39902fca313a2883143ad78bfa3bcf9e200818378835e2c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "credentialsMap", value)

    @builtins.property
    @jsii.member(jsii_name="customAuthenticationType")
    def custom_authentication_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customAuthenticationType"))

    @custom_authentication_type.setter
    def custom_authentication_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34c6b41d6702476637538132327652710e4f7b567e30e01e5c4c4d718688c55f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customAuthenticationType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustom]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustom], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustom],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4c803641f41d61ba5d72358fb532862c2078669f07e18815f9cc1645ed2cb45)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2",
    jsii_struct_bases=[],
    name_mapping={
        "access_token": "accessToken",
        "client_id": "clientId",
        "client_secret": "clientSecret",
        "oauth_request": "oauthRequest",
        "refresh_token": "refreshToken",
    },
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2:
    def __init__(
        self,
        *,
        access_token: typing.Optional[builtins.str] = None,
        client_id: typing.Optional[builtins.str] = None,
        client_secret: typing.Optional[builtins.str] = None,
        oauth_request: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequest", typing.Dict[builtins.str, typing.Any]]] = None,
        refresh_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_token AppflowConnectorProfile#access_token}.
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_id AppflowConnectorProfile#client_id}.
        :param client_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_secret AppflowConnectorProfile#client_secret}.
        :param oauth_request: oauth_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_request AppflowConnectorProfile#oauth_request}
        :param refresh_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#refresh_token AppflowConnectorProfile#refresh_token}.
        '''
        if isinstance(oauth_request, dict):
            oauth_request = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequest(**oauth_request)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af28b6af78b0a60ef8c3f74185788e5aef77e0c15995eb935da5d2911ed393da)
            check_type(argname="argument access_token", value=access_token, expected_type=type_hints["access_token"])
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
            check_type(argname="argument oauth_request", value=oauth_request, expected_type=type_hints["oauth_request"])
            check_type(argname="argument refresh_token", value=refresh_token, expected_type=type_hints["refresh_token"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if access_token is not None:
            self._values["access_token"] = access_token
        if client_id is not None:
            self._values["client_id"] = client_id
        if client_secret is not None:
            self._values["client_secret"] = client_secret
        if oauth_request is not None:
            self._values["oauth_request"] = oauth_request
        if refresh_token is not None:
            self._values["refresh_token"] = refresh_token

    @builtins.property
    def access_token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_token AppflowConnectorProfile#access_token}.'''
        result = self._values.get("access_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_id AppflowConnectorProfile#client_id}.'''
        result = self._values.get("client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_secret(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_secret AppflowConnectorProfile#client_secret}.'''
        result = self._values.get("client_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_request(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequest"]:
        '''oauth_request block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_request AppflowConnectorProfile#oauth_request}
        '''
        result = self._values.get("oauth_request")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequest"], result)

    @builtins.property
    def refresh_token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#refresh_token AppflowConnectorProfile#refresh_token}.'''
        result = self._values.get("refresh_token")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequest",
    jsii_struct_bases=[],
    name_mapping={"auth_code": "authCode", "redirect_uri": "redirectUri"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequest:
    def __init__(
        self,
        *,
        auth_code: typing.Optional[builtins.str] = None,
        redirect_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code AppflowConnectorProfile#auth_code}.
        :param redirect_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redirect_uri AppflowConnectorProfile#redirect_uri}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2479ad553e3db9cf7c36aba2b86f8673a508e514fd1297675d5c3d1b1232d6a2)
            check_type(argname="argument auth_code", value=auth_code, expected_type=type_hints["auth_code"])
            check_type(argname="argument redirect_uri", value=redirect_uri, expected_type=type_hints["redirect_uri"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if auth_code is not None:
            self._values["auth_code"] = auth_code
        if redirect_uri is not None:
            self._values["redirect_uri"] = redirect_uri

    @builtins.property
    def auth_code(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code AppflowConnectorProfile#auth_code}.'''
        result = self._values.get("auth_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def redirect_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redirect_uri AppflowConnectorProfile#redirect_uri}.'''
        result = self._values.get("redirect_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequestOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequestOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8f76a4839555202c3411b6be7e0bbd03a3a1a9868560b25606521ca335073fb0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAuthCode")
    def reset_auth_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthCode", []))

    @jsii.member(jsii_name="resetRedirectUri")
    def reset_redirect_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedirectUri", []))

    @builtins.property
    @jsii.member(jsii_name="authCodeInput")
    def auth_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectUriInput")
    def redirect_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "redirectUriInput"))

    @builtins.property
    @jsii.member(jsii_name="authCode")
    def auth_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authCode"))

    @auth_code.setter
    def auth_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__663c6adf32f8e6605263787cb926260829902981363e72f183fe1eef664e08ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authCode", value)

    @builtins.property
    @jsii.member(jsii_name="redirectUri")
    def redirect_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redirectUri"))

    @redirect_uri.setter
    def redirect_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5884a3f7af422b7fa7bee2ba3674d961385e23dc4778dfddd5576bfb720500f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redirectUri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequest]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequest], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequest],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7dcc5c1fde74871448da356ed480b8774071c38e5efdd65b1ff49930babdcf4c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__81f514d01bd9a036e4084acd88ebfbd30f2d19c8fb6e4f3ea0ea33e41113840d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putOauthRequest")
    def put_oauth_request(
        self,
        *,
        auth_code: typing.Optional[builtins.str] = None,
        redirect_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code AppflowConnectorProfile#auth_code}.
        :param redirect_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redirect_uri AppflowConnectorProfile#redirect_uri}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequest(
            auth_code=auth_code, redirect_uri=redirect_uri
        )

        return typing.cast(None, jsii.invoke(self, "putOauthRequest", [value]))

    @jsii.member(jsii_name="resetAccessToken")
    def reset_access_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessToken", []))

    @jsii.member(jsii_name="resetClientId")
    def reset_client_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientId", []))

    @jsii.member(jsii_name="resetClientSecret")
    def reset_client_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientSecret", []))

    @jsii.member(jsii_name="resetOauthRequest")
    def reset_oauth_request(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthRequest", []))

    @jsii.member(jsii_name="resetRefreshToken")
    def reset_refresh_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRefreshToken", []))

    @builtins.property
    @jsii.member(jsii_name="oauthRequest")
    def oauth_request(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequestOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequestOutputReference, jsii.get(self, "oauthRequest"))

    @builtins.property
    @jsii.member(jsii_name="accessTokenInput")
    def access_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretInput")
    def client_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthRequestInput")
    def oauth_request_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequest]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequest], jsii.get(self, "oauthRequestInput"))

    @builtins.property
    @jsii.member(jsii_name="refreshTokenInput")
    def refresh_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "refreshTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="accessToken")
    def access_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessToken"))

    @access_token.setter
    def access_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44851f56f1a97eb1a07fefc69654bbb5602993a68ebd50437ee47f391f6b7981)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessToken", value)

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea8bbba5acd0b760fcdd6674c5cb69722a8b42942471208a4e00869f0f80fa5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0cf671349aecc891150e705abccaea63122498cd63001b3ecb0ad748e0c2db42)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="refreshToken")
    def refresh_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "refreshToken"))

    @refresh_token.setter
    def refresh_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bf35ee5c8c1ebc7838cb0791d21c85b5e34627b5ced33d87f9286bd15e808c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "refreshToken", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35729fb13f908bd160a2f77d3275cdc622335462d69287183b123a4e54d063a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a32fc211edd3db9575cf2ecf24bfb1b9039e5d136fbb7d05354e85c9a21de82e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putApiKey")
    def put_api_key(
        self,
        *,
        api_key: builtins.str,
        api_secret_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param api_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#api_key AppflowConnectorProfile#api_key}.
        :param api_secret_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#api_secret_key AppflowConnectorProfile#api_secret_key}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKey(
            api_key=api_key, api_secret_key=api_secret_key
        )

        return typing.cast(None, jsii.invoke(self, "putApiKey", [value]))

    @jsii.member(jsii_name="putBasic")
    def put_basic(self, *, password: builtins.str, username: builtins.str) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#password AppflowConnectorProfile#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#username AppflowConnectorProfile#username}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasic(
            password=password, username=username
        )

        return typing.cast(None, jsii.invoke(self, "putBasic", [value]))

    @jsii.member(jsii_name="putCustom")
    def put_custom(
        self,
        *,
        custom_authentication_type: builtins.str,
        credentials_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param custom_authentication_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#custom_authentication_type AppflowConnectorProfile#custom_authentication_type}.
        :param credentials_map: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#credentials_map AppflowConnectorProfile#credentials_map}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustom(
            custom_authentication_type=custom_authentication_type,
            credentials_map=credentials_map,
        )

        return typing.cast(None, jsii.invoke(self, "putCustom", [value]))

    @jsii.member(jsii_name="putOauth2")
    def put_oauth2(
        self,
        *,
        access_token: typing.Optional[builtins.str] = None,
        client_id: typing.Optional[builtins.str] = None,
        client_secret: typing.Optional[builtins.str] = None,
        oauth_request: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequest, typing.Dict[builtins.str, typing.Any]]] = None,
        refresh_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_token AppflowConnectorProfile#access_token}.
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_id AppflowConnectorProfile#client_id}.
        :param client_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_secret AppflowConnectorProfile#client_secret}.
        :param oauth_request: oauth_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_request AppflowConnectorProfile#oauth_request}
        :param refresh_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#refresh_token AppflowConnectorProfile#refresh_token}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2(
            access_token=access_token,
            client_id=client_id,
            client_secret=client_secret,
            oauth_request=oauth_request,
            refresh_token=refresh_token,
        )

        return typing.cast(None, jsii.invoke(self, "putOauth2", [value]))

    @jsii.member(jsii_name="resetApiKey")
    def reset_api_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiKey", []))

    @jsii.member(jsii_name="resetBasic")
    def reset_basic(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBasic", []))

    @jsii.member(jsii_name="resetCustom")
    def reset_custom(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustom", []))

    @jsii.member(jsii_name="resetOauth2")
    def reset_oauth2(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauth2", []))

    @builtins.property
    @jsii.member(jsii_name="apiKey")
    def api_key(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKeyOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKeyOutputReference, jsii.get(self, "apiKey"))

    @builtins.property
    @jsii.member(jsii_name="basic")
    def basic(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasicOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasicOutputReference, jsii.get(self, "basic"))

    @builtins.property
    @jsii.member(jsii_name="custom")
    def custom(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustomOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustomOutputReference, jsii.get(self, "custom"))

    @builtins.property
    @jsii.member(jsii_name="oauth2")
    def oauth2(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OutputReference, jsii.get(self, "oauth2"))

    @builtins.property
    @jsii.member(jsii_name="apiKeyInput")
    def api_key_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKey]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKey], jsii.get(self, "apiKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="authenticationTypeInput")
    def authentication_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authenticationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="basicInput")
    def basic_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasic]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasic], jsii.get(self, "basicInput"))

    @builtins.property
    @jsii.member(jsii_name="customInput")
    def custom_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustom]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustom], jsii.get(self, "customInput"))

    @builtins.property
    @jsii.member(jsii_name="oauth2Input")
    def oauth2_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2], jsii.get(self, "oauth2Input"))

    @builtins.property
    @jsii.member(jsii_name="authenticationType")
    def authentication_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authenticationType"))

    @authentication_type.setter
    def authentication_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9d9436561df75df4de1113ac1864f3778441bdd99b04cad4bdea0eb4fe707ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authenticationType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnector]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnector], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnector],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9104533818b8d31a5462969a0dc6b3ede080b08152e3cd3dfe8b13c6f87f6186)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadog",
    jsii_struct_bases=[],
    name_mapping={"api_key": "apiKey", "application_key": "applicationKey"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadog:
    def __init__(self, *, api_key: builtins.str, application_key: builtins.str) -> None:
        '''
        :param api_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#api_key AppflowConnectorProfile#api_key}.
        :param application_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#application_key AppflowConnectorProfile#application_key}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76cceacfcce609f35f018cbd20125e03c7becebb977c784dad28ebf94b5b026f)
            check_type(argname="argument api_key", value=api_key, expected_type=type_hints["api_key"])
            check_type(argname="argument application_key", value=application_key, expected_type=type_hints["application_key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_key": api_key,
            "application_key": application_key,
        }

    @builtins.property
    def api_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#api_key AppflowConnectorProfile#api_key}.'''
        result = self._values.get("api_key")
        assert result is not None, "Required property 'api_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def application_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#application_key AppflowConnectorProfile#application_key}.'''
        result = self._values.get("application_key")
        assert result is not None, "Required property 'application_key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadog(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadogOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadogOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bf7d62a861681a7bac83b2366e5a346c4be9bb070d838e6ec77a9420bd33b505)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="apiKeyInput")
    def api_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="applicationKeyInput")
    def application_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applicationKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="apiKey")
    def api_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiKey"))

    @api_key.setter
    def api_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__798c10ab6f86a6022638f85875253c3b26abbfcb5085e4b02af979754a94d2b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiKey", value)

    @builtins.property
    @jsii.member(jsii_name="applicationKey")
    def application_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "applicationKey"))

    @application_key.setter
    def application_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__344e8b6a6a7b23a342d0652be4276d4b5999386b3b30e7b34fa168d785a68afc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadog]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadog], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadog],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba344cd4f3bfc4273fc53db3a93a4de4fa052712031cebb06eaf64f8e2bd6545)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatrace",
    jsii_struct_bases=[],
    name_mapping={"api_token": "apiToken"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatrace:
    def __init__(self, *, api_token: builtins.str) -> None:
        '''
        :param api_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#api_token AppflowConnectorProfile#api_token}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__358e6f20c136071ed498a406a422b41ce3c3b7916057dda25f428d130fe35030)
            check_type(argname="argument api_token", value=api_token, expected_type=type_hints["api_token"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_token": api_token,
        }

    @builtins.property
    def api_token(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#api_token AppflowConnectorProfile#api_token}.'''
        result = self._values.get("api_token")
        assert result is not None, "Required property 'api_token' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatrace(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatraceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatraceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__99049168d99d7970cdcd8ad048bd9e864c83fb6cb1605c3bce034a2cc8877dde)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="apiTokenInput")
    def api_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="apiToken")
    def api_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiToken"))

    @api_token.setter
    def api_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9747717c1dc28b298d3827fe812522633f477863d50ac33627f139524fe49de1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiToken", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatrace]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatrace], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatrace],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6883891ec1e115b322ac9a05552b1a8b9efdccdda67b2824c16bbe93b508fd4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalytics",
    jsii_struct_bases=[],
    name_mapping={
        "client_id": "clientId",
        "client_secret": "clientSecret",
        "access_token": "accessToken",
        "oauth_request": "oauthRequest",
        "refresh_token": "refreshToken",
    },
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalytics:
    def __init__(
        self,
        *,
        client_id: builtins.str,
        client_secret: builtins.str,
        access_token: typing.Optional[builtins.str] = None,
        oauth_request: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequest", typing.Dict[builtins.str, typing.Any]]] = None,
        refresh_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_id AppflowConnectorProfile#client_id}.
        :param client_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_secret AppflowConnectorProfile#client_secret}.
        :param access_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_token AppflowConnectorProfile#access_token}.
        :param oauth_request: oauth_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_request AppflowConnectorProfile#oauth_request}
        :param refresh_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#refresh_token AppflowConnectorProfile#refresh_token}.
        '''
        if isinstance(oauth_request, dict):
            oauth_request = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequest(**oauth_request)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__755a66fd23787930c9d972a7eb066940b1cd68196c05e29ac05bd0b4e1430158)
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
            check_type(argname="argument access_token", value=access_token, expected_type=type_hints["access_token"])
            check_type(argname="argument oauth_request", value=oauth_request, expected_type=type_hints["oauth_request"])
            check_type(argname="argument refresh_token", value=refresh_token, expected_type=type_hints["refresh_token"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "client_id": client_id,
            "client_secret": client_secret,
        }
        if access_token is not None:
            self._values["access_token"] = access_token
        if oauth_request is not None:
            self._values["oauth_request"] = oauth_request
        if refresh_token is not None:
            self._values["refresh_token"] = refresh_token

    @builtins.property
    def client_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_id AppflowConnectorProfile#client_id}.'''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_secret AppflowConnectorProfile#client_secret}.'''
        result = self._values.get("client_secret")
        assert result is not None, "Required property 'client_secret' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_token AppflowConnectorProfile#access_token}.'''
        result = self._values.get("access_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_request(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequest"]:
        '''oauth_request block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_request AppflowConnectorProfile#oauth_request}
        '''
        result = self._values.get("oauth_request")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequest"], result)

    @builtins.property
    def refresh_token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#refresh_token AppflowConnectorProfile#refresh_token}.'''
        result = self._values.get("refresh_token")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalytics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequest",
    jsii_struct_bases=[],
    name_mapping={"auth_code": "authCode", "redirect_uri": "redirectUri"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequest:
    def __init__(
        self,
        *,
        auth_code: typing.Optional[builtins.str] = None,
        redirect_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code AppflowConnectorProfile#auth_code}.
        :param redirect_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redirect_uri AppflowConnectorProfile#redirect_uri}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__623fbed82966657247b3d4964998827825e51e3ae007483e0023aaa75bb1bf39)
            check_type(argname="argument auth_code", value=auth_code, expected_type=type_hints["auth_code"])
            check_type(argname="argument redirect_uri", value=redirect_uri, expected_type=type_hints["redirect_uri"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if auth_code is not None:
            self._values["auth_code"] = auth_code
        if redirect_uri is not None:
            self._values["redirect_uri"] = redirect_uri

    @builtins.property
    def auth_code(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code AppflowConnectorProfile#auth_code}.'''
        result = self._values.get("auth_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def redirect_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redirect_uri AppflowConnectorProfile#redirect_uri}.'''
        result = self._values.get("redirect_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequestOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequestOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3492bcc0c0e95908bf9c6a16e55e8439db3030f5e1bdb1ca298d86e48de95615)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAuthCode")
    def reset_auth_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthCode", []))

    @jsii.member(jsii_name="resetRedirectUri")
    def reset_redirect_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedirectUri", []))

    @builtins.property
    @jsii.member(jsii_name="authCodeInput")
    def auth_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectUriInput")
    def redirect_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "redirectUriInput"))

    @builtins.property
    @jsii.member(jsii_name="authCode")
    def auth_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authCode"))

    @auth_code.setter
    def auth_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d534b8da128c51abdeafadaf48253b635c99b86c2b13f774c35d6aa4ec65d4c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authCode", value)

    @builtins.property
    @jsii.member(jsii_name="redirectUri")
    def redirect_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redirectUri"))

    @redirect_uri.setter
    def redirect_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afb9b7c1d3643a644d5cfd2601243e6f5b81e3772c1a844da31d945b7985791f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redirectUri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequest]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequest], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequest],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bc5282e0c3b572e7ff6e30640ae3eabe9d80c5eab9ef6aad3c3b0c783c40f33)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__62645b32e596e510bdaf802520ccf9088ed18c48d033cf8a79b19dfef46baec8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putOauthRequest")
    def put_oauth_request(
        self,
        *,
        auth_code: typing.Optional[builtins.str] = None,
        redirect_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code AppflowConnectorProfile#auth_code}.
        :param redirect_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redirect_uri AppflowConnectorProfile#redirect_uri}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequest(
            auth_code=auth_code, redirect_uri=redirect_uri
        )

        return typing.cast(None, jsii.invoke(self, "putOauthRequest", [value]))

    @jsii.member(jsii_name="resetAccessToken")
    def reset_access_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessToken", []))

    @jsii.member(jsii_name="resetOauthRequest")
    def reset_oauth_request(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthRequest", []))

    @jsii.member(jsii_name="resetRefreshToken")
    def reset_refresh_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRefreshToken", []))

    @builtins.property
    @jsii.member(jsii_name="oauthRequest")
    def oauth_request(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequestOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequestOutputReference, jsii.get(self, "oauthRequest"))

    @builtins.property
    @jsii.member(jsii_name="accessTokenInput")
    def access_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretInput")
    def client_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthRequestInput")
    def oauth_request_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequest]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequest], jsii.get(self, "oauthRequestInput"))

    @builtins.property
    @jsii.member(jsii_name="refreshTokenInput")
    def refresh_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "refreshTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="accessToken")
    def access_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessToken"))

    @access_token.setter
    def access_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cbe109c7f4994d8152430635d045f2c84f136803a6d4ebe904c1af2e7ac8a9b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessToken", value)

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23d3b1fea0a699ad81e0fd38172c4cc5e1d1bc139c7a5fa793855367640986e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e403d357f8ae5e289c17198fdf54abbeae333f20bdbbd79cb4f72e0f23305e42)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="refreshToken")
    def refresh_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "refreshToken"))

    @refresh_token.setter
    def refresh_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9513dd1a6cf5c98a8cf6c72caee8c574d48cfbe966efd615d28f5ad6a3a4e2e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "refreshToken", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalytics]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalytics], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalytics],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d50c8a22d1755efd664fe0edcf6fdd270512ed5fdbd332e0b7a8f9561a35d86)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycode",
    jsii_struct_bases=[],
    name_mapping={
        "access_token": "accessToken",
        "oauth_request": "oauthRequest",
        "refresh_token": "refreshToken",
    },
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycode:
    def __init__(
        self,
        *,
        access_token: typing.Optional[builtins.str] = None,
        oauth_request: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequest", typing.Dict[builtins.str, typing.Any]]] = None,
        refresh_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_token AppflowConnectorProfile#access_token}.
        :param oauth_request: oauth_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_request AppflowConnectorProfile#oauth_request}
        :param refresh_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#refresh_token AppflowConnectorProfile#refresh_token}.
        '''
        if isinstance(oauth_request, dict):
            oauth_request = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequest(**oauth_request)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15f2ba7ba11ea1f63b58d287cc74b9a2fc16a1be1abb559cb7e5f2bdc7c9d271)
            check_type(argname="argument access_token", value=access_token, expected_type=type_hints["access_token"])
            check_type(argname="argument oauth_request", value=oauth_request, expected_type=type_hints["oauth_request"])
            check_type(argname="argument refresh_token", value=refresh_token, expected_type=type_hints["refresh_token"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if access_token is not None:
            self._values["access_token"] = access_token
        if oauth_request is not None:
            self._values["oauth_request"] = oauth_request
        if refresh_token is not None:
            self._values["refresh_token"] = refresh_token

    @builtins.property
    def access_token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_token AppflowConnectorProfile#access_token}.'''
        result = self._values.get("access_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_request(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequest"]:
        '''oauth_request block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_request AppflowConnectorProfile#oauth_request}
        '''
        result = self._values.get("oauth_request")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequest"], result)

    @builtins.property
    def refresh_token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#refresh_token AppflowConnectorProfile#refresh_token}.'''
        result = self._values.get("refresh_token")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycode(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequest",
    jsii_struct_bases=[],
    name_mapping={"auth_code": "authCode", "redirect_uri": "redirectUri"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequest:
    def __init__(
        self,
        *,
        auth_code: typing.Optional[builtins.str] = None,
        redirect_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code AppflowConnectorProfile#auth_code}.
        :param redirect_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redirect_uri AppflowConnectorProfile#redirect_uri}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__891826f62d5ba8de245a53c065f25789d4e8997311d10fef4a54920c18257419)
            check_type(argname="argument auth_code", value=auth_code, expected_type=type_hints["auth_code"])
            check_type(argname="argument redirect_uri", value=redirect_uri, expected_type=type_hints["redirect_uri"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if auth_code is not None:
            self._values["auth_code"] = auth_code
        if redirect_uri is not None:
            self._values["redirect_uri"] = redirect_uri

    @builtins.property
    def auth_code(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code AppflowConnectorProfile#auth_code}.'''
        result = self._values.get("auth_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def redirect_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redirect_uri AppflowConnectorProfile#redirect_uri}.'''
        result = self._values.get("redirect_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequestOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequestOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2e9e290eed65104bac368b32e2ec9b79ba2dd317a3156178adf3ff208930b78c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAuthCode")
    def reset_auth_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthCode", []))

    @jsii.member(jsii_name="resetRedirectUri")
    def reset_redirect_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedirectUri", []))

    @builtins.property
    @jsii.member(jsii_name="authCodeInput")
    def auth_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectUriInput")
    def redirect_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "redirectUriInput"))

    @builtins.property
    @jsii.member(jsii_name="authCode")
    def auth_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authCode"))

    @auth_code.setter
    def auth_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8af7b9499406d7ddb533845b7dd61f79e85c3dff16d38a5ea55302d9c061547)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authCode", value)

    @builtins.property
    @jsii.member(jsii_name="redirectUri")
    def redirect_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redirectUri"))

    @redirect_uri.setter
    def redirect_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e111b3de83493aa2a5a113f338253cbf261298ddcb4990f0fe6b12ca81460ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redirectUri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequest]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequest], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequest],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__977759a1481045cf5d2216e0588418dff35380a0dbf3db47dd8519e323079af3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0757aa39c21db62005386b06f33b4d8394bfafb1b2bd27936f472fd911efacaf)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putOauthRequest")
    def put_oauth_request(
        self,
        *,
        auth_code: typing.Optional[builtins.str] = None,
        redirect_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code AppflowConnectorProfile#auth_code}.
        :param redirect_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redirect_uri AppflowConnectorProfile#redirect_uri}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequest(
            auth_code=auth_code, redirect_uri=redirect_uri
        )

        return typing.cast(None, jsii.invoke(self, "putOauthRequest", [value]))

    @jsii.member(jsii_name="resetAccessToken")
    def reset_access_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessToken", []))

    @jsii.member(jsii_name="resetOauthRequest")
    def reset_oauth_request(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthRequest", []))

    @jsii.member(jsii_name="resetRefreshToken")
    def reset_refresh_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRefreshToken", []))

    @builtins.property
    @jsii.member(jsii_name="oauthRequest")
    def oauth_request(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequestOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequestOutputReference, jsii.get(self, "oauthRequest"))

    @builtins.property
    @jsii.member(jsii_name="accessTokenInput")
    def access_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthRequestInput")
    def oauth_request_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequest]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequest], jsii.get(self, "oauthRequestInput"))

    @builtins.property
    @jsii.member(jsii_name="refreshTokenInput")
    def refresh_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "refreshTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="accessToken")
    def access_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessToken"))

    @access_token.setter
    def access_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1bcda14dea3afa4b5ef5a194c7da2123ea7b7cd0dea0f50bc89a9fafa857244a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessToken", value)

    @builtins.property
    @jsii.member(jsii_name="refreshToken")
    def refresh_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "refreshToken"))

    @refresh_token.setter
    def refresh_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2f767823c0b5700e9980ffb09ab16c11c4c9ac4f614fda26214a29e6b8bf04e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "refreshToken", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycode]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycode], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycode],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2559e8f2b37921dbff7d02b228b6a8be69cfeba1f3b8d9d8f9c66026536a10ca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexus",
    jsii_struct_bases=[],
    name_mapping={
        "access_key_id": "accessKeyId",
        "datakey": "datakey",
        "secret_access_key": "secretAccessKey",
        "user_id": "userId",
    },
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexus:
    def __init__(
        self,
        *,
        access_key_id: builtins.str,
        datakey: builtins.str,
        secret_access_key: builtins.str,
        user_id: builtins.str,
    ) -> None:
        '''
        :param access_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_key_id AppflowConnectorProfile#access_key_id}.
        :param datakey: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#datakey AppflowConnectorProfile#datakey}.
        :param secret_access_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#secret_access_key AppflowConnectorProfile#secret_access_key}.
        :param user_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#user_id AppflowConnectorProfile#user_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1cdb791c31c9000b9e446294d82216a85dbfff20e48f5797a9a5d1c39227031)
            check_type(argname="argument access_key_id", value=access_key_id, expected_type=type_hints["access_key_id"])
            check_type(argname="argument datakey", value=datakey, expected_type=type_hints["datakey"])
            check_type(argname="argument secret_access_key", value=secret_access_key, expected_type=type_hints["secret_access_key"])
            check_type(argname="argument user_id", value=user_id, expected_type=type_hints["user_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "access_key_id": access_key_id,
            "datakey": datakey,
            "secret_access_key": secret_access_key,
            "user_id": user_id,
        }

    @builtins.property
    def access_key_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_key_id AppflowConnectorProfile#access_key_id}.'''
        result = self._values.get("access_key_id")
        assert result is not None, "Required property 'access_key_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def datakey(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#datakey AppflowConnectorProfile#datakey}.'''
        result = self._values.get("datakey")
        assert result is not None, "Required property 'datakey' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def secret_access_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#secret_access_key AppflowConnectorProfile#secret_access_key}.'''
        result = self._values.get("secret_access_key")
        assert result is not None, "Required property 'secret_access_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#user_id AppflowConnectorProfile#user_id}.'''
        result = self._values.get("user_id")
        assert result is not None, "Required property 'user_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexus(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexusOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexusOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__73cc6cb656c384b019813169cd70f7f19800e0226531ce39d1074766d88b9896)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="accessKeyIdInput")
    def access_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="datakeyInput")
    def datakey_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datakeyInput"))

    @builtins.property
    @jsii.member(jsii_name="secretAccessKeyInput")
    def secret_access_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretAccessKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="userIdInput")
    def user_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userIdInput"))

    @builtins.property
    @jsii.member(jsii_name="accessKeyId")
    def access_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessKeyId"))

    @access_key_id.setter
    def access_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__646bff31e9c436ef46c97ec78ae722c89a618486877f2246c1ebf87d2b956972)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="datakey")
    def datakey(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datakey"))

    @datakey.setter
    def datakey(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da0fbc14e3064895074e97c7224ec4421027137e24466cd64a9974298f0f58c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datakey", value)

    @builtins.property
    @jsii.member(jsii_name="secretAccessKey")
    def secret_access_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretAccessKey"))

    @secret_access_key.setter
    def secret_access_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae944892a1fbe5b5ddf455de169c6001b0010eee7eb7cb271ae1fbfd8d1460f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretAccessKey", value)

    @builtins.property
    @jsii.member(jsii_name="userId")
    def user_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userId"))

    @user_id.setter
    def user_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__072f5b723415c40d8a695a8d81c08fd0be691b6475e6ef213ad85f08880c60d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexus]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexus], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexus],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1294d360fbcd349d2fb817a5c496fb0a84ccaf9403cb5caa6cdf62cda9d9bd95)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketo",
    jsii_struct_bases=[],
    name_mapping={
        "client_id": "clientId",
        "client_secret": "clientSecret",
        "access_token": "accessToken",
        "oauth_request": "oauthRequest",
    },
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketo:
    def __init__(
        self,
        *,
        client_id: builtins.str,
        client_secret: builtins.str,
        access_token: typing.Optional[builtins.str] = None,
        oauth_request: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequest", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_id AppflowConnectorProfile#client_id}.
        :param client_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_secret AppflowConnectorProfile#client_secret}.
        :param access_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_token AppflowConnectorProfile#access_token}.
        :param oauth_request: oauth_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_request AppflowConnectorProfile#oauth_request}
        '''
        if isinstance(oauth_request, dict):
            oauth_request = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequest(**oauth_request)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8509a0f1442b61dca4f3a1dcb0759b821b4b79c9aa2d1401d9400505c81b2d5c)
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
            check_type(argname="argument access_token", value=access_token, expected_type=type_hints["access_token"])
            check_type(argname="argument oauth_request", value=oauth_request, expected_type=type_hints["oauth_request"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "client_id": client_id,
            "client_secret": client_secret,
        }
        if access_token is not None:
            self._values["access_token"] = access_token
        if oauth_request is not None:
            self._values["oauth_request"] = oauth_request

    @builtins.property
    def client_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_id AppflowConnectorProfile#client_id}.'''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_secret AppflowConnectorProfile#client_secret}.'''
        result = self._values.get("client_secret")
        assert result is not None, "Required property 'client_secret' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_token AppflowConnectorProfile#access_token}.'''
        result = self._values.get("access_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_request(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequest"]:
        '''oauth_request block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_request AppflowConnectorProfile#oauth_request}
        '''
        result = self._values.get("oauth_request")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequest"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequest",
    jsii_struct_bases=[],
    name_mapping={"auth_code": "authCode", "redirect_uri": "redirectUri"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequest:
    def __init__(
        self,
        *,
        auth_code: typing.Optional[builtins.str] = None,
        redirect_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code AppflowConnectorProfile#auth_code}.
        :param redirect_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redirect_uri AppflowConnectorProfile#redirect_uri}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ecd6627ed4bf57528f035700e5fe6c9a8f487b5b8325ea78eadba0b1be18ef05)
            check_type(argname="argument auth_code", value=auth_code, expected_type=type_hints["auth_code"])
            check_type(argname="argument redirect_uri", value=redirect_uri, expected_type=type_hints["redirect_uri"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if auth_code is not None:
            self._values["auth_code"] = auth_code
        if redirect_uri is not None:
            self._values["redirect_uri"] = redirect_uri

    @builtins.property
    def auth_code(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code AppflowConnectorProfile#auth_code}.'''
        result = self._values.get("auth_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def redirect_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redirect_uri AppflowConnectorProfile#redirect_uri}.'''
        result = self._values.get("redirect_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequestOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequestOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__956b70819122bc6083c2e31115ccff5b700eb7491ead09479254733289d24c25)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAuthCode")
    def reset_auth_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthCode", []))

    @jsii.member(jsii_name="resetRedirectUri")
    def reset_redirect_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedirectUri", []))

    @builtins.property
    @jsii.member(jsii_name="authCodeInput")
    def auth_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectUriInput")
    def redirect_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "redirectUriInput"))

    @builtins.property
    @jsii.member(jsii_name="authCode")
    def auth_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authCode"))

    @auth_code.setter
    def auth_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b8898b53437a49f74847aca6fcd659248879b6e01355cdf5d8fa448144666e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authCode", value)

    @builtins.property
    @jsii.member(jsii_name="redirectUri")
    def redirect_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redirectUri"))

    @redirect_uri.setter
    def redirect_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29ba99cac108d2d9d3e52f741fc2a5092e400981d0d65660cf76e83a8c617d88)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redirectUri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequest]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequest], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequest],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2120f483e64e53deb9c8531d8f05868c69ea2a2dd8d8d06d2e353cfc46b20e5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__01b2d8a1157f2dcde07ec68016aaeb45553730b4bb5fddc69e639b73368d15a8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putOauthRequest")
    def put_oauth_request(
        self,
        *,
        auth_code: typing.Optional[builtins.str] = None,
        redirect_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code AppflowConnectorProfile#auth_code}.
        :param redirect_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redirect_uri AppflowConnectorProfile#redirect_uri}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequest(
            auth_code=auth_code, redirect_uri=redirect_uri
        )

        return typing.cast(None, jsii.invoke(self, "putOauthRequest", [value]))

    @jsii.member(jsii_name="resetAccessToken")
    def reset_access_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessToken", []))

    @jsii.member(jsii_name="resetOauthRequest")
    def reset_oauth_request(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthRequest", []))

    @builtins.property
    @jsii.member(jsii_name="oauthRequest")
    def oauth_request(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequestOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequestOutputReference, jsii.get(self, "oauthRequest"))

    @builtins.property
    @jsii.member(jsii_name="accessTokenInput")
    def access_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretInput")
    def client_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthRequestInput")
    def oauth_request_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequest]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequest], jsii.get(self, "oauthRequestInput"))

    @builtins.property
    @jsii.member(jsii_name="accessToken")
    def access_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessToken"))

    @access_token.setter
    def access_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1358939f075cf7a7dfe1f97fbc56c0cd6ae4006be321c88b0df2d2f8694cf058)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessToken", value)

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6bdf27f9c9f4fdc489279e195fc55636003b57a7021966e1c7f904e04ef2edfd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b56d1b91c0a7394131d2988b4e9554ae6b86110fa933968cb3510b00e2548f9b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketo]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketo],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__380646869b6151c91444e4b3aea656ea8e9ec863a8068e5a4947bd47d58027d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__de2b931eae7011d8628c604f26e2dfefb5f3d4df7e4d0e42d8ed8c07041c8efc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAmplitude")
    def put_amplitude(self, *, api_key: builtins.str, secret_key: builtins.str) -> None:
        '''
        :param api_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#api_key AppflowConnectorProfile#api_key}.
        :param secret_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#secret_key AppflowConnectorProfile#secret_key}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitude(
            api_key=api_key, secret_key=secret_key
        )

        return typing.cast(None, jsii.invoke(self, "putAmplitude", [value]))

    @jsii.member(jsii_name="putCustomConnector")
    def put_custom_connector(
        self,
        *,
        authentication_type: builtins.str,
        api_key: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKey, typing.Dict[builtins.str, typing.Any]]] = None,
        basic: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasic, typing.Dict[builtins.str, typing.Any]]] = None,
        custom: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustom, typing.Dict[builtins.str, typing.Any]]] = None,
        oauth2: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param authentication_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#authentication_type AppflowConnectorProfile#authentication_type}.
        :param api_key: api_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#api_key AppflowConnectorProfile#api_key}
        :param basic: basic block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#basic AppflowConnectorProfile#basic}
        :param custom: custom block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#custom AppflowConnectorProfile#custom}
        :param oauth2: oauth2 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth2 AppflowConnectorProfile#oauth2}
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnector(
            authentication_type=authentication_type,
            api_key=api_key,
            basic=basic,
            custom=custom,
            oauth2=oauth2,
        )

        return typing.cast(None, jsii.invoke(self, "putCustomConnector", [value]))

    @jsii.member(jsii_name="putDatadog")
    def put_datadog(
        self,
        *,
        api_key: builtins.str,
        application_key: builtins.str,
    ) -> None:
        '''
        :param api_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#api_key AppflowConnectorProfile#api_key}.
        :param application_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#application_key AppflowConnectorProfile#application_key}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadog(
            api_key=api_key, application_key=application_key
        )

        return typing.cast(None, jsii.invoke(self, "putDatadog", [value]))

    @jsii.member(jsii_name="putDynatrace")
    def put_dynatrace(self, *, api_token: builtins.str) -> None:
        '''
        :param api_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#api_token AppflowConnectorProfile#api_token}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatrace(
            api_token=api_token
        )

        return typing.cast(None, jsii.invoke(self, "putDynatrace", [value]))

    @jsii.member(jsii_name="putGoogleAnalytics")
    def put_google_analytics(
        self,
        *,
        client_id: builtins.str,
        client_secret: builtins.str,
        access_token: typing.Optional[builtins.str] = None,
        oauth_request: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequest, typing.Dict[builtins.str, typing.Any]]] = None,
        refresh_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_id AppflowConnectorProfile#client_id}.
        :param client_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_secret AppflowConnectorProfile#client_secret}.
        :param access_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_token AppflowConnectorProfile#access_token}.
        :param oauth_request: oauth_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_request AppflowConnectorProfile#oauth_request}
        :param refresh_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#refresh_token AppflowConnectorProfile#refresh_token}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalytics(
            client_id=client_id,
            client_secret=client_secret,
            access_token=access_token,
            oauth_request=oauth_request,
            refresh_token=refresh_token,
        )

        return typing.cast(None, jsii.invoke(self, "putGoogleAnalytics", [value]))

    @jsii.member(jsii_name="putHoneycode")
    def put_honeycode(
        self,
        *,
        access_token: typing.Optional[builtins.str] = None,
        oauth_request: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequest, typing.Dict[builtins.str, typing.Any]]] = None,
        refresh_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_token AppflowConnectorProfile#access_token}.
        :param oauth_request: oauth_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_request AppflowConnectorProfile#oauth_request}
        :param refresh_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#refresh_token AppflowConnectorProfile#refresh_token}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycode(
            access_token=access_token,
            oauth_request=oauth_request,
            refresh_token=refresh_token,
        )

        return typing.cast(None, jsii.invoke(self, "putHoneycode", [value]))

    @jsii.member(jsii_name="putInforNexus")
    def put_infor_nexus(
        self,
        *,
        access_key_id: builtins.str,
        datakey: builtins.str,
        secret_access_key: builtins.str,
        user_id: builtins.str,
    ) -> None:
        '''
        :param access_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_key_id AppflowConnectorProfile#access_key_id}.
        :param datakey: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#datakey AppflowConnectorProfile#datakey}.
        :param secret_access_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#secret_access_key AppflowConnectorProfile#secret_access_key}.
        :param user_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#user_id AppflowConnectorProfile#user_id}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexus(
            access_key_id=access_key_id,
            datakey=datakey,
            secret_access_key=secret_access_key,
            user_id=user_id,
        )

        return typing.cast(None, jsii.invoke(self, "putInforNexus", [value]))

    @jsii.member(jsii_name="putMarketo")
    def put_marketo(
        self,
        *,
        client_id: builtins.str,
        client_secret: builtins.str,
        access_token: typing.Optional[builtins.str] = None,
        oauth_request: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequest, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_id AppflowConnectorProfile#client_id}.
        :param client_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_secret AppflowConnectorProfile#client_secret}.
        :param access_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_token AppflowConnectorProfile#access_token}.
        :param oauth_request: oauth_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_request AppflowConnectorProfile#oauth_request}
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketo(
            client_id=client_id,
            client_secret=client_secret,
            access_token=access_token,
            oauth_request=oauth_request,
        )

        return typing.cast(None, jsii.invoke(self, "putMarketo", [value]))

    @jsii.member(jsii_name="putRedshift")
    def put_redshift(self, *, password: builtins.str, username: builtins.str) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#password AppflowConnectorProfile#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#username AppflowConnectorProfile#username}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshift(
            password=password, username=username
        )

        return typing.cast(None, jsii.invoke(self, "putRedshift", [value]))

    @jsii.member(jsii_name="putSalesforce")
    def put_salesforce(
        self,
        *,
        access_token: typing.Optional[builtins.str] = None,
        client_credentials_arn: typing.Optional[builtins.str] = None,
        oauth_request: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequest", typing.Dict[builtins.str, typing.Any]]] = None,
        refresh_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_token AppflowConnectorProfile#access_token}.
        :param client_credentials_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_credentials_arn AppflowConnectorProfile#client_credentials_arn}.
        :param oauth_request: oauth_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_request AppflowConnectorProfile#oauth_request}
        :param refresh_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#refresh_token AppflowConnectorProfile#refresh_token}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforce(
            access_token=access_token,
            client_credentials_arn=client_credentials_arn,
            oauth_request=oauth_request,
            refresh_token=refresh_token,
        )

        return typing.cast(None, jsii.invoke(self, "putSalesforce", [value]))

    @jsii.member(jsii_name="putSapoData")
    def put_sapo_data(
        self,
        *,
        basic_auth_credentials: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentials", typing.Dict[builtins.str, typing.Any]]] = None,
        oauth_credentials: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentials", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param basic_auth_credentials: basic_auth_credentials block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#basic_auth_credentials AppflowConnectorProfile#basic_auth_credentials}
        :param oauth_credentials: oauth_credentials block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_credentials AppflowConnectorProfile#oauth_credentials}
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoData(
            basic_auth_credentials=basic_auth_credentials,
            oauth_credentials=oauth_credentials,
        )

        return typing.cast(None, jsii.invoke(self, "putSapoData", [value]))

    @jsii.member(jsii_name="putServiceNow")
    def put_service_now(
        self,
        *,
        password: builtins.str,
        username: builtins.str,
    ) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#password AppflowConnectorProfile#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#username AppflowConnectorProfile#username}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNow(
            password=password, username=username
        )

        return typing.cast(None, jsii.invoke(self, "putServiceNow", [value]))

    @jsii.member(jsii_name="putSingular")
    def put_singular(self, *, api_key: builtins.str) -> None:
        '''
        :param api_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#api_key AppflowConnectorProfile#api_key}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingular(
            api_key=api_key
        )

        return typing.cast(None, jsii.invoke(self, "putSingular", [value]))

    @jsii.member(jsii_name="putSlack")
    def put_slack(
        self,
        *,
        client_id: builtins.str,
        client_secret: builtins.str,
        access_token: typing.Optional[builtins.str] = None,
        oauth_request: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequest", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_id AppflowConnectorProfile#client_id}.
        :param client_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_secret AppflowConnectorProfile#client_secret}.
        :param access_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_token AppflowConnectorProfile#access_token}.
        :param oauth_request: oauth_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_request AppflowConnectorProfile#oauth_request}
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlack(
            client_id=client_id,
            client_secret=client_secret,
            access_token=access_token,
            oauth_request=oauth_request,
        )

        return typing.cast(None, jsii.invoke(self, "putSlack", [value]))

    @jsii.member(jsii_name="putSnowflake")
    def put_snowflake(self, *, password: builtins.str, username: builtins.str) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#password AppflowConnectorProfile#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#username AppflowConnectorProfile#username}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflake(
            password=password, username=username
        )

        return typing.cast(None, jsii.invoke(self, "putSnowflake", [value]))

    @jsii.member(jsii_name="putTrendmicro")
    def put_trendmicro(self, *, api_secret_key: builtins.str) -> None:
        '''
        :param api_secret_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#api_secret_key AppflowConnectorProfile#api_secret_key}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicro(
            api_secret_key=api_secret_key
        )

        return typing.cast(None, jsii.invoke(self, "putTrendmicro", [value]))

    @jsii.member(jsii_name="putVeeva")
    def put_veeva(self, *, password: builtins.str, username: builtins.str) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#password AppflowConnectorProfile#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#username AppflowConnectorProfile#username}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeeva(
            password=password, username=username
        )

        return typing.cast(None, jsii.invoke(self, "putVeeva", [value]))

    @jsii.member(jsii_name="putZendesk")
    def put_zendesk(
        self,
        *,
        client_id: builtins.str,
        client_secret: builtins.str,
        access_token: typing.Optional[builtins.str] = None,
        oauth_request: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequest", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_id AppflowConnectorProfile#client_id}.
        :param client_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_secret AppflowConnectorProfile#client_secret}.
        :param access_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_token AppflowConnectorProfile#access_token}.
        :param oauth_request: oauth_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_request AppflowConnectorProfile#oauth_request}
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendesk(
            client_id=client_id,
            client_secret=client_secret,
            access_token=access_token,
            oauth_request=oauth_request,
        )

        return typing.cast(None, jsii.invoke(self, "putZendesk", [value]))

    @jsii.member(jsii_name="resetAmplitude")
    def reset_amplitude(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAmplitude", []))

    @jsii.member(jsii_name="resetCustomConnector")
    def reset_custom_connector(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomConnector", []))

    @jsii.member(jsii_name="resetDatadog")
    def reset_datadog(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatadog", []))

    @jsii.member(jsii_name="resetDynatrace")
    def reset_dynatrace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDynatrace", []))

    @jsii.member(jsii_name="resetGoogleAnalytics")
    def reset_google_analytics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGoogleAnalytics", []))

    @jsii.member(jsii_name="resetHoneycode")
    def reset_honeycode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHoneycode", []))

    @jsii.member(jsii_name="resetInforNexus")
    def reset_infor_nexus(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInforNexus", []))

    @jsii.member(jsii_name="resetMarketo")
    def reset_marketo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMarketo", []))

    @jsii.member(jsii_name="resetRedshift")
    def reset_redshift(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedshift", []))

    @jsii.member(jsii_name="resetSalesforce")
    def reset_salesforce(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSalesforce", []))

    @jsii.member(jsii_name="resetSapoData")
    def reset_sapo_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSapoData", []))

    @jsii.member(jsii_name="resetServiceNow")
    def reset_service_now(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceNow", []))

    @jsii.member(jsii_name="resetSingular")
    def reset_singular(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSingular", []))

    @jsii.member(jsii_name="resetSlack")
    def reset_slack(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSlack", []))

    @jsii.member(jsii_name="resetSnowflake")
    def reset_snowflake(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSnowflake", []))

    @jsii.member(jsii_name="resetTrendmicro")
    def reset_trendmicro(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrendmicro", []))

    @jsii.member(jsii_name="resetVeeva")
    def reset_veeva(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVeeva", []))

    @jsii.member(jsii_name="resetZendesk")
    def reset_zendesk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZendesk", []))

    @builtins.property
    @jsii.member(jsii_name="amplitude")
    def amplitude(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitudeOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitudeOutputReference, jsii.get(self, "amplitude"))

    @builtins.property
    @jsii.member(jsii_name="customConnector")
    def custom_connector(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOutputReference, jsii.get(self, "customConnector"))

    @builtins.property
    @jsii.member(jsii_name="datadog")
    def datadog(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadogOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadogOutputReference, jsii.get(self, "datadog"))

    @builtins.property
    @jsii.member(jsii_name="dynatrace")
    def dynatrace(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatraceOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatraceOutputReference, jsii.get(self, "dynatrace"))

    @builtins.property
    @jsii.member(jsii_name="googleAnalytics")
    def google_analytics(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOutputReference, jsii.get(self, "googleAnalytics"))

    @builtins.property
    @jsii.member(jsii_name="honeycode")
    def honeycode(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOutputReference, jsii.get(self, "honeycode"))

    @builtins.property
    @jsii.member(jsii_name="inforNexus")
    def infor_nexus(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexusOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexusOutputReference, jsii.get(self, "inforNexus"))

    @builtins.property
    @jsii.member(jsii_name="marketo")
    def marketo(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOutputReference, jsii.get(self, "marketo"))

    @builtins.property
    @jsii.member(jsii_name="redshift")
    def redshift(
        self,
    ) -> "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshiftOutputReference":
        return typing.cast("AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshiftOutputReference", jsii.get(self, "redshift"))

    @builtins.property
    @jsii.member(jsii_name="salesforce")
    def salesforce(
        self,
    ) -> "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOutputReference":
        return typing.cast("AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOutputReference", jsii.get(self, "salesforce"))

    @builtins.property
    @jsii.member(jsii_name="sapoData")
    def sapo_data(
        self,
    ) -> "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOutputReference":
        return typing.cast("AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOutputReference", jsii.get(self, "sapoData"))

    @builtins.property
    @jsii.member(jsii_name="serviceNow")
    def service_now(
        self,
    ) -> "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNowOutputReference":
        return typing.cast("AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNowOutputReference", jsii.get(self, "serviceNow"))

    @builtins.property
    @jsii.member(jsii_name="singular")
    def singular(
        self,
    ) -> "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingularOutputReference":
        return typing.cast("AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingularOutputReference", jsii.get(self, "singular"))

    @builtins.property
    @jsii.member(jsii_name="slack")
    def slack(
        self,
    ) -> "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOutputReference":
        return typing.cast("AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOutputReference", jsii.get(self, "slack"))

    @builtins.property
    @jsii.member(jsii_name="snowflake")
    def snowflake(
        self,
    ) -> "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflakeOutputReference":
        return typing.cast("AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflakeOutputReference", jsii.get(self, "snowflake"))

    @builtins.property
    @jsii.member(jsii_name="trendmicro")
    def trendmicro(
        self,
    ) -> "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicroOutputReference":
        return typing.cast("AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicroOutputReference", jsii.get(self, "trendmicro"))

    @builtins.property
    @jsii.member(jsii_name="veeva")
    def veeva(
        self,
    ) -> "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeevaOutputReference":
        return typing.cast("AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeevaOutputReference", jsii.get(self, "veeva"))

    @builtins.property
    @jsii.member(jsii_name="zendesk")
    def zendesk(
        self,
    ) -> "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOutputReference":
        return typing.cast("AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOutputReference", jsii.get(self, "zendesk"))

    @builtins.property
    @jsii.member(jsii_name="amplitudeInput")
    def amplitude_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitude]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitude], jsii.get(self, "amplitudeInput"))

    @builtins.property
    @jsii.member(jsii_name="customConnectorInput")
    def custom_connector_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnector]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnector], jsii.get(self, "customConnectorInput"))

    @builtins.property
    @jsii.member(jsii_name="datadogInput")
    def datadog_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadog]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadog], jsii.get(self, "datadogInput"))

    @builtins.property
    @jsii.member(jsii_name="dynatraceInput")
    def dynatrace_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatrace]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatrace], jsii.get(self, "dynatraceInput"))

    @builtins.property
    @jsii.member(jsii_name="googleAnalyticsInput")
    def google_analytics_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalytics]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalytics], jsii.get(self, "googleAnalyticsInput"))

    @builtins.property
    @jsii.member(jsii_name="honeycodeInput")
    def honeycode_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycode]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycode], jsii.get(self, "honeycodeInput"))

    @builtins.property
    @jsii.member(jsii_name="inforNexusInput")
    def infor_nexus_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexus]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexus], jsii.get(self, "inforNexusInput"))

    @builtins.property
    @jsii.member(jsii_name="marketoInput")
    def marketo_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketo]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketo], jsii.get(self, "marketoInput"))

    @builtins.property
    @jsii.member(jsii_name="redshiftInput")
    def redshift_input(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshift"]:
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshift"], jsii.get(self, "redshiftInput"))

    @builtins.property
    @jsii.member(jsii_name="salesforceInput")
    def salesforce_input(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforce"]:
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforce"], jsii.get(self, "salesforceInput"))

    @builtins.property
    @jsii.member(jsii_name="sapoDataInput")
    def sapo_data_input(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoData"]:
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoData"], jsii.get(self, "sapoDataInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceNowInput")
    def service_now_input(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNow"]:
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNow"], jsii.get(self, "serviceNowInput"))

    @builtins.property
    @jsii.member(jsii_name="singularInput")
    def singular_input(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingular"]:
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingular"], jsii.get(self, "singularInput"))

    @builtins.property
    @jsii.member(jsii_name="slackInput")
    def slack_input(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlack"]:
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlack"], jsii.get(self, "slackInput"))

    @builtins.property
    @jsii.member(jsii_name="snowflakeInput")
    def snowflake_input(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflake"]:
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflake"], jsii.get(self, "snowflakeInput"))

    @builtins.property
    @jsii.member(jsii_name="trendmicroInput")
    def trendmicro_input(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicro"]:
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicro"], jsii.get(self, "trendmicroInput"))

    @builtins.property
    @jsii.member(jsii_name="veevaInput")
    def veeva_input(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeeva"]:
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeeva"], jsii.get(self, "veevaInput"))

    @builtins.property
    @jsii.member(jsii_name="zendeskInput")
    def zendesk_input(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendesk"]:
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendesk"], jsii.get(self, "zendeskInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentials]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentials], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentials],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e5e90b5dc1a66c46600bbb752c1137309661a2e984fb8abc628a7708b63965e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshift",
    jsii_struct_bases=[],
    name_mapping={"password": "password", "username": "username"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshift:
    def __init__(self, *, password: builtins.str, username: builtins.str) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#password AppflowConnectorProfile#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#username AppflowConnectorProfile#username}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbe7d541f38235c6d4c8cc7a563b5d773c35d092954fb0a131dde42517814690)
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "password": password,
            "username": username,
        }

    @builtins.property
    def password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#password AppflowConnectorProfile#password}.'''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#username AppflowConnectorProfile#username}.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshift(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshiftOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshiftOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8cd13f73147d5167d4bdd46c9d206b817951fb2be8b357cc2c8d52ade8bb0009)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2eff0027297184fcd9d41a8739ab90da0e1d09aa344d5d07870359e0deda86eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc49328371a8f30bc7b0f81266b44c7cc03131995c6676873496e982c07cb92d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshift]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshift], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshift],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d96063e3ff1e33b618948a3fd9f0bf54b19e07dfb8af124411f0bbddb8e3c86)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforce",
    jsii_struct_bases=[],
    name_mapping={
        "access_token": "accessToken",
        "client_credentials_arn": "clientCredentialsArn",
        "oauth_request": "oauthRequest",
        "refresh_token": "refreshToken",
    },
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforce:
    def __init__(
        self,
        *,
        access_token: typing.Optional[builtins.str] = None,
        client_credentials_arn: typing.Optional[builtins.str] = None,
        oauth_request: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequest", typing.Dict[builtins.str, typing.Any]]] = None,
        refresh_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_token AppflowConnectorProfile#access_token}.
        :param client_credentials_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_credentials_arn AppflowConnectorProfile#client_credentials_arn}.
        :param oauth_request: oauth_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_request AppflowConnectorProfile#oauth_request}
        :param refresh_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#refresh_token AppflowConnectorProfile#refresh_token}.
        '''
        if isinstance(oauth_request, dict):
            oauth_request = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequest(**oauth_request)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84145676624144ce4ec85ca32d9b50447170aeda7a0493ee7e2cf4b4a025d99e)
            check_type(argname="argument access_token", value=access_token, expected_type=type_hints["access_token"])
            check_type(argname="argument client_credentials_arn", value=client_credentials_arn, expected_type=type_hints["client_credentials_arn"])
            check_type(argname="argument oauth_request", value=oauth_request, expected_type=type_hints["oauth_request"])
            check_type(argname="argument refresh_token", value=refresh_token, expected_type=type_hints["refresh_token"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if access_token is not None:
            self._values["access_token"] = access_token
        if client_credentials_arn is not None:
            self._values["client_credentials_arn"] = client_credentials_arn
        if oauth_request is not None:
            self._values["oauth_request"] = oauth_request
        if refresh_token is not None:
            self._values["refresh_token"] = refresh_token

    @builtins.property
    def access_token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_token AppflowConnectorProfile#access_token}.'''
        result = self._values.get("access_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_credentials_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_credentials_arn AppflowConnectorProfile#client_credentials_arn}.'''
        result = self._values.get("client_credentials_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_request(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequest"]:
        '''oauth_request block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_request AppflowConnectorProfile#oauth_request}
        '''
        result = self._values.get("oauth_request")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequest"], result)

    @builtins.property
    def refresh_token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#refresh_token AppflowConnectorProfile#refresh_token}.'''
        result = self._values.get("refresh_token")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforce(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequest",
    jsii_struct_bases=[],
    name_mapping={"auth_code": "authCode", "redirect_uri": "redirectUri"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequest:
    def __init__(
        self,
        *,
        auth_code: typing.Optional[builtins.str] = None,
        redirect_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code AppflowConnectorProfile#auth_code}.
        :param redirect_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redirect_uri AppflowConnectorProfile#redirect_uri}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__365dc022282d1548bbf989b43b8cdad26138f7d81a705e487c49a9234235bcf3)
            check_type(argname="argument auth_code", value=auth_code, expected_type=type_hints["auth_code"])
            check_type(argname="argument redirect_uri", value=redirect_uri, expected_type=type_hints["redirect_uri"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if auth_code is not None:
            self._values["auth_code"] = auth_code
        if redirect_uri is not None:
            self._values["redirect_uri"] = redirect_uri

    @builtins.property
    def auth_code(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code AppflowConnectorProfile#auth_code}.'''
        result = self._values.get("auth_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def redirect_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redirect_uri AppflowConnectorProfile#redirect_uri}.'''
        result = self._values.get("redirect_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequestOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequestOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__155f16ad4526aea57e46fed2efcbc12395f0806d08965231be521424a5ca6a13)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAuthCode")
    def reset_auth_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthCode", []))

    @jsii.member(jsii_name="resetRedirectUri")
    def reset_redirect_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedirectUri", []))

    @builtins.property
    @jsii.member(jsii_name="authCodeInput")
    def auth_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectUriInput")
    def redirect_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "redirectUriInput"))

    @builtins.property
    @jsii.member(jsii_name="authCode")
    def auth_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authCode"))

    @auth_code.setter
    def auth_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab8fdd861d28804dd63aa9ad3828d563409f6abe2e2447f17a843b368a343d2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authCode", value)

    @builtins.property
    @jsii.member(jsii_name="redirectUri")
    def redirect_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redirectUri"))

    @redirect_uri.setter
    def redirect_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff9622cc5ecd7052fe94dd204c7ea550091056176a556fde910d8fac2464dde7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redirectUri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequest]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequest], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequest],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1e27239514e40b088dbcb2ea5a11683379b6c26b4943bcb969359ed8e08dcb6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0a15ea9480e99a2bc4c5931197f5313ed280ecf51a148a1be2f8c9413adbe556)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putOauthRequest")
    def put_oauth_request(
        self,
        *,
        auth_code: typing.Optional[builtins.str] = None,
        redirect_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code AppflowConnectorProfile#auth_code}.
        :param redirect_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redirect_uri AppflowConnectorProfile#redirect_uri}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequest(
            auth_code=auth_code, redirect_uri=redirect_uri
        )

        return typing.cast(None, jsii.invoke(self, "putOauthRequest", [value]))

    @jsii.member(jsii_name="resetAccessToken")
    def reset_access_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessToken", []))

    @jsii.member(jsii_name="resetClientCredentialsArn")
    def reset_client_credentials_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientCredentialsArn", []))

    @jsii.member(jsii_name="resetOauthRequest")
    def reset_oauth_request(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthRequest", []))

    @jsii.member(jsii_name="resetRefreshToken")
    def reset_refresh_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRefreshToken", []))

    @builtins.property
    @jsii.member(jsii_name="oauthRequest")
    def oauth_request(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequestOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequestOutputReference, jsii.get(self, "oauthRequest"))

    @builtins.property
    @jsii.member(jsii_name="accessTokenInput")
    def access_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="clientCredentialsArnInput")
    def client_credentials_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientCredentialsArnInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthRequestInput")
    def oauth_request_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequest]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequest], jsii.get(self, "oauthRequestInput"))

    @builtins.property
    @jsii.member(jsii_name="refreshTokenInput")
    def refresh_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "refreshTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="accessToken")
    def access_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessToken"))

    @access_token.setter
    def access_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66a56b8f047f79d6007624fb56ba9612f3a17a0a2762adbbb03516f1e8d460f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessToken", value)

    @builtins.property
    @jsii.member(jsii_name="clientCredentialsArn")
    def client_credentials_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientCredentialsArn"))

    @client_credentials_arn.setter
    def client_credentials_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__adfb01011493e4fa3ac0eb0a0fc181d7ed9b26ec8495cddf66bd0cc406642641)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientCredentialsArn", value)

    @builtins.property
    @jsii.member(jsii_name="refreshToken")
    def refresh_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "refreshToken"))

    @refresh_token.setter
    def refresh_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2b56a333ba2f3a02b8af8df18b6af946c2e37ba528692fddc83627d31d1ff82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "refreshToken", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforce]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforce], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforce],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24790825786a4a20eef3f4bd40b46b095b985cdbacf8f2e28d063f565af8869f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoData",
    jsii_struct_bases=[],
    name_mapping={
        "basic_auth_credentials": "basicAuthCredentials",
        "oauth_credentials": "oauthCredentials",
    },
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoData:
    def __init__(
        self,
        *,
        basic_auth_credentials: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentials", typing.Dict[builtins.str, typing.Any]]] = None,
        oauth_credentials: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentials", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param basic_auth_credentials: basic_auth_credentials block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#basic_auth_credentials AppflowConnectorProfile#basic_auth_credentials}
        :param oauth_credentials: oauth_credentials block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_credentials AppflowConnectorProfile#oauth_credentials}
        '''
        if isinstance(basic_auth_credentials, dict):
            basic_auth_credentials = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentials(**basic_auth_credentials)
        if isinstance(oauth_credentials, dict):
            oauth_credentials = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentials(**oauth_credentials)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3da20e636399312a8cd3c5f0c1fda6ca69b866c41a53dd76fcb64e03fc0ec7a5)
            check_type(argname="argument basic_auth_credentials", value=basic_auth_credentials, expected_type=type_hints["basic_auth_credentials"])
            check_type(argname="argument oauth_credentials", value=oauth_credentials, expected_type=type_hints["oauth_credentials"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if basic_auth_credentials is not None:
            self._values["basic_auth_credentials"] = basic_auth_credentials
        if oauth_credentials is not None:
            self._values["oauth_credentials"] = oauth_credentials

    @builtins.property
    def basic_auth_credentials(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentials"]:
        '''basic_auth_credentials block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#basic_auth_credentials AppflowConnectorProfile#basic_auth_credentials}
        '''
        result = self._values.get("basic_auth_credentials")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentials"], result)

    @builtins.property
    def oauth_credentials(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentials"]:
        '''oauth_credentials block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_credentials AppflowConnectorProfile#oauth_credentials}
        '''
        result = self._values.get("oauth_credentials")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentials"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoData(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentials",
    jsii_struct_bases=[],
    name_mapping={"password": "password", "username": "username"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentials:
    def __init__(self, *, password: builtins.str, username: builtins.str) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#password AppflowConnectorProfile#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#username AppflowConnectorProfile#username}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c8046c6ebf75720c30113c2717257b68dd9635915fc686b2257f414b8fd587d)
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "password": password,
            "username": username,
        }

    @builtins.property
    def password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#password AppflowConnectorProfile#password}.'''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#username AppflowConnectorProfile#username}.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentials(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentialsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentialsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ef1e10c5270dbfe808da8dcef1cadef57595774bc28629d6491f65958acb5ff1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f0601c6444b29c1d33e6762afbab5fe0fe7f5e6cf250e309d364a08ec8f83f27)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d19c1e3af0506e135fbe702a313870f21ae6821f14ac4742aa9d5c0f672ec1f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentials]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentials], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentials],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e12ff8604dfaba8bed8198410efb4302457ec31444664490c3af3ed2f0317089)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentials",
    jsii_struct_bases=[],
    name_mapping={
        "client_id": "clientId",
        "client_secret": "clientSecret",
        "access_token": "accessToken",
        "oauth_request": "oauthRequest",
        "refresh_token": "refreshToken",
    },
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentials:
    def __init__(
        self,
        *,
        client_id: builtins.str,
        client_secret: builtins.str,
        access_token: typing.Optional[builtins.str] = None,
        oauth_request: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequest", typing.Dict[builtins.str, typing.Any]]] = None,
        refresh_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_id AppflowConnectorProfile#client_id}.
        :param client_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_secret AppflowConnectorProfile#client_secret}.
        :param access_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_token AppflowConnectorProfile#access_token}.
        :param oauth_request: oauth_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_request AppflowConnectorProfile#oauth_request}
        :param refresh_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#refresh_token AppflowConnectorProfile#refresh_token}.
        '''
        if isinstance(oauth_request, dict):
            oauth_request = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequest(**oauth_request)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ccda68882ff6b953e86a32e097d3ac0c4d4b9fe1d7726df55384da479b4984f)
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
            check_type(argname="argument access_token", value=access_token, expected_type=type_hints["access_token"])
            check_type(argname="argument oauth_request", value=oauth_request, expected_type=type_hints["oauth_request"])
            check_type(argname="argument refresh_token", value=refresh_token, expected_type=type_hints["refresh_token"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "client_id": client_id,
            "client_secret": client_secret,
        }
        if access_token is not None:
            self._values["access_token"] = access_token
        if oauth_request is not None:
            self._values["oauth_request"] = oauth_request
        if refresh_token is not None:
            self._values["refresh_token"] = refresh_token

    @builtins.property
    def client_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_id AppflowConnectorProfile#client_id}.'''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_secret AppflowConnectorProfile#client_secret}.'''
        result = self._values.get("client_secret")
        assert result is not None, "Required property 'client_secret' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_token AppflowConnectorProfile#access_token}.'''
        result = self._values.get("access_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_request(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequest"]:
        '''oauth_request block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_request AppflowConnectorProfile#oauth_request}
        '''
        result = self._values.get("oauth_request")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequest"], result)

    @builtins.property
    def refresh_token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#refresh_token AppflowConnectorProfile#refresh_token}.'''
        result = self._values.get("refresh_token")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentials(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequest",
    jsii_struct_bases=[],
    name_mapping={"auth_code": "authCode", "redirect_uri": "redirectUri"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequest:
    def __init__(
        self,
        *,
        auth_code: typing.Optional[builtins.str] = None,
        redirect_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code AppflowConnectorProfile#auth_code}.
        :param redirect_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redirect_uri AppflowConnectorProfile#redirect_uri}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e8ff2b6067a9d67dfce3cf5d9e490e92dbc5ed5b57a50e0cd3e2733895c9c8d)
            check_type(argname="argument auth_code", value=auth_code, expected_type=type_hints["auth_code"])
            check_type(argname="argument redirect_uri", value=redirect_uri, expected_type=type_hints["redirect_uri"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if auth_code is not None:
            self._values["auth_code"] = auth_code
        if redirect_uri is not None:
            self._values["redirect_uri"] = redirect_uri

    @builtins.property
    def auth_code(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code AppflowConnectorProfile#auth_code}.'''
        result = self._values.get("auth_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def redirect_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redirect_uri AppflowConnectorProfile#redirect_uri}.'''
        result = self._values.get("redirect_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequestOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequestOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5e8deedd82cf2d078fdf88f7397e94e73bdd4a4f465bd63b8f9b668f73a23025)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAuthCode")
    def reset_auth_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthCode", []))

    @jsii.member(jsii_name="resetRedirectUri")
    def reset_redirect_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedirectUri", []))

    @builtins.property
    @jsii.member(jsii_name="authCodeInput")
    def auth_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectUriInput")
    def redirect_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "redirectUriInput"))

    @builtins.property
    @jsii.member(jsii_name="authCode")
    def auth_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authCode"))

    @auth_code.setter
    def auth_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a70707b1ece55dbac16d5dccae190efbfb65ea872c5c7b881f81797ff6ea504)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authCode", value)

    @builtins.property
    @jsii.member(jsii_name="redirectUri")
    def redirect_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redirectUri"))

    @redirect_uri.setter
    def redirect_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3f776a2c2a3796b9677a6d4454746989600b545009130c033a6fc3937ddebca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redirectUri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequest]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequest], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequest],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7cf7d225c7f7199c6d9b87c63aeec0b49871181495fdef28176d9f9222b1dd1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a4c29f53c7cae77e8d9f5e4b905336bc3c6757c081e941538f07533fe114ee12)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putOauthRequest")
    def put_oauth_request(
        self,
        *,
        auth_code: typing.Optional[builtins.str] = None,
        redirect_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code AppflowConnectorProfile#auth_code}.
        :param redirect_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redirect_uri AppflowConnectorProfile#redirect_uri}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequest(
            auth_code=auth_code, redirect_uri=redirect_uri
        )

        return typing.cast(None, jsii.invoke(self, "putOauthRequest", [value]))

    @jsii.member(jsii_name="resetAccessToken")
    def reset_access_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessToken", []))

    @jsii.member(jsii_name="resetOauthRequest")
    def reset_oauth_request(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthRequest", []))

    @jsii.member(jsii_name="resetRefreshToken")
    def reset_refresh_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRefreshToken", []))

    @builtins.property
    @jsii.member(jsii_name="oauthRequest")
    def oauth_request(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequestOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequestOutputReference, jsii.get(self, "oauthRequest"))

    @builtins.property
    @jsii.member(jsii_name="accessTokenInput")
    def access_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretInput")
    def client_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthRequestInput")
    def oauth_request_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequest]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequest], jsii.get(self, "oauthRequestInput"))

    @builtins.property
    @jsii.member(jsii_name="refreshTokenInput")
    def refresh_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "refreshTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="accessToken")
    def access_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessToken"))

    @access_token.setter
    def access_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ecd2c480c0e84594327772ba200b77a15bf7f34dfa0e4dd829592d833f1608f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessToken", value)

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d16bb221c7d9a72b0b8505c1d92a3b9d8d305bb90d745f58f94d75d1275c23d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__586edceb6570a5243cc668f388e2a1aea38d10bcdaedb0a2981b0db208435c7a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="refreshToken")
    def refresh_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "refreshToken"))

    @refresh_token.setter
    def refresh_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84b4f07d02c44cbc309e3b3a118c5139984a19341784e674bf970123b6df4569)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "refreshToken", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentials]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentials], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentials],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bd3c8f38f15334b50c6dee2572d629719a97c5cdf0fd5b327e906ce9d59ad97)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c74a13fd85208f92cf7263d11ec98af16a3b9f43fa08f7cf74c79a69d405668e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putBasicAuthCredentials")
    def put_basic_auth_credentials(
        self,
        *,
        password: builtins.str,
        username: builtins.str,
    ) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#password AppflowConnectorProfile#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#username AppflowConnectorProfile#username}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentials(
            password=password, username=username
        )

        return typing.cast(None, jsii.invoke(self, "putBasicAuthCredentials", [value]))

    @jsii.member(jsii_name="putOauthCredentials")
    def put_oauth_credentials(
        self,
        *,
        client_id: builtins.str,
        client_secret: builtins.str,
        access_token: typing.Optional[builtins.str] = None,
        oauth_request: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequest, typing.Dict[builtins.str, typing.Any]]] = None,
        refresh_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_id AppflowConnectorProfile#client_id}.
        :param client_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_secret AppflowConnectorProfile#client_secret}.
        :param access_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_token AppflowConnectorProfile#access_token}.
        :param oauth_request: oauth_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_request AppflowConnectorProfile#oauth_request}
        :param refresh_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#refresh_token AppflowConnectorProfile#refresh_token}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentials(
            client_id=client_id,
            client_secret=client_secret,
            access_token=access_token,
            oauth_request=oauth_request,
            refresh_token=refresh_token,
        )

        return typing.cast(None, jsii.invoke(self, "putOauthCredentials", [value]))

    @jsii.member(jsii_name="resetBasicAuthCredentials")
    def reset_basic_auth_credentials(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBasicAuthCredentials", []))

    @jsii.member(jsii_name="resetOauthCredentials")
    def reset_oauth_credentials(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthCredentials", []))

    @builtins.property
    @jsii.member(jsii_name="basicAuthCredentials")
    def basic_auth_credentials(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentialsOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentialsOutputReference, jsii.get(self, "basicAuthCredentials"))

    @builtins.property
    @jsii.member(jsii_name="oauthCredentials")
    def oauth_credentials(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOutputReference, jsii.get(self, "oauthCredentials"))

    @builtins.property
    @jsii.member(jsii_name="basicAuthCredentialsInput")
    def basic_auth_credentials_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentials]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentials], jsii.get(self, "basicAuthCredentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthCredentialsInput")
    def oauth_credentials_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentials]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentials], jsii.get(self, "oauthCredentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoData]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoData], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoData],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c417d37d0230cbdef357b0a4edb463162169efe8ffa720ad1f882c3348d17d5f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNow",
    jsii_struct_bases=[],
    name_mapping={"password": "password", "username": "username"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNow:
    def __init__(self, *, password: builtins.str, username: builtins.str) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#password AppflowConnectorProfile#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#username AppflowConnectorProfile#username}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8161665b61e4e766698e0733be69186cfa9543d16e10ee91400a002eb44ffa59)
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "password": password,
            "username": username,
        }

    @builtins.property
    def password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#password AppflowConnectorProfile#password}.'''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#username AppflowConnectorProfile#username}.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNow(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNowOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNowOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1048b7d35c229c443f549d9aa842c04e034d0fc79d6f478cbcc36a604cec520b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__eda4d14e1330ba114091c044b478a398e778213b1bb6a4789535104d3970fbaa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9a1c21e1ba9348c0aa231677bc72b9ff5ff240f1f1cc69de49a9b7e2a608e41)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNow]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNow], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNow],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e24edebbfd1bc29125b859d3eef8b6bf2775e9b7d626d54971ae70321043ebb8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingular",
    jsii_struct_bases=[],
    name_mapping={"api_key": "apiKey"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingular:
    def __init__(self, *, api_key: builtins.str) -> None:
        '''
        :param api_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#api_key AppflowConnectorProfile#api_key}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ed9e86581f2c9c1993a5f89d08a358759f6ea1f702a83c167dfe0c05b0e1dcc)
            check_type(argname="argument api_key", value=api_key, expected_type=type_hints["api_key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_key": api_key,
        }

    @builtins.property
    def api_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#api_key AppflowConnectorProfile#api_key}.'''
        result = self._values.get("api_key")
        assert result is not None, "Required property 'api_key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingular(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingularOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingularOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e1ed6e48f850bc1a0438179e429897a82f710e0f57f72aa86b054ec5b750592f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="apiKeyInput")
    def api_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="apiKey")
    def api_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiKey"))

    @api_key.setter
    def api_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__455459e293f59727ac6a524bb17e91793e2eabdb6b99b3f7f6e078d7dbd690a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingular]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingular], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingular],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d735216c0ac159fe783b40617014ba323b47e6d3cdf8b5dfae2ea7e972c8f5c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlack",
    jsii_struct_bases=[],
    name_mapping={
        "client_id": "clientId",
        "client_secret": "clientSecret",
        "access_token": "accessToken",
        "oauth_request": "oauthRequest",
    },
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlack:
    def __init__(
        self,
        *,
        client_id: builtins.str,
        client_secret: builtins.str,
        access_token: typing.Optional[builtins.str] = None,
        oauth_request: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequest", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_id AppflowConnectorProfile#client_id}.
        :param client_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_secret AppflowConnectorProfile#client_secret}.
        :param access_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_token AppflowConnectorProfile#access_token}.
        :param oauth_request: oauth_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_request AppflowConnectorProfile#oauth_request}
        '''
        if isinstance(oauth_request, dict):
            oauth_request = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequest(**oauth_request)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b92a387285c6ac027f11588c488093e438e8045d3f3fde055af5d76d94795aa8)
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
            check_type(argname="argument access_token", value=access_token, expected_type=type_hints["access_token"])
            check_type(argname="argument oauth_request", value=oauth_request, expected_type=type_hints["oauth_request"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "client_id": client_id,
            "client_secret": client_secret,
        }
        if access_token is not None:
            self._values["access_token"] = access_token
        if oauth_request is not None:
            self._values["oauth_request"] = oauth_request

    @builtins.property
    def client_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_id AppflowConnectorProfile#client_id}.'''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_secret AppflowConnectorProfile#client_secret}.'''
        result = self._values.get("client_secret")
        assert result is not None, "Required property 'client_secret' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_token AppflowConnectorProfile#access_token}.'''
        result = self._values.get("access_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_request(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequest"]:
        '''oauth_request block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_request AppflowConnectorProfile#oauth_request}
        '''
        result = self._values.get("oauth_request")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequest"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlack(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequest",
    jsii_struct_bases=[],
    name_mapping={"auth_code": "authCode", "redirect_uri": "redirectUri"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequest:
    def __init__(
        self,
        *,
        auth_code: typing.Optional[builtins.str] = None,
        redirect_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code AppflowConnectorProfile#auth_code}.
        :param redirect_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redirect_uri AppflowConnectorProfile#redirect_uri}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1b2d3f0f783d3c14b2e557626d3438ac1d4a03a8dbecf7d31efa5bbbd5dfc59)
            check_type(argname="argument auth_code", value=auth_code, expected_type=type_hints["auth_code"])
            check_type(argname="argument redirect_uri", value=redirect_uri, expected_type=type_hints["redirect_uri"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if auth_code is not None:
            self._values["auth_code"] = auth_code
        if redirect_uri is not None:
            self._values["redirect_uri"] = redirect_uri

    @builtins.property
    def auth_code(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code AppflowConnectorProfile#auth_code}.'''
        result = self._values.get("auth_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def redirect_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redirect_uri AppflowConnectorProfile#redirect_uri}.'''
        result = self._values.get("redirect_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequestOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequestOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5a5cce45b9a9cda969c3a5531254035f193017bad6919685b04b29a5c5d18912)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAuthCode")
    def reset_auth_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthCode", []))

    @jsii.member(jsii_name="resetRedirectUri")
    def reset_redirect_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedirectUri", []))

    @builtins.property
    @jsii.member(jsii_name="authCodeInput")
    def auth_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectUriInput")
    def redirect_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "redirectUriInput"))

    @builtins.property
    @jsii.member(jsii_name="authCode")
    def auth_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authCode"))

    @auth_code.setter
    def auth_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f4840a4b154a03f27d67b4dbac2fae30e631ff77de44d79e9464d73af6c8266)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authCode", value)

    @builtins.property
    @jsii.member(jsii_name="redirectUri")
    def redirect_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redirectUri"))

    @redirect_uri.setter
    def redirect_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__697122a95f28cb4ee8c39d01d10e696e421d97764c3567d04867ce07a8ff2a35)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redirectUri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequest]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequest], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequest],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ae7aef5f5dcd9be8e4409457b20ccfd95339c6dbde51d29e155cf4710af00de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__57eee686173541dd0da989fb94f2048bb3188e3e7bca89ac21d5a2ad47d6630f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putOauthRequest")
    def put_oauth_request(
        self,
        *,
        auth_code: typing.Optional[builtins.str] = None,
        redirect_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code AppflowConnectorProfile#auth_code}.
        :param redirect_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redirect_uri AppflowConnectorProfile#redirect_uri}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequest(
            auth_code=auth_code, redirect_uri=redirect_uri
        )

        return typing.cast(None, jsii.invoke(self, "putOauthRequest", [value]))

    @jsii.member(jsii_name="resetAccessToken")
    def reset_access_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessToken", []))

    @jsii.member(jsii_name="resetOauthRequest")
    def reset_oauth_request(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthRequest", []))

    @builtins.property
    @jsii.member(jsii_name="oauthRequest")
    def oauth_request(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequestOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequestOutputReference, jsii.get(self, "oauthRequest"))

    @builtins.property
    @jsii.member(jsii_name="accessTokenInput")
    def access_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretInput")
    def client_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthRequestInput")
    def oauth_request_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequest]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequest], jsii.get(self, "oauthRequestInput"))

    @builtins.property
    @jsii.member(jsii_name="accessToken")
    def access_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessToken"))

    @access_token.setter
    def access_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83add6225362b559f57a9baa287f7a87c7417d9663b1798dcdaa9bf4ffcfd27d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessToken", value)

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abd788108ed717984391d57a1c3310e17929610170661abc03dc778c7790e5d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c96fb6cf4092006970d7ffe1f9a6b57838c94e896be72361d0d6ce3835f09b92)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlack]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlack], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlack],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__535c0972747c46a9eba87781bc2c3952c0648e2edceffe8fe6ec29a7ab092dac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflake",
    jsii_struct_bases=[],
    name_mapping={"password": "password", "username": "username"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflake:
    def __init__(self, *, password: builtins.str, username: builtins.str) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#password AppflowConnectorProfile#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#username AppflowConnectorProfile#username}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d5f2a98c83fefb76667b869bac2003a733a0d620fff522b04d45a05e5802cca)
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "password": password,
            "username": username,
        }

    @builtins.property
    def password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#password AppflowConnectorProfile#password}.'''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#username AppflowConnectorProfile#username}.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflake(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflakeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflakeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__39434e59bcef530340accf11db836380ad163710c2511ea135045edeb37ad641)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5ba6c779d09cfacb86abe80f0bf3c569d12d93a44638f0ae89a0ad1b216f7eab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__485ad44a4566e35cb6db17e724e99de719798e5c00a370b1f0e65b86ebee78c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflake]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflake], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflake],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0bf663abd48b10315850db14618fe530b39666be898c8fec90af286f6780bbf5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicro",
    jsii_struct_bases=[],
    name_mapping={"api_secret_key": "apiSecretKey"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicro:
    def __init__(self, *, api_secret_key: builtins.str) -> None:
        '''
        :param api_secret_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#api_secret_key AppflowConnectorProfile#api_secret_key}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7103d2d524ef96829700b9d6a943416d9dcad9e8913ea45675dbdbf7342189e7)
            check_type(argname="argument api_secret_key", value=api_secret_key, expected_type=type_hints["api_secret_key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_secret_key": api_secret_key,
        }

    @builtins.property
    def api_secret_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#api_secret_key AppflowConnectorProfile#api_secret_key}.'''
        result = self._values.get("api_secret_key")
        assert result is not None, "Required property 'api_secret_key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicro(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicroOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicroOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ef86b35e4616a43670363ff082500cf2fc919f1298a7f4acac3e049154870d02)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="apiSecretKeyInput")
    def api_secret_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiSecretKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="apiSecretKey")
    def api_secret_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiSecretKey"))

    @api_secret_key.setter
    def api_secret_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0403cb56945d509090ab828c8f598790a403f01cb1d5216007bcf4b101929481)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiSecretKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicro]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicro], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicro],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58cd8f016fa4b0dcceb6dd8b1f02ea0c1d00f95399074672c938d22e0f1f68a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeeva",
    jsii_struct_bases=[],
    name_mapping={"password": "password", "username": "username"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeeva:
    def __init__(self, *, password: builtins.str, username: builtins.str) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#password AppflowConnectorProfile#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#username AppflowConnectorProfile#username}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6135392831d8b46af3ba92e5cea748b62c2066690ee20ecc21b42b7c4b8bc793)
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "password": password,
            "username": username,
        }

    @builtins.property
    def password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#password AppflowConnectorProfile#password}.'''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#username AppflowConnectorProfile#username}.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeeva(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeevaOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeevaOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c695a1142cc82518e0ba122a483f00fe3a2f51a1c8d0980b108f7f8def384557)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7b529e54829a8ecc0ff1800f5442abf9f32e5633c37e155cead72c4737e9c771)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5eac0080395fc849edc3caffa6847f40c957c41e50828dcbd936d2390934d8e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeeva]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeeva], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeeva],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b30dd3f6c9f77d3f64ab9106c3bcb8ac31a3cf66aea7a9af81b09b51aafa7c32)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendesk",
    jsii_struct_bases=[],
    name_mapping={
        "client_id": "clientId",
        "client_secret": "clientSecret",
        "access_token": "accessToken",
        "oauth_request": "oauthRequest",
    },
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendesk:
    def __init__(
        self,
        *,
        client_id: builtins.str,
        client_secret: builtins.str,
        access_token: typing.Optional[builtins.str] = None,
        oauth_request: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequest", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_id AppflowConnectorProfile#client_id}.
        :param client_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_secret AppflowConnectorProfile#client_secret}.
        :param access_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_token AppflowConnectorProfile#access_token}.
        :param oauth_request: oauth_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_request AppflowConnectorProfile#oauth_request}
        '''
        if isinstance(oauth_request, dict):
            oauth_request = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequest(**oauth_request)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30f9f7594f5c343c71e65317ca8798cc3fdb2d0dff78364ed621780319503c25)
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
            check_type(argname="argument access_token", value=access_token, expected_type=type_hints["access_token"])
            check_type(argname="argument oauth_request", value=oauth_request, expected_type=type_hints["oauth_request"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "client_id": client_id,
            "client_secret": client_secret,
        }
        if access_token is not None:
            self._values["access_token"] = access_token
        if oauth_request is not None:
            self._values["oauth_request"] = oauth_request

    @builtins.property
    def client_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_id AppflowConnectorProfile#client_id}.'''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_secret AppflowConnectorProfile#client_secret}.'''
        result = self._values.get("client_secret")
        assert result is not None, "Required property 'client_secret' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_token AppflowConnectorProfile#access_token}.'''
        result = self._values.get("access_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_request(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequest"]:
        '''oauth_request block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_request AppflowConnectorProfile#oauth_request}
        '''
        result = self._values.get("oauth_request")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequest"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendesk(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequest",
    jsii_struct_bases=[],
    name_mapping={"auth_code": "authCode", "redirect_uri": "redirectUri"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequest:
    def __init__(
        self,
        *,
        auth_code: typing.Optional[builtins.str] = None,
        redirect_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code AppflowConnectorProfile#auth_code}.
        :param redirect_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redirect_uri AppflowConnectorProfile#redirect_uri}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f80cd07527c0b46a36283175c5a6211100a5be471664e370e4f93d7665d88a1b)
            check_type(argname="argument auth_code", value=auth_code, expected_type=type_hints["auth_code"])
            check_type(argname="argument redirect_uri", value=redirect_uri, expected_type=type_hints["redirect_uri"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if auth_code is not None:
            self._values["auth_code"] = auth_code
        if redirect_uri is not None:
            self._values["redirect_uri"] = redirect_uri

    @builtins.property
    def auth_code(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code AppflowConnectorProfile#auth_code}.'''
        result = self._values.get("auth_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def redirect_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redirect_uri AppflowConnectorProfile#redirect_uri}.'''
        result = self._values.get("redirect_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequestOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequestOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__160bdec4d558f7574581713587da129c8900fa559a44d4c50d76ee5754430b2e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAuthCode")
    def reset_auth_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthCode", []))

    @jsii.member(jsii_name="resetRedirectUri")
    def reset_redirect_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedirectUri", []))

    @builtins.property
    @jsii.member(jsii_name="authCodeInput")
    def auth_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectUriInput")
    def redirect_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "redirectUriInput"))

    @builtins.property
    @jsii.member(jsii_name="authCode")
    def auth_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authCode"))

    @auth_code.setter
    def auth_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc7ebdd14a4f0af96b24f3b8584c1d13e2d4df2278e3550345d4397a2748c896)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authCode", value)

    @builtins.property
    @jsii.member(jsii_name="redirectUri")
    def redirect_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redirectUri"))

    @redirect_uri.setter
    def redirect_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d17fe2a9565f430ba6e6b86de7b2cb442a3aeb4567970f5dd6adc9325d26f2e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redirectUri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequest]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequest], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequest],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6f201ac08a4cbd8f282c13a5e0a97ce587434a5e398b33ecd137cdb6fd26dcf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1f781554f4404d9a2e50d06d7c25764ba92c6ab13c9d2685b8418755eb803ad5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putOauthRequest")
    def put_oauth_request(
        self,
        *,
        auth_code: typing.Optional[builtins.str] = None,
        redirect_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code AppflowConnectorProfile#auth_code}.
        :param redirect_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redirect_uri AppflowConnectorProfile#redirect_uri}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequest(
            auth_code=auth_code, redirect_uri=redirect_uri
        )

        return typing.cast(None, jsii.invoke(self, "putOauthRequest", [value]))

    @jsii.member(jsii_name="resetAccessToken")
    def reset_access_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessToken", []))

    @jsii.member(jsii_name="resetOauthRequest")
    def reset_oauth_request(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthRequest", []))

    @builtins.property
    @jsii.member(jsii_name="oauthRequest")
    def oauth_request(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequestOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequestOutputReference, jsii.get(self, "oauthRequest"))

    @builtins.property
    @jsii.member(jsii_name="accessTokenInput")
    def access_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretInput")
    def client_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthRequestInput")
    def oauth_request_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequest]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequest], jsii.get(self, "oauthRequestInput"))

    @builtins.property
    @jsii.member(jsii_name="accessToken")
    def access_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessToken"))

    @access_token.setter
    def access_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2dd96d5b9973fccce57105f81cb834321e64e8fe8e75bd0acc4c1e1a5cd737b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessToken", value)

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be117183e195a92b56e8649f1121b287048d0bf7e19b103d112791c988e68fca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2de3369b7582014c91298678fcad50d4b14f78adea14f9f77c39028f10732f3b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendesk]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendesk], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendesk],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__601b137464027d4541b3794d631236531fc84aab78aac3a500578cd07116a744)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileProperties",
    jsii_struct_bases=[],
    name_mapping={
        "amplitude": "amplitude",
        "custom_connector": "customConnector",
        "datadog": "datadog",
        "dynatrace": "dynatrace",
        "google_analytics": "googleAnalytics",
        "honeycode": "honeycode",
        "infor_nexus": "inforNexus",
        "marketo": "marketo",
        "redshift": "redshift",
        "salesforce": "salesforce",
        "sapo_data": "sapoData",
        "service_now": "serviceNow",
        "singular": "singular",
        "slack": "slack",
        "snowflake": "snowflake",
        "trendmicro": "trendmicro",
        "veeva": "veeva",
        "zendesk": "zendesk",
    },
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileProperties:
    def __init__(
        self,
        *,
        amplitude: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitude", typing.Dict[builtins.str, typing.Any]]] = None,
        custom_connector: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnector", typing.Dict[builtins.str, typing.Any]]] = None,
        datadog: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadog", typing.Dict[builtins.str, typing.Any]]] = None,
        dynatrace: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatrace", typing.Dict[builtins.str, typing.Any]]] = None,
        google_analytics: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalytics", typing.Dict[builtins.str, typing.Any]]] = None,
        honeycode: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycode", typing.Dict[builtins.str, typing.Any]]] = None,
        infor_nexus: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexus", typing.Dict[builtins.str, typing.Any]]] = None,
        marketo: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketo", typing.Dict[builtins.str, typing.Any]]] = None,
        redshift: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshift", typing.Dict[builtins.str, typing.Any]]] = None,
        salesforce: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforce", typing.Dict[builtins.str, typing.Any]]] = None,
        sapo_data: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoData", typing.Dict[builtins.str, typing.Any]]] = None,
        service_now: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNow", typing.Dict[builtins.str, typing.Any]]] = None,
        singular: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingular", typing.Dict[builtins.str, typing.Any]]] = None,
        slack: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlack", typing.Dict[builtins.str, typing.Any]]] = None,
        snowflake: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflake", typing.Dict[builtins.str, typing.Any]]] = None,
        trendmicro: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicro", typing.Dict[builtins.str, typing.Any]]] = None,
        veeva: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeeva", typing.Dict[builtins.str, typing.Any]]] = None,
        zendesk: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendesk", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param amplitude: amplitude block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#amplitude AppflowConnectorProfile#amplitude}
        :param custom_connector: custom_connector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#custom_connector AppflowConnectorProfile#custom_connector}
        :param datadog: datadog block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#datadog AppflowConnectorProfile#datadog}
        :param dynatrace: dynatrace block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#dynatrace AppflowConnectorProfile#dynatrace}
        :param google_analytics: google_analytics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#google_analytics AppflowConnectorProfile#google_analytics}
        :param honeycode: honeycode block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#honeycode AppflowConnectorProfile#honeycode}
        :param infor_nexus: infor_nexus block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#infor_nexus AppflowConnectorProfile#infor_nexus}
        :param marketo: marketo block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#marketo AppflowConnectorProfile#marketo}
        :param redshift: redshift block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redshift AppflowConnectorProfile#redshift}
        :param salesforce: salesforce block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#salesforce AppflowConnectorProfile#salesforce}
        :param sapo_data: sapo_data block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#sapo_data AppflowConnectorProfile#sapo_data}
        :param service_now: service_now block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#service_now AppflowConnectorProfile#service_now}
        :param singular: singular block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#singular AppflowConnectorProfile#singular}
        :param slack: slack block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#slack AppflowConnectorProfile#slack}
        :param snowflake: snowflake block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#snowflake AppflowConnectorProfile#snowflake}
        :param trendmicro: trendmicro block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#trendmicro AppflowConnectorProfile#trendmicro}
        :param veeva: veeva block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#veeva AppflowConnectorProfile#veeva}
        :param zendesk: zendesk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#zendesk AppflowConnectorProfile#zendesk}
        '''
        if isinstance(amplitude, dict):
            amplitude = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitude(**amplitude)
        if isinstance(custom_connector, dict):
            custom_connector = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnector(**custom_connector)
        if isinstance(datadog, dict):
            datadog = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadog(**datadog)
        if isinstance(dynatrace, dict):
            dynatrace = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatrace(**dynatrace)
        if isinstance(google_analytics, dict):
            google_analytics = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalytics(**google_analytics)
        if isinstance(honeycode, dict):
            honeycode = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycode(**honeycode)
        if isinstance(infor_nexus, dict):
            infor_nexus = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexus(**infor_nexus)
        if isinstance(marketo, dict):
            marketo = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketo(**marketo)
        if isinstance(redshift, dict):
            redshift = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshift(**redshift)
        if isinstance(salesforce, dict):
            salesforce = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforce(**salesforce)
        if isinstance(sapo_data, dict):
            sapo_data = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoData(**sapo_data)
        if isinstance(service_now, dict):
            service_now = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNow(**service_now)
        if isinstance(singular, dict):
            singular = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingular(**singular)
        if isinstance(slack, dict):
            slack = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlack(**slack)
        if isinstance(snowflake, dict):
            snowflake = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflake(**snowflake)
        if isinstance(trendmicro, dict):
            trendmicro = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicro(**trendmicro)
        if isinstance(veeva, dict):
            veeva = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeeva(**veeva)
        if isinstance(zendesk, dict):
            zendesk = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendesk(**zendesk)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b095b0281163a9aa16ec538c5b8ba02a63894fa181bb0385dac56afa1cd354bf)
            check_type(argname="argument amplitude", value=amplitude, expected_type=type_hints["amplitude"])
            check_type(argname="argument custom_connector", value=custom_connector, expected_type=type_hints["custom_connector"])
            check_type(argname="argument datadog", value=datadog, expected_type=type_hints["datadog"])
            check_type(argname="argument dynatrace", value=dynatrace, expected_type=type_hints["dynatrace"])
            check_type(argname="argument google_analytics", value=google_analytics, expected_type=type_hints["google_analytics"])
            check_type(argname="argument honeycode", value=honeycode, expected_type=type_hints["honeycode"])
            check_type(argname="argument infor_nexus", value=infor_nexus, expected_type=type_hints["infor_nexus"])
            check_type(argname="argument marketo", value=marketo, expected_type=type_hints["marketo"])
            check_type(argname="argument redshift", value=redshift, expected_type=type_hints["redshift"])
            check_type(argname="argument salesforce", value=salesforce, expected_type=type_hints["salesforce"])
            check_type(argname="argument sapo_data", value=sapo_data, expected_type=type_hints["sapo_data"])
            check_type(argname="argument service_now", value=service_now, expected_type=type_hints["service_now"])
            check_type(argname="argument singular", value=singular, expected_type=type_hints["singular"])
            check_type(argname="argument slack", value=slack, expected_type=type_hints["slack"])
            check_type(argname="argument snowflake", value=snowflake, expected_type=type_hints["snowflake"])
            check_type(argname="argument trendmicro", value=trendmicro, expected_type=type_hints["trendmicro"])
            check_type(argname="argument veeva", value=veeva, expected_type=type_hints["veeva"])
            check_type(argname="argument zendesk", value=zendesk, expected_type=type_hints["zendesk"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if amplitude is not None:
            self._values["amplitude"] = amplitude
        if custom_connector is not None:
            self._values["custom_connector"] = custom_connector
        if datadog is not None:
            self._values["datadog"] = datadog
        if dynatrace is not None:
            self._values["dynatrace"] = dynatrace
        if google_analytics is not None:
            self._values["google_analytics"] = google_analytics
        if honeycode is not None:
            self._values["honeycode"] = honeycode
        if infor_nexus is not None:
            self._values["infor_nexus"] = infor_nexus
        if marketo is not None:
            self._values["marketo"] = marketo
        if redshift is not None:
            self._values["redshift"] = redshift
        if salesforce is not None:
            self._values["salesforce"] = salesforce
        if sapo_data is not None:
            self._values["sapo_data"] = sapo_data
        if service_now is not None:
            self._values["service_now"] = service_now
        if singular is not None:
            self._values["singular"] = singular
        if slack is not None:
            self._values["slack"] = slack
        if snowflake is not None:
            self._values["snowflake"] = snowflake
        if trendmicro is not None:
            self._values["trendmicro"] = trendmicro
        if veeva is not None:
            self._values["veeva"] = veeva
        if zendesk is not None:
            self._values["zendesk"] = zendesk

    @builtins.property
    def amplitude(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitude"]:
        '''amplitude block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#amplitude AppflowConnectorProfile#amplitude}
        '''
        result = self._values.get("amplitude")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitude"], result)

    @builtins.property
    def custom_connector(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnector"]:
        '''custom_connector block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#custom_connector AppflowConnectorProfile#custom_connector}
        '''
        result = self._values.get("custom_connector")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnector"], result)

    @builtins.property
    def datadog(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadog"]:
        '''datadog block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#datadog AppflowConnectorProfile#datadog}
        '''
        result = self._values.get("datadog")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadog"], result)

    @builtins.property
    def dynatrace(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatrace"]:
        '''dynatrace block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#dynatrace AppflowConnectorProfile#dynatrace}
        '''
        result = self._values.get("dynatrace")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatrace"], result)

    @builtins.property
    def google_analytics(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalytics"]:
        '''google_analytics block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#google_analytics AppflowConnectorProfile#google_analytics}
        '''
        result = self._values.get("google_analytics")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalytics"], result)

    @builtins.property
    def honeycode(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycode"]:
        '''honeycode block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#honeycode AppflowConnectorProfile#honeycode}
        '''
        result = self._values.get("honeycode")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycode"], result)

    @builtins.property
    def infor_nexus(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexus"]:
        '''infor_nexus block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#infor_nexus AppflowConnectorProfile#infor_nexus}
        '''
        result = self._values.get("infor_nexus")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexus"], result)

    @builtins.property
    def marketo(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketo"]:
        '''marketo block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#marketo AppflowConnectorProfile#marketo}
        '''
        result = self._values.get("marketo")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketo"], result)

    @builtins.property
    def redshift(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshift"]:
        '''redshift block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redshift AppflowConnectorProfile#redshift}
        '''
        result = self._values.get("redshift")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshift"], result)

    @builtins.property
    def salesforce(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforce"]:
        '''salesforce block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#salesforce AppflowConnectorProfile#salesforce}
        '''
        result = self._values.get("salesforce")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforce"], result)

    @builtins.property
    def sapo_data(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoData"]:
        '''sapo_data block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#sapo_data AppflowConnectorProfile#sapo_data}
        '''
        result = self._values.get("sapo_data")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoData"], result)

    @builtins.property
    def service_now(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNow"]:
        '''service_now block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#service_now AppflowConnectorProfile#service_now}
        '''
        result = self._values.get("service_now")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNow"], result)

    @builtins.property
    def singular(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingular"]:
        '''singular block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#singular AppflowConnectorProfile#singular}
        '''
        result = self._values.get("singular")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingular"], result)

    @builtins.property
    def slack(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlack"]:
        '''slack block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#slack AppflowConnectorProfile#slack}
        '''
        result = self._values.get("slack")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlack"], result)

    @builtins.property
    def snowflake(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflake"]:
        '''snowflake block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#snowflake AppflowConnectorProfile#snowflake}
        '''
        result = self._values.get("snowflake")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflake"], result)

    @builtins.property
    def trendmicro(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicro"]:
        '''trendmicro block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#trendmicro AppflowConnectorProfile#trendmicro}
        '''
        result = self._values.get("trendmicro")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicro"], result)

    @builtins.property
    def veeva(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeeva"]:
        '''veeva block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#veeva AppflowConnectorProfile#veeva}
        '''
        result = self._values.get("veeva")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeeva"], result)

    @builtins.property
    def zendesk(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendesk"]:
        '''zendesk block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#zendesk AppflowConnectorProfile#zendesk}
        '''
        result = self._values.get("zendesk")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendesk"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileProperties(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitude",
    jsii_struct_bases=[],
    name_mapping={},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitude:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitude(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitudeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitudeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ba4d2d65160c2edd979d5cc81b5f8b20f62041035b8403e73e10d7458eb55f03)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitude]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitude], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitude],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8adf04a8d653cba12bb0e28944c3939c2922b2a8f05ace3ade6a6117d1585b34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnector",
    jsii_struct_bases=[],
    name_mapping={
        "oauth2_properties": "oauth2Properties",
        "profile_properties": "profileProperties",
    },
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnector:
    def __init__(
        self,
        *,
        oauth2_properties: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2Properties", typing.Dict[builtins.str, typing.Any]]] = None,
        profile_properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param oauth2_properties: oauth2_properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth2_properties AppflowConnectorProfile#oauth2_properties}
        :param profile_properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#profile_properties AppflowConnectorProfile#profile_properties}.
        '''
        if isinstance(oauth2_properties, dict):
            oauth2_properties = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2Properties(**oauth2_properties)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d735c7784dedc6080836402944ffec29708ce67287efcffb600d0ec903e949c0)
            check_type(argname="argument oauth2_properties", value=oauth2_properties, expected_type=type_hints["oauth2_properties"])
            check_type(argname="argument profile_properties", value=profile_properties, expected_type=type_hints["profile_properties"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if oauth2_properties is not None:
            self._values["oauth2_properties"] = oauth2_properties
        if profile_properties is not None:
            self._values["profile_properties"] = profile_properties

    @builtins.property
    def oauth2_properties(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2Properties"]:
        '''oauth2_properties block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth2_properties AppflowConnectorProfile#oauth2_properties}
        '''
        result = self._values.get("oauth2_properties")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2Properties"], result)

    @builtins.property
    def profile_properties(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#profile_properties AppflowConnectorProfile#profile_properties}.'''
        result = self._values.get("profile_properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2Properties",
    jsii_struct_bases=[],
    name_mapping={
        "oauth2_grant_type": "oauth2GrantType",
        "token_url": "tokenUrl",
        "token_url_custom_properties": "tokenUrlCustomProperties",
    },
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2Properties:
    def __init__(
        self,
        *,
        oauth2_grant_type: builtins.str,
        token_url: builtins.str,
        token_url_custom_properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param oauth2_grant_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth2_grant_type AppflowConnectorProfile#oauth2_grant_type}.
        :param token_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#token_url AppflowConnectorProfile#token_url}.
        :param token_url_custom_properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#token_url_custom_properties AppflowConnectorProfile#token_url_custom_properties}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c428d7813185e7dbb983325c3310947e8c9467e322f025d663c9490c4472c750)
            check_type(argname="argument oauth2_grant_type", value=oauth2_grant_type, expected_type=type_hints["oauth2_grant_type"])
            check_type(argname="argument token_url", value=token_url, expected_type=type_hints["token_url"])
            check_type(argname="argument token_url_custom_properties", value=token_url_custom_properties, expected_type=type_hints["token_url_custom_properties"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "oauth2_grant_type": oauth2_grant_type,
            "token_url": token_url,
        }
        if token_url_custom_properties is not None:
            self._values["token_url_custom_properties"] = token_url_custom_properties

    @builtins.property
    def oauth2_grant_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth2_grant_type AppflowConnectorProfile#oauth2_grant_type}.'''
        result = self._values.get("oauth2_grant_type")
        assert result is not None, "Required property 'oauth2_grant_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def token_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#token_url AppflowConnectorProfile#token_url}.'''
        result = self._values.get("token_url")
        assert result is not None, "Required property 'token_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def token_url_custom_properties(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#token_url_custom_properties AppflowConnectorProfile#token_url_custom_properties}.'''
        result = self._values.get("token_url_custom_properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2Properties(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2PropertiesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2PropertiesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e8c195f1db511dc39ec2cd03f198b38be1baa93238f7bf71f30440736bd3a5dd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetTokenUrlCustomProperties")
    def reset_token_url_custom_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenUrlCustomProperties", []))

    @builtins.property
    @jsii.member(jsii_name="oauth2GrantTypeInput")
    def oauth2_grant_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oauth2GrantTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenUrlCustomPropertiesInput")
    def token_url_custom_properties_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tokenUrlCustomPropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenUrlInput")
    def token_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="oauth2GrantType")
    def oauth2_grant_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "oauth2GrantType"))

    @oauth2_grant_type.setter
    def oauth2_grant_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7aa2f72a395e707e0c6f1deaf9e4380afd5cf262dae76c26d2ee0627f8b13d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauth2GrantType", value)

    @builtins.property
    @jsii.member(jsii_name="tokenUrl")
    def token_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tokenUrl"))

    @token_url.setter
    def token_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0402e2a9f616c894519e94ceb309634e7d9727104083a6c2cb40c4b6c033546b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenUrl", value)

    @builtins.property
    @jsii.member(jsii_name="tokenUrlCustomProperties")
    def token_url_custom_properties(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tokenUrlCustomProperties"))

    @token_url_custom_properties.setter
    def token_url_custom_properties(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c234a02476dcde2e8a5215b49aa791878c7957e0b131b7d0bd83553f7930fc3e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenUrlCustomProperties", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2Properties]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2Properties], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2Properties],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f1d50bdc03600452a98dbb28086b4775eb947ee6226b44d91f39f6921625862)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1393c48b095a98bc707d1ddef54d2bbca16d8038627bcae446cff9709c78a00c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putOauth2Properties")
    def put_oauth2_properties(
        self,
        *,
        oauth2_grant_type: builtins.str,
        token_url: builtins.str,
        token_url_custom_properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param oauth2_grant_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth2_grant_type AppflowConnectorProfile#oauth2_grant_type}.
        :param token_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#token_url AppflowConnectorProfile#token_url}.
        :param token_url_custom_properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#token_url_custom_properties AppflowConnectorProfile#token_url_custom_properties}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2Properties(
            oauth2_grant_type=oauth2_grant_type,
            token_url=token_url,
            token_url_custom_properties=token_url_custom_properties,
        )

        return typing.cast(None, jsii.invoke(self, "putOauth2Properties", [value]))

    @jsii.member(jsii_name="resetOauth2Properties")
    def reset_oauth2_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauth2Properties", []))

    @jsii.member(jsii_name="resetProfileProperties")
    def reset_profile_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProfileProperties", []))

    @builtins.property
    @jsii.member(jsii_name="oauth2Properties")
    def oauth2_properties(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2PropertiesOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2PropertiesOutputReference, jsii.get(self, "oauth2Properties"))

    @builtins.property
    @jsii.member(jsii_name="oauth2PropertiesInput")
    def oauth2_properties_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2Properties]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2Properties], jsii.get(self, "oauth2PropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="profilePropertiesInput")
    def profile_properties_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "profilePropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="profileProperties")
    def profile_properties(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "profileProperties"))

    @profile_properties.setter
    def profile_properties(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__adbaf6447758029d65dfba3d9ea81a97d76346766525a8852a8e34c5069944d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "profileProperties", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnector]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnector], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnector],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b8dabe1fb4838c07916bdeeb653a5a0df4cc7397fdf98a0c4bbb0bdd27bb645)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadog",
    jsii_struct_bases=[],
    name_mapping={"instance_url": "instanceUrl"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadog:
    def __init__(self, *, instance_url: builtins.str) -> None:
        '''
        :param instance_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f9ff553621c8acf7a9ce8e6e36ba25b8b6f76fd9e20404e25d78741857904b4)
            check_type(argname="argument instance_url", value=instance_url, expected_type=type_hints["instance_url"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_url": instance_url,
        }

    @builtins.property
    def instance_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.'''
        result = self._values.get("instance_url")
        assert result is not None, "Required property 'instance_url' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadog(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadogOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadogOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9fabd4fb9581e954774ddb7b48c04445e1c597d20ad572fb8c3878afa2c7be06)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="instanceUrlInput")
    def instance_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceUrl")
    def instance_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceUrl"))

    @instance_url.setter
    def instance_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ef25d3708d51c7b4459e7734a4016e43e5e85ade421a0a810b3c38f3c637d73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadog]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadog], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadog],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33e67d586390cce03b87d683d97f4c302d078cdbfb757dd02bc90d9cb7223308)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatrace",
    jsii_struct_bases=[],
    name_mapping={"instance_url": "instanceUrl"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatrace:
    def __init__(self, *, instance_url: builtins.str) -> None:
        '''
        :param instance_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3db7f25cf6ff1568fb8d5248a042751d36cf73a0d078e8c77155eebd5e2a5e9)
            check_type(argname="argument instance_url", value=instance_url, expected_type=type_hints["instance_url"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_url": instance_url,
        }

    @builtins.property
    def instance_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.'''
        result = self._values.get("instance_url")
        assert result is not None, "Required property 'instance_url' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatrace(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatraceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatraceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__92673e9fbd5482e4d9d5dc0f0428a902ed43bc11022dca98abb858ac2cd10411)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="instanceUrlInput")
    def instance_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceUrl")
    def instance_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceUrl"))

    @instance_url.setter
    def instance_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd66ec29cc91b0ed72dea300ae13cc03be6952fba3b7d7b27ba09b590e1fe052)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatrace]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatrace], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatrace],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aab62bf3214dda510e57aa201f0249045dadd555d05713071c17addc05e16e02)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalytics",
    jsii_struct_bases=[],
    name_mapping={},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalytics:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalytics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalyticsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalyticsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__333a727b9de094b70dc75a07cda39bcbe0a53b6a4caec8ed91402b880e721fa3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalytics]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalytics], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalytics],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__145cdb9f89a64dc5d8dedf5d142b6c53f632029846460568fc784fc900b6078e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycode",
    jsii_struct_bases=[],
    name_mapping={},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycode:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycode(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycodeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycodeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0d99e408ee8febbacde4c6a4212f7abccb877828ca2fee67916ef8d60426dacf)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycode]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycode], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycode],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bde9bb90ce238cd6f8ccc9b37aef18167b63be7a6a9ffc9a51700a0ef9b22a82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexus",
    jsii_struct_bases=[],
    name_mapping={"instance_url": "instanceUrl"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexus:
    def __init__(self, *, instance_url: builtins.str) -> None:
        '''
        :param instance_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb2b60470aa27b1cd678de80a41e87a6dc01e2d89859f784d7aa081b31518ef7)
            check_type(argname="argument instance_url", value=instance_url, expected_type=type_hints["instance_url"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_url": instance_url,
        }

    @builtins.property
    def instance_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.'''
        result = self._values.get("instance_url")
        assert result is not None, "Required property 'instance_url' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexus(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexusOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexusOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3c8f1e9cf07557edbb5dfe0776014a9f99852920f637be689057eae2a3021eaf)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="instanceUrlInput")
    def instance_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceUrl")
    def instance_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceUrl"))

    @instance_url.setter
    def instance_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37452a1dfffbabb264905848c4295d984c1cb3d835b6aff1b1a12d091edce208)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexus]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexus], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexus],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afee05945d3d6533227512067a4876bff3bd94986e7edab846881a41807b0eed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketo",
    jsii_struct_bases=[],
    name_mapping={"instance_url": "instanceUrl"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketo:
    def __init__(self, *, instance_url: builtins.str) -> None:
        '''
        :param instance_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8cbabd1b50d26ce8113e7b683e77486be1708c6ffc521039bfc34614a725d7c)
            check_type(argname="argument instance_url", value=instance_url, expected_type=type_hints["instance_url"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_url": instance_url,
        }

    @builtins.property
    def instance_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.'''
        result = self._values.get("instance_url")
        assert result is not None, "Required property 'instance_url' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketoOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketoOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__777a58e585385f1e74de27c4d52d50c7946b1f4148e7389b06fbb7acc87faeac)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="instanceUrlInput")
    def instance_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceUrl")
    def instance_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceUrl"))

    @instance_url.setter
    def instance_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e3718e4b23411666d3fc2f3129957cd5fa5ca5eb874b90ae842ddacbf6efc38)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketo]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketo],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d089d26949ec6e66c601e16a455cee96ed2b8cd6632aa321ff6f6d27c183136)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1dc721ff7ea8d3063e365a1a5a16a04c162a2c89964d591b0b703b8678cd1cef)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAmplitude")
    def put_amplitude(self) -> None:
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitude()

        return typing.cast(None, jsii.invoke(self, "putAmplitude", [value]))

    @jsii.member(jsii_name="putCustomConnector")
    def put_custom_connector(
        self,
        *,
        oauth2_properties: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2Properties, typing.Dict[builtins.str, typing.Any]]] = None,
        profile_properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param oauth2_properties: oauth2_properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth2_properties AppflowConnectorProfile#oauth2_properties}
        :param profile_properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#profile_properties AppflowConnectorProfile#profile_properties}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnector(
            oauth2_properties=oauth2_properties, profile_properties=profile_properties
        )

        return typing.cast(None, jsii.invoke(self, "putCustomConnector", [value]))

    @jsii.member(jsii_name="putDatadog")
    def put_datadog(self, *, instance_url: builtins.str) -> None:
        '''
        :param instance_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadog(
            instance_url=instance_url
        )

        return typing.cast(None, jsii.invoke(self, "putDatadog", [value]))

    @jsii.member(jsii_name="putDynatrace")
    def put_dynatrace(self, *, instance_url: builtins.str) -> None:
        '''
        :param instance_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatrace(
            instance_url=instance_url
        )

        return typing.cast(None, jsii.invoke(self, "putDynatrace", [value]))

    @jsii.member(jsii_name="putGoogleAnalytics")
    def put_google_analytics(self) -> None:
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalytics()

        return typing.cast(None, jsii.invoke(self, "putGoogleAnalytics", [value]))

    @jsii.member(jsii_name="putHoneycode")
    def put_honeycode(self) -> None:
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycode()

        return typing.cast(None, jsii.invoke(self, "putHoneycode", [value]))

    @jsii.member(jsii_name="putInforNexus")
    def put_infor_nexus(self, *, instance_url: builtins.str) -> None:
        '''
        :param instance_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexus(
            instance_url=instance_url
        )

        return typing.cast(None, jsii.invoke(self, "putInforNexus", [value]))

    @jsii.member(jsii_name="putMarketo")
    def put_marketo(self, *, instance_url: builtins.str) -> None:
        '''
        :param instance_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketo(
            instance_url=instance_url
        )

        return typing.cast(None, jsii.invoke(self, "putMarketo", [value]))

    @jsii.member(jsii_name="putRedshift")
    def put_redshift(
        self,
        *,
        bucket_name: builtins.str,
        role_arn: builtins.str,
        bucket_prefix: typing.Optional[builtins.str] = None,
        cluster_identifier: typing.Optional[builtins.str] = None,
        data_api_role_arn: typing.Optional[builtins.str] = None,
        database_name: typing.Optional[builtins.str] = None,
        database_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#bucket_name AppflowConnectorProfile#bucket_name}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#role_arn AppflowConnectorProfile#role_arn}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#bucket_prefix AppflowConnectorProfile#bucket_prefix}.
        :param cluster_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#cluster_identifier AppflowConnectorProfile#cluster_identifier}.
        :param data_api_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#data_api_role_arn AppflowConnectorProfile#data_api_role_arn}.
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#database_name AppflowConnectorProfile#database_name}.
        :param database_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#database_url AppflowConnectorProfile#database_url}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshift(
            bucket_name=bucket_name,
            role_arn=role_arn,
            bucket_prefix=bucket_prefix,
            cluster_identifier=cluster_identifier,
            data_api_role_arn=data_api_role_arn,
            database_name=database_name,
            database_url=database_url,
        )

        return typing.cast(None, jsii.invoke(self, "putRedshift", [value]))

    @jsii.member(jsii_name="putSalesforce")
    def put_salesforce(
        self,
        *,
        instance_url: typing.Optional[builtins.str] = None,
        is_sandbox_environment: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param instance_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.
        :param is_sandbox_environment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#is_sandbox_environment AppflowConnectorProfile#is_sandbox_environment}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforce(
            instance_url=instance_url, is_sandbox_environment=is_sandbox_environment
        )

        return typing.cast(None, jsii.invoke(self, "putSalesforce", [value]))

    @jsii.member(jsii_name="putSapoData")
    def put_sapo_data(
        self,
        *,
        application_host_url: builtins.str,
        application_service_path: builtins.str,
        client_number: builtins.str,
        port_number: jsii.Number,
        logon_language: typing.Optional[builtins.str] = None,
        oauth_properties: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthProperties", typing.Dict[builtins.str, typing.Any]]] = None,
        private_link_service_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param application_host_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#application_host_url AppflowConnectorProfile#application_host_url}.
        :param application_service_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#application_service_path AppflowConnectorProfile#application_service_path}.
        :param client_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_number AppflowConnectorProfile#client_number}.
        :param port_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#port_number AppflowConnectorProfile#port_number}.
        :param logon_language: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#logon_language AppflowConnectorProfile#logon_language}.
        :param oauth_properties: oauth_properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_properties AppflowConnectorProfile#oauth_properties}
        :param private_link_service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#private_link_service_name AppflowConnectorProfile#private_link_service_name}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoData(
            application_host_url=application_host_url,
            application_service_path=application_service_path,
            client_number=client_number,
            port_number=port_number,
            logon_language=logon_language,
            oauth_properties=oauth_properties,
            private_link_service_name=private_link_service_name,
        )

        return typing.cast(None, jsii.invoke(self, "putSapoData", [value]))

    @jsii.member(jsii_name="putServiceNow")
    def put_service_now(self, *, instance_url: builtins.str) -> None:
        '''
        :param instance_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNow(
            instance_url=instance_url
        )

        return typing.cast(None, jsii.invoke(self, "putServiceNow", [value]))

    @jsii.member(jsii_name="putSingular")
    def put_singular(self) -> None:
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingular()

        return typing.cast(None, jsii.invoke(self, "putSingular", [value]))

    @jsii.member(jsii_name="putSlack")
    def put_slack(self, *, instance_url: builtins.str) -> None:
        '''
        :param instance_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlack(
            instance_url=instance_url
        )

        return typing.cast(None, jsii.invoke(self, "putSlack", [value]))

    @jsii.member(jsii_name="putSnowflake")
    def put_snowflake(
        self,
        *,
        bucket_name: builtins.str,
        stage: builtins.str,
        warehouse: builtins.str,
        account_name: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        private_link_service_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#bucket_name AppflowConnectorProfile#bucket_name}.
        :param stage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#stage AppflowConnectorProfile#stage}.
        :param warehouse: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#warehouse AppflowConnectorProfile#warehouse}.
        :param account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#account_name AppflowConnectorProfile#account_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#bucket_prefix AppflowConnectorProfile#bucket_prefix}.
        :param private_link_service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#private_link_service_name AppflowConnectorProfile#private_link_service_name}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#region AppflowConnectorProfile#region}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflake(
            bucket_name=bucket_name,
            stage=stage,
            warehouse=warehouse,
            account_name=account_name,
            bucket_prefix=bucket_prefix,
            private_link_service_name=private_link_service_name,
            region=region,
        )

        return typing.cast(None, jsii.invoke(self, "putSnowflake", [value]))

    @jsii.member(jsii_name="putTrendmicro")
    def put_trendmicro(self) -> None:
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicro()

        return typing.cast(None, jsii.invoke(self, "putTrendmicro", [value]))

    @jsii.member(jsii_name="putVeeva")
    def put_veeva(self, *, instance_url: builtins.str) -> None:
        '''
        :param instance_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeeva(
            instance_url=instance_url
        )

        return typing.cast(None, jsii.invoke(self, "putVeeva", [value]))

    @jsii.member(jsii_name="putZendesk")
    def put_zendesk(self, *, instance_url: builtins.str) -> None:
        '''
        :param instance_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendesk(
            instance_url=instance_url
        )

        return typing.cast(None, jsii.invoke(self, "putZendesk", [value]))

    @jsii.member(jsii_name="resetAmplitude")
    def reset_amplitude(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAmplitude", []))

    @jsii.member(jsii_name="resetCustomConnector")
    def reset_custom_connector(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomConnector", []))

    @jsii.member(jsii_name="resetDatadog")
    def reset_datadog(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatadog", []))

    @jsii.member(jsii_name="resetDynatrace")
    def reset_dynatrace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDynatrace", []))

    @jsii.member(jsii_name="resetGoogleAnalytics")
    def reset_google_analytics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGoogleAnalytics", []))

    @jsii.member(jsii_name="resetHoneycode")
    def reset_honeycode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHoneycode", []))

    @jsii.member(jsii_name="resetInforNexus")
    def reset_infor_nexus(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInforNexus", []))

    @jsii.member(jsii_name="resetMarketo")
    def reset_marketo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMarketo", []))

    @jsii.member(jsii_name="resetRedshift")
    def reset_redshift(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedshift", []))

    @jsii.member(jsii_name="resetSalesforce")
    def reset_salesforce(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSalesforce", []))

    @jsii.member(jsii_name="resetSapoData")
    def reset_sapo_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSapoData", []))

    @jsii.member(jsii_name="resetServiceNow")
    def reset_service_now(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceNow", []))

    @jsii.member(jsii_name="resetSingular")
    def reset_singular(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSingular", []))

    @jsii.member(jsii_name="resetSlack")
    def reset_slack(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSlack", []))

    @jsii.member(jsii_name="resetSnowflake")
    def reset_snowflake(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSnowflake", []))

    @jsii.member(jsii_name="resetTrendmicro")
    def reset_trendmicro(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrendmicro", []))

    @jsii.member(jsii_name="resetVeeva")
    def reset_veeva(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVeeva", []))

    @jsii.member(jsii_name="resetZendesk")
    def reset_zendesk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZendesk", []))

    @builtins.property
    @jsii.member(jsii_name="amplitude")
    def amplitude(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitudeOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitudeOutputReference, jsii.get(self, "amplitude"))

    @builtins.property
    @jsii.member(jsii_name="customConnector")
    def custom_connector(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOutputReference, jsii.get(self, "customConnector"))

    @builtins.property
    @jsii.member(jsii_name="datadog")
    def datadog(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadogOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadogOutputReference, jsii.get(self, "datadog"))

    @builtins.property
    @jsii.member(jsii_name="dynatrace")
    def dynatrace(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatraceOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatraceOutputReference, jsii.get(self, "dynatrace"))

    @builtins.property
    @jsii.member(jsii_name="googleAnalytics")
    def google_analytics(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalyticsOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalyticsOutputReference, jsii.get(self, "googleAnalytics"))

    @builtins.property
    @jsii.member(jsii_name="honeycode")
    def honeycode(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycodeOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycodeOutputReference, jsii.get(self, "honeycode"))

    @builtins.property
    @jsii.member(jsii_name="inforNexus")
    def infor_nexus(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexusOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexusOutputReference, jsii.get(self, "inforNexus"))

    @builtins.property
    @jsii.member(jsii_name="marketo")
    def marketo(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketoOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketoOutputReference, jsii.get(self, "marketo"))

    @builtins.property
    @jsii.member(jsii_name="redshift")
    def redshift(
        self,
    ) -> "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshiftOutputReference":
        return typing.cast("AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshiftOutputReference", jsii.get(self, "redshift"))

    @builtins.property
    @jsii.member(jsii_name="salesforce")
    def salesforce(
        self,
    ) -> "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforceOutputReference":
        return typing.cast("AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforceOutputReference", jsii.get(self, "salesforce"))

    @builtins.property
    @jsii.member(jsii_name="sapoData")
    def sapo_data(
        self,
    ) -> "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOutputReference":
        return typing.cast("AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOutputReference", jsii.get(self, "sapoData"))

    @builtins.property
    @jsii.member(jsii_name="serviceNow")
    def service_now(
        self,
    ) -> "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNowOutputReference":
        return typing.cast("AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNowOutputReference", jsii.get(self, "serviceNow"))

    @builtins.property
    @jsii.member(jsii_name="singular")
    def singular(
        self,
    ) -> "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingularOutputReference":
        return typing.cast("AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingularOutputReference", jsii.get(self, "singular"))

    @builtins.property
    @jsii.member(jsii_name="slack")
    def slack(
        self,
    ) -> "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlackOutputReference":
        return typing.cast("AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlackOutputReference", jsii.get(self, "slack"))

    @builtins.property
    @jsii.member(jsii_name="snowflake")
    def snowflake(
        self,
    ) -> "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflakeOutputReference":
        return typing.cast("AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflakeOutputReference", jsii.get(self, "snowflake"))

    @builtins.property
    @jsii.member(jsii_name="trendmicro")
    def trendmicro(
        self,
    ) -> "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicroOutputReference":
        return typing.cast("AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicroOutputReference", jsii.get(self, "trendmicro"))

    @builtins.property
    @jsii.member(jsii_name="veeva")
    def veeva(
        self,
    ) -> "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeevaOutputReference":
        return typing.cast("AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeevaOutputReference", jsii.get(self, "veeva"))

    @builtins.property
    @jsii.member(jsii_name="zendesk")
    def zendesk(
        self,
    ) -> "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendeskOutputReference":
        return typing.cast("AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendeskOutputReference", jsii.get(self, "zendesk"))

    @builtins.property
    @jsii.member(jsii_name="amplitudeInput")
    def amplitude_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitude]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitude], jsii.get(self, "amplitudeInput"))

    @builtins.property
    @jsii.member(jsii_name="customConnectorInput")
    def custom_connector_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnector]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnector], jsii.get(self, "customConnectorInput"))

    @builtins.property
    @jsii.member(jsii_name="datadogInput")
    def datadog_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadog]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadog], jsii.get(self, "datadogInput"))

    @builtins.property
    @jsii.member(jsii_name="dynatraceInput")
    def dynatrace_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatrace]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatrace], jsii.get(self, "dynatraceInput"))

    @builtins.property
    @jsii.member(jsii_name="googleAnalyticsInput")
    def google_analytics_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalytics]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalytics], jsii.get(self, "googleAnalyticsInput"))

    @builtins.property
    @jsii.member(jsii_name="honeycodeInput")
    def honeycode_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycode]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycode], jsii.get(self, "honeycodeInput"))

    @builtins.property
    @jsii.member(jsii_name="inforNexusInput")
    def infor_nexus_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexus]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexus], jsii.get(self, "inforNexusInput"))

    @builtins.property
    @jsii.member(jsii_name="marketoInput")
    def marketo_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketo]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketo], jsii.get(self, "marketoInput"))

    @builtins.property
    @jsii.member(jsii_name="redshiftInput")
    def redshift_input(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshift"]:
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshift"], jsii.get(self, "redshiftInput"))

    @builtins.property
    @jsii.member(jsii_name="salesforceInput")
    def salesforce_input(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforce"]:
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforce"], jsii.get(self, "salesforceInput"))

    @builtins.property
    @jsii.member(jsii_name="sapoDataInput")
    def sapo_data_input(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoData"]:
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoData"], jsii.get(self, "sapoDataInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceNowInput")
    def service_now_input(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNow"]:
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNow"], jsii.get(self, "serviceNowInput"))

    @builtins.property
    @jsii.member(jsii_name="singularInput")
    def singular_input(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingular"]:
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingular"], jsii.get(self, "singularInput"))

    @builtins.property
    @jsii.member(jsii_name="slackInput")
    def slack_input(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlack"]:
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlack"], jsii.get(self, "slackInput"))

    @builtins.property
    @jsii.member(jsii_name="snowflakeInput")
    def snowflake_input(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflake"]:
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflake"], jsii.get(self, "snowflakeInput"))

    @builtins.property
    @jsii.member(jsii_name="trendmicroInput")
    def trendmicro_input(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicro"]:
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicro"], jsii.get(self, "trendmicroInput"))

    @builtins.property
    @jsii.member(jsii_name="veevaInput")
    def veeva_input(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeeva"]:
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeeva"], jsii.get(self, "veevaInput"))

    @builtins.property
    @jsii.member(jsii_name="zendeskInput")
    def zendesk_input(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendesk"]:
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendesk"], jsii.get(self, "zendeskInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileProperties]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileProperties], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileProperties],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ed69841c6b68fa04e0d5ee8cf418eb5017960e1510a68433990ec95c88243bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshift",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "role_arn": "roleArn",
        "bucket_prefix": "bucketPrefix",
        "cluster_identifier": "clusterIdentifier",
        "data_api_role_arn": "dataApiRoleArn",
        "database_name": "databaseName",
        "database_url": "databaseUrl",
    },
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshift:
    def __init__(
        self,
        *,
        bucket_name: builtins.str,
        role_arn: builtins.str,
        bucket_prefix: typing.Optional[builtins.str] = None,
        cluster_identifier: typing.Optional[builtins.str] = None,
        data_api_role_arn: typing.Optional[builtins.str] = None,
        database_name: typing.Optional[builtins.str] = None,
        database_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#bucket_name AppflowConnectorProfile#bucket_name}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#role_arn AppflowConnectorProfile#role_arn}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#bucket_prefix AppflowConnectorProfile#bucket_prefix}.
        :param cluster_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#cluster_identifier AppflowConnectorProfile#cluster_identifier}.
        :param data_api_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#data_api_role_arn AppflowConnectorProfile#data_api_role_arn}.
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#database_name AppflowConnectorProfile#database_name}.
        :param database_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#database_url AppflowConnectorProfile#database_url}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba8cc6740904e61b2f58eb5b9f8967e620f704bdf693edbe096caa0cc07b2823)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
            check_type(argname="argument cluster_identifier", value=cluster_identifier, expected_type=type_hints["cluster_identifier"])
            check_type(argname="argument data_api_role_arn", value=data_api_role_arn, expected_type=type_hints["data_api_role_arn"])
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument database_url", value=database_url, expected_type=type_hints["database_url"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket_name": bucket_name,
            "role_arn": role_arn,
        }
        if bucket_prefix is not None:
            self._values["bucket_prefix"] = bucket_prefix
        if cluster_identifier is not None:
            self._values["cluster_identifier"] = cluster_identifier
        if data_api_role_arn is not None:
            self._values["data_api_role_arn"] = data_api_role_arn
        if database_name is not None:
            self._values["database_name"] = database_name
        if database_url is not None:
            self._values["database_url"] = database_url

    @builtins.property
    def bucket_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#bucket_name AppflowConnectorProfile#bucket_name}.'''
        result = self._values.get("bucket_name")
        assert result is not None, "Required property 'bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#role_arn AppflowConnectorProfile#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bucket_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#bucket_prefix AppflowConnectorProfile#bucket_prefix}.'''
        result = self._values.get("bucket_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cluster_identifier(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#cluster_identifier AppflowConnectorProfile#cluster_identifier}.'''
        result = self._values.get("cluster_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_api_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#data_api_role_arn AppflowConnectorProfile#data_api_role_arn}.'''
        result = self._values.get("data_api_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def database_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#database_name AppflowConnectorProfile#database_name}.'''
        result = self._values.get("database_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def database_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#database_url AppflowConnectorProfile#database_url}.'''
        result = self._values.get("database_url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshift(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshiftOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshiftOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__50415ebbbfa0e3b73cf633e209a1622a7111ec865edfc8b6ef6b2819068e9868)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBucketPrefix")
    def reset_bucket_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketPrefix", []))

    @jsii.member(jsii_name="resetClusterIdentifier")
    def reset_cluster_identifier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterIdentifier", []))

    @jsii.member(jsii_name="resetDataApiRoleArn")
    def reset_data_api_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataApiRoleArn", []))

    @jsii.member(jsii_name="resetDatabaseName")
    def reset_database_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatabaseName", []))

    @jsii.member(jsii_name="resetDatabaseUrl")
    def reset_database_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatabaseUrl", []))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketPrefixInput")
    def bucket_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterIdentifierInput")
    def cluster_identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterIdentifierInput"))

    @builtins.property
    @jsii.member(jsii_name="dataApiRoleArnInput")
    def data_api_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataApiRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseNameInput")
    def database_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseNameInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseUrlInput")
    def database_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fbfa34014b9f252e9b080336dd7331345bde2bee3d9a01ffed4bbf39b651a143)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="bucketPrefix")
    def bucket_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketPrefix"))

    @bucket_prefix.setter
    def bucket_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0d2be1a9ad3696ed462ff94f8da76b6838361be4da4a895a7a103cd3713e8aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="clusterIdentifier")
    def cluster_identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterIdentifier"))

    @cluster_identifier.setter
    def cluster_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__006dad5b19d9ef175105300fccca630f8e9587d9f38dfd0bdf06a57203e6aa47)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="dataApiRoleArn")
    def data_api_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataApiRoleArn"))

    @data_api_role_arn.setter
    def data_api_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8c4fe1f6249807f00dbb555577eebad1cb2b7ec35b14b608b93387caef48b0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataApiRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="databaseName")
    def database_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseName"))

    @database_name.setter
    def database_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96d4e4a482009bc347bcfa4884923950a04a8191e703eed16363b2fb79eaaec9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseName", value)

    @builtins.property
    @jsii.member(jsii_name="databaseUrl")
    def database_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseUrl"))

    @database_url.setter
    def database_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aadff60126cc7565b19962a85dbf91532f9a772e1852b3c28ac38907b9807317)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseUrl", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c791158b6bc2cb9ec2e852f5e4cef5c8bf160915647ac86cc4ab10c4ca3e45d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshift]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshift], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshift],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d84d10bc9e57d5d29c33940999fa458c8c143d74934b411598762fbf75d441d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforce",
    jsii_struct_bases=[],
    name_mapping={
        "instance_url": "instanceUrl",
        "is_sandbox_environment": "isSandboxEnvironment",
    },
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforce:
    def __init__(
        self,
        *,
        instance_url: typing.Optional[builtins.str] = None,
        is_sandbox_environment: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param instance_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.
        :param is_sandbox_environment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#is_sandbox_environment AppflowConnectorProfile#is_sandbox_environment}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1595733a2190ee0f4bf387a947a6c38a49e7b5f37437fba0a2fae9956f6108e3)
            check_type(argname="argument instance_url", value=instance_url, expected_type=type_hints["instance_url"])
            check_type(argname="argument is_sandbox_environment", value=is_sandbox_environment, expected_type=type_hints["is_sandbox_environment"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if instance_url is not None:
            self._values["instance_url"] = instance_url
        if is_sandbox_environment is not None:
            self._values["is_sandbox_environment"] = is_sandbox_environment

    @builtins.property
    def instance_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.'''
        result = self._values.get("instance_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def is_sandbox_environment(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#is_sandbox_environment AppflowConnectorProfile#is_sandbox_environment}.'''
        result = self._values.get("is_sandbox_environment")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforce(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f3b0dce2209a09110bbf29c55ee0271e7dd8096b9cbea98d3e5727d62e1026bc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetInstanceUrl")
    def reset_instance_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceUrl", []))

    @jsii.member(jsii_name="resetIsSandboxEnvironment")
    def reset_is_sandbox_environment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsSandboxEnvironment", []))

    @builtins.property
    @jsii.member(jsii_name="instanceUrlInput")
    def instance_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="isSandboxEnvironmentInput")
    def is_sandbox_environment_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "isSandboxEnvironmentInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceUrl")
    def instance_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceUrl"))

    @instance_url.setter
    def instance_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28cfd887659c5a3dd8c402f9163135c05120ba79a0220577fb8d4adcba37a07a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceUrl", value)

    @builtins.property
    @jsii.member(jsii_name="isSandboxEnvironment")
    def is_sandbox_environment(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "isSandboxEnvironment"))

    @is_sandbox_environment.setter
    def is_sandbox_environment(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b8170254a210e38c0991c76c9d6a6f398a58a0a12585acc9426d60fdc4a8178)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isSandboxEnvironment", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforce]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforce], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforce],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__943757c6abcae90f18f9a10b37a5cd4a454cbeb390c21a4781c90d0f4f47e092)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoData",
    jsii_struct_bases=[],
    name_mapping={
        "application_host_url": "applicationHostUrl",
        "application_service_path": "applicationServicePath",
        "client_number": "clientNumber",
        "port_number": "portNumber",
        "logon_language": "logonLanguage",
        "oauth_properties": "oauthProperties",
        "private_link_service_name": "privateLinkServiceName",
    },
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoData:
    def __init__(
        self,
        *,
        application_host_url: builtins.str,
        application_service_path: builtins.str,
        client_number: builtins.str,
        port_number: jsii.Number,
        logon_language: typing.Optional[builtins.str] = None,
        oauth_properties: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthProperties", typing.Dict[builtins.str, typing.Any]]] = None,
        private_link_service_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param application_host_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#application_host_url AppflowConnectorProfile#application_host_url}.
        :param application_service_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#application_service_path AppflowConnectorProfile#application_service_path}.
        :param client_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_number AppflowConnectorProfile#client_number}.
        :param port_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#port_number AppflowConnectorProfile#port_number}.
        :param logon_language: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#logon_language AppflowConnectorProfile#logon_language}.
        :param oauth_properties: oauth_properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_properties AppflowConnectorProfile#oauth_properties}
        :param private_link_service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#private_link_service_name AppflowConnectorProfile#private_link_service_name}.
        '''
        if isinstance(oauth_properties, dict):
            oauth_properties = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthProperties(**oauth_properties)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d458cd9c942ed9c9f25c50db8129203bc4d83dd027336796f5f978f137a4cf16)
            check_type(argname="argument application_host_url", value=application_host_url, expected_type=type_hints["application_host_url"])
            check_type(argname="argument application_service_path", value=application_service_path, expected_type=type_hints["application_service_path"])
            check_type(argname="argument client_number", value=client_number, expected_type=type_hints["client_number"])
            check_type(argname="argument port_number", value=port_number, expected_type=type_hints["port_number"])
            check_type(argname="argument logon_language", value=logon_language, expected_type=type_hints["logon_language"])
            check_type(argname="argument oauth_properties", value=oauth_properties, expected_type=type_hints["oauth_properties"])
            check_type(argname="argument private_link_service_name", value=private_link_service_name, expected_type=type_hints["private_link_service_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_host_url": application_host_url,
            "application_service_path": application_service_path,
            "client_number": client_number,
            "port_number": port_number,
        }
        if logon_language is not None:
            self._values["logon_language"] = logon_language
        if oauth_properties is not None:
            self._values["oauth_properties"] = oauth_properties
        if private_link_service_name is not None:
            self._values["private_link_service_name"] = private_link_service_name

    @builtins.property
    def application_host_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#application_host_url AppflowConnectorProfile#application_host_url}.'''
        result = self._values.get("application_host_url")
        assert result is not None, "Required property 'application_host_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def application_service_path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#application_service_path AppflowConnectorProfile#application_service_path}.'''
        result = self._values.get("application_service_path")
        assert result is not None, "Required property 'application_service_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_number(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_number AppflowConnectorProfile#client_number}.'''
        result = self._values.get("client_number")
        assert result is not None, "Required property 'client_number' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port_number(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#port_number AppflowConnectorProfile#port_number}.'''
        result = self._values.get("port_number")
        assert result is not None, "Required property 'port_number' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def logon_language(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#logon_language AppflowConnectorProfile#logon_language}.'''
        result = self._values.get("logon_language")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_properties(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthProperties"]:
        '''oauth_properties block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_properties AppflowConnectorProfile#oauth_properties}
        '''
        result = self._values.get("oauth_properties")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthProperties"], result)

    @builtins.property
    def private_link_service_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#private_link_service_name AppflowConnectorProfile#private_link_service_name}.'''
        result = self._values.get("private_link_service_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoData(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthProperties",
    jsii_struct_bases=[],
    name_mapping={
        "auth_code_url": "authCodeUrl",
        "oauth_scopes": "oauthScopes",
        "token_url": "tokenUrl",
    },
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthProperties:
    def __init__(
        self,
        *,
        auth_code_url: builtins.str,
        oauth_scopes: typing.Sequence[builtins.str],
        token_url: builtins.str,
    ) -> None:
        '''
        :param auth_code_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code_url AppflowConnectorProfile#auth_code_url}.
        :param oauth_scopes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_scopes AppflowConnectorProfile#oauth_scopes}.
        :param token_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#token_url AppflowConnectorProfile#token_url}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__053ff9d6b59c5ea156260e8e0b7c3846d71e0f025bdc378352644a0830f9138d)
            check_type(argname="argument auth_code_url", value=auth_code_url, expected_type=type_hints["auth_code_url"])
            check_type(argname="argument oauth_scopes", value=oauth_scopes, expected_type=type_hints["oauth_scopes"])
            check_type(argname="argument token_url", value=token_url, expected_type=type_hints["token_url"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "auth_code_url": auth_code_url,
            "oauth_scopes": oauth_scopes,
            "token_url": token_url,
        }

    @builtins.property
    def auth_code_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code_url AppflowConnectorProfile#auth_code_url}.'''
        result = self._values.get("auth_code_url")
        assert result is not None, "Required property 'auth_code_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def oauth_scopes(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_scopes AppflowConnectorProfile#oauth_scopes}.'''
        result = self._values.get("oauth_scopes")
        assert result is not None, "Required property 'oauth_scopes' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def token_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#token_url AppflowConnectorProfile#token_url}.'''
        result = self._values.get("token_url")
        assert result is not None, "Required property 'token_url' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthProperties(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthPropertiesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthPropertiesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__437caa7ad50e3b43658f1b8181fa74de814dcc76b0233d206eadb825937f27bc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="authCodeUrlInput")
    def auth_code_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authCodeUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthScopesInput")
    def oauth_scopes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "oauthScopesInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenUrlInput")
    def token_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="authCodeUrl")
    def auth_code_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authCodeUrl"))

    @auth_code_url.setter
    def auth_code_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e40b06daae0c04daa3d475af9c355b54052fe1b62977a2405f87b3dd690ae44e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authCodeUrl", value)

    @builtins.property
    @jsii.member(jsii_name="oauthScopes")
    def oauth_scopes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "oauthScopes"))

    @oauth_scopes.setter
    def oauth_scopes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d82232bfbe69e81545090327f5d3a704c2cbb70b76e03bf275010f43d9dedba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauthScopes", value)

    @builtins.property
    @jsii.member(jsii_name="tokenUrl")
    def token_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tokenUrl"))

    @token_url.setter
    def token_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74ea7ea7054b93c9f564e1bce8b0d164ad38b27dda330ea335c3edce495d0aac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthProperties]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthProperties], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthProperties],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cce705c1b743c55543db5294e5622413bf037d39e1a085f6c41002b0a2f943fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a939e3255b570b7ec98aa0ad15276da5195ff3786d8de8f105d34ad33f27fd95)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putOauthProperties")
    def put_oauth_properties(
        self,
        *,
        auth_code_url: builtins.str,
        oauth_scopes: typing.Sequence[builtins.str],
        token_url: builtins.str,
    ) -> None:
        '''
        :param auth_code_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code_url AppflowConnectorProfile#auth_code_url}.
        :param oauth_scopes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_scopes AppflowConnectorProfile#oauth_scopes}.
        :param token_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#token_url AppflowConnectorProfile#token_url}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthProperties(
            auth_code_url=auth_code_url, oauth_scopes=oauth_scopes, token_url=token_url
        )

        return typing.cast(None, jsii.invoke(self, "putOauthProperties", [value]))

    @jsii.member(jsii_name="resetLogonLanguage")
    def reset_logon_language(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogonLanguage", []))

    @jsii.member(jsii_name="resetOauthProperties")
    def reset_oauth_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthProperties", []))

    @jsii.member(jsii_name="resetPrivateLinkServiceName")
    def reset_private_link_service_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateLinkServiceName", []))

    @builtins.property
    @jsii.member(jsii_name="oauthProperties")
    def oauth_properties(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthPropertiesOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthPropertiesOutputReference, jsii.get(self, "oauthProperties"))

    @builtins.property
    @jsii.member(jsii_name="applicationHostUrlInput")
    def application_host_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applicationHostUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="applicationServicePathInput")
    def application_service_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applicationServicePathInput"))

    @builtins.property
    @jsii.member(jsii_name="clientNumberInput")
    def client_number_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="logonLanguageInput")
    def logon_language_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logonLanguageInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthPropertiesInput")
    def oauth_properties_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthProperties]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthProperties], jsii.get(self, "oauthPropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="portNumberInput")
    def port_number_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="privateLinkServiceNameInput")
    def private_link_service_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateLinkServiceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="applicationHostUrl")
    def application_host_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "applicationHostUrl"))

    @application_host_url.setter
    def application_host_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a805a2fd21027bb3b9dfb04f1b6b7401c6ecc1a5096dc53a4f70af0e35748c10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationHostUrl", value)

    @builtins.property
    @jsii.member(jsii_name="applicationServicePath")
    def application_service_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "applicationServicePath"))

    @application_service_path.setter
    def application_service_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be9a6f0db36efef994c5d2419bacd0008b566e1178d1518a6dce0420754558d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationServicePath", value)

    @builtins.property
    @jsii.member(jsii_name="clientNumber")
    def client_number(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientNumber"))

    @client_number.setter
    def client_number(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3526ddc869fbd8f3082e72d1390d93c04913568a3cc3fac625a76aee3cb2d4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientNumber", value)

    @builtins.property
    @jsii.member(jsii_name="logonLanguage")
    def logon_language(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logonLanguage"))

    @logon_language.setter
    def logon_language(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e04a6c72d4429569c1db0e7e01be02fdc0382be5b066cc550ac2aff112ed177)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logonLanguage", value)

    @builtins.property
    @jsii.member(jsii_name="portNumber")
    def port_number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "portNumber"))

    @port_number.setter
    def port_number(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca08f8921871885d473c90dbced3257b08bdfece4d58290b470d09f44e6ac42b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "portNumber", value)

    @builtins.property
    @jsii.member(jsii_name="privateLinkServiceName")
    def private_link_service_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateLinkServiceName"))

    @private_link_service_name.setter
    def private_link_service_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b757431f7b6895a3e1573ba049dfc4ce54c1e9d3cc7f3b093560a1ba22bdbc59)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateLinkServiceName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoData]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoData], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoData],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f4537be4165325784546f59cd4fe8790a98c3930a08c71ebbab9c0c452ee163)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNow",
    jsii_struct_bases=[],
    name_mapping={"instance_url": "instanceUrl"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNow:
    def __init__(self, *, instance_url: builtins.str) -> None:
        '''
        :param instance_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddd1a1d27273517aa401895ee907ea16961ea7f2af91f71b1dfca61087a1c50c)
            check_type(argname="argument instance_url", value=instance_url, expected_type=type_hints["instance_url"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_url": instance_url,
        }

    @builtins.property
    def instance_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.'''
        result = self._values.get("instance_url")
        assert result is not None, "Required property 'instance_url' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNow(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNowOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNowOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0359a443d5dd0213099250d0256a1b3daf75fb292d55869f7b2277915a9a18c9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="instanceUrlInput")
    def instance_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceUrl")
    def instance_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceUrl"))

    @instance_url.setter
    def instance_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8179f01f125b95df9b2299410e9833db16bba1e6ba2af301e6560550e2ce6c3b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNow]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNow], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNow],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b2d3c22febb4d209f5812a308a17bbea7f4a1582f4f572c4ad801105e2d8898)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingular",
    jsii_struct_bases=[],
    name_mapping={},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingular:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingular(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingularOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingularOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__499baf31df91ddee835dad617b8f519ddbfdeb046aeb814943f96678fdee3815)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingular]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingular], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingular],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea6593ac859da5c951dde2e6dd89641aeabb352c362660633e0f2711f79deabb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlack",
    jsii_struct_bases=[],
    name_mapping={"instance_url": "instanceUrl"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlack:
    def __init__(self, *, instance_url: builtins.str) -> None:
        '''
        :param instance_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccde0100d65c2ad565e73cc50d369adc6df45d1dcc2b93068378211a12b03a53)
            check_type(argname="argument instance_url", value=instance_url, expected_type=type_hints["instance_url"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_url": instance_url,
        }

    @builtins.property
    def instance_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.'''
        result = self._values.get("instance_url")
        assert result is not None, "Required property 'instance_url' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlack(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlackOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlackOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__746b08f719c2ab8bdae9f55cd484cb6e5bc46b31d8697e4a406326e0cd15157c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="instanceUrlInput")
    def instance_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceUrl")
    def instance_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceUrl"))

    @instance_url.setter
    def instance_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__937eacb6076c60b1c940592061a9473f1a0916844b8dde3e4c278861667d1cc1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlack]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlack], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlack],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3726ca4b6ea4e46237e3580cee9f740341a8b8328bfe3c106a9a6615df924467)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflake",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "stage": "stage",
        "warehouse": "warehouse",
        "account_name": "accountName",
        "bucket_prefix": "bucketPrefix",
        "private_link_service_name": "privateLinkServiceName",
        "region": "region",
    },
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflake:
    def __init__(
        self,
        *,
        bucket_name: builtins.str,
        stage: builtins.str,
        warehouse: builtins.str,
        account_name: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        private_link_service_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#bucket_name AppflowConnectorProfile#bucket_name}.
        :param stage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#stage AppflowConnectorProfile#stage}.
        :param warehouse: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#warehouse AppflowConnectorProfile#warehouse}.
        :param account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#account_name AppflowConnectorProfile#account_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#bucket_prefix AppflowConnectorProfile#bucket_prefix}.
        :param private_link_service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#private_link_service_name AppflowConnectorProfile#private_link_service_name}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#region AppflowConnectorProfile#region}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12110ad2ccd83ab20c614a173a9ccb40c939083531c9513f5c141ac798916bd7)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument stage", value=stage, expected_type=type_hints["stage"])
            check_type(argname="argument warehouse", value=warehouse, expected_type=type_hints["warehouse"])
            check_type(argname="argument account_name", value=account_name, expected_type=type_hints["account_name"])
            check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
            check_type(argname="argument private_link_service_name", value=private_link_service_name, expected_type=type_hints["private_link_service_name"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket_name": bucket_name,
            "stage": stage,
            "warehouse": warehouse,
        }
        if account_name is not None:
            self._values["account_name"] = account_name
        if bucket_prefix is not None:
            self._values["bucket_prefix"] = bucket_prefix
        if private_link_service_name is not None:
            self._values["private_link_service_name"] = private_link_service_name
        if region is not None:
            self._values["region"] = region

    @builtins.property
    def bucket_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#bucket_name AppflowConnectorProfile#bucket_name}.'''
        result = self._values.get("bucket_name")
        assert result is not None, "Required property 'bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def stage(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#stage AppflowConnectorProfile#stage}.'''
        result = self._values.get("stage")
        assert result is not None, "Required property 'stage' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def warehouse(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#warehouse AppflowConnectorProfile#warehouse}.'''
        result = self._values.get("warehouse")
        assert result is not None, "Required property 'warehouse' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#account_name AppflowConnectorProfile#account_name}.'''
        result = self._values.get("account_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#bucket_prefix AppflowConnectorProfile#bucket_prefix}.'''
        result = self._values.get("bucket_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def private_link_service_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#private_link_service_name AppflowConnectorProfile#private_link_service_name}.'''
        result = self._values.get("private_link_service_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#region AppflowConnectorProfile#region}.'''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflake(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflakeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflakeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__97a32d4adc97c5ebe8f336dcb1ce4751dc0369a6645954e7a538e2cdd0700a42)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAccountName")
    def reset_account_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountName", []))

    @jsii.member(jsii_name="resetBucketPrefix")
    def reset_bucket_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketPrefix", []))

    @jsii.member(jsii_name="resetPrivateLinkServiceName")
    def reset_private_link_service_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateLinkServiceName", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @builtins.property
    @jsii.member(jsii_name="accountNameInput")
    def account_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountNameInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketPrefixInput")
    def bucket_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="privateLinkServiceNameInput")
    def private_link_service_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateLinkServiceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="stageInput")
    def stage_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stageInput"))

    @builtins.property
    @jsii.member(jsii_name="warehouseInput")
    def warehouse_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "warehouseInput"))

    @builtins.property
    @jsii.member(jsii_name="accountName")
    def account_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountName"))

    @account_name.setter
    def account_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb34384ee7ac5382e631de2df59d7ca4dbaddd7907748370a235180258360ab3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountName", value)

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6cf1ef2f067856bf49c2f712e5ee398be4a12543fe2a1f6cf069c6e97da8ebf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="bucketPrefix")
    def bucket_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketPrefix"))

    @bucket_prefix.setter
    def bucket_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9d09e56a50b691174f3c309c64363e42db501b23bad5618169e87d824f6d2f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="privateLinkServiceName")
    def private_link_service_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateLinkServiceName"))

    @private_link_service_name.setter
    def private_link_service_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1f46802cbadba377c558468742833a120a7b3cfaa5daa12b756699b5affdeee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateLinkServiceName", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2dc52194b16160a42df24684ddfa6ca16db2b7018a3aba86143c12dff45c522)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="stage")
    def stage(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stage"))

    @stage.setter
    def stage(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50aa0ed6e3ade7b4f690ce37f5972d2756b87a146033ee419528ce1c02c58d81)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stage", value)

    @builtins.property
    @jsii.member(jsii_name="warehouse")
    def warehouse(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "warehouse"))

    @warehouse.setter
    def warehouse(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4286d581fbdfb594caa010fb8b4788676a538cad7660fe2265f998f2078cbaf8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "warehouse", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflake]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflake], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflake],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de59bb5b9162519ec5084031d96c5f9a76e0bdf8cdec1410dfbee8d3762b51cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicro",
    jsii_struct_bases=[],
    name_mapping={},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicro:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicro(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicroOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicroOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cd8763b19b64a0cd2649123fbb22709fbe2816f6bba9ebdbfa8754626f934765)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicro]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicro], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicro],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d615a065c53a4f50d67f579b9dae749c691b2fdb32c0e34ae8778414ff6e8295)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeeva",
    jsii_struct_bases=[],
    name_mapping={"instance_url": "instanceUrl"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeeva:
    def __init__(self, *, instance_url: builtins.str) -> None:
        '''
        :param instance_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4812be1d2cf756498b4f920794e7e6f275cad727a989e1e5d46813474597ee1)
            check_type(argname="argument instance_url", value=instance_url, expected_type=type_hints["instance_url"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_url": instance_url,
        }

    @builtins.property
    def instance_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.'''
        result = self._values.get("instance_url")
        assert result is not None, "Required property 'instance_url' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeeva(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeevaOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeevaOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__071db8336164eb1a5de852fdd1f5f6fc14bef322a58d98a708a70cc22580b4e2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="instanceUrlInput")
    def instance_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceUrl")
    def instance_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceUrl"))

    @instance_url.setter
    def instance_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e94f7b70b76b2cbac2014f8a994385764282df27e49f6a222370f982b2dbae7a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeeva]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeeva], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeeva],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__066106b5b18747be97471087d4e4381504998c205a316ed12b15b04de9c9efae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendesk",
    jsii_struct_bases=[],
    name_mapping={"instance_url": "instanceUrl"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendesk:
    def __init__(self, *, instance_url: builtins.str) -> None:
        '''
        :param instance_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ccba491011fc58ec7616d39893a4a2aa3d8b0a49c6120d97e23050bdd8e4c4f)
            check_type(argname="argument instance_url", value=instance_url, expected_type=type_hints["instance_url"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_url": instance_url,
        }

    @builtins.property
    def instance_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.'''
        result = self._values.get("instance_url")
        assert result is not None, "Required property 'instance_url' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendesk(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendeskOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendeskOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__10ca8ab25235ab5784f35b429210164f0e2c2a62cc349ed65db6fa9cea66ff15)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="instanceUrlInput")
    def instance_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceUrl")
    def instance_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceUrl"))

    @instance_url.setter
    def instance_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c089a38f7e3e07e6220566cf2e2f37e8ce2e3d578e89854ec95c4b3bb145013c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendesk]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendesk], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendesk],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ea448c1b86251710ff0c8cc17ceed9809dc59ae56956bbb11e420b7b1af6008)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowConnectorProfileConnectorProfileConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d8034f221b4a23489df70b3be0b259316a4286b0702e2567f1e16b6532a49954)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putConnectorProfileCredentials")
    def put_connector_profile_credentials(
        self,
        *,
        amplitude: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitude, typing.Dict[builtins.str, typing.Any]]] = None,
        custom_connector: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnector, typing.Dict[builtins.str, typing.Any]]] = None,
        datadog: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadog, typing.Dict[builtins.str, typing.Any]]] = None,
        dynatrace: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatrace, typing.Dict[builtins.str, typing.Any]]] = None,
        google_analytics: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalytics, typing.Dict[builtins.str, typing.Any]]] = None,
        honeycode: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycode, typing.Dict[builtins.str, typing.Any]]] = None,
        infor_nexus: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexus, typing.Dict[builtins.str, typing.Any]]] = None,
        marketo: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketo, typing.Dict[builtins.str, typing.Any]]] = None,
        redshift: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshift, typing.Dict[builtins.str, typing.Any]]] = None,
        salesforce: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforce, typing.Dict[builtins.str, typing.Any]]] = None,
        sapo_data: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoData, typing.Dict[builtins.str, typing.Any]]] = None,
        service_now: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNow, typing.Dict[builtins.str, typing.Any]]] = None,
        singular: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingular, typing.Dict[builtins.str, typing.Any]]] = None,
        slack: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlack, typing.Dict[builtins.str, typing.Any]]] = None,
        snowflake: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflake, typing.Dict[builtins.str, typing.Any]]] = None,
        trendmicro: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicro, typing.Dict[builtins.str, typing.Any]]] = None,
        veeva: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeeva, typing.Dict[builtins.str, typing.Any]]] = None,
        zendesk: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendesk, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param amplitude: amplitude block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#amplitude AppflowConnectorProfile#amplitude}
        :param custom_connector: custom_connector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#custom_connector AppflowConnectorProfile#custom_connector}
        :param datadog: datadog block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#datadog AppflowConnectorProfile#datadog}
        :param dynatrace: dynatrace block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#dynatrace AppflowConnectorProfile#dynatrace}
        :param google_analytics: google_analytics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#google_analytics AppflowConnectorProfile#google_analytics}
        :param honeycode: honeycode block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#honeycode AppflowConnectorProfile#honeycode}
        :param infor_nexus: infor_nexus block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#infor_nexus AppflowConnectorProfile#infor_nexus}
        :param marketo: marketo block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#marketo AppflowConnectorProfile#marketo}
        :param redshift: redshift block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redshift AppflowConnectorProfile#redshift}
        :param salesforce: salesforce block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#salesforce AppflowConnectorProfile#salesforce}
        :param sapo_data: sapo_data block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#sapo_data AppflowConnectorProfile#sapo_data}
        :param service_now: service_now block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#service_now AppflowConnectorProfile#service_now}
        :param singular: singular block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#singular AppflowConnectorProfile#singular}
        :param slack: slack block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#slack AppflowConnectorProfile#slack}
        :param snowflake: snowflake block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#snowflake AppflowConnectorProfile#snowflake}
        :param trendmicro: trendmicro block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#trendmicro AppflowConnectorProfile#trendmicro}
        :param veeva: veeva block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#veeva AppflowConnectorProfile#veeva}
        :param zendesk: zendesk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#zendesk AppflowConnectorProfile#zendesk}
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentials(
            amplitude=amplitude,
            custom_connector=custom_connector,
            datadog=datadog,
            dynatrace=dynatrace,
            google_analytics=google_analytics,
            honeycode=honeycode,
            infor_nexus=infor_nexus,
            marketo=marketo,
            redshift=redshift,
            salesforce=salesforce,
            sapo_data=sapo_data,
            service_now=service_now,
            singular=singular,
            slack=slack,
            snowflake=snowflake,
            trendmicro=trendmicro,
            veeva=veeva,
            zendesk=zendesk,
        )

        return typing.cast(None, jsii.invoke(self, "putConnectorProfileCredentials", [value]))

    @jsii.member(jsii_name="putConnectorProfileProperties")
    def put_connector_profile_properties(
        self,
        *,
        amplitude: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitude, typing.Dict[builtins.str, typing.Any]]] = None,
        custom_connector: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnector, typing.Dict[builtins.str, typing.Any]]] = None,
        datadog: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadog, typing.Dict[builtins.str, typing.Any]]] = None,
        dynatrace: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatrace, typing.Dict[builtins.str, typing.Any]]] = None,
        google_analytics: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalytics, typing.Dict[builtins.str, typing.Any]]] = None,
        honeycode: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycode, typing.Dict[builtins.str, typing.Any]]] = None,
        infor_nexus: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexus, typing.Dict[builtins.str, typing.Any]]] = None,
        marketo: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketo, typing.Dict[builtins.str, typing.Any]]] = None,
        redshift: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshift, typing.Dict[builtins.str, typing.Any]]] = None,
        salesforce: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforce, typing.Dict[builtins.str, typing.Any]]] = None,
        sapo_data: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoData, typing.Dict[builtins.str, typing.Any]]] = None,
        service_now: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNow, typing.Dict[builtins.str, typing.Any]]] = None,
        singular: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingular, typing.Dict[builtins.str, typing.Any]]] = None,
        slack: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlack, typing.Dict[builtins.str, typing.Any]]] = None,
        snowflake: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflake, typing.Dict[builtins.str, typing.Any]]] = None,
        trendmicro: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicro, typing.Dict[builtins.str, typing.Any]]] = None,
        veeva: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeeva, typing.Dict[builtins.str, typing.Any]]] = None,
        zendesk: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendesk, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param amplitude: amplitude block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#amplitude AppflowConnectorProfile#amplitude}
        :param custom_connector: custom_connector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#custom_connector AppflowConnectorProfile#custom_connector}
        :param datadog: datadog block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#datadog AppflowConnectorProfile#datadog}
        :param dynatrace: dynatrace block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#dynatrace AppflowConnectorProfile#dynatrace}
        :param google_analytics: google_analytics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#google_analytics AppflowConnectorProfile#google_analytics}
        :param honeycode: honeycode block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#honeycode AppflowConnectorProfile#honeycode}
        :param infor_nexus: infor_nexus block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#infor_nexus AppflowConnectorProfile#infor_nexus}
        :param marketo: marketo block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#marketo AppflowConnectorProfile#marketo}
        :param redshift: redshift block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redshift AppflowConnectorProfile#redshift}
        :param salesforce: salesforce block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#salesforce AppflowConnectorProfile#salesforce}
        :param sapo_data: sapo_data block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#sapo_data AppflowConnectorProfile#sapo_data}
        :param service_now: service_now block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#service_now AppflowConnectorProfile#service_now}
        :param singular: singular block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#singular AppflowConnectorProfile#singular}
        :param slack: slack block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#slack AppflowConnectorProfile#slack}
        :param snowflake: snowflake block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#snowflake AppflowConnectorProfile#snowflake}
        :param trendmicro: trendmicro block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#trendmicro AppflowConnectorProfile#trendmicro}
        :param veeva: veeva block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#veeva AppflowConnectorProfile#veeva}
        :param zendesk: zendesk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#zendesk AppflowConnectorProfile#zendesk}
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileProperties(
            amplitude=amplitude,
            custom_connector=custom_connector,
            datadog=datadog,
            dynatrace=dynatrace,
            google_analytics=google_analytics,
            honeycode=honeycode,
            infor_nexus=infor_nexus,
            marketo=marketo,
            redshift=redshift,
            salesforce=salesforce,
            sapo_data=sapo_data,
            service_now=service_now,
            singular=singular,
            slack=slack,
            snowflake=snowflake,
            trendmicro=trendmicro,
            veeva=veeva,
            zendesk=zendesk,
        )

        return typing.cast(None, jsii.invoke(self, "putConnectorProfileProperties", [value]))

    @builtins.property
    @jsii.member(jsii_name="connectorProfileCredentials")
    def connector_profile_credentials(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsOutputReference, jsii.get(self, "connectorProfileCredentials"))

    @builtins.property
    @jsii.member(jsii_name="connectorProfileProperties")
    def connector_profile_properties(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesOutputReference, jsii.get(self, "connectorProfileProperties"))

    @builtins.property
    @jsii.member(jsii_name="connectorProfileCredentialsInput")
    def connector_profile_credentials_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentials]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentials], jsii.get(self, "connectorProfileCredentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="connectorProfilePropertiesInput")
    def connector_profile_properties_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileProperties]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileProperties], jsii.get(self, "connectorProfilePropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfig]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f26954a025c4d30f8d2418a0267a4e1242caed3b0a51ad265f0d359ffd967ff1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "AppflowConnectorProfile",
    "AppflowConnectorProfileConfig",
    "AppflowConnectorProfileConnectorProfileConfig",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentials",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitude",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitudeOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnector",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKey",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKeyOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasic",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasicOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustom",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustomOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequest",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequestOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadog",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadogOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatrace",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatraceOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalytics",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequest",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequestOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycode",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequest",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequestOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexus",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexusOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketo",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequest",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequestOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshift",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshiftOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforce",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequest",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequestOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoData",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentials",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentialsOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentials",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequest",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequestOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNow",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNowOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingular",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingularOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlack",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequest",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequestOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflake",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflakeOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicro",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicroOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeeva",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeevaOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendesk",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequest",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequestOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileProperties",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitude",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitudeOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnector",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2Properties",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2PropertiesOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadog",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadogOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatrace",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatraceOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalytics",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalyticsOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycode",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycodeOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexus",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexusOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketo",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketoOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshift",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshiftOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforce",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforceOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoData",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthProperties",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthPropertiesOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNow",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNowOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingular",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingularOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlack",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlackOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflake",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflakeOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicro",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicroOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeeva",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeevaOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendesk",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendeskOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigOutputReference",
]

publication.publish()

def _typecheckingstub__467d06a6c034038a3200e65f379a2c2642aff6f0cb2d8b9acdee2f4c137bc6e9(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    connection_mode: builtins.str,
    connector_profile_config: typing.Union[AppflowConnectorProfileConnectorProfileConfig, typing.Dict[builtins.str, typing.Any]],
    connector_type: builtins.str,
    name: builtins.str,
    connector_label: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    kms_arn: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__7cc9dad6f882df50531a264399a3516926eebaadf513e236079a07b51c363322(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c85b96dd9f746ee3ec96f47733b7533ece6b7ac1f0ce5852e4295975ad54752(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b98b72d8a3796a31081ddb1fedd031297745ca53ce775166902fed1e27c2791(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d8b80377bbc42cf1f08b9bb65421d4cf86b1a99ba2e2308a04318dd90ef3475(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__becdf48c4096ee1be7f9bc532ce34c77a2aaebcf0f527c9f96774d6124a1639c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__138e14335d269f31264505cb3ea26174c6f40b50817fbe2572da24792eadd118(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54e8cda6287b9fffb8989744b68315dcd075e93b7cfd087fd73de262fb7fc5e3(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    connection_mode: builtins.str,
    connector_profile_config: typing.Union[AppflowConnectorProfileConnectorProfileConfig, typing.Dict[builtins.str, typing.Any]],
    connector_type: builtins.str,
    name: builtins.str,
    connector_label: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    kms_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__258944cd6bb6d386c7d2a1f0fa509fda676023bbeea260fe98cf931c61011b78(
    *,
    connector_profile_credentials: typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentials, typing.Dict[builtins.str, typing.Any]],
    connector_profile_properties: typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileProperties, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b8482bdacb35fce0c59fc8a0887304b209695f7230bec55e3b5d7fb9ee5e0de(
    *,
    amplitude: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitude, typing.Dict[builtins.str, typing.Any]]] = None,
    custom_connector: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnector, typing.Dict[builtins.str, typing.Any]]] = None,
    datadog: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadog, typing.Dict[builtins.str, typing.Any]]] = None,
    dynatrace: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatrace, typing.Dict[builtins.str, typing.Any]]] = None,
    google_analytics: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalytics, typing.Dict[builtins.str, typing.Any]]] = None,
    honeycode: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycode, typing.Dict[builtins.str, typing.Any]]] = None,
    infor_nexus: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexus, typing.Dict[builtins.str, typing.Any]]] = None,
    marketo: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketo, typing.Dict[builtins.str, typing.Any]]] = None,
    redshift: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshift, typing.Dict[builtins.str, typing.Any]]] = None,
    salesforce: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforce, typing.Dict[builtins.str, typing.Any]]] = None,
    sapo_data: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoData, typing.Dict[builtins.str, typing.Any]]] = None,
    service_now: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNow, typing.Dict[builtins.str, typing.Any]]] = None,
    singular: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingular, typing.Dict[builtins.str, typing.Any]]] = None,
    slack: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlack, typing.Dict[builtins.str, typing.Any]]] = None,
    snowflake: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflake, typing.Dict[builtins.str, typing.Any]]] = None,
    trendmicro: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicro, typing.Dict[builtins.str, typing.Any]]] = None,
    veeva: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeeva, typing.Dict[builtins.str, typing.Any]]] = None,
    zendesk: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendesk, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80dc6355640dc7b28d3589f2161d3b2e8f9d57786fbacf9ab6778cc9ac099b00(
    *,
    api_key: builtins.str,
    secret_key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30b2a831eff9499a5dde409e1b7b77ed0511cdb95061d60f4cd4b1bee95291b6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b954fca3a1ba6234a0230cc40af7b2a343c326a94b7372742a8c3f8533576920(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2d1ef5dc9d1324e5bca694a2db9a56d2e412efd2ae782954467d666e66cd06f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36de010b0d6b2b3267c1e77ea835dec7a7e16f7612c8adb760c3aaea28c2f0a9(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitude],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2e1f157108fbcbf97a52e272c3faa4c969a6ce4b673b6e3055a467386438a59(
    *,
    authentication_type: builtins.str,
    api_key: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKey, typing.Dict[builtins.str, typing.Any]]] = None,
    basic: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasic, typing.Dict[builtins.str, typing.Any]]] = None,
    custom: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustom, typing.Dict[builtins.str, typing.Any]]] = None,
    oauth2: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cbd7a8c0343b3065d53c4331b2a421fb528545de1d166649e6b55a05ece2b9a(
    *,
    api_key: builtins.str,
    api_secret_key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f86fc09f574869766b1c468dbfe70aac2eb601611c399479f13df06a6bc779a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__552b3a8c60115ab9c655c7d4be8e137e2f0cb5532cc5b7530e1e80adf8332d24(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24ac690f4063c8b9fb71f1c9d54d50ee26d74131f06dd06f01a4f9cb3b5e0eb8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd59fe929ad04e61dc16a5ba09d1cacb52edd16be0e8ccbf0315cc5dd7c772a8(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKey],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d4b2d2ef86af0a51a9a518549a33921c93923394213a80c55dd989713e62e4b(
    *,
    password: builtins.str,
    username: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c2318212120443d9cc650795f04cb86f935806720681a036c0ccd4ef54ef716(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aba4dd4bb587f70db19e55176395c2386c00d8a1bc7285c26772fec053168cce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7c78864dab2ef39a9b7d8876d8ce917d45d7985cf4c3f3ee4603b7878af842e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__022045c0cb00c1dc959cd7f4fcafe0194808e2e7fb71099a57fb30a1bf3e8be9(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasic],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94afd2390fb7351382086adb0166647abd98d648536688e00a92c76b68b4b0ab(
    *,
    custom_authentication_type: builtins.str,
    credentials_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e1c7c66cccd4475cedfc818fd35ac791f7cfffc109f5607795a158db4b48341(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9402c95209d848ad39902fca313a2883143ad78bfa3bcf9e200818378835e2c9(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34c6b41d6702476637538132327652710e4f7b567e30e01e5c4c4d718688c55f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4c803641f41d61ba5d72358fb532862c2078669f07e18815f9cc1645ed2cb45(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustom],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af28b6af78b0a60ef8c3f74185788e5aef77e0c15995eb935da5d2911ed393da(
    *,
    access_token: typing.Optional[builtins.str] = None,
    client_id: typing.Optional[builtins.str] = None,
    client_secret: typing.Optional[builtins.str] = None,
    oauth_request: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequest, typing.Dict[builtins.str, typing.Any]]] = None,
    refresh_token: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2479ad553e3db9cf7c36aba2b86f8673a508e514fd1297675d5c3d1b1232d6a2(
    *,
    auth_code: typing.Optional[builtins.str] = None,
    redirect_uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f76a4839555202c3411b6be7e0bbd03a3a1a9868560b25606521ca335073fb0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__663c6adf32f8e6605263787cb926260829902981363e72f183fe1eef664e08ee(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5884a3f7af422b7fa7bee2ba3674d961385e23dc4778dfddd5576bfb720500f9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7dcc5c1fde74871448da356ed480b8774071c38e5efdd65b1ff49930babdcf4c(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequest],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81f514d01bd9a036e4084acd88ebfbd30f2d19c8fb6e4f3ea0ea33e41113840d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44851f56f1a97eb1a07fefc69654bbb5602993a68ebd50437ee47f391f6b7981(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea8bbba5acd0b760fcdd6674c5cb69722a8b42942471208a4e00869f0f80fa5d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cf671349aecc891150e705abccaea63122498cd63001b3ecb0ad748e0c2db42(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bf35ee5c8c1ebc7838cb0791d21c85b5e34627b5ced33d87f9286bd15e808c7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35729fb13f908bd160a2f77d3275cdc622335462d69287183b123a4e54d063a7(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a32fc211edd3db9575cf2ecf24bfb1b9039e5d136fbb7d05354e85c9a21de82e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9d9436561df75df4de1113ac1864f3778441bdd99b04cad4bdea0eb4fe707ac(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9104533818b8d31a5462969a0dc6b3ede080b08152e3cd3dfe8b13c6f87f6186(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnector],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76cceacfcce609f35f018cbd20125e03c7becebb977c784dad28ebf94b5b026f(
    *,
    api_key: builtins.str,
    application_key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf7d62a861681a7bac83b2366e5a346c4be9bb070d838e6ec77a9420bd33b505(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__798c10ab6f86a6022638f85875253c3b26abbfcb5085e4b02af979754a94d2b2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__344e8b6a6a7b23a342d0652be4276d4b5999386b3b30e7b34fa168d785a68afc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba344cd4f3bfc4273fc53db3a93a4de4fa052712031cebb06eaf64f8e2bd6545(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadog],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__358e6f20c136071ed498a406a422b41ce3c3b7916057dda25f428d130fe35030(
    *,
    api_token: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99049168d99d7970cdcd8ad048bd9e864c83fb6cb1605c3bce034a2cc8877dde(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9747717c1dc28b298d3827fe812522633f477863d50ac33627f139524fe49de1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6883891ec1e115b322ac9a05552b1a8b9efdccdda67b2824c16bbe93b508fd4(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatrace],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__755a66fd23787930c9d972a7eb066940b1cd68196c05e29ac05bd0b4e1430158(
    *,
    client_id: builtins.str,
    client_secret: builtins.str,
    access_token: typing.Optional[builtins.str] = None,
    oauth_request: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequest, typing.Dict[builtins.str, typing.Any]]] = None,
    refresh_token: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__623fbed82966657247b3d4964998827825e51e3ae007483e0023aaa75bb1bf39(
    *,
    auth_code: typing.Optional[builtins.str] = None,
    redirect_uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3492bcc0c0e95908bf9c6a16e55e8439db3030f5e1bdb1ca298d86e48de95615(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d534b8da128c51abdeafadaf48253b635c99b86c2b13f774c35d6aa4ec65d4c2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afb9b7c1d3643a644d5cfd2601243e6f5b81e3772c1a844da31d945b7985791f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bc5282e0c3b572e7ff6e30640ae3eabe9d80c5eab9ef6aad3c3b0c783c40f33(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequest],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62645b32e596e510bdaf802520ccf9088ed18c48d033cf8a79b19dfef46baec8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cbe109c7f4994d8152430635d045f2c84f136803a6d4ebe904c1af2e7ac8a9b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23d3b1fea0a699ad81e0fd38172c4cc5e1d1bc139c7a5fa793855367640986e9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e403d357f8ae5e289c17198fdf54abbeae333f20bdbbd79cb4f72e0f23305e42(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9513dd1a6cf5c98a8cf6c72caee8c574d48cfbe966efd615d28f5ad6a3a4e2e0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d50c8a22d1755efd664fe0edcf6fdd270512ed5fdbd332e0b7a8f9561a35d86(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalytics],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15f2ba7ba11ea1f63b58d287cc74b9a2fc16a1be1abb559cb7e5f2bdc7c9d271(
    *,
    access_token: typing.Optional[builtins.str] = None,
    oauth_request: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequest, typing.Dict[builtins.str, typing.Any]]] = None,
    refresh_token: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__891826f62d5ba8de245a53c065f25789d4e8997311d10fef4a54920c18257419(
    *,
    auth_code: typing.Optional[builtins.str] = None,
    redirect_uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e9e290eed65104bac368b32e2ec9b79ba2dd317a3156178adf3ff208930b78c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8af7b9499406d7ddb533845b7dd61f79e85c3dff16d38a5ea55302d9c061547(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e111b3de83493aa2a5a113f338253cbf261298ddcb4990f0fe6b12ca81460ef(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__977759a1481045cf5d2216e0588418dff35380a0dbf3db47dd8519e323079af3(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequest],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0757aa39c21db62005386b06f33b4d8394bfafb1b2bd27936f472fd911efacaf(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bcda14dea3afa4b5ef5a194c7da2123ea7b7cd0dea0f50bc89a9fafa857244a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2f767823c0b5700e9980ffb09ab16c11c4c9ac4f614fda26214a29e6b8bf04e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2559e8f2b37921dbff7d02b228b6a8be69cfeba1f3b8d9d8f9c66026536a10ca(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycode],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1cdb791c31c9000b9e446294d82216a85dbfff20e48f5797a9a5d1c39227031(
    *,
    access_key_id: builtins.str,
    datakey: builtins.str,
    secret_access_key: builtins.str,
    user_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73cc6cb656c384b019813169cd70f7f19800e0226531ce39d1074766d88b9896(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__646bff31e9c436ef46c97ec78ae722c89a618486877f2246c1ebf87d2b956972(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da0fbc14e3064895074e97c7224ec4421027137e24466cd64a9974298f0f58c4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae944892a1fbe5b5ddf455de169c6001b0010eee7eb7cb271ae1fbfd8d1460f1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__072f5b723415c40d8a695a8d81c08fd0be691b6475e6ef213ad85f08880c60d8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1294d360fbcd349d2fb817a5c496fb0a84ccaf9403cb5caa6cdf62cda9d9bd95(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexus],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8509a0f1442b61dca4f3a1dcb0759b821b4b79c9aa2d1401d9400505c81b2d5c(
    *,
    client_id: builtins.str,
    client_secret: builtins.str,
    access_token: typing.Optional[builtins.str] = None,
    oauth_request: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequest, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecd6627ed4bf57528f035700e5fe6c9a8f487b5b8325ea78eadba0b1be18ef05(
    *,
    auth_code: typing.Optional[builtins.str] = None,
    redirect_uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__956b70819122bc6083c2e31115ccff5b700eb7491ead09479254733289d24c25(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b8898b53437a49f74847aca6fcd659248879b6e01355cdf5d8fa448144666e7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29ba99cac108d2d9d3e52f741fc2a5092e400981d0d65660cf76e83a8c617d88(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2120f483e64e53deb9c8531d8f05868c69ea2a2dd8d8d06d2e353cfc46b20e5d(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequest],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01b2d8a1157f2dcde07ec68016aaeb45553730b4bb5fddc69e639b73368d15a8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1358939f075cf7a7dfe1f97fbc56c0cd6ae4006be321c88b0df2d2f8694cf058(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bdf27f9c9f4fdc489279e195fc55636003b57a7021966e1c7f904e04ef2edfd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b56d1b91c0a7394131d2988b4e9554ae6b86110fa933968cb3510b00e2548f9b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__380646869b6151c91444e4b3aea656ea8e9ec863a8068e5a4947bd47d58027d0(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketo],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de2b931eae7011d8628c604f26e2dfefb5f3d4df7e4d0e42d8ed8c07041c8efc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e5e90b5dc1a66c46600bbb752c1137309661a2e984fb8abc628a7708b63965e(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentials],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbe7d541f38235c6d4c8cc7a563b5d773c35d092954fb0a131dde42517814690(
    *,
    password: builtins.str,
    username: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cd13f73147d5167d4bdd46c9d206b817951fb2be8b357cc2c8d52ade8bb0009(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2eff0027297184fcd9d41a8739ab90da0e1d09aa344d5d07870359e0deda86eb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc49328371a8f30bc7b0f81266b44c7cc03131995c6676873496e982c07cb92d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d96063e3ff1e33b618948a3fd9f0bf54b19e07dfb8af124411f0bbddb8e3c86(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshift],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84145676624144ce4ec85ca32d9b50447170aeda7a0493ee7e2cf4b4a025d99e(
    *,
    access_token: typing.Optional[builtins.str] = None,
    client_credentials_arn: typing.Optional[builtins.str] = None,
    oauth_request: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequest, typing.Dict[builtins.str, typing.Any]]] = None,
    refresh_token: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__365dc022282d1548bbf989b43b8cdad26138f7d81a705e487c49a9234235bcf3(
    *,
    auth_code: typing.Optional[builtins.str] = None,
    redirect_uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__155f16ad4526aea57e46fed2efcbc12395f0806d08965231be521424a5ca6a13(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab8fdd861d28804dd63aa9ad3828d563409f6abe2e2447f17a843b368a343d2d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff9622cc5ecd7052fe94dd204c7ea550091056176a556fde910d8fac2464dde7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1e27239514e40b088dbcb2ea5a11683379b6c26b4943bcb969359ed8e08dcb6(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequest],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a15ea9480e99a2bc4c5931197f5313ed280ecf51a148a1be2f8c9413adbe556(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66a56b8f047f79d6007624fb56ba9612f3a17a0a2762adbbb03516f1e8d460f3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adfb01011493e4fa3ac0eb0a0fc181d7ed9b26ec8495cddf66bd0cc406642641(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2b56a333ba2f3a02b8af8df18b6af946c2e37ba528692fddc83627d31d1ff82(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24790825786a4a20eef3f4bd40b46b095b985cdbacf8f2e28d063f565af8869f(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforce],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3da20e636399312a8cd3c5f0c1fda6ca69b866c41a53dd76fcb64e03fc0ec7a5(
    *,
    basic_auth_credentials: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentials, typing.Dict[builtins.str, typing.Any]]] = None,
    oauth_credentials: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentials, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c8046c6ebf75720c30113c2717257b68dd9635915fc686b2257f414b8fd587d(
    *,
    password: builtins.str,
    username: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef1e10c5270dbfe808da8dcef1cadef57595774bc28629d6491f65958acb5ff1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0601c6444b29c1d33e6762afbab5fe0fe7f5e6cf250e309d364a08ec8f83f27(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d19c1e3af0506e135fbe702a313870f21ae6821f14ac4742aa9d5c0f672ec1f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e12ff8604dfaba8bed8198410efb4302457ec31444664490c3af3ed2f0317089(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentials],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ccda68882ff6b953e86a32e097d3ac0c4d4b9fe1d7726df55384da479b4984f(
    *,
    client_id: builtins.str,
    client_secret: builtins.str,
    access_token: typing.Optional[builtins.str] = None,
    oauth_request: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequest, typing.Dict[builtins.str, typing.Any]]] = None,
    refresh_token: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e8ff2b6067a9d67dfce3cf5d9e490e92dbc5ed5b57a50e0cd3e2733895c9c8d(
    *,
    auth_code: typing.Optional[builtins.str] = None,
    redirect_uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e8deedd82cf2d078fdf88f7397e94e73bdd4a4f465bd63b8f9b668f73a23025(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a70707b1ece55dbac16d5dccae190efbfb65ea872c5c7b881f81797ff6ea504(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3f776a2c2a3796b9677a6d4454746989600b545009130c033a6fc3937ddebca(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7cf7d225c7f7199c6d9b87c63aeec0b49871181495fdef28176d9f9222b1dd1(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequest],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4c29f53c7cae77e8d9f5e4b905336bc3c6757c081e941538f07533fe114ee12(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ecd2c480c0e84594327772ba200b77a15bf7f34dfa0e4dd829592d833f1608f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d16bb221c7d9a72b0b8505c1d92a3b9d8d305bb90d745f58f94d75d1275c23d5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__586edceb6570a5243cc668f388e2a1aea38d10bcdaedb0a2981b0db208435c7a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84b4f07d02c44cbc309e3b3a118c5139984a19341784e674bf970123b6df4569(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bd3c8f38f15334b50c6dee2572d629719a97c5cdf0fd5b327e906ce9d59ad97(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentials],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c74a13fd85208f92cf7263d11ec98af16a3b9f43fa08f7cf74c79a69d405668e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c417d37d0230cbdef357b0a4edb463162169efe8ffa720ad1f882c3348d17d5f(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoData],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8161665b61e4e766698e0733be69186cfa9543d16e10ee91400a002eb44ffa59(
    *,
    password: builtins.str,
    username: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1048b7d35c229c443f549d9aa842c04e034d0fc79d6f478cbcc36a604cec520b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eda4d14e1330ba114091c044b478a398e778213b1bb6a4789535104d3970fbaa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9a1c21e1ba9348c0aa231677bc72b9ff5ff240f1f1cc69de49a9b7e2a608e41(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e24edebbfd1bc29125b859d3eef8b6bf2775e9b7d626d54971ae70321043ebb8(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNow],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ed9e86581f2c9c1993a5f89d08a358759f6ea1f702a83c167dfe0c05b0e1dcc(
    *,
    api_key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1ed6e48f850bc1a0438179e429897a82f710e0f57f72aa86b054ec5b750592f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__455459e293f59727ac6a524bb17e91793e2eabdb6b99b3f7f6e078d7dbd690a0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d735216c0ac159fe783b40617014ba323b47e6d3cdf8b5dfae2ea7e972c8f5c(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingular],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b92a387285c6ac027f11588c488093e438e8045d3f3fde055af5d76d94795aa8(
    *,
    client_id: builtins.str,
    client_secret: builtins.str,
    access_token: typing.Optional[builtins.str] = None,
    oauth_request: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequest, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1b2d3f0f783d3c14b2e557626d3438ac1d4a03a8dbecf7d31efa5bbbd5dfc59(
    *,
    auth_code: typing.Optional[builtins.str] = None,
    redirect_uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a5cce45b9a9cda969c3a5531254035f193017bad6919685b04b29a5c5d18912(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f4840a4b154a03f27d67b4dbac2fae30e631ff77de44d79e9464d73af6c8266(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__697122a95f28cb4ee8c39d01d10e696e421d97764c3567d04867ce07a8ff2a35(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ae7aef5f5dcd9be8e4409457b20ccfd95339c6dbde51d29e155cf4710af00de(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequest],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57eee686173541dd0da989fb94f2048bb3188e3e7bca89ac21d5a2ad47d6630f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83add6225362b559f57a9baa287f7a87c7417d9663b1798dcdaa9bf4ffcfd27d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abd788108ed717984391d57a1c3310e17929610170661abc03dc778c7790e5d9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c96fb6cf4092006970d7ffe1f9a6b57838c94e896be72361d0d6ce3835f09b92(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__535c0972747c46a9eba87781bc2c3952c0648e2edceffe8fe6ec29a7ab092dac(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlack],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d5f2a98c83fefb76667b869bac2003a733a0d620fff522b04d45a05e5802cca(
    *,
    password: builtins.str,
    username: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39434e59bcef530340accf11db836380ad163710c2511ea135045edeb37ad641(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ba6c779d09cfacb86abe80f0bf3c569d12d93a44638f0ae89a0ad1b216f7eab(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__485ad44a4566e35cb6db17e724e99de719798e5c00a370b1f0e65b86ebee78c3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bf663abd48b10315850db14618fe530b39666be898c8fec90af286f6780bbf5(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflake],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7103d2d524ef96829700b9d6a943416d9dcad9e8913ea45675dbdbf7342189e7(
    *,
    api_secret_key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef86b35e4616a43670363ff082500cf2fc919f1298a7f4acac3e049154870d02(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0403cb56945d509090ab828c8f598790a403f01cb1d5216007bcf4b101929481(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58cd8f016fa4b0dcceb6dd8b1f02ea0c1d00f95399074672c938d22e0f1f68a8(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicro],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6135392831d8b46af3ba92e5cea748b62c2066690ee20ecc21b42b7c4b8bc793(
    *,
    password: builtins.str,
    username: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c695a1142cc82518e0ba122a483f00fe3a2f51a1c8d0980b108f7f8def384557(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b529e54829a8ecc0ff1800f5442abf9f32e5633c37e155cead72c4737e9c771(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5eac0080395fc849edc3caffa6847f40c957c41e50828dcbd936d2390934d8e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b30dd3f6c9f77d3f64ab9106c3bcb8ac31a3cf66aea7a9af81b09b51aafa7c32(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeeva],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30f9f7594f5c343c71e65317ca8798cc3fdb2d0dff78364ed621780319503c25(
    *,
    client_id: builtins.str,
    client_secret: builtins.str,
    access_token: typing.Optional[builtins.str] = None,
    oauth_request: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequest, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f80cd07527c0b46a36283175c5a6211100a5be471664e370e4f93d7665d88a1b(
    *,
    auth_code: typing.Optional[builtins.str] = None,
    redirect_uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__160bdec4d558f7574581713587da129c8900fa559a44d4c50d76ee5754430b2e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc7ebdd14a4f0af96b24f3b8584c1d13e2d4df2278e3550345d4397a2748c896(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d17fe2a9565f430ba6e6b86de7b2cb442a3aeb4567970f5dd6adc9325d26f2e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6f201ac08a4cbd8f282c13a5e0a97ce587434a5e398b33ecd137cdb6fd26dcf(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequest],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f781554f4404d9a2e50d06d7c25764ba92c6ab13c9d2685b8418755eb803ad5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2dd96d5b9973fccce57105f81cb834321e64e8fe8e75bd0acc4c1e1a5cd737b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be117183e195a92b56e8649f1121b287048d0bf7e19b103d112791c988e68fca(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2de3369b7582014c91298678fcad50d4b14f78adea14f9f77c39028f10732f3b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__601b137464027d4541b3794d631236531fc84aab78aac3a500578cd07116a744(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendesk],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b095b0281163a9aa16ec538c5b8ba02a63894fa181bb0385dac56afa1cd354bf(
    *,
    amplitude: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitude, typing.Dict[builtins.str, typing.Any]]] = None,
    custom_connector: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnector, typing.Dict[builtins.str, typing.Any]]] = None,
    datadog: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadog, typing.Dict[builtins.str, typing.Any]]] = None,
    dynatrace: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatrace, typing.Dict[builtins.str, typing.Any]]] = None,
    google_analytics: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalytics, typing.Dict[builtins.str, typing.Any]]] = None,
    honeycode: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycode, typing.Dict[builtins.str, typing.Any]]] = None,
    infor_nexus: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexus, typing.Dict[builtins.str, typing.Any]]] = None,
    marketo: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketo, typing.Dict[builtins.str, typing.Any]]] = None,
    redshift: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshift, typing.Dict[builtins.str, typing.Any]]] = None,
    salesforce: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforce, typing.Dict[builtins.str, typing.Any]]] = None,
    sapo_data: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoData, typing.Dict[builtins.str, typing.Any]]] = None,
    service_now: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNow, typing.Dict[builtins.str, typing.Any]]] = None,
    singular: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingular, typing.Dict[builtins.str, typing.Any]]] = None,
    slack: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlack, typing.Dict[builtins.str, typing.Any]]] = None,
    snowflake: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflake, typing.Dict[builtins.str, typing.Any]]] = None,
    trendmicro: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicro, typing.Dict[builtins.str, typing.Any]]] = None,
    veeva: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeeva, typing.Dict[builtins.str, typing.Any]]] = None,
    zendesk: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendesk, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba4d2d65160c2edd979d5cc81b5f8b20f62041035b8403e73e10d7458eb55f03(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8adf04a8d653cba12bb0e28944c3939c2922b2a8f05ace3ade6a6117d1585b34(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitude],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d735c7784dedc6080836402944ffec29708ce67287efcffb600d0ec903e949c0(
    *,
    oauth2_properties: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2Properties, typing.Dict[builtins.str, typing.Any]]] = None,
    profile_properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c428d7813185e7dbb983325c3310947e8c9467e322f025d663c9490c4472c750(
    *,
    oauth2_grant_type: builtins.str,
    token_url: builtins.str,
    token_url_custom_properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8c195f1db511dc39ec2cd03f198b38be1baa93238f7bf71f30440736bd3a5dd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7aa2f72a395e707e0c6f1deaf9e4380afd5cf262dae76c26d2ee0627f8b13d0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0402e2a9f616c894519e94ceb309634e7d9727104083a6c2cb40c4b6c033546b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c234a02476dcde2e8a5215b49aa791878c7957e0b131b7d0bd83553f7930fc3e(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f1d50bdc03600452a98dbb28086b4775eb947ee6226b44d91f39f6921625862(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2Properties],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1393c48b095a98bc707d1ddef54d2bbca16d8038627bcae446cff9709c78a00c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adbaf6447758029d65dfba3d9ea81a97d76346766525a8852a8e34c5069944d6(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b8dabe1fb4838c07916bdeeb653a5a0df4cc7397fdf98a0c4bbb0bdd27bb645(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnector],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f9ff553621c8acf7a9ce8e6e36ba25b8b6f76fd9e20404e25d78741857904b4(
    *,
    instance_url: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fabd4fb9581e954774ddb7b48c04445e1c597d20ad572fb8c3878afa2c7be06(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ef25d3708d51c7b4459e7734a4016e43e5e85ade421a0a810b3c38f3c637d73(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33e67d586390cce03b87d683d97f4c302d078cdbfb757dd02bc90d9cb7223308(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadog],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3db7f25cf6ff1568fb8d5248a042751d36cf73a0d078e8c77155eebd5e2a5e9(
    *,
    instance_url: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92673e9fbd5482e4d9d5dc0f0428a902ed43bc11022dca98abb858ac2cd10411(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd66ec29cc91b0ed72dea300ae13cc03be6952fba3b7d7b27ba09b590e1fe052(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aab62bf3214dda510e57aa201f0249045dadd555d05713071c17addc05e16e02(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatrace],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__333a727b9de094b70dc75a07cda39bcbe0a53b6a4caec8ed91402b880e721fa3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__145cdb9f89a64dc5d8dedf5d142b6c53f632029846460568fc784fc900b6078e(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalytics],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d99e408ee8febbacde4c6a4212f7abccb877828ca2fee67916ef8d60426dacf(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bde9bb90ce238cd6f8ccc9b37aef18167b63be7a6a9ffc9a51700a0ef9b22a82(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycode],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb2b60470aa27b1cd678de80a41e87a6dc01e2d89859f784d7aa081b31518ef7(
    *,
    instance_url: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c8f1e9cf07557edbb5dfe0776014a9f99852920f637be689057eae2a3021eaf(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37452a1dfffbabb264905848c4295d984c1cb3d835b6aff1b1a12d091edce208(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afee05945d3d6533227512067a4876bff3bd94986e7edab846881a41807b0eed(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexus],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8cbabd1b50d26ce8113e7b683e77486be1708c6ffc521039bfc34614a725d7c(
    *,
    instance_url: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__777a58e585385f1e74de27c4d52d50c7946b1f4148e7389b06fbb7acc87faeac(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e3718e4b23411666d3fc2f3129957cd5fa5ca5eb874b90ae842ddacbf6efc38(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d089d26949ec6e66c601e16a455cee96ed2b8cd6632aa321ff6f6d27c183136(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketo],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1dc721ff7ea8d3063e365a1a5a16a04c162a2c89964d591b0b703b8678cd1cef(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ed69841c6b68fa04e0d5ee8cf418eb5017960e1510a68433990ec95c88243bc(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileProperties],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba8cc6740904e61b2f58eb5b9f8967e620f704bdf693edbe096caa0cc07b2823(
    *,
    bucket_name: builtins.str,
    role_arn: builtins.str,
    bucket_prefix: typing.Optional[builtins.str] = None,
    cluster_identifier: typing.Optional[builtins.str] = None,
    data_api_role_arn: typing.Optional[builtins.str] = None,
    database_name: typing.Optional[builtins.str] = None,
    database_url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50415ebbbfa0e3b73cf633e209a1622a7111ec865edfc8b6ef6b2819068e9868(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbfa34014b9f252e9b080336dd7331345bde2bee3d9a01ffed4bbf39b651a143(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0d2be1a9ad3696ed462ff94f8da76b6838361be4da4a895a7a103cd3713e8aa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__006dad5b19d9ef175105300fccca630f8e9587d9f38dfd0bdf06a57203e6aa47(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8c4fe1f6249807f00dbb555577eebad1cb2b7ec35b14b608b93387caef48b0c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96d4e4a482009bc347bcfa4884923950a04a8191e703eed16363b2fb79eaaec9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aadff60126cc7565b19962a85dbf91532f9a772e1852b3c28ac38907b9807317(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c791158b6bc2cb9ec2e852f5e4cef5c8bf160915647ac86cc4ab10c4ca3e45d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d84d10bc9e57d5d29c33940999fa458c8c143d74934b411598762fbf75d441d6(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshift],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1595733a2190ee0f4bf387a947a6c38a49e7b5f37437fba0a2fae9956f6108e3(
    *,
    instance_url: typing.Optional[builtins.str] = None,
    is_sandbox_environment: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3b0dce2209a09110bbf29c55ee0271e7dd8096b9cbea98d3e5727d62e1026bc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28cfd887659c5a3dd8c402f9163135c05120ba79a0220577fb8d4adcba37a07a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b8170254a210e38c0991c76c9d6a6f398a58a0a12585acc9426d60fdc4a8178(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__943757c6abcae90f18f9a10b37a5cd4a454cbeb390c21a4781c90d0f4f47e092(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforce],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d458cd9c942ed9c9f25c50db8129203bc4d83dd027336796f5f978f137a4cf16(
    *,
    application_host_url: builtins.str,
    application_service_path: builtins.str,
    client_number: builtins.str,
    port_number: jsii.Number,
    logon_language: typing.Optional[builtins.str] = None,
    oauth_properties: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthProperties, typing.Dict[builtins.str, typing.Any]]] = None,
    private_link_service_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__053ff9d6b59c5ea156260e8e0b7c3846d71e0f025bdc378352644a0830f9138d(
    *,
    auth_code_url: builtins.str,
    oauth_scopes: typing.Sequence[builtins.str],
    token_url: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__437caa7ad50e3b43658f1b8181fa74de814dcc76b0233d206eadb825937f27bc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e40b06daae0c04daa3d475af9c355b54052fe1b62977a2405f87b3dd690ae44e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d82232bfbe69e81545090327f5d3a704c2cbb70b76e03bf275010f43d9dedba(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74ea7ea7054b93c9f564e1bce8b0d164ad38b27dda330ea335c3edce495d0aac(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cce705c1b743c55543db5294e5622413bf037d39e1a085f6c41002b0a2f943fc(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthProperties],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a939e3255b570b7ec98aa0ad15276da5195ff3786d8de8f105d34ad33f27fd95(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a805a2fd21027bb3b9dfb04f1b6b7401c6ecc1a5096dc53a4f70af0e35748c10(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be9a6f0db36efef994c5d2419bacd0008b566e1178d1518a6dce0420754558d5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3526ddc869fbd8f3082e72d1390d93c04913568a3cc3fac625a76aee3cb2d4e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e04a6c72d4429569c1db0e7e01be02fdc0382be5b066cc550ac2aff112ed177(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca08f8921871885d473c90dbced3257b08bdfece4d58290b470d09f44e6ac42b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b757431f7b6895a3e1573ba049dfc4ce54c1e9d3cc7f3b093560a1ba22bdbc59(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f4537be4165325784546f59cd4fe8790a98c3930a08c71ebbab9c0c452ee163(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoData],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddd1a1d27273517aa401895ee907ea16961ea7f2af91f71b1dfca61087a1c50c(
    *,
    instance_url: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0359a443d5dd0213099250d0256a1b3daf75fb292d55869f7b2277915a9a18c9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8179f01f125b95df9b2299410e9833db16bba1e6ba2af301e6560550e2ce6c3b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b2d3c22febb4d209f5812a308a17bbea7f4a1582f4f572c4ad801105e2d8898(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNow],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__499baf31df91ddee835dad617b8f519ddbfdeb046aeb814943f96678fdee3815(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea6593ac859da5c951dde2e6dd89641aeabb352c362660633e0f2711f79deabb(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingular],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccde0100d65c2ad565e73cc50d369adc6df45d1dcc2b93068378211a12b03a53(
    *,
    instance_url: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__746b08f719c2ab8bdae9f55cd484cb6e5bc46b31d8697e4a406326e0cd15157c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__937eacb6076c60b1c940592061a9473f1a0916844b8dde3e4c278861667d1cc1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3726ca4b6ea4e46237e3580cee9f740341a8b8328bfe3c106a9a6615df924467(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlack],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12110ad2ccd83ab20c614a173a9ccb40c939083531c9513f5c141ac798916bd7(
    *,
    bucket_name: builtins.str,
    stage: builtins.str,
    warehouse: builtins.str,
    account_name: typing.Optional[builtins.str] = None,
    bucket_prefix: typing.Optional[builtins.str] = None,
    private_link_service_name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97a32d4adc97c5ebe8f336dcb1ce4751dc0369a6645954e7a538e2cdd0700a42(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb34384ee7ac5382e631de2df59d7ca4dbaddd7907748370a235180258360ab3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6cf1ef2f067856bf49c2f712e5ee398be4a12543fe2a1f6cf069c6e97da8ebf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9d09e56a50b691174f3c309c64363e42db501b23bad5618169e87d824f6d2f5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1f46802cbadba377c558468742833a120a7b3cfaa5daa12b756699b5affdeee(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2dc52194b16160a42df24684ddfa6ca16db2b7018a3aba86143c12dff45c522(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50aa0ed6e3ade7b4f690ce37f5972d2756b87a146033ee419528ce1c02c58d81(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4286d581fbdfb594caa010fb8b4788676a538cad7660fe2265f998f2078cbaf8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de59bb5b9162519ec5084031d96c5f9a76e0bdf8cdec1410dfbee8d3762b51cf(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflake],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd8763b19b64a0cd2649123fbb22709fbe2816f6bba9ebdbfa8754626f934765(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d615a065c53a4f50d67f579b9dae749c691b2fdb32c0e34ae8778414ff6e8295(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicro],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4812be1d2cf756498b4f920794e7e6f275cad727a989e1e5d46813474597ee1(
    *,
    instance_url: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__071db8336164eb1a5de852fdd1f5f6fc14bef322a58d98a708a70cc22580b4e2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e94f7b70b76b2cbac2014f8a994385764282df27e49f6a222370f982b2dbae7a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__066106b5b18747be97471087d4e4381504998c205a316ed12b15b04de9c9efae(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeeva],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ccba491011fc58ec7616d39893a4a2aa3d8b0a49c6120d97e23050bdd8e4c4f(
    *,
    instance_url: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10ca8ab25235ab5784f35b429210164f0e2c2a62cc349ed65db6fa9cea66ff15(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c089a38f7e3e07e6220566cf2e2f37e8ce2e3d578e89854ec95c4b3bb145013c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ea448c1b86251710ff0c8cc17ceed9809dc59ae56956bbb11e420b7b1af6008(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendesk],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8034f221b4a23489df70b3be0b259316a4286b0702e2567f1e16b6532a49954(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f26954a025c4d30f8d2418a0267a4e1242caed3b0a51ad265f0d359ffd967ff1(
    value: typing.Optional[AppflowConnectorProfileConnectorProfileConfig],
) -> None:
    """Type checking stubs"""
    pass
