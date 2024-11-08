'''
# `aws_amplify_app`

Refer to the Terraform Registory for docs: [`aws_amplify_app`](https://www.terraform.io/docs/providers/aws/r/amplify_app).
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


class AmplifyApp(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.amplifyApp.AmplifyApp",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/amplify_app aws_amplify_app}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        access_token: typing.Optional[builtins.str] = None,
        auto_branch_creation_config: typing.Optional[typing.Union["AmplifyAppAutoBranchCreationConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        auto_branch_creation_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
        basic_auth_credentials: typing.Optional[builtins.str] = None,
        build_spec: typing.Optional[builtins.str] = None,
        custom_rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AmplifyAppCustomRule", typing.Dict[builtins.str, typing.Any]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        enable_auto_branch_creation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_basic_auth: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_branch_auto_build: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_branch_auto_deletion: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        environment_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        iam_service_role_arn: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        oauth_token: typing.Optional[builtins.str] = None,
        platform: typing.Optional[builtins.str] = None,
        repository: typing.Optional[builtins.str] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/amplify_app aws_amplify_app} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#name AmplifyApp#name}.
        :param access_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#access_token AmplifyApp#access_token}.
        :param auto_branch_creation_config: auto_branch_creation_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#auto_branch_creation_config AmplifyApp#auto_branch_creation_config}
        :param auto_branch_creation_patterns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#auto_branch_creation_patterns AmplifyApp#auto_branch_creation_patterns}.
        :param basic_auth_credentials: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#basic_auth_credentials AmplifyApp#basic_auth_credentials}.
        :param build_spec: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#build_spec AmplifyApp#build_spec}.
        :param custom_rule: custom_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#custom_rule AmplifyApp#custom_rule}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#description AmplifyApp#description}.
        :param enable_auto_branch_creation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#enable_auto_branch_creation AmplifyApp#enable_auto_branch_creation}.
        :param enable_basic_auth: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#enable_basic_auth AmplifyApp#enable_basic_auth}.
        :param enable_branch_auto_build: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#enable_branch_auto_build AmplifyApp#enable_branch_auto_build}.
        :param enable_branch_auto_deletion: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#enable_branch_auto_deletion AmplifyApp#enable_branch_auto_deletion}.
        :param environment_variables: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#environment_variables AmplifyApp#environment_variables}.
        :param iam_service_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#iam_service_role_arn AmplifyApp#iam_service_role_arn}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#id AmplifyApp#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param oauth_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#oauth_token AmplifyApp#oauth_token}.
        :param platform: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#platform AmplifyApp#platform}.
        :param repository: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#repository AmplifyApp#repository}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#tags AmplifyApp#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#tags_all AmplifyApp#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37bf792d1b04fb62b70f6723b38b2e9d51bda087dcad763a37151b9f91b85cfe)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AmplifyAppConfig(
            name=name,
            access_token=access_token,
            auto_branch_creation_config=auto_branch_creation_config,
            auto_branch_creation_patterns=auto_branch_creation_patterns,
            basic_auth_credentials=basic_auth_credentials,
            build_spec=build_spec,
            custom_rule=custom_rule,
            description=description,
            enable_auto_branch_creation=enable_auto_branch_creation,
            enable_basic_auth=enable_basic_auth,
            enable_branch_auto_build=enable_branch_auto_build,
            enable_branch_auto_deletion=enable_branch_auto_deletion,
            environment_variables=environment_variables,
            iam_service_role_arn=iam_service_role_arn,
            id=id,
            oauth_token=oauth_token,
            platform=platform,
            repository=repository,
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

    @jsii.member(jsii_name="putAutoBranchCreationConfig")
    def put_auto_branch_creation_config(
        self,
        *,
        basic_auth_credentials: typing.Optional[builtins.str] = None,
        build_spec: typing.Optional[builtins.str] = None,
        enable_auto_build: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_basic_auth: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_performance_mode: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_pull_request_preview: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        environment_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        framework: typing.Optional[builtins.str] = None,
        pull_request_environment_name: typing.Optional[builtins.str] = None,
        stage: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param basic_auth_credentials: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#basic_auth_credentials AmplifyApp#basic_auth_credentials}.
        :param build_spec: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#build_spec AmplifyApp#build_spec}.
        :param enable_auto_build: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#enable_auto_build AmplifyApp#enable_auto_build}.
        :param enable_basic_auth: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#enable_basic_auth AmplifyApp#enable_basic_auth}.
        :param enable_performance_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#enable_performance_mode AmplifyApp#enable_performance_mode}.
        :param enable_pull_request_preview: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#enable_pull_request_preview AmplifyApp#enable_pull_request_preview}.
        :param environment_variables: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#environment_variables AmplifyApp#environment_variables}.
        :param framework: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#framework AmplifyApp#framework}.
        :param pull_request_environment_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#pull_request_environment_name AmplifyApp#pull_request_environment_name}.
        :param stage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#stage AmplifyApp#stage}.
        '''
        value = AmplifyAppAutoBranchCreationConfig(
            basic_auth_credentials=basic_auth_credentials,
            build_spec=build_spec,
            enable_auto_build=enable_auto_build,
            enable_basic_auth=enable_basic_auth,
            enable_performance_mode=enable_performance_mode,
            enable_pull_request_preview=enable_pull_request_preview,
            environment_variables=environment_variables,
            framework=framework,
            pull_request_environment_name=pull_request_environment_name,
            stage=stage,
        )

        return typing.cast(None, jsii.invoke(self, "putAutoBranchCreationConfig", [value]))

    @jsii.member(jsii_name="putCustomRule")
    def put_custom_rule(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AmplifyAppCustomRule", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__430c864841ad7420e8ca202873d21258254cf4534c1fc53dedfe2237df2496ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCustomRule", [value]))

    @jsii.member(jsii_name="resetAccessToken")
    def reset_access_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessToken", []))

    @jsii.member(jsii_name="resetAutoBranchCreationConfig")
    def reset_auto_branch_creation_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoBranchCreationConfig", []))

    @jsii.member(jsii_name="resetAutoBranchCreationPatterns")
    def reset_auto_branch_creation_patterns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoBranchCreationPatterns", []))

    @jsii.member(jsii_name="resetBasicAuthCredentials")
    def reset_basic_auth_credentials(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBasicAuthCredentials", []))

    @jsii.member(jsii_name="resetBuildSpec")
    def reset_build_spec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBuildSpec", []))

    @jsii.member(jsii_name="resetCustomRule")
    def reset_custom_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomRule", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetEnableAutoBranchCreation")
    def reset_enable_auto_branch_creation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableAutoBranchCreation", []))

    @jsii.member(jsii_name="resetEnableBasicAuth")
    def reset_enable_basic_auth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableBasicAuth", []))

    @jsii.member(jsii_name="resetEnableBranchAutoBuild")
    def reset_enable_branch_auto_build(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableBranchAutoBuild", []))

    @jsii.member(jsii_name="resetEnableBranchAutoDeletion")
    def reset_enable_branch_auto_deletion(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableBranchAutoDeletion", []))

    @jsii.member(jsii_name="resetEnvironmentVariables")
    def reset_environment_variables(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnvironmentVariables", []))

    @jsii.member(jsii_name="resetIamServiceRoleArn")
    def reset_iam_service_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIamServiceRoleArn", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetOauthToken")
    def reset_oauth_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthToken", []))

    @jsii.member(jsii_name="resetPlatform")
    def reset_platform(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlatform", []))

    @jsii.member(jsii_name="resetRepository")
    def reset_repository(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRepository", []))

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
    @jsii.member(jsii_name="autoBranchCreationConfig")
    def auto_branch_creation_config(
        self,
    ) -> "AmplifyAppAutoBranchCreationConfigOutputReference":
        return typing.cast("AmplifyAppAutoBranchCreationConfigOutputReference", jsii.get(self, "autoBranchCreationConfig"))

    @builtins.property
    @jsii.member(jsii_name="customRule")
    def custom_rule(self) -> "AmplifyAppCustomRuleList":
        return typing.cast("AmplifyAppCustomRuleList", jsii.get(self, "customRule"))

    @builtins.property
    @jsii.member(jsii_name="defaultDomain")
    def default_domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultDomain"))

    @builtins.property
    @jsii.member(jsii_name="productionBranch")
    def production_branch(self) -> "AmplifyAppProductionBranchList":
        return typing.cast("AmplifyAppProductionBranchList", jsii.get(self, "productionBranch"))

    @builtins.property
    @jsii.member(jsii_name="accessTokenInput")
    def access_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="autoBranchCreationConfigInput")
    def auto_branch_creation_config_input(
        self,
    ) -> typing.Optional["AmplifyAppAutoBranchCreationConfig"]:
        return typing.cast(typing.Optional["AmplifyAppAutoBranchCreationConfig"], jsii.get(self, "autoBranchCreationConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="autoBranchCreationPatternsInput")
    def auto_branch_creation_patterns_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "autoBranchCreationPatternsInput"))

    @builtins.property
    @jsii.member(jsii_name="basicAuthCredentialsInput")
    def basic_auth_credentials_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "basicAuthCredentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="buildSpecInput")
    def build_spec_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "buildSpecInput"))

    @builtins.property
    @jsii.member(jsii_name="customRuleInput")
    def custom_rule_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AmplifyAppCustomRule"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AmplifyAppCustomRule"]]], jsii.get(self, "customRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="enableAutoBranchCreationInput")
    def enable_auto_branch_creation_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableAutoBranchCreationInput"))

    @builtins.property
    @jsii.member(jsii_name="enableBasicAuthInput")
    def enable_basic_auth_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableBasicAuthInput"))

    @builtins.property
    @jsii.member(jsii_name="enableBranchAutoBuildInput")
    def enable_branch_auto_build_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableBranchAutoBuildInput"))

    @builtins.property
    @jsii.member(jsii_name="enableBranchAutoDeletionInput")
    def enable_branch_auto_deletion_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableBranchAutoDeletionInput"))

    @builtins.property
    @jsii.member(jsii_name="environmentVariablesInput")
    def environment_variables_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "environmentVariablesInput"))

    @builtins.property
    @jsii.member(jsii_name="iamServiceRoleArnInput")
    def iam_service_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iamServiceRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthTokenInput")
    def oauth_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oauthTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="platformInput")
    def platform_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "platformInput"))

    @builtins.property
    @jsii.member(jsii_name="repositoryInput")
    def repository_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repositoryInput"))

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
    @jsii.member(jsii_name="accessToken")
    def access_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessToken"))

    @access_token.setter
    def access_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e35a3b905d1c8cb96d521019bce578b92ebdc96bb9c61a6753522fc0962d5923)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessToken", value)

    @builtins.property
    @jsii.member(jsii_name="autoBranchCreationPatterns")
    def auto_branch_creation_patterns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "autoBranchCreationPatterns"))

    @auto_branch_creation_patterns.setter
    def auto_branch_creation_patterns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6f400f31eebfdf00d7c3cb13edfde121447e4adbc856794cbfd1ea23e002ad6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoBranchCreationPatterns", value)

    @builtins.property
    @jsii.member(jsii_name="basicAuthCredentials")
    def basic_auth_credentials(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "basicAuthCredentials"))

    @basic_auth_credentials.setter
    def basic_auth_credentials(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f57d699c6485f9a2a181a3d96695239d3c33e36e8e3a0f671e8aba00e770efe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "basicAuthCredentials", value)

    @builtins.property
    @jsii.member(jsii_name="buildSpec")
    def build_spec(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "buildSpec"))

    @build_spec.setter
    def build_spec(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc3c7d8f20841009c2e1ab1351295361583a180cb7cde66fbdf11a99ed6114c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "buildSpec", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aff999bcfceb6680917b1014fa5a468968bcf78062e477571cc8c9b502ce8698)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="enableAutoBranchCreation")
    def enable_auto_branch_creation(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableAutoBranchCreation"))

    @enable_auto_branch_creation.setter
    def enable_auto_branch_creation(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec632b9be5245f3b1ee434dfec431c93af428ce6a82c4901a7d19648949166ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableAutoBranchCreation", value)

    @builtins.property
    @jsii.member(jsii_name="enableBasicAuth")
    def enable_basic_auth(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableBasicAuth"))

    @enable_basic_auth.setter
    def enable_basic_auth(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d52f07f15462915145a1a31f33ef75068d1871583acde7afc25315e53af0b7b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableBasicAuth", value)

    @builtins.property
    @jsii.member(jsii_name="enableBranchAutoBuild")
    def enable_branch_auto_build(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableBranchAutoBuild"))

    @enable_branch_auto_build.setter
    def enable_branch_auto_build(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6420ebdb217dc04ea9b733cfa1e2ae63d9c0db52c1c83e7f74ee7db997dc0ae2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableBranchAutoBuild", value)

    @builtins.property
    @jsii.member(jsii_name="enableBranchAutoDeletion")
    def enable_branch_auto_deletion(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableBranchAutoDeletion"))

    @enable_branch_auto_deletion.setter
    def enable_branch_auto_deletion(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3bec2c78715b02de41a31da49e7018ee13eecba281e652d51728af695b98bb7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableBranchAutoDeletion", value)

    @builtins.property
    @jsii.member(jsii_name="environmentVariables")
    def environment_variables(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "environmentVariables"))

    @environment_variables.setter
    def environment_variables(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77c27bd9342b0bf25c77b766b563c657826acdbff7b15a10c0396dc00762d24e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentVariables", value)

    @builtins.property
    @jsii.member(jsii_name="iamServiceRoleArn")
    def iam_service_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iamServiceRoleArn"))

    @iam_service_role_arn.setter
    def iam_service_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72d8e08e6b1688d91710e2e93a46c1223bf4f5466a30c7fa4c4c0dbe6380706a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamServiceRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5ef8753f95852e735142cd07111ab4890b4434d7384ca4e2b1fd231f181ad72)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7effa85304685d33870d1811c5f55b84712219602ef2f98d8989c82a39e31ae6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="oauthToken")
    def oauth_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "oauthToken"))

    @oauth_token.setter
    def oauth_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90685023fa96fd28063d4c5b1058784d3336c7bf46a0c1cd5e6430c311758831)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauthToken", value)

    @builtins.property
    @jsii.member(jsii_name="platform")
    def platform(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "platform"))

    @platform.setter
    def platform(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__071008ef36c844b9126937bc9b959a6cb1d283082565ed1f8ec1fc83b973272e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "platform", value)

    @builtins.property
    @jsii.member(jsii_name="repository")
    def repository(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repository"))

    @repository.setter
    def repository(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0694bfebc8c9bb6293d7a8772a0798a46b7ea6570219378c44362ee848fa24d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repository", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dac6ffb19d58e085ae6d908284d015f95cebbfa0742ea44ebee42f6fc330d9ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbd2d43e4e9e3e821ad79d44b6815f61ac9932bd0d8ec03a85e1819599b6d781)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.amplifyApp.AmplifyAppAutoBranchCreationConfig",
    jsii_struct_bases=[],
    name_mapping={
        "basic_auth_credentials": "basicAuthCredentials",
        "build_spec": "buildSpec",
        "enable_auto_build": "enableAutoBuild",
        "enable_basic_auth": "enableBasicAuth",
        "enable_performance_mode": "enablePerformanceMode",
        "enable_pull_request_preview": "enablePullRequestPreview",
        "environment_variables": "environmentVariables",
        "framework": "framework",
        "pull_request_environment_name": "pullRequestEnvironmentName",
        "stage": "stage",
    },
)
class AmplifyAppAutoBranchCreationConfig:
    def __init__(
        self,
        *,
        basic_auth_credentials: typing.Optional[builtins.str] = None,
        build_spec: typing.Optional[builtins.str] = None,
        enable_auto_build: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_basic_auth: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_performance_mode: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_pull_request_preview: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        environment_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        framework: typing.Optional[builtins.str] = None,
        pull_request_environment_name: typing.Optional[builtins.str] = None,
        stage: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param basic_auth_credentials: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#basic_auth_credentials AmplifyApp#basic_auth_credentials}.
        :param build_spec: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#build_spec AmplifyApp#build_spec}.
        :param enable_auto_build: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#enable_auto_build AmplifyApp#enable_auto_build}.
        :param enable_basic_auth: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#enable_basic_auth AmplifyApp#enable_basic_auth}.
        :param enable_performance_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#enable_performance_mode AmplifyApp#enable_performance_mode}.
        :param enable_pull_request_preview: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#enable_pull_request_preview AmplifyApp#enable_pull_request_preview}.
        :param environment_variables: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#environment_variables AmplifyApp#environment_variables}.
        :param framework: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#framework AmplifyApp#framework}.
        :param pull_request_environment_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#pull_request_environment_name AmplifyApp#pull_request_environment_name}.
        :param stage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#stage AmplifyApp#stage}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d462048d0d2bb7dd167f0d1b6a989b47a3974411eb8722e443ca88e7b73a5e3)
            check_type(argname="argument basic_auth_credentials", value=basic_auth_credentials, expected_type=type_hints["basic_auth_credentials"])
            check_type(argname="argument build_spec", value=build_spec, expected_type=type_hints["build_spec"])
            check_type(argname="argument enable_auto_build", value=enable_auto_build, expected_type=type_hints["enable_auto_build"])
            check_type(argname="argument enable_basic_auth", value=enable_basic_auth, expected_type=type_hints["enable_basic_auth"])
            check_type(argname="argument enable_performance_mode", value=enable_performance_mode, expected_type=type_hints["enable_performance_mode"])
            check_type(argname="argument enable_pull_request_preview", value=enable_pull_request_preview, expected_type=type_hints["enable_pull_request_preview"])
            check_type(argname="argument environment_variables", value=environment_variables, expected_type=type_hints["environment_variables"])
            check_type(argname="argument framework", value=framework, expected_type=type_hints["framework"])
            check_type(argname="argument pull_request_environment_name", value=pull_request_environment_name, expected_type=type_hints["pull_request_environment_name"])
            check_type(argname="argument stage", value=stage, expected_type=type_hints["stage"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if basic_auth_credentials is not None:
            self._values["basic_auth_credentials"] = basic_auth_credentials
        if build_spec is not None:
            self._values["build_spec"] = build_spec
        if enable_auto_build is not None:
            self._values["enable_auto_build"] = enable_auto_build
        if enable_basic_auth is not None:
            self._values["enable_basic_auth"] = enable_basic_auth
        if enable_performance_mode is not None:
            self._values["enable_performance_mode"] = enable_performance_mode
        if enable_pull_request_preview is not None:
            self._values["enable_pull_request_preview"] = enable_pull_request_preview
        if environment_variables is not None:
            self._values["environment_variables"] = environment_variables
        if framework is not None:
            self._values["framework"] = framework
        if pull_request_environment_name is not None:
            self._values["pull_request_environment_name"] = pull_request_environment_name
        if stage is not None:
            self._values["stage"] = stage

    @builtins.property
    def basic_auth_credentials(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#basic_auth_credentials AmplifyApp#basic_auth_credentials}.'''
        result = self._values.get("basic_auth_credentials")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def build_spec(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#build_spec AmplifyApp#build_spec}.'''
        result = self._values.get("build_spec")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_auto_build(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#enable_auto_build AmplifyApp#enable_auto_build}.'''
        result = self._values.get("enable_auto_build")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def enable_basic_auth(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#enable_basic_auth AmplifyApp#enable_basic_auth}.'''
        result = self._values.get("enable_basic_auth")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def enable_performance_mode(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#enable_performance_mode AmplifyApp#enable_performance_mode}.'''
        result = self._values.get("enable_performance_mode")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def enable_pull_request_preview(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#enable_pull_request_preview AmplifyApp#enable_pull_request_preview}.'''
        result = self._values.get("enable_pull_request_preview")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def environment_variables(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#environment_variables AmplifyApp#environment_variables}.'''
        result = self._values.get("environment_variables")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def framework(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#framework AmplifyApp#framework}.'''
        result = self._values.get("framework")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pull_request_environment_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#pull_request_environment_name AmplifyApp#pull_request_environment_name}.'''
        result = self._values.get("pull_request_environment_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def stage(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#stage AmplifyApp#stage}.'''
        result = self._values.get("stage")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AmplifyAppAutoBranchCreationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AmplifyAppAutoBranchCreationConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.amplifyApp.AmplifyAppAutoBranchCreationConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ae340ed8803ab205fcc009a54b2eeb5c83d911e17935303805d9e0841ba6a21b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBasicAuthCredentials")
    def reset_basic_auth_credentials(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBasicAuthCredentials", []))

    @jsii.member(jsii_name="resetBuildSpec")
    def reset_build_spec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBuildSpec", []))

    @jsii.member(jsii_name="resetEnableAutoBuild")
    def reset_enable_auto_build(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableAutoBuild", []))

    @jsii.member(jsii_name="resetEnableBasicAuth")
    def reset_enable_basic_auth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableBasicAuth", []))

    @jsii.member(jsii_name="resetEnablePerformanceMode")
    def reset_enable_performance_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnablePerformanceMode", []))

    @jsii.member(jsii_name="resetEnablePullRequestPreview")
    def reset_enable_pull_request_preview(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnablePullRequestPreview", []))

    @jsii.member(jsii_name="resetEnvironmentVariables")
    def reset_environment_variables(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnvironmentVariables", []))

    @jsii.member(jsii_name="resetFramework")
    def reset_framework(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFramework", []))

    @jsii.member(jsii_name="resetPullRequestEnvironmentName")
    def reset_pull_request_environment_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPullRequestEnvironmentName", []))

    @jsii.member(jsii_name="resetStage")
    def reset_stage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStage", []))

    @builtins.property
    @jsii.member(jsii_name="basicAuthCredentialsInput")
    def basic_auth_credentials_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "basicAuthCredentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="buildSpecInput")
    def build_spec_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "buildSpecInput"))

    @builtins.property
    @jsii.member(jsii_name="enableAutoBuildInput")
    def enable_auto_build_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableAutoBuildInput"))

    @builtins.property
    @jsii.member(jsii_name="enableBasicAuthInput")
    def enable_basic_auth_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableBasicAuthInput"))

    @builtins.property
    @jsii.member(jsii_name="enablePerformanceModeInput")
    def enable_performance_mode_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enablePerformanceModeInput"))

    @builtins.property
    @jsii.member(jsii_name="enablePullRequestPreviewInput")
    def enable_pull_request_preview_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enablePullRequestPreviewInput"))

    @builtins.property
    @jsii.member(jsii_name="environmentVariablesInput")
    def environment_variables_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "environmentVariablesInput"))

    @builtins.property
    @jsii.member(jsii_name="frameworkInput")
    def framework_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "frameworkInput"))

    @builtins.property
    @jsii.member(jsii_name="pullRequestEnvironmentNameInput")
    def pull_request_environment_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pullRequestEnvironmentNameInput"))

    @builtins.property
    @jsii.member(jsii_name="stageInput")
    def stage_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stageInput"))

    @builtins.property
    @jsii.member(jsii_name="basicAuthCredentials")
    def basic_auth_credentials(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "basicAuthCredentials"))

    @basic_auth_credentials.setter
    def basic_auth_credentials(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc697e831f40d0061a8ad20e7afddaeb603064f61466ec088dc6d04529ccbf65)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "basicAuthCredentials", value)

    @builtins.property
    @jsii.member(jsii_name="buildSpec")
    def build_spec(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "buildSpec"))

    @build_spec.setter
    def build_spec(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ecd1b1a12ac46b5b93878f67c93ec32a7fc03a59ee7ef235deb07df9bed97d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "buildSpec", value)

    @builtins.property
    @jsii.member(jsii_name="enableAutoBuild")
    def enable_auto_build(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableAutoBuild"))

    @enable_auto_build.setter
    def enable_auto_build(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__027835dc24967d9ac0fa7d56ae993d342285b9458e6dbd6a419e58c173b6b414)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableAutoBuild", value)

    @builtins.property
    @jsii.member(jsii_name="enableBasicAuth")
    def enable_basic_auth(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableBasicAuth"))

    @enable_basic_auth.setter
    def enable_basic_auth(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efc53ad94d219cae2f42106d8ae09eb5e0e07fbf667c93cc76d0789e1a4bbc3a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableBasicAuth", value)

    @builtins.property
    @jsii.member(jsii_name="enablePerformanceMode")
    def enable_performance_mode(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enablePerformanceMode"))

    @enable_performance_mode.setter
    def enable_performance_mode(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f95d5174d738eb72d9411af0cd1580ac950b66ca44ec9854f6a36f2aada262bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enablePerformanceMode", value)

    @builtins.property
    @jsii.member(jsii_name="enablePullRequestPreview")
    def enable_pull_request_preview(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enablePullRequestPreview"))

    @enable_pull_request_preview.setter
    def enable_pull_request_preview(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc7da1a914f89cea863068f581ed380a3f8b5fd08eaae294b670889ec2c6018a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enablePullRequestPreview", value)

    @builtins.property
    @jsii.member(jsii_name="environmentVariables")
    def environment_variables(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "environmentVariables"))

    @environment_variables.setter
    def environment_variables(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc1591b6e6936f03f3b9457e29813de20c61a777f11475408031ce0fcf776db7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentVariables", value)

    @builtins.property
    @jsii.member(jsii_name="framework")
    def framework(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "framework"))

    @framework.setter
    def framework(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9df0cb79b948cee65e139623d723d61c13e391b6ef144c66ca32c6bcef167643)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "framework", value)

    @builtins.property
    @jsii.member(jsii_name="pullRequestEnvironmentName")
    def pull_request_environment_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pullRequestEnvironmentName"))

    @pull_request_environment_name.setter
    def pull_request_environment_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47ff74e1eb0e9cb64e781cc0b1720e77e44331a2375c8a3a263ccbdea656f4bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pullRequestEnvironmentName", value)

    @builtins.property
    @jsii.member(jsii_name="stage")
    def stage(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stage"))

    @stage.setter
    def stage(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44c77aa1404b35ce30a18e0cc523f3a8774f1847f029eb54b47ad2754105f9db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stage", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AmplifyAppAutoBranchCreationConfig]:
        return typing.cast(typing.Optional[AmplifyAppAutoBranchCreationConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AmplifyAppAutoBranchCreationConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5673212d23e05b5d6267b998cb3fef8fc9e6a85dc9f3f24e6097ab254cca39fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.amplifyApp.AmplifyAppConfig",
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
        "access_token": "accessToken",
        "auto_branch_creation_config": "autoBranchCreationConfig",
        "auto_branch_creation_patterns": "autoBranchCreationPatterns",
        "basic_auth_credentials": "basicAuthCredentials",
        "build_spec": "buildSpec",
        "custom_rule": "customRule",
        "description": "description",
        "enable_auto_branch_creation": "enableAutoBranchCreation",
        "enable_basic_auth": "enableBasicAuth",
        "enable_branch_auto_build": "enableBranchAutoBuild",
        "enable_branch_auto_deletion": "enableBranchAutoDeletion",
        "environment_variables": "environmentVariables",
        "iam_service_role_arn": "iamServiceRoleArn",
        "id": "id",
        "oauth_token": "oauthToken",
        "platform": "platform",
        "repository": "repository",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class AmplifyAppConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        access_token: typing.Optional[builtins.str] = None,
        auto_branch_creation_config: typing.Optional[typing.Union[AmplifyAppAutoBranchCreationConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        auto_branch_creation_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
        basic_auth_credentials: typing.Optional[builtins.str] = None,
        build_spec: typing.Optional[builtins.str] = None,
        custom_rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AmplifyAppCustomRule", typing.Dict[builtins.str, typing.Any]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        enable_auto_branch_creation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_basic_auth: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_branch_auto_build: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_branch_auto_deletion: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        environment_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        iam_service_role_arn: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        oauth_token: typing.Optional[builtins.str] = None,
        platform: typing.Optional[builtins.str] = None,
        repository: typing.Optional[builtins.str] = None,
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
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#name AmplifyApp#name}.
        :param access_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#access_token AmplifyApp#access_token}.
        :param auto_branch_creation_config: auto_branch_creation_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#auto_branch_creation_config AmplifyApp#auto_branch_creation_config}
        :param auto_branch_creation_patterns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#auto_branch_creation_patterns AmplifyApp#auto_branch_creation_patterns}.
        :param basic_auth_credentials: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#basic_auth_credentials AmplifyApp#basic_auth_credentials}.
        :param build_spec: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#build_spec AmplifyApp#build_spec}.
        :param custom_rule: custom_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#custom_rule AmplifyApp#custom_rule}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#description AmplifyApp#description}.
        :param enable_auto_branch_creation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#enable_auto_branch_creation AmplifyApp#enable_auto_branch_creation}.
        :param enable_basic_auth: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#enable_basic_auth AmplifyApp#enable_basic_auth}.
        :param enable_branch_auto_build: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#enable_branch_auto_build AmplifyApp#enable_branch_auto_build}.
        :param enable_branch_auto_deletion: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#enable_branch_auto_deletion AmplifyApp#enable_branch_auto_deletion}.
        :param environment_variables: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#environment_variables AmplifyApp#environment_variables}.
        :param iam_service_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#iam_service_role_arn AmplifyApp#iam_service_role_arn}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#id AmplifyApp#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param oauth_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#oauth_token AmplifyApp#oauth_token}.
        :param platform: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#platform AmplifyApp#platform}.
        :param repository: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#repository AmplifyApp#repository}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#tags AmplifyApp#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#tags_all AmplifyApp#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(auto_branch_creation_config, dict):
            auto_branch_creation_config = AmplifyAppAutoBranchCreationConfig(**auto_branch_creation_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcb933108e9cee6c369823a9f7e754c14a0c0c3eee2e533238bcd935609fddb1)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument access_token", value=access_token, expected_type=type_hints["access_token"])
            check_type(argname="argument auto_branch_creation_config", value=auto_branch_creation_config, expected_type=type_hints["auto_branch_creation_config"])
            check_type(argname="argument auto_branch_creation_patterns", value=auto_branch_creation_patterns, expected_type=type_hints["auto_branch_creation_patterns"])
            check_type(argname="argument basic_auth_credentials", value=basic_auth_credentials, expected_type=type_hints["basic_auth_credentials"])
            check_type(argname="argument build_spec", value=build_spec, expected_type=type_hints["build_spec"])
            check_type(argname="argument custom_rule", value=custom_rule, expected_type=type_hints["custom_rule"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument enable_auto_branch_creation", value=enable_auto_branch_creation, expected_type=type_hints["enable_auto_branch_creation"])
            check_type(argname="argument enable_basic_auth", value=enable_basic_auth, expected_type=type_hints["enable_basic_auth"])
            check_type(argname="argument enable_branch_auto_build", value=enable_branch_auto_build, expected_type=type_hints["enable_branch_auto_build"])
            check_type(argname="argument enable_branch_auto_deletion", value=enable_branch_auto_deletion, expected_type=type_hints["enable_branch_auto_deletion"])
            check_type(argname="argument environment_variables", value=environment_variables, expected_type=type_hints["environment_variables"])
            check_type(argname="argument iam_service_role_arn", value=iam_service_role_arn, expected_type=type_hints["iam_service_role_arn"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument oauth_token", value=oauth_token, expected_type=type_hints["oauth_token"])
            check_type(argname="argument platform", value=platform, expected_type=type_hints["platform"])
            check_type(argname="argument repository", value=repository, expected_type=type_hints["repository"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
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
        if access_token is not None:
            self._values["access_token"] = access_token
        if auto_branch_creation_config is not None:
            self._values["auto_branch_creation_config"] = auto_branch_creation_config
        if auto_branch_creation_patterns is not None:
            self._values["auto_branch_creation_patterns"] = auto_branch_creation_patterns
        if basic_auth_credentials is not None:
            self._values["basic_auth_credentials"] = basic_auth_credentials
        if build_spec is not None:
            self._values["build_spec"] = build_spec
        if custom_rule is not None:
            self._values["custom_rule"] = custom_rule
        if description is not None:
            self._values["description"] = description
        if enable_auto_branch_creation is not None:
            self._values["enable_auto_branch_creation"] = enable_auto_branch_creation
        if enable_basic_auth is not None:
            self._values["enable_basic_auth"] = enable_basic_auth
        if enable_branch_auto_build is not None:
            self._values["enable_branch_auto_build"] = enable_branch_auto_build
        if enable_branch_auto_deletion is not None:
            self._values["enable_branch_auto_deletion"] = enable_branch_auto_deletion
        if environment_variables is not None:
            self._values["environment_variables"] = environment_variables
        if iam_service_role_arn is not None:
            self._values["iam_service_role_arn"] = iam_service_role_arn
        if id is not None:
            self._values["id"] = id
        if oauth_token is not None:
            self._values["oauth_token"] = oauth_token
        if platform is not None:
            self._values["platform"] = platform
        if repository is not None:
            self._values["repository"] = repository
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
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#name AmplifyApp#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#access_token AmplifyApp#access_token}.'''
        result = self._values.get("access_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auto_branch_creation_config(
        self,
    ) -> typing.Optional[AmplifyAppAutoBranchCreationConfig]:
        '''auto_branch_creation_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#auto_branch_creation_config AmplifyApp#auto_branch_creation_config}
        '''
        result = self._values.get("auto_branch_creation_config")
        return typing.cast(typing.Optional[AmplifyAppAutoBranchCreationConfig], result)

    @builtins.property
    def auto_branch_creation_patterns(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#auto_branch_creation_patterns AmplifyApp#auto_branch_creation_patterns}.'''
        result = self._values.get("auto_branch_creation_patterns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def basic_auth_credentials(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#basic_auth_credentials AmplifyApp#basic_auth_credentials}.'''
        result = self._values.get("basic_auth_credentials")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def build_spec(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#build_spec AmplifyApp#build_spec}.'''
        result = self._values.get("build_spec")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_rule(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AmplifyAppCustomRule"]]]:
        '''custom_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#custom_rule AmplifyApp#custom_rule}
        '''
        result = self._values.get("custom_rule")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AmplifyAppCustomRule"]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#description AmplifyApp#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_auto_branch_creation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#enable_auto_branch_creation AmplifyApp#enable_auto_branch_creation}.'''
        result = self._values.get("enable_auto_branch_creation")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def enable_basic_auth(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#enable_basic_auth AmplifyApp#enable_basic_auth}.'''
        result = self._values.get("enable_basic_auth")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def enable_branch_auto_build(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#enable_branch_auto_build AmplifyApp#enable_branch_auto_build}.'''
        result = self._values.get("enable_branch_auto_build")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def enable_branch_auto_deletion(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#enable_branch_auto_deletion AmplifyApp#enable_branch_auto_deletion}.'''
        result = self._values.get("enable_branch_auto_deletion")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def environment_variables(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#environment_variables AmplifyApp#environment_variables}.'''
        result = self._values.get("environment_variables")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def iam_service_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#iam_service_role_arn AmplifyApp#iam_service_role_arn}.'''
        result = self._values.get("iam_service_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#id AmplifyApp#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#oauth_token AmplifyApp#oauth_token}.'''
        result = self._values.get("oauth_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def platform(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#platform AmplifyApp#platform}.'''
        result = self._values.get("platform")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def repository(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#repository AmplifyApp#repository}.'''
        result = self._values.get("repository")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#tags AmplifyApp#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#tags_all AmplifyApp#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AmplifyAppConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.amplifyApp.AmplifyAppCustomRule",
    jsii_struct_bases=[],
    name_mapping={
        "source": "source",
        "target": "target",
        "condition": "condition",
        "status": "status",
    },
)
class AmplifyAppCustomRule:
    def __init__(
        self,
        *,
        source: builtins.str,
        target: builtins.str,
        condition: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param source: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#source AmplifyApp#source}.
        :param target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#target AmplifyApp#target}.
        :param condition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#condition AmplifyApp#condition}.
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#status AmplifyApp#status}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1a3fb1fb1133606a9e5d0d13f5b777461ae646c26f1055549d3feb021907880)
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument condition", value=condition, expected_type=type_hints["condition"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "source": source,
            "target": target,
        }
        if condition is not None:
            self._values["condition"] = condition
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def source(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#source AmplifyApp#source}.'''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#target AmplifyApp#target}.'''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def condition(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#condition AmplifyApp#condition}.'''
        result = self._values.get("condition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/amplify_app#status AmplifyApp#status}.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AmplifyAppCustomRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AmplifyAppCustomRuleList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.amplifyApp.AmplifyAppCustomRuleList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8914a3c5233ea6045686e15632b805a008b69eff1a6dd201cf55d0557d85af7a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AmplifyAppCustomRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f60440453d1ebc56640a149ef44a219da7fa70112840c4d6a0c7553efa9eb27)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AmplifyAppCustomRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c53331788616c9b924ff9d0bdcabcf4e3a68e4d37d0a8a2d06714642947dfc39)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f8bb89e296fb45fa3affbd5ec59ec076f0de15f64d17fcc7755583aa9488365a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__07943ed4574020ae3f37fe3732f874151c5414d6f9687a3da4545b37cc491224)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AmplifyAppCustomRule]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AmplifyAppCustomRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AmplifyAppCustomRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c53c3cb573cc69aec913d10a6026aa8bb38828d892de6ceae1758ceebbffd57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AmplifyAppCustomRuleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.amplifyApp.AmplifyAppCustomRuleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e43c908b075df7a4a9bcdec0006477ce1c1d81ac7d03134e70d9a122e9224107)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCondition")
    def reset_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCondition", []))

    @jsii.member(jsii_name="resetStatus")
    def reset_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatus", []))

    @builtins.property
    @jsii.member(jsii_name="conditionInput")
    def condition_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "conditionInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceInput")
    def source_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceInput"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="condition")
    def condition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "condition"))

    @condition.setter
    def condition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__faadf8979564f52ae402839bd1e483478879fff07d950477f60372a200d7e1a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "condition", value)

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "source"))

    @source.setter
    def source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__765ce9cc39c3822d3853ff957b6e606cf862a66f3dd0f78b77bdb7e2047e8e4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0461b43614ab152fb513ae5db537c55cbeb69572f87297d80bf50a1c4df9640)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae3a6aa0c7dee5383b88aeb021821fb7efdfcce777642ae153bcd322c2af3060)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AmplifyAppCustomRule, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AmplifyAppCustomRule, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AmplifyAppCustomRule, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc8947a7b0db1734a9e3f2a4f8e2dda6af577e7b10f534f4776f11c8e9dcaf44)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.amplifyApp.AmplifyAppProductionBranch",
    jsii_struct_bases=[],
    name_mapping={},
)
class AmplifyAppProductionBranch:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AmplifyAppProductionBranch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AmplifyAppProductionBranchList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.amplifyApp.AmplifyAppProductionBranchList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7efb20843dc617e6df2ce767c57d6be221056981fd469397fdbb7cff262c4bd4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AmplifyAppProductionBranchOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__611a2d954665d48fab4b1786bcd6f72fddb19980e87a8f101595685a90b53504)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AmplifyAppProductionBranchOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c821e351c8b77df1dd19f2e8549ba86ab2d71b0e8db93b3ebf8d3735c2d6a84)
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
            type_hints = typing.get_type_hints(_typecheckingstub__385e1d541417a37eac9ed0eafe4a8fd85aa30b8c8f74731fef30c75f0bc2213e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__625a1f17361ea90e494506c9cc8172c363745cb3737689f9597b75cb5b0da4e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class AmplifyAppProductionBranchOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.amplifyApp.AmplifyAppProductionBranchOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9dfcbf62df8d8db27218ba1a9685a6d52ad5ba61b130e554a058d3f241ec887e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="branchName")
    def branch_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "branchName"))

    @builtins.property
    @jsii.member(jsii_name="lastDeployTime")
    def last_deploy_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastDeployTime"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="thumbnailUrl")
    def thumbnail_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "thumbnailUrl"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AmplifyAppProductionBranch]:
        return typing.cast(typing.Optional[AmplifyAppProductionBranch], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AmplifyAppProductionBranch],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc64e2876c3cac7bf5908dff52bddaca39f44466fb512f7d2c14e9eb164c4c9e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "AmplifyApp",
    "AmplifyAppAutoBranchCreationConfig",
    "AmplifyAppAutoBranchCreationConfigOutputReference",
    "AmplifyAppConfig",
    "AmplifyAppCustomRule",
    "AmplifyAppCustomRuleList",
    "AmplifyAppCustomRuleOutputReference",
    "AmplifyAppProductionBranch",
    "AmplifyAppProductionBranchList",
    "AmplifyAppProductionBranchOutputReference",
]

publication.publish()

def _typecheckingstub__37bf792d1b04fb62b70f6723b38b2e9d51bda087dcad763a37151b9f91b85cfe(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    access_token: typing.Optional[builtins.str] = None,
    auto_branch_creation_config: typing.Optional[typing.Union[AmplifyAppAutoBranchCreationConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    auto_branch_creation_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
    basic_auth_credentials: typing.Optional[builtins.str] = None,
    build_spec: typing.Optional[builtins.str] = None,
    custom_rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AmplifyAppCustomRule, typing.Dict[builtins.str, typing.Any]]]]] = None,
    description: typing.Optional[builtins.str] = None,
    enable_auto_branch_creation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_basic_auth: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_branch_auto_build: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_branch_auto_deletion: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    environment_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    iam_service_role_arn: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    oauth_token: typing.Optional[builtins.str] = None,
    platform: typing.Optional[builtins.str] = None,
    repository: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__430c864841ad7420e8ca202873d21258254cf4534c1fc53dedfe2237df2496ad(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AmplifyAppCustomRule, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e35a3b905d1c8cb96d521019bce578b92ebdc96bb9c61a6753522fc0962d5923(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6f400f31eebfdf00d7c3cb13edfde121447e4adbc856794cbfd1ea23e002ad6(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f57d699c6485f9a2a181a3d96695239d3c33e36e8e3a0f671e8aba00e770efe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc3c7d8f20841009c2e1ab1351295361583a180cb7cde66fbdf11a99ed6114c7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aff999bcfceb6680917b1014fa5a468968bcf78062e477571cc8c9b502ce8698(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec632b9be5245f3b1ee434dfec431c93af428ce6a82c4901a7d19648949166ed(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d52f07f15462915145a1a31f33ef75068d1871583acde7afc25315e53af0b7b3(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6420ebdb217dc04ea9b733cfa1e2ae63d9c0db52c1c83e7f74ee7db997dc0ae2(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bec2c78715b02de41a31da49e7018ee13eecba281e652d51728af695b98bb7b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77c27bd9342b0bf25c77b766b563c657826acdbff7b15a10c0396dc00762d24e(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72d8e08e6b1688d91710e2e93a46c1223bf4f5466a30c7fa4c4c0dbe6380706a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5ef8753f95852e735142cd07111ab4890b4434d7384ca4e2b1fd231f181ad72(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7effa85304685d33870d1811c5f55b84712219602ef2f98d8989c82a39e31ae6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90685023fa96fd28063d4c5b1058784d3336c7bf46a0c1cd5e6430c311758831(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__071008ef36c844b9126937bc9b959a6cb1d283082565ed1f8ec1fc83b973272e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0694bfebc8c9bb6293d7a8772a0798a46b7ea6570219378c44362ee848fa24d0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dac6ffb19d58e085ae6d908284d015f95cebbfa0742ea44ebee42f6fc330d9ce(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbd2d43e4e9e3e821ad79d44b6815f61ac9932bd0d8ec03a85e1819599b6d781(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d462048d0d2bb7dd167f0d1b6a989b47a3974411eb8722e443ca88e7b73a5e3(
    *,
    basic_auth_credentials: typing.Optional[builtins.str] = None,
    build_spec: typing.Optional[builtins.str] = None,
    enable_auto_build: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_basic_auth: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_performance_mode: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_pull_request_preview: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    environment_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    framework: typing.Optional[builtins.str] = None,
    pull_request_environment_name: typing.Optional[builtins.str] = None,
    stage: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae340ed8803ab205fcc009a54b2eeb5c83d911e17935303805d9e0841ba6a21b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc697e831f40d0061a8ad20e7afddaeb603064f61466ec088dc6d04529ccbf65(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ecd1b1a12ac46b5b93878f67c93ec32a7fc03a59ee7ef235deb07df9bed97d4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__027835dc24967d9ac0fa7d56ae993d342285b9458e6dbd6a419e58c173b6b414(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efc53ad94d219cae2f42106d8ae09eb5e0e07fbf667c93cc76d0789e1a4bbc3a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f95d5174d738eb72d9411af0cd1580ac950b66ca44ec9854f6a36f2aada262bd(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc7da1a914f89cea863068f581ed380a3f8b5fd08eaae294b670889ec2c6018a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc1591b6e6936f03f3b9457e29813de20c61a777f11475408031ce0fcf776db7(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9df0cb79b948cee65e139623d723d61c13e391b6ef144c66ca32c6bcef167643(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47ff74e1eb0e9cb64e781cc0b1720e77e44331a2375c8a3a263ccbdea656f4bb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44c77aa1404b35ce30a18e0cc523f3a8774f1847f029eb54b47ad2754105f9db(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5673212d23e05b5d6267b998cb3fef8fc9e6a85dc9f3f24e6097ab254cca39fc(
    value: typing.Optional[AmplifyAppAutoBranchCreationConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcb933108e9cee6c369823a9f7e754c14a0c0c3eee2e533238bcd935609fddb1(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    access_token: typing.Optional[builtins.str] = None,
    auto_branch_creation_config: typing.Optional[typing.Union[AmplifyAppAutoBranchCreationConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    auto_branch_creation_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
    basic_auth_credentials: typing.Optional[builtins.str] = None,
    build_spec: typing.Optional[builtins.str] = None,
    custom_rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AmplifyAppCustomRule, typing.Dict[builtins.str, typing.Any]]]]] = None,
    description: typing.Optional[builtins.str] = None,
    enable_auto_branch_creation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_basic_auth: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_branch_auto_build: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_branch_auto_deletion: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    environment_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    iam_service_role_arn: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    oauth_token: typing.Optional[builtins.str] = None,
    platform: typing.Optional[builtins.str] = None,
    repository: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1a3fb1fb1133606a9e5d0d13f5b777461ae646c26f1055549d3feb021907880(
    *,
    source: builtins.str,
    target: builtins.str,
    condition: typing.Optional[builtins.str] = None,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8914a3c5233ea6045686e15632b805a008b69eff1a6dd201cf55d0557d85af7a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f60440453d1ebc56640a149ef44a219da7fa70112840c4d6a0c7553efa9eb27(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c53331788616c9b924ff9d0bdcabcf4e3a68e4d37d0a8a2d06714642947dfc39(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8bb89e296fb45fa3affbd5ec59ec076f0de15f64d17fcc7755583aa9488365a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07943ed4574020ae3f37fe3732f874151c5414d6f9687a3da4545b37cc491224(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c53c3cb573cc69aec913d10a6026aa8bb38828d892de6ceae1758ceebbffd57(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AmplifyAppCustomRule]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e43c908b075df7a4a9bcdec0006477ce1c1d81ac7d03134e70d9a122e9224107(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__faadf8979564f52ae402839bd1e483478879fff07d950477f60372a200d7e1a8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__765ce9cc39c3822d3853ff957b6e606cf862a66f3dd0f78b77bdb7e2047e8e4e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0461b43614ab152fb513ae5db537c55cbeb69572f87297d80bf50a1c4df9640(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae3a6aa0c7dee5383b88aeb021821fb7efdfcce777642ae153bcd322c2af3060(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc8947a7b0db1734a9e3f2a4f8e2dda6af577e7b10f534f4776f11c8e9dcaf44(
    value: typing.Optional[typing.Union[AmplifyAppCustomRule, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7efb20843dc617e6df2ce767c57d6be221056981fd469397fdbb7cff262c4bd4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__611a2d954665d48fab4b1786bcd6f72fddb19980e87a8f101595685a90b53504(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c821e351c8b77df1dd19f2e8549ba86ab2d71b0e8db93b3ebf8d3735c2d6a84(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__385e1d541417a37eac9ed0eafe4a8fd85aa30b8c8f74731fef30c75f0bc2213e(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__625a1f17361ea90e494506c9cc8172c363745cb3737689f9597b75cb5b0da4e5(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9dfcbf62df8d8db27218ba1a9685a6d52ad5ba61b130e554a058d3f241ec887e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc64e2876c3cac7bf5908dff52bddaca39f44466fb512f7d2c14e9eb164c4c9e(
    value: typing.Optional[AmplifyAppProductionBranch],
) -> None:
    """Type checking stubs"""
    pass
