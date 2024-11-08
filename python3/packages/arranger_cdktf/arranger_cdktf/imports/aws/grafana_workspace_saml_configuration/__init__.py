'''
# `aws_grafana_workspace_saml_configuration`

Refer to the Terraform Registory for docs: [`aws_grafana_workspace_saml_configuration`](https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration).
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


class GrafanaWorkspaceSamlConfiguration(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.grafanaWorkspaceSamlConfiguration.GrafanaWorkspaceSamlConfiguration",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration aws_grafana_workspace_saml_configuration}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        editor_role_values: typing.Sequence[builtins.str],
        workspace_id: builtins.str,
        admin_role_values: typing.Optional[typing.Sequence[builtins.str]] = None,
        allowed_organizations: typing.Optional[typing.Sequence[builtins.str]] = None,
        email_assertion: typing.Optional[builtins.str] = None,
        groups_assertion: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        idp_metadata_url: typing.Optional[builtins.str] = None,
        idp_metadata_xml: typing.Optional[builtins.str] = None,
        login_assertion: typing.Optional[builtins.str] = None,
        login_validity_duration: typing.Optional[jsii.Number] = None,
        name_assertion: typing.Optional[builtins.str] = None,
        org_assertion: typing.Optional[builtins.str] = None,
        role_assertion: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GrafanaWorkspaceSamlConfigurationTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration aws_grafana_workspace_saml_configuration} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param editor_role_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#editor_role_values GrafanaWorkspaceSamlConfiguration#editor_role_values}.
        :param workspace_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#workspace_id GrafanaWorkspaceSamlConfiguration#workspace_id}.
        :param admin_role_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#admin_role_values GrafanaWorkspaceSamlConfiguration#admin_role_values}.
        :param allowed_organizations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#allowed_organizations GrafanaWorkspaceSamlConfiguration#allowed_organizations}.
        :param email_assertion: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#email_assertion GrafanaWorkspaceSamlConfiguration#email_assertion}.
        :param groups_assertion: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#groups_assertion GrafanaWorkspaceSamlConfiguration#groups_assertion}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#id GrafanaWorkspaceSamlConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param idp_metadata_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#idp_metadata_url GrafanaWorkspaceSamlConfiguration#idp_metadata_url}.
        :param idp_metadata_xml: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#idp_metadata_xml GrafanaWorkspaceSamlConfiguration#idp_metadata_xml}.
        :param login_assertion: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#login_assertion GrafanaWorkspaceSamlConfiguration#login_assertion}.
        :param login_validity_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#login_validity_duration GrafanaWorkspaceSamlConfiguration#login_validity_duration}.
        :param name_assertion: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#name_assertion GrafanaWorkspaceSamlConfiguration#name_assertion}.
        :param org_assertion: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#org_assertion GrafanaWorkspaceSamlConfiguration#org_assertion}.
        :param role_assertion: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#role_assertion GrafanaWorkspaceSamlConfiguration#role_assertion}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#timeouts GrafanaWorkspaceSamlConfiguration#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6f9a347d15119928ae8ef2a3a350dab54910a89045d987264fb26b1032edd53)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GrafanaWorkspaceSamlConfigurationConfig(
            editor_role_values=editor_role_values,
            workspace_id=workspace_id,
            admin_role_values=admin_role_values,
            allowed_organizations=allowed_organizations,
            email_assertion=email_assertion,
            groups_assertion=groups_assertion,
            id=id,
            idp_metadata_url=idp_metadata_url,
            idp_metadata_xml=idp_metadata_xml,
            login_assertion=login_assertion,
            login_validity_duration=login_validity_duration,
            name_assertion=name_assertion,
            org_assertion=org_assertion,
            role_assertion=role_assertion,
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

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#create GrafanaWorkspaceSamlConfiguration#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#delete GrafanaWorkspaceSamlConfiguration#delete}.
        '''
        value = GrafanaWorkspaceSamlConfigurationTimeouts(create=create, delete=delete)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAdminRoleValues")
    def reset_admin_role_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdminRoleValues", []))

    @jsii.member(jsii_name="resetAllowedOrganizations")
    def reset_allowed_organizations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedOrganizations", []))

    @jsii.member(jsii_name="resetEmailAssertion")
    def reset_email_assertion(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailAssertion", []))

    @jsii.member(jsii_name="resetGroupsAssertion")
    def reset_groups_assertion(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupsAssertion", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdpMetadataUrl")
    def reset_idp_metadata_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdpMetadataUrl", []))

    @jsii.member(jsii_name="resetIdpMetadataXml")
    def reset_idp_metadata_xml(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdpMetadataXml", []))

    @jsii.member(jsii_name="resetLoginAssertion")
    def reset_login_assertion(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoginAssertion", []))

    @jsii.member(jsii_name="resetLoginValidityDuration")
    def reset_login_validity_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoginValidityDuration", []))

    @jsii.member(jsii_name="resetNameAssertion")
    def reset_name_assertion(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNameAssertion", []))

    @jsii.member(jsii_name="resetOrgAssertion")
    def reset_org_assertion(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrgAssertion", []))

    @jsii.member(jsii_name="resetRoleAssertion")
    def reset_role_assertion(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRoleAssertion", []))

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
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GrafanaWorkspaceSamlConfigurationTimeoutsOutputReference":
        return typing.cast("GrafanaWorkspaceSamlConfigurationTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="adminRoleValuesInput")
    def admin_role_values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "adminRoleValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedOrganizationsInput")
    def allowed_organizations_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedOrganizationsInput"))

    @builtins.property
    @jsii.member(jsii_name="editorRoleValuesInput")
    def editor_role_values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "editorRoleValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="emailAssertionInput")
    def email_assertion_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailAssertionInput"))

    @builtins.property
    @jsii.member(jsii_name="groupsAssertionInput")
    def groups_assertion_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupsAssertionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="idpMetadataUrlInput")
    def idp_metadata_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idpMetadataUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="idpMetadataXmlInput")
    def idp_metadata_xml_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idpMetadataXmlInput"))

    @builtins.property
    @jsii.member(jsii_name="loginAssertionInput")
    def login_assertion_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loginAssertionInput"))

    @builtins.property
    @jsii.member(jsii_name="loginValidityDurationInput")
    def login_validity_duration_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "loginValidityDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameAssertionInput")
    def name_assertion_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameAssertionInput"))

    @builtins.property
    @jsii.member(jsii_name="orgAssertionInput")
    def org_assertion_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "orgAssertionInput"))

    @builtins.property
    @jsii.member(jsii_name="roleAssertionInput")
    def role_assertion_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleAssertionInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GrafanaWorkspaceSamlConfigurationTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GrafanaWorkspaceSamlConfigurationTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="workspaceIdInput")
    def workspace_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workspaceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="adminRoleValues")
    def admin_role_values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "adminRoleValues"))

    @admin_role_values.setter
    def admin_role_values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1dd1fcc6b7518fc9a3fbb7825ae52bd2240d7fa2c651ea969022e56c800bfe7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminRoleValues", value)

    @builtins.property
    @jsii.member(jsii_name="allowedOrganizations")
    def allowed_organizations(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedOrganizations"))

    @allowed_organizations.setter
    def allowed_organizations(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ef06bffbbd5e4dbb40c61a59d11a8bcf3bcc1aeb5c302856075221cb485535b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedOrganizations", value)

    @builtins.property
    @jsii.member(jsii_name="editorRoleValues")
    def editor_role_values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "editorRoleValues"))

    @editor_role_values.setter
    def editor_role_values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06af71db3090fc0345e7f69f7285f8cea60dba7ac93b321d5616d1ab220765d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "editorRoleValues", value)

    @builtins.property
    @jsii.member(jsii_name="emailAssertion")
    def email_assertion(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "emailAssertion"))

    @email_assertion.setter
    def email_assertion(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ad7998232ebcf3bdedf0760afd830844ff1a9ba0a157dfe2ba0258bf1fccbeb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailAssertion", value)

    @builtins.property
    @jsii.member(jsii_name="groupsAssertion")
    def groups_assertion(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupsAssertion"))

    @groups_assertion.setter
    def groups_assertion(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e2a7de96c8b2d25e2c055decb12c25d7134fa9ac5050fe4fab092176a1ccf25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupsAssertion", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f659c25e99db56a9d020bb6c610219522a9bdeee69c265bb501b08f6fcb90895)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="idpMetadataUrl")
    def idp_metadata_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "idpMetadataUrl"))

    @idp_metadata_url.setter
    def idp_metadata_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb7876e8039a1adb395cf12fe57e689880b0da14c7abae444be154d560a486f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idpMetadataUrl", value)

    @builtins.property
    @jsii.member(jsii_name="idpMetadataXml")
    def idp_metadata_xml(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "idpMetadataXml"))

    @idp_metadata_xml.setter
    def idp_metadata_xml(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f59d956f226bb7ae81c76541cc9a6a6b00a8cab47f3ebc78919571e8bda7646)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idpMetadataXml", value)

    @builtins.property
    @jsii.member(jsii_name="loginAssertion")
    def login_assertion(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loginAssertion"))

    @login_assertion.setter
    def login_assertion(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3e978bb32b60c67b970abcb1f7b75386780e94f81a480e6e8dead8c5a40ecef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loginAssertion", value)

    @builtins.property
    @jsii.member(jsii_name="loginValidityDuration")
    def login_validity_duration(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "loginValidityDuration"))

    @login_validity_duration.setter
    def login_validity_duration(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bfd2a61c6610db02bad13df429dbf23918a69772f7402d08942db6430546d98)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loginValidityDuration", value)

    @builtins.property
    @jsii.member(jsii_name="nameAssertion")
    def name_assertion(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nameAssertion"))

    @name_assertion.setter
    def name_assertion(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49c059af7466a86996db833490c12cb64d1c473cc6d1345793fd43d1ba39c73e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nameAssertion", value)

    @builtins.property
    @jsii.member(jsii_name="orgAssertion")
    def org_assertion(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "orgAssertion"))

    @org_assertion.setter
    def org_assertion(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f135ba30ba3a38eb34d6feef21e98590aec1da03a900b22173c283070f16b9f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "orgAssertion", value)

    @builtins.property
    @jsii.member(jsii_name="roleAssertion")
    def role_assertion(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleAssertion"))

    @role_assertion.setter
    def role_assertion(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05995523930b992ebea47c033245f4efc7b5ff914c22a5f71bf3897b94ab9824)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleAssertion", value)

    @builtins.property
    @jsii.member(jsii_name="workspaceId")
    def workspace_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "workspaceId"))

    @workspace_id.setter
    def workspace_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c22732b05af1cfa21c5be4fd6aa1b34d49a51576639aea431fda720cc142ea62)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workspaceId", value)


