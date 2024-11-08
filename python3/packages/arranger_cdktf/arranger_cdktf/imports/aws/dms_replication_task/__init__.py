'''
# `aws_dms_replication_task`

Refer to the Terraform Registory for docs: [`aws_dms_replication_task`](https://www.terraform.io/docs/providers/aws/r/dms_replication_task).
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


class DmsReplicationTask(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dmsReplicationTask.DmsReplicationTask",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task aws_dms_replication_task}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        migration_type: builtins.str,
        replication_instance_arn: builtins.str,
        replication_task_id: builtins.str,
        source_endpoint_arn: builtins.str,
        table_mappings: builtins.str,
        target_endpoint_arn: builtins.str,
        cdc_start_position: typing.Optional[builtins.str] = None,
        cdc_start_time: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        replication_task_settings: typing.Optional[builtins.str] = None,
        start_replication_task: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task aws_dms_replication_task} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param migration_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#migration_type DmsReplicationTask#migration_type}.
        :param replication_instance_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#replication_instance_arn DmsReplicationTask#replication_instance_arn}.
        :param replication_task_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#replication_task_id DmsReplicationTask#replication_task_id}.
        :param source_endpoint_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#source_endpoint_arn DmsReplicationTask#source_endpoint_arn}.
        :param table_mappings: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#table_mappings DmsReplicationTask#table_mappings}.
        :param target_endpoint_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#target_endpoint_arn DmsReplicationTask#target_endpoint_arn}.
        :param cdc_start_position: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#cdc_start_position DmsReplicationTask#cdc_start_position}.
        :param cdc_start_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#cdc_start_time DmsReplicationTask#cdc_start_time}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#id DmsReplicationTask#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param replication_task_settings: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#replication_task_settings DmsReplicationTask#replication_task_settings}.
        :param start_replication_task: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#start_replication_task DmsReplicationTask#start_replication_task}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#tags DmsReplicationTask#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#tags_all DmsReplicationTask#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b212183aeaca85c2982b115cfac815421e4234bcfb06c83c5624ffaa58391ffb)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DmsReplicationTaskConfig(
            migration_type=migration_type,
            replication_instance_arn=replication_instance_arn,
            replication_task_id=replication_task_id,
            source_endpoint_arn=source_endpoint_arn,
            table_mappings=table_mappings,
            target_endpoint_arn=target_endpoint_arn,
            cdc_start_position=cdc_start_position,
            cdc_start_time=cdc_start_time,
            id=id,
            replication_task_settings=replication_task_settings,
            start_replication_task=start_replication_task,
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

    @jsii.member(jsii_name="resetCdcStartPosition")
    def reset_cdc_start_position(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCdcStartPosition", []))

    @jsii.member(jsii_name="resetCdcStartTime")
    def reset_cdc_start_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCdcStartTime", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetReplicationTaskSettings")
    def reset_replication_task_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReplicationTaskSettings", []))

    @jsii.member(jsii_name="resetStartReplicationTask")
    def reset_start_replication_task(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartReplicationTask", []))

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
    @jsii.member(jsii_name="replicationTaskArn")
    def replication_task_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "replicationTaskArn"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="cdcStartPositionInput")
    def cdc_start_position_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cdcStartPositionInput"))

    @builtins.property
    @jsii.member(jsii_name="cdcStartTimeInput")
    def cdc_start_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cdcStartTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="migrationTypeInput")
    def migration_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "migrationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="replicationInstanceArnInput")
    def replication_instance_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "replicationInstanceArnInput"))

    @builtins.property
    @jsii.member(jsii_name="replicationTaskIdInput")
    def replication_task_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "replicationTaskIdInput"))

    @builtins.property
    @jsii.member(jsii_name="replicationTaskSettingsInput")
    def replication_task_settings_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "replicationTaskSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceEndpointArnInput")
    def source_endpoint_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceEndpointArnInput"))

    @builtins.property
    @jsii.member(jsii_name="startReplicationTaskInput")
    def start_replication_task_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "startReplicationTaskInput"))

    @builtins.property
    @jsii.member(jsii_name="tableMappingsInput")
    def table_mappings_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableMappingsInput"))

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
    @jsii.member(jsii_name="targetEndpointArnInput")
    def target_endpoint_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetEndpointArnInput"))

    @builtins.property
    @jsii.member(jsii_name="cdcStartPosition")
    def cdc_start_position(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cdcStartPosition"))

    @cdc_start_position.setter
    def cdc_start_position(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3393412b68cf0b2ea06f0694373f602486fcea2e6a631e6c656b97ce3525614b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cdcStartPosition", value)

    @builtins.property
    @jsii.member(jsii_name="cdcStartTime")
    def cdc_start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cdcStartTime"))

    @cdc_start_time.setter
    def cdc_start_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46f409d249cc2bda936cfcfd18e8d1a57e690ea6902319a530e424267dfdea18)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cdcStartTime", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4fab960c6ce72a3595429aad0fa3b914f3ea81ca6a5c1784df0f42fa54e460a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="migrationType")
    def migration_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "migrationType"))

    @migration_type.setter
    def migration_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d34bf20232f5a08f9a996b656e5922f971c7787d32f5cdb6095618bb169b24af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "migrationType", value)

    @builtins.property
    @jsii.member(jsii_name="replicationInstanceArn")
    def replication_instance_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "replicationInstanceArn"))

    @replication_instance_arn.setter
    def replication_instance_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afc1b7b342be1dad35e154bc74d1d972049eaf299c7d8edd62af13351e6cb73b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicationInstanceArn", value)

    @builtins.property
    @jsii.member(jsii_name="replicationTaskId")
    def replication_task_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "replicationTaskId"))

    @replication_task_id.setter
    def replication_task_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ce890990e742f89dac027dbdc8aea6ba6bebbd32b953119b65a07d8e482f226)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicationTaskId", value)

    @builtins.property
    @jsii.member(jsii_name="replicationTaskSettings")
    def replication_task_settings(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "replicationTaskSettings"))

    @replication_task_settings.setter
    def replication_task_settings(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2879009691b5b9126136059e1340f01cf1b4e93ac5922b85071f956466754cf5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicationTaskSettings", value)

    @builtins.property
    @jsii.member(jsii_name="sourceEndpointArn")
    def source_endpoint_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceEndpointArn"))

    @source_endpoint_arn.setter
    def source_endpoint_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b2e4ddd409a6ada6ff02d4d062d1a0e1e9f2cb1b01d20ef488a264aae33a131)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceEndpointArn", value)

    @builtins.property
    @jsii.member(jsii_name="startReplicationTask")
    def start_replication_task(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "startReplicationTask"))

    @start_replication_task.setter
    def start_replication_task(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15f10db8e98f046fd502b67539e792af5036465e4babfcdf8c9e30b160658cee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startReplicationTask", value)

    @builtins.property
    @jsii.member(jsii_name="tableMappings")
    def table_mappings(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tableMappings"))

    @table_mappings.setter
    def table_mappings(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40bb8a8e740f961e3719450ee40b6942ee2568abf286492d307f2cd19a95b8b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableMappings", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d08e97172319a01e37722183a9846b9a650c87dd7b52a25204a7f98acaa0bfc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be03a72a7df8f155d7a82bf5020bb8673e25a9ea536e18a62d58929f55f65efe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="targetEndpointArn")
    def target_endpoint_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetEndpointArn"))

    @target_endpoint_arn.setter
    def target_endpoint_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__daf9b504c9a793ec2629730b9de39aabdcbde0c5919bd4e7a45cad1f26f96e15)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetEndpointArn", value)


@jsii.data_type(
    jsii_type="aws.dmsReplicationTask.DmsReplicationTaskConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "migration_type": "migrationType",
        "replication_instance_arn": "replicationInstanceArn",
        "replication_task_id": "replicationTaskId",
        "source_endpoint_arn": "sourceEndpointArn",
        "table_mappings": "tableMappings",
        "target_endpoint_arn": "targetEndpointArn",
        "cdc_start_position": "cdcStartPosition",
        "cdc_start_time": "cdcStartTime",
        "id": "id",
        "replication_task_settings": "replicationTaskSettings",
        "start_replication_task": "startReplicationTask",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class DmsReplicationTaskConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        migration_type: builtins.str,
        replication_instance_arn: builtins.str,
        replication_task_id: builtins.str,
        source_endpoint_arn: builtins.str,
        table_mappings: builtins.str,
        target_endpoint_arn: builtins.str,
        cdc_start_position: typing.Optional[builtins.str] = None,
        cdc_start_time: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        replication_task_settings: typing.Optional[builtins.str] = None,
        start_replication_task: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
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
        :param migration_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#migration_type DmsReplicationTask#migration_type}.
        :param replication_instance_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#replication_instance_arn DmsReplicationTask#replication_instance_arn}.
        :param replication_task_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#replication_task_id DmsReplicationTask#replication_task_id}.
        :param source_endpoint_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#source_endpoint_arn DmsReplicationTask#source_endpoint_arn}.
        :param table_mappings: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#table_mappings DmsReplicationTask#table_mappings}.
        :param target_endpoint_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#target_endpoint_arn DmsReplicationTask#target_endpoint_arn}.
        :param cdc_start_position: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#cdc_start_position DmsReplicationTask#cdc_start_position}.
        :param cdc_start_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#cdc_start_time DmsReplicationTask#cdc_start_time}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#id DmsReplicationTask#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param replication_task_settings: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#replication_task_settings DmsReplicationTask#replication_task_settings}.
        :param start_replication_task: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#start_replication_task DmsReplicationTask#start_replication_task}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#tags DmsReplicationTask#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#tags_all DmsReplicationTask#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b58aa9050e76fa87ad8fc3a835f4d0d214b7a0f73b003ed74e3690ccf40a2224)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument migration_type", value=migration_type, expected_type=type_hints["migration_type"])
            check_type(argname="argument replication_instance_arn", value=replication_instance_arn, expected_type=type_hints["replication_instance_arn"])
            check_type(argname="argument replication_task_id", value=replication_task_id, expected_type=type_hints["replication_task_id"])
            check_type(argname="argument source_endpoint_arn", value=source_endpoint_arn, expected_type=type_hints["source_endpoint_arn"])
            check_type(argname="argument table_mappings", value=table_mappings, expected_type=type_hints["table_mappings"])
            check_type(argname="argument target_endpoint_arn", value=target_endpoint_arn, expected_type=type_hints["target_endpoint_arn"])
            check_type(argname="argument cdc_start_position", value=cdc_start_position, expected_type=type_hints["cdc_start_position"])
            check_type(argname="argument cdc_start_time", value=cdc_start_time, expected_type=type_hints["cdc_start_time"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument replication_task_settings", value=replication_task_settings, expected_type=type_hints["replication_task_settings"])
            check_type(argname="argument start_replication_task", value=start_replication_task, expected_type=type_hints["start_replication_task"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "migration_type": migration_type,
            "replication_instance_arn": replication_instance_arn,
            "replication_task_id": replication_task_id,
            "source_endpoint_arn": source_endpoint_arn,
            "table_mappings": table_mappings,
            "target_endpoint_arn": target_endpoint_arn,
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
        if cdc_start_position is not None:
            self._values["cdc_start_position"] = cdc_start_position
        if cdc_start_time is not None:
            self._values["cdc_start_time"] = cdc_start_time
        if id is not None:
            self._values["id"] = id
        if replication_task_settings is not None:
            self._values["replication_task_settings"] = replication_task_settings
        if start_replication_task is not None:
            self._values["start_replication_task"] = start_replication_task
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
    def migration_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#migration_type DmsReplicationTask#migration_type}.'''
        result = self._values.get("migration_type")
        assert result is not None, "Required property 'migration_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def replication_instance_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#replication_instance_arn DmsReplicationTask#replication_instance_arn}.'''
        result = self._values.get("replication_instance_arn")
        assert result is not None, "Required property 'replication_instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def replication_task_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#replication_task_id DmsReplicationTask#replication_task_id}.'''
        result = self._values.get("replication_task_id")
        assert result is not None, "Required property 'replication_task_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_endpoint_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#source_endpoint_arn DmsReplicationTask#source_endpoint_arn}.'''
        result = self._values.get("source_endpoint_arn")
        assert result is not None, "Required property 'source_endpoint_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def table_mappings(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#table_mappings DmsReplicationTask#table_mappings}.'''
        result = self._values.get("table_mappings")
        assert result is not None, "Required property 'table_mappings' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_endpoint_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#target_endpoint_arn DmsReplicationTask#target_endpoint_arn}.'''
        result = self._values.get("target_endpoint_arn")
        assert result is not None, "Required property 'target_endpoint_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cdc_start_position(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#cdc_start_position DmsReplicationTask#cdc_start_position}.'''
        result = self._values.get("cdc_start_position")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cdc_start_time(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#cdc_start_time DmsReplicationTask#cdc_start_time}.'''
        result = self._values.get("cdc_start_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#id DmsReplicationTask#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def replication_task_settings(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#replication_task_settings DmsReplicationTask#replication_task_settings}.'''
        result = self._values.get("replication_task_settings")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start_replication_task(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#start_replication_task DmsReplicationTask#start_replication_task}.'''
        result = self._values.get("start_replication_task")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#tags DmsReplicationTask#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_replication_task#tags_all DmsReplicationTask#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DmsReplicationTaskConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DmsReplicationTask",
    "DmsReplicationTaskConfig",
]

publication.publish()

def _typecheckingstub__b212183aeaca85c2982b115cfac815421e4234bcfb06c83c5624ffaa58391ffb(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    migration_type: builtins.str,
    replication_instance_arn: builtins.str,
    replication_task_id: builtins.str,
    source_endpoint_arn: builtins.str,
    table_mappings: builtins.str,
    target_endpoint_arn: builtins.str,
    cdc_start_position: typing.Optional[builtins.str] = None,
    cdc_start_time: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    replication_task_settings: typing.Optional[builtins.str] = None,
    start_replication_task: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
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

def _typecheckingstub__3393412b68cf0b2ea06f0694373f602486fcea2e6a631e6c656b97ce3525614b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46f409d249cc2bda936cfcfd18e8d1a57e690ea6902319a530e424267dfdea18(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fab960c6ce72a3595429aad0fa3b914f3ea81ca6a5c1784df0f42fa54e460a9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d34bf20232f5a08f9a996b656e5922f971c7787d32f5cdb6095618bb169b24af(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afc1b7b342be1dad35e154bc74d1d972049eaf299c7d8edd62af13351e6cb73b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ce890990e742f89dac027dbdc8aea6ba6bebbd32b953119b65a07d8e482f226(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2879009691b5b9126136059e1340f01cf1b4e93ac5922b85071f956466754cf5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b2e4ddd409a6ada6ff02d4d062d1a0e1e9f2cb1b01d20ef488a264aae33a131(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15f10db8e98f046fd502b67539e792af5036465e4babfcdf8c9e30b160658cee(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40bb8a8e740f961e3719450ee40b6942ee2568abf286492d307f2cd19a95b8b5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d08e97172319a01e37722183a9846b9a650c87dd7b52a25204a7f98acaa0bfc(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be03a72a7df8f155d7a82bf5020bb8673e25a9ea536e18a62d58929f55f65efe(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__daf9b504c9a793ec2629730b9de39aabdcbde0c5919bd4e7a45cad1f26f96e15(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b58aa9050e76fa87ad8fc3a835f4d0d214b7a0f73b003ed74e3690ccf40a2224(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    migration_type: builtins.str,
    replication_instance_arn: builtins.str,
    replication_task_id: builtins.str,
    source_endpoint_arn: builtins.str,
    table_mappings: builtins.str,
    target_endpoint_arn: builtins.str,
    cdc_start_position: typing.Optional[builtins.str] = None,
    cdc_start_time: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    replication_task_settings: typing.Optional[builtins.str] = None,
    start_replication_task: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
