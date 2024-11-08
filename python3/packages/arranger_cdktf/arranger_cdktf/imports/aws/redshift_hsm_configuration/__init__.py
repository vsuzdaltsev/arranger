'''
# `aws_redshift_hsm_configuration`

Refer to the Terraform Registory for docs: [`aws_redshift_hsm_configuration`](https://www.terraform.io/docs/providers/aws/r/redshift_hsm_configuration).
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


class RedshiftHsmConfiguration(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.redshiftHsmConfiguration.RedshiftHsmConfiguration",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/redshift_hsm_configuration aws_redshift_hsm_configuration}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        description: builtins.str,
        hsm_configuration_identifier: builtins.str,
        hsm_ip_address: builtins.str,
        hsm_partition_name: builtins.str,
        hsm_partition_password: builtins.str,
        hsm_server_public_certificate: builtins.str,
        id: typing.Optional[builtins.str] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/redshift_hsm_configuration aws_redshift_hsm_configuration} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/redshift_hsm_configuration#description RedshiftHsmConfiguration#description}.
        :param hsm_configuration_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/redshift_hsm_configuration#hsm_configuration_identifier RedshiftHsmConfiguration#hsm_configuration_identifier}.
        :param hsm_ip_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/redshift_hsm_configuration#hsm_ip_address RedshiftHsmConfiguration#hsm_ip_address}.
        :param hsm_partition_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/redshift_hsm_configuration#hsm_partition_name RedshiftHsmConfiguration#hsm_partition_name}.
        :param hsm_partition_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/redshift_hsm_configuration#hsm_partition_password RedshiftHsmConfiguration#hsm_partition_password}.
        :param hsm_server_public_certificate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/redshift_hsm_configuration#hsm_server_public_certificate RedshiftHsmConfiguration#hsm_server_public_certificate}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/redshift_hsm_configuration#id RedshiftHsmConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/redshift_hsm_configuration#tags RedshiftHsmConfiguration#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/redshift_hsm_configuration#tags_all RedshiftHsmConfiguration#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec4b45c333970feff8df3af57a408a213f21c8b1f42feed88a27695f988b39fa)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = RedshiftHsmConfigurationConfig(
            description=description,
            hsm_configuration_identifier=hsm_configuration_identifier,
            hsm_ip_address=hsm_ip_address,
            hsm_partition_name=hsm_partition_name,
            hsm_partition_password=hsm_partition_password,
            hsm_server_public_certificate=hsm_server_public_certificate,
            id=id,
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

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

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
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="hsmConfigurationIdentifierInput")
    def hsm_configuration_identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hsmConfigurationIdentifierInput"))

    @builtins.property
    @jsii.member(jsii_name="hsmIpAddressInput")
    def hsm_ip_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hsmIpAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="hsmPartitionNameInput")
    def hsm_partition_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hsmPartitionNameInput"))

    @builtins.property
    @jsii.member(jsii_name="hsmPartitionPasswordInput")
    def hsm_partition_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hsmPartitionPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="hsmServerPublicCertificateInput")
    def hsm_server_public_certificate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hsmServerPublicCertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

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
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52d8876860c23493852820ca942d1c085e44a1f3bd7e30e06da148144cdd7dd2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="hsmConfigurationIdentifier")
    def hsm_configuration_identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hsmConfigurationIdentifier"))

    @hsm_configuration_identifier.setter
    def hsm_configuration_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90120c84e3875076d8aa93f6676a251018c9446391a538eb71e3e13e538d17fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hsmConfigurationIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="hsmIpAddress")
    def hsm_ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hsmIpAddress"))

    @hsm_ip_address.setter
    def hsm_ip_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__980b208337c8be5e0aa1bc268310f21b9f9b6acefb305facdc868a27bfef749a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hsmIpAddress", value)

    @builtins.property
    @jsii.member(jsii_name="hsmPartitionName")
    def hsm_partition_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hsmPartitionName"))

    @hsm_partition_name.setter
    def hsm_partition_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6f68f96353c96ba0026faf0e62c56a1c34644c097ff3662730903559651f615)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hsmPartitionName", value)

    @builtins.property
    @jsii.member(jsii_name="hsmPartitionPassword")
    def hsm_partition_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hsmPartitionPassword"))

    @hsm_partition_password.setter
    def hsm_partition_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbdd851626470817cac849adefe50d418104556e1e5a1f970bc0db878f10129c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hsmPartitionPassword", value)

    @builtins.property
    @jsii.member(jsii_name="hsmServerPublicCertificate")
    def hsm_server_public_certificate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hsmServerPublicCertificate"))

    @hsm_server_public_certificate.setter
    def hsm_server_public_certificate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abc0ac0e8e7d7f8cd6fdcd0dce20f72c632913361ce585494b516c51fcb9a384)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hsmServerPublicCertificate", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e6d820b96cf9bbfae3e290bc37575869d46cec08a9b3838fb716f6468cf2cc2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7a402b873b604dad7b2e11e5c1db329c483dfde4c733db30c0044f1941bda50)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c20a7ca6c5dc49a8a539885df1445973806cdfdfd144c0e3e628679ec125650a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.redshiftHsmConfiguration.RedshiftHsmConfigurationConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "description": "description",
        "hsm_configuration_identifier": "hsmConfigurationIdentifier",
        "hsm_ip_address": "hsmIpAddress",
        "hsm_partition_name": "hsmPartitionName",
        "hsm_partition_password": "hsmPartitionPassword",
        "hsm_server_public_certificate": "hsmServerPublicCertificate",
        "id": "id",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class RedshiftHsmConfigurationConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        description: builtins.str,
        hsm_configuration_identifier: builtins.str,
        hsm_ip_address: builtins.str,
        hsm_partition_name: builtins.str,
        hsm_partition_password: builtins.str,
        hsm_server_public_certificate: builtins.str,
        id: typing.Optional[builtins.str] = None,
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
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/redshift_hsm_configuration#description RedshiftHsmConfiguration#description}.
        :param hsm_configuration_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/redshift_hsm_configuration#hsm_configuration_identifier RedshiftHsmConfiguration#hsm_configuration_identifier}.
        :param hsm_ip_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/redshift_hsm_configuration#hsm_ip_address RedshiftHsmConfiguration#hsm_ip_address}.
        :param hsm_partition_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/redshift_hsm_configuration#hsm_partition_name RedshiftHsmConfiguration#hsm_partition_name}.
        :param hsm_partition_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/redshift_hsm_configuration#hsm_partition_password RedshiftHsmConfiguration#hsm_partition_password}.
        :param hsm_server_public_certificate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/redshift_hsm_configuration#hsm_server_public_certificate RedshiftHsmConfiguration#hsm_server_public_certificate}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/redshift_hsm_configuration#id RedshiftHsmConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/redshift_hsm_configuration#tags RedshiftHsmConfiguration#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/redshift_hsm_configuration#tags_all RedshiftHsmConfiguration#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7d7cef5b26a8b6c084cb50e39000a64995c651053760b432630f5680bb7f6d2)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument hsm_configuration_identifier", value=hsm_configuration_identifier, expected_type=type_hints["hsm_configuration_identifier"])
            check_type(argname="argument hsm_ip_address", value=hsm_ip_address, expected_type=type_hints["hsm_ip_address"])
            check_type(argname="argument hsm_partition_name", value=hsm_partition_name, expected_type=type_hints["hsm_partition_name"])
            check_type(argname="argument hsm_partition_password", value=hsm_partition_password, expected_type=type_hints["hsm_partition_password"])
            check_type(argname="argument hsm_server_public_certificate", value=hsm_server_public_certificate, expected_type=type_hints["hsm_server_public_certificate"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "hsm_configuration_identifier": hsm_configuration_identifier,
            "hsm_ip_address": hsm_ip_address,
            "hsm_partition_name": hsm_partition_name,
            "hsm_partition_password": hsm_partition_password,
            "hsm_server_public_certificate": hsm_server_public_certificate,
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
        if id is not None:
            self._values["id"] = id
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
    def description(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/redshift_hsm_configuration#description RedshiftHsmConfiguration#description}.'''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def hsm_configuration_identifier(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/redshift_hsm_configuration#hsm_configuration_identifier RedshiftHsmConfiguration#hsm_configuration_identifier}.'''
        result = self._values.get("hsm_configuration_identifier")
        assert result is not None, "Required property 'hsm_configuration_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def hsm_ip_address(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/redshift_hsm_configuration#hsm_ip_address RedshiftHsmConfiguration#hsm_ip_address}.'''
        result = self._values.get("hsm_ip_address")
        assert result is not None, "Required property 'hsm_ip_address' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def hsm_partition_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/redshift_hsm_configuration#hsm_partition_name RedshiftHsmConfiguration#hsm_partition_name}.'''
        result = self._values.get("hsm_partition_name")
        assert result is not None, "Required property 'hsm_partition_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def hsm_partition_password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/redshift_hsm_configuration#hsm_partition_password RedshiftHsmConfiguration#hsm_partition_password}.'''
        result = self._values.get("hsm_partition_password")
        assert result is not None, "Required property 'hsm_partition_password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def hsm_server_public_certificate(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/redshift_hsm_configuration#hsm_server_public_certificate RedshiftHsmConfiguration#hsm_server_public_certificate}.'''
        result = self._values.get("hsm_server_public_certificate")
        assert result is not None, "Required property 'hsm_server_public_certificate' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/redshift_hsm_configuration#id RedshiftHsmConfiguration#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/redshift_hsm_configuration#tags RedshiftHsmConfiguration#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/redshift_hsm_configuration#tags_all RedshiftHsmConfiguration#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RedshiftHsmConfigurationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "RedshiftHsmConfiguration",
    "RedshiftHsmConfigurationConfig",
]

