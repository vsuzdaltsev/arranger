'''
# `aws_imagebuilder_distribution_configuration`

Refer to the Terraform Registory for docs: [`aws_imagebuilder_distribution_configuration`](https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration).
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


class ImagebuilderDistributionConfiguration(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.imagebuilderDistributionConfiguration.ImagebuilderDistributionConfiguration",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration aws_imagebuilder_distribution_configuration}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        distribution: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ImagebuilderDistributionConfigurationDistribution", typing.Dict[builtins.str, typing.Any]]]],
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration aws_imagebuilder_distribution_configuration} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param distribution: distribution block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#distribution ImagebuilderDistributionConfiguration#distribution}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#name ImagebuilderDistributionConfiguration#name}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#description ImagebuilderDistributionConfiguration#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#id ImagebuilderDistributionConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#tags ImagebuilderDistributionConfiguration#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#tags_all ImagebuilderDistributionConfiguration#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f66cb2e0c73c974e296447c0da2980036bb6aded7dcc62538a75f8ea9671faf)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ImagebuilderDistributionConfigurationConfig(
            distribution=distribution,
            name=name,
            description=description,
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

    @jsii.member(jsii_name="putDistribution")
    def put_distribution(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ImagebuilderDistributionConfigurationDistribution", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72d72c233d7cd6bfae7e2b5ef2337e1a5602618600a19029d6b150b1906024d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDistribution", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

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
    @jsii.member(jsii_name="dateCreated")
    def date_created(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dateCreated"))

    @builtins.property
    @jsii.member(jsii_name="dateUpdated")
    def date_updated(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dateUpdated"))

    @builtins.property
    @jsii.member(jsii_name="distribution")
    def distribution(self) -> "ImagebuilderDistributionConfigurationDistributionList":
        return typing.cast("ImagebuilderDistributionConfigurationDistributionList", jsii.get(self, "distribution"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="distributionInput")
    def distribution_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ImagebuilderDistributionConfigurationDistribution"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ImagebuilderDistributionConfigurationDistribution"]]], jsii.get(self, "distributionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__c97858b6a58825d148a33950d790c7a41b89a455ec21d8392f55d1f234b1ae5c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__818de1fa368e63955893d93642196ccc1c7185d6a5f11cd446383a36950fa49f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7a9fd11f9a30783c5efd1a62d04ceaa728f56a338a14b33ecb833a76bbfdfdb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__601518209bc0f1489473620ae06f54b01c9bd4d3787ffa5106ae04f22e16a507)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f0c39485cdf4a2c75cf3db5919f00caafd6a90ff869d1a22026d7ce6aed27fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.imagebuilderDistributionConfiguration.ImagebuilderDistributionConfigurationConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "distribution": "distribution",
        "name": "name",
        "description": "description",
        "id": "id",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class ImagebuilderDistributionConfigurationConfig(
    _cdktf_9a9027ec.TerraformMetaArguments,
):
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
        distribution: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ImagebuilderDistributionConfigurationDistribution", typing.Dict[builtins.str, typing.Any]]]],
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
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
        :param distribution: distribution block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#distribution ImagebuilderDistributionConfiguration#distribution}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#name ImagebuilderDistributionConfiguration#name}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#description ImagebuilderDistributionConfiguration#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#id ImagebuilderDistributionConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#tags ImagebuilderDistributionConfiguration#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#tags_all ImagebuilderDistributionConfiguration#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2065fdc685463367e51a39f8bf47f1c8ae9cc8058aa0dddb90b90792acc6fbf9)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument distribution", value=distribution, expected_type=type_hints["distribution"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "distribution": distribution,
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
        if description is not None:
            self._values["description"] = description
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
    def distribution(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ImagebuilderDistributionConfigurationDistribution"]]:
        '''distribution block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#distribution ImagebuilderDistributionConfiguration#distribution}
        '''
        result = self._values.get("distribution")
        assert result is not None, "Required property 'distribution' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ImagebuilderDistributionConfigurationDistribution"]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#name ImagebuilderDistributionConfiguration#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#description ImagebuilderDistributionConfiguration#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#id ImagebuilderDistributionConfiguration#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#tags ImagebuilderDistributionConfiguration#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#tags_all ImagebuilderDistributionConfiguration#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ImagebuilderDistributionConfigurationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.imagebuilderDistributionConfiguration.ImagebuilderDistributionConfigurationDistribution",
    jsii_struct_bases=[],
    name_mapping={
        "region": "region",
        "ami_distribution_configuration": "amiDistributionConfiguration",
        "container_distribution_configuration": "containerDistributionConfiguration",
        "fast_launch_configuration": "fastLaunchConfiguration",
        "launch_template_configuration": "launchTemplateConfiguration",
        "license_configuration_arns": "licenseConfigurationArns",
    },
)
class ImagebuilderDistributionConfigurationDistribution:
    def __init__(
        self,
        *,
        region: builtins.str,
        ami_distribution_configuration: typing.Optional[typing.Union["ImagebuilderDistributionConfigurationDistributionAmiDistributionConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        container_distribution_configuration: typing.Optional[typing.Union["ImagebuilderDistributionConfigurationDistributionContainerDistributionConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        fast_launch_configuration: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ImagebuilderDistributionConfigurationDistributionFastLaunchConfiguration", typing.Dict[builtins.str, typing.Any]]]]] = None,
        launch_template_configuration: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ImagebuilderDistributionConfigurationDistributionLaunchTemplateConfiguration", typing.Dict[builtins.str, typing.Any]]]]] = None,
        license_configuration_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#region ImagebuilderDistributionConfiguration#region}.
        :param ami_distribution_configuration: ami_distribution_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#ami_distribution_configuration ImagebuilderDistributionConfiguration#ami_distribution_configuration}
        :param container_distribution_configuration: container_distribution_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#container_distribution_configuration ImagebuilderDistributionConfiguration#container_distribution_configuration}
        :param fast_launch_configuration: fast_launch_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#fast_launch_configuration ImagebuilderDistributionConfiguration#fast_launch_configuration}
        :param launch_template_configuration: launch_template_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#launch_template_configuration ImagebuilderDistributionConfiguration#launch_template_configuration}
        :param license_configuration_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#license_configuration_arns ImagebuilderDistributionConfiguration#license_configuration_arns}.
        '''
        if isinstance(ami_distribution_configuration, dict):
            ami_distribution_configuration = ImagebuilderDistributionConfigurationDistributionAmiDistributionConfiguration(**ami_distribution_configuration)
        if isinstance(container_distribution_configuration, dict):
            container_distribution_configuration = ImagebuilderDistributionConfigurationDistributionContainerDistributionConfiguration(**container_distribution_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5f4ad28eb403f6dc32bddc74a2954de227a362dcda05380ad082038c795fdea)
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument ami_distribution_configuration", value=ami_distribution_configuration, expected_type=type_hints["ami_distribution_configuration"])
            check_type(argname="argument container_distribution_configuration", value=container_distribution_configuration, expected_type=type_hints["container_distribution_configuration"])
            check_type(argname="argument fast_launch_configuration", value=fast_launch_configuration, expected_type=type_hints["fast_launch_configuration"])
            check_type(argname="argument launch_template_configuration", value=launch_template_configuration, expected_type=type_hints["launch_template_configuration"])
            check_type(argname="argument license_configuration_arns", value=license_configuration_arns, expected_type=type_hints["license_configuration_arns"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "region": region,
        }
        if ami_distribution_configuration is not None:
            self._values["ami_distribution_configuration"] = ami_distribution_configuration
        if container_distribution_configuration is not None:
            self._values["container_distribution_configuration"] = container_distribution_configuration
        if fast_launch_configuration is not None:
            self._values["fast_launch_configuration"] = fast_launch_configuration
        if launch_template_configuration is not None:
            self._values["launch_template_configuration"] = launch_template_configuration
        if license_configuration_arns is not None:
            self._values["license_configuration_arns"] = license_configuration_arns

    @builtins.property
    def region(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#region ImagebuilderDistributionConfiguration#region}.'''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ami_distribution_configuration(
        self,
    ) -> typing.Optional["ImagebuilderDistributionConfigurationDistributionAmiDistributionConfiguration"]:
        '''ami_distribution_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#ami_distribution_configuration ImagebuilderDistributionConfiguration#ami_distribution_configuration}
        '''
        result = self._values.get("ami_distribution_configuration")
        return typing.cast(typing.Optional["ImagebuilderDistributionConfigurationDistributionAmiDistributionConfiguration"], result)

    @builtins.property
    def container_distribution_configuration(
        self,
    ) -> typing.Optional["ImagebuilderDistributionConfigurationDistributionContainerDistributionConfiguration"]:
        '''container_distribution_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#container_distribution_configuration ImagebuilderDistributionConfiguration#container_distribution_configuration}
        '''
        result = self._values.get("container_distribution_configuration")
        return typing.cast(typing.Optional["ImagebuilderDistributionConfigurationDistributionContainerDistributionConfiguration"], result)

    @builtins.property
    def fast_launch_configuration(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ImagebuilderDistributionConfigurationDistributionFastLaunchConfiguration"]]]:
        '''fast_launch_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#fast_launch_configuration ImagebuilderDistributionConfiguration#fast_launch_configuration}
        '''
        result = self._values.get("fast_launch_configuration")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ImagebuilderDistributionConfigurationDistributionFastLaunchConfiguration"]]], result)

    @builtins.property
    def launch_template_configuration(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ImagebuilderDistributionConfigurationDistributionLaunchTemplateConfiguration"]]]:
        '''launch_template_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#launch_template_configuration ImagebuilderDistributionConfiguration#launch_template_configuration}
        '''
        result = self._values.get("launch_template_configuration")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ImagebuilderDistributionConfigurationDistributionLaunchTemplateConfiguration"]]], result)

    @builtins.property
    def license_configuration_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#license_configuration_arns ImagebuilderDistributionConfiguration#license_configuration_arns}.'''
        result = self._values.get("license_configuration_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ImagebuilderDistributionConfigurationDistribution(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.imagebuilderDistributionConfiguration.ImagebuilderDistributionConfigurationDistributionAmiDistributionConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "ami_tags": "amiTags",
        "description": "description",
        "kms_key_id": "kmsKeyId",
        "launch_permission": "launchPermission",
        "name": "name",
        "target_account_ids": "targetAccountIds",
    },
)
class ImagebuilderDistributionConfigurationDistributionAmiDistributionConfiguration:
    def __init__(
        self,
        *,
        ami_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        launch_permission: typing.Optional[typing.Union["ImagebuilderDistributionConfigurationDistributionAmiDistributionConfigurationLaunchPermission", typing.Dict[builtins.str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
        target_account_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param ami_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#ami_tags ImagebuilderDistributionConfiguration#ami_tags}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#description ImagebuilderDistributionConfiguration#description}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#kms_key_id ImagebuilderDistributionConfiguration#kms_key_id}.
        :param launch_permission: launch_permission block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#launch_permission ImagebuilderDistributionConfiguration#launch_permission}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#name ImagebuilderDistributionConfiguration#name}.
        :param target_account_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#target_account_ids ImagebuilderDistributionConfiguration#target_account_ids}.
        '''
        if isinstance(launch_permission, dict):
            launch_permission = ImagebuilderDistributionConfigurationDistributionAmiDistributionConfigurationLaunchPermission(**launch_permission)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af2113f82fc57222153e2ffb74623e61d8abd63e2be966126a310c6c76e779e6)
            check_type(argname="argument ami_tags", value=ami_tags, expected_type=type_hints["ami_tags"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument launch_permission", value=launch_permission, expected_type=type_hints["launch_permission"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument target_account_ids", value=target_account_ids, expected_type=type_hints["target_account_ids"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if ami_tags is not None:
            self._values["ami_tags"] = ami_tags
        if description is not None:
            self._values["description"] = description
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if launch_permission is not None:
            self._values["launch_permission"] = launch_permission
        if name is not None:
            self._values["name"] = name
        if target_account_ids is not None:
            self._values["target_account_ids"] = target_account_ids

    @builtins.property
    def ami_tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#ami_tags ImagebuilderDistributionConfiguration#ami_tags}.'''
        result = self._values.get("ami_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#description ImagebuilderDistributionConfiguration#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#kms_key_id ImagebuilderDistributionConfiguration#kms_key_id}.'''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def launch_permission(
        self,
    ) -> typing.Optional["ImagebuilderDistributionConfigurationDistributionAmiDistributionConfigurationLaunchPermission"]:
        '''launch_permission block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#launch_permission ImagebuilderDistributionConfiguration#launch_permission}
        '''
        result = self._values.get("launch_permission")
        return typing.cast(typing.Optional["ImagebuilderDistributionConfigurationDistributionAmiDistributionConfigurationLaunchPermission"], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#name ImagebuilderDistributionConfiguration#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_account_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#target_account_ids ImagebuilderDistributionConfiguration#target_account_ids}.'''
        result = self._values.get("target_account_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ImagebuilderDistributionConfigurationDistributionAmiDistributionConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.imagebuilderDistributionConfiguration.ImagebuilderDistributionConfigurationDistributionAmiDistributionConfigurationLaunchPermission",
    jsii_struct_bases=[],
    name_mapping={
        "organizational_unit_arns": "organizationalUnitArns",
        "organization_arns": "organizationArns",
        "user_groups": "userGroups",
        "user_ids": "userIds",
    },
)
class ImagebuilderDistributionConfigurationDistributionAmiDistributionConfigurationLaunchPermission:
    def __init__(
        self,
        *,
        organizational_unit_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        organization_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        user_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        user_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param organizational_unit_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#organizational_unit_arns ImagebuilderDistributionConfiguration#organizational_unit_arns}.
        :param organization_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#organization_arns ImagebuilderDistributionConfiguration#organization_arns}.
        :param user_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#user_groups ImagebuilderDistributionConfiguration#user_groups}.
        :param user_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#user_ids ImagebuilderDistributionConfiguration#user_ids}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b06ca2f73e555aa2b7e93057bc77814cd207567d65d8b4a978bc90f6288f363)
            check_type(argname="argument organizational_unit_arns", value=organizational_unit_arns, expected_type=type_hints["organizational_unit_arns"])
            check_type(argname="argument organization_arns", value=organization_arns, expected_type=type_hints["organization_arns"])
            check_type(argname="argument user_groups", value=user_groups, expected_type=type_hints["user_groups"])
            check_type(argname="argument user_ids", value=user_ids, expected_type=type_hints["user_ids"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if organizational_unit_arns is not None:
            self._values["organizational_unit_arns"] = organizational_unit_arns
        if organization_arns is not None:
            self._values["organization_arns"] = organization_arns
        if user_groups is not None:
            self._values["user_groups"] = user_groups
        if user_ids is not None:
            self._values["user_ids"] = user_ids

    @builtins.property
    def organizational_unit_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#organizational_unit_arns ImagebuilderDistributionConfiguration#organizational_unit_arns}.'''
        result = self._values.get("organizational_unit_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def organization_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#organization_arns ImagebuilderDistributionConfiguration#organization_arns}.'''
        result = self._values.get("organization_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def user_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#user_groups ImagebuilderDistributionConfiguration#user_groups}.'''
        result = self._values.get("user_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def user_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#user_ids ImagebuilderDistributionConfiguration#user_ids}.'''
        result = self._values.get("user_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ImagebuilderDistributionConfigurationDistributionAmiDistributionConfigurationLaunchPermission(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ImagebuilderDistributionConfigurationDistributionAmiDistributionConfigurationLaunchPermissionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.imagebuilderDistributionConfiguration.ImagebuilderDistributionConfigurationDistributionAmiDistributionConfigurationLaunchPermissionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2a247c3d04af937aacde73128a9960cf4fdeb1b4d5d345b7abbf746cf06e55be)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetOrganizationalUnitArns")
    def reset_organizational_unit_arns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrganizationalUnitArns", []))

    @jsii.member(jsii_name="resetOrganizationArns")
    def reset_organization_arns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrganizationArns", []))

    @jsii.member(jsii_name="resetUserGroups")
    def reset_user_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserGroups", []))

    @jsii.member(jsii_name="resetUserIds")
    def reset_user_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserIds", []))

    @builtins.property
    @jsii.member(jsii_name="organizationalUnitArnsInput")
    def organizational_unit_arns_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "organizationalUnitArnsInput"))

    @builtins.property
    @jsii.member(jsii_name="organizationArnsInput")
    def organization_arns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "organizationArnsInput"))

    @builtins.property
    @jsii.member(jsii_name="userGroupsInput")
    def user_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "userGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="userIdsInput")
    def user_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "userIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="organizationalUnitArns")
    def organizational_unit_arns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "organizationalUnitArns"))

    @organizational_unit_arns.setter
    def organizational_unit_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0115927d6a352d58242ace4e5c792098febdde41998114729d8589b7c2d19725)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organizationalUnitArns", value)

    @builtins.property
    @jsii.member(jsii_name="organizationArns")
    def organization_arns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "organizationArns"))

    @organization_arns.setter
    def organization_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3941d3aeb5fad101bc4f38f51d717763b8caab0b74006b4d89f23fde94996aa4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organizationArns", value)

    @builtins.property
    @jsii.member(jsii_name="userGroups")
    def user_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "userGroups"))

    @user_groups.setter
    def user_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8632eee77b06f89eb095449b590119dbcdb4c1db0d2e14723afa789c0074875f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userGroups", value)

    @builtins.property
    @jsii.member(jsii_name="userIds")
    def user_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "userIds"))

    @user_ids.setter
    def user_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9aac7b9ac92b00c22477bc0b950502e19f84415810436587a708eedccf88a994)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userIds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ImagebuilderDistributionConfigurationDistributionAmiDistributionConfigurationLaunchPermission]:
        return typing.cast(typing.Optional[ImagebuilderDistributionConfigurationDistributionAmiDistributionConfigurationLaunchPermission], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ImagebuilderDistributionConfigurationDistributionAmiDistributionConfigurationLaunchPermission],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc3baa87c071828dcb258510cf466e8e308e6a817e7eaaba103f6dee4d6207ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ImagebuilderDistributionConfigurationDistributionAmiDistributionConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.imagebuilderDistributionConfiguration.ImagebuilderDistributionConfigurationDistributionAmiDistributionConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e83123993f22f9c32af9097f0dba6502d04dfb73822eb5500604c1198a2e3a74)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putLaunchPermission")
    def put_launch_permission(
        self,
        *,
        organizational_unit_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        organization_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        user_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        user_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param organizational_unit_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#organizational_unit_arns ImagebuilderDistributionConfiguration#organizational_unit_arns}.
        :param organization_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#organization_arns ImagebuilderDistributionConfiguration#organization_arns}.
        :param user_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#user_groups ImagebuilderDistributionConfiguration#user_groups}.
        :param user_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#user_ids ImagebuilderDistributionConfiguration#user_ids}.
        '''
        value = ImagebuilderDistributionConfigurationDistributionAmiDistributionConfigurationLaunchPermission(
            organizational_unit_arns=organizational_unit_arns,
            organization_arns=organization_arns,
            user_groups=user_groups,
            user_ids=user_ids,
        )

        return typing.cast(None, jsii.invoke(self, "putLaunchPermission", [value]))

    @jsii.member(jsii_name="resetAmiTags")
    def reset_ami_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAmiTags", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetKmsKeyId")
    def reset_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyId", []))

    @jsii.member(jsii_name="resetLaunchPermission")
    def reset_launch_permission(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLaunchPermission", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetTargetAccountIds")
    def reset_target_account_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetAccountIds", []))

    @builtins.property
    @jsii.member(jsii_name="launchPermission")
    def launch_permission(
        self,
    ) -> ImagebuilderDistributionConfigurationDistributionAmiDistributionConfigurationLaunchPermissionOutputReference:
        return typing.cast(ImagebuilderDistributionConfigurationDistributionAmiDistributionConfigurationLaunchPermissionOutputReference, jsii.get(self, "launchPermission"))

    @builtins.property
    @jsii.member(jsii_name="amiTagsInput")
    def ami_tags_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "amiTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyIdInput")
    def kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="launchPermissionInput")
    def launch_permission_input(
        self,
    ) -> typing.Optional[ImagebuilderDistributionConfigurationDistributionAmiDistributionConfigurationLaunchPermission]:
        return typing.cast(typing.Optional[ImagebuilderDistributionConfigurationDistributionAmiDistributionConfigurationLaunchPermission], jsii.get(self, "launchPermissionInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="targetAccountIdsInput")
    def target_account_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "targetAccountIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="amiTags")
    def ami_tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "amiTags"))

    @ami_tags.setter
    def ami_tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4298259d9862ebb4211ec7f812a952b8ee86199f93961705c7526936c40f787d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "amiTags", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc7ca542b2bc065279b67b0b82fdcb9c188b8762b1cebc821e92ed742f84a2f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c20958e84983f3960fd8f1d9faee687f11840b75d3a605d6ad0c04f8b8bbece)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88d0e0e9a05b15030e1c963b076a127f9e163fe1930f47580a3f2b6512a2552c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="targetAccountIds")
    def target_account_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "targetAccountIds"))

    @target_account_ids.setter
    def target_account_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0368d8f5439fd51adac33b77cbe36c56a1bcfe9d0ebbd9a930d2e8fb8a8edc48)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetAccountIds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ImagebuilderDistributionConfigurationDistributionAmiDistributionConfiguration]:
        return typing.cast(typing.Optional[ImagebuilderDistributionConfigurationDistributionAmiDistributionConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ImagebuilderDistributionConfigurationDistributionAmiDistributionConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1365dd6df07c532656c70f2d4fef39fdc38b3e2f44bd7d97e6875cabd860b989)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.imagebuilderDistributionConfiguration.ImagebuilderDistributionConfigurationDistributionContainerDistributionConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "target_repository": "targetRepository",
        "container_tags": "containerTags",
        "description": "description",
    },
)
class ImagebuilderDistributionConfigurationDistributionContainerDistributionConfiguration:
    def __init__(
        self,
        *,
        target_repository: typing.Union["ImagebuilderDistributionConfigurationDistributionContainerDistributionConfigurationTargetRepository", typing.Dict[builtins.str, typing.Any]],
        container_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param target_repository: target_repository block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#target_repository ImagebuilderDistributionConfiguration#target_repository}
        :param container_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#container_tags ImagebuilderDistributionConfiguration#container_tags}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#description ImagebuilderDistributionConfiguration#description}.
        '''
        if isinstance(target_repository, dict):
            target_repository = ImagebuilderDistributionConfigurationDistributionContainerDistributionConfigurationTargetRepository(**target_repository)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__105f454e15b24e357ea7fd025ef96da5c36894804ceb94078e6977cc59b8ec17)
            check_type(argname="argument target_repository", value=target_repository, expected_type=type_hints["target_repository"])
            check_type(argname="argument container_tags", value=container_tags, expected_type=type_hints["container_tags"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "target_repository": target_repository,
        }
        if container_tags is not None:
            self._values["container_tags"] = container_tags
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def target_repository(
        self,
    ) -> "ImagebuilderDistributionConfigurationDistributionContainerDistributionConfigurationTargetRepository":
        '''target_repository block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#target_repository ImagebuilderDistributionConfiguration#target_repository}
        '''
        result = self._values.get("target_repository")
        assert result is not None, "Required property 'target_repository' is missing"
        return typing.cast("ImagebuilderDistributionConfigurationDistributionContainerDistributionConfigurationTargetRepository", result)

    @builtins.property
    def container_tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#container_tags ImagebuilderDistributionConfiguration#container_tags}.'''
        result = self._values.get("container_tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#description ImagebuilderDistributionConfiguration#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ImagebuilderDistributionConfigurationDistributionContainerDistributionConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ImagebuilderDistributionConfigurationDistributionContainerDistributionConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.imagebuilderDistributionConfiguration.ImagebuilderDistributionConfigurationDistributionContainerDistributionConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__287c367684b749dc1caf1af375bf47de3f207eddce772d0b45fdb0b7150165cc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putTargetRepository")
    def put_target_repository(
        self,
        *,
        repository_name: builtins.str,
        service: builtins.str,
    ) -> None:
        '''
        :param repository_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#repository_name ImagebuilderDistributionConfiguration#repository_name}.
        :param service: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#service ImagebuilderDistributionConfiguration#service}.
        '''
        value = ImagebuilderDistributionConfigurationDistributionContainerDistributionConfigurationTargetRepository(
            repository_name=repository_name, service=service
        )

        return typing.cast(None, jsii.invoke(self, "putTargetRepository", [value]))

    @jsii.member(jsii_name="resetContainerTags")
    def reset_container_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainerTags", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @builtins.property
    @jsii.member(jsii_name="targetRepository")
    def target_repository(
        self,
    ) -> "ImagebuilderDistributionConfigurationDistributionContainerDistributionConfigurationTargetRepositoryOutputReference":
        return typing.cast("ImagebuilderDistributionConfigurationDistributionContainerDistributionConfigurationTargetRepositoryOutputReference", jsii.get(self, "targetRepository"))

    @builtins.property
    @jsii.member(jsii_name="containerTagsInput")
    def container_tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "containerTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="targetRepositoryInput")
    def target_repository_input(
        self,
    ) -> typing.Optional["ImagebuilderDistributionConfigurationDistributionContainerDistributionConfigurationTargetRepository"]:
        return typing.cast(typing.Optional["ImagebuilderDistributionConfigurationDistributionContainerDistributionConfigurationTargetRepository"], jsii.get(self, "targetRepositoryInput"))

    @builtins.property
    @jsii.member(jsii_name="containerTags")
    def container_tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "containerTags"))

    @container_tags.setter
    def container_tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce7e631753b115de8bfa03c4890944c89bb83e743930ba9c3413f143ad9da8a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerTags", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f31e480e2dde41bc7a090f566e704f3566be69d36a47879320e48a5eec8ff19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ImagebuilderDistributionConfigurationDistributionContainerDistributionConfiguration]:
        return typing.cast(typing.Optional[ImagebuilderDistributionConfigurationDistributionContainerDistributionConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ImagebuilderDistributionConfigurationDistributionContainerDistributionConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f847f22b0d05c23e729ee349074b68cbd6866c1564e13fffb67dc32ea40be4e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.imagebuilderDistributionConfiguration.ImagebuilderDistributionConfigurationDistributionContainerDistributionConfigurationTargetRepository",
    jsii_struct_bases=[],
    name_mapping={"repository_name": "repositoryName", "service": "service"},
)
class ImagebuilderDistributionConfigurationDistributionContainerDistributionConfigurationTargetRepository:
    def __init__(self, *, repository_name: builtins.str, service: builtins.str) -> None:
        '''
        :param repository_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#repository_name ImagebuilderDistributionConfiguration#repository_name}.
        :param service: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#service ImagebuilderDistributionConfiguration#service}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee0e4f39b437f1015d7d43294c8d1d520472f98439420c1bafee5e6f22d455f7)
            check_type(argname="argument repository_name", value=repository_name, expected_type=type_hints["repository_name"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "repository_name": repository_name,
            "service": service,
        }

    @builtins.property
    def repository_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#repository_name ImagebuilderDistributionConfiguration#repository_name}.'''
        result = self._values.get("repository_name")
        assert result is not None, "Required property 'repository_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#service ImagebuilderDistributionConfiguration#service}.'''
        result = self._values.get("service")
        assert result is not None, "Required property 'service' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ImagebuilderDistributionConfigurationDistributionContainerDistributionConfigurationTargetRepository(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ImagebuilderDistributionConfigurationDistributionContainerDistributionConfigurationTargetRepositoryOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.imagebuilderDistributionConfiguration.ImagebuilderDistributionConfigurationDistributionContainerDistributionConfigurationTargetRepositoryOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7a6fe10a976f8d7a49052a411bf79c8a24bd85885bea9dd9382cf72d7465316e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="repositoryNameInput")
    def repository_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repositoryNameInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceInput")
    def service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceInput"))

    @builtins.property
    @jsii.member(jsii_name="repositoryName")
    def repository_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repositoryName"))

    @repository_name.setter
    def repository_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9469422f1ef035f6ffc51c857357f3bc8e883e7480612a5ef0203ba0e1c77ff2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repositoryName", value)

    @builtins.property
    @jsii.member(jsii_name="service")
    def service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "service"))

    @service.setter
    def service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6ffb5b3c5d1f1aa064ade41ec6952d277fc1e017a475b98bea520adfdb95f8c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "service", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ImagebuilderDistributionConfigurationDistributionContainerDistributionConfigurationTargetRepository]:
        return typing.cast(typing.Optional[ImagebuilderDistributionConfigurationDistributionContainerDistributionConfigurationTargetRepository], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ImagebuilderDistributionConfigurationDistributionContainerDistributionConfigurationTargetRepository],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b62e142fd3bc0da9cfe122304eb8559ac8b8332a509a5a20795ce4f616eddb2a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.imagebuilderDistributionConfiguration.ImagebuilderDistributionConfigurationDistributionFastLaunchConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "account_id": "accountId",
        "enabled": "enabled",
        "launch_template": "launchTemplate",
        "max_parallel_launches": "maxParallelLaunches",
        "snapshot_configuration": "snapshotConfiguration",
    },
)
class ImagebuilderDistributionConfigurationDistributionFastLaunchConfiguration:
    def __init__(
        self,
        *,
        account_id: builtins.str,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        launch_template: typing.Optional[typing.Union["ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationLaunchTemplate", typing.Dict[builtins.str, typing.Any]]] = None,
        max_parallel_launches: typing.Optional[jsii.Number] = None,
        snapshot_configuration: typing.Optional[typing.Union["ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationSnapshotConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#account_id ImagebuilderDistributionConfiguration#account_id}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#enabled ImagebuilderDistributionConfiguration#enabled}.
        :param launch_template: launch_template block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#launch_template ImagebuilderDistributionConfiguration#launch_template}
        :param max_parallel_launches: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#max_parallel_launches ImagebuilderDistributionConfiguration#max_parallel_launches}.
        :param snapshot_configuration: snapshot_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#snapshot_configuration ImagebuilderDistributionConfiguration#snapshot_configuration}
        '''
        if isinstance(launch_template, dict):
            launch_template = ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationLaunchTemplate(**launch_template)
        if isinstance(snapshot_configuration, dict):
            snapshot_configuration = ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationSnapshotConfiguration(**snapshot_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8512f6029406c8a09501d3c8f29f21af0c03816cfc9db7f77b61a27ca6697458)
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument launch_template", value=launch_template, expected_type=type_hints["launch_template"])
            check_type(argname="argument max_parallel_launches", value=max_parallel_launches, expected_type=type_hints["max_parallel_launches"])
            check_type(argname="argument snapshot_configuration", value=snapshot_configuration, expected_type=type_hints["snapshot_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account_id": account_id,
            "enabled": enabled,
        }
        if launch_template is not None:
            self._values["launch_template"] = launch_template
        if max_parallel_launches is not None:
            self._values["max_parallel_launches"] = max_parallel_launches
        if snapshot_configuration is not None:
            self._values["snapshot_configuration"] = snapshot_configuration

    @builtins.property
    def account_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#account_id ImagebuilderDistributionConfiguration#account_id}.'''
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#enabled ImagebuilderDistributionConfiguration#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def launch_template(
        self,
    ) -> typing.Optional["ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationLaunchTemplate"]:
        '''launch_template block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#launch_template ImagebuilderDistributionConfiguration#launch_template}
        '''
        result = self._values.get("launch_template")
        return typing.cast(typing.Optional["ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationLaunchTemplate"], result)

    @builtins.property
    def max_parallel_launches(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#max_parallel_launches ImagebuilderDistributionConfiguration#max_parallel_launches}.'''
        result = self._values.get("max_parallel_launches")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def snapshot_configuration(
        self,
    ) -> typing.Optional["ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationSnapshotConfiguration"]:
        '''snapshot_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#snapshot_configuration ImagebuilderDistributionConfiguration#snapshot_configuration}
        '''
        result = self._values.get("snapshot_configuration")
        return typing.cast(typing.Optional["ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationSnapshotConfiguration"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ImagebuilderDistributionConfigurationDistributionFastLaunchConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.imagebuilderDistributionConfiguration.ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationLaunchTemplate",
    jsii_struct_bases=[],
    name_mapping={
        "launch_template_id": "launchTemplateId",
        "launch_template_name": "launchTemplateName",
        "launch_template_version": "launchTemplateVersion",
    },
)
class ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationLaunchTemplate:
    def __init__(
        self,
        *,
        launch_template_id: typing.Optional[builtins.str] = None,
        launch_template_name: typing.Optional[builtins.str] = None,
        launch_template_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param launch_template_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#launch_template_id ImagebuilderDistributionConfiguration#launch_template_id}.
        :param launch_template_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#launch_template_name ImagebuilderDistributionConfiguration#launch_template_name}.
        :param launch_template_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#launch_template_version ImagebuilderDistributionConfiguration#launch_template_version}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b47ea8031551ca9a71ceec32d76063da8d65bbf160522de004f32ceecacb24c)
            check_type(argname="argument launch_template_id", value=launch_template_id, expected_type=type_hints["launch_template_id"])
            check_type(argname="argument launch_template_name", value=launch_template_name, expected_type=type_hints["launch_template_name"])
            check_type(argname="argument launch_template_version", value=launch_template_version, expected_type=type_hints["launch_template_version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if launch_template_id is not None:
            self._values["launch_template_id"] = launch_template_id
        if launch_template_name is not None:
            self._values["launch_template_name"] = launch_template_name
        if launch_template_version is not None:
            self._values["launch_template_version"] = launch_template_version

    @builtins.property
    def launch_template_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#launch_template_id ImagebuilderDistributionConfiguration#launch_template_id}.'''
        result = self._values.get("launch_template_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def launch_template_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#launch_template_name ImagebuilderDistributionConfiguration#launch_template_name}.'''
        result = self._values.get("launch_template_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def launch_template_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#launch_template_version ImagebuilderDistributionConfiguration#launch_template_version}.'''
        result = self._values.get("launch_template_version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationLaunchTemplate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationLaunchTemplateOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.imagebuilderDistributionConfiguration.ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationLaunchTemplateOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9b2c74c5e124a066693156cc82c14a7d0b365ad15857c6f083b6ad18a0345232)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetLaunchTemplateId")
    def reset_launch_template_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLaunchTemplateId", []))

    @jsii.member(jsii_name="resetLaunchTemplateName")
    def reset_launch_template_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLaunchTemplateName", []))

    @jsii.member(jsii_name="resetLaunchTemplateVersion")
    def reset_launch_template_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLaunchTemplateVersion", []))

    @builtins.property
    @jsii.member(jsii_name="launchTemplateIdInput")
    def launch_template_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "launchTemplateIdInput"))

    @builtins.property
    @jsii.member(jsii_name="launchTemplateNameInput")
    def launch_template_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "launchTemplateNameInput"))

    @builtins.property
    @jsii.member(jsii_name="launchTemplateVersionInput")
    def launch_template_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "launchTemplateVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="launchTemplateId")
    def launch_template_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "launchTemplateId"))

    @launch_template_id.setter
    def launch_template_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d553c6eacc2b8759643c51275d932853d9b901d00a2e93a5720268fc1d3384a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "launchTemplateId", value)

    @builtins.property
    @jsii.member(jsii_name="launchTemplateName")
    def launch_template_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "launchTemplateName"))

    @launch_template_name.setter
    def launch_template_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e399a35b6608c369264ff04d070900f14f21303cb3a36d7bdde483da1a5c5deb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "launchTemplateName", value)

    @builtins.property
    @jsii.member(jsii_name="launchTemplateVersion")
    def launch_template_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "launchTemplateVersion"))

    @launch_template_version.setter
    def launch_template_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c81b3cfb19fab4ad7b469811422f837c5981c57fd6215a118af7dd2230fe2fe1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "launchTemplateVersion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationLaunchTemplate]:
        return typing.cast(typing.Optional[ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationLaunchTemplate], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationLaunchTemplate],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33c6c89120441964dc0ebdbdd6f5624dfbf4904258e2651537418dae16c0b595)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.imagebuilderDistributionConfiguration.ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__931930363c41ea48f45ea800b29b2bb10a85fe2bfe5a6eae2e9d128d422cbab0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d9df93ca88019daacbd6f37e5dcf191254c115e14b0a2184668d69ac7824d66)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94c53aff9a77919ba1245592172070bb682a4b42e4117e8f9eeb089683403ac8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bcdf8637aa0c7b0904bf57819986369c3d273f4b3b98f7ceec7418d57c8cdf55)
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
            type_hints = typing.get_type_hints(_typecheckingstub__dd3a4a95b566be914d2399241433bc6a0d04204d0bbd5c30a14d9b0703caf0a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ImagebuilderDistributionConfigurationDistributionFastLaunchConfiguration]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ImagebuilderDistributionConfigurationDistributionFastLaunchConfiguration]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ImagebuilderDistributionConfigurationDistributionFastLaunchConfiguration]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73a8010c6fc33567e5d9e7191c089d92fd73d3c77639990182c14dc144f5bac4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.imagebuilderDistributionConfiguration.ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2cf8687c51e08bfaee4eb1b4012b2cbc47d73ca74c792ed39b9d13d0e1a1541d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putLaunchTemplate")
    def put_launch_template(
        self,
        *,
        launch_template_id: typing.Optional[builtins.str] = None,
        launch_template_name: typing.Optional[builtins.str] = None,
        launch_template_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param launch_template_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#launch_template_id ImagebuilderDistributionConfiguration#launch_template_id}.
        :param launch_template_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#launch_template_name ImagebuilderDistributionConfiguration#launch_template_name}.
        :param launch_template_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#launch_template_version ImagebuilderDistributionConfiguration#launch_template_version}.
        '''
        value = ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationLaunchTemplate(
            launch_template_id=launch_template_id,
            launch_template_name=launch_template_name,
            launch_template_version=launch_template_version,
        )

        return typing.cast(None, jsii.invoke(self, "putLaunchTemplate", [value]))

    @jsii.member(jsii_name="putSnapshotConfiguration")
    def put_snapshot_configuration(
        self,
        *,
        target_resource_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param target_resource_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#target_resource_count ImagebuilderDistributionConfiguration#target_resource_count}.
        '''
        value = ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationSnapshotConfiguration(
            target_resource_count=target_resource_count
        )

        return typing.cast(None, jsii.invoke(self, "putSnapshotConfiguration", [value]))

    @jsii.member(jsii_name="resetLaunchTemplate")
    def reset_launch_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLaunchTemplate", []))

    @jsii.member(jsii_name="resetMaxParallelLaunches")
    def reset_max_parallel_launches(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxParallelLaunches", []))

    @jsii.member(jsii_name="resetSnapshotConfiguration")
    def reset_snapshot_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSnapshotConfiguration", []))

    @builtins.property
    @jsii.member(jsii_name="launchTemplate")
    def launch_template(
        self,
    ) -> ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationLaunchTemplateOutputReference:
        return typing.cast(ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationLaunchTemplateOutputReference, jsii.get(self, "launchTemplate"))

    @builtins.property
    @jsii.member(jsii_name="snapshotConfiguration")
    def snapshot_configuration(
        self,
    ) -> "ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationSnapshotConfigurationOutputReference":
        return typing.cast("ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationSnapshotConfigurationOutputReference", jsii.get(self, "snapshotConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="launchTemplateInput")
    def launch_template_input(
        self,
    ) -> typing.Optional[ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationLaunchTemplate]:
        return typing.cast(typing.Optional[ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationLaunchTemplate], jsii.get(self, "launchTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="maxParallelLaunchesInput")
    def max_parallel_launches_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxParallelLaunchesInput"))

    @builtins.property
    @jsii.member(jsii_name="snapshotConfigurationInput")
    def snapshot_configuration_input(
        self,
    ) -> typing.Optional["ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationSnapshotConfiguration"]:
        return typing.cast(typing.Optional["ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationSnapshotConfiguration"], jsii.get(self, "snapshotConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b0909be231ec2e8498f3042abce802ee05eaad039412db65d5bcbd0acc47c57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5d35ed988ed112ce6bed093d2159ad70be8a3715aaa25f8f7cd7fd67f7e1fd6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="maxParallelLaunches")
    def max_parallel_launches(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxParallelLaunches"))

    @max_parallel_launches.setter
    def max_parallel_launches(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5309a40a77256e52009118df3fcf5b37afe199625d8b4347b3e77329fa61efe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxParallelLaunches", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ImagebuilderDistributionConfigurationDistributionFastLaunchConfiguration, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ImagebuilderDistributionConfigurationDistributionFastLaunchConfiguration, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ImagebuilderDistributionConfigurationDistributionFastLaunchConfiguration, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9819877d0920f3d076d01f1dd248a0491ed7c921e86d3d8085a2ba525995171)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.imagebuilderDistributionConfiguration.ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationSnapshotConfiguration",
    jsii_struct_bases=[],
    name_mapping={"target_resource_count": "targetResourceCount"},
)
class ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationSnapshotConfiguration:
    def __init__(
        self,
        *,
        target_resource_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param target_resource_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#target_resource_count ImagebuilderDistributionConfiguration#target_resource_count}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72f50119787327dccf47605d8baf37c2d001b1e7f4521084708d76ece82814db)
            check_type(argname="argument target_resource_count", value=target_resource_count, expected_type=type_hints["target_resource_count"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if target_resource_count is not None:
            self._values["target_resource_count"] = target_resource_count

    @builtins.property
    def target_resource_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#target_resource_count ImagebuilderDistributionConfiguration#target_resource_count}.'''
        result = self._values.get("target_resource_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationSnapshotConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationSnapshotConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.imagebuilderDistributionConfiguration.ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationSnapshotConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f3873b45d9f91fcaf8229f78dce493d945a7078b5c35d133c17511c2f018d603)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetTargetResourceCount")
    def reset_target_resource_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetResourceCount", []))

    @builtins.property
    @jsii.member(jsii_name="targetResourceCountInput")
    def target_resource_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "targetResourceCountInput"))

    @builtins.property
    @jsii.member(jsii_name="targetResourceCount")
    def target_resource_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "targetResourceCount"))

    @target_resource_count.setter
    def target_resource_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d0d10b08577a8280ed943217a1d4ec17a253b74dce6b80f1b6c979ede7820c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetResourceCount", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationSnapshotConfiguration]:
        return typing.cast(typing.Optional[ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationSnapshotConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationSnapshotConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4faa9fc8920ec0603eab1c2872d5fdaad752bdb2ed88c091e23db5b5957e3d2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.imagebuilderDistributionConfiguration.ImagebuilderDistributionConfigurationDistributionLaunchTemplateConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "launch_template_id": "launchTemplateId",
        "account_id": "accountId",
        "default": "default",
    },
)
class ImagebuilderDistributionConfigurationDistributionLaunchTemplateConfiguration:
    def __init__(
        self,
        *,
        launch_template_id: builtins.str,
        account_id: typing.Optional[builtins.str] = None,
        default: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param launch_template_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#launch_template_id ImagebuilderDistributionConfiguration#launch_template_id}.
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#account_id ImagebuilderDistributionConfiguration#account_id}.
        :param default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#default ImagebuilderDistributionConfiguration#default}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__224233e6a2342f327842a127d347f88f1d647e6791169cf583c38321f0989ae2)
            check_type(argname="argument launch_template_id", value=launch_template_id, expected_type=type_hints["launch_template_id"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument default", value=default, expected_type=type_hints["default"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "launch_template_id": launch_template_id,
        }
        if account_id is not None:
            self._values["account_id"] = account_id
        if default is not None:
            self._values["default"] = default

    @builtins.property
    def launch_template_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#launch_template_id ImagebuilderDistributionConfiguration#launch_template_id}.'''
        result = self._values.get("launch_template_id")
        assert result is not None, "Required property 'launch_template_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#account_id ImagebuilderDistributionConfiguration#account_id}.'''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#default ImagebuilderDistributionConfiguration#default}.'''
        result = self._values.get("default")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ImagebuilderDistributionConfigurationDistributionLaunchTemplateConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ImagebuilderDistributionConfigurationDistributionLaunchTemplateConfigurationList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.imagebuilderDistributionConfiguration.ImagebuilderDistributionConfigurationDistributionLaunchTemplateConfigurationList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3713549757a3d4bb18f7023b69e6e90fd53cdb6abf74e2b99152e793e6c9d4e8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ImagebuilderDistributionConfigurationDistributionLaunchTemplateConfigurationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93fb4a825c97919e0b09209e617e342afd4180ed7df8299997492b2fa025a322)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ImagebuilderDistributionConfigurationDistributionLaunchTemplateConfigurationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a9158d0bb70fedd511202d4a6990aa3f521da77bb91a42a76ba05f42f4588e8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__dadfa6783a47f5f1c2e5b41018acec9f577215cdfd90e2170b0de88022df8523)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8466777eea7af4e4ec93e8654a96f22dd94882c0d4ed9612202ff8939cd462df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ImagebuilderDistributionConfigurationDistributionLaunchTemplateConfiguration]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ImagebuilderDistributionConfigurationDistributionLaunchTemplateConfiguration]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ImagebuilderDistributionConfigurationDistributionLaunchTemplateConfiguration]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fac640ec537ce5bf0578c4bfcf8820b1216f5a828aefc028372587a5a1471bfb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ImagebuilderDistributionConfigurationDistributionLaunchTemplateConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.imagebuilderDistributionConfiguration.ImagebuilderDistributionConfigurationDistributionLaunchTemplateConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__77f9ca354afdfb7e7cfc9f0b76300bafea17cc73b5a9c468abb2ca2d7421e429)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAccountId")
    def reset_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountId", []))

    @jsii.member(jsii_name="resetDefault")
    def reset_default(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefault", []))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultInput")
    def default_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "defaultInput"))

    @builtins.property
    @jsii.member(jsii_name="launchTemplateIdInput")
    def launch_template_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "launchTemplateIdInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78a933257458db864855b150dc3e8afb47e97441ae2395b748d0c1980919c997)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="default")
    def default(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "default"))

    @default.setter
    def default(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa9d5e34c82bd5eb8ed0fa20750a5da3e70f88e6a116b95d13050634f62240e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "default", value)

    @builtins.property
    @jsii.member(jsii_name="launchTemplateId")
    def launch_template_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "launchTemplateId"))

    @launch_template_id.setter
    def launch_template_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f673293c8e560233c6bf3c3134233e62026254a034800599501993c5d1e5797d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "launchTemplateId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ImagebuilderDistributionConfigurationDistributionLaunchTemplateConfiguration, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ImagebuilderDistributionConfigurationDistributionLaunchTemplateConfiguration, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ImagebuilderDistributionConfigurationDistributionLaunchTemplateConfiguration, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8d86b1702bf5c11c2a77ece5af9b8ff98a680f5805908a964ccfd85830c8101)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ImagebuilderDistributionConfigurationDistributionList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.imagebuilderDistributionConfiguration.ImagebuilderDistributionConfigurationDistributionList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__455a7142d9335f19002bfd1217ff1cc9fc460bfdcdf346241671aabec4d86131)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ImagebuilderDistributionConfigurationDistributionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6657dbd5c0ad68e732560a48dd69ebf51d9e4507b1b71e3e417772f20227daf7)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ImagebuilderDistributionConfigurationDistributionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fcb82332b00c809a797f5151f8c6e1cc190d3386adc9b7d4a26d1e443eec1975)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0b96597f83b5f94e29a7a7252fc0300f7ec80889621279510f4c26091d6a5fa2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b39787b2fc6e88a3c290136bc0ad99443fcf3920ad5a2cc020c4ec287b9bbecb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ImagebuilderDistributionConfigurationDistribution]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ImagebuilderDistributionConfigurationDistribution]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ImagebuilderDistributionConfigurationDistribution]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21dc6d622efe69a70b8e483044196469219007608c09cd098cb6154c629b83d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ImagebuilderDistributionConfigurationDistributionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.imagebuilderDistributionConfiguration.ImagebuilderDistributionConfigurationDistributionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8a9e6d5d11d79e7fc4763735f84cb6c73d6a0152aeec88b7e7d6bfcce5a59116)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAmiDistributionConfiguration")
    def put_ami_distribution_configuration(
        self,
        *,
        ami_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        launch_permission: typing.Optional[typing.Union[ImagebuilderDistributionConfigurationDistributionAmiDistributionConfigurationLaunchPermission, typing.Dict[builtins.str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
        target_account_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param ami_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#ami_tags ImagebuilderDistributionConfiguration#ami_tags}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#description ImagebuilderDistributionConfiguration#description}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#kms_key_id ImagebuilderDistributionConfiguration#kms_key_id}.
        :param launch_permission: launch_permission block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#launch_permission ImagebuilderDistributionConfiguration#launch_permission}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#name ImagebuilderDistributionConfiguration#name}.
        :param target_account_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#target_account_ids ImagebuilderDistributionConfiguration#target_account_ids}.
        '''
        value = ImagebuilderDistributionConfigurationDistributionAmiDistributionConfiguration(
            ami_tags=ami_tags,
            description=description,
            kms_key_id=kms_key_id,
            launch_permission=launch_permission,
            name=name,
            target_account_ids=target_account_ids,
        )

        return typing.cast(None, jsii.invoke(self, "putAmiDistributionConfiguration", [value]))

    @jsii.member(jsii_name="putContainerDistributionConfiguration")
    def put_container_distribution_configuration(
        self,
        *,
        target_repository: typing.Union[ImagebuilderDistributionConfigurationDistributionContainerDistributionConfigurationTargetRepository, typing.Dict[builtins.str, typing.Any]],
        container_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param target_repository: target_repository block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#target_repository ImagebuilderDistributionConfiguration#target_repository}
        :param container_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#container_tags ImagebuilderDistributionConfiguration#container_tags}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/imagebuilder_distribution_configuration#description ImagebuilderDistributionConfiguration#description}.
        '''
        value = ImagebuilderDistributionConfigurationDistributionContainerDistributionConfiguration(
            target_repository=target_repository,
            container_tags=container_tags,
            description=description,
        )

        return typing.cast(None, jsii.invoke(self, "putContainerDistributionConfiguration", [value]))

    @jsii.member(jsii_name="putFastLaunchConfiguration")
    def put_fast_launch_configuration(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ImagebuilderDistributionConfigurationDistributionFastLaunchConfiguration, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__680af109fe31d001aaa43b560ad2a31700bcecbf671f61105caa230e84f70b55)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFastLaunchConfiguration", [value]))

    @jsii.member(jsii_name="putLaunchTemplateConfiguration")
    def put_launch_template_configuration(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ImagebuilderDistributionConfigurationDistributionLaunchTemplateConfiguration, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b8b4c8844c058107bcff2a389e65f012aabfefbda46955913f26e9963807252)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLaunchTemplateConfiguration", [value]))

    @jsii.member(jsii_name="resetAmiDistributionConfiguration")
    def reset_ami_distribution_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAmiDistributionConfiguration", []))

    @jsii.member(jsii_name="resetContainerDistributionConfiguration")
    def reset_container_distribution_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainerDistributionConfiguration", []))

    @jsii.member(jsii_name="resetFastLaunchConfiguration")
    def reset_fast_launch_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFastLaunchConfiguration", []))

    @jsii.member(jsii_name="resetLaunchTemplateConfiguration")
    def reset_launch_template_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLaunchTemplateConfiguration", []))

    @jsii.member(jsii_name="resetLicenseConfigurationArns")
    def reset_license_configuration_arns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLicenseConfigurationArns", []))

    @builtins.property
    @jsii.member(jsii_name="amiDistributionConfiguration")
    def ami_distribution_configuration(
        self,
    ) -> ImagebuilderDistributionConfigurationDistributionAmiDistributionConfigurationOutputReference:
        return typing.cast(ImagebuilderDistributionConfigurationDistributionAmiDistributionConfigurationOutputReference, jsii.get(self, "amiDistributionConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="containerDistributionConfiguration")
    def container_distribution_configuration(
        self,
    ) -> ImagebuilderDistributionConfigurationDistributionContainerDistributionConfigurationOutputReference:
        return typing.cast(ImagebuilderDistributionConfigurationDistributionContainerDistributionConfigurationOutputReference, jsii.get(self, "containerDistributionConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="fastLaunchConfiguration")
    def fast_launch_configuration(
        self,
    ) -> ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationList:
        return typing.cast(ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationList, jsii.get(self, "fastLaunchConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="launchTemplateConfiguration")
    def launch_template_configuration(
        self,
    ) -> ImagebuilderDistributionConfigurationDistributionLaunchTemplateConfigurationList:
        return typing.cast(ImagebuilderDistributionConfigurationDistributionLaunchTemplateConfigurationList, jsii.get(self, "launchTemplateConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="amiDistributionConfigurationInput")
    def ami_distribution_configuration_input(
        self,
    ) -> typing.Optional[ImagebuilderDistributionConfigurationDistributionAmiDistributionConfiguration]:
        return typing.cast(typing.Optional[ImagebuilderDistributionConfigurationDistributionAmiDistributionConfiguration], jsii.get(self, "amiDistributionConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="containerDistributionConfigurationInput")
    def container_distribution_configuration_input(
        self,
    ) -> typing.Optional[ImagebuilderDistributionConfigurationDistributionContainerDistributionConfiguration]:
        return typing.cast(typing.Optional[ImagebuilderDistributionConfigurationDistributionContainerDistributionConfiguration], jsii.get(self, "containerDistributionConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="fastLaunchConfigurationInput")
    def fast_launch_configuration_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ImagebuilderDistributionConfigurationDistributionFastLaunchConfiguration]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ImagebuilderDistributionConfigurationDistributionFastLaunchConfiguration]]], jsii.get(self, "fastLaunchConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="launchTemplateConfigurationInput")
    def launch_template_configuration_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ImagebuilderDistributionConfigurationDistributionLaunchTemplateConfiguration]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ImagebuilderDistributionConfigurationDistributionLaunchTemplateConfiguration]]], jsii.get(self, "launchTemplateConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="licenseConfigurationArnsInput")
    def license_configuration_arns_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "licenseConfigurationArnsInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="licenseConfigurationArns")
    def license_configuration_arns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "licenseConfigurationArns"))

    @license_configuration_arns.setter
    def license_configuration_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d955d1c117811dfda56eebe733ff56adfd98965412c06f3f3d7f6e7de7cf46cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "licenseConfigurationArns", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__712e8f76145fea675b83fed4d301c73934435690fd94421696885c020bd59d3e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ImagebuilderDistributionConfigurationDistribution, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ImagebuilderDistributionConfigurationDistribution, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ImagebuilderDistributionConfigurationDistribution, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46a11779368f463d6c520c91988256562b79cfa6824f60b3db870cd9e046e52b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ImagebuilderDistributionConfiguration",
    "ImagebuilderDistributionConfigurationConfig",
    "ImagebuilderDistributionConfigurationDistribution",
    "ImagebuilderDistributionConfigurationDistributionAmiDistributionConfiguration",
    "ImagebuilderDistributionConfigurationDistributionAmiDistributionConfigurationLaunchPermission",
    "ImagebuilderDistributionConfigurationDistributionAmiDistributionConfigurationLaunchPermissionOutputReference",
    "ImagebuilderDistributionConfigurationDistributionAmiDistributionConfigurationOutputReference",
    "ImagebuilderDistributionConfigurationDistributionContainerDistributionConfiguration",
    "ImagebuilderDistributionConfigurationDistributionContainerDistributionConfigurationOutputReference",
    "ImagebuilderDistributionConfigurationDistributionContainerDistributionConfigurationTargetRepository",
    "ImagebuilderDistributionConfigurationDistributionContainerDistributionConfigurationTargetRepositoryOutputReference",
    "ImagebuilderDistributionConfigurationDistributionFastLaunchConfiguration",
    "ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationLaunchTemplate",
    "ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationLaunchTemplateOutputReference",
    "ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationList",
    "ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationOutputReference",
    "ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationSnapshotConfiguration",
    "ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationSnapshotConfigurationOutputReference",
    "ImagebuilderDistributionConfigurationDistributionLaunchTemplateConfiguration",
    "ImagebuilderDistributionConfigurationDistributionLaunchTemplateConfigurationList",
    "ImagebuilderDistributionConfigurationDistributionLaunchTemplateConfigurationOutputReference",
    "ImagebuilderDistributionConfigurationDistributionList",
    "ImagebuilderDistributionConfigurationDistributionOutputReference",
]

publication.publish()

def _typecheckingstub__9f66cb2e0c73c974e296447c0da2980036bb6aded7dcc62538a75f8ea9671faf(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    distribution: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ImagebuilderDistributionConfigurationDistribution, typing.Dict[builtins.str, typing.Any]]]],
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__72d72c233d7cd6bfae7e2b5ef2337e1a5602618600a19029d6b150b1906024d2(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ImagebuilderDistributionConfigurationDistribution, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c97858b6a58825d148a33950d790c7a41b89a455ec21d8392f55d1f234b1ae5c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__818de1fa368e63955893d93642196ccc1c7185d6a5f11cd446383a36950fa49f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7a9fd11f9a30783c5efd1a62d04ceaa728f56a338a14b33ecb833a76bbfdfdb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__601518209bc0f1489473620ae06f54b01c9bd4d3787ffa5106ae04f22e16a507(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f0c39485cdf4a2c75cf3db5919f00caafd6a90ff869d1a22026d7ce6aed27fd(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2065fdc685463367e51a39f8bf47f1c8ae9cc8058aa0dddb90b90792acc6fbf9(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    distribution: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ImagebuilderDistributionConfigurationDistribution, typing.Dict[builtins.str, typing.Any]]]],
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5f4ad28eb403f6dc32bddc74a2954de227a362dcda05380ad082038c795fdea(
    *,
    region: builtins.str,
    ami_distribution_configuration: typing.Optional[typing.Union[ImagebuilderDistributionConfigurationDistributionAmiDistributionConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    container_distribution_configuration: typing.Optional[typing.Union[ImagebuilderDistributionConfigurationDistributionContainerDistributionConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    fast_launch_configuration: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ImagebuilderDistributionConfigurationDistributionFastLaunchConfiguration, typing.Dict[builtins.str, typing.Any]]]]] = None,
    launch_template_configuration: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ImagebuilderDistributionConfigurationDistributionLaunchTemplateConfiguration, typing.Dict[builtins.str, typing.Any]]]]] = None,
    license_configuration_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af2113f82fc57222153e2ffb74623e61d8abd63e2be966126a310c6c76e779e6(
    *,
    ami_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    description: typing.Optional[builtins.str] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    launch_permission: typing.Optional[typing.Union[ImagebuilderDistributionConfigurationDistributionAmiDistributionConfigurationLaunchPermission, typing.Dict[builtins.str, typing.Any]]] = None,
    name: typing.Optional[builtins.str] = None,
    target_account_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b06ca2f73e555aa2b7e93057bc77814cd207567d65d8b4a978bc90f6288f363(
    *,
    organizational_unit_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    organization_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    user_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    user_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a247c3d04af937aacde73128a9960cf4fdeb1b4d5d345b7abbf746cf06e55be(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0115927d6a352d58242ace4e5c792098febdde41998114729d8589b7c2d19725(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3941d3aeb5fad101bc4f38f51d717763b8caab0b74006b4d89f23fde94996aa4(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8632eee77b06f89eb095449b590119dbcdb4c1db0d2e14723afa789c0074875f(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9aac7b9ac92b00c22477bc0b950502e19f84415810436587a708eedccf88a994(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc3baa87c071828dcb258510cf466e8e308e6a817e7eaaba103f6dee4d6207ff(
    value: typing.Optional[ImagebuilderDistributionConfigurationDistributionAmiDistributionConfigurationLaunchPermission],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e83123993f22f9c32af9097f0dba6502d04dfb73822eb5500604c1198a2e3a74(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4298259d9862ebb4211ec7f812a952b8ee86199f93961705c7526936c40f787d(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc7ca542b2bc065279b67b0b82fdcb9c188b8762b1cebc821e92ed742f84a2f1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c20958e84983f3960fd8f1d9faee687f11840b75d3a605d6ad0c04f8b8bbece(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88d0e0e9a05b15030e1c963b076a127f9e163fe1930f47580a3f2b6512a2552c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0368d8f5439fd51adac33b77cbe36c56a1bcfe9d0ebbd9a930d2e8fb8a8edc48(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1365dd6df07c532656c70f2d4fef39fdc38b3e2f44bd7d97e6875cabd860b989(
    value: typing.Optional[ImagebuilderDistributionConfigurationDistributionAmiDistributionConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__105f454e15b24e357ea7fd025ef96da5c36894804ceb94078e6977cc59b8ec17(
    *,
    target_repository: typing.Union[ImagebuilderDistributionConfigurationDistributionContainerDistributionConfigurationTargetRepository, typing.Dict[builtins.str, typing.Any]],
    container_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__287c367684b749dc1caf1af375bf47de3f207eddce772d0b45fdb0b7150165cc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce7e631753b115de8bfa03c4890944c89bb83e743930ba9c3413f143ad9da8a1(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f31e480e2dde41bc7a090f566e704f3566be69d36a47879320e48a5eec8ff19(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f847f22b0d05c23e729ee349074b68cbd6866c1564e13fffb67dc32ea40be4e0(
    value: typing.Optional[ImagebuilderDistributionConfigurationDistributionContainerDistributionConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee0e4f39b437f1015d7d43294c8d1d520472f98439420c1bafee5e6f22d455f7(
    *,
    repository_name: builtins.str,
    service: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a6fe10a976f8d7a49052a411bf79c8a24bd85885bea9dd9382cf72d7465316e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9469422f1ef035f6ffc51c857357f3bc8e883e7480612a5ef0203ba0e1c77ff2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6ffb5b3c5d1f1aa064ade41ec6952d277fc1e017a475b98bea520adfdb95f8c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b62e142fd3bc0da9cfe122304eb8559ac8b8332a509a5a20795ce4f616eddb2a(
    value: typing.Optional[ImagebuilderDistributionConfigurationDistributionContainerDistributionConfigurationTargetRepository],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8512f6029406c8a09501d3c8f29f21af0c03816cfc9db7f77b61a27ca6697458(
    *,
    account_id: builtins.str,
    enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    launch_template: typing.Optional[typing.Union[ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationLaunchTemplate, typing.Dict[builtins.str, typing.Any]]] = None,
    max_parallel_launches: typing.Optional[jsii.Number] = None,
    snapshot_configuration: typing.Optional[typing.Union[ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationSnapshotConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b47ea8031551ca9a71ceec32d76063da8d65bbf160522de004f32ceecacb24c(
    *,
    launch_template_id: typing.Optional[builtins.str] = None,
    launch_template_name: typing.Optional[builtins.str] = None,
    launch_template_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b2c74c5e124a066693156cc82c14a7d0b365ad15857c6f083b6ad18a0345232(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d553c6eacc2b8759643c51275d932853d9b901d00a2e93a5720268fc1d3384a1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e399a35b6608c369264ff04d070900f14f21303cb3a36d7bdde483da1a5c5deb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c81b3cfb19fab4ad7b469811422f837c5981c57fd6215a118af7dd2230fe2fe1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33c6c89120441964dc0ebdbdd6f5624dfbf4904258e2651537418dae16c0b595(
    value: typing.Optional[ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationLaunchTemplate],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__931930363c41ea48f45ea800b29b2bb10a85fe2bfe5a6eae2e9d128d422cbab0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d9df93ca88019daacbd6f37e5dcf191254c115e14b0a2184668d69ac7824d66(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94c53aff9a77919ba1245592172070bb682a4b42e4117e8f9eeb089683403ac8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcdf8637aa0c7b0904bf57819986369c3d273f4b3b98f7ceec7418d57c8cdf55(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd3a4a95b566be914d2399241433bc6a0d04204d0bbd5c30a14d9b0703caf0a0(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73a8010c6fc33567e5d9e7191c089d92fd73d3c77639990182c14dc144f5bac4(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ImagebuilderDistributionConfigurationDistributionFastLaunchConfiguration]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cf8687c51e08bfaee4eb1b4012b2cbc47d73ca74c792ed39b9d13d0e1a1541d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b0909be231ec2e8498f3042abce802ee05eaad039412db65d5bcbd0acc47c57(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5d35ed988ed112ce6bed093d2159ad70be8a3715aaa25f8f7cd7fd67f7e1fd6(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5309a40a77256e52009118df3fcf5b37afe199625d8b4347b3e77329fa61efe(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9819877d0920f3d076d01f1dd248a0491ed7c921e86d3d8085a2ba525995171(
    value: typing.Optional[typing.Union[ImagebuilderDistributionConfigurationDistributionFastLaunchConfiguration, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72f50119787327dccf47605d8baf37c2d001b1e7f4521084708d76ece82814db(
    *,
    target_resource_count: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3873b45d9f91fcaf8229f78dce493d945a7078b5c35d133c17511c2f018d603(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d0d10b08577a8280ed943217a1d4ec17a253b74dce6b80f1b6c979ede7820c5(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4faa9fc8920ec0603eab1c2872d5fdaad752bdb2ed88c091e23db5b5957e3d2d(
    value: typing.Optional[ImagebuilderDistributionConfigurationDistributionFastLaunchConfigurationSnapshotConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__224233e6a2342f327842a127d347f88f1d647e6791169cf583c38321f0989ae2(
    *,
    launch_template_id: builtins.str,
    account_id: typing.Optional[builtins.str] = None,
    default: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3713549757a3d4bb18f7023b69e6e90fd53cdb6abf74e2b99152e793e6c9d4e8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93fb4a825c97919e0b09209e617e342afd4180ed7df8299997492b2fa025a322(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a9158d0bb70fedd511202d4a6990aa3f521da77bb91a42a76ba05f42f4588e8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dadfa6783a47f5f1c2e5b41018acec9f577215cdfd90e2170b0de88022df8523(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8466777eea7af4e4ec93e8654a96f22dd94882c0d4ed9612202ff8939cd462df(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fac640ec537ce5bf0578c4bfcf8820b1216f5a828aefc028372587a5a1471bfb(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ImagebuilderDistributionConfigurationDistributionLaunchTemplateConfiguration]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77f9ca354afdfb7e7cfc9f0b76300bafea17cc73b5a9c468abb2ca2d7421e429(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78a933257458db864855b150dc3e8afb47e97441ae2395b748d0c1980919c997(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa9d5e34c82bd5eb8ed0fa20750a5da3e70f88e6a116b95d13050634f62240e0(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f673293c8e560233c6bf3c3134233e62026254a034800599501993c5d1e5797d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8d86b1702bf5c11c2a77ece5af9b8ff98a680f5805908a964ccfd85830c8101(
    value: typing.Optional[typing.Union[ImagebuilderDistributionConfigurationDistributionLaunchTemplateConfiguration, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__455a7142d9335f19002bfd1217ff1cc9fc460bfdcdf346241671aabec4d86131(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6657dbd5c0ad68e732560a48dd69ebf51d9e4507b1b71e3e417772f20227daf7(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcb82332b00c809a797f5151f8c6e1cc190d3386adc9b7d4a26d1e443eec1975(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b96597f83b5f94e29a7a7252fc0300f7ec80889621279510f4c26091d6a5fa2(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b39787b2fc6e88a3c290136bc0ad99443fcf3920ad5a2cc020c4ec287b9bbecb(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21dc6d622efe69a70b8e483044196469219007608c09cd098cb6154c629b83d5(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ImagebuilderDistributionConfigurationDistribution]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a9e6d5d11d79e7fc4763735f84cb6c73d6a0152aeec88b7e7d6bfcce5a59116(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__680af109fe31d001aaa43b560ad2a31700bcecbf671f61105caa230e84f70b55(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ImagebuilderDistributionConfigurationDistributionFastLaunchConfiguration, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b8b4c8844c058107bcff2a389e65f012aabfefbda46955913f26e9963807252(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ImagebuilderDistributionConfigurationDistributionLaunchTemplateConfiguration, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d955d1c117811dfda56eebe733ff56adfd98965412c06f3f3d7f6e7de7cf46cc(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__712e8f76145fea675b83fed4d301c73934435690fd94421696885c020bd59d3e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46a11779368f463d6c520c91988256562b79cfa6824f60b3db870cd9e046e52b(
    value: typing.Optional[typing.Union[ImagebuilderDistributionConfigurationDistribution, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
