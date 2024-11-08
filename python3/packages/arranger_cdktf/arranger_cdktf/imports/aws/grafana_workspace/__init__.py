'''
# `aws_grafana_workspace`

Refer to the Terraform Registory for docs: [`aws_grafana_workspace`](https://www.terraform.io/docs/providers/aws/r/grafana_workspace).
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


class GrafanaWorkspace(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.grafanaWorkspace.GrafanaWorkspace",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace aws_grafana_workspace}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        account_access_type: builtins.str,
        authentication_providers: typing.Sequence[builtins.str],
        permission_type: builtins.str,
        data_sources: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        notification_destinations: typing.Optional[typing.Sequence[builtins.str]] = None,
        organizational_units: typing.Optional[typing.Sequence[builtins.str]] = None,
        organization_role_name: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
        stack_set_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["GrafanaWorkspaceTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        vpc_configuration: typing.Optional[typing.Union["GrafanaWorkspaceVpcConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace aws_grafana_workspace} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param account_access_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#account_access_type GrafanaWorkspace#account_access_type}.
        :param authentication_providers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#authentication_providers GrafanaWorkspace#authentication_providers}.
        :param permission_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#permission_type GrafanaWorkspace#permission_type}.
        :param data_sources: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#data_sources GrafanaWorkspace#data_sources}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#description GrafanaWorkspace#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#id GrafanaWorkspace#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#name GrafanaWorkspace#name}.
        :param notification_destinations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#notification_destinations GrafanaWorkspace#notification_destinations}.
        :param organizational_units: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#organizational_units GrafanaWorkspace#organizational_units}.
        :param organization_role_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#organization_role_name GrafanaWorkspace#organization_role_name}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#role_arn GrafanaWorkspace#role_arn}.
        :param stack_set_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#stack_set_name GrafanaWorkspace#stack_set_name}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#tags GrafanaWorkspace#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#tags_all GrafanaWorkspace#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#timeouts GrafanaWorkspace#timeouts}
        :param vpc_configuration: vpc_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#vpc_configuration GrafanaWorkspace#vpc_configuration}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad0649329575ceb947be85b6f776e14244796bfc20e314b771817e1f6df220fc)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GrafanaWorkspaceConfig(
            account_access_type=account_access_type,
            authentication_providers=authentication_providers,
            permission_type=permission_type,
            data_sources=data_sources,
            description=description,
            id=id,
            name=name,
            notification_destinations=notification_destinations,
            organizational_units=organizational_units,
            organization_role_name=organization_role_name,
            role_arn=role_arn,
            stack_set_name=stack_set_name,
            tags=tags,
            tags_all=tags_all,
            timeouts=timeouts,
            vpc_configuration=vpc_configuration,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#create GrafanaWorkspace#create}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#update GrafanaWorkspace#update}.
        '''
        value = GrafanaWorkspaceTimeouts(create=create, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putVpcConfiguration")
    def put_vpc_configuration(
        self,
        *,
        security_group_ids: typing.Sequence[builtins.str],
        subnet_ids: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#security_group_ids GrafanaWorkspace#security_group_ids}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#subnet_ids GrafanaWorkspace#subnet_ids}.
        '''
        value = GrafanaWorkspaceVpcConfiguration(
            security_group_ids=security_group_ids, subnet_ids=subnet_ids
        )

        return typing.cast(None, jsii.invoke(self, "putVpcConfiguration", [value]))

    @jsii.member(jsii_name="resetDataSources")
    def reset_data_sources(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataSources", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNotificationDestinations")
    def reset_notification_destinations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotificationDestinations", []))

    @jsii.member(jsii_name="resetOrganizationalUnits")
    def reset_organizational_units(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrganizationalUnits", []))

    @jsii.member(jsii_name="resetOrganizationRoleName")
    def reset_organization_role_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrganizationRoleName", []))

    @jsii.member(jsii_name="resetRoleArn")
    def reset_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRoleArn", []))

    @jsii.member(jsii_name="resetStackSetName")
    def reset_stack_set_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStackSetName", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetVpcConfiguration")
    def reset_vpc_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpcConfiguration", []))

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
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @builtins.property
    @jsii.member(jsii_name="grafanaVersion")
    def grafana_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "grafanaVersion"))

    @builtins.property
    @jsii.member(jsii_name="samlConfigurationStatus")
    def saml_configuration_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "samlConfigurationStatus"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GrafanaWorkspaceTimeoutsOutputReference":
        return typing.cast("GrafanaWorkspaceTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="vpcConfiguration")
    def vpc_configuration(self) -> "GrafanaWorkspaceVpcConfigurationOutputReference":
        return typing.cast("GrafanaWorkspaceVpcConfigurationOutputReference", jsii.get(self, "vpcConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="accountAccessTypeInput")
    def account_access_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountAccessTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="authenticationProvidersInput")
    def authentication_providers_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "authenticationProvidersInput"))

    @builtins.property
    @jsii.member(jsii_name="dataSourcesInput")
    def data_sources_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dataSourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationDestinationsInput")
    def notification_destinations_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "notificationDestinationsInput"))

    @builtins.property
    @jsii.member(jsii_name="organizationalUnitsInput")
    def organizational_units_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "organizationalUnitsInput"))

    @builtins.property
    @jsii.member(jsii_name="organizationRoleNameInput")
    def organization_role_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "organizationRoleNameInput"))

    @builtins.property
    @jsii.member(jsii_name="permissionTypeInput")
    def permission_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "permissionTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="stackSetNameInput")
    def stack_set_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stackSetNameInput"))

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
    ) -> typing.Optional[typing.Union["GrafanaWorkspaceTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GrafanaWorkspaceTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcConfigurationInput")
    def vpc_configuration_input(
        self,
    ) -> typing.Optional["GrafanaWorkspaceVpcConfiguration"]:
        return typing.cast(typing.Optional["GrafanaWorkspaceVpcConfiguration"], jsii.get(self, "vpcConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="accountAccessType")
    def account_access_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountAccessType"))

    @account_access_type.setter
    def account_access_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eebd59893181db061fcf397c2522989a81be557d6a994f8bea84a79994a1e781)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountAccessType", value)

    @builtins.property
    @jsii.member(jsii_name="authenticationProviders")
    def authentication_providers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "authenticationProviders"))

    @authentication_providers.setter
    def authentication_providers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57ded94c364a85111533bf6b60f18588e691cbe36d223cd9c5da9bd7e404211a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authenticationProviders", value)

    @builtins.property
    @jsii.member(jsii_name="dataSources")
    def data_sources(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "dataSources"))

    @data_sources.setter
    def data_sources(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01e3f97ba2b25e0a85edddbd73a6d118d8ac77a7dd34d71b739ae5c9e133dddc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataSources", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__284636c0c1fa9ab98c8e5c7ead772628d28254078252e89927bb94a3866c512f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75b0753b594be6f63a0720b183a01de6d0817e73582ce08a13c8ae9f0efeb8b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c7a5d62d9df1f0c0fc048012454b869f60d70aff97a160846d6179bee1db318)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="notificationDestinations")
    def notification_destinations(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "notificationDestinations"))

    @notification_destinations.setter
    def notification_destinations(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03e816543fac399c59edbb08791be1c33a97d296aa63ee6696ef15a9043c026f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationDestinations", value)

    @builtins.property
    @jsii.member(jsii_name="organizationalUnits")
    def organizational_units(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "organizationalUnits"))

    @organizational_units.setter
    def organizational_units(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c88aad4ab3633c0e42b641130d68c756e2462e7968f7ecb333ad1a429a630408)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organizationalUnits", value)

    @builtins.property
    @jsii.member(jsii_name="organizationRoleName")
    def organization_role_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "organizationRoleName"))

    @organization_role_name.setter
    def organization_role_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fdb258818fa8c97f8693dfd61f3f59b581a340437bba10df91886f63794960c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organizationRoleName", value)

    @builtins.property
    @jsii.member(jsii_name="permissionType")
    def permission_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "permissionType"))

    @permission_type.setter
    def permission_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b083af2960e693af7d5ee381df782b9d6e35e7c87a680d0fa6639c432387125b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissionType", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7be4640dacf60576da5fa51680843a466379eae0e214723eb6a9017cfea704aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="stackSetName")
    def stack_set_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stackSetName"))

    @stack_set_name.setter
    def stack_set_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b0f06a591330de7f78d81368db0fc9eb894832b1d1ce8aa652eef076b1bf4de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stackSetName", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36326f5d03926dfa8b0b163fe1e233b6f64ae0a2354e16d159128d52e5d86dfa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c67d64b95a956a054e5f8a4ada2da15aa6ca3a29c480a381459a43c4fcb53539)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.grafanaWorkspace.GrafanaWorkspaceConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "account_access_type": "accountAccessType",
        "authentication_providers": "authenticationProviders",
        "permission_type": "permissionType",
        "data_sources": "dataSources",
        "description": "description",
        "id": "id",
        "name": "name",
        "notification_destinations": "notificationDestinations",
        "organizational_units": "organizationalUnits",
        "organization_role_name": "organizationRoleName",
        "role_arn": "roleArn",
        "stack_set_name": "stackSetName",
        "tags": "tags",
        "tags_all": "tagsAll",
        "timeouts": "timeouts",
        "vpc_configuration": "vpcConfiguration",
    },
)
class GrafanaWorkspaceConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        account_access_type: builtins.str,
        authentication_providers: typing.Sequence[builtins.str],
        permission_type: builtins.str,
        data_sources: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        notification_destinations: typing.Optional[typing.Sequence[builtins.str]] = None,
        organizational_units: typing.Optional[typing.Sequence[builtins.str]] = None,
        organization_role_name: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
        stack_set_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["GrafanaWorkspaceTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        vpc_configuration: typing.Optional[typing.Union["GrafanaWorkspaceVpcConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param account_access_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#account_access_type GrafanaWorkspace#account_access_type}.
        :param authentication_providers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#authentication_providers GrafanaWorkspace#authentication_providers}.
        :param permission_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#permission_type GrafanaWorkspace#permission_type}.
        :param data_sources: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#data_sources GrafanaWorkspace#data_sources}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#description GrafanaWorkspace#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#id GrafanaWorkspace#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#name GrafanaWorkspace#name}.
        :param notification_destinations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#notification_destinations GrafanaWorkspace#notification_destinations}.
        :param organizational_units: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#organizational_units GrafanaWorkspace#organizational_units}.
        :param organization_role_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#organization_role_name GrafanaWorkspace#organization_role_name}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#role_arn GrafanaWorkspace#role_arn}.
        :param stack_set_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#stack_set_name GrafanaWorkspace#stack_set_name}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#tags GrafanaWorkspace#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#tags_all GrafanaWorkspace#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#timeouts GrafanaWorkspace#timeouts}
        :param vpc_configuration: vpc_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#vpc_configuration GrafanaWorkspace#vpc_configuration}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = GrafanaWorkspaceTimeouts(**timeouts)
        if isinstance(vpc_configuration, dict):
            vpc_configuration = GrafanaWorkspaceVpcConfiguration(**vpc_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36a1bb1ec3aa6ad61fcc2a970a2f3cb10010beb4bb882a24902c0af129568d35)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument account_access_type", value=account_access_type, expected_type=type_hints["account_access_type"])
            check_type(argname="argument authentication_providers", value=authentication_providers, expected_type=type_hints["authentication_providers"])
            check_type(argname="argument permission_type", value=permission_type, expected_type=type_hints["permission_type"])
            check_type(argname="argument data_sources", value=data_sources, expected_type=type_hints["data_sources"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument notification_destinations", value=notification_destinations, expected_type=type_hints["notification_destinations"])
            check_type(argname="argument organizational_units", value=organizational_units, expected_type=type_hints["organizational_units"])
            check_type(argname="argument organization_role_name", value=organization_role_name, expected_type=type_hints["organization_role_name"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument stack_set_name", value=stack_set_name, expected_type=type_hints["stack_set_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument vpc_configuration", value=vpc_configuration, expected_type=type_hints["vpc_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account_access_type": account_access_type,
            "authentication_providers": authentication_providers,
            "permission_type": permission_type,
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
        if data_sources is not None:
            self._values["data_sources"] = data_sources
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name
        if notification_destinations is not None:
            self._values["notification_destinations"] = notification_destinations
        if organizational_units is not None:
            self._values["organizational_units"] = organizational_units
        if organization_role_name is not None:
            self._values["organization_role_name"] = organization_role_name
        if role_arn is not None:
            self._values["role_arn"] = role_arn
        if stack_set_name is not None:
            self._values["stack_set_name"] = stack_set_name
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if vpc_configuration is not None:
            self._values["vpc_configuration"] = vpc_configuration

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
    def account_access_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#account_access_type GrafanaWorkspace#account_access_type}.'''
        result = self._values.get("account_access_type")
        assert result is not None, "Required property 'account_access_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authentication_providers(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#authentication_providers GrafanaWorkspace#authentication_providers}.'''
        result = self._values.get("authentication_providers")
        assert result is not None, "Required property 'authentication_providers' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def permission_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#permission_type GrafanaWorkspace#permission_type}.'''
        result = self._values.get("permission_type")
        assert result is not None, "Required property 'permission_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_sources(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#data_sources GrafanaWorkspace#data_sources}.'''
        result = self._values.get("data_sources")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#description GrafanaWorkspace#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#id GrafanaWorkspace#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#name GrafanaWorkspace#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notification_destinations(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#notification_destinations GrafanaWorkspace#notification_destinations}.'''
        result = self._values.get("notification_destinations")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def organizational_units(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#organizational_units GrafanaWorkspace#organizational_units}.'''
        result = self._values.get("organizational_units")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def organization_role_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#organization_role_name GrafanaWorkspace#organization_role_name}.'''
        result = self._values.get("organization_role_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#role_arn GrafanaWorkspace#role_arn}.'''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def stack_set_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#stack_set_name GrafanaWorkspace#stack_set_name}.'''
        result = self._values.get("stack_set_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#tags GrafanaWorkspace#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#tags_all GrafanaWorkspace#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GrafanaWorkspaceTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#timeouts GrafanaWorkspace#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GrafanaWorkspaceTimeouts"], result)

    @builtins.property
    def vpc_configuration(self) -> typing.Optional["GrafanaWorkspaceVpcConfiguration"]:
        '''vpc_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#vpc_configuration GrafanaWorkspace#vpc_configuration}
        '''
        result = self._values.get("vpc_configuration")
        return typing.cast(typing.Optional["GrafanaWorkspaceVpcConfiguration"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GrafanaWorkspaceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.grafanaWorkspace.GrafanaWorkspaceTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "update": "update"},
)
class GrafanaWorkspaceTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#create GrafanaWorkspace#create}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#update GrafanaWorkspace#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5db85e85746902f979939610a5ae0532c85f994d2992d463bb67367483306421)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#create GrafanaWorkspace#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#update GrafanaWorkspace#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GrafanaWorkspaceTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GrafanaWorkspaceTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.grafanaWorkspace.GrafanaWorkspaceTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e485db8ca4a0c89a81b45c8ba47336d696f1b9d8e7c08552c7387a096d3d5f0c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__d109a39f699b9be8ae4393c3f78873b9219aced3d483b33df59d16936f38f56e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0cc7ae0990478036db7ea90fc5fe8bcde83f2bcf32987bb16c3ff1c853539770)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GrafanaWorkspaceTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GrafanaWorkspaceTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GrafanaWorkspaceTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68030195dafe64ecedaf92652bd349286c942b9ef60f5cb822772f3d2b46a68f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.grafanaWorkspace.GrafanaWorkspaceVpcConfiguration",
    jsii_struct_bases=[],
    name_mapping={"security_group_ids": "securityGroupIds", "subnet_ids": "subnetIds"},
)
class GrafanaWorkspaceVpcConfiguration:
    def __init__(
        self,
        *,
        security_group_ids: typing.Sequence[builtins.str],
        subnet_ids: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#security_group_ids GrafanaWorkspace#security_group_ids}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#subnet_ids GrafanaWorkspace#subnet_ids}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c1433d4bb4a3093c165a1536a02b5cf2215e99be78e1159a1f772d4072083ff)
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "security_group_ids": security_group_ids,
            "subnet_ids": subnet_ids,
        }

    @builtins.property
    def security_group_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#security_group_ids GrafanaWorkspace#security_group_ids}.'''
        result = self._values.get("security_group_ids")
        assert result is not None, "Required property 'security_group_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace#subnet_ids GrafanaWorkspace#subnet_ids}.'''
        result = self._values.get("subnet_ids")
        assert result is not None, "Required property 'subnet_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GrafanaWorkspaceVpcConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GrafanaWorkspaceVpcConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.grafanaWorkspace.GrafanaWorkspaceVpcConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3c18f2d1a63f9462d51f105ad42dbf00cc9c954ac17e6e91338acd3f260d506e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="securityGroupIdsInput")
    def security_group_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdsInput")
    def subnet_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59f06e4210251acff92ef11f8b90ef8cea204ec80b6f47dc31ee4e69ce09ae05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0dca7fc0fe400212d360e39f9c420215ac4ba1e526892bc89ddf145a5c0e7e93)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GrafanaWorkspaceVpcConfiguration]:
        return typing.cast(typing.Optional[GrafanaWorkspaceVpcConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GrafanaWorkspaceVpcConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98cf916862552f5e08102efd5f20cedf794324f57fba4375a2d5319f17081f34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GrafanaWorkspace",
    "GrafanaWorkspaceConfig",
    "GrafanaWorkspaceTimeouts",
    "GrafanaWorkspaceTimeoutsOutputReference",
    "GrafanaWorkspaceVpcConfiguration",
    "GrafanaWorkspaceVpcConfigurationOutputReference",
]

publication.publish()

def _typecheckingstub__ad0649329575ceb947be85b6f776e14244796bfc20e314b771817e1f6df220fc(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    account_access_type: builtins.str,
    authentication_providers: typing.Sequence[builtins.str],
    permission_type: builtins.str,
    data_sources: typing.Optional[typing.Sequence[builtins.str]] = None,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    notification_destinations: typing.Optional[typing.Sequence[builtins.str]] = None,
    organizational_units: typing.Optional[typing.Sequence[builtins.str]] = None,
    organization_role_name: typing.Optional[builtins.str] = None,
    role_arn: typing.Optional[builtins.str] = None,
    stack_set_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[GrafanaWorkspaceTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    vpc_configuration: typing.Optional[typing.Union[GrafanaWorkspaceVpcConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__eebd59893181db061fcf397c2522989a81be557d6a994f8bea84a79994a1e781(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57ded94c364a85111533bf6b60f18588e691cbe36d223cd9c5da9bd7e404211a(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01e3f97ba2b25e0a85edddbd73a6d118d8ac77a7dd34d71b739ae5c9e133dddc(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__284636c0c1fa9ab98c8e5c7ead772628d28254078252e89927bb94a3866c512f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75b0753b594be6f63a0720b183a01de6d0817e73582ce08a13c8ae9f0efeb8b2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c7a5d62d9df1f0c0fc048012454b869f60d70aff97a160846d6179bee1db318(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03e816543fac399c59edbb08791be1c33a97d296aa63ee6696ef15a9043c026f(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c88aad4ab3633c0e42b641130d68c756e2462e7968f7ecb333ad1a429a630408(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fdb258818fa8c97f8693dfd61f3f59b581a340437bba10df91886f63794960c7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b083af2960e693af7d5ee381df782b9d6e35e7c87a680d0fa6639c432387125b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7be4640dacf60576da5fa51680843a466379eae0e214723eb6a9017cfea704aa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b0f06a591330de7f78d81368db0fc9eb894832b1d1ce8aa652eef076b1bf4de(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36326f5d03926dfa8b0b163fe1e233b6f64ae0a2354e16d159128d52e5d86dfa(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c67d64b95a956a054e5f8a4ada2da15aa6ca3a29c480a381459a43c4fcb53539(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36a1bb1ec3aa6ad61fcc2a970a2f3cb10010beb4bb882a24902c0af129568d35(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    account_access_type: builtins.str,
    authentication_providers: typing.Sequence[builtins.str],
    permission_type: builtins.str,
    data_sources: typing.Optional[typing.Sequence[builtins.str]] = None,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    notification_destinations: typing.Optional[typing.Sequence[builtins.str]] = None,
    organizational_units: typing.Optional[typing.Sequence[builtins.str]] = None,
    organization_role_name: typing.Optional[builtins.str] = None,
    role_arn: typing.Optional[builtins.str] = None,
    stack_set_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[GrafanaWorkspaceTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    vpc_configuration: typing.Optional[typing.Union[GrafanaWorkspaceVpcConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5db85e85746902f979939610a5ae0532c85f994d2992d463bb67367483306421(
    *,
    create: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e485db8ca4a0c89a81b45c8ba47336d696f1b9d8e7c08552c7387a096d3d5f0c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d109a39f699b9be8ae4393c3f78873b9219aced3d483b33df59d16936f38f56e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cc7ae0990478036db7ea90fc5fe8bcde83f2bcf32987bb16c3ff1c853539770(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68030195dafe64ecedaf92652bd349286c942b9ef60f5cb822772f3d2b46a68f(
    value: typing.Optional[typing.Union[GrafanaWorkspaceTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c1433d4bb4a3093c165a1536a02b5cf2215e99be78e1159a1f772d4072083ff(
    *,
    security_group_ids: typing.Sequence[builtins.str],
    subnet_ids: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c18f2d1a63f9462d51f105ad42dbf00cc9c954ac17e6e91338acd3f260d506e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59f06e4210251acff92ef11f8b90ef8cea204ec80b6f47dc31ee4e69ce09ae05(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0dca7fc0fe400212d360e39f9c420215ac4ba1e526892bc89ddf145a5c0e7e93(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98cf916862552f5e08102efd5f20cedf794324f57fba4375a2d5319f17081f34(
    value: typing.Optional[GrafanaWorkspaceVpcConfiguration],
) -> None:
    """Type checking stubs"""
    pass
