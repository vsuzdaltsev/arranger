'''
# `aws_gamelift_fleet`

Refer to the Terraform Registory for docs: [`aws_gamelift_fleet`](https://www.terraform.io/docs/providers/aws/r/gamelift_fleet).
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


class GameliftFleet(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.gameliftFleet.GameliftFleet",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet aws_gamelift_fleet}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        ec2_instance_type: builtins.str,
        name: builtins.str,
        build_id: typing.Optional[builtins.str] = None,
        certificate_configuration: typing.Optional[typing.Union["GameliftFleetCertificateConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        ec2_inbound_permission: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GameliftFleetEc2InboundPermission", typing.Dict[builtins.str, typing.Any]]]]] = None,
        fleet_type: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        instance_role_arn: typing.Optional[builtins.str] = None,
        metric_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        new_game_session_protection_policy: typing.Optional[builtins.str] = None,
        resource_creation_limit_policy: typing.Optional[typing.Union["GameliftFleetResourceCreationLimitPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        runtime_configuration: typing.Optional[typing.Union["GameliftFleetRuntimeConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        script_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["GameliftFleetTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet aws_gamelift_fleet} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param ec2_instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#ec2_instance_type GameliftFleet#ec2_instance_type}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#name GameliftFleet#name}.
        :param build_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#build_id GameliftFleet#build_id}.
        :param certificate_configuration: certificate_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#certificate_configuration GameliftFleet#certificate_configuration}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#description GameliftFleet#description}.
        :param ec2_inbound_permission: ec2_inbound_permission block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#ec2_inbound_permission GameliftFleet#ec2_inbound_permission}
        :param fleet_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#fleet_type GameliftFleet#fleet_type}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#id GameliftFleet#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param instance_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#instance_role_arn GameliftFleet#instance_role_arn}.
        :param metric_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#metric_groups GameliftFleet#metric_groups}.
        :param new_game_session_protection_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#new_game_session_protection_policy GameliftFleet#new_game_session_protection_policy}.
        :param resource_creation_limit_policy: resource_creation_limit_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#resource_creation_limit_policy GameliftFleet#resource_creation_limit_policy}
        :param runtime_configuration: runtime_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#runtime_configuration GameliftFleet#runtime_configuration}
        :param script_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#script_id GameliftFleet#script_id}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#tags GameliftFleet#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#tags_all GameliftFleet#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#timeouts GameliftFleet#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9218537b24144f4b1ed63b215e1d9ccf2449b90ba6fc6f0ebe0d93ac19cdf14d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GameliftFleetConfig(
            ec2_instance_type=ec2_instance_type,
            name=name,
            build_id=build_id,
            certificate_configuration=certificate_configuration,
            description=description,
            ec2_inbound_permission=ec2_inbound_permission,
            fleet_type=fleet_type,
            id=id,
            instance_role_arn=instance_role_arn,
            metric_groups=metric_groups,
            new_game_session_protection_policy=new_game_session_protection_policy,
            resource_creation_limit_policy=resource_creation_limit_policy,
            runtime_configuration=runtime_configuration,
            script_id=script_id,
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

    @jsii.member(jsii_name="putCertificateConfiguration")
    def put_certificate_configuration(
        self,
        *,
        certificate_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param certificate_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#certificate_type GameliftFleet#certificate_type}.
        '''
        value = GameliftFleetCertificateConfiguration(
            certificate_type=certificate_type
        )

        return typing.cast(None, jsii.invoke(self, "putCertificateConfiguration", [value]))

    @jsii.member(jsii_name="putEc2InboundPermission")
    def put_ec2_inbound_permission(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GameliftFleetEc2InboundPermission", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__460fe5a94b38e70af0811ca036ca84ac2b72fa5e80a1a2a1df5abe9f8644e44a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEc2InboundPermission", [value]))

    @jsii.member(jsii_name="putResourceCreationLimitPolicy")
    def put_resource_creation_limit_policy(
        self,
        *,
        new_game_sessions_per_creator: typing.Optional[jsii.Number] = None,
        policy_period_in_minutes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param new_game_sessions_per_creator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#new_game_sessions_per_creator GameliftFleet#new_game_sessions_per_creator}.
        :param policy_period_in_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#policy_period_in_minutes GameliftFleet#policy_period_in_minutes}.
        '''
        value = GameliftFleetResourceCreationLimitPolicy(
            new_game_sessions_per_creator=new_game_sessions_per_creator,
            policy_period_in_minutes=policy_period_in_minutes,
        )

        return typing.cast(None, jsii.invoke(self, "putResourceCreationLimitPolicy", [value]))

    @jsii.member(jsii_name="putRuntimeConfiguration")
    def put_runtime_configuration(
        self,
        *,
        game_session_activation_timeout_seconds: typing.Optional[jsii.Number] = None,
        max_concurrent_game_session_activations: typing.Optional[jsii.Number] = None,
        server_process: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GameliftFleetRuntimeConfigurationServerProcess", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param game_session_activation_timeout_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#game_session_activation_timeout_seconds GameliftFleet#game_session_activation_timeout_seconds}.
        :param max_concurrent_game_session_activations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#max_concurrent_game_session_activations GameliftFleet#max_concurrent_game_session_activations}.
        :param server_process: server_process block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#server_process GameliftFleet#server_process}
        '''
        value = GameliftFleetRuntimeConfiguration(
            game_session_activation_timeout_seconds=game_session_activation_timeout_seconds,
            max_concurrent_game_session_activations=max_concurrent_game_session_activations,
            server_process=server_process,
        )

        return typing.cast(None, jsii.invoke(self, "putRuntimeConfiguration", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#create GameliftFleet#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#delete GameliftFleet#delete}.
        '''
        value = GameliftFleetTimeouts(create=create, delete=delete)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetBuildId")
    def reset_build_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBuildId", []))

    @jsii.member(jsii_name="resetCertificateConfiguration")
    def reset_certificate_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificateConfiguration", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetEc2InboundPermission")
    def reset_ec2_inbound_permission(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEc2InboundPermission", []))

    @jsii.member(jsii_name="resetFleetType")
    def reset_fleet_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFleetType", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInstanceRoleArn")
    def reset_instance_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceRoleArn", []))

    @jsii.member(jsii_name="resetMetricGroups")
    def reset_metric_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricGroups", []))

    @jsii.member(jsii_name="resetNewGameSessionProtectionPolicy")
    def reset_new_game_session_protection_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNewGameSessionProtectionPolicy", []))

    @jsii.member(jsii_name="resetResourceCreationLimitPolicy")
    def reset_resource_creation_limit_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceCreationLimitPolicy", []))

    @jsii.member(jsii_name="resetRuntimeConfiguration")
    def reset_runtime_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRuntimeConfiguration", []))

    @jsii.member(jsii_name="resetScriptId")
    def reset_script_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScriptId", []))

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
    @jsii.member(jsii_name="buildArn")
    def build_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "buildArn"))

    @builtins.property
    @jsii.member(jsii_name="certificateConfiguration")
    def certificate_configuration(
        self,
    ) -> "GameliftFleetCertificateConfigurationOutputReference":
        return typing.cast("GameliftFleetCertificateConfigurationOutputReference", jsii.get(self, "certificateConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="ec2InboundPermission")
    def ec2_inbound_permission(self) -> "GameliftFleetEc2InboundPermissionList":
        return typing.cast("GameliftFleetEc2InboundPermissionList", jsii.get(self, "ec2InboundPermission"))

    @builtins.property
    @jsii.member(jsii_name="logPaths")
    def log_paths(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "logPaths"))

    @builtins.property
    @jsii.member(jsii_name="operatingSystem")
    def operating_system(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operatingSystem"))

    @builtins.property
    @jsii.member(jsii_name="resourceCreationLimitPolicy")
    def resource_creation_limit_policy(
        self,
    ) -> "GameliftFleetResourceCreationLimitPolicyOutputReference":
        return typing.cast("GameliftFleetResourceCreationLimitPolicyOutputReference", jsii.get(self, "resourceCreationLimitPolicy"))

    @builtins.property
    @jsii.member(jsii_name="runtimeConfiguration")
    def runtime_configuration(
        self,
    ) -> "GameliftFleetRuntimeConfigurationOutputReference":
        return typing.cast("GameliftFleetRuntimeConfigurationOutputReference", jsii.get(self, "runtimeConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="scriptArn")
    def script_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scriptArn"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GameliftFleetTimeoutsOutputReference":
        return typing.cast("GameliftFleetTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="buildIdInput")
    def build_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "buildIdInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateConfigurationInput")
    def certificate_configuration_input(
        self,
    ) -> typing.Optional["GameliftFleetCertificateConfiguration"]:
        return typing.cast(typing.Optional["GameliftFleetCertificateConfiguration"], jsii.get(self, "certificateConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="ec2InboundPermissionInput")
    def ec2_inbound_permission_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GameliftFleetEc2InboundPermission"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GameliftFleetEc2InboundPermission"]]], jsii.get(self, "ec2InboundPermissionInput"))

    @builtins.property
    @jsii.member(jsii_name="ec2InstanceTypeInput")
    def ec2_instance_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ec2InstanceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="fleetTypeInput")
    def fleet_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fleetTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceRoleArnInput")
    def instance_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="metricGroupsInput")
    def metric_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "metricGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="newGameSessionProtectionPolicyInput")
    def new_game_session_protection_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "newGameSessionProtectionPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceCreationLimitPolicyInput")
    def resource_creation_limit_policy_input(
        self,
    ) -> typing.Optional["GameliftFleetResourceCreationLimitPolicy"]:
        return typing.cast(typing.Optional["GameliftFleetResourceCreationLimitPolicy"], jsii.get(self, "resourceCreationLimitPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="runtimeConfigurationInput")
    def runtime_configuration_input(
        self,
    ) -> typing.Optional["GameliftFleetRuntimeConfiguration"]:
        return typing.cast(typing.Optional["GameliftFleetRuntimeConfiguration"], jsii.get(self, "runtimeConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="scriptIdInput")
    def script_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scriptIdInput"))

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
    ) -> typing.Optional[typing.Union["GameliftFleetTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GameliftFleetTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="buildId")
    def build_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "buildId"))

    @build_id.setter
    def build_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d381917c5bf0fd9ca804e46d3820d8ecd707e8860e161711d216eef7f7fe29f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "buildId", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70177906d204e7dc5407c2d921278904715f04cdbb7381a706560ecffd802c4c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="ec2InstanceType")
    def ec2_instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ec2InstanceType"))

    @ec2_instance_type.setter
    def ec2_instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb45ffa5b0b0cf04ffc7e866dd2c7b3d65a4d26af6b87ad9614f6c522ecb7b9d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ec2InstanceType", value)

    @builtins.property
    @jsii.member(jsii_name="fleetType")
    def fleet_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fleetType"))

    @fleet_type.setter
    def fleet_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__571c245e42e133c7c67e0f18901b5c520c85d5933462f3538789a9952165370c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fleetType", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dac77df9c21b038513881143e755b08e11af3aee9cd8bb1d1e2635353a7558c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="instanceRoleArn")
    def instance_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceRoleArn"))

    @instance_role_arn.setter
    def instance_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f57338f0aa2f93e263b56b37d7b3c8b5a3d1ba234b7c66b1afa9b2068314f50)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="metricGroups")
    def metric_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "metricGroups"))

    @metric_groups.setter
    def metric_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60e9b042f130ce706123b11bad5a2c9414eecf9891c083cde1e24a6b43cb3b66)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricGroups", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65e061e84f15c900361832d0deb3230b4433c7121811f987a5ec92bf7fa6230c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="newGameSessionProtectionPolicy")
    def new_game_session_protection_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "newGameSessionProtectionPolicy"))

    @new_game_session_protection_policy.setter
    def new_game_session_protection_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__911a743f4f66796815869a8b25aeb310bf621a39704fc5d957b185373c9398a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "newGameSessionProtectionPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="scriptId")
    def script_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scriptId"))

    @script_id.setter
    def script_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eaf0568c0e35f2fd027f02f366e62e526bb6c122e1d5201ac9a14c3130cdd13c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scriptId", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9528ffcd8e4933e77de0755f946590d887a317e67aa85d655ccdcc832583e635)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33aad221784d20bb5398a1951018f5bdc39ac22bd041d8879361c68e0838f30a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.gameliftFleet.GameliftFleetCertificateConfiguration",
    jsii_struct_bases=[],
    name_mapping={"certificate_type": "certificateType"},
)
class GameliftFleetCertificateConfiguration:
    def __init__(
        self,
        *,
        certificate_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param certificate_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#certificate_type GameliftFleet#certificate_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c22591cedb3f7621ffe3660deb9f3976f75e5c0529b58660215bc5fe54521bb)
            check_type(argname="argument certificate_type", value=certificate_type, expected_type=type_hints["certificate_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if certificate_type is not None:
            self._values["certificate_type"] = certificate_type

    @builtins.property
    def certificate_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#certificate_type GameliftFleet#certificate_type}.'''
        result = self._values.get("certificate_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GameliftFleetCertificateConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GameliftFleetCertificateConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.gameliftFleet.GameliftFleetCertificateConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cf18a08af1cc67f964e34479066d95f29e3700749dc8777faf6269704d3d36ba)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCertificateType")
    def reset_certificate_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificateType", []))

    @builtins.property
    @jsii.member(jsii_name="certificateTypeInput")
    def certificate_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateType")
    def certificate_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateType"))

    @certificate_type.setter
    def certificate_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4b0c70cedf98b7c61344e544d83834c374069a828b0c4cdc4802507147c3637)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GameliftFleetCertificateConfiguration]:
        return typing.cast(typing.Optional[GameliftFleetCertificateConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GameliftFleetCertificateConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b12c9e43c930ad021af3c299a84004effaab0fbab5fc26f1c7523a0140a0faf6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.gameliftFleet.GameliftFleetConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "ec2_instance_type": "ec2InstanceType",
        "name": "name",
        "build_id": "buildId",
        "certificate_configuration": "certificateConfiguration",
        "description": "description",
        "ec2_inbound_permission": "ec2InboundPermission",
        "fleet_type": "fleetType",
        "id": "id",
        "instance_role_arn": "instanceRoleArn",
        "metric_groups": "metricGroups",
        "new_game_session_protection_policy": "newGameSessionProtectionPolicy",
        "resource_creation_limit_policy": "resourceCreationLimitPolicy",
        "runtime_configuration": "runtimeConfiguration",
        "script_id": "scriptId",
        "tags": "tags",
        "tags_all": "tagsAll",
        "timeouts": "timeouts",
    },
)
class GameliftFleetConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        ec2_instance_type: builtins.str,
        name: builtins.str,
        build_id: typing.Optional[builtins.str] = None,
        certificate_configuration: typing.Optional[typing.Union[GameliftFleetCertificateConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        ec2_inbound_permission: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GameliftFleetEc2InboundPermission", typing.Dict[builtins.str, typing.Any]]]]] = None,
        fleet_type: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        instance_role_arn: typing.Optional[builtins.str] = None,
        metric_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        new_game_session_protection_policy: typing.Optional[builtins.str] = None,
        resource_creation_limit_policy: typing.Optional[typing.Union["GameliftFleetResourceCreationLimitPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        runtime_configuration: typing.Optional[typing.Union["GameliftFleetRuntimeConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        script_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["GameliftFleetTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param ec2_instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#ec2_instance_type GameliftFleet#ec2_instance_type}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#name GameliftFleet#name}.
        :param build_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#build_id GameliftFleet#build_id}.
        :param certificate_configuration: certificate_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#certificate_configuration GameliftFleet#certificate_configuration}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#description GameliftFleet#description}.
        :param ec2_inbound_permission: ec2_inbound_permission block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#ec2_inbound_permission GameliftFleet#ec2_inbound_permission}
        :param fleet_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#fleet_type GameliftFleet#fleet_type}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#id GameliftFleet#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param instance_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#instance_role_arn GameliftFleet#instance_role_arn}.
        :param metric_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#metric_groups GameliftFleet#metric_groups}.
        :param new_game_session_protection_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#new_game_session_protection_policy GameliftFleet#new_game_session_protection_policy}.
        :param resource_creation_limit_policy: resource_creation_limit_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#resource_creation_limit_policy GameliftFleet#resource_creation_limit_policy}
        :param runtime_configuration: runtime_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#runtime_configuration GameliftFleet#runtime_configuration}
        :param script_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#script_id GameliftFleet#script_id}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#tags GameliftFleet#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#tags_all GameliftFleet#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#timeouts GameliftFleet#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(certificate_configuration, dict):
            certificate_configuration = GameliftFleetCertificateConfiguration(**certificate_configuration)
        if isinstance(resource_creation_limit_policy, dict):
            resource_creation_limit_policy = GameliftFleetResourceCreationLimitPolicy(**resource_creation_limit_policy)
        if isinstance(runtime_configuration, dict):
            runtime_configuration = GameliftFleetRuntimeConfiguration(**runtime_configuration)
        if isinstance(timeouts, dict):
            timeouts = GameliftFleetTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__495418a229ad9392b66955ebf180d5651742911d199618157701ef8f5546b547)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument ec2_instance_type", value=ec2_instance_type, expected_type=type_hints["ec2_instance_type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument build_id", value=build_id, expected_type=type_hints["build_id"])
            check_type(argname="argument certificate_configuration", value=certificate_configuration, expected_type=type_hints["certificate_configuration"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument ec2_inbound_permission", value=ec2_inbound_permission, expected_type=type_hints["ec2_inbound_permission"])
            check_type(argname="argument fleet_type", value=fleet_type, expected_type=type_hints["fleet_type"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument instance_role_arn", value=instance_role_arn, expected_type=type_hints["instance_role_arn"])
            check_type(argname="argument metric_groups", value=metric_groups, expected_type=type_hints["metric_groups"])
            check_type(argname="argument new_game_session_protection_policy", value=new_game_session_protection_policy, expected_type=type_hints["new_game_session_protection_policy"])
            check_type(argname="argument resource_creation_limit_policy", value=resource_creation_limit_policy, expected_type=type_hints["resource_creation_limit_policy"])
            check_type(argname="argument runtime_configuration", value=runtime_configuration, expected_type=type_hints["runtime_configuration"])
            check_type(argname="argument script_id", value=script_id, expected_type=type_hints["script_id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ec2_instance_type": ec2_instance_type,
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
        if build_id is not None:
            self._values["build_id"] = build_id
        if certificate_configuration is not None:
            self._values["certificate_configuration"] = certificate_configuration
        if description is not None:
            self._values["description"] = description
        if ec2_inbound_permission is not None:
            self._values["ec2_inbound_permission"] = ec2_inbound_permission
        if fleet_type is not None:
            self._values["fleet_type"] = fleet_type
        if id is not None:
            self._values["id"] = id
        if instance_role_arn is not None:
            self._values["instance_role_arn"] = instance_role_arn
        if metric_groups is not None:
            self._values["metric_groups"] = metric_groups
        if new_game_session_protection_policy is not None:
            self._values["new_game_session_protection_policy"] = new_game_session_protection_policy
        if resource_creation_limit_policy is not None:
            self._values["resource_creation_limit_policy"] = resource_creation_limit_policy
        if runtime_configuration is not None:
            self._values["runtime_configuration"] = runtime_configuration
        if script_id is not None:
            self._values["script_id"] = script_id
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
    def ec2_instance_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#ec2_instance_type GameliftFleet#ec2_instance_type}.'''
        result = self._values.get("ec2_instance_type")
        assert result is not None, "Required property 'ec2_instance_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#name GameliftFleet#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def build_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#build_id GameliftFleet#build_id}.'''
        result = self._values.get("build_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate_configuration(
        self,
    ) -> typing.Optional[GameliftFleetCertificateConfiguration]:
        '''certificate_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#certificate_configuration GameliftFleet#certificate_configuration}
        '''
        result = self._values.get("certificate_configuration")
        return typing.cast(typing.Optional[GameliftFleetCertificateConfiguration], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#description GameliftFleet#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ec2_inbound_permission(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GameliftFleetEc2InboundPermission"]]]:
        '''ec2_inbound_permission block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#ec2_inbound_permission GameliftFleet#ec2_inbound_permission}
        '''
        result = self._values.get("ec2_inbound_permission")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GameliftFleetEc2InboundPermission"]]], result)

    @builtins.property
    def fleet_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#fleet_type GameliftFleet#fleet_type}.'''
        result = self._values.get("fleet_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#id GameliftFleet#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#instance_role_arn GameliftFleet#instance_role_arn}.'''
        result = self._values.get("instance_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metric_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#metric_groups GameliftFleet#metric_groups}.'''
        result = self._values.get("metric_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def new_game_session_protection_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#new_game_session_protection_policy GameliftFleet#new_game_session_protection_policy}.'''
        result = self._values.get("new_game_session_protection_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_creation_limit_policy(
        self,
    ) -> typing.Optional["GameliftFleetResourceCreationLimitPolicy"]:
        '''resource_creation_limit_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#resource_creation_limit_policy GameliftFleet#resource_creation_limit_policy}
        '''
        result = self._values.get("resource_creation_limit_policy")
        return typing.cast(typing.Optional["GameliftFleetResourceCreationLimitPolicy"], result)

    @builtins.property
    def runtime_configuration(
        self,
    ) -> typing.Optional["GameliftFleetRuntimeConfiguration"]:
        '''runtime_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#runtime_configuration GameliftFleet#runtime_configuration}
        '''
        result = self._values.get("runtime_configuration")
        return typing.cast(typing.Optional["GameliftFleetRuntimeConfiguration"], result)

    @builtins.property
    def script_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#script_id GameliftFleet#script_id}.'''
        result = self._values.get("script_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#tags GameliftFleet#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#tags_all GameliftFleet#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GameliftFleetTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#timeouts GameliftFleet#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GameliftFleetTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GameliftFleetConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.gameliftFleet.GameliftFleetEc2InboundPermission",
    jsii_struct_bases=[],
    name_mapping={
        "from_port": "fromPort",
        "ip_range": "ipRange",
        "protocol": "protocol",
        "to_port": "toPort",
    },
)
class GameliftFleetEc2InboundPermission:
    def __init__(
        self,
        *,
        from_port: jsii.Number,
        ip_range: builtins.str,
        protocol: builtins.str,
        to_port: jsii.Number,
    ) -> None:
        '''
        :param from_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#from_port GameliftFleet#from_port}.
        :param ip_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#ip_range GameliftFleet#ip_range}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#protocol GameliftFleet#protocol}.
        :param to_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#to_port GameliftFleet#to_port}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5fdf60ea10ea1fb5fdecc0b904e05377ecccbc14132e8db23dbf6a346fc0da2)
            check_type(argname="argument from_port", value=from_port, expected_type=type_hints["from_port"])
            check_type(argname="argument ip_range", value=ip_range, expected_type=type_hints["ip_range"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument to_port", value=to_port, expected_type=type_hints["to_port"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "from_port": from_port,
            "ip_range": ip_range,
            "protocol": protocol,
            "to_port": to_port,
        }

    @builtins.property
    def from_port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#from_port GameliftFleet#from_port}.'''
        result = self._values.get("from_port")
        assert result is not None, "Required property 'from_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def ip_range(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#ip_range GameliftFleet#ip_range}.'''
        result = self._values.get("ip_range")
        assert result is not None, "Required property 'ip_range' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#protocol GameliftFleet#protocol}.'''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def to_port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#to_port GameliftFleet#to_port}.'''
        result = self._values.get("to_port")
        assert result is not None, "Required property 'to_port' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GameliftFleetEc2InboundPermission(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GameliftFleetEc2InboundPermissionList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.gameliftFleet.GameliftFleetEc2InboundPermissionList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__08aef57b403b0cae83dc880159d34b9b423a82de22d61ab739220a4e0338146c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GameliftFleetEc2InboundPermissionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b37adc904cefca6186dbb98f7b93bb48bbfe4697d44b12125296117e63ed58b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GameliftFleetEc2InboundPermissionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9f9ec4d69804885b396421ebcf4552ecc86804675fd59d9042113f5b133b9d4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b80a6d0136dce160ae4befb9dc4d2e473a03c7ea13c4985b6f37c740f8b4d2e7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__65ddeff18d3ac74b9e64c341ed691a9e7db2adcdf1a4e709f9bbe0cdfd5c0d9d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GameliftFleetEc2InboundPermission]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GameliftFleetEc2InboundPermission]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GameliftFleetEc2InboundPermission]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4330bcf3b63c0b7b6d465ff1a45c094364cabe4eee594e7e817af59078f1fbb0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GameliftFleetEc2InboundPermissionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.gameliftFleet.GameliftFleetEc2InboundPermissionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__132934785666369665e0a7a24763b387640cd69b024611c44dba6cb48a50af5b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="fromPortInput")
    def from_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "fromPortInput"))

    @builtins.property
    @jsii.member(jsii_name="ipRangeInput")
    def ip_range_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="toPortInput")
    def to_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "toPortInput"))

    @builtins.property
    @jsii.member(jsii_name="fromPort")
    def from_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "fromPort"))

    @from_port.setter
    def from_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34a042ddb90541056ddaf3ba0c32099cc6c44b0d84fb9cd8cffd8d7ca1495758)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fromPort", value)

    @builtins.property
    @jsii.member(jsii_name="ipRange")
    def ip_range(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipRange"))

    @ip_range.setter
    def ip_range(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aca535242755b20db372a449b6ec4588e03049cea9664d152a960c944d45074c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipRange", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3813cd49cc599b4e10d4f1c73317a4348223b98364a9409664349eabc43fcd1c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="toPort")
    def to_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "toPort"))

    @to_port.setter
    def to_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c96a35d08b8efbcc2e8cf0a5f3474b7ef185dd36330925fe9b50dabb904bcdd4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "toPort", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GameliftFleetEc2InboundPermission, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GameliftFleetEc2InboundPermission, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GameliftFleetEc2InboundPermission, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__972fb47ae9758a4f961f2f7889e4ddc95dfe660dcd43f787386ae98134c745f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.gameliftFleet.GameliftFleetResourceCreationLimitPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "new_game_sessions_per_creator": "newGameSessionsPerCreator",
        "policy_period_in_minutes": "policyPeriodInMinutes",
    },
)
class GameliftFleetResourceCreationLimitPolicy:
    def __init__(
        self,
        *,
        new_game_sessions_per_creator: typing.Optional[jsii.Number] = None,
        policy_period_in_minutes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param new_game_sessions_per_creator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#new_game_sessions_per_creator GameliftFleet#new_game_sessions_per_creator}.
        :param policy_period_in_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#policy_period_in_minutes GameliftFleet#policy_period_in_minutes}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d074027c1b6a8eeb581342d58e069ee1a23f611759cac904743dbd6b401cbe5c)
            check_type(argname="argument new_game_sessions_per_creator", value=new_game_sessions_per_creator, expected_type=type_hints["new_game_sessions_per_creator"])
            check_type(argname="argument policy_period_in_minutes", value=policy_period_in_minutes, expected_type=type_hints["policy_period_in_minutes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if new_game_sessions_per_creator is not None:
            self._values["new_game_sessions_per_creator"] = new_game_sessions_per_creator
        if policy_period_in_minutes is not None:
            self._values["policy_period_in_minutes"] = policy_period_in_minutes

    @builtins.property
    def new_game_sessions_per_creator(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#new_game_sessions_per_creator GameliftFleet#new_game_sessions_per_creator}.'''
        result = self._values.get("new_game_sessions_per_creator")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def policy_period_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#policy_period_in_minutes GameliftFleet#policy_period_in_minutes}.'''
        result = self._values.get("policy_period_in_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GameliftFleetResourceCreationLimitPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GameliftFleetResourceCreationLimitPolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.gameliftFleet.GameliftFleetResourceCreationLimitPolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ce3821e84674b20292125fa1cf5a3c71ce67b6f9bcf6ff5a6108024854c0889e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetNewGameSessionsPerCreator")
    def reset_new_game_sessions_per_creator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNewGameSessionsPerCreator", []))

    @jsii.member(jsii_name="resetPolicyPeriodInMinutes")
    def reset_policy_period_in_minutes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolicyPeriodInMinutes", []))

    @builtins.property
    @jsii.member(jsii_name="newGameSessionsPerCreatorInput")
    def new_game_sessions_per_creator_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "newGameSessionsPerCreatorInput"))

    @builtins.property
    @jsii.member(jsii_name="policyPeriodInMinutesInput")
    def policy_period_in_minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "policyPeriodInMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="newGameSessionsPerCreator")
    def new_game_sessions_per_creator(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "newGameSessionsPerCreator"))

    @new_game_sessions_per_creator.setter
    def new_game_sessions_per_creator(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1004126c91c47e5317cc0b7d8441d7be4cc4cf01dee738b136182cc33c7a1120)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "newGameSessionsPerCreator", value)

    @builtins.property
    @jsii.member(jsii_name="policyPeriodInMinutes")
    def policy_period_in_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "policyPeriodInMinutes"))

    @policy_period_in_minutes.setter
    def policy_period_in_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b610c9272f15b7903ccd8023dc963f9383bdd50155534d710d5572490bcfb13)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyPeriodInMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GameliftFleetResourceCreationLimitPolicy]:
        return typing.cast(typing.Optional[GameliftFleetResourceCreationLimitPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GameliftFleetResourceCreationLimitPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__641055c79acfb3a918963847e4a33390d7401b43e751a7506e9eb8b0db0e349b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.gameliftFleet.GameliftFleetRuntimeConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "game_session_activation_timeout_seconds": "gameSessionActivationTimeoutSeconds",
        "max_concurrent_game_session_activations": "maxConcurrentGameSessionActivations",
        "server_process": "serverProcess",
    },
)
class GameliftFleetRuntimeConfiguration:
    def __init__(
        self,
        *,
        game_session_activation_timeout_seconds: typing.Optional[jsii.Number] = None,
        max_concurrent_game_session_activations: typing.Optional[jsii.Number] = None,
        server_process: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GameliftFleetRuntimeConfigurationServerProcess", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param game_session_activation_timeout_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#game_session_activation_timeout_seconds GameliftFleet#game_session_activation_timeout_seconds}.
        :param max_concurrent_game_session_activations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#max_concurrent_game_session_activations GameliftFleet#max_concurrent_game_session_activations}.
        :param server_process: server_process block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#server_process GameliftFleet#server_process}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8d1249411305375720187bb0ff37985936b40249c7ff18abc42ecd7042d5b59)
            check_type(argname="argument game_session_activation_timeout_seconds", value=game_session_activation_timeout_seconds, expected_type=type_hints["game_session_activation_timeout_seconds"])
            check_type(argname="argument max_concurrent_game_session_activations", value=max_concurrent_game_session_activations, expected_type=type_hints["max_concurrent_game_session_activations"])
            check_type(argname="argument server_process", value=server_process, expected_type=type_hints["server_process"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if game_session_activation_timeout_seconds is not None:
            self._values["game_session_activation_timeout_seconds"] = game_session_activation_timeout_seconds
        if max_concurrent_game_session_activations is not None:
            self._values["max_concurrent_game_session_activations"] = max_concurrent_game_session_activations
        if server_process is not None:
            self._values["server_process"] = server_process

    @builtins.property
    def game_session_activation_timeout_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#game_session_activation_timeout_seconds GameliftFleet#game_session_activation_timeout_seconds}.'''
        result = self._values.get("game_session_activation_timeout_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_concurrent_game_session_activations(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#max_concurrent_game_session_activations GameliftFleet#max_concurrent_game_session_activations}.'''
        result = self._values.get("max_concurrent_game_session_activations")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def server_process(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GameliftFleetRuntimeConfigurationServerProcess"]]]:
        '''server_process block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#server_process GameliftFleet#server_process}
        '''
        result = self._values.get("server_process")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GameliftFleetRuntimeConfigurationServerProcess"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GameliftFleetRuntimeConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GameliftFleetRuntimeConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.gameliftFleet.GameliftFleetRuntimeConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d43fc819727500ca72368483f98401615c880e782b7415b4a1d8c78cda818ae9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putServerProcess")
    def put_server_process(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GameliftFleetRuntimeConfigurationServerProcess", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2b8f668e4903cbe7139a05254865b9ced4f3703061c2144167ac0a163d3acce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putServerProcess", [value]))

    @jsii.member(jsii_name="resetGameSessionActivationTimeoutSeconds")
    def reset_game_session_activation_timeout_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGameSessionActivationTimeoutSeconds", []))

    @jsii.member(jsii_name="resetMaxConcurrentGameSessionActivations")
    def reset_max_concurrent_game_session_activations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxConcurrentGameSessionActivations", []))

    @jsii.member(jsii_name="resetServerProcess")
    def reset_server_process(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerProcess", []))

    @builtins.property
    @jsii.member(jsii_name="serverProcess")
    def server_process(self) -> "GameliftFleetRuntimeConfigurationServerProcessList":
        return typing.cast("GameliftFleetRuntimeConfigurationServerProcessList", jsii.get(self, "serverProcess"))

    @builtins.property
    @jsii.member(jsii_name="gameSessionActivationTimeoutSecondsInput")
    def game_session_activation_timeout_seconds_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "gameSessionActivationTimeoutSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxConcurrentGameSessionActivationsInput")
    def max_concurrent_game_session_activations_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxConcurrentGameSessionActivationsInput"))

    @builtins.property
    @jsii.member(jsii_name="serverProcessInput")
    def server_process_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GameliftFleetRuntimeConfigurationServerProcess"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GameliftFleetRuntimeConfigurationServerProcess"]]], jsii.get(self, "serverProcessInput"))

    @builtins.property
    @jsii.member(jsii_name="gameSessionActivationTimeoutSeconds")
    def game_session_activation_timeout_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "gameSessionActivationTimeoutSeconds"))

    @game_session_activation_timeout_seconds.setter
    def game_session_activation_timeout_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68795e0a2133deaf5ab02c7887f38e17fc30504069db68ca461fd54da31f3788)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gameSessionActivationTimeoutSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="maxConcurrentGameSessionActivations")
    def max_concurrent_game_session_activations(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConcurrentGameSessionActivations"))

    @max_concurrent_game_session_activations.setter
    def max_concurrent_game_session_activations(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85f401b65b0c283298f983aac696ee4ac3d8b9777ed4775b71fd1b92c681a17c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConcurrentGameSessionActivations", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GameliftFleetRuntimeConfiguration]:
        return typing.cast(typing.Optional[GameliftFleetRuntimeConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GameliftFleetRuntimeConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a0d04f492875bbe9bb8551c2b7427e86fabd5bb1c732ffdbc604ebbf34860d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.gameliftFleet.GameliftFleetRuntimeConfigurationServerProcess",
    jsii_struct_bases=[],
    name_mapping={
        "concurrent_executions": "concurrentExecutions",
        "launch_path": "launchPath",
        "parameters": "parameters",
    },
)
class GameliftFleetRuntimeConfigurationServerProcess:
    def __init__(
        self,
        *,
        concurrent_executions: jsii.Number,
        launch_path: builtins.str,
        parameters: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param concurrent_executions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#concurrent_executions GameliftFleet#concurrent_executions}.
        :param launch_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#launch_path GameliftFleet#launch_path}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#parameters GameliftFleet#parameters}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28f2a0789813f9da55c9a5ee0d2e04ea1e79fda8722f77143dad2c71c5c6855f)
            check_type(argname="argument concurrent_executions", value=concurrent_executions, expected_type=type_hints["concurrent_executions"])
            check_type(argname="argument launch_path", value=launch_path, expected_type=type_hints["launch_path"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "concurrent_executions": concurrent_executions,
            "launch_path": launch_path,
        }
        if parameters is not None:
            self._values["parameters"] = parameters

    @builtins.property
    def concurrent_executions(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#concurrent_executions GameliftFleet#concurrent_executions}.'''
        result = self._values.get("concurrent_executions")
        assert result is not None, "Required property 'concurrent_executions' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def launch_path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#launch_path GameliftFleet#launch_path}.'''
        result = self._values.get("launch_path")
        assert result is not None, "Required property 'launch_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameters(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#parameters GameliftFleet#parameters}.'''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GameliftFleetRuntimeConfigurationServerProcess(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GameliftFleetRuntimeConfigurationServerProcessList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.gameliftFleet.GameliftFleetRuntimeConfigurationServerProcessList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__760cd78e7a15bfc924088e5cf59e1117571e772de6d7dc178100cd9cdc815b4a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GameliftFleetRuntimeConfigurationServerProcessOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12b65c6ef082b9a549a9dc27470f8233f000c00e9d686577409df48131672ab5)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GameliftFleetRuntimeConfigurationServerProcessOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35e8193ca1df5ca657f979043201ca19d46c833ab03a1798787662d709492acd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__eefafdd132d24bdc360d816f329a96811779fa67753693ac83daec06d703f512)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d26100070b3d176bbf925042540c89652bb0e54392fa22d376591f7fb3f3fbf1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GameliftFleetRuntimeConfigurationServerProcess]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GameliftFleetRuntimeConfigurationServerProcess]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GameliftFleetRuntimeConfigurationServerProcess]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e4962a692d3f270b819ca2bb682522468ac620e73c3206c92267de24216e155)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GameliftFleetRuntimeConfigurationServerProcessOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.gameliftFleet.GameliftFleetRuntimeConfigurationServerProcessOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__73a34ea90f7af921acabf99ac0aeacdefe0c4ccd9c73f15437cb17dff267bb42)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetParameters")
    def reset_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameters", []))

    @builtins.property
    @jsii.member(jsii_name="concurrentExecutionsInput")
    def concurrent_executions_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "concurrentExecutionsInput"))

    @builtins.property
    @jsii.member(jsii_name="launchPathInput")
    def launch_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "launchPathInput"))

    @builtins.property
    @jsii.member(jsii_name="parametersInput")
    def parameters_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parametersInput"))

    @builtins.property
    @jsii.member(jsii_name="concurrentExecutions")
    def concurrent_executions(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "concurrentExecutions"))

    @concurrent_executions.setter
    def concurrent_executions(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56a41f95ba050b4345ba99c3bd07ee287c41191353c664361086ff51d0af5604)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "concurrentExecutions", value)

    @builtins.property
    @jsii.member(jsii_name="launchPath")
    def launch_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "launchPath"))

    @launch_path.setter
    def launch_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67930efa99fb3a95a90c2c6d5b27da4f26fc88e5ae186d16dc69614c934e12c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "launchPath", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a67754e3adeb28813abca8828df3fc425dcfb655887576ad58d3f1b2ab0f61d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GameliftFleetRuntimeConfigurationServerProcess, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GameliftFleetRuntimeConfigurationServerProcess, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GameliftFleetRuntimeConfigurationServerProcess, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dcc5351f082ec28c2cdb1848f59e4635c002b962f33435466e50284a7e548413)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.gameliftFleet.GameliftFleetTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete"},
)
class GameliftFleetTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#create GameliftFleet#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#delete GameliftFleet#delete}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a115f970cd3482b8389bceaa3cb808254a108a028b1a7bad9dc6f95b5324428d)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#create GameliftFleet#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/gamelift_fleet#delete GameliftFleet#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GameliftFleetTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GameliftFleetTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.gameliftFleet.GameliftFleetTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__93b5feeb806f4cf8d93199ea8b26b77006c39b96ca86a80f74a5a8ccf3f5deb2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2b9b5a37b78f052b78e9e43ad34376d985844d703d118e3c772b715e05a3b7f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a135b79a15893f06351fab10249ce0d7569157bf0b341bfd452e9d9c34e1340)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GameliftFleetTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GameliftFleetTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GameliftFleetTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b27efbd2bc7e4e4b36ff29f9c073af6be97b417a1f49f412acaa9bd6c1d8d15e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GameliftFleet",
    "GameliftFleetCertificateConfiguration",
    "GameliftFleetCertificateConfigurationOutputReference",
    "GameliftFleetConfig",
    "GameliftFleetEc2InboundPermission",
    "GameliftFleetEc2InboundPermissionList",
    "GameliftFleetEc2InboundPermissionOutputReference",
    "GameliftFleetResourceCreationLimitPolicy",
    "GameliftFleetResourceCreationLimitPolicyOutputReference",
    "GameliftFleetRuntimeConfiguration",
    "GameliftFleetRuntimeConfigurationOutputReference",
    "GameliftFleetRuntimeConfigurationServerProcess",
    "GameliftFleetRuntimeConfigurationServerProcessList",
    "GameliftFleetRuntimeConfigurationServerProcessOutputReference",
    "GameliftFleetTimeouts",
    "GameliftFleetTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__9218537b24144f4b1ed63b215e1d9ccf2449b90ba6fc6f0ebe0d93ac19cdf14d(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    ec2_instance_type: builtins.str,
    name: builtins.str,
    build_id: typing.Optional[builtins.str] = None,
    certificate_configuration: typing.Optional[typing.Union[GameliftFleetCertificateConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    description: typing.Optional[builtins.str] = None,
    ec2_inbound_permission: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GameliftFleetEc2InboundPermission, typing.Dict[builtins.str, typing.Any]]]]] = None,
    fleet_type: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    instance_role_arn: typing.Optional[builtins.str] = None,
    metric_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    new_game_session_protection_policy: typing.Optional[builtins.str] = None,
    resource_creation_limit_policy: typing.Optional[typing.Union[GameliftFleetResourceCreationLimitPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    runtime_configuration: typing.Optional[typing.Union[GameliftFleetRuntimeConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    script_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[GameliftFleetTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__460fe5a94b38e70af0811ca036ca84ac2b72fa5e80a1a2a1df5abe9f8644e44a(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GameliftFleetEc2InboundPermission, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d381917c5bf0fd9ca804e46d3820d8ecd707e8860e161711d216eef7f7fe29f6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70177906d204e7dc5407c2d921278904715f04cdbb7381a706560ecffd802c4c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb45ffa5b0b0cf04ffc7e866dd2c7b3d65a4d26af6b87ad9614f6c522ecb7b9d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__571c245e42e133c7c67e0f18901b5c520c85d5933462f3538789a9952165370c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dac77df9c21b038513881143e755b08e11af3aee9cd8bb1d1e2635353a7558c3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f57338f0aa2f93e263b56b37d7b3c8b5a3d1ba234b7c66b1afa9b2068314f50(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60e9b042f130ce706123b11bad5a2c9414eecf9891c083cde1e24a6b43cb3b66(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65e061e84f15c900361832d0deb3230b4433c7121811f987a5ec92bf7fa6230c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__911a743f4f66796815869a8b25aeb310bf621a39704fc5d957b185373c9398a3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eaf0568c0e35f2fd027f02f366e62e526bb6c122e1d5201ac9a14c3130cdd13c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9528ffcd8e4933e77de0755f946590d887a317e67aa85d655ccdcc832583e635(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33aad221784d20bb5398a1951018f5bdc39ac22bd041d8879361c68e0838f30a(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c22591cedb3f7621ffe3660deb9f3976f75e5c0529b58660215bc5fe54521bb(
    *,
    certificate_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf18a08af1cc67f964e34479066d95f29e3700749dc8777faf6269704d3d36ba(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4b0c70cedf98b7c61344e544d83834c374069a828b0c4cdc4802507147c3637(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b12c9e43c930ad021af3c299a84004effaab0fbab5fc26f1c7523a0140a0faf6(
    value: typing.Optional[GameliftFleetCertificateConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__495418a229ad9392b66955ebf180d5651742911d199618157701ef8f5546b547(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ec2_instance_type: builtins.str,
    name: builtins.str,
    build_id: typing.Optional[builtins.str] = None,
    certificate_configuration: typing.Optional[typing.Union[GameliftFleetCertificateConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    description: typing.Optional[builtins.str] = None,
    ec2_inbound_permission: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GameliftFleetEc2InboundPermission, typing.Dict[builtins.str, typing.Any]]]]] = None,
    fleet_type: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    instance_role_arn: typing.Optional[builtins.str] = None,
    metric_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    new_game_session_protection_policy: typing.Optional[builtins.str] = None,
    resource_creation_limit_policy: typing.Optional[typing.Union[GameliftFleetResourceCreationLimitPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    runtime_configuration: typing.Optional[typing.Union[GameliftFleetRuntimeConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    script_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[GameliftFleetTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5fdf60ea10ea1fb5fdecc0b904e05377ecccbc14132e8db23dbf6a346fc0da2(
    *,
    from_port: jsii.Number,
    ip_range: builtins.str,
    protocol: builtins.str,
    to_port: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08aef57b403b0cae83dc880159d34b9b423a82de22d61ab739220a4e0338146c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b37adc904cefca6186dbb98f7b93bb48bbfe4697d44b12125296117e63ed58b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9f9ec4d69804885b396421ebcf4552ecc86804675fd59d9042113f5b133b9d4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b80a6d0136dce160ae4befb9dc4d2e473a03c7ea13c4985b6f37c740f8b4d2e7(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65ddeff18d3ac74b9e64c341ed691a9e7db2adcdf1a4e709f9bbe0cdfd5c0d9d(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4330bcf3b63c0b7b6d465ff1a45c094364cabe4eee594e7e817af59078f1fbb0(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GameliftFleetEc2InboundPermission]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__132934785666369665e0a7a24763b387640cd69b024611c44dba6cb48a50af5b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34a042ddb90541056ddaf3ba0c32099cc6c44b0d84fb9cd8cffd8d7ca1495758(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aca535242755b20db372a449b6ec4588e03049cea9664d152a960c944d45074c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3813cd49cc599b4e10d4f1c73317a4348223b98364a9409664349eabc43fcd1c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c96a35d08b8efbcc2e8cf0a5f3474b7ef185dd36330925fe9b50dabb904bcdd4(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__972fb47ae9758a4f961f2f7889e4ddc95dfe660dcd43f787386ae98134c745f1(
    value: typing.Optional[typing.Union[GameliftFleetEc2InboundPermission, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d074027c1b6a8eeb581342d58e069ee1a23f611759cac904743dbd6b401cbe5c(
    *,
    new_game_sessions_per_creator: typing.Optional[jsii.Number] = None,
    policy_period_in_minutes: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce3821e84674b20292125fa1cf5a3c71ce67b6f9bcf6ff5a6108024854c0889e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1004126c91c47e5317cc0b7d8441d7be4cc4cf01dee738b136182cc33c7a1120(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b610c9272f15b7903ccd8023dc963f9383bdd50155534d710d5572490bcfb13(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__641055c79acfb3a918963847e4a33390d7401b43e751a7506e9eb8b0db0e349b(
    value: typing.Optional[GameliftFleetResourceCreationLimitPolicy],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8d1249411305375720187bb0ff37985936b40249c7ff18abc42ecd7042d5b59(
    *,
    game_session_activation_timeout_seconds: typing.Optional[jsii.Number] = None,
    max_concurrent_game_session_activations: typing.Optional[jsii.Number] = None,
    server_process: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GameliftFleetRuntimeConfigurationServerProcess, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d43fc819727500ca72368483f98401615c880e782b7415b4a1d8c78cda818ae9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2b8f668e4903cbe7139a05254865b9ced4f3703061c2144167ac0a163d3acce(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GameliftFleetRuntimeConfigurationServerProcess, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68795e0a2133deaf5ab02c7887f38e17fc30504069db68ca461fd54da31f3788(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85f401b65b0c283298f983aac696ee4ac3d8b9777ed4775b71fd1b92c681a17c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a0d04f492875bbe9bb8551c2b7427e86fabd5bb1c732ffdbc604ebbf34860d8(
    value: typing.Optional[GameliftFleetRuntimeConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28f2a0789813f9da55c9a5ee0d2e04ea1e79fda8722f77143dad2c71c5c6855f(
    *,
    concurrent_executions: jsii.Number,
    launch_path: builtins.str,
    parameters: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__760cd78e7a15bfc924088e5cf59e1117571e772de6d7dc178100cd9cdc815b4a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12b65c6ef082b9a549a9dc27470f8233f000c00e9d686577409df48131672ab5(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35e8193ca1df5ca657f979043201ca19d46c833ab03a1798787662d709492acd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eefafdd132d24bdc360d816f329a96811779fa67753693ac83daec06d703f512(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d26100070b3d176bbf925042540c89652bb0e54392fa22d376591f7fb3f3fbf1(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e4962a692d3f270b819ca2bb682522468ac620e73c3206c92267de24216e155(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GameliftFleetRuntimeConfigurationServerProcess]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73a34ea90f7af921acabf99ac0aeacdefe0c4ccd9c73f15437cb17dff267bb42(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56a41f95ba050b4345ba99c3bd07ee287c41191353c664361086ff51d0af5604(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67930efa99fb3a95a90c2c6d5b27da4f26fc88e5ae186d16dc69614c934e12c4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a67754e3adeb28813abca8828df3fc425dcfb655887576ad58d3f1b2ab0f61d6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcc5351f082ec28c2cdb1848f59e4635c002b962f33435466e50284a7e548413(
    value: typing.Optional[typing.Union[GameliftFleetRuntimeConfigurationServerProcess, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a115f970cd3482b8389bceaa3cb808254a108a028b1a7bad9dc6f95b5324428d(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93b5feeb806f4cf8d93199ea8b26b77006c39b96ca86a80f74a5a8ccf3f5deb2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b9b5a37b78f052b78e9e43ad34376d985844d703d118e3c772b715e05a3b7f3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a135b79a15893f06351fab10249ce0d7569157bf0b341bfd452e9d9c34e1340(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b27efbd2bc7e4e4b36ff29f9c073af6be97b417a1f49f412acaa9bd6c1d8d15e(
    value: typing.Optional[typing.Union[GameliftFleetTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
