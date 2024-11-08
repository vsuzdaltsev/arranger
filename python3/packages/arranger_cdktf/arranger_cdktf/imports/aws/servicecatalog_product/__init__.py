'''
# `aws_servicecatalog_product`

Refer to the Terraform Registory for docs: [`aws_servicecatalog_product`](https://www.terraform.io/docs/providers/aws/r/servicecatalog_product).
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


class ServicecatalogProduct(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.servicecatalogProduct.ServicecatalogProduct",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product aws_servicecatalog_product}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        owner: builtins.str,
        provisioning_artifact_parameters: typing.Union["ServicecatalogProductProvisioningArtifactParameters", typing.Dict[builtins.str, typing.Any]],
        type: builtins.str,
        accept_language: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        distributor: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        support_description: typing.Optional[builtins.str] = None,
        support_email: typing.Optional[builtins.str] = None,
        support_url: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ServicecatalogProductTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product aws_servicecatalog_product} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#name ServicecatalogProduct#name}.
        :param owner: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#owner ServicecatalogProduct#owner}.
        :param provisioning_artifact_parameters: provisioning_artifact_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#provisioning_artifact_parameters ServicecatalogProduct#provisioning_artifact_parameters}
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#type ServicecatalogProduct#type}.
        :param accept_language: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#accept_language ServicecatalogProduct#accept_language}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#description ServicecatalogProduct#description}.
        :param distributor: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#distributor ServicecatalogProduct#distributor}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#id ServicecatalogProduct#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param support_description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#support_description ServicecatalogProduct#support_description}.
        :param support_email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#support_email ServicecatalogProduct#support_email}.
        :param support_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#support_url ServicecatalogProduct#support_url}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#tags ServicecatalogProduct#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#tags_all ServicecatalogProduct#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#timeouts ServicecatalogProduct#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea850f3f53cedcc7160f2ca8fbcc4ea656309a418ec17d9813e9ee49b2826cbe)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ServicecatalogProductConfig(
            name=name,
            owner=owner,
            provisioning_artifact_parameters=provisioning_artifact_parameters,
            type=type,
            accept_language=accept_language,
            description=description,
            distributor=distributor,
            id=id,
            support_description=support_description,
            support_email=support_email,
            support_url=support_url,
            tags=tags,
            tags_all=tags_all,
            timeouts=timeouts,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putProvisioningArtifactParameters")
    def put_provisioning_artifact_parameters(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        disable_template_validation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
        template_physical_id: typing.Optional[builtins.str] = None,
        template_url: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#description ServicecatalogProduct#description}.
        :param disable_template_validation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#disable_template_validation ServicecatalogProduct#disable_template_validation}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#name ServicecatalogProduct#name}.
        :param template_physical_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#template_physical_id ServicecatalogProduct#template_physical_id}.
        :param template_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#template_url ServicecatalogProduct#template_url}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#type ServicecatalogProduct#type}.
        '''
        value = ServicecatalogProductProvisioningArtifactParameters(
            description=description,
            disable_template_validation=disable_template_validation,
            name=name,
            template_physical_id=template_physical_id,
            template_url=template_url,
            type=type,
        )

        return typing.cast(None, jsii.invoke(self, "putProvisioningArtifactParameters", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#create ServicecatalogProduct#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#delete ServicecatalogProduct#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#read ServicecatalogProduct#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#update ServicecatalogProduct#update}.
        '''
        value = ServicecatalogProductTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAcceptLanguage")
    def reset_accept_language(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAcceptLanguage", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDistributor")
    def reset_distributor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDistributor", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSupportDescription")
    def reset_support_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSupportDescription", []))

    @jsii.member(jsii_name="resetSupportEmail")
    def reset_support_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSupportEmail", []))

    @jsii.member(jsii_name="resetSupportUrl")
    def reset_support_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSupportUrl", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

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
    @jsii.member(jsii_name="createdTime")
    def created_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdTime"))

    @builtins.property
    @jsii.member(jsii_name="hasDefaultPath")
    def has_default_path(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "hasDefaultPath"))

    @builtins.property
    @jsii.member(jsii_name="provisioningArtifactParameters")
    def provisioning_artifact_parameters(
        self,
    ) -> "ServicecatalogProductProvisioningArtifactParametersOutputReference":
        return typing.cast("ServicecatalogProductProvisioningArtifactParametersOutputReference", jsii.get(self, "provisioningArtifactParameters"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ServicecatalogProductTimeoutsOutputReference":
        return typing.cast("ServicecatalogProductTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="acceptLanguageInput")
    def accept_language_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "acceptLanguageInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="distributorInput")
    def distributor_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "distributorInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="ownerInput")
    def owner_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ownerInput"))

    @builtins.property
    @jsii.member(jsii_name="provisioningArtifactParametersInput")
    def provisioning_artifact_parameters_input(
        self,
    ) -> typing.Optional["ServicecatalogProductProvisioningArtifactParameters"]:
        return typing.cast(typing.Optional["ServicecatalogProductProvisioningArtifactParameters"], jsii.get(self, "provisioningArtifactParametersInput"))

    @builtins.property
    @jsii.member(jsii_name="supportDescriptionInput")
    def support_description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "supportDescriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="supportEmailInput")
    def support_email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "supportEmailInput"))

    @builtins.property
    @jsii.member(jsii_name="supportUrlInput")
    def support_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "supportUrlInput"))

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
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["ServicecatalogProductTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ServicecatalogProductTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="acceptLanguage")
    def accept_language(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "acceptLanguage"))

    @accept_language.setter
    def accept_language(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bca2bbf794b7bcb30842747f63dcb9f8630dd31d9e834a26109fdd226ddbfd6c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acceptLanguage", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3fd433ef16f7aea9e72b15bf2cb7a8c56025616609695acaee6448ef9883b9f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="distributor")
    def distributor(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "distributor"))

    @distributor.setter
    def distributor(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afcdc9776d81dbb67a6866e106e3de53ca6182ad35876a8c0558ef7f9167e701)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "distributor", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d97e08b8114d971ca819145e140c114534b18027468f70a306882a2a95bdcb1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1e9ab0e90c6cdd64cd4514756c6fcff44b2dbad1414de4a3be26bbfb2e181de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="owner")
    def owner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "owner"))

    @owner.setter
    def owner(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00ec6fadb44f84591c6ee8ac5267f84af98fc855179b8e40b2f508ece3ab30fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "owner", value)

    @builtins.property
    @jsii.member(jsii_name="supportDescription")
    def support_description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "supportDescription"))

    @support_description.setter
    def support_description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0e2de5d82bfdf4c0e6036aedbfa704efadcc1b36ab4d4ade4a96d244d0d4955)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "supportDescription", value)

    @builtins.property
    @jsii.member(jsii_name="supportEmail")
    def support_email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "supportEmail"))

    @support_email.setter
    def support_email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7beeb7313e95e06a966023bf669d609221c5aac3cac81549e40fe3d81568ae6b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "supportEmail", value)

    @builtins.property
    @jsii.member(jsii_name="supportUrl")
    def support_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "supportUrl"))

    @support_url.setter
    def support_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88a2de86f6f29413f0404b5c55d3050adcc01dfb9aee6aff8d9ef02f16d10a4a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "supportUrl", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2834e4157b227c1ed8848ad630584c16cb09827af3868c500987c5314a97124c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0eb23707e1df74c83eeec8c9ca982fc1fb88e4a67765d55de35564420f01d84e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05c527aab12e6b02a99cd63a6b9505df859a4ac79f097db4c964ed0e76df45a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)


@jsii.data_type(
    jsii_type="aws.servicecatalogProduct.ServicecatalogProductConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "owner": "owner",
        "provisioning_artifact_parameters": "provisioningArtifactParameters",
        "type": "type",
        "accept_language": "acceptLanguage",
        "description": "description",
        "distributor": "distributor",
        "id": "id",
        "support_description": "supportDescription",
        "support_email": "supportEmail",
        "support_url": "supportUrl",
        "tags": "tags",
        "tags_all": "tagsAll",
        "timeouts": "timeouts",
    },
)
class ServicecatalogProductConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        name: builtins.str,
        owner: builtins.str,
        provisioning_artifact_parameters: typing.Union["ServicecatalogProductProvisioningArtifactParameters", typing.Dict[builtins.str, typing.Any]],
        type: builtins.str,
        accept_language: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        distributor: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        support_description: typing.Optional[builtins.str] = None,
        support_email: typing.Optional[builtins.str] = None,
        support_url: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ServicecatalogProductTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#name ServicecatalogProduct#name}.
        :param owner: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#owner ServicecatalogProduct#owner}.
        :param provisioning_artifact_parameters: provisioning_artifact_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#provisioning_artifact_parameters ServicecatalogProduct#provisioning_artifact_parameters}
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#type ServicecatalogProduct#type}.
        :param accept_language: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#accept_language ServicecatalogProduct#accept_language}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#description ServicecatalogProduct#description}.
        :param distributor: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#distributor ServicecatalogProduct#distributor}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#id ServicecatalogProduct#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param support_description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#support_description ServicecatalogProduct#support_description}.
        :param support_email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#support_email ServicecatalogProduct#support_email}.
        :param support_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#support_url ServicecatalogProduct#support_url}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#tags ServicecatalogProduct#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#tags_all ServicecatalogProduct#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#timeouts ServicecatalogProduct#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(provisioning_artifact_parameters, dict):
            provisioning_artifact_parameters = ServicecatalogProductProvisioningArtifactParameters(**provisioning_artifact_parameters)
        if isinstance(timeouts, dict):
            timeouts = ServicecatalogProductTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0db61aa37a7a25459b9febc511558ffeb3c89e3cfe555be2686da860ff712b7)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument owner", value=owner, expected_type=type_hints["owner"])
            check_type(argname="argument provisioning_artifact_parameters", value=provisioning_artifact_parameters, expected_type=type_hints["provisioning_artifact_parameters"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument accept_language", value=accept_language, expected_type=type_hints["accept_language"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument distributor", value=distributor, expected_type=type_hints["distributor"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument support_description", value=support_description, expected_type=type_hints["support_description"])
            check_type(argname="argument support_email", value=support_email, expected_type=type_hints["support_email"])
            check_type(argname="argument support_url", value=support_url, expected_type=type_hints["support_url"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "owner": owner,
            "provisioning_artifact_parameters": provisioning_artifact_parameters,
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
        if accept_language is not None:
            self._values["accept_language"] = accept_language
        if description is not None:
            self._values["description"] = description
        if distributor is not None:
            self._values["distributor"] = distributor
        if id is not None:
            self._values["id"] = id
        if support_description is not None:
            self._values["support_description"] = support_description
        if support_email is not None:
            self._values["support_email"] = support_email
        if support_url is not None:
            self._values["support_url"] = support_url
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if timeouts is not None:
            self._values["timeouts"] = timeouts

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
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#name ServicecatalogProduct#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def owner(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#owner ServicecatalogProduct#owner}.'''
        result = self._values.get("owner")
        assert result is not None, "Required property 'owner' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def provisioning_artifact_parameters(
        self,
    ) -> "ServicecatalogProductProvisioningArtifactParameters":
        '''provisioning_artifact_parameters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#provisioning_artifact_parameters ServicecatalogProduct#provisioning_artifact_parameters}
        '''
        result = self._values.get("provisioning_artifact_parameters")
        assert result is not None, "Required property 'provisioning_artifact_parameters' is missing"
        return typing.cast("ServicecatalogProductProvisioningArtifactParameters", result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#type ServicecatalogProduct#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def accept_language(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#accept_language ServicecatalogProduct#accept_language}.'''
        result = self._values.get("accept_language")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#description ServicecatalogProduct#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def distributor(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#distributor ServicecatalogProduct#distributor}.'''
        result = self._values.get("distributor")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#id ServicecatalogProduct#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def support_description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#support_description ServicecatalogProduct#support_description}.'''
        result = self._values.get("support_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def support_email(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#support_email ServicecatalogProduct#support_email}.'''
        result = self._values.get("support_email")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def support_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#support_url ServicecatalogProduct#support_url}.'''
        result = self._values.get("support_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#tags ServicecatalogProduct#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#tags_all ServicecatalogProduct#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ServicecatalogProductTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#timeouts ServicecatalogProduct#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ServicecatalogProductTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServicecatalogProductConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.servicecatalogProduct.ServicecatalogProductProvisioningArtifactParameters",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "disable_template_validation": "disableTemplateValidation",
        "name": "name",
        "template_physical_id": "templatePhysicalId",
        "template_url": "templateUrl",
        "type": "type",
    },
)
class ServicecatalogProductProvisioningArtifactParameters:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        disable_template_validation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
        template_physical_id: typing.Optional[builtins.str] = None,
        template_url: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#description ServicecatalogProduct#description}.
        :param disable_template_validation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#disable_template_validation ServicecatalogProduct#disable_template_validation}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#name ServicecatalogProduct#name}.
        :param template_physical_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#template_physical_id ServicecatalogProduct#template_physical_id}.
        :param template_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#template_url ServicecatalogProduct#template_url}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#type ServicecatalogProduct#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fdad715291246e11abd519b2abba155c28f5e54a9a810b21e888aad9d9f4174a)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument disable_template_validation", value=disable_template_validation, expected_type=type_hints["disable_template_validation"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument template_physical_id", value=template_physical_id, expected_type=type_hints["template_physical_id"])
            check_type(argname="argument template_url", value=template_url, expected_type=type_hints["template_url"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if disable_template_validation is not None:
            self._values["disable_template_validation"] = disable_template_validation
        if name is not None:
            self._values["name"] = name
        if template_physical_id is not None:
            self._values["template_physical_id"] = template_physical_id
        if template_url is not None:
            self._values["template_url"] = template_url
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#description ServicecatalogProduct#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disable_template_validation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#disable_template_validation ServicecatalogProduct#disable_template_validation}.'''
        result = self._values.get("disable_template_validation")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#name ServicecatalogProduct#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def template_physical_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#template_physical_id ServicecatalogProduct#template_physical_id}.'''
        result = self._values.get("template_physical_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def template_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#template_url ServicecatalogProduct#template_url}.'''
        result = self._values.get("template_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#type ServicecatalogProduct#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServicecatalogProductProvisioningArtifactParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServicecatalogProductProvisioningArtifactParametersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.servicecatalogProduct.ServicecatalogProductProvisioningArtifactParametersOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e5bf6bd1ad3e1e3848ec931c1371579e19a4703ae6c0c9aa0f6ad043fac39756)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDisableTemplateValidation")
    def reset_disable_template_validation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableTemplateValidation", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetTemplatePhysicalId")
    def reset_template_physical_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTemplatePhysicalId", []))

    @jsii.member(jsii_name="resetTemplateUrl")
    def reset_template_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTemplateUrl", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="disableTemplateValidationInput")
    def disable_template_validation_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disableTemplateValidationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="templatePhysicalIdInput")
    def template_physical_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templatePhysicalIdInput"))

    @builtins.property
    @jsii.member(jsii_name="templateUrlInput")
    def template_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__702f9feab1b36b4ca3ff407be52082da07e239ece6bca0c1cd208eec46d1a053)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="disableTemplateValidation")
    def disable_template_validation(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "disableTemplateValidation"))

    @disable_template_validation.setter
    def disable_template_validation(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4b57fc14a45315a02948af874d6b3bad6f63dd3451314f10061494f45dc6295)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableTemplateValidation", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f181aa52b13aea0461052a0fdffa391f265b059f91bba48e36fa409b0ac47da7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="templatePhysicalId")
    def template_physical_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "templatePhysicalId"))

    @template_physical_id.setter
    def template_physical_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__582506778fca6ea861cb1a5845a789fb11b18a8b35ad849fc61e6b383a241b10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templatePhysicalId", value)

    @builtins.property
    @jsii.member(jsii_name="templateUrl")
    def template_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "templateUrl"))

    @template_url.setter
    def template_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__509879f2e4d8777b271c91578dd711271773ee588604e6ee676d25764368c358)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateUrl", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e3dc439760924102fe158f1692a9f66f97d721df5b56b5695a7deb3b34fffbc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ServicecatalogProductProvisioningArtifactParameters]:
        return typing.cast(typing.Optional[ServicecatalogProductProvisioningArtifactParameters], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ServicecatalogProductProvisioningArtifactParameters],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__912d3e3dcba7d577514b473036a7ac5a11772e5cf7611a6eecd1d48e03682734)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.servicecatalogProduct.ServicecatalogProductTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class ServicecatalogProductTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#create ServicecatalogProduct#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#delete ServicecatalogProduct#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#read ServicecatalogProduct#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#update ServicecatalogProduct#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c698a8fa4002024c0493f4406b1d16c5656b039fb115bb76688e0fcdf6d771da)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument read", value=read, expected_type=type_hints["read"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if read is not None:
            self._values["read"] = read
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#create ServicecatalogProduct#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#delete ServicecatalogProduct#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#read ServicecatalogProduct#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/servicecatalog_product#update ServicecatalogProduct#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServicecatalogProductTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServicecatalogProductTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.servicecatalogProduct.ServicecatalogProductTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b7a68021dbf28bca4bafa5e09b7ea2b208e0cfa465bdec5b00847fdfbc3f4a99)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetRead")
    def reset_read(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRead", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="readInput")
    def read_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "readInput"))

    @builtins.property
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f355cc37c8fb5e2108f32366666e0c26501028742a550a164d33c709db33cffa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c57c3a5f74d50ea105b024742315c3d479590aaced2d50e1583dbc43e475ac6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f868613e02ce04ae201be6ea7f151ac4c98ff7180c5e5080e17ee1186c83eddd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__844e6e296982f9e3eaecdfb290171d2463a2bdd7a9ad1cf3e461729410edef2c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ServicecatalogProductTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ServicecatalogProductTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ServicecatalogProductTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1bd942c6e5c9fa6b933a1c67749bd9b745a18f162658df93c5a1903c71da059f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ServicecatalogProduct",
    "ServicecatalogProductConfig",
    "ServicecatalogProductProvisioningArtifactParameters",
    "ServicecatalogProductProvisioningArtifactParametersOutputReference",
    "ServicecatalogProductTimeouts",
    "ServicecatalogProductTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__ea850f3f53cedcc7160f2ca8fbcc4ea656309a418ec17d9813e9ee49b2826cbe(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    owner: builtins.str,
    provisioning_artifact_parameters: typing.Union[ServicecatalogProductProvisioningArtifactParameters, typing.Dict[builtins.str, typing.Any]],
    type: builtins.str,
    accept_language: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    distributor: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    support_description: typing.Optional[builtins.str] = None,
    support_email: typing.Optional[builtins.str] = None,
    support_url: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[ServicecatalogProductTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__bca2bbf794b7bcb30842747f63dcb9f8630dd31d9e834a26109fdd226ddbfd6c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fd433ef16f7aea9e72b15bf2cb7a8c56025616609695acaee6448ef9883b9f9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afcdc9776d81dbb67a6866e106e3de53ca6182ad35876a8c0558ef7f9167e701(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d97e08b8114d971ca819145e140c114534b18027468f70a306882a2a95bdcb1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1e9ab0e90c6cdd64cd4514756c6fcff44b2dbad1414de4a3be26bbfb2e181de(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00ec6fadb44f84591c6ee8ac5267f84af98fc855179b8e40b2f508ece3ab30fa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0e2de5d82bfdf4c0e6036aedbfa704efadcc1b36ab4d4ade4a96d244d0d4955(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7beeb7313e95e06a966023bf669d609221c5aac3cac81549e40fe3d81568ae6b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88a2de86f6f29413f0404b5c55d3050adcc01dfb9aee6aff8d9ef02f16d10a4a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2834e4157b227c1ed8848ad630584c16cb09827af3868c500987c5314a97124c(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0eb23707e1df74c83eeec8c9ca982fc1fb88e4a67765d55de35564420f01d84e(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05c527aab12e6b02a99cd63a6b9505df859a4ac79f097db4c964ed0e76df45a4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0db61aa37a7a25459b9febc511558ffeb3c89e3cfe555be2686da860ff712b7(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    owner: builtins.str,
    provisioning_artifact_parameters: typing.Union[ServicecatalogProductProvisioningArtifactParameters, typing.Dict[builtins.str, typing.Any]],
    type: builtins.str,
    accept_language: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    distributor: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    support_description: typing.Optional[builtins.str] = None,
    support_email: typing.Optional[builtins.str] = None,
    support_url: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[ServicecatalogProductTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fdad715291246e11abd519b2abba155c28f5e54a9a810b21e888aad9d9f4174a(
    *,
    description: typing.Optional[builtins.str] = None,
    disable_template_validation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    name: typing.Optional[builtins.str] = None,
    template_physical_id: typing.Optional[builtins.str] = None,
    template_url: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5bf6bd1ad3e1e3848ec931c1371579e19a4703ae6c0c9aa0f6ad043fac39756(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__702f9feab1b36b4ca3ff407be52082da07e239ece6bca0c1cd208eec46d1a053(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4b57fc14a45315a02948af874d6b3bad6f63dd3451314f10061494f45dc6295(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f181aa52b13aea0461052a0fdffa391f265b059f91bba48e36fa409b0ac47da7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__582506778fca6ea861cb1a5845a789fb11b18a8b35ad849fc61e6b383a241b10(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__509879f2e4d8777b271c91578dd711271773ee588604e6ee676d25764368c358(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e3dc439760924102fe158f1692a9f66f97d721df5b56b5695a7deb3b34fffbc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__912d3e3dcba7d577514b473036a7ac5a11772e5cf7611a6eecd1d48e03682734(
    value: typing.Optional[ServicecatalogProductProvisioningArtifactParameters],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c698a8fa4002024c0493f4406b1d16c5656b039fb115bb76688e0fcdf6d771da(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    read: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7a68021dbf28bca4bafa5e09b7ea2b208e0cfa465bdec5b00847fdfbc3f4a99(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f355cc37c8fb5e2108f32366666e0c26501028742a550a164d33c709db33cffa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c57c3a5f74d50ea105b024742315c3d479590aaced2d50e1583dbc43e475ac6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f868613e02ce04ae201be6ea7f151ac4c98ff7180c5e5080e17ee1186c83eddd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__844e6e296982f9e3eaecdfb290171d2463a2bdd7a9ad1cf3e461729410edef2c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bd942c6e5c9fa6b933a1c67749bd9b745a18f162658df93c5a1903c71da059f(
    value: typing.Optional[typing.Union[ServicecatalogProductTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
