'''
# `aws_codebuild_project`

Refer to the Terraform Registory for docs: [`aws_codebuild_project`](https://www.terraform.io/docs/providers/aws/r/codebuild_project).
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


class CodebuildProject(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codebuildProject.CodebuildProject",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project aws_codebuild_project}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        artifacts: typing.Union["CodebuildProjectArtifacts", typing.Dict[builtins.str, typing.Any]],
        environment: typing.Union["CodebuildProjectEnvironment", typing.Dict[builtins.str, typing.Any]],
        name: builtins.str,
        service_role: builtins.str,
        source: typing.Union["CodebuildProjectSource", typing.Dict[builtins.str, typing.Any]],
        badge_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        build_batch_config: typing.Optional[typing.Union["CodebuildProjectBuildBatchConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        build_timeout: typing.Optional[jsii.Number] = None,
        cache: typing.Optional[typing.Union["CodebuildProjectCache", typing.Dict[builtins.str, typing.Any]]] = None,
        concurrent_build_limit: typing.Optional[jsii.Number] = None,
        description: typing.Optional[builtins.str] = None,
        encryption_key: typing.Optional[builtins.str] = None,
        file_system_locations: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CodebuildProjectFileSystemLocations", typing.Dict[builtins.str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        logs_config: typing.Optional[typing.Union["CodebuildProjectLogsConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        project_visibility: typing.Optional[builtins.str] = None,
        queued_timeout: typing.Optional[jsii.Number] = None,
        resource_access_role: typing.Optional[builtins.str] = None,
        secondary_artifacts: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CodebuildProjectSecondaryArtifacts", typing.Dict[builtins.str, typing.Any]]]]] = None,
        secondary_sources: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CodebuildProjectSecondarySources", typing.Dict[builtins.str, typing.Any]]]]] = None,
        secondary_source_version: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CodebuildProjectSecondarySourceVersion", typing.Dict[builtins.str, typing.Any]]]]] = None,
        source_version: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        vpc_config: typing.Optional[typing.Union["CodebuildProjectVpcConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project aws_codebuild_project} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param artifacts: artifacts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#artifacts CodebuildProject#artifacts}
        :param environment: environment block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#environment CodebuildProject#environment}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#name CodebuildProject#name}.
        :param service_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#service_role CodebuildProject#service_role}.
        :param source: source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#source CodebuildProject#source}
        :param badge_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#badge_enabled CodebuildProject#badge_enabled}.
        :param build_batch_config: build_batch_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#build_batch_config CodebuildProject#build_batch_config}
        :param build_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#build_timeout CodebuildProject#build_timeout}.
        :param cache: cache block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#cache CodebuildProject#cache}
        :param concurrent_build_limit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#concurrent_build_limit CodebuildProject#concurrent_build_limit}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#description CodebuildProject#description}.
        :param encryption_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#encryption_key CodebuildProject#encryption_key}.
        :param file_system_locations: file_system_locations block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#file_system_locations CodebuildProject#file_system_locations}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#id CodebuildProject#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param logs_config: logs_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#logs_config CodebuildProject#logs_config}
        :param project_visibility: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#project_visibility CodebuildProject#project_visibility}.
        :param queued_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#queued_timeout CodebuildProject#queued_timeout}.
        :param resource_access_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#resource_access_role CodebuildProject#resource_access_role}.
        :param secondary_artifacts: secondary_artifacts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#secondary_artifacts CodebuildProject#secondary_artifacts}
        :param secondary_sources: secondary_sources block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#secondary_sources CodebuildProject#secondary_sources}
        :param secondary_source_version: secondary_source_version block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#secondary_source_version CodebuildProject#secondary_source_version}
        :param source_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#source_version CodebuildProject#source_version}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#tags CodebuildProject#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#tags_all CodebuildProject#tags_all}.
        :param vpc_config: vpc_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#vpc_config CodebuildProject#vpc_config}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea7c392ec6ab016a0e106974108b385089bec193544a66c53dd8dca25e031262)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CodebuildProjectConfig(
            artifacts=artifacts,
            environment=environment,
            name=name,
            service_role=service_role,
            source=source,
            badge_enabled=badge_enabled,
            build_batch_config=build_batch_config,
            build_timeout=build_timeout,
            cache=cache,
            concurrent_build_limit=concurrent_build_limit,
            description=description,
            encryption_key=encryption_key,
            file_system_locations=file_system_locations,
            id=id,
            logs_config=logs_config,
            project_visibility=project_visibility,
            queued_timeout=queued_timeout,
            resource_access_role=resource_access_role,
            secondary_artifacts=secondary_artifacts,
            secondary_sources=secondary_sources,
            secondary_source_version=secondary_source_version,
            source_version=source_version,
            tags=tags,
            tags_all=tags_all,
            vpc_config=vpc_config,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putArtifacts")
    def put_artifacts(
        self,
        *,
        type: builtins.str,
        artifact_identifier: typing.Optional[builtins.str] = None,
        bucket_owner_access: typing.Optional[builtins.str] = None,
        encryption_disabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        location: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        namespace_type: typing.Optional[builtins.str] = None,
        override_artifact_name: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        packaging: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.
        :param artifact_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#artifact_identifier CodebuildProject#artifact_identifier}.
        :param bucket_owner_access: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#bucket_owner_access CodebuildProject#bucket_owner_access}.
        :param encryption_disabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#encryption_disabled CodebuildProject#encryption_disabled}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#location CodebuildProject#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#name CodebuildProject#name}.
        :param namespace_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#namespace_type CodebuildProject#namespace_type}.
        :param override_artifact_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#override_artifact_name CodebuildProject#override_artifact_name}.
        :param packaging: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#packaging CodebuildProject#packaging}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#path CodebuildProject#path}.
        '''
        value = CodebuildProjectArtifacts(
            type=type,
            artifact_identifier=artifact_identifier,
            bucket_owner_access=bucket_owner_access,
            encryption_disabled=encryption_disabled,
            location=location,
            name=name,
            namespace_type=namespace_type,
            override_artifact_name=override_artifact_name,
            packaging=packaging,
            path=path,
        )

        return typing.cast(None, jsii.invoke(self, "putArtifacts", [value]))

    @jsii.member(jsii_name="putBuildBatchConfig")
    def put_build_batch_config(
        self,
        *,
        service_role: builtins.str,
        combine_artifacts: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        restrictions: typing.Optional[typing.Union["CodebuildProjectBuildBatchConfigRestrictions", typing.Dict[builtins.str, typing.Any]]] = None,
        timeout_in_mins: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param service_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#service_role CodebuildProject#service_role}.
        :param combine_artifacts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#combine_artifacts CodebuildProject#combine_artifacts}.
        :param restrictions: restrictions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#restrictions CodebuildProject#restrictions}
        :param timeout_in_mins: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#timeout_in_mins CodebuildProject#timeout_in_mins}.
        '''
        value = CodebuildProjectBuildBatchConfig(
            service_role=service_role,
            combine_artifacts=combine_artifacts,
            restrictions=restrictions,
            timeout_in_mins=timeout_in_mins,
        )

        return typing.cast(None, jsii.invoke(self, "putBuildBatchConfig", [value]))

    @jsii.member(jsii_name="putCache")
    def put_cache(
        self,
        *,
        location: typing.Optional[builtins.str] = None,
        modes: typing.Optional[typing.Sequence[builtins.str]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#location CodebuildProject#location}.
        :param modes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#modes CodebuildProject#modes}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.
        '''
        value = CodebuildProjectCache(location=location, modes=modes, type=type)

        return typing.cast(None, jsii.invoke(self, "putCache", [value]))

    @jsii.member(jsii_name="putEnvironment")
    def put_environment(
        self,
        *,
        compute_type: builtins.str,
        image: builtins.str,
        type: builtins.str,
        certificate: typing.Optional[builtins.str] = None,
        environment_variable: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CodebuildProjectEnvironmentEnvironmentVariable", typing.Dict[builtins.str, typing.Any]]]]] = None,
        image_pull_credentials_type: typing.Optional[builtins.str] = None,
        privileged_mode: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        registry_credential: typing.Optional[typing.Union["CodebuildProjectEnvironmentRegistryCredential", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param compute_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#compute_type CodebuildProject#compute_type}.
        :param image: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#image CodebuildProject#image}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.
        :param certificate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#certificate CodebuildProject#certificate}.
        :param environment_variable: environment_variable block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#environment_variable CodebuildProject#environment_variable}
        :param image_pull_credentials_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#image_pull_credentials_type CodebuildProject#image_pull_credentials_type}.
        :param privileged_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#privileged_mode CodebuildProject#privileged_mode}.
        :param registry_credential: registry_credential block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#registry_credential CodebuildProject#registry_credential}
        '''
        value = CodebuildProjectEnvironment(
            compute_type=compute_type,
            image=image,
            type=type,
            certificate=certificate,
            environment_variable=environment_variable,
            image_pull_credentials_type=image_pull_credentials_type,
            privileged_mode=privileged_mode,
            registry_credential=registry_credential,
        )

        return typing.cast(None, jsii.invoke(self, "putEnvironment", [value]))

    @jsii.member(jsii_name="putFileSystemLocations")
    def put_file_system_locations(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CodebuildProjectFileSystemLocations", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20e452d4d56bb053f946eb3baed1cdc0a84c744cbb88289c7d6369d6de1937f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFileSystemLocations", [value]))

    @jsii.member(jsii_name="putLogsConfig")
    def put_logs_config(
        self,
        *,
        cloudwatch_logs: typing.Optional[typing.Union["CodebuildProjectLogsConfigCloudwatchLogs", typing.Dict[builtins.str, typing.Any]]] = None,
        s3_logs: typing.Optional[typing.Union["CodebuildProjectLogsConfigS3Logs", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cloudwatch_logs: cloudwatch_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#cloudwatch_logs CodebuildProject#cloudwatch_logs}
        :param s3_logs: s3_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#s3_logs CodebuildProject#s3_logs}
        '''
        value = CodebuildProjectLogsConfig(
            cloudwatch_logs=cloudwatch_logs, s3_logs=s3_logs
        )

        return typing.cast(None, jsii.invoke(self, "putLogsConfig", [value]))

    @jsii.member(jsii_name="putSecondaryArtifacts")
    def put_secondary_artifacts(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CodebuildProjectSecondaryArtifacts", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db263907270d09cc1afee2830c08f60e6f3b373af011122571779badbf39f688)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSecondaryArtifacts", [value]))

    @jsii.member(jsii_name="putSecondarySources")
    def put_secondary_sources(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CodebuildProjectSecondarySources", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7febe70bed1853e746bf43493a7821c715fdfd0bcfc8ab7fdcc789940b704889)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSecondarySources", [value]))

    @jsii.member(jsii_name="putSecondarySourceVersion")
    def put_secondary_source_version(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CodebuildProjectSecondarySourceVersion", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b06522bcb8b0f2269969f718c5e4a9dff964ec42c6b9c12ac2ae7817e9b6c7ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSecondarySourceVersion", [value]))

    @jsii.member(jsii_name="putSource")
    def put_source(
        self,
        *,
        type: builtins.str,
        auth: typing.Optional[typing.Union["CodebuildProjectSourceAuth", typing.Dict[builtins.str, typing.Any]]] = None,
        buildspec: typing.Optional[builtins.str] = None,
        build_status_config: typing.Optional[typing.Union["CodebuildProjectSourceBuildStatusConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        git_clone_depth: typing.Optional[jsii.Number] = None,
        git_submodules_config: typing.Optional[typing.Union["CodebuildProjectSourceGitSubmodulesConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        insecure_ssl: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        location: typing.Optional[builtins.str] = None,
        report_build_status: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.
        :param auth: auth block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#auth CodebuildProject#auth}
        :param buildspec: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#buildspec CodebuildProject#buildspec}.
        :param build_status_config: build_status_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#build_status_config CodebuildProject#build_status_config}
        :param git_clone_depth: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#git_clone_depth CodebuildProject#git_clone_depth}.
        :param git_submodules_config: git_submodules_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#git_submodules_config CodebuildProject#git_submodules_config}
        :param insecure_ssl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#insecure_ssl CodebuildProject#insecure_ssl}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#location CodebuildProject#location}.
        :param report_build_status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#report_build_status CodebuildProject#report_build_status}.
        '''
        value = CodebuildProjectSource(
            type=type,
            auth=auth,
            buildspec=buildspec,
            build_status_config=build_status_config,
            git_clone_depth=git_clone_depth,
            git_submodules_config=git_submodules_config,
            insecure_ssl=insecure_ssl,
            location=location,
            report_build_status=report_build_status,
        )

        return typing.cast(None, jsii.invoke(self, "putSource", [value]))

    @jsii.member(jsii_name="putVpcConfig")
    def put_vpc_config(
        self,
        *,
        security_group_ids: typing.Sequence[builtins.str],
        subnets: typing.Sequence[builtins.str],
        vpc_id: builtins.str,
    ) -> None:
        '''
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#security_group_ids CodebuildProject#security_group_ids}.
        :param subnets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#subnets CodebuildProject#subnets}.
        :param vpc_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#vpc_id CodebuildProject#vpc_id}.
        '''
        value = CodebuildProjectVpcConfig(
            security_group_ids=security_group_ids, subnets=subnets, vpc_id=vpc_id
        )

        return typing.cast(None, jsii.invoke(self, "putVpcConfig", [value]))

    @jsii.member(jsii_name="resetBadgeEnabled")
    def reset_badge_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBadgeEnabled", []))

    @jsii.member(jsii_name="resetBuildBatchConfig")
    def reset_build_batch_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBuildBatchConfig", []))

    @jsii.member(jsii_name="resetBuildTimeout")
    def reset_build_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBuildTimeout", []))

    @jsii.member(jsii_name="resetCache")
    def reset_cache(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCache", []))

    @jsii.member(jsii_name="resetConcurrentBuildLimit")
    def reset_concurrent_build_limit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConcurrentBuildLimit", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetEncryptionKey")
    def reset_encryption_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionKey", []))

    @jsii.member(jsii_name="resetFileSystemLocations")
    def reset_file_system_locations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileSystemLocations", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLogsConfig")
    def reset_logs_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogsConfig", []))

    @jsii.member(jsii_name="resetProjectVisibility")
    def reset_project_visibility(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProjectVisibility", []))

    @jsii.member(jsii_name="resetQueuedTimeout")
    def reset_queued_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueuedTimeout", []))

    @jsii.member(jsii_name="resetResourceAccessRole")
    def reset_resource_access_role(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceAccessRole", []))

    @jsii.member(jsii_name="resetSecondaryArtifacts")
    def reset_secondary_artifacts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecondaryArtifacts", []))

    @jsii.member(jsii_name="resetSecondarySources")
    def reset_secondary_sources(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecondarySources", []))

    @jsii.member(jsii_name="resetSecondarySourceVersion")
    def reset_secondary_source_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecondarySourceVersion", []))

    @jsii.member(jsii_name="resetSourceVersion")
    def reset_source_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceVersion", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetVpcConfig")
    def reset_vpc_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpcConfig", []))

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
    @jsii.member(jsii_name="artifacts")
    def artifacts(self) -> "CodebuildProjectArtifactsOutputReference":
        return typing.cast("CodebuildProjectArtifactsOutputReference", jsii.get(self, "artifacts"))

    @builtins.property
    @jsii.member(jsii_name="badgeUrl")
    def badge_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "badgeUrl"))

    @builtins.property
    @jsii.member(jsii_name="buildBatchConfig")
    def build_batch_config(self) -> "CodebuildProjectBuildBatchConfigOutputReference":
        return typing.cast("CodebuildProjectBuildBatchConfigOutputReference", jsii.get(self, "buildBatchConfig"))

    @builtins.property
    @jsii.member(jsii_name="cache")
    def cache(self) -> "CodebuildProjectCacheOutputReference":
        return typing.cast("CodebuildProjectCacheOutputReference", jsii.get(self, "cache"))

    @builtins.property
    @jsii.member(jsii_name="environment")
    def environment(self) -> "CodebuildProjectEnvironmentOutputReference":
        return typing.cast("CodebuildProjectEnvironmentOutputReference", jsii.get(self, "environment"))

    @builtins.property
    @jsii.member(jsii_name="fileSystemLocations")
    def file_system_locations(self) -> "CodebuildProjectFileSystemLocationsList":
        return typing.cast("CodebuildProjectFileSystemLocationsList", jsii.get(self, "fileSystemLocations"))

    @builtins.property
    @jsii.member(jsii_name="logsConfig")
    def logs_config(self) -> "CodebuildProjectLogsConfigOutputReference":
        return typing.cast("CodebuildProjectLogsConfigOutputReference", jsii.get(self, "logsConfig"))

    @builtins.property
    @jsii.member(jsii_name="publicProjectAlias")
    def public_project_alias(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicProjectAlias"))

    @builtins.property
    @jsii.member(jsii_name="secondaryArtifacts")
    def secondary_artifacts(self) -> "CodebuildProjectSecondaryArtifactsList":
        return typing.cast("CodebuildProjectSecondaryArtifactsList", jsii.get(self, "secondaryArtifacts"))

    @builtins.property
    @jsii.member(jsii_name="secondarySources")
    def secondary_sources(self) -> "CodebuildProjectSecondarySourcesList":
        return typing.cast("CodebuildProjectSecondarySourcesList", jsii.get(self, "secondarySources"))

    @builtins.property
    @jsii.member(jsii_name="secondarySourceVersion")
    def secondary_source_version(self) -> "CodebuildProjectSecondarySourceVersionList":
        return typing.cast("CodebuildProjectSecondarySourceVersionList", jsii.get(self, "secondarySourceVersion"))

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> "CodebuildProjectSourceOutputReference":
        return typing.cast("CodebuildProjectSourceOutputReference", jsii.get(self, "source"))

    @builtins.property
    @jsii.member(jsii_name="vpcConfig")
    def vpc_config(self) -> "CodebuildProjectVpcConfigOutputReference":
        return typing.cast("CodebuildProjectVpcConfigOutputReference", jsii.get(self, "vpcConfig"))

    @builtins.property
    @jsii.member(jsii_name="artifactsInput")
    def artifacts_input(self) -> typing.Optional["CodebuildProjectArtifacts"]:
        return typing.cast(typing.Optional["CodebuildProjectArtifacts"], jsii.get(self, "artifactsInput"))

    @builtins.property
    @jsii.member(jsii_name="badgeEnabledInput")
    def badge_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "badgeEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="buildBatchConfigInput")
    def build_batch_config_input(
        self,
    ) -> typing.Optional["CodebuildProjectBuildBatchConfig"]:
        return typing.cast(typing.Optional["CodebuildProjectBuildBatchConfig"], jsii.get(self, "buildBatchConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="buildTimeoutInput")
    def build_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "buildTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheInput")
    def cache_input(self) -> typing.Optional["CodebuildProjectCache"]:
        return typing.cast(typing.Optional["CodebuildProjectCache"], jsii.get(self, "cacheInput"))

    @builtins.property
    @jsii.member(jsii_name="concurrentBuildLimitInput")
    def concurrent_build_limit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "concurrentBuildLimitInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionKeyInput")
    def encryption_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptionKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="environmentInput")
    def environment_input(self) -> typing.Optional["CodebuildProjectEnvironment"]:
        return typing.cast(typing.Optional["CodebuildProjectEnvironment"], jsii.get(self, "environmentInput"))

    @builtins.property
    @jsii.member(jsii_name="fileSystemLocationsInput")
    def file_system_locations_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CodebuildProjectFileSystemLocations"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CodebuildProjectFileSystemLocations"]]], jsii.get(self, "fileSystemLocationsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="logsConfigInput")
    def logs_config_input(self) -> typing.Optional["CodebuildProjectLogsConfig"]:
        return typing.cast(typing.Optional["CodebuildProjectLogsConfig"], jsii.get(self, "logsConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="projectVisibilityInput")
    def project_visibility_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectVisibilityInput"))

    @builtins.property
    @jsii.member(jsii_name="queuedTimeoutInput")
    def queued_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "queuedTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceAccessRoleInput")
    def resource_access_role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceAccessRoleInput"))

    @builtins.property
    @jsii.member(jsii_name="secondaryArtifactsInput")
    def secondary_artifacts_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CodebuildProjectSecondaryArtifacts"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CodebuildProjectSecondaryArtifacts"]]], jsii.get(self, "secondaryArtifactsInput"))

    @builtins.property
    @jsii.member(jsii_name="secondarySourcesInput")
    def secondary_sources_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CodebuildProjectSecondarySources"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CodebuildProjectSecondarySources"]]], jsii.get(self, "secondarySourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="secondarySourceVersionInput")
    def secondary_source_version_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CodebuildProjectSecondarySourceVersion"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CodebuildProjectSecondarySourceVersion"]]], jsii.get(self, "secondarySourceVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceRoleInput")
    def service_role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceRoleInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceInput")
    def source_input(self) -> typing.Optional["CodebuildProjectSource"]:
        return typing.cast(typing.Optional["CodebuildProjectSource"], jsii.get(self, "sourceInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceVersionInput")
    def source_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceVersionInput"))

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
    @jsii.member(jsii_name="vpcConfigInput")
    def vpc_config_input(self) -> typing.Optional["CodebuildProjectVpcConfig"]:
        return typing.cast(typing.Optional["CodebuildProjectVpcConfig"], jsii.get(self, "vpcConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="badgeEnabled")
    def badge_enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "badgeEnabled"))

    @badge_enabled.setter
    def badge_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a47754483b9b490c7b8735c6e7cea185719bc104f24fa5a11955de7f27931bdd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "badgeEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="buildTimeout")
    def build_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "buildTimeout"))

    @build_timeout.setter
    def build_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69f472423fbe928a7e8d67aa6e688e7d809b88252a4017d44dd3301757dccf18)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "buildTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="concurrentBuildLimit")
    def concurrent_build_limit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "concurrentBuildLimit"))

    @concurrent_build_limit.setter
    def concurrent_build_limit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c5ea9350a08ecdc6140ebcbfed545ade2346c42377c9dbe7cad9e59ca5cf32b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "concurrentBuildLimit", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea5115af55c3426f84b74f3c0725d530399675ae255e54e1084de2e95c447a01)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionKey")
    def encryption_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encryptionKey"))

    @encryption_key.setter
    def encryption_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b53da2f0032879e089479584cf4b2ce76f7a6cf2e905440cc506e34e9875ff81)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionKey", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2dc38e88976aa8294df59d983c74cb6879ae6df6ce3b8f2f39af89eda657ba9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac21ac7de235e7dad75b976a0172bb84e583618a3c162a82080fe1276a48c245)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="projectVisibility")
    def project_visibility(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectVisibility"))

    @project_visibility.setter
    def project_visibility(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3c438a309a89f328c2cab84d86604a3390f02332414559cda18d989e2187353)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectVisibility", value)

    @builtins.property
    @jsii.member(jsii_name="queuedTimeout")
    def queued_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "queuedTimeout"))

    @queued_timeout.setter
    def queued_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e539762dc739e14f379afebe28f0b3fe770b39606e1998fa91ca421884aa89ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queuedTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="resourceAccessRole")
    def resource_access_role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceAccessRole"))

    @resource_access_role.setter
    def resource_access_role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3f0a63d736b1d519b104894b1ab4978930814854149ea958fd77b12355bf00c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceAccessRole", value)

    @builtins.property
    @jsii.member(jsii_name="serviceRole")
    def service_role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceRole"))

    @service_role.setter
    def service_role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__751381ebbc9a81fb839c818ca7f9e9e071ff06a9713d907ea49ab0865c8a6246)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceRole", value)

    @builtins.property
    @jsii.member(jsii_name="sourceVersion")
    def source_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceVersion"))

    @source_version.setter
    def source_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__777793a8c84edbe66e04154be7bf11a5a44026779998ab58b7ade094ec07299d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceVersion", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ad749379a7cfcf29eb6fb11e39e81100237ff6922e2bdd43d69e71659a1f3e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f75948599993d31569bae1f8ff2fd48d72fcb75e3b6aaf81b786035d63d5de34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.codebuildProject.CodebuildProjectArtifacts",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "artifact_identifier": "artifactIdentifier",
        "bucket_owner_access": "bucketOwnerAccess",
        "encryption_disabled": "encryptionDisabled",
        "location": "location",
        "name": "name",
        "namespace_type": "namespaceType",
        "override_artifact_name": "overrideArtifactName",
        "packaging": "packaging",
        "path": "path",
    },
)
class CodebuildProjectArtifacts:
    def __init__(
        self,
        *,
        type: builtins.str,
        artifact_identifier: typing.Optional[builtins.str] = None,
        bucket_owner_access: typing.Optional[builtins.str] = None,
        encryption_disabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        location: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        namespace_type: typing.Optional[builtins.str] = None,
        override_artifact_name: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        packaging: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.
        :param artifact_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#artifact_identifier CodebuildProject#artifact_identifier}.
        :param bucket_owner_access: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#bucket_owner_access CodebuildProject#bucket_owner_access}.
        :param encryption_disabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#encryption_disabled CodebuildProject#encryption_disabled}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#location CodebuildProject#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#name CodebuildProject#name}.
        :param namespace_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#namespace_type CodebuildProject#namespace_type}.
        :param override_artifact_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#override_artifact_name CodebuildProject#override_artifact_name}.
        :param packaging: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#packaging CodebuildProject#packaging}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#path CodebuildProject#path}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb092af1df85cfc874d14a934c6104e0fe6b9e3b71acd918bfc4c7959bc4daca)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument artifact_identifier", value=artifact_identifier, expected_type=type_hints["artifact_identifier"])
            check_type(argname="argument bucket_owner_access", value=bucket_owner_access, expected_type=type_hints["bucket_owner_access"])
            check_type(argname="argument encryption_disabled", value=encryption_disabled, expected_type=type_hints["encryption_disabled"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace_type", value=namespace_type, expected_type=type_hints["namespace_type"])
            check_type(argname="argument override_artifact_name", value=override_artifact_name, expected_type=type_hints["override_artifact_name"])
            check_type(argname="argument packaging", value=packaging, expected_type=type_hints["packaging"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if artifact_identifier is not None:
            self._values["artifact_identifier"] = artifact_identifier
        if bucket_owner_access is not None:
            self._values["bucket_owner_access"] = bucket_owner_access
        if encryption_disabled is not None:
            self._values["encryption_disabled"] = encryption_disabled
        if location is not None:
            self._values["location"] = location
        if name is not None:
            self._values["name"] = name
        if namespace_type is not None:
            self._values["namespace_type"] = namespace_type
        if override_artifact_name is not None:
            self._values["override_artifact_name"] = override_artifact_name
        if packaging is not None:
            self._values["packaging"] = packaging
        if path is not None:
            self._values["path"] = path

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def artifact_identifier(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#artifact_identifier CodebuildProject#artifact_identifier}.'''
        result = self._values.get("artifact_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket_owner_access(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#bucket_owner_access CodebuildProject#bucket_owner_access}.'''
        result = self._values.get("bucket_owner_access")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#encryption_disabled CodebuildProject#encryption_disabled}.'''
        result = self._values.get("encryption_disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def location(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#location CodebuildProject#location}.'''
        result = self._values.get("location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#name CodebuildProject#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#namespace_type CodebuildProject#namespace_type}.'''
        result = self._values.get("namespace_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def override_artifact_name(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#override_artifact_name CodebuildProject#override_artifact_name}.'''
        result = self._values.get("override_artifact_name")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def packaging(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#packaging CodebuildProject#packaging}.'''
        result = self._values.get("packaging")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#path CodebuildProject#path}.'''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodebuildProjectArtifacts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodebuildProjectArtifactsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codebuildProject.CodebuildProjectArtifactsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c19806eec59124a4158fb08dc4f1cb237a241a178428d74799fdd61adacb324d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetArtifactIdentifier")
    def reset_artifact_identifier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArtifactIdentifier", []))

    @jsii.member(jsii_name="resetBucketOwnerAccess")
    def reset_bucket_owner_access(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketOwnerAccess", []))

    @jsii.member(jsii_name="resetEncryptionDisabled")
    def reset_encryption_disabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionDisabled", []))

    @jsii.member(jsii_name="resetLocation")
    def reset_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocation", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamespaceType")
    def reset_namespace_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespaceType", []))

    @jsii.member(jsii_name="resetOverrideArtifactName")
    def reset_override_artifact_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOverrideArtifactName", []))

    @jsii.member(jsii_name="resetPackaging")
    def reset_packaging(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPackaging", []))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @builtins.property
    @jsii.member(jsii_name="artifactIdentifierInput")
    def artifact_identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "artifactIdentifierInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketOwnerAccessInput")
    def bucket_owner_access_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketOwnerAccessInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionDisabledInput")
    def encryption_disabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "encryptionDisabledInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceTypeInput")
    def namespace_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="overrideArtifactNameInput")
    def override_artifact_name_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "overrideArtifactNameInput"))

    @builtins.property
    @jsii.member(jsii_name="packagingInput")
    def packaging_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "packagingInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="artifactIdentifier")
    def artifact_identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "artifactIdentifier"))

    @artifact_identifier.setter
    def artifact_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20963fbb1df0437f1a1239f815615ab02b0efc6773e99cb6fe9d28b2f35310ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "artifactIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="bucketOwnerAccess")
    def bucket_owner_access(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketOwnerAccess"))

    @bucket_owner_access.setter
    def bucket_owner_access(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__251e1ec5f701668bc00815caec109043b238d1e93580f061e3aa88d2d83060fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketOwnerAccess", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionDisabled")
    def encryption_disabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "encryptionDisabled"))

    @encryption_disabled.setter
    def encryption_disabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f8186468fae5723482cd7b84fee6b65981d8d9cd3d23c0a1985fbeda1921ce8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionDisabled", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__841f8539627517f797d1d6cee7db652d526d50f93c0fdb389641c38c76d251b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12f9cdeac4451b433ad21f7e7cd28f89ca74c47bea9f0bb6db0977c81c894cd7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespaceType")
    def namespace_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespaceType"))

    @namespace_type.setter
    def namespace_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11a8002fb110df79c71f76955a6c0012cfcfb1d756a1f727cade8675a408ad2c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespaceType", value)

    @builtins.property
    @jsii.member(jsii_name="overrideArtifactName")
    def override_artifact_name(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "overrideArtifactName"))

    @override_artifact_name.setter
    def override_artifact_name(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28ec914c253e35c0be8c5bdea7a5f4c7d26ba0465f9ce6456e8a6e276a3e6d86)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "overrideArtifactName", value)

    @builtins.property
    @jsii.member(jsii_name="packaging")
    def packaging(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "packaging"))

    @packaging.setter
    def packaging(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff24787c9930ceb80b4311dc23776e49f38ae09fb6316aa274d8de6d7f20b9ca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "packaging", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2496330b29daca8ec6f8ceab2b1a48495e4b075945642930bbee2f7e52681cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7d1fbd86457fd5e7b66a29860ed22be6df8378e81255e307f5e9046d84bf713)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CodebuildProjectArtifacts]:
        return typing.cast(typing.Optional[CodebuildProjectArtifacts], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[CodebuildProjectArtifacts]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc902fe3c9c08dc52f5a5136d1ef0479a73580fc87d16b29b006076582e6f559)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.codebuildProject.CodebuildProjectBuildBatchConfig",
    jsii_struct_bases=[],
    name_mapping={
        "service_role": "serviceRole",
        "combine_artifacts": "combineArtifacts",
        "restrictions": "restrictions",
        "timeout_in_mins": "timeoutInMins",
    },
)
class CodebuildProjectBuildBatchConfig:
    def __init__(
        self,
        *,
        service_role: builtins.str,
        combine_artifacts: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        restrictions: typing.Optional[typing.Union["CodebuildProjectBuildBatchConfigRestrictions", typing.Dict[builtins.str, typing.Any]]] = None,
        timeout_in_mins: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param service_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#service_role CodebuildProject#service_role}.
        :param combine_artifacts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#combine_artifacts CodebuildProject#combine_artifacts}.
        :param restrictions: restrictions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#restrictions CodebuildProject#restrictions}
        :param timeout_in_mins: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#timeout_in_mins CodebuildProject#timeout_in_mins}.
        '''
        if isinstance(restrictions, dict):
            restrictions = CodebuildProjectBuildBatchConfigRestrictions(**restrictions)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__700011e1d00d52a8f35364860c1bc43eeb7af741b423084932b2db71f07523e0)
            check_type(argname="argument service_role", value=service_role, expected_type=type_hints["service_role"])
            check_type(argname="argument combine_artifacts", value=combine_artifacts, expected_type=type_hints["combine_artifacts"])
            check_type(argname="argument restrictions", value=restrictions, expected_type=type_hints["restrictions"])
            check_type(argname="argument timeout_in_mins", value=timeout_in_mins, expected_type=type_hints["timeout_in_mins"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "service_role": service_role,
        }
        if combine_artifacts is not None:
            self._values["combine_artifacts"] = combine_artifacts
        if restrictions is not None:
            self._values["restrictions"] = restrictions
        if timeout_in_mins is not None:
            self._values["timeout_in_mins"] = timeout_in_mins

    @builtins.property
    def service_role(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#service_role CodebuildProject#service_role}.'''
        result = self._values.get("service_role")
        assert result is not None, "Required property 'service_role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def combine_artifacts(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#combine_artifacts CodebuildProject#combine_artifacts}.'''
        result = self._values.get("combine_artifacts")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def restrictions(
        self,
    ) -> typing.Optional["CodebuildProjectBuildBatchConfigRestrictions"]:
        '''restrictions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#restrictions CodebuildProject#restrictions}
        '''
        result = self._values.get("restrictions")
        return typing.cast(typing.Optional["CodebuildProjectBuildBatchConfigRestrictions"], result)

    @builtins.property
    def timeout_in_mins(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#timeout_in_mins CodebuildProject#timeout_in_mins}.'''
        result = self._values.get("timeout_in_mins")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodebuildProjectBuildBatchConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodebuildProjectBuildBatchConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codebuildProject.CodebuildProjectBuildBatchConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d0f7a8818f0f94ecd6d0341ee3a05707d8e20179e3af331c13a3bf08cd41a4e2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRestrictions")
    def put_restrictions(
        self,
        *,
        compute_types_allowed: typing.Optional[typing.Sequence[builtins.str]] = None,
        maximum_builds_allowed: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param compute_types_allowed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#compute_types_allowed CodebuildProject#compute_types_allowed}.
        :param maximum_builds_allowed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#maximum_builds_allowed CodebuildProject#maximum_builds_allowed}.
        '''
        value = CodebuildProjectBuildBatchConfigRestrictions(
            compute_types_allowed=compute_types_allowed,
            maximum_builds_allowed=maximum_builds_allowed,
        )

        return typing.cast(None, jsii.invoke(self, "putRestrictions", [value]))

    @jsii.member(jsii_name="resetCombineArtifacts")
    def reset_combine_artifacts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCombineArtifacts", []))

    @jsii.member(jsii_name="resetRestrictions")
    def reset_restrictions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRestrictions", []))

    @jsii.member(jsii_name="resetTimeoutInMins")
    def reset_timeout_in_mins(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeoutInMins", []))

    @builtins.property
    @jsii.member(jsii_name="restrictions")
    def restrictions(
        self,
    ) -> "CodebuildProjectBuildBatchConfigRestrictionsOutputReference":
        return typing.cast("CodebuildProjectBuildBatchConfigRestrictionsOutputReference", jsii.get(self, "restrictions"))

    @builtins.property
    @jsii.member(jsii_name="combineArtifactsInput")
    def combine_artifacts_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "combineArtifactsInput"))

    @builtins.property
    @jsii.member(jsii_name="restrictionsInput")
    def restrictions_input(
        self,
    ) -> typing.Optional["CodebuildProjectBuildBatchConfigRestrictions"]:
        return typing.cast(typing.Optional["CodebuildProjectBuildBatchConfigRestrictions"], jsii.get(self, "restrictionsInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceRoleInput")
    def service_role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceRoleInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutInMinsInput")
    def timeout_in_mins_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutInMinsInput"))

    @builtins.property
    @jsii.member(jsii_name="combineArtifacts")
    def combine_artifacts(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "combineArtifacts"))

    @combine_artifacts.setter
    def combine_artifacts(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23c847123bbbbf9429c2c47374491825e375959fe37a0a98b5bf3e969dde0b11)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "combineArtifacts", value)

    @builtins.property
    @jsii.member(jsii_name="serviceRole")
    def service_role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceRole"))

    @service_role.setter
    def service_role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c322638e904201ef41413f94efd52a35549ca642839c873bc049a621c49c118)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceRole", value)

    @builtins.property
    @jsii.member(jsii_name="timeoutInMins")
    def timeout_in_mins(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeoutInMins"))

    @timeout_in_mins.setter
    def timeout_in_mins(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84a13172f340b851344b1ef218867e5fed8eb62c656b261aec2ed5f8f7e1ebb9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutInMins", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CodebuildProjectBuildBatchConfig]:
        return typing.cast(typing.Optional[CodebuildProjectBuildBatchConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodebuildProjectBuildBatchConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be29742081e93d2bbee985089cdc3c46e5d1de499e9d13837619cd22605be9bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.codebuildProject.CodebuildProjectBuildBatchConfigRestrictions",
    jsii_struct_bases=[],
    name_mapping={
        "compute_types_allowed": "computeTypesAllowed",
        "maximum_builds_allowed": "maximumBuildsAllowed",
    },
)
class CodebuildProjectBuildBatchConfigRestrictions:
    def __init__(
        self,
        *,
        compute_types_allowed: typing.Optional[typing.Sequence[builtins.str]] = None,
        maximum_builds_allowed: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param compute_types_allowed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#compute_types_allowed CodebuildProject#compute_types_allowed}.
        :param maximum_builds_allowed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#maximum_builds_allowed CodebuildProject#maximum_builds_allowed}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__feb18f6eee2561e572fbdd33dd63545673823caafa0d08977fc9e28565469e65)
            check_type(argname="argument compute_types_allowed", value=compute_types_allowed, expected_type=type_hints["compute_types_allowed"])
            check_type(argname="argument maximum_builds_allowed", value=maximum_builds_allowed, expected_type=type_hints["maximum_builds_allowed"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if compute_types_allowed is not None:
            self._values["compute_types_allowed"] = compute_types_allowed
        if maximum_builds_allowed is not None:
            self._values["maximum_builds_allowed"] = maximum_builds_allowed

    @builtins.property
    def compute_types_allowed(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#compute_types_allowed CodebuildProject#compute_types_allowed}.'''
        result = self._values.get("compute_types_allowed")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def maximum_builds_allowed(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#maximum_builds_allowed CodebuildProject#maximum_builds_allowed}.'''
        result = self._values.get("maximum_builds_allowed")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodebuildProjectBuildBatchConfigRestrictions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodebuildProjectBuildBatchConfigRestrictionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codebuildProject.CodebuildProjectBuildBatchConfigRestrictionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fd1d1b361db73ca10b4d76cf7980fd84715cb13086d4d1b1b94397e7fde53a05)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetComputeTypesAllowed")
    def reset_compute_types_allowed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComputeTypesAllowed", []))

    @jsii.member(jsii_name="resetMaximumBuildsAllowed")
    def reset_maximum_builds_allowed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaximumBuildsAllowed", []))

    @builtins.property
    @jsii.member(jsii_name="computeTypesAllowedInput")
    def compute_types_allowed_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "computeTypesAllowedInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumBuildsAllowedInput")
    def maximum_builds_allowed_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maximumBuildsAllowedInput"))

    @builtins.property
    @jsii.member(jsii_name="computeTypesAllowed")
    def compute_types_allowed(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "computeTypesAllowed"))

    @compute_types_allowed.setter
    def compute_types_allowed(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ab3343d71b2648c48275abda5c77ca0576911aed0c652e744fbf5231d73c4b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "computeTypesAllowed", value)

    @builtins.property
    @jsii.member(jsii_name="maximumBuildsAllowed")
    def maximum_builds_allowed(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maximumBuildsAllowed"))

    @maximum_builds_allowed.setter
    def maximum_builds_allowed(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14899afaed61069cdac0a16c512103a46ece3ba38b4b00061add9fe769afe888)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumBuildsAllowed", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CodebuildProjectBuildBatchConfigRestrictions]:
        return typing.cast(typing.Optional[CodebuildProjectBuildBatchConfigRestrictions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodebuildProjectBuildBatchConfigRestrictions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccfbecba65037f07c9783e4f65d958a12c1b3e69b405e0142290eab4f9112186)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.codebuildProject.CodebuildProjectCache",
    jsii_struct_bases=[],
    name_mapping={"location": "location", "modes": "modes", "type": "type"},
)
class CodebuildProjectCache:
    def __init__(
        self,
        *,
        location: typing.Optional[builtins.str] = None,
        modes: typing.Optional[typing.Sequence[builtins.str]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#location CodebuildProject#location}.
        :param modes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#modes CodebuildProject#modes}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69dbc62af7768c00619bd610addcba8cdf08ba265149877d4def20e072001837)
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument modes", value=modes, expected_type=type_hints["modes"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if location is not None:
            self._values["location"] = location
        if modes is not None:
            self._values["modes"] = modes
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def location(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#location CodebuildProject#location}.'''
        result = self._values.get("location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def modes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#modes CodebuildProject#modes}.'''
        result = self._values.get("modes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodebuildProjectCache(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodebuildProjectCacheOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codebuildProject.CodebuildProjectCacheOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3b7cc3ff572a3bff8846ec484e9292ed5c105a925beb1563f14c18c98f2c7ecb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetLocation")
    def reset_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocation", []))

    @jsii.member(jsii_name="resetModes")
    def reset_modes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetModes", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="modesInput")
    def modes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "modesInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efdbacd86a3039dbd308e52a17ed462268c7a22f63c6eaf2e647653c06144249)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="modes")
    def modes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "modes"))

    @modes.setter
    def modes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37fa6ae80596985a5d3a9a0e105ae7a59d554006ac35c8279b446789940f635f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "modes", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4dd6743d863e00f8124532733112f203726cb26a2f6d1704f0136762a3348aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CodebuildProjectCache]:
        return typing.cast(typing.Optional[CodebuildProjectCache], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[CodebuildProjectCache]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3259b055e2174d70ebac79374807b91eea00a17dee0ffe926e150bb713a56998)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.codebuildProject.CodebuildProjectConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "artifacts": "artifacts",
        "environment": "environment",
        "name": "name",
        "service_role": "serviceRole",
        "source": "source",
        "badge_enabled": "badgeEnabled",
        "build_batch_config": "buildBatchConfig",
        "build_timeout": "buildTimeout",
        "cache": "cache",
        "concurrent_build_limit": "concurrentBuildLimit",
        "description": "description",
        "encryption_key": "encryptionKey",
        "file_system_locations": "fileSystemLocations",
        "id": "id",
        "logs_config": "logsConfig",
        "project_visibility": "projectVisibility",
        "queued_timeout": "queuedTimeout",
        "resource_access_role": "resourceAccessRole",
        "secondary_artifacts": "secondaryArtifacts",
        "secondary_sources": "secondarySources",
        "secondary_source_version": "secondarySourceVersion",
        "source_version": "sourceVersion",
        "tags": "tags",
        "tags_all": "tagsAll",
        "vpc_config": "vpcConfig",
    },
)
class CodebuildProjectConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        artifacts: typing.Union[CodebuildProjectArtifacts, typing.Dict[builtins.str, typing.Any]],
        environment: typing.Union["CodebuildProjectEnvironment", typing.Dict[builtins.str, typing.Any]],
        name: builtins.str,
        service_role: builtins.str,
        source: typing.Union["CodebuildProjectSource", typing.Dict[builtins.str, typing.Any]],
        badge_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        build_batch_config: typing.Optional[typing.Union[CodebuildProjectBuildBatchConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        build_timeout: typing.Optional[jsii.Number] = None,
        cache: typing.Optional[typing.Union[CodebuildProjectCache, typing.Dict[builtins.str, typing.Any]]] = None,
        concurrent_build_limit: typing.Optional[jsii.Number] = None,
        description: typing.Optional[builtins.str] = None,
        encryption_key: typing.Optional[builtins.str] = None,
        file_system_locations: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CodebuildProjectFileSystemLocations", typing.Dict[builtins.str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        logs_config: typing.Optional[typing.Union["CodebuildProjectLogsConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        project_visibility: typing.Optional[builtins.str] = None,
        queued_timeout: typing.Optional[jsii.Number] = None,
        resource_access_role: typing.Optional[builtins.str] = None,
        secondary_artifacts: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CodebuildProjectSecondaryArtifacts", typing.Dict[builtins.str, typing.Any]]]]] = None,
        secondary_sources: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CodebuildProjectSecondarySources", typing.Dict[builtins.str, typing.Any]]]]] = None,
        secondary_source_version: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CodebuildProjectSecondarySourceVersion", typing.Dict[builtins.str, typing.Any]]]]] = None,
        source_version: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        vpc_config: typing.Optional[typing.Union["CodebuildProjectVpcConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param artifacts: artifacts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#artifacts CodebuildProject#artifacts}
        :param environment: environment block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#environment CodebuildProject#environment}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#name CodebuildProject#name}.
        :param service_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#service_role CodebuildProject#service_role}.
        :param source: source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#source CodebuildProject#source}
        :param badge_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#badge_enabled CodebuildProject#badge_enabled}.
        :param build_batch_config: build_batch_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#build_batch_config CodebuildProject#build_batch_config}
        :param build_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#build_timeout CodebuildProject#build_timeout}.
        :param cache: cache block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#cache CodebuildProject#cache}
        :param concurrent_build_limit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#concurrent_build_limit CodebuildProject#concurrent_build_limit}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#description CodebuildProject#description}.
        :param encryption_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#encryption_key CodebuildProject#encryption_key}.
        :param file_system_locations: file_system_locations block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#file_system_locations CodebuildProject#file_system_locations}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#id CodebuildProject#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param logs_config: logs_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#logs_config CodebuildProject#logs_config}
        :param project_visibility: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#project_visibility CodebuildProject#project_visibility}.
        :param queued_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#queued_timeout CodebuildProject#queued_timeout}.
        :param resource_access_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#resource_access_role CodebuildProject#resource_access_role}.
        :param secondary_artifacts: secondary_artifacts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#secondary_artifacts CodebuildProject#secondary_artifacts}
        :param secondary_sources: secondary_sources block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#secondary_sources CodebuildProject#secondary_sources}
        :param secondary_source_version: secondary_source_version block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#secondary_source_version CodebuildProject#secondary_source_version}
        :param source_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#source_version CodebuildProject#source_version}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#tags CodebuildProject#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#tags_all CodebuildProject#tags_all}.
        :param vpc_config: vpc_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#vpc_config CodebuildProject#vpc_config}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(artifacts, dict):
            artifacts = CodebuildProjectArtifacts(**artifacts)
        if isinstance(environment, dict):
            environment = CodebuildProjectEnvironment(**environment)
        if isinstance(source, dict):
            source = CodebuildProjectSource(**source)
        if isinstance(build_batch_config, dict):
            build_batch_config = CodebuildProjectBuildBatchConfig(**build_batch_config)
        if isinstance(cache, dict):
            cache = CodebuildProjectCache(**cache)
        if isinstance(logs_config, dict):
            logs_config = CodebuildProjectLogsConfig(**logs_config)
        if isinstance(vpc_config, dict):
            vpc_config = CodebuildProjectVpcConfig(**vpc_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fce208a1961fa45f79ccd9acb096c46e50d3e6c1b899d0ce6488a238b468f90)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument artifacts", value=artifacts, expected_type=type_hints["artifacts"])
            check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument service_role", value=service_role, expected_type=type_hints["service_role"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument badge_enabled", value=badge_enabled, expected_type=type_hints["badge_enabled"])
            check_type(argname="argument build_batch_config", value=build_batch_config, expected_type=type_hints["build_batch_config"])
            check_type(argname="argument build_timeout", value=build_timeout, expected_type=type_hints["build_timeout"])
            check_type(argname="argument cache", value=cache, expected_type=type_hints["cache"])
            check_type(argname="argument concurrent_build_limit", value=concurrent_build_limit, expected_type=type_hints["concurrent_build_limit"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument encryption_key", value=encryption_key, expected_type=type_hints["encryption_key"])
            check_type(argname="argument file_system_locations", value=file_system_locations, expected_type=type_hints["file_system_locations"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument logs_config", value=logs_config, expected_type=type_hints["logs_config"])
            check_type(argname="argument project_visibility", value=project_visibility, expected_type=type_hints["project_visibility"])
            check_type(argname="argument queued_timeout", value=queued_timeout, expected_type=type_hints["queued_timeout"])
            check_type(argname="argument resource_access_role", value=resource_access_role, expected_type=type_hints["resource_access_role"])
            check_type(argname="argument secondary_artifacts", value=secondary_artifacts, expected_type=type_hints["secondary_artifacts"])
            check_type(argname="argument secondary_sources", value=secondary_sources, expected_type=type_hints["secondary_sources"])
            check_type(argname="argument secondary_source_version", value=secondary_source_version, expected_type=type_hints["secondary_source_version"])
            check_type(argname="argument source_version", value=source_version, expected_type=type_hints["source_version"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument vpc_config", value=vpc_config, expected_type=type_hints["vpc_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "artifacts": artifacts,
            "environment": environment,
            "name": name,
            "service_role": service_role,
            "source": source,
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
        if badge_enabled is not None:
            self._values["badge_enabled"] = badge_enabled
        if build_batch_config is not None:
            self._values["build_batch_config"] = build_batch_config
        if build_timeout is not None:
            self._values["build_timeout"] = build_timeout
        if cache is not None:
            self._values["cache"] = cache
        if concurrent_build_limit is not None:
            self._values["concurrent_build_limit"] = concurrent_build_limit
        if description is not None:
            self._values["description"] = description
        if encryption_key is not None:
            self._values["encryption_key"] = encryption_key
        if file_system_locations is not None:
            self._values["file_system_locations"] = file_system_locations
        if id is not None:
            self._values["id"] = id
        if logs_config is not None:
            self._values["logs_config"] = logs_config
        if project_visibility is not None:
            self._values["project_visibility"] = project_visibility
        if queued_timeout is not None:
            self._values["queued_timeout"] = queued_timeout
        if resource_access_role is not None:
            self._values["resource_access_role"] = resource_access_role
        if secondary_artifacts is not None:
            self._values["secondary_artifacts"] = secondary_artifacts
        if secondary_sources is not None:
            self._values["secondary_sources"] = secondary_sources
        if secondary_source_version is not None:
            self._values["secondary_source_version"] = secondary_source_version
        if source_version is not None:
            self._values["source_version"] = source_version
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if vpc_config is not None:
            self._values["vpc_config"] = vpc_config

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
    def artifacts(self) -> CodebuildProjectArtifacts:
        '''artifacts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#artifacts CodebuildProject#artifacts}
        '''
        result = self._values.get("artifacts")
        assert result is not None, "Required property 'artifacts' is missing"
        return typing.cast(CodebuildProjectArtifacts, result)

    @builtins.property
    def environment(self) -> "CodebuildProjectEnvironment":
        '''environment block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#environment CodebuildProject#environment}
        '''
        result = self._values.get("environment")
        assert result is not None, "Required property 'environment' is missing"
        return typing.cast("CodebuildProjectEnvironment", result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#name CodebuildProject#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_role(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#service_role CodebuildProject#service_role}.'''
        result = self._values.get("service_role")
        assert result is not None, "Required property 'service_role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source(self) -> "CodebuildProjectSource":
        '''source block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#source CodebuildProject#source}
        '''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast("CodebuildProjectSource", result)

    @builtins.property
    def badge_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#badge_enabled CodebuildProject#badge_enabled}.'''
        result = self._values.get("badge_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def build_batch_config(self) -> typing.Optional[CodebuildProjectBuildBatchConfig]:
        '''build_batch_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#build_batch_config CodebuildProject#build_batch_config}
        '''
        result = self._values.get("build_batch_config")
        return typing.cast(typing.Optional[CodebuildProjectBuildBatchConfig], result)

    @builtins.property
    def build_timeout(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#build_timeout CodebuildProject#build_timeout}.'''
        result = self._values.get("build_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cache(self) -> typing.Optional[CodebuildProjectCache]:
        '''cache block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#cache CodebuildProject#cache}
        '''
        result = self._values.get("cache")
        return typing.cast(typing.Optional[CodebuildProjectCache], result)

    @builtins.property
    def concurrent_build_limit(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#concurrent_build_limit CodebuildProject#concurrent_build_limit}.'''
        result = self._values.get("concurrent_build_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#description CodebuildProject#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#encryption_key CodebuildProject#encryption_key}.'''
        result = self._values.get("encryption_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def file_system_locations(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CodebuildProjectFileSystemLocations"]]]:
        '''file_system_locations block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#file_system_locations CodebuildProject#file_system_locations}
        '''
        result = self._values.get("file_system_locations")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CodebuildProjectFileSystemLocations"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#id CodebuildProject#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logs_config(self) -> typing.Optional["CodebuildProjectLogsConfig"]:
        '''logs_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#logs_config CodebuildProject#logs_config}
        '''
        result = self._values.get("logs_config")
        return typing.cast(typing.Optional["CodebuildProjectLogsConfig"], result)

    @builtins.property
    def project_visibility(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#project_visibility CodebuildProject#project_visibility}.'''
        result = self._values.get("project_visibility")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def queued_timeout(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#queued_timeout CodebuildProject#queued_timeout}.'''
        result = self._values.get("queued_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def resource_access_role(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#resource_access_role CodebuildProject#resource_access_role}.'''
        result = self._values.get("resource_access_role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secondary_artifacts(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CodebuildProjectSecondaryArtifacts"]]]:
        '''secondary_artifacts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#secondary_artifacts CodebuildProject#secondary_artifacts}
        '''
        result = self._values.get("secondary_artifacts")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CodebuildProjectSecondaryArtifacts"]]], result)

    @builtins.property
    def secondary_sources(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CodebuildProjectSecondarySources"]]]:
        '''secondary_sources block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#secondary_sources CodebuildProject#secondary_sources}
        '''
        result = self._values.get("secondary_sources")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CodebuildProjectSecondarySources"]]], result)

    @builtins.property
    def secondary_source_version(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CodebuildProjectSecondarySourceVersion"]]]:
        '''secondary_source_version block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#secondary_source_version CodebuildProject#secondary_source_version}
        '''
        result = self._values.get("secondary_source_version")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CodebuildProjectSecondarySourceVersion"]]], result)

    @builtins.property
    def source_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#source_version CodebuildProject#source_version}.'''
        result = self._values.get("source_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#tags CodebuildProject#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#tags_all CodebuildProject#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def vpc_config(self) -> typing.Optional["CodebuildProjectVpcConfig"]:
        '''vpc_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#vpc_config CodebuildProject#vpc_config}
        '''
        result = self._values.get("vpc_config")
        return typing.cast(typing.Optional["CodebuildProjectVpcConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodebuildProjectConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.codebuildProject.CodebuildProjectEnvironment",
    jsii_struct_bases=[],
    name_mapping={
        "compute_type": "computeType",
        "image": "image",
        "type": "type",
        "certificate": "certificate",
        "environment_variable": "environmentVariable",
        "image_pull_credentials_type": "imagePullCredentialsType",
        "privileged_mode": "privilegedMode",
        "registry_credential": "registryCredential",
    },
)
class CodebuildProjectEnvironment:
    def __init__(
        self,
        *,
        compute_type: builtins.str,
        image: builtins.str,
        type: builtins.str,
        certificate: typing.Optional[builtins.str] = None,
        environment_variable: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CodebuildProjectEnvironmentEnvironmentVariable", typing.Dict[builtins.str, typing.Any]]]]] = None,
        image_pull_credentials_type: typing.Optional[builtins.str] = None,
        privileged_mode: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        registry_credential: typing.Optional[typing.Union["CodebuildProjectEnvironmentRegistryCredential", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param compute_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#compute_type CodebuildProject#compute_type}.
        :param image: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#image CodebuildProject#image}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.
        :param certificate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#certificate CodebuildProject#certificate}.
        :param environment_variable: environment_variable block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#environment_variable CodebuildProject#environment_variable}
        :param image_pull_credentials_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#image_pull_credentials_type CodebuildProject#image_pull_credentials_type}.
        :param privileged_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#privileged_mode CodebuildProject#privileged_mode}.
        :param registry_credential: registry_credential block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#registry_credential CodebuildProject#registry_credential}
        '''
        if isinstance(registry_credential, dict):
            registry_credential = CodebuildProjectEnvironmentRegistryCredential(**registry_credential)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19fb50fca1a236f58ca8396358c92e7ba56d70253a0e206b6160171938758234)
            check_type(argname="argument compute_type", value=compute_type, expected_type=type_hints["compute_type"])
            check_type(argname="argument image", value=image, expected_type=type_hints["image"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument environment_variable", value=environment_variable, expected_type=type_hints["environment_variable"])
            check_type(argname="argument image_pull_credentials_type", value=image_pull_credentials_type, expected_type=type_hints["image_pull_credentials_type"])
            check_type(argname="argument privileged_mode", value=privileged_mode, expected_type=type_hints["privileged_mode"])
            check_type(argname="argument registry_credential", value=registry_credential, expected_type=type_hints["registry_credential"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "compute_type": compute_type,
            "image": image,
            "type": type,
        }
        if certificate is not None:
            self._values["certificate"] = certificate
        if environment_variable is not None:
            self._values["environment_variable"] = environment_variable
        if image_pull_credentials_type is not None:
            self._values["image_pull_credentials_type"] = image_pull_credentials_type
        if privileged_mode is not None:
            self._values["privileged_mode"] = privileged_mode
        if registry_credential is not None:
            self._values["registry_credential"] = registry_credential

    @builtins.property
    def compute_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#compute_type CodebuildProject#compute_type}.'''
        result = self._values.get("compute_type")
        assert result is not None, "Required property 'compute_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def image(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#image CodebuildProject#image}.'''
        result = self._values.get("image")
        assert result is not None, "Required property 'image' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#certificate CodebuildProject#certificate}.'''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def environment_variable(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CodebuildProjectEnvironmentEnvironmentVariable"]]]:
        '''environment_variable block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#environment_variable CodebuildProject#environment_variable}
        '''
        result = self._values.get("environment_variable")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CodebuildProjectEnvironmentEnvironmentVariable"]]], result)

    @builtins.property
    def image_pull_credentials_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#image_pull_credentials_type CodebuildProject#image_pull_credentials_type}.'''
        result = self._values.get("image_pull_credentials_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def privileged_mode(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#privileged_mode CodebuildProject#privileged_mode}.'''
        result = self._values.get("privileged_mode")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def registry_credential(
        self,
    ) -> typing.Optional["CodebuildProjectEnvironmentRegistryCredential"]:
        '''registry_credential block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#registry_credential CodebuildProject#registry_credential}
        '''
        result = self._values.get("registry_credential")
        return typing.cast(typing.Optional["CodebuildProjectEnvironmentRegistryCredential"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodebuildProjectEnvironment(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.codebuildProject.CodebuildProjectEnvironmentEnvironmentVariable",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value", "type": "type"},
)
class CodebuildProjectEnvironmentEnvironmentVariable:
    def __init__(
        self,
        *,
        name: builtins.str,
        value: builtins.str,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#name CodebuildProject#name}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#value CodebuildProject#value}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a68cdbf22ece3f4b8a2f6328edc33e0e61b7d3dd9aa23147e2515ec4ea8c102c)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "value": value,
        }
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#name CodebuildProject#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#value CodebuildProject#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodebuildProjectEnvironmentEnvironmentVariable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodebuildProjectEnvironmentEnvironmentVariableList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codebuildProject.CodebuildProjectEnvironmentEnvironmentVariableList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__53261d72013217e3e3a8601ffe7dee10cd094633ff6874aa94971f50b24d50e4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CodebuildProjectEnvironmentEnvironmentVariableOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31a8832d4143563dd669900b02f01ecda057216c1c21a39181515e5d7eb28c0c)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CodebuildProjectEnvironmentEnvironmentVariableOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ee7d9f43695a323e953665d87c4f77a5e9b9b2ad20605b4a73a6c3c36d35528)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f2cc2571692a01db77baa4afc89a2663ef5ec421faf4696d91a633577ff90715)
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
            type_hints = typing.get_type_hints(_typecheckingstub__affa87a8966233f94bd86aba4b10868ae8a18789bd5281c7fab41fe62410c655)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodebuildProjectEnvironmentEnvironmentVariable]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodebuildProjectEnvironmentEnvironmentVariable]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodebuildProjectEnvironmentEnvironmentVariable]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b22d6b49ce9998fe7e5953a759435de07c2d6adaeb0b01de6f9016bc27338ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CodebuildProjectEnvironmentEnvironmentVariableOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codebuildProject.CodebuildProjectEnvironmentEnvironmentVariableOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c0dc8b2f60fa4d971e2a9a98d2aab4ccb80fd981c89a5d9922c0eeddc27df613)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7722319d2fb7061a6409ed98c9ecb0542ca817a67b4a5f9618fbb4515fc6110f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7254b287ee1e38acaedcd7f1adf6808de86db0ff690f8bdc292e98c68b63ca09)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__393351147cc3d91f893b877b998ca4523bcaa636646504cc12fc015407d4673e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CodebuildProjectEnvironmentEnvironmentVariable, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CodebuildProjectEnvironmentEnvironmentVariable, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CodebuildProjectEnvironmentEnvironmentVariable, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0959c04edcf6fd78af43c943cf3f537db4b68d242df2f712abb077c2aa960e24)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CodebuildProjectEnvironmentOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codebuildProject.CodebuildProjectEnvironmentOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__74660c6ab86ceae72a4f8866534e86ae4487557893283ef338315fe3f5ecaaef)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putEnvironmentVariable")
    def put_environment_variable(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CodebuildProjectEnvironmentEnvironmentVariable, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b800ee660cb832799efb6ebd2b487d5ded1fbe79be769bee5cf68b44aef32157)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEnvironmentVariable", [value]))

    @jsii.member(jsii_name="putRegistryCredential")
    def put_registry_credential(
        self,
        *,
        credential: builtins.str,
        credential_provider: builtins.str,
    ) -> None:
        '''
        :param credential: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#credential CodebuildProject#credential}.
        :param credential_provider: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#credential_provider CodebuildProject#credential_provider}.
        '''
        value = CodebuildProjectEnvironmentRegistryCredential(
            credential=credential, credential_provider=credential_provider
        )

        return typing.cast(None, jsii.invoke(self, "putRegistryCredential", [value]))

    @jsii.member(jsii_name="resetCertificate")
    def reset_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificate", []))

    @jsii.member(jsii_name="resetEnvironmentVariable")
    def reset_environment_variable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnvironmentVariable", []))

    @jsii.member(jsii_name="resetImagePullCredentialsType")
    def reset_image_pull_credentials_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImagePullCredentialsType", []))

    @jsii.member(jsii_name="resetPrivilegedMode")
    def reset_privileged_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivilegedMode", []))

    @jsii.member(jsii_name="resetRegistryCredential")
    def reset_registry_credential(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegistryCredential", []))

    @builtins.property
    @jsii.member(jsii_name="environmentVariable")
    def environment_variable(
        self,
    ) -> CodebuildProjectEnvironmentEnvironmentVariableList:
        return typing.cast(CodebuildProjectEnvironmentEnvironmentVariableList, jsii.get(self, "environmentVariable"))

    @builtins.property
    @jsii.member(jsii_name="registryCredential")
    def registry_credential(
        self,
    ) -> "CodebuildProjectEnvironmentRegistryCredentialOutputReference":
        return typing.cast("CodebuildProjectEnvironmentRegistryCredentialOutputReference", jsii.get(self, "registryCredential"))

    @builtins.property
    @jsii.member(jsii_name="certificateInput")
    def certificate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateInput"))

    @builtins.property
    @jsii.member(jsii_name="computeTypeInput")
    def compute_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "computeTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="environmentVariableInput")
    def environment_variable_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodebuildProjectEnvironmentEnvironmentVariable]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodebuildProjectEnvironmentEnvironmentVariable]]], jsii.get(self, "environmentVariableInput"))

    @builtins.property
    @jsii.member(jsii_name="imageInput")
    def image_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageInput"))

    @builtins.property
    @jsii.member(jsii_name="imagePullCredentialsTypeInput")
    def image_pull_credentials_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imagePullCredentialsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="privilegedModeInput")
    def privileged_mode_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "privilegedModeInput"))

    @builtins.property
    @jsii.member(jsii_name="registryCredentialInput")
    def registry_credential_input(
        self,
    ) -> typing.Optional["CodebuildProjectEnvironmentRegistryCredential"]:
        return typing.cast(typing.Optional["CodebuildProjectEnvironmentRegistryCredential"], jsii.get(self, "registryCredentialInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificate"))

    @certificate.setter
    def certificate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__235252b960458da7985b1c996ce2369e117bea9a4149db3d60c0717630149e79)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificate", value)

    @builtins.property
    @jsii.member(jsii_name="computeType")
    def compute_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "computeType"))

    @compute_type.setter
    def compute_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c1160921a51ec74dd7dec86d682dac9d5eca81f360c3976b236a57fb86cd702)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "computeType", value)

    @builtins.property
    @jsii.member(jsii_name="image")
    def image(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "image"))

    @image.setter
    def image(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__592c5926b3571bfa4449062b6ff6b98cf03d18fe0d03f0ecf089e38c8a9381a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "image", value)

    @builtins.property
    @jsii.member(jsii_name="imagePullCredentialsType")
    def image_pull_credentials_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imagePullCredentialsType"))

    @image_pull_credentials_type.setter
    def image_pull_credentials_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__971e2e11750c49ed5e68858284e993bf43411fbacb7d1ba9d523e2f146759860)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imagePullCredentialsType", value)

    @builtins.property
    @jsii.member(jsii_name="privilegedMode")
    def privileged_mode(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "privilegedMode"))

    @privileged_mode.setter
    def privileged_mode(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa51f9944429919f9562eef17eed92f720671a1144558a2b5c108a26e8b7531c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privilegedMode", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6c235e1a88993c5c05bf220d6a6f0a740d6ee66110761d9d871e641add80a26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CodebuildProjectEnvironment]:
        return typing.cast(typing.Optional[CodebuildProjectEnvironment], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodebuildProjectEnvironment],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34e2e7ec1c5632cf0a7861a49eafa6d911617bc46832d3f8f81de0e920eefdf6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.codebuildProject.CodebuildProjectEnvironmentRegistryCredential",
    jsii_struct_bases=[],
    name_mapping={
        "credential": "credential",
        "credential_provider": "credentialProvider",
    },
)
class CodebuildProjectEnvironmentRegistryCredential:
    def __init__(
        self,
        *,
        credential: builtins.str,
        credential_provider: builtins.str,
    ) -> None:
        '''
        :param credential: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#credential CodebuildProject#credential}.
        :param credential_provider: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#credential_provider CodebuildProject#credential_provider}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe2fe812b4f939198c427caa66c46f681d6f0e01a80a945c26fb3895e651007d)
            check_type(argname="argument credential", value=credential, expected_type=type_hints["credential"])
            check_type(argname="argument credential_provider", value=credential_provider, expected_type=type_hints["credential_provider"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "credential": credential,
            "credential_provider": credential_provider,
        }

    @builtins.property
    def credential(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#credential CodebuildProject#credential}.'''
        result = self._values.get("credential")
        assert result is not None, "Required property 'credential' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def credential_provider(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#credential_provider CodebuildProject#credential_provider}.'''
        result = self._values.get("credential_provider")
        assert result is not None, "Required property 'credential_provider' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodebuildProjectEnvironmentRegistryCredential(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodebuildProjectEnvironmentRegistryCredentialOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codebuildProject.CodebuildProjectEnvironmentRegistryCredentialOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__55af52e79631de187406956a1acf81b7e5862f09a03dc1bdb8ecbf08b6cfed1a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="credentialInput")
    def credential_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "credentialInput"))

    @builtins.property
    @jsii.member(jsii_name="credentialProviderInput")
    def credential_provider_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "credentialProviderInput"))

    @builtins.property
    @jsii.member(jsii_name="credential")
    def credential(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "credential"))

    @credential.setter
    def credential(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76ad118c488c290429b8eaf5cc7a0d5b796a08258570157a2e64120042a2bc2b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "credential", value)

    @builtins.property
    @jsii.member(jsii_name="credentialProvider")
    def credential_provider(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "credentialProvider"))

    @credential_provider.setter
    def credential_provider(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21bd4f1bffd8dadea62b6ead057f9bb214c071de18f76f594b713b3ce8f6369d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "credentialProvider", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CodebuildProjectEnvironmentRegistryCredential]:
        return typing.cast(typing.Optional[CodebuildProjectEnvironmentRegistryCredential], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodebuildProjectEnvironmentRegistryCredential],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5084cbef6ee4ca5af627d93f4a055740c821cd553355c84881637d6d3265a799)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.codebuildProject.CodebuildProjectFileSystemLocations",
    jsii_struct_bases=[],
    name_mapping={
        "identifier": "identifier",
        "location": "location",
        "mount_options": "mountOptions",
        "mount_point": "mountPoint",
        "type": "type",
    },
)
class CodebuildProjectFileSystemLocations:
    def __init__(
        self,
        *,
        identifier: typing.Optional[builtins.str] = None,
        location: typing.Optional[builtins.str] = None,
        mount_options: typing.Optional[builtins.str] = None,
        mount_point: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#identifier CodebuildProject#identifier}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#location CodebuildProject#location}.
        :param mount_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#mount_options CodebuildProject#mount_options}.
        :param mount_point: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#mount_point CodebuildProject#mount_point}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebca4b0a5936306cbfdbfb8786a8da00a13158ff509dd938db9e15bf18fc4693)
            check_type(argname="argument identifier", value=identifier, expected_type=type_hints["identifier"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument mount_options", value=mount_options, expected_type=type_hints["mount_options"])
            check_type(argname="argument mount_point", value=mount_point, expected_type=type_hints["mount_point"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if identifier is not None:
            self._values["identifier"] = identifier
        if location is not None:
            self._values["location"] = location
        if mount_options is not None:
            self._values["mount_options"] = mount_options
        if mount_point is not None:
            self._values["mount_point"] = mount_point
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def identifier(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#identifier CodebuildProject#identifier}.'''
        result = self._values.get("identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def location(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#location CodebuildProject#location}.'''
        result = self._values.get("location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mount_options(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#mount_options CodebuildProject#mount_options}.'''
        result = self._values.get("mount_options")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mount_point(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#mount_point CodebuildProject#mount_point}.'''
        result = self._values.get("mount_point")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodebuildProjectFileSystemLocations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodebuildProjectFileSystemLocationsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codebuildProject.CodebuildProjectFileSystemLocationsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__08c187f243974130f5c16c520be35e4184b1ce6b61a56214bae148eda6f151be)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CodebuildProjectFileSystemLocationsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66f64a3fef1f2cfa3c5447d60a93286e5e8a81e38513d7091de1e5eb09f1a1d8)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CodebuildProjectFileSystemLocationsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad447049b02297be1054a5bccd1349921d5525f4aa0c484360424dafa7e88947)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3ab04d01c39c9339d41560e4c621c095c4264d7940cda62909bbaf2157349f7e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8752898ee45dd9a971a9d66e8232bf83be73f7ddde2e1420b8f4ed478174e0bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodebuildProjectFileSystemLocations]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodebuildProjectFileSystemLocations]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodebuildProjectFileSystemLocations]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f2dde18028dda7ca34cb686235717e47879a42d9390558665f99e0f988dc1c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CodebuildProjectFileSystemLocationsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codebuildProject.CodebuildProjectFileSystemLocationsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3bd13a5c14646f442d2285a371d1ef33e2f3d3a657a11e153e95bc69950b6ad7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetIdentifier")
    def reset_identifier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentifier", []))

    @jsii.member(jsii_name="resetLocation")
    def reset_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocation", []))

    @jsii.member(jsii_name="resetMountOptions")
    def reset_mount_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMountOptions", []))

    @jsii.member(jsii_name="resetMountPoint")
    def reset_mount_point(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMountPoint", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="identifierInput")
    def identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identifierInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="mountOptionsInput")
    def mount_options_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mountOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="mountPointInput")
    def mount_point_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mountPointInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="identifier")
    def identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identifier"))

    @identifier.setter
    def identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f3d90e07257adb6104ec970b7ca1e2f09c9f2e7c850c7fc2965c341563e4936)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identifier", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__435d57a8ff849c3fce5eb9638c0f81f9c4719475b0213a8416b609c127738e8b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="mountOptions")
    def mount_options(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mountOptions"))

    @mount_options.setter
    def mount_options(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14946fc4c287c804255f76cad7d77c7c52f65c8d097df5ca7ab04220483a368b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mountOptions", value)

    @builtins.property
    @jsii.member(jsii_name="mountPoint")
    def mount_point(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mountPoint"))

    @mount_point.setter
    def mount_point(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03528b6e2b4dc009a6538d93a5f88f22e67fb97f017898b4e39a36e3a4c59a18)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mountPoint", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99e4840aba70fe49ab5895232b19bd536a6a71fad941fbc0a400820956d2a146)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CodebuildProjectFileSystemLocations, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CodebuildProjectFileSystemLocations, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CodebuildProjectFileSystemLocations, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91c28e36a2de34e46d0cec53bd706467f4a4deb2b2e43f7929c819eb2ead87d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.codebuildProject.CodebuildProjectLogsConfig",
    jsii_struct_bases=[],
    name_mapping={"cloudwatch_logs": "cloudwatchLogs", "s3_logs": "s3Logs"},
)
class CodebuildProjectLogsConfig:
    def __init__(
        self,
        *,
        cloudwatch_logs: typing.Optional[typing.Union["CodebuildProjectLogsConfigCloudwatchLogs", typing.Dict[builtins.str, typing.Any]]] = None,
        s3_logs: typing.Optional[typing.Union["CodebuildProjectLogsConfigS3Logs", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cloudwatch_logs: cloudwatch_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#cloudwatch_logs CodebuildProject#cloudwatch_logs}
        :param s3_logs: s3_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#s3_logs CodebuildProject#s3_logs}
        '''
        if isinstance(cloudwatch_logs, dict):
            cloudwatch_logs = CodebuildProjectLogsConfigCloudwatchLogs(**cloudwatch_logs)
        if isinstance(s3_logs, dict):
            s3_logs = CodebuildProjectLogsConfigS3Logs(**s3_logs)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3298be36907698b253abd89552ab434e461f9d7b144963ced98d2fad50dd5324)
            check_type(argname="argument cloudwatch_logs", value=cloudwatch_logs, expected_type=type_hints["cloudwatch_logs"])
            check_type(argname="argument s3_logs", value=s3_logs, expected_type=type_hints["s3_logs"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cloudwatch_logs is not None:
            self._values["cloudwatch_logs"] = cloudwatch_logs
        if s3_logs is not None:
            self._values["s3_logs"] = s3_logs

    @builtins.property
    def cloudwatch_logs(
        self,
    ) -> typing.Optional["CodebuildProjectLogsConfigCloudwatchLogs"]:
        '''cloudwatch_logs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#cloudwatch_logs CodebuildProject#cloudwatch_logs}
        '''
        result = self._values.get("cloudwatch_logs")
        return typing.cast(typing.Optional["CodebuildProjectLogsConfigCloudwatchLogs"], result)

    @builtins.property
    def s3_logs(self) -> typing.Optional["CodebuildProjectLogsConfigS3Logs"]:
        '''s3_logs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#s3_logs CodebuildProject#s3_logs}
        '''
        result = self._values.get("s3_logs")
        return typing.cast(typing.Optional["CodebuildProjectLogsConfigS3Logs"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodebuildProjectLogsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.codebuildProject.CodebuildProjectLogsConfigCloudwatchLogs",
    jsii_struct_bases=[],
    name_mapping={
        "group_name": "groupName",
        "status": "status",
        "stream_name": "streamName",
    },
)
class CodebuildProjectLogsConfigCloudwatchLogs:
    def __init__(
        self,
        *,
        group_name: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
        stream_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#group_name CodebuildProject#group_name}.
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#status CodebuildProject#status}.
        :param stream_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#stream_name CodebuildProject#stream_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__565e64ffe90856210d1875a81f2d87ad195335c4ecabf61ac35be6e1c8d1cede)
            check_type(argname="argument group_name", value=group_name, expected_type=type_hints["group_name"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument stream_name", value=stream_name, expected_type=type_hints["stream_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if group_name is not None:
            self._values["group_name"] = group_name
        if status is not None:
            self._values["status"] = status
        if stream_name is not None:
            self._values["stream_name"] = stream_name

    @builtins.property
    def group_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#group_name CodebuildProject#group_name}.'''
        result = self._values.get("group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#status CodebuildProject#status}.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def stream_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#stream_name CodebuildProject#stream_name}.'''
        result = self._values.get("stream_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodebuildProjectLogsConfigCloudwatchLogs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodebuildProjectLogsConfigCloudwatchLogsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codebuildProject.CodebuildProjectLogsConfigCloudwatchLogsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8e40839a9fe29a32c6e5ec7a0d5bddc2e8f2e463de7889e9f85f5733ec7b3bf4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetGroupName")
    def reset_group_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupName", []))

    @jsii.member(jsii_name="resetStatus")
    def reset_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatus", []))

    @jsii.member(jsii_name="resetStreamName")
    def reset_stream_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStreamName", []))

    @builtins.property
    @jsii.member(jsii_name="groupNameInput")
    def group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="streamNameInput")
    def stream_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "streamNameInput"))

    @builtins.property
    @jsii.member(jsii_name="groupName")
    def group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupName"))

    @group_name.setter
    def group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a848ae98d7b6de3df26b4afd2d5546f6dff977227f89b5f0203beb16dceb68b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupName", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b4e886647bbad21b10c273d2292bdd1951087a9c1c29b1a0b43a3a36877d96b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="streamName")
    def stream_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "streamName"))

    @stream_name.setter
    def stream_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c089a3b78152ee8d0981f75be5d3545958b14b24a3a1f23279a5fde3e57fbdb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streamName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CodebuildProjectLogsConfigCloudwatchLogs]:
        return typing.cast(typing.Optional[CodebuildProjectLogsConfigCloudwatchLogs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodebuildProjectLogsConfigCloudwatchLogs],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c337ab1f65cd4e0175e57fc1dce17da1eb4f0316bc52c7a0088a14032d99138)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CodebuildProjectLogsConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codebuildProject.CodebuildProjectLogsConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__febf357d7ec38164fbdfb82ba8e4d9f111c058ccf5d84b0c13b3dd9b720f11b2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCloudwatchLogs")
    def put_cloudwatch_logs(
        self,
        *,
        group_name: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
        stream_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#group_name CodebuildProject#group_name}.
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#status CodebuildProject#status}.
        :param stream_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#stream_name CodebuildProject#stream_name}.
        '''
        value = CodebuildProjectLogsConfigCloudwatchLogs(
            group_name=group_name, status=status, stream_name=stream_name
        )

        return typing.cast(None, jsii.invoke(self, "putCloudwatchLogs", [value]))

    @jsii.member(jsii_name="putS3Logs")
    def put_s3_logs(
        self,
        *,
        bucket_owner_access: typing.Optional[builtins.str] = None,
        encryption_disabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        location: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_owner_access: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#bucket_owner_access CodebuildProject#bucket_owner_access}.
        :param encryption_disabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#encryption_disabled CodebuildProject#encryption_disabled}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#location CodebuildProject#location}.
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#status CodebuildProject#status}.
        '''
        value = CodebuildProjectLogsConfigS3Logs(
            bucket_owner_access=bucket_owner_access,
            encryption_disabled=encryption_disabled,
            location=location,
            status=status,
        )

        return typing.cast(None, jsii.invoke(self, "putS3Logs", [value]))

    @jsii.member(jsii_name="resetCloudwatchLogs")
    def reset_cloudwatch_logs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudwatchLogs", []))

    @jsii.member(jsii_name="resetS3Logs")
    def reset_s3_logs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3Logs", []))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLogs")
    def cloudwatch_logs(
        self,
    ) -> CodebuildProjectLogsConfigCloudwatchLogsOutputReference:
        return typing.cast(CodebuildProjectLogsConfigCloudwatchLogsOutputReference, jsii.get(self, "cloudwatchLogs"))

    @builtins.property
    @jsii.member(jsii_name="s3Logs")
    def s3_logs(self) -> "CodebuildProjectLogsConfigS3LogsOutputReference":
        return typing.cast("CodebuildProjectLogsConfigS3LogsOutputReference", jsii.get(self, "s3Logs"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLogsInput")
    def cloudwatch_logs_input(
        self,
    ) -> typing.Optional[CodebuildProjectLogsConfigCloudwatchLogs]:
        return typing.cast(typing.Optional[CodebuildProjectLogsConfigCloudwatchLogs], jsii.get(self, "cloudwatchLogsInput"))

    @builtins.property
    @jsii.member(jsii_name="s3LogsInput")
    def s3_logs_input(self) -> typing.Optional["CodebuildProjectLogsConfigS3Logs"]:
        return typing.cast(typing.Optional["CodebuildProjectLogsConfigS3Logs"], jsii.get(self, "s3LogsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CodebuildProjectLogsConfig]:
        return typing.cast(typing.Optional[CodebuildProjectLogsConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodebuildProjectLogsConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ebf12fbe4331b0666169d191111b6624e6f8075246ed244d46144ad7908708c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.codebuildProject.CodebuildProjectLogsConfigS3Logs",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_owner_access": "bucketOwnerAccess",
        "encryption_disabled": "encryptionDisabled",
        "location": "location",
        "status": "status",
    },
)
class CodebuildProjectLogsConfigS3Logs:
    def __init__(
        self,
        *,
        bucket_owner_access: typing.Optional[builtins.str] = None,
        encryption_disabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        location: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_owner_access: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#bucket_owner_access CodebuildProject#bucket_owner_access}.
        :param encryption_disabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#encryption_disabled CodebuildProject#encryption_disabled}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#location CodebuildProject#location}.
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#status CodebuildProject#status}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c6f70aeed22b54f37a167d5b8043e7c8e7ff71f09f29c4a25501ad1b8e0bc90)
            check_type(argname="argument bucket_owner_access", value=bucket_owner_access, expected_type=type_hints["bucket_owner_access"])
            check_type(argname="argument encryption_disabled", value=encryption_disabled, expected_type=type_hints["encryption_disabled"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if bucket_owner_access is not None:
            self._values["bucket_owner_access"] = bucket_owner_access
        if encryption_disabled is not None:
            self._values["encryption_disabled"] = encryption_disabled
        if location is not None:
            self._values["location"] = location
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def bucket_owner_access(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#bucket_owner_access CodebuildProject#bucket_owner_access}.'''
        result = self._values.get("bucket_owner_access")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#encryption_disabled CodebuildProject#encryption_disabled}.'''
        result = self._values.get("encryption_disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def location(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#location CodebuildProject#location}.'''
        result = self._values.get("location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#status CodebuildProject#status}.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodebuildProjectLogsConfigS3Logs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodebuildProjectLogsConfigS3LogsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codebuildProject.CodebuildProjectLogsConfigS3LogsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b1745947f8f00c46f45bc26768373d39e2f5de618294f1a51cb7d02498517824)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBucketOwnerAccess")
    def reset_bucket_owner_access(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketOwnerAccess", []))

    @jsii.member(jsii_name="resetEncryptionDisabled")
    def reset_encryption_disabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionDisabled", []))

    @jsii.member(jsii_name="resetLocation")
    def reset_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocation", []))

    @jsii.member(jsii_name="resetStatus")
    def reset_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatus", []))

    @builtins.property
    @jsii.member(jsii_name="bucketOwnerAccessInput")
    def bucket_owner_access_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketOwnerAccessInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionDisabledInput")
    def encryption_disabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "encryptionDisabledInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketOwnerAccess")
    def bucket_owner_access(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketOwnerAccess"))

    @bucket_owner_access.setter
    def bucket_owner_access(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2462080e67f31fa7a3864f728165734a849c35ca7416fe288439800adca208e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketOwnerAccess", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionDisabled")
    def encryption_disabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "encryptionDisabled"))

    @encryption_disabled.setter
    def encryption_disabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aff75b31d135dd0b1f250a1775fa16cf77b6b9a6d57062cc3769085462ec12d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionDisabled", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a89ffde9a0e7036052acfa55501d8328c67d72167966321910b6aea079d6766)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ae77895d9d675894d7e14751e2a8757429dff6a3d53fa4ec806c143806ccee0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CodebuildProjectLogsConfigS3Logs]:
        return typing.cast(typing.Optional[CodebuildProjectLogsConfigS3Logs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodebuildProjectLogsConfigS3Logs],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__787d947a3f5f806eeec5d6fa71389b30d48f658ab6fba0127ad58ebeb7ac4cb8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.codebuildProject.CodebuildProjectSecondaryArtifacts",
    jsii_struct_bases=[],
    name_mapping={
        "artifact_identifier": "artifactIdentifier",
        "type": "type",
        "bucket_owner_access": "bucketOwnerAccess",
        "encryption_disabled": "encryptionDisabled",
        "location": "location",
        "name": "name",
        "namespace_type": "namespaceType",
        "override_artifact_name": "overrideArtifactName",
        "packaging": "packaging",
        "path": "path",
    },
)
class CodebuildProjectSecondaryArtifacts:
    def __init__(
        self,
        *,
        artifact_identifier: builtins.str,
        type: builtins.str,
        bucket_owner_access: typing.Optional[builtins.str] = None,
        encryption_disabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        location: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        namespace_type: typing.Optional[builtins.str] = None,
        override_artifact_name: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        packaging: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param artifact_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#artifact_identifier CodebuildProject#artifact_identifier}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.
        :param bucket_owner_access: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#bucket_owner_access CodebuildProject#bucket_owner_access}.
        :param encryption_disabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#encryption_disabled CodebuildProject#encryption_disabled}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#location CodebuildProject#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#name CodebuildProject#name}.
        :param namespace_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#namespace_type CodebuildProject#namespace_type}.
        :param override_artifact_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#override_artifact_name CodebuildProject#override_artifact_name}.
        :param packaging: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#packaging CodebuildProject#packaging}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#path CodebuildProject#path}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f987c5241c6571ab9d4c7e02991fcca69ced951ba7f4f941adcb799e5d9e7740)
            check_type(argname="argument artifact_identifier", value=artifact_identifier, expected_type=type_hints["artifact_identifier"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument bucket_owner_access", value=bucket_owner_access, expected_type=type_hints["bucket_owner_access"])
            check_type(argname="argument encryption_disabled", value=encryption_disabled, expected_type=type_hints["encryption_disabled"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace_type", value=namespace_type, expected_type=type_hints["namespace_type"])
            check_type(argname="argument override_artifact_name", value=override_artifact_name, expected_type=type_hints["override_artifact_name"])
            check_type(argname="argument packaging", value=packaging, expected_type=type_hints["packaging"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "artifact_identifier": artifact_identifier,
            "type": type,
        }
        if bucket_owner_access is not None:
            self._values["bucket_owner_access"] = bucket_owner_access
        if encryption_disabled is not None:
            self._values["encryption_disabled"] = encryption_disabled
        if location is not None:
            self._values["location"] = location
        if name is not None:
            self._values["name"] = name
        if namespace_type is not None:
            self._values["namespace_type"] = namespace_type
        if override_artifact_name is not None:
            self._values["override_artifact_name"] = override_artifact_name
        if packaging is not None:
            self._values["packaging"] = packaging
        if path is not None:
            self._values["path"] = path

    @builtins.property
    def artifact_identifier(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#artifact_identifier CodebuildProject#artifact_identifier}.'''
        result = self._values.get("artifact_identifier")
        assert result is not None, "Required property 'artifact_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bucket_owner_access(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#bucket_owner_access CodebuildProject#bucket_owner_access}.'''
        result = self._values.get("bucket_owner_access")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#encryption_disabled CodebuildProject#encryption_disabled}.'''
        result = self._values.get("encryption_disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def location(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#location CodebuildProject#location}.'''
        result = self._values.get("location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#name CodebuildProject#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#namespace_type CodebuildProject#namespace_type}.'''
        result = self._values.get("namespace_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def override_artifact_name(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#override_artifact_name CodebuildProject#override_artifact_name}.'''
        result = self._values.get("override_artifact_name")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def packaging(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#packaging CodebuildProject#packaging}.'''
        result = self._values.get("packaging")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#path CodebuildProject#path}.'''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodebuildProjectSecondaryArtifacts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodebuildProjectSecondaryArtifactsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codebuildProject.CodebuildProjectSecondaryArtifactsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__839a628c4c3409baf9532bfe061ca1ee8b6c16b6626ca679ae40348547f2fb2b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CodebuildProjectSecondaryArtifactsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d858705ff18ed21800ba77d0ea7edd4e20d8f4624edf6c0e1bbff533ab8b9fbb)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CodebuildProjectSecondaryArtifactsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d9701bb33f24f0d5142b2c828759f758a84b176ac5dafd3e69ded7939ca1d75)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d5617527e503c4f23beb8c308c6b3113de4ade100189eec5ae4ed37df11c1fc2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f5abe30f2cc79fe49e9ba2cc28311b8689c2f3cb95a696c3c5dcfb1b7b851514)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodebuildProjectSecondaryArtifacts]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodebuildProjectSecondaryArtifacts]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodebuildProjectSecondaryArtifacts]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09581ed2d497a52375de375df6b67857a94341cbf0dd4d167b8f6cd1a946bd70)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CodebuildProjectSecondaryArtifactsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codebuildProject.CodebuildProjectSecondaryArtifactsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e1799beaf56b40a9adf2940fde7ded17636f0f76f5b24039aadb14497477e318)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetBucketOwnerAccess")
    def reset_bucket_owner_access(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketOwnerAccess", []))

    @jsii.member(jsii_name="resetEncryptionDisabled")
    def reset_encryption_disabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionDisabled", []))

    @jsii.member(jsii_name="resetLocation")
    def reset_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocation", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamespaceType")
    def reset_namespace_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespaceType", []))

    @jsii.member(jsii_name="resetOverrideArtifactName")
    def reset_override_artifact_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOverrideArtifactName", []))

    @jsii.member(jsii_name="resetPackaging")
    def reset_packaging(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPackaging", []))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @builtins.property
    @jsii.member(jsii_name="artifactIdentifierInput")
    def artifact_identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "artifactIdentifierInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketOwnerAccessInput")
    def bucket_owner_access_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketOwnerAccessInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionDisabledInput")
    def encryption_disabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "encryptionDisabledInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceTypeInput")
    def namespace_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="overrideArtifactNameInput")
    def override_artifact_name_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "overrideArtifactNameInput"))

    @builtins.property
    @jsii.member(jsii_name="packagingInput")
    def packaging_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "packagingInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="artifactIdentifier")
    def artifact_identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "artifactIdentifier"))

    @artifact_identifier.setter
    def artifact_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4e9a8219f409a30f6ba216e0c4f23dcf14323f0add3e89cb44e11e8d1d4c632)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "artifactIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="bucketOwnerAccess")
    def bucket_owner_access(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketOwnerAccess"))

    @bucket_owner_access.setter
    def bucket_owner_access(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e5771128844dded2ee2efed27bf126156d4a3364d3f9bc2d26c9dedba4ce573)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketOwnerAccess", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionDisabled")
    def encryption_disabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "encryptionDisabled"))

    @encryption_disabled.setter
    def encryption_disabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61c98d34aee87ddff9b2d8800904db7c390e3720918c3ef7462877b71797a7bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionDisabled", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fd4bdfc37601882beb466b6c546b0d02156e43dc5cdec4d05e0f11e75a74a55)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf2f35be6b4cd6b2a088d42b03c22401bef592f97fa3ccae73cd21b7de33520e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespaceType")
    def namespace_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespaceType"))

    @namespace_type.setter
    def namespace_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e42d92d358429681261c4129164e99dc210d43cb5f74f8172ffc6b262dbd8867)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespaceType", value)

    @builtins.property
    @jsii.member(jsii_name="overrideArtifactName")
    def override_artifact_name(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "overrideArtifactName"))

    @override_artifact_name.setter
    def override_artifact_name(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c5a66ab5839f7038c25d250dc56c12cc4e568a5517c501ffc1908b5e7aa8c31)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "overrideArtifactName", value)

    @builtins.property
    @jsii.member(jsii_name="packaging")
    def packaging(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "packaging"))

    @packaging.setter
    def packaging(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83a63a9bb77781ae1082d0655903347aeb36846fe0285bf3ac8959ff23ab0f38)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "packaging", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47ca6433faa82c69f5a4dc3d1db2e8f0a8089e090d34153615c749e9d24b9c0d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__550eb9d7eca2e0b319755362baeeb97a396259a9f9c2c464f19f91693e40aa38)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CodebuildProjectSecondaryArtifacts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CodebuildProjectSecondaryArtifacts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CodebuildProjectSecondaryArtifacts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49dda78950291def4932959acfa8e5cc2faaf42c814b352826c26ae466e008fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.codebuildProject.CodebuildProjectSecondarySourceVersion",
    jsii_struct_bases=[],
    name_mapping={
        "source_identifier": "sourceIdentifier",
        "source_version": "sourceVersion",
    },
)
class CodebuildProjectSecondarySourceVersion:
    def __init__(
        self,
        *,
        source_identifier: builtins.str,
        source_version: builtins.str,
    ) -> None:
        '''
        :param source_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#source_identifier CodebuildProject#source_identifier}.
        :param source_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#source_version CodebuildProject#source_version}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9ebc035899d8897beb2832efcb59a738a41bac1808a51e93bffe4cca513304e)
            check_type(argname="argument source_identifier", value=source_identifier, expected_type=type_hints["source_identifier"])
            check_type(argname="argument source_version", value=source_version, expected_type=type_hints["source_version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "source_identifier": source_identifier,
            "source_version": source_version,
        }

    @builtins.property
    def source_identifier(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#source_identifier CodebuildProject#source_identifier}.'''
        result = self._values.get("source_identifier")
        assert result is not None, "Required property 'source_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#source_version CodebuildProject#source_version}.'''
        result = self._values.get("source_version")
        assert result is not None, "Required property 'source_version' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodebuildProjectSecondarySourceVersion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodebuildProjectSecondarySourceVersionList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codebuildProject.CodebuildProjectSecondarySourceVersionList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__040e45ba67fbbfd66c76aa1588eece65f11bdd99faef18934d1601acec5298a3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CodebuildProjectSecondarySourceVersionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31f09cbb5a0af1ece1d857508f2bcb7e977ec141e98664694b9340d985082793)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CodebuildProjectSecondarySourceVersionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__859e07d82f148162ac051cfa9fa5d752a2a156175e497e100a3c441ede50a8f3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__37f6757615dc44ce11722a392c0a85d3d41a3ff60ef1879d35eb6499c0ad239e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b12cf7a0cf0a3bb03a1d66b41a5a7c1057fc024531ed8be70c37c15901259f54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodebuildProjectSecondarySourceVersion]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodebuildProjectSecondarySourceVersion]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodebuildProjectSecondarySourceVersion]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf61b1eb1c9b559e147d0b0957ef8ba8e51bc72defe7e238425c3bf435f56bf4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CodebuildProjectSecondarySourceVersionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codebuildProject.CodebuildProjectSecondarySourceVersionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6c512f814c161dea487cc08dcde68118e37c14585acd711dd193f1a18fc94756)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="sourceIdentifierInput")
    def source_identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceIdentifierInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceVersionInput")
    def source_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceIdentifier")
    def source_identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceIdentifier"))

    @source_identifier.setter
    def source_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0e2c217e586803ae462c8f957dfb9dac1d8f2de4784032abe8458a03528b06e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="sourceVersion")
    def source_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceVersion"))

    @source_version.setter
    def source_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__182e3f87dc83131da4282de5a83a6d2f9451d17a3f21020daa900d837717ee90)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceVersion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CodebuildProjectSecondarySourceVersion, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CodebuildProjectSecondarySourceVersion, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CodebuildProjectSecondarySourceVersion, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0580ec54b33af58252f2cc095672ac5d0849e7513746bb1ad50916e06a1ac65b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.codebuildProject.CodebuildProjectSecondarySources",
    jsii_struct_bases=[],
    name_mapping={
        "source_identifier": "sourceIdentifier",
        "type": "type",
        "auth": "auth",
        "buildspec": "buildspec",
        "build_status_config": "buildStatusConfig",
        "git_clone_depth": "gitCloneDepth",
        "git_submodules_config": "gitSubmodulesConfig",
        "insecure_ssl": "insecureSsl",
        "location": "location",
        "report_build_status": "reportBuildStatus",
    },
)
class CodebuildProjectSecondarySources:
    def __init__(
        self,
        *,
        source_identifier: builtins.str,
        type: builtins.str,
        auth: typing.Optional[typing.Union["CodebuildProjectSecondarySourcesAuth", typing.Dict[builtins.str, typing.Any]]] = None,
        buildspec: typing.Optional[builtins.str] = None,
        build_status_config: typing.Optional[typing.Union["CodebuildProjectSecondarySourcesBuildStatusConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        git_clone_depth: typing.Optional[jsii.Number] = None,
        git_submodules_config: typing.Optional[typing.Union["CodebuildProjectSecondarySourcesGitSubmodulesConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        insecure_ssl: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        location: typing.Optional[builtins.str] = None,
        report_build_status: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param source_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#source_identifier CodebuildProject#source_identifier}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.
        :param auth: auth block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#auth CodebuildProject#auth}
        :param buildspec: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#buildspec CodebuildProject#buildspec}.
        :param build_status_config: build_status_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#build_status_config CodebuildProject#build_status_config}
        :param git_clone_depth: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#git_clone_depth CodebuildProject#git_clone_depth}.
        :param git_submodules_config: git_submodules_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#git_submodules_config CodebuildProject#git_submodules_config}
        :param insecure_ssl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#insecure_ssl CodebuildProject#insecure_ssl}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#location CodebuildProject#location}.
        :param report_build_status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#report_build_status CodebuildProject#report_build_status}.
        '''
        if isinstance(auth, dict):
            auth = CodebuildProjectSecondarySourcesAuth(**auth)
        if isinstance(build_status_config, dict):
            build_status_config = CodebuildProjectSecondarySourcesBuildStatusConfig(**build_status_config)
        if isinstance(git_submodules_config, dict):
            git_submodules_config = CodebuildProjectSecondarySourcesGitSubmodulesConfig(**git_submodules_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c83c4e11d3ecb49123dd2093ab8db085b9477b4744aaa9aab1560ee0c2ee1fc8)
            check_type(argname="argument source_identifier", value=source_identifier, expected_type=type_hints["source_identifier"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument auth", value=auth, expected_type=type_hints["auth"])
            check_type(argname="argument buildspec", value=buildspec, expected_type=type_hints["buildspec"])
            check_type(argname="argument build_status_config", value=build_status_config, expected_type=type_hints["build_status_config"])
            check_type(argname="argument git_clone_depth", value=git_clone_depth, expected_type=type_hints["git_clone_depth"])
            check_type(argname="argument git_submodules_config", value=git_submodules_config, expected_type=type_hints["git_submodules_config"])
            check_type(argname="argument insecure_ssl", value=insecure_ssl, expected_type=type_hints["insecure_ssl"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument report_build_status", value=report_build_status, expected_type=type_hints["report_build_status"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "source_identifier": source_identifier,
            "type": type,
        }
        if auth is not None:
            self._values["auth"] = auth
        if buildspec is not None:
            self._values["buildspec"] = buildspec
        if build_status_config is not None:
            self._values["build_status_config"] = build_status_config
        if git_clone_depth is not None:
            self._values["git_clone_depth"] = git_clone_depth
        if git_submodules_config is not None:
            self._values["git_submodules_config"] = git_submodules_config
        if insecure_ssl is not None:
            self._values["insecure_ssl"] = insecure_ssl
        if location is not None:
            self._values["location"] = location
        if report_build_status is not None:
            self._values["report_build_status"] = report_build_status

    @builtins.property
    def source_identifier(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#source_identifier CodebuildProject#source_identifier}.'''
        result = self._values.get("source_identifier")
        assert result is not None, "Required property 'source_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auth(self) -> typing.Optional["CodebuildProjectSecondarySourcesAuth"]:
        '''auth block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#auth CodebuildProject#auth}
        '''
        result = self._values.get("auth")
        return typing.cast(typing.Optional["CodebuildProjectSecondarySourcesAuth"], result)

    @builtins.property
    def buildspec(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#buildspec CodebuildProject#buildspec}.'''
        result = self._values.get("buildspec")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def build_status_config(
        self,
    ) -> typing.Optional["CodebuildProjectSecondarySourcesBuildStatusConfig"]:
        '''build_status_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#build_status_config CodebuildProject#build_status_config}
        '''
        result = self._values.get("build_status_config")
        return typing.cast(typing.Optional["CodebuildProjectSecondarySourcesBuildStatusConfig"], result)

    @builtins.property
    def git_clone_depth(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#git_clone_depth CodebuildProject#git_clone_depth}.'''
        result = self._values.get("git_clone_depth")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def git_submodules_config(
        self,
    ) -> typing.Optional["CodebuildProjectSecondarySourcesGitSubmodulesConfig"]:
        '''git_submodules_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#git_submodules_config CodebuildProject#git_submodules_config}
        '''
        result = self._values.get("git_submodules_config")
        return typing.cast(typing.Optional["CodebuildProjectSecondarySourcesGitSubmodulesConfig"], result)

    @builtins.property
    def insecure_ssl(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#insecure_ssl CodebuildProject#insecure_ssl}.'''
        result = self._values.get("insecure_ssl")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def location(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#location CodebuildProject#location}.'''
        result = self._values.get("location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def report_build_status(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#report_build_status CodebuildProject#report_build_status}.'''
        result = self._values.get("report_build_status")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodebuildProjectSecondarySources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.codebuildProject.CodebuildProjectSecondarySourcesAuth",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "resource": "resource"},
)
class CodebuildProjectSecondarySourcesAuth:
    def __init__(
        self,
        *,
        type: builtins.str,
        resource: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.
        :param resource: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#resource CodebuildProject#resource}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb7b241095fc754af7eff0929baece76a3356e8f14840e1d31a3a43748e53cf7)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if resource is not None:
            self._values["resource"] = resource

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#resource CodebuildProject#resource}.'''
        result = self._values.get("resource")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodebuildProjectSecondarySourcesAuth(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodebuildProjectSecondarySourcesAuthOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codebuildProject.CodebuildProjectSecondarySourcesAuthOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__18980cf6ebd3e4375d2ced0eb7a3b188e4df7355bdc62eb41e09c536e399b7f1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetResource")
    def reset_resource(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResource", []))

    @builtins.property
    @jsii.member(jsii_name="resourceInput")
    def resource_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="resource")
    def resource(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resource"))

    @resource.setter
    def resource(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5cb5c3f79580cd73e5879c69821d1de2d37dc4c289685982fbd6936e5fb37454)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resource", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a688d0a24a2c7286d5207ce420c54ad9105c97c5594981df275036452d61cf14)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CodebuildProjectSecondarySourcesAuth]:
        return typing.cast(typing.Optional[CodebuildProjectSecondarySourcesAuth], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodebuildProjectSecondarySourcesAuth],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d66f4b8c7c25af113b0f666df3097afb5f18fec104475ddd8026386606aa19a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.codebuildProject.CodebuildProjectSecondarySourcesBuildStatusConfig",
    jsii_struct_bases=[],
    name_mapping={"context": "context", "target_url": "targetUrl"},
)
class CodebuildProjectSecondarySourcesBuildStatusConfig:
    def __init__(
        self,
        *,
        context: typing.Optional[builtins.str] = None,
        target_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param context: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#context CodebuildProject#context}.
        :param target_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#target_url CodebuildProject#target_url}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6fc0c33b318e375edd8620581ccde038c98778dc3c3c51c80881d6d0d499ab96)
            check_type(argname="argument context", value=context, expected_type=type_hints["context"])
            check_type(argname="argument target_url", value=target_url, expected_type=type_hints["target_url"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if context is not None:
            self._values["context"] = context
        if target_url is not None:
            self._values["target_url"] = target_url

    @builtins.property
    def context(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#context CodebuildProject#context}.'''
        result = self._values.get("context")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#target_url CodebuildProject#target_url}.'''
        result = self._values.get("target_url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodebuildProjectSecondarySourcesBuildStatusConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodebuildProjectSecondarySourcesBuildStatusConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codebuildProject.CodebuildProjectSecondarySourcesBuildStatusConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a88ce5e5f51f1a2cfc3951270b5c902f599d90517d9047e33f14db40cf530d7b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetContext")
    def reset_context(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContext", []))

    @jsii.member(jsii_name="resetTargetUrl")
    def reset_target_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetUrl", []))

    @builtins.property
    @jsii.member(jsii_name="contextInput")
    def context_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contextInput"))

    @builtins.property
    @jsii.member(jsii_name="targetUrlInput")
    def target_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="context")
    def context(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "context"))

    @context.setter
    def context(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__edeb15ce721f2c0af27d3659393289b931fb1fc2594b6ce574a5794c3744b9a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "context", value)

    @builtins.property
    @jsii.member(jsii_name="targetUrl")
    def target_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetUrl"))

    @target_url.setter
    def target_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b212e830eda26bedd21b5e70d7a2189ee5963bac90621362c3cf6da24b05b7c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CodebuildProjectSecondarySourcesBuildStatusConfig]:
        return typing.cast(typing.Optional[CodebuildProjectSecondarySourcesBuildStatusConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodebuildProjectSecondarySourcesBuildStatusConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3270a75db0d5842b056e483f08ceea969a46dbfce32c40eea3475b7edb9cf320)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.codebuildProject.CodebuildProjectSecondarySourcesGitSubmodulesConfig",
    jsii_struct_bases=[],
    name_mapping={"fetch_submodules": "fetchSubmodules"},
)
class CodebuildProjectSecondarySourcesGitSubmodulesConfig:
    def __init__(
        self,
        *,
        fetch_submodules: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param fetch_submodules: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#fetch_submodules CodebuildProject#fetch_submodules}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3d96d4b34f11358ba4f6b1a3d0bec17b745dff95f998496ff4ba41fc7b12fe7)
            check_type(argname="argument fetch_submodules", value=fetch_submodules, expected_type=type_hints["fetch_submodules"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "fetch_submodules": fetch_submodules,
        }

    @builtins.property
    def fetch_submodules(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#fetch_submodules CodebuildProject#fetch_submodules}.'''
        result = self._values.get("fetch_submodules")
        assert result is not None, "Required property 'fetch_submodules' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodebuildProjectSecondarySourcesGitSubmodulesConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodebuildProjectSecondarySourcesGitSubmodulesConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codebuildProject.CodebuildProjectSecondarySourcesGitSubmodulesConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b50ff1fad7f338c4cbd906427eadcf33adf44595d336d6aeb48ad52ebd6abaae)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="fetchSubmodulesInput")
    def fetch_submodules_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "fetchSubmodulesInput"))

    @builtins.property
    @jsii.member(jsii_name="fetchSubmodules")
    def fetch_submodules(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "fetchSubmodules"))

    @fetch_submodules.setter
    def fetch_submodules(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b8f9227233e82302b93a2cd3bca3252e9bee012af007ca01bba6fab638d0d54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fetchSubmodules", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CodebuildProjectSecondarySourcesGitSubmodulesConfig]:
        return typing.cast(typing.Optional[CodebuildProjectSecondarySourcesGitSubmodulesConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodebuildProjectSecondarySourcesGitSubmodulesConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21e7bbba353403a082983c2958f6c1643bfb9b73fe3f503aea0bcf49e46ddd9a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CodebuildProjectSecondarySourcesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codebuildProject.CodebuildProjectSecondarySourcesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b44ac4bac2372aa81592bba1795008c459b577bc8c63eec318c0f0222ea54cb8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CodebuildProjectSecondarySourcesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5540ab4d8a39720b93b0d32d58f5c6ebbfc9f7dff157e1c92e355c7590629e95)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CodebuildProjectSecondarySourcesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09e4a35ec878faeadfb373701ef6487f2abad676d948492c2380e6fda2e81217)
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
            type_hints = typing.get_type_hints(_typecheckingstub__73d81ffe6da98c54600401ac31cb7eebd486e2585229d61c58591148efc2fe1f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e2f1c98656bc0dc2827f88a44eb51464d3768caa4456f610f49afd3aafe25cd4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodebuildProjectSecondarySources]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodebuildProjectSecondarySources]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodebuildProjectSecondarySources]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3158bb315c631a8420dc3b26a472f8930ea126d4929ae0a5082409b82ec6b5f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CodebuildProjectSecondarySourcesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codebuildProject.CodebuildProjectSecondarySourcesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__940d01beaf6408f2a4f79c72c572691f32a368ff0dfcb7191639256c35e2d881)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAuth")
    def put_auth(
        self,
        *,
        type: builtins.str,
        resource: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.
        :param resource: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#resource CodebuildProject#resource}.
        '''
        value = CodebuildProjectSecondarySourcesAuth(type=type, resource=resource)

        return typing.cast(None, jsii.invoke(self, "putAuth", [value]))

    @jsii.member(jsii_name="putBuildStatusConfig")
    def put_build_status_config(
        self,
        *,
        context: typing.Optional[builtins.str] = None,
        target_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param context: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#context CodebuildProject#context}.
        :param target_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#target_url CodebuildProject#target_url}.
        '''
        value = CodebuildProjectSecondarySourcesBuildStatusConfig(
            context=context, target_url=target_url
        )

        return typing.cast(None, jsii.invoke(self, "putBuildStatusConfig", [value]))

    @jsii.member(jsii_name="putGitSubmodulesConfig")
    def put_git_submodules_config(
        self,
        *,
        fetch_submodules: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param fetch_submodules: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#fetch_submodules CodebuildProject#fetch_submodules}.
        '''
        value = CodebuildProjectSecondarySourcesGitSubmodulesConfig(
            fetch_submodules=fetch_submodules
        )

        return typing.cast(None, jsii.invoke(self, "putGitSubmodulesConfig", [value]))

    @jsii.member(jsii_name="resetAuth")
    def reset_auth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuth", []))

    @jsii.member(jsii_name="resetBuildspec")
    def reset_buildspec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBuildspec", []))

    @jsii.member(jsii_name="resetBuildStatusConfig")
    def reset_build_status_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBuildStatusConfig", []))

    @jsii.member(jsii_name="resetGitCloneDepth")
    def reset_git_clone_depth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGitCloneDepth", []))

    @jsii.member(jsii_name="resetGitSubmodulesConfig")
    def reset_git_submodules_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGitSubmodulesConfig", []))

    @jsii.member(jsii_name="resetInsecureSsl")
    def reset_insecure_ssl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInsecureSsl", []))

    @jsii.member(jsii_name="resetLocation")
    def reset_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocation", []))

    @jsii.member(jsii_name="resetReportBuildStatus")
    def reset_report_build_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReportBuildStatus", []))

    @builtins.property
    @jsii.member(jsii_name="auth")
    def auth(self) -> CodebuildProjectSecondarySourcesAuthOutputReference:
        return typing.cast(CodebuildProjectSecondarySourcesAuthOutputReference, jsii.get(self, "auth"))

    @builtins.property
    @jsii.member(jsii_name="buildStatusConfig")
    def build_status_config(
        self,
    ) -> CodebuildProjectSecondarySourcesBuildStatusConfigOutputReference:
        return typing.cast(CodebuildProjectSecondarySourcesBuildStatusConfigOutputReference, jsii.get(self, "buildStatusConfig"))

    @builtins.property
    @jsii.member(jsii_name="gitSubmodulesConfig")
    def git_submodules_config(
        self,
    ) -> CodebuildProjectSecondarySourcesGitSubmodulesConfigOutputReference:
        return typing.cast(CodebuildProjectSecondarySourcesGitSubmodulesConfigOutputReference, jsii.get(self, "gitSubmodulesConfig"))

    @builtins.property
    @jsii.member(jsii_name="authInput")
    def auth_input(self) -> typing.Optional[CodebuildProjectSecondarySourcesAuth]:
        return typing.cast(typing.Optional[CodebuildProjectSecondarySourcesAuth], jsii.get(self, "authInput"))

    @builtins.property
    @jsii.member(jsii_name="buildspecInput")
    def buildspec_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "buildspecInput"))

    @builtins.property
    @jsii.member(jsii_name="buildStatusConfigInput")
    def build_status_config_input(
        self,
    ) -> typing.Optional[CodebuildProjectSecondarySourcesBuildStatusConfig]:
        return typing.cast(typing.Optional[CodebuildProjectSecondarySourcesBuildStatusConfig], jsii.get(self, "buildStatusConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="gitCloneDepthInput")
    def git_clone_depth_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "gitCloneDepthInput"))

    @builtins.property
    @jsii.member(jsii_name="gitSubmodulesConfigInput")
    def git_submodules_config_input(
        self,
    ) -> typing.Optional[CodebuildProjectSecondarySourcesGitSubmodulesConfig]:
        return typing.cast(typing.Optional[CodebuildProjectSecondarySourcesGitSubmodulesConfig], jsii.get(self, "gitSubmodulesConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="insecureSslInput")
    def insecure_ssl_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "insecureSslInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="reportBuildStatusInput")
    def report_build_status_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "reportBuildStatusInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceIdentifierInput")
    def source_identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceIdentifierInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="buildspec")
    def buildspec(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "buildspec"))

    @buildspec.setter
    def buildspec(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46f1d9027e1d2d0dc0da83eb4e91f0cf12efdbed74f111a21c708d4d0a64e04d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "buildspec", value)

    @builtins.property
    @jsii.member(jsii_name="gitCloneDepth")
    def git_clone_depth(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "gitCloneDepth"))

    @git_clone_depth.setter
    def git_clone_depth(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f549386f7934d423a993a7448a3d72957fc5a3dc146068ca063059dc2f8551ca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gitCloneDepth", value)

    @builtins.property
    @jsii.member(jsii_name="insecureSsl")
    def insecure_ssl(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "insecureSsl"))

    @insecure_ssl.setter
    def insecure_ssl(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__765b7712f5d83a987d6ec50357036e22ca3731ccc21d22c5d21fdaa7debf2d77)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insecureSsl", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17cf561618dd512a089224c498f0c8b3eb22c942129e7b4f24e31b8aec84930f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="reportBuildStatus")
    def report_build_status(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "reportBuildStatus"))

    @report_build_status.setter
    def report_build_status(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d185d7512ba28860e4b4fa92e8574909678db6150ffd01ca9ce5aa3e3eab8729)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reportBuildStatus", value)

    @builtins.property
    @jsii.member(jsii_name="sourceIdentifier")
    def source_identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceIdentifier"))

    @source_identifier.setter
    def source_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94390ab44fa79fdea4d5fc6b370d92dbc9084d592a26baed2663ac06f277d935)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__328336b3c685d36696129932d2962afe1b0f1ee42cd59a935db00e3de21aba7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CodebuildProjectSecondarySources, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CodebuildProjectSecondarySources, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CodebuildProjectSecondarySources, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26fcaec3dbcf4e397cdcb23d2e0e4fc39aebfecebb04f6741b51c54f6cf32b27)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.codebuildProject.CodebuildProjectSource",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "auth": "auth",
        "buildspec": "buildspec",
        "build_status_config": "buildStatusConfig",
        "git_clone_depth": "gitCloneDepth",
        "git_submodules_config": "gitSubmodulesConfig",
        "insecure_ssl": "insecureSsl",
        "location": "location",
        "report_build_status": "reportBuildStatus",
    },
)
class CodebuildProjectSource:
    def __init__(
        self,
        *,
        type: builtins.str,
        auth: typing.Optional[typing.Union["CodebuildProjectSourceAuth", typing.Dict[builtins.str, typing.Any]]] = None,
        buildspec: typing.Optional[builtins.str] = None,
        build_status_config: typing.Optional[typing.Union["CodebuildProjectSourceBuildStatusConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        git_clone_depth: typing.Optional[jsii.Number] = None,
        git_submodules_config: typing.Optional[typing.Union["CodebuildProjectSourceGitSubmodulesConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        insecure_ssl: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        location: typing.Optional[builtins.str] = None,
        report_build_status: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.
        :param auth: auth block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#auth CodebuildProject#auth}
        :param buildspec: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#buildspec CodebuildProject#buildspec}.
        :param build_status_config: build_status_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#build_status_config CodebuildProject#build_status_config}
        :param git_clone_depth: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#git_clone_depth CodebuildProject#git_clone_depth}.
        :param git_submodules_config: git_submodules_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#git_submodules_config CodebuildProject#git_submodules_config}
        :param insecure_ssl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#insecure_ssl CodebuildProject#insecure_ssl}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#location CodebuildProject#location}.
        :param report_build_status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#report_build_status CodebuildProject#report_build_status}.
        '''
        if isinstance(auth, dict):
            auth = CodebuildProjectSourceAuth(**auth)
        if isinstance(build_status_config, dict):
            build_status_config = CodebuildProjectSourceBuildStatusConfig(**build_status_config)
        if isinstance(git_submodules_config, dict):
            git_submodules_config = CodebuildProjectSourceGitSubmodulesConfig(**git_submodules_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c8c796045851072770e6d8a3811f974083fb7c55a34b3491a0f7aa14af8cdf5)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument auth", value=auth, expected_type=type_hints["auth"])
            check_type(argname="argument buildspec", value=buildspec, expected_type=type_hints["buildspec"])
            check_type(argname="argument build_status_config", value=build_status_config, expected_type=type_hints["build_status_config"])
            check_type(argname="argument git_clone_depth", value=git_clone_depth, expected_type=type_hints["git_clone_depth"])
            check_type(argname="argument git_submodules_config", value=git_submodules_config, expected_type=type_hints["git_submodules_config"])
            check_type(argname="argument insecure_ssl", value=insecure_ssl, expected_type=type_hints["insecure_ssl"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument report_build_status", value=report_build_status, expected_type=type_hints["report_build_status"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if auth is not None:
            self._values["auth"] = auth
        if buildspec is not None:
            self._values["buildspec"] = buildspec
        if build_status_config is not None:
            self._values["build_status_config"] = build_status_config
        if git_clone_depth is not None:
            self._values["git_clone_depth"] = git_clone_depth
        if git_submodules_config is not None:
            self._values["git_submodules_config"] = git_submodules_config
        if insecure_ssl is not None:
            self._values["insecure_ssl"] = insecure_ssl
        if location is not None:
            self._values["location"] = location
        if report_build_status is not None:
            self._values["report_build_status"] = report_build_status

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auth(self) -> typing.Optional["CodebuildProjectSourceAuth"]:
        '''auth block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#auth CodebuildProject#auth}
        '''
        result = self._values.get("auth")
        return typing.cast(typing.Optional["CodebuildProjectSourceAuth"], result)

    @builtins.property
    def buildspec(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#buildspec CodebuildProject#buildspec}.'''
        result = self._values.get("buildspec")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def build_status_config(
        self,
    ) -> typing.Optional["CodebuildProjectSourceBuildStatusConfig"]:
        '''build_status_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#build_status_config CodebuildProject#build_status_config}
        '''
        result = self._values.get("build_status_config")
        return typing.cast(typing.Optional["CodebuildProjectSourceBuildStatusConfig"], result)

    @builtins.property
    def git_clone_depth(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#git_clone_depth CodebuildProject#git_clone_depth}.'''
        result = self._values.get("git_clone_depth")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def git_submodules_config(
        self,
    ) -> typing.Optional["CodebuildProjectSourceGitSubmodulesConfig"]:
        '''git_submodules_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#git_submodules_config CodebuildProject#git_submodules_config}
        '''
        result = self._values.get("git_submodules_config")
        return typing.cast(typing.Optional["CodebuildProjectSourceGitSubmodulesConfig"], result)

    @builtins.property
    def insecure_ssl(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#insecure_ssl CodebuildProject#insecure_ssl}.'''
        result = self._values.get("insecure_ssl")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def location(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#location CodebuildProject#location}.'''
        result = self._values.get("location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def report_build_status(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#report_build_status CodebuildProject#report_build_status}.'''
        result = self._values.get("report_build_status")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodebuildProjectSource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.codebuildProject.CodebuildProjectSourceAuth",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "resource": "resource"},
)
class CodebuildProjectSourceAuth:
    def __init__(
        self,
        *,
        type: builtins.str,
        resource: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.
        :param resource: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#resource CodebuildProject#resource}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7439c6e820032fe891d48858031801d464cb15d0c1dc5f55093ab92b931418c2)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if resource is not None:
            self._values["resource"] = resource

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#resource CodebuildProject#resource}.'''
        result = self._values.get("resource")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodebuildProjectSourceAuth(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodebuildProjectSourceAuthOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codebuildProject.CodebuildProjectSourceAuthOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9bed43aa25ea33875f96b34b66be22a7cac830e72a5e3a4dcbb6498fe10aca3a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetResource")
    def reset_resource(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResource", []))

    @builtins.property
    @jsii.member(jsii_name="resourceInput")
    def resource_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="resource")
    def resource(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resource"))

    @resource.setter
    def resource(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f89b3561b1534160aa1bc38f5457d52fb72d58850d47f068006f3a9c0db7856a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resource", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19b95b626fdd85274ede2b56aa57ada405e4f90b28f43ac714e1245a3568ff4a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CodebuildProjectSourceAuth]:
        return typing.cast(typing.Optional[CodebuildProjectSourceAuth], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodebuildProjectSourceAuth],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa562fc2f981aee784fea3399ae875bad1deab6b2ed7f1d86d09fd605dc62171)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.codebuildProject.CodebuildProjectSourceBuildStatusConfig",
    jsii_struct_bases=[],
    name_mapping={"context": "context", "target_url": "targetUrl"},
)
class CodebuildProjectSourceBuildStatusConfig:
    def __init__(
        self,
        *,
        context: typing.Optional[builtins.str] = None,
        target_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param context: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#context CodebuildProject#context}.
        :param target_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#target_url CodebuildProject#target_url}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__566ffb0f65b64c2c2480295bf128924562607cc57897a0a478f00d9a08ff9af5)
            check_type(argname="argument context", value=context, expected_type=type_hints["context"])
            check_type(argname="argument target_url", value=target_url, expected_type=type_hints["target_url"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if context is not None:
            self._values["context"] = context
        if target_url is not None:
            self._values["target_url"] = target_url

    @builtins.property
    def context(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#context CodebuildProject#context}.'''
        result = self._values.get("context")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#target_url CodebuildProject#target_url}.'''
        result = self._values.get("target_url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodebuildProjectSourceBuildStatusConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodebuildProjectSourceBuildStatusConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codebuildProject.CodebuildProjectSourceBuildStatusConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c85b23040931f39b2917b348178b8d6185255874950ced763f8cf4081d5e9097)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetContext")
    def reset_context(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContext", []))

    @jsii.member(jsii_name="resetTargetUrl")
    def reset_target_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetUrl", []))

    @builtins.property
    @jsii.member(jsii_name="contextInput")
    def context_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contextInput"))

    @builtins.property
    @jsii.member(jsii_name="targetUrlInput")
    def target_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="context")
    def context(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "context"))

    @context.setter
    def context(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78c650c4526d2c4bb723d505d1b09df60031e73ebb6f99aac7b22ad2cdecc8d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "context", value)

    @builtins.property
    @jsii.member(jsii_name="targetUrl")
    def target_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetUrl"))

    @target_url.setter
    def target_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea92c1637fe600de538d07da2e8c5774bf14e59b0ce9ad8ba90fe9937f10a1b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CodebuildProjectSourceBuildStatusConfig]:
        return typing.cast(typing.Optional[CodebuildProjectSourceBuildStatusConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodebuildProjectSourceBuildStatusConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bad8451c0bd821167d1054f54dab28b4fce28c7b70f5d8f82ca60459facc019)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.codebuildProject.CodebuildProjectSourceGitSubmodulesConfig",
    jsii_struct_bases=[],
    name_mapping={"fetch_submodules": "fetchSubmodules"},
)
class CodebuildProjectSourceGitSubmodulesConfig:
    def __init__(
        self,
        *,
        fetch_submodules: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param fetch_submodules: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#fetch_submodules CodebuildProject#fetch_submodules}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25429300112c2ab913e7546a5d579583023be0be59203bdbfcc5771a937b4115)
            check_type(argname="argument fetch_submodules", value=fetch_submodules, expected_type=type_hints["fetch_submodules"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "fetch_submodules": fetch_submodules,
        }

    @builtins.property
    def fetch_submodules(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#fetch_submodules CodebuildProject#fetch_submodules}.'''
        result = self._values.get("fetch_submodules")
        assert result is not None, "Required property 'fetch_submodules' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodebuildProjectSourceGitSubmodulesConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodebuildProjectSourceGitSubmodulesConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codebuildProject.CodebuildProjectSourceGitSubmodulesConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5d6b4b582ef66484f0a1636f8147a6b66bdd7d7bea3ffe5ba777105446cc4cd5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="fetchSubmodulesInput")
    def fetch_submodules_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "fetchSubmodulesInput"))

    @builtins.property
    @jsii.member(jsii_name="fetchSubmodules")
    def fetch_submodules(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "fetchSubmodules"))

    @fetch_submodules.setter
    def fetch_submodules(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75c2dcf4c15323988e3466f8707a2be2e52d4e77500344c4b5c3db321c9f0837)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fetchSubmodules", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CodebuildProjectSourceGitSubmodulesConfig]:
        return typing.cast(typing.Optional[CodebuildProjectSourceGitSubmodulesConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodebuildProjectSourceGitSubmodulesConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__236ea6dd98e81b2fd1c6c5c608d298a1e3162847bc573f1e39257655f41dd396)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CodebuildProjectSourceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codebuildProject.CodebuildProjectSourceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f28835eb3c05de33c7d8b5eff5cd36f07d678d69a1c4d8fe18a5e5c0faf2c700)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAuth")
    def put_auth(
        self,
        *,
        type: builtins.str,
        resource: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.
        :param resource: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#resource CodebuildProject#resource}.
        '''
        value = CodebuildProjectSourceAuth(type=type, resource=resource)

        return typing.cast(None, jsii.invoke(self, "putAuth", [value]))

    @jsii.member(jsii_name="putBuildStatusConfig")
    def put_build_status_config(
        self,
        *,
        context: typing.Optional[builtins.str] = None,
        target_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param context: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#context CodebuildProject#context}.
        :param target_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#target_url CodebuildProject#target_url}.
        '''
        value = CodebuildProjectSourceBuildStatusConfig(
            context=context, target_url=target_url
        )

        return typing.cast(None, jsii.invoke(self, "putBuildStatusConfig", [value]))

    @jsii.member(jsii_name="putGitSubmodulesConfig")
    def put_git_submodules_config(
        self,
        *,
        fetch_submodules: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param fetch_submodules: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#fetch_submodules CodebuildProject#fetch_submodules}.
        '''
        value = CodebuildProjectSourceGitSubmodulesConfig(
            fetch_submodules=fetch_submodules
        )

        return typing.cast(None, jsii.invoke(self, "putGitSubmodulesConfig", [value]))

    @jsii.member(jsii_name="resetAuth")
    def reset_auth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuth", []))

    @jsii.member(jsii_name="resetBuildspec")
    def reset_buildspec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBuildspec", []))

    @jsii.member(jsii_name="resetBuildStatusConfig")
    def reset_build_status_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBuildStatusConfig", []))

    @jsii.member(jsii_name="resetGitCloneDepth")
    def reset_git_clone_depth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGitCloneDepth", []))

    @jsii.member(jsii_name="resetGitSubmodulesConfig")
    def reset_git_submodules_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGitSubmodulesConfig", []))

    @jsii.member(jsii_name="resetInsecureSsl")
    def reset_insecure_ssl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInsecureSsl", []))

    @jsii.member(jsii_name="resetLocation")
    def reset_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocation", []))

    @jsii.member(jsii_name="resetReportBuildStatus")
    def reset_report_build_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReportBuildStatus", []))

    @builtins.property
    @jsii.member(jsii_name="auth")
    def auth(self) -> CodebuildProjectSourceAuthOutputReference:
        return typing.cast(CodebuildProjectSourceAuthOutputReference, jsii.get(self, "auth"))

    @builtins.property
    @jsii.member(jsii_name="buildStatusConfig")
    def build_status_config(
        self,
    ) -> CodebuildProjectSourceBuildStatusConfigOutputReference:
        return typing.cast(CodebuildProjectSourceBuildStatusConfigOutputReference, jsii.get(self, "buildStatusConfig"))

    @builtins.property
    @jsii.member(jsii_name="gitSubmodulesConfig")
    def git_submodules_config(
        self,
    ) -> CodebuildProjectSourceGitSubmodulesConfigOutputReference:
        return typing.cast(CodebuildProjectSourceGitSubmodulesConfigOutputReference, jsii.get(self, "gitSubmodulesConfig"))

    @builtins.property
    @jsii.member(jsii_name="authInput")
    def auth_input(self) -> typing.Optional[CodebuildProjectSourceAuth]:
        return typing.cast(typing.Optional[CodebuildProjectSourceAuth], jsii.get(self, "authInput"))

    @builtins.property
    @jsii.member(jsii_name="buildspecInput")
    def buildspec_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "buildspecInput"))

    @builtins.property
    @jsii.member(jsii_name="buildStatusConfigInput")
    def build_status_config_input(
        self,
    ) -> typing.Optional[CodebuildProjectSourceBuildStatusConfig]:
        return typing.cast(typing.Optional[CodebuildProjectSourceBuildStatusConfig], jsii.get(self, "buildStatusConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="gitCloneDepthInput")
    def git_clone_depth_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "gitCloneDepthInput"))

    @builtins.property
    @jsii.member(jsii_name="gitSubmodulesConfigInput")
    def git_submodules_config_input(
        self,
    ) -> typing.Optional[CodebuildProjectSourceGitSubmodulesConfig]:
        return typing.cast(typing.Optional[CodebuildProjectSourceGitSubmodulesConfig], jsii.get(self, "gitSubmodulesConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="insecureSslInput")
    def insecure_ssl_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "insecureSslInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="reportBuildStatusInput")
    def report_build_status_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "reportBuildStatusInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="buildspec")
    def buildspec(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "buildspec"))

    @buildspec.setter
    def buildspec(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__456f66fb89c8067b1774e74d23f9687d526f36b1a70411e4f5f358fd473ca7d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "buildspec", value)

    @builtins.property
    @jsii.member(jsii_name="gitCloneDepth")
    def git_clone_depth(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "gitCloneDepth"))

    @git_clone_depth.setter
    def git_clone_depth(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__508f096961864595d9617ce1a02d748720760e8b4225d667fad2b29991c64f1c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gitCloneDepth", value)

    @builtins.property
    @jsii.member(jsii_name="insecureSsl")
    def insecure_ssl(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "insecureSsl"))

    @insecure_ssl.setter
    def insecure_ssl(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd41cd3cc4491247ee6b4468cc270db6c024217d69cf5efe38dceb874c242bb0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insecureSsl", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f022b2518adf47a82154249aa3a1964207876cb162533b2d5dc2a19d3e913e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="reportBuildStatus")
    def report_build_status(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "reportBuildStatus"))

    @report_build_status.setter
    def report_build_status(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfc0d2c55669266a5da0d574077cb5e626ec12e69752212e9105625a8ccde99c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reportBuildStatus", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b39be68990ae4ca0836eb3723e9d6b11c5e1bfc2bd31ff1afb90defef6950472)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CodebuildProjectSource]:
        return typing.cast(typing.Optional[CodebuildProjectSource], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[CodebuildProjectSource]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__230db9c56b002b714bdd6e29c8cf8be218d0890932afc94cb744b3eb48dc677c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.codebuildProject.CodebuildProjectVpcConfig",
    jsii_struct_bases=[],
    name_mapping={
        "security_group_ids": "securityGroupIds",
        "subnets": "subnets",
        "vpc_id": "vpcId",
    },
)
class CodebuildProjectVpcConfig:
    def __init__(
        self,
        *,
        security_group_ids: typing.Sequence[builtins.str],
        subnets: typing.Sequence[builtins.str],
        vpc_id: builtins.str,
    ) -> None:
        '''
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#security_group_ids CodebuildProject#security_group_ids}.
        :param subnets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#subnets CodebuildProject#subnets}.
        :param vpc_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#vpc_id CodebuildProject#vpc_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6937cf93ca94f5cf0f9b5035dc5be689bfbf7082dc0aa3b99083d935c696e5f)
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument subnets", value=subnets, expected_type=type_hints["subnets"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "security_group_ids": security_group_ids,
            "subnets": subnets,
            "vpc_id": vpc_id,
        }

    @builtins.property
    def security_group_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#security_group_ids CodebuildProject#security_group_ids}.'''
        result = self._values.get("security_group_ids")
        assert result is not None, "Required property 'security_group_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def subnets(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#subnets CodebuildProject#subnets}.'''
        result = self._values.get("subnets")
        assert result is not None, "Required property 'subnets' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def vpc_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#vpc_id CodebuildProject#vpc_id}.'''
        result = self._values.get("vpc_id")
        assert result is not None, "Required property 'vpc_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodebuildProjectVpcConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodebuildProjectVpcConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codebuildProject.CodebuildProjectVpcConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b5e8fd7212429da948f14a93594308dc35cf6dbcc3e832bf856492d853193084)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="securityGroupIdsInput")
    def security_group_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetsInput")
    def subnets_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetsInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcIdInput")
    def vpc_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpcIdInput"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70d9347a5755bf3d981828b3d92696d163f9060dd63801150d67618e94dd5abb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="subnets")
    def subnets(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnets"))

    @subnets.setter
    def subnets(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98e908df16d7cf38990a71fcb5d043e14bdee29dd7f590a241fbed785fb9c311)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnets", value)

    @builtins.property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcId"))

    @vpc_id.setter
    def vpc_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d61525f55bf640c05568f18756a43c03c8d93d79f474dac42c972ac69a87e43)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CodebuildProjectVpcConfig]:
        return typing.cast(typing.Optional[CodebuildProjectVpcConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[CodebuildProjectVpcConfig]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15e7aa3821be709c473e76a14b3a870f64a10fe5ea42f07834afb70a56218ece)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CodebuildProject",
    "CodebuildProjectArtifacts",
    "CodebuildProjectArtifactsOutputReference",
    "CodebuildProjectBuildBatchConfig",
    "CodebuildProjectBuildBatchConfigOutputReference",
    "CodebuildProjectBuildBatchConfigRestrictions",
    "CodebuildProjectBuildBatchConfigRestrictionsOutputReference",
    "CodebuildProjectCache",
    "CodebuildProjectCacheOutputReference",
    "CodebuildProjectConfig",
    "CodebuildProjectEnvironment",
    "CodebuildProjectEnvironmentEnvironmentVariable",
    "CodebuildProjectEnvironmentEnvironmentVariableList",
    "CodebuildProjectEnvironmentEnvironmentVariableOutputReference",
    "CodebuildProjectEnvironmentOutputReference",
    "CodebuildProjectEnvironmentRegistryCredential",
    "CodebuildProjectEnvironmentRegistryCredentialOutputReference",
    "CodebuildProjectFileSystemLocations",
    "CodebuildProjectFileSystemLocationsList",
    "CodebuildProjectFileSystemLocationsOutputReference",
    "CodebuildProjectLogsConfig",
    "CodebuildProjectLogsConfigCloudwatchLogs",
    "CodebuildProjectLogsConfigCloudwatchLogsOutputReference",
    "CodebuildProjectLogsConfigOutputReference",
    "CodebuildProjectLogsConfigS3Logs",
    "CodebuildProjectLogsConfigS3LogsOutputReference",
    "CodebuildProjectSecondaryArtifacts",
    "CodebuildProjectSecondaryArtifactsList",
    "CodebuildProjectSecondaryArtifactsOutputReference",
    "CodebuildProjectSecondarySourceVersion",
    "CodebuildProjectSecondarySourceVersionList",
    "CodebuildProjectSecondarySourceVersionOutputReference",
    "CodebuildProjectSecondarySources",
    "CodebuildProjectSecondarySourcesAuth",
    "CodebuildProjectSecondarySourcesAuthOutputReference",
    "CodebuildProjectSecondarySourcesBuildStatusConfig",
    "CodebuildProjectSecondarySourcesBuildStatusConfigOutputReference",
    "CodebuildProjectSecondarySourcesGitSubmodulesConfig",
    "CodebuildProjectSecondarySourcesGitSubmodulesConfigOutputReference",
    "CodebuildProjectSecondarySourcesList",
    "CodebuildProjectSecondarySourcesOutputReference",
    "CodebuildProjectSource",
    "CodebuildProjectSourceAuth",
    "CodebuildProjectSourceAuthOutputReference",
    "CodebuildProjectSourceBuildStatusConfig",
    "CodebuildProjectSourceBuildStatusConfigOutputReference",
    "CodebuildProjectSourceGitSubmodulesConfig",
    "CodebuildProjectSourceGitSubmodulesConfigOutputReference",
    "CodebuildProjectSourceOutputReference",
    "CodebuildProjectVpcConfig",
    "CodebuildProjectVpcConfigOutputReference",
]

publication.publish()

def _typecheckingstub__ea7c392ec6ab016a0e106974108b385089bec193544a66c53dd8dca25e031262(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    artifacts: typing.Union[CodebuildProjectArtifacts, typing.Dict[builtins.str, typing.Any]],
    environment: typing.Union[CodebuildProjectEnvironment, typing.Dict[builtins.str, typing.Any]],
    name: builtins.str,
    service_role: builtins.str,
    source: typing.Union[CodebuildProjectSource, typing.Dict[builtins.str, typing.Any]],
    badge_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    build_batch_config: typing.Optional[typing.Union[CodebuildProjectBuildBatchConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    build_timeout: typing.Optional[jsii.Number] = None,
    cache: typing.Optional[typing.Union[CodebuildProjectCache, typing.Dict[builtins.str, typing.Any]]] = None,
    concurrent_build_limit: typing.Optional[jsii.Number] = None,
    description: typing.Optional[builtins.str] = None,
    encryption_key: typing.Optional[builtins.str] = None,
    file_system_locations: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CodebuildProjectFileSystemLocations, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
    logs_config: typing.Optional[typing.Union[CodebuildProjectLogsConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    project_visibility: typing.Optional[builtins.str] = None,
    queued_timeout: typing.Optional[jsii.Number] = None,
    resource_access_role: typing.Optional[builtins.str] = None,
    secondary_artifacts: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CodebuildProjectSecondaryArtifacts, typing.Dict[builtins.str, typing.Any]]]]] = None,
    secondary_sources: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CodebuildProjectSecondarySources, typing.Dict[builtins.str, typing.Any]]]]] = None,
    secondary_source_version: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CodebuildProjectSecondarySourceVersion, typing.Dict[builtins.str, typing.Any]]]]] = None,
    source_version: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    vpc_config: typing.Optional[typing.Union[CodebuildProjectVpcConfig, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__20e452d4d56bb053f946eb3baed1cdc0a84c744cbb88289c7d6369d6de1937f3(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CodebuildProjectFileSystemLocations, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db263907270d09cc1afee2830c08f60e6f3b373af011122571779badbf39f688(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CodebuildProjectSecondaryArtifacts, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7febe70bed1853e746bf43493a7821c715fdfd0bcfc8ab7fdcc789940b704889(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CodebuildProjectSecondarySources, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b06522bcb8b0f2269969f718c5e4a9dff964ec42c6b9c12ac2ae7817e9b6c7ae(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CodebuildProjectSecondarySourceVersion, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a47754483b9b490c7b8735c6e7cea185719bc104f24fa5a11955de7f27931bdd(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69f472423fbe928a7e8d67aa6e688e7d809b88252a4017d44dd3301757dccf18(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c5ea9350a08ecdc6140ebcbfed545ade2346c42377c9dbe7cad9e59ca5cf32b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea5115af55c3426f84b74f3c0725d530399675ae255e54e1084de2e95c447a01(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b53da2f0032879e089479584cf4b2ce76f7a6cf2e905440cc506e34e9875ff81(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2dc38e88976aa8294df59d983c74cb6879ae6df6ce3b8f2f39af89eda657ba9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac21ac7de235e7dad75b976a0172bb84e583618a3c162a82080fe1276a48c245(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3c438a309a89f328c2cab84d86604a3390f02332414559cda18d989e2187353(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e539762dc739e14f379afebe28f0b3fe770b39606e1998fa91ca421884aa89ef(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3f0a63d736b1d519b104894b1ab4978930814854149ea958fd77b12355bf00c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__751381ebbc9a81fb839c818ca7f9e9e071ff06a9713d907ea49ab0865c8a6246(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__777793a8c84edbe66e04154be7bf11a5a44026779998ab58b7ade094ec07299d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ad749379a7cfcf29eb6fb11e39e81100237ff6922e2bdd43d69e71659a1f3e0(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f75948599993d31569bae1f8ff2fd48d72fcb75e3b6aaf81b786035d63d5de34(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb092af1df85cfc874d14a934c6104e0fe6b9e3b71acd918bfc4c7959bc4daca(
    *,
    type: builtins.str,
    artifact_identifier: typing.Optional[builtins.str] = None,
    bucket_owner_access: typing.Optional[builtins.str] = None,
    encryption_disabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    location: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    namespace_type: typing.Optional[builtins.str] = None,
    override_artifact_name: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    packaging: typing.Optional[builtins.str] = None,
    path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c19806eec59124a4158fb08dc4f1cb237a241a178428d74799fdd61adacb324d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20963fbb1df0437f1a1239f815615ab02b0efc6773e99cb6fe9d28b2f35310ce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__251e1ec5f701668bc00815caec109043b238d1e93580f061e3aa88d2d83060fa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f8186468fae5723482cd7b84fee6b65981d8d9cd3d23c0a1985fbeda1921ce8(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__841f8539627517f797d1d6cee7db652d526d50f93c0fdb389641c38c76d251b2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12f9cdeac4451b433ad21f7e7cd28f89ca74c47bea9f0bb6db0977c81c894cd7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11a8002fb110df79c71f76955a6c0012cfcfb1d756a1f727cade8675a408ad2c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28ec914c253e35c0be8c5bdea7a5f4c7d26ba0465f9ce6456e8a6e276a3e6d86(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff24787c9930ceb80b4311dc23776e49f38ae09fb6316aa274d8de6d7f20b9ca(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2496330b29daca8ec6f8ceab2b1a48495e4b075945642930bbee2f7e52681cf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7d1fbd86457fd5e7b66a29860ed22be6df8378e81255e307f5e9046d84bf713(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc902fe3c9c08dc52f5a5136d1ef0479a73580fc87d16b29b006076582e6f559(
    value: typing.Optional[CodebuildProjectArtifacts],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__700011e1d00d52a8f35364860c1bc43eeb7af741b423084932b2db71f07523e0(
    *,
    service_role: builtins.str,
    combine_artifacts: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    restrictions: typing.Optional[typing.Union[CodebuildProjectBuildBatchConfigRestrictions, typing.Dict[builtins.str, typing.Any]]] = None,
    timeout_in_mins: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0f7a8818f0f94ecd6d0341ee3a05707d8e20179e3af331c13a3bf08cd41a4e2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23c847123bbbbf9429c2c47374491825e375959fe37a0a98b5bf3e969dde0b11(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c322638e904201ef41413f94efd52a35549ca642839c873bc049a621c49c118(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84a13172f340b851344b1ef218867e5fed8eb62c656b261aec2ed5f8f7e1ebb9(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be29742081e93d2bbee985089cdc3c46e5d1de499e9d13837619cd22605be9bc(
    value: typing.Optional[CodebuildProjectBuildBatchConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__feb18f6eee2561e572fbdd33dd63545673823caafa0d08977fc9e28565469e65(
    *,
    compute_types_allowed: typing.Optional[typing.Sequence[builtins.str]] = None,
    maximum_builds_allowed: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd1d1b361db73ca10b4d76cf7980fd84715cb13086d4d1b1b94397e7fde53a05(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ab3343d71b2648c48275abda5c77ca0576911aed0c652e744fbf5231d73c4b2(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14899afaed61069cdac0a16c512103a46ece3ba38b4b00061add9fe769afe888(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccfbecba65037f07c9783e4f65d958a12c1b3e69b405e0142290eab4f9112186(
    value: typing.Optional[CodebuildProjectBuildBatchConfigRestrictions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69dbc62af7768c00619bd610addcba8cdf08ba265149877d4def20e072001837(
    *,
    location: typing.Optional[builtins.str] = None,
    modes: typing.Optional[typing.Sequence[builtins.str]] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b7cc3ff572a3bff8846ec484e9292ed5c105a925beb1563f14c18c98f2c7ecb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efdbacd86a3039dbd308e52a17ed462268c7a22f63c6eaf2e647653c06144249(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37fa6ae80596985a5d3a9a0e105ae7a59d554006ac35c8279b446789940f635f(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4dd6743d863e00f8124532733112f203726cb26a2f6d1704f0136762a3348aa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3259b055e2174d70ebac79374807b91eea00a17dee0ffe926e150bb713a56998(
    value: typing.Optional[CodebuildProjectCache],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fce208a1961fa45f79ccd9acb096c46e50d3e6c1b899d0ce6488a238b468f90(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    artifacts: typing.Union[CodebuildProjectArtifacts, typing.Dict[builtins.str, typing.Any]],
    environment: typing.Union[CodebuildProjectEnvironment, typing.Dict[builtins.str, typing.Any]],
    name: builtins.str,
    service_role: builtins.str,
    source: typing.Union[CodebuildProjectSource, typing.Dict[builtins.str, typing.Any]],
    badge_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    build_batch_config: typing.Optional[typing.Union[CodebuildProjectBuildBatchConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    build_timeout: typing.Optional[jsii.Number] = None,
    cache: typing.Optional[typing.Union[CodebuildProjectCache, typing.Dict[builtins.str, typing.Any]]] = None,
    concurrent_build_limit: typing.Optional[jsii.Number] = None,
    description: typing.Optional[builtins.str] = None,
    encryption_key: typing.Optional[builtins.str] = None,
    file_system_locations: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CodebuildProjectFileSystemLocations, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
    logs_config: typing.Optional[typing.Union[CodebuildProjectLogsConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    project_visibility: typing.Optional[builtins.str] = None,
    queued_timeout: typing.Optional[jsii.Number] = None,
    resource_access_role: typing.Optional[builtins.str] = None,
    secondary_artifacts: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CodebuildProjectSecondaryArtifacts, typing.Dict[builtins.str, typing.Any]]]]] = None,
    secondary_sources: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CodebuildProjectSecondarySources, typing.Dict[builtins.str, typing.Any]]]]] = None,
    secondary_source_version: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CodebuildProjectSecondarySourceVersion, typing.Dict[builtins.str, typing.Any]]]]] = None,
    source_version: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    vpc_config: typing.Optional[typing.Union[CodebuildProjectVpcConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19fb50fca1a236f58ca8396358c92e7ba56d70253a0e206b6160171938758234(
    *,
    compute_type: builtins.str,
    image: builtins.str,
    type: builtins.str,
    certificate: typing.Optional[builtins.str] = None,
    environment_variable: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CodebuildProjectEnvironmentEnvironmentVariable, typing.Dict[builtins.str, typing.Any]]]]] = None,
    image_pull_credentials_type: typing.Optional[builtins.str] = None,
    privileged_mode: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    registry_credential: typing.Optional[typing.Union[CodebuildProjectEnvironmentRegistryCredential, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a68cdbf22ece3f4b8a2f6328edc33e0e61b7d3dd9aa23147e2515ec4ea8c102c(
    *,
    name: builtins.str,
    value: builtins.str,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53261d72013217e3e3a8601ffe7dee10cd094633ff6874aa94971f50b24d50e4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31a8832d4143563dd669900b02f01ecda057216c1c21a39181515e5d7eb28c0c(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ee7d9f43695a323e953665d87c4f77a5e9b9b2ad20605b4a73a6c3c36d35528(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2cc2571692a01db77baa4afc89a2663ef5ec421faf4696d91a633577ff90715(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__affa87a8966233f94bd86aba4b10868ae8a18789bd5281c7fab41fe62410c655(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b22d6b49ce9998fe7e5953a759435de07c2d6adaeb0b01de6f9016bc27338ee(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodebuildProjectEnvironmentEnvironmentVariable]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0dc8b2f60fa4d971e2a9a98d2aab4ccb80fd981c89a5d9922c0eeddc27df613(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7722319d2fb7061a6409ed98c9ecb0542ca817a67b4a5f9618fbb4515fc6110f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7254b287ee1e38acaedcd7f1adf6808de86db0ff690f8bdc292e98c68b63ca09(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__393351147cc3d91f893b877b998ca4523bcaa636646504cc12fc015407d4673e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0959c04edcf6fd78af43c943cf3f537db4b68d242df2f712abb077c2aa960e24(
    value: typing.Optional[typing.Union[CodebuildProjectEnvironmentEnvironmentVariable, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74660c6ab86ceae72a4f8866534e86ae4487557893283ef338315fe3f5ecaaef(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b800ee660cb832799efb6ebd2b487d5ded1fbe79be769bee5cf68b44aef32157(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CodebuildProjectEnvironmentEnvironmentVariable, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__235252b960458da7985b1c996ce2369e117bea9a4149db3d60c0717630149e79(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c1160921a51ec74dd7dec86d682dac9d5eca81f360c3976b236a57fb86cd702(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__592c5926b3571bfa4449062b6ff6b98cf03d18fe0d03f0ecf089e38c8a9381a9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__971e2e11750c49ed5e68858284e993bf43411fbacb7d1ba9d523e2f146759860(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa51f9944429919f9562eef17eed92f720671a1144558a2b5c108a26e8b7531c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6c235e1a88993c5c05bf220d6a6f0a740d6ee66110761d9d871e641add80a26(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34e2e7ec1c5632cf0a7861a49eafa6d911617bc46832d3f8f81de0e920eefdf6(
    value: typing.Optional[CodebuildProjectEnvironment],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe2fe812b4f939198c427caa66c46f681d6f0e01a80a945c26fb3895e651007d(
    *,
    credential: builtins.str,
    credential_provider: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55af52e79631de187406956a1acf81b7e5862f09a03dc1bdb8ecbf08b6cfed1a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76ad118c488c290429b8eaf5cc7a0d5b796a08258570157a2e64120042a2bc2b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21bd4f1bffd8dadea62b6ead057f9bb214c071de18f76f594b713b3ce8f6369d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5084cbef6ee4ca5af627d93f4a055740c821cd553355c84881637d6d3265a799(
    value: typing.Optional[CodebuildProjectEnvironmentRegistryCredential],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebca4b0a5936306cbfdbfb8786a8da00a13158ff509dd938db9e15bf18fc4693(
    *,
    identifier: typing.Optional[builtins.str] = None,
    location: typing.Optional[builtins.str] = None,
    mount_options: typing.Optional[builtins.str] = None,
    mount_point: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08c187f243974130f5c16c520be35e4184b1ce6b61a56214bae148eda6f151be(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66f64a3fef1f2cfa3c5447d60a93286e5e8a81e38513d7091de1e5eb09f1a1d8(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad447049b02297be1054a5bccd1349921d5525f4aa0c484360424dafa7e88947(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ab04d01c39c9339d41560e4c621c095c4264d7940cda62909bbaf2157349f7e(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8752898ee45dd9a971a9d66e8232bf83be73f7ddde2e1420b8f4ed478174e0bd(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f2dde18028dda7ca34cb686235717e47879a42d9390558665f99e0f988dc1c5(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodebuildProjectFileSystemLocations]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bd13a5c14646f442d2285a371d1ef33e2f3d3a657a11e153e95bc69950b6ad7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f3d90e07257adb6104ec970b7ca1e2f09c9f2e7c850c7fc2965c341563e4936(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__435d57a8ff849c3fce5eb9638c0f81f9c4719475b0213a8416b609c127738e8b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14946fc4c287c804255f76cad7d77c7c52f65c8d097df5ca7ab04220483a368b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03528b6e2b4dc009a6538d93a5f88f22e67fb97f017898b4e39a36e3a4c59a18(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99e4840aba70fe49ab5895232b19bd536a6a71fad941fbc0a400820956d2a146(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91c28e36a2de34e46d0cec53bd706467f4a4deb2b2e43f7929c819eb2ead87d6(
    value: typing.Optional[typing.Union[CodebuildProjectFileSystemLocations, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3298be36907698b253abd89552ab434e461f9d7b144963ced98d2fad50dd5324(
    *,
    cloudwatch_logs: typing.Optional[typing.Union[CodebuildProjectLogsConfigCloudwatchLogs, typing.Dict[builtins.str, typing.Any]]] = None,
    s3_logs: typing.Optional[typing.Union[CodebuildProjectLogsConfigS3Logs, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__565e64ffe90856210d1875a81f2d87ad195335c4ecabf61ac35be6e1c8d1cede(
    *,
    group_name: typing.Optional[builtins.str] = None,
    status: typing.Optional[builtins.str] = None,
    stream_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e40839a9fe29a32c6e5ec7a0d5bddc2e8f2e463de7889e9f85f5733ec7b3bf4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a848ae98d7b6de3df26b4afd2d5546f6dff977227f89b5f0203beb16dceb68b4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b4e886647bbad21b10c273d2292bdd1951087a9c1c29b1a0b43a3a36877d96b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c089a3b78152ee8d0981f75be5d3545958b14b24a3a1f23279a5fde3e57fbdb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c337ab1f65cd4e0175e57fc1dce17da1eb4f0316bc52c7a0088a14032d99138(
    value: typing.Optional[CodebuildProjectLogsConfigCloudwatchLogs],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__febf357d7ec38164fbdfb82ba8e4d9f111c058ccf5d84b0c13b3dd9b720f11b2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ebf12fbe4331b0666169d191111b6624e6f8075246ed244d46144ad7908708c(
    value: typing.Optional[CodebuildProjectLogsConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c6f70aeed22b54f37a167d5b8043e7c8e7ff71f09f29c4a25501ad1b8e0bc90(
    *,
    bucket_owner_access: typing.Optional[builtins.str] = None,
    encryption_disabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    location: typing.Optional[builtins.str] = None,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1745947f8f00c46f45bc26768373d39e2f5de618294f1a51cb7d02498517824(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2462080e67f31fa7a3864f728165734a849c35ca7416fe288439800adca208e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aff75b31d135dd0b1f250a1775fa16cf77b6b9a6d57062cc3769085462ec12d4(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a89ffde9a0e7036052acfa55501d8328c67d72167966321910b6aea079d6766(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ae77895d9d675894d7e14751e2a8757429dff6a3d53fa4ec806c143806ccee0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__787d947a3f5f806eeec5d6fa71389b30d48f658ab6fba0127ad58ebeb7ac4cb8(
    value: typing.Optional[CodebuildProjectLogsConfigS3Logs],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f987c5241c6571ab9d4c7e02991fcca69ced951ba7f4f941adcb799e5d9e7740(
    *,
    artifact_identifier: builtins.str,
    type: builtins.str,
    bucket_owner_access: typing.Optional[builtins.str] = None,
    encryption_disabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    location: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    namespace_type: typing.Optional[builtins.str] = None,
    override_artifact_name: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    packaging: typing.Optional[builtins.str] = None,
    path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__839a628c4c3409baf9532bfe061ca1ee8b6c16b6626ca679ae40348547f2fb2b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d858705ff18ed21800ba77d0ea7edd4e20d8f4624edf6c0e1bbff533ab8b9fbb(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d9701bb33f24f0d5142b2c828759f758a84b176ac5dafd3e69ded7939ca1d75(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5617527e503c4f23beb8c308c6b3113de4ade100189eec5ae4ed37df11c1fc2(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5abe30f2cc79fe49e9ba2cc28311b8689c2f3cb95a696c3c5dcfb1b7b851514(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09581ed2d497a52375de375df6b67857a94341cbf0dd4d167b8f6cd1a946bd70(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodebuildProjectSecondaryArtifacts]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1799beaf56b40a9adf2940fde7ded17636f0f76f5b24039aadb14497477e318(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4e9a8219f409a30f6ba216e0c4f23dcf14323f0add3e89cb44e11e8d1d4c632(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e5771128844dded2ee2efed27bf126156d4a3364d3f9bc2d26c9dedba4ce573(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61c98d34aee87ddff9b2d8800904db7c390e3720918c3ef7462877b71797a7bc(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fd4bdfc37601882beb466b6c546b0d02156e43dc5cdec4d05e0f11e75a74a55(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf2f35be6b4cd6b2a088d42b03c22401bef592f97fa3ccae73cd21b7de33520e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e42d92d358429681261c4129164e99dc210d43cb5f74f8172ffc6b262dbd8867(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c5a66ab5839f7038c25d250dc56c12cc4e568a5517c501ffc1908b5e7aa8c31(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83a63a9bb77781ae1082d0655903347aeb36846fe0285bf3ac8959ff23ab0f38(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47ca6433faa82c69f5a4dc3d1db2e8f0a8089e090d34153615c749e9d24b9c0d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__550eb9d7eca2e0b319755362baeeb97a396259a9f9c2c464f19f91693e40aa38(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49dda78950291def4932959acfa8e5cc2faaf42c814b352826c26ae466e008fa(
    value: typing.Optional[typing.Union[CodebuildProjectSecondaryArtifacts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9ebc035899d8897beb2832efcb59a738a41bac1808a51e93bffe4cca513304e(
    *,
    source_identifier: builtins.str,
    source_version: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__040e45ba67fbbfd66c76aa1588eece65f11bdd99faef18934d1601acec5298a3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31f09cbb5a0af1ece1d857508f2bcb7e977ec141e98664694b9340d985082793(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__859e07d82f148162ac051cfa9fa5d752a2a156175e497e100a3c441ede50a8f3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37f6757615dc44ce11722a392c0a85d3d41a3ff60ef1879d35eb6499c0ad239e(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b12cf7a0cf0a3bb03a1d66b41a5a7c1057fc024531ed8be70c37c15901259f54(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf61b1eb1c9b559e147d0b0957ef8ba8e51bc72defe7e238425c3bf435f56bf4(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodebuildProjectSecondarySourceVersion]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c512f814c161dea487cc08dcde68118e37c14585acd711dd193f1a18fc94756(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0e2c217e586803ae462c8f957dfb9dac1d8f2de4784032abe8458a03528b06e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__182e3f87dc83131da4282de5a83a6d2f9451d17a3f21020daa900d837717ee90(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0580ec54b33af58252f2cc095672ac5d0849e7513746bb1ad50916e06a1ac65b(
    value: typing.Optional[typing.Union[CodebuildProjectSecondarySourceVersion, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c83c4e11d3ecb49123dd2093ab8db085b9477b4744aaa9aab1560ee0c2ee1fc8(
    *,
    source_identifier: builtins.str,
    type: builtins.str,
    auth: typing.Optional[typing.Union[CodebuildProjectSecondarySourcesAuth, typing.Dict[builtins.str, typing.Any]]] = None,
    buildspec: typing.Optional[builtins.str] = None,
    build_status_config: typing.Optional[typing.Union[CodebuildProjectSecondarySourcesBuildStatusConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    git_clone_depth: typing.Optional[jsii.Number] = None,
    git_submodules_config: typing.Optional[typing.Union[CodebuildProjectSecondarySourcesGitSubmodulesConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    insecure_ssl: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    location: typing.Optional[builtins.str] = None,
    report_build_status: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb7b241095fc754af7eff0929baece76a3356e8f14840e1d31a3a43748e53cf7(
    *,
    type: builtins.str,
    resource: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18980cf6ebd3e4375d2ced0eb7a3b188e4df7355bdc62eb41e09c536e399b7f1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5cb5c3f79580cd73e5879c69821d1de2d37dc4c289685982fbd6936e5fb37454(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a688d0a24a2c7286d5207ce420c54ad9105c97c5594981df275036452d61cf14(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d66f4b8c7c25af113b0f666df3097afb5f18fec104475ddd8026386606aa19a(
    value: typing.Optional[CodebuildProjectSecondarySourcesAuth],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fc0c33b318e375edd8620581ccde038c98778dc3c3c51c80881d6d0d499ab96(
    *,
    context: typing.Optional[builtins.str] = None,
    target_url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a88ce5e5f51f1a2cfc3951270b5c902f599d90517d9047e33f14db40cf530d7b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__edeb15ce721f2c0af27d3659393289b931fb1fc2594b6ce574a5794c3744b9a4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b212e830eda26bedd21b5e70d7a2189ee5963bac90621362c3cf6da24b05b7c9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3270a75db0d5842b056e483f08ceea969a46dbfce32c40eea3475b7edb9cf320(
    value: typing.Optional[CodebuildProjectSecondarySourcesBuildStatusConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3d96d4b34f11358ba4f6b1a3d0bec17b745dff95f998496ff4ba41fc7b12fe7(
    *,
    fetch_submodules: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b50ff1fad7f338c4cbd906427eadcf33adf44595d336d6aeb48ad52ebd6abaae(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b8f9227233e82302b93a2cd3bca3252e9bee012af007ca01bba6fab638d0d54(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21e7bbba353403a082983c2958f6c1643bfb9b73fe3f503aea0bcf49e46ddd9a(
    value: typing.Optional[CodebuildProjectSecondarySourcesGitSubmodulesConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b44ac4bac2372aa81592bba1795008c459b577bc8c63eec318c0f0222ea54cb8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5540ab4d8a39720b93b0d32d58f5c6ebbfc9f7dff157e1c92e355c7590629e95(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09e4a35ec878faeadfb373701ef6487f2abad676d948492c2380e6fda2e81217(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73d81ffe6da98c54600401ac31cb7eebd486e2585229d61c58591148efc2fe1f(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2f1c98656bc0dc2827f88a44eb51464d3768caa4456f610f49afd3aafe25cd4(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3158bb315c631a8420dc3b26a472f8930ea126d4929ae0a5082409b82ec6b5f3(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodebuildProjectSecondarySources]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__940d01beaf6408f2a4f79c72c572691f32a368ff0dfcb7191639256c35e2d881(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46f1d9027e1d2d0dc0da83eb4e91f0cf12efdbed74f111a21c708d4d0a64e04d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f549386f7934d423a993a7448a3d72957fc5a3dc146068ca063059dc2f8551ca(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__765b7712f5d83a987d6ec50357036e22ca3731ccc21d22c5d21fdaa7debf2d77(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17cf561618dd512a089224c498f0c8b3eb22c942129e7b4f24e31b8aec84930f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d185d7512ba28860e4b4fa92e8574909678db6150ffd01ca9ce5aa3e3eab8729(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94390ab44fa79fdea4d5fc6b370d92dbc9084d592a26baed2663ac06f277d935(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__328336b3c685d36696129932d2962afe1b0f1ee42cd59a935db00e3de21aba7d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26fcaec3dbcf4e397cdcb23d2e0e4fc39aebfecebb04f6741b51c54f6cf32b27(
    value: typing.Optional[typing.Union[CodebuildProjectSecondarySources, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c8c796045851072770e6d8a3811f974083fb7c55a34b3491a0f7aa14af8cdf5(
    *,
    type: builtins.str,
    auth: typing.Optional[typing.Union[CodebuildProjectSourceAuth, typing.Dict[builtins.str, typing.Any]]] = None,
    buildspec: typing.Optional[builtins.str] = None,
    build_status_config: typing.Optional[typing.Union[CodebuildProjectSourceBuildStatusConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    git_clone_depth: typing.Optional[jsii.Number] = None,
    git_submodules_config: typing.Optional[typing.Union[CodebuildProjectSourceGitSubmodulesConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    insecure_ssl: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    location: typing.Optional[builtins.str] = None,
    report_build_status: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7439c6e820032fe891d48858031801d464cb15d0c1dc5f55093ab92b931418c2(
    *,
    type: builtins.str,
    resource: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bed43aa25ea33875f96b34b66be22a7cac830e72a5e3a4dcbb6498fe10aca3a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f89b3561b1534160aa1bc38f5457d52fb72d58850d47f068006f3a9c0db7856a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19b95b626fdd85274ede2b56aa57ada405e4f90b28f43ac714e1245a3568ff4a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa562fc2f981aee784fea3399ae875bad1deab6b2ed7f1d86d09fd605dc62171(
    value: typing.Optional[CodebuildProjectSourceAuth],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__566ffb0f65b64c2c2480295bf128924562607cc57897a0a478f00d9a08ff9af5(
    *,
    context: typing.Optional[builtins.str] = None,
    target_url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c85b23040931f39b2917b348178b8d6185255874950ced763f8cf4081d5e9097(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78c650c4526d2c4bb723d505d1b09df60031e73ebb6f99aac7b22ad2cdecc8d2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea92c1637fe600de538d07da2e8c5774bf14e59b0ce9ad8ba90fe9937f10a1b5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bad8451c0bd821167d1054f54dab28b4fce28c7b70f5d8f82ca60459facc019(
    value: typing.Optional[CodebuildProjectSourceBuildStatusConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25429300112c2ab913e7546a5d579583023be0be59203bdbfcc5771a937b4115(
    *,
    fetch_submodules: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d6b4b582ef66484f0a1636f8147a6b66bdd7d7bea3ffe5ba777105446cc4cd5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75c2dcf4c15323988e3466f8707a2be2e52d4e77500344c4b5c3db321c9f0837(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__236ea6dd98e81b2fd1c6c5c608d298a1e3162847bc573f1e39257655f41dd396(
    value: typing.Optional[CodebuildProjectSourceGitSubmodulesConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f28835eb3c05de33c7d8b5eff5cd36f07d678d69a1c4d8fe18a5e5c0faf2c700(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__456f66fb89c8067b1774e74d23f9687d526f36b1a70411e4f5f358fd473ca7d7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__508f096961864595d9617ce1a02d748720760e8b4225d667fad2b29991c64f1c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd41cd3cc4491247ee6b4468cc270db6c024217d69cf5efe38dceb874c242bb0(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f022b2518adf47a82154249aa3a1964207876cb162533b2d5dc2a19d3e913e0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfc0d2c55669266a5da0d574077cb5e626ec12e69752212e9105625a8ccde99c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b39be68990ae4ca0836eb3723e9d6b11c5e1bfc2bd31ff1afb90defef6950472(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__230db9c56b002b714bdd6e29c8cf8be218d0890932afc94cb744b3eb48dc677c(
    value: typing.Optional[CodebuildProjectSource],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6937cf93ca94f5cf0f9b5035dc5be689bfbf7082dc0aa3b99083d935c696e5f(
    *,
    security_group_ids: typing.Sequence[builtins.str],
    subnets: typing.Sequence[builtins.str],
    vpc_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5e8fd7212429da948f14a93594308dc35cf6dbcc3e832bf856492d853193084(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70d9347a5755bf3d981828b3d92696d163f9060dd63801150d67618e94dd5abb(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98e908df16d7cf38990a71fcb5d043e14bdee29dd7f590a241fbed785fb9c311(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d61525f55bf640c05568f18756a43c03c8d93d79f474dac42c972ac69a87e43(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15e7aa3821be709c473e76a14b3a870f64a10fe5ea42f07834afb70a56218ece(
    value: typing.Optional[CodebuildProjectVpcConfig],
) -> None:
    """Type checking stubs"""
    pass