@jsii.data_type(
    jsii_type="aws.grafanaWorkspaceSamlConfiguration.GrafanaWorkspaceSamlConfigurationConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "editor_role_values": "editorRoleValues",
        "workspace_id": "workspaceId",
        "admin_role_values": "adminRoleValues",
        "allowed_organizations": "allowedOrganizations",
        "email_assertion": "emailAssertion",
        "groups_assertion": "groupsAssertion",
        "id": "id",
        "idp_metadata_url": "idpMetadataUrl",
        "idp_metadata_xml": "idpMetadataXml",
        "login_assertion": "loginAssertion",
        "login_validity_duration": "loginValidityDuration",
        "name_assertion": "nameAssertion",
        "org_assertion": "orgAssertion",
        "role_assertion": "roleAssertion",
        "timeouts": "timeouts",
    },
)
class GrafanaWorkspaceSamlConfigurationConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        editor_role_values: typing.Sequence[builtins.str],
        workspace_id: builtins.str,
        admin_role_values: typing.Optional[typing.Sequence[builtins.str]] = None,
        allowed_organizations: typing.Optional[typing.Sequence[builtins.str]] = None,
        email_assertion: typing.Optional[builtins.str] = None,
        groups_assertion: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        idp_metadata_url: typing.Optional[builtins.str] = None,
        idp_metadata_xml: typing.Optional[builtins.str] = None,
        login_assertion: typing.Optional[builtins.str] = None,
        login_validity_duration: typing.Optional[jsii.Number] = None,
        name_assertion: typing.Optional[builtins.str] = None,
        org_assertion: typing.Optional[builtins.str] = None,
        role_assertion: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GrafanaWorkspaceSamlConfigurationTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param editor_role_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#editor_role_values GrafanaWorkspaceSamlConfiguration#editor_role_values}.
        :param workspace_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#workspace_id GrafanaWorkspaceSamlConfiguration#workspace_id}.
        :param admin_role_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#admin_role_values GrafanaWorkspaceSamlConfiguration#admin_role_values}.
        :param allowed_organizations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#allowed_organizations GrafanaWorkspaceSamlConfiguration#allowed_organizations}.
        :param email_assertion: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#email_assertion GrafanaWorkspaceSamlConfiguration#email_assertion}.
        :param groups_assertion: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#groups_assertion GrafanaWorkspaceSamlConfiguration#groups_assertion}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#id GrafanaWorkspaceSamlConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param idp_metadata_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#idp_metadata_url GrafanaWorkspaceSamlConfiguration#idp_metadata_url}.
        :param idp_metadata_xml: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#idp_metadata_xml GrafanaWorkspaceSamlConfiguration#idp_metadata_xml}.
        :param login_assertion: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#login_assertion GrafanaWorkspaceSamlConfiguration#login_assertion}.
        :param login_validity_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#login_validity_duration GrafanaWorkspaceSamlConfiguration#login_validity_duration}.
        :param name_assertion: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#name_assertion GrafanaWorkspaceSamlConfiguration#name_assertion}.
        :param org_assertion: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#org_assertion GrafanaWorkspaceSamlConfiguration#org_assertion}.
        :param role_assertion: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#role_assertion GrafanaWorkspaceSamlConfiguration#role_assertion}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#timeouts GrafanaWorkspaceSamlConfiguration#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = GrafanaWorkspaceSamlConfigurationTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__212091dfbe9514711e3403d5140111916766746702aa3c252f698e3b79dd8c6f)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument editor_role_values", value=editor_role_values, expected_type=type_hints["editor_role_values"])
            check_type(argname="argument workspace_id", value=workspace_id, expected_type=type_hints["workspace_id"])
            check_type(argname="argument admin_role_values", value=admin_role_values, expected_type=type_hints["admin_role_values"])
            check_type(argname="argument allowed_organizations", value=allowed_organizations, expected_type=type_hints["allowed_organizations"])
            check_type(argname="argument email_assertion", value=email_assertion, expected_type=type_hints["email_assertion"])
            check_type(argname="argument groups_assertion", value=groups_assertion, expected_type=type_hints["groups_assertion"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument idp_metadata_url", value=idp_metadata_url, expected_type=type_hints["idp_metadata_url"])
            check_type(argname="argument idp_metadata_xml", value=idp_metadata_xml, expected_type=type_hints["idp_metadata_xml"])
            check_type(argname="argument login_assertion", value=login_assertion, expected_type=type_hints["login_assertion"])
            check_type(argname="argument login_validity_duration", value=login_validity_duration, expected_type=type_hints["login_validity_duration"])
            check_type(argname="argument name_assertion", value=name_assertion, expected_type=type_hints["name_assertion"])
            check_type(argname="argument org_assertion", value=org_assertion, expected_type=type_hints["org_assertion"])
            check_type(argname="argument role_assertion", value=role_assertion, expected_type=type_hints["role_assertion"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "editor_role_values": editor_role_values,
            "workspace_id": workspace_id,
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
        if admin_role_values is not None:
            self._values["admin_role_values"] = admin_role_values
        if allowed_organizations is not None:
            self._values["allowed_organizations"] = allowed_organizations
        if email_assertion is not None:
            self._values["email_assertion"] = email_assertion
        if groups_assertion is not None:
            self._values["groups_assertion"] = groups_assertion
        if id is not None:
            self._values["id"] = id
        if idp_metadata_url is not None:
            self._values["idp_metadata_url"] = idp_metadata_url
        if idp_metadata_xml is not None:
            self._values["idp_metadata_xml"] = idp_metadata_xml
        if login_assertion is not None:
            self._values["login_assertion"] = login_assertion
        if login_validity_duration is not None:
            self._values["login_validity_duration"] = login_validity_duration
        if name_assertion is not None:
            self._values["name_assertion"] = name_assertion
        if org_assertion is not None:
            self._values["org_assertion"] = org_assertion
        if role_assertion is not None:
            self._values["role_assertion"] = role_assertion
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
    def editor_role_values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#editor_role_values GrafanaWorkspaceSamlConfiguration#editor_role_values}.'''
        result = self._values.get("editor_role_values")
        assert result is not None, "Required property 'editor_role_values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def workspace_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#workspace_id GrafanaWorkspaceSamlConfiguration#workspace_id}.'''
        result = self._values.get("workspace_id")
        assert result is not None, "Required property 'workspace_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def admin_role_values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#admin_role_values GrafanaWorkspaceSamlConfiguration#admin_role_values}.'''
        result = self._values.get("admin_role_values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def allowed_organizations(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#allowed_organizations GrafanaWorkspaceSamlConfiguration#allowed_organizations}.'''
        result = self._values.get("allowed_organizations")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def email_assertion(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#email_assertion GrafanaWorkspaceSamlConfiguration#email_assertion}.'''
        result = self._values.get("email_assertion")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def groups_assertion(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#groups_assertion GrafanaWorkspaceSamlConfiguration#groups_assertion}.'''
        result = self._values.get("groups_assertion")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#id GrafanaWorkspaceSamlConfiguration#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def idp_metadata_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#idp_metadata_url GrafanaWorkspaceSamlConfiguration#idp_metadata_url}.'''
        result = self._values.get("idp_metadata_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def idp_metadata_xml(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#idp_metadata_xml GrafanaWorkspaceSamlConfiguration#idp_metadata_xml}.'''
        result = self._values.get("idp_metadata_xml")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def login_assertion(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#login_assertion GrafanaWorkspaceSamlConfiguration#login_assertion}.'''
        result = self._values.get("login_assertion")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def login_validity_duration(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#login_validity_duration GrafanaWorkspaceSamlConfiguration#login_validity_duration}.'''
        result = self._values.get("login_validity_duration")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name_assertion(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#name_assertion GrafanaWorkspaceSamlConfiguration#name_assertion}.'''
        result = self._values.get("name_assertion")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def org_assertion(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#org_assertion GrafanaWorkspaceSamlConfiguration#org_assertion}.'''
        result = self._values.get("org_assertion")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role_assertion(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#role_assertion GrafanaWorkspaceSamlConfiguration#role_assertion}.'''
        result = self._values.get("role_assertion")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GrafanaWorkspaceSamlConfigurationTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#timeouts GrafanaWorkspaceSamlConfiguration#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GrafanaWorkspaceSamlConfigurationTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GrafanaWorkspaceSamlConfigurationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.grafanaWorkspaceSamlConfiguration.GrafanaWorkspaceSamlConfigurationTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete"},
)
class GrafanaWorkspaceSamlConfigurationTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#create GrafanaWorkspaceSamlConfiguration#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#delete GrafanaWorkspaceSamlConfiguration#delete}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34c8e63668d40f8008730a9a0e9c3e3e96b50027939492d098e04558cf381472)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#create GrafanaWorkspaceSamlConfiguration#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/grafana_workspace_saml_configuration#delete GrafanaWorkspaceSamlConfiguration#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GrafanaWorkspaceSamlConfigurationTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GrafanaWorkspaceSamlConfigurationTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.grafanaWorkspaceSamlConfiguration.GrafanaWorkspaceSamlConfigurationTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0d03976e145e1890c1533242809aeb1a959ac27d3e24847fcd8a372eab5bb1e0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f8dedcc4adb4d94ac1ed4c3d84ebbc70c44cec357686b46b9c7d47e942d9098)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__126a3830767a266b7fdefd3da69712c95544f592609073b2e3b338a60654be06)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GrafanaWorkspaceSamlConfigurationTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GrafanaWorkspaceSamlConfigurationTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GrafanaWorkspaceSamlConfigurationTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a97f08d44133e56f98541e4fef1cc858b5a6d6684b95089f8bb4e77b66237f2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GrafanaWorkspaceSamlConfiguration",
    "GrafanaWorkspaceSamlConfigurationConfig",
    "GrafanaWorkspaceSamlConfigurationTimeouts",
    "GrafanaWorkspaceSamlConfigurationTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__e6f9a347d15119928ae8ef2a3a350dab54910a89045d987264fb26b1032edd53(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    editor_role_values: typing.Sequence[builtins.str],
    workspace_id: builtins.str,
    admin_role_values: typing.Optional[typing.Sequence[builtins.str]] = None,
    allowed_organizations: typing.Optional[typing.Sequence[builtins.str]] = None,
    email_assertion: typing.Optional[builtins.str] = None,
    groups_assertion: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    idp_metadata_url: typing.Optional[builtins.str] = None,
    idp_metadata_xml: typing.Optional[builtins.str] = None,
    login_assertion: typing.Optional[builtins.str] = None,
    login_validity_duration: typing.Optional[jsii.Number] = None,
    name_assertion: typing.Optional[builtins.str] = None,
    org_assertion: typing.Optional[builtins.str] = None,
    role_assertion: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[GrafanaWorkspaceSamlConfigurationTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__b1dd1fcc6b7518fc9a3fbb7825ae52bd2240d7fa2c651ea969022e56c800bfe7(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ef06bffbbd5e4dbb40c61a59d11a8bcf3bcc1aeb5c302856075221cb485535b(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06af71db3090fc0345e7f69f7285f8cea60dba7ac93b321d5616d1ab220765d6(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ad7998232ebcf3bdedf0760afd830844ff1a9ba0a157dfe2ba0258bf1fccbeb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e2a7de96c8b2d25e2c055decb12c25d7134fa9ac5050fe4fab092176a1ccf25(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f659c25e99db56a9d020bb6c610219522a9bdeee69c265bb501b08f6fcb90895(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb7876e8039a1adb395cf12fe57e689880b0da14c7abae444be154d560a486f2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f59d956f226bb7ae81c76541cc9a6a6b00a8cab47f3ebc78919571e8bda7646(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3e978bb32b60c67b970abcb1f7b75386780e94f81a480e6e8dead8c5a40ecef(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bfd2a61c6610db02bad13df429dbf23918a69772f7402d08942db6430546d98(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49c059af7466a86996db833490c12cb64d1c473cc6d1345793fd43d1ba39c73e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f135ba30ba3a38eb34d6feef21e98590aec1da03a900b22173c283070f16b9f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05995523930b992ebea47c033245f4efc7b5ff914c22a5f71bf3897b94ab9824(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c22732b05af1cfa21c5be4fd6aa1b34d49a51576639aea431fda720cc142ea62(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__212091dfbe9514711e3403d5140111916766746702aa3c252f698e3b79dd8c6f(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    editor_role_values: typing.Sequence[builtins.str],
    workspace_id: builtins.str,
    admin_role_values: typing.Optional[typing.Sequence[builtins.str]] = None,
    allowed_organizations: typing.Optional[typing.Sequence[builtins.str]] = None,
    email_assertion: typing.Optional[builtins.str] = None,
    groups_assertion: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    idp_metadata_url: typing.Optional[builtins.str] = None,
    idp_metadata_xml: typing.Optional[builtins.str] = None,
    login_assertion: typing.Optional[builtins.str] = None,
    login_validity_duration: typing.Optional[jsii.Number] = None,
    name_assertion: typing.Optional[builtins.str] = None,
    org_assertion: typing.Optional[builtins.str] = None,
    role_assertion: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[GrafanaWorkspaceSamlConfigurationTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34c8e63668d40f8008730a9a0e9c3e3e96b50027939492d098e04558cf381472(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d03976e145e1890c1533242809aeb1a959ac27d3e24847fcd8a372eab5bb1e0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f8dedcc4adb4d94ac1ed4c3d84ebbc70c44cec357686b46b9c7d47e942d9098(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__126a3830767a266b7fdefd3da69712c95544f592609073b2e3b338a60654be06(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a97f08d44133e56f98541e4fef1cc858b5a6d6684b95089f8bb4e77b66237f2d(
    value: typing.Optional[typing.Union[GrafanaWorkspaceSamlConfigurationTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