publication.publish()

def _typecheckingstub__ec4b45c333970feff8df3af57a408a213f21c8b1f42feed88a27695f988b39fa(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    description: builtins.str,
    hsm_configuration_identifier: builtins.str,
    hsm_ip_address: builtins.str,
    hsm_partition_name: builtins.str,
    hsm_partition_password: builtins.str,
    hsm_server_public_certificate: builtins.str,
    id: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__52d8876860c23493852820ca942d1c085e44a1f3bd7e30e06da148144cdd7dd2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90120c84e3875076d8aa93f6676a251018c9446391a538eb71e3e13e538d17fa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__980b208337c8be5e0aa1bc268310f21b9f9b6acefb305facdc868a27bfef749a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6f68f96353c96ba0026faf0e62c56a1c34644c097ff3662730903559651f615(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbdd851626470817cac849adefe50d418104556e1e5a1f970bc0db878f10129c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abc0ac0e8e7d7f8cd6fdcd0dce20f72c632913361ce585494b516c51fcb9a384(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e6d820b96cf9bbfae3e290bc37575869d46cec08a9b3838fb716f6468cf2cc2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7a402b873b604dad7b2e11e5c1db329c483dfde4c733db30c0044f1941bda50(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c20a7ca6c5dc49a8a539885df1445973806cdfdfd144c0e3e628679ec125650a(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7d7cef5b26a8b6c084cb50e39000a64995c651053760b432630f5680bb7f6d2(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    description: builtins.str,
    hsm_configuration_identifier: builtins.str,
    hsm_ip_address: builtins.str,
    hsm_partition_name: builtins.str,
    hsm_partition_password: builtins.str,
    hsm_server_public_certificate: builtins.str,
    id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
