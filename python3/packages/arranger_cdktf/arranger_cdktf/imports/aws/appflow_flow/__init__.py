'''
# `aws_appflow_flow`

Refer to the Terraform Registory for docs: [`aws_appflow_flow`](https://www.terraform.io/docs/providers/aws/r/appflow_flow).
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


class AppflowFlow(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlow",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow aws_appflow_flow}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        destination_flow_config: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AppflowFlowDestinationFlowConfig", typing.Dict[builtins.str, typing.Any]]]],
        name: builtins.str,
        source_flow_config: typing.Union["AppflowFlowSourceFlowConfig", typing.Dict[builtins.str, typing.Any]],
        task: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AppflowFlowTask", typing.Dict[builtins.str, typing.Any]]]],
        trigger_config: typing.Union["AppflowFlowTriggerConfig", typing.Dict[builtins.str, typing.Any]],
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        kms_arn: typing.Optional[builtins.str] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow aws_appflow_flow} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param destination_flow_config: destination_flow_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#destination_flow_config AppflowFlow#destination_flow_config}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#name AppflowFlow#name}.
        :param source_flow_config: source_flow_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#source_flow_config AppflowFlow#source_flow_config}
        :param task: task block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#task AppflowFlow#task}
        :param trigger_config: trigger_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#trigger_config AppflowFlow#trigger_config}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#description AppflowFlow#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#id AppflowFlow#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kms_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#kms_arn AppflowFlow#kms_arn}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#tags AppflowFlow#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#tags_all AppflowFlow#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05a923e7604d13822e0a12c550ed0d1bee650c17dfe0c4f8095e74a82c87a060)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AppflowFlowConfig(
            destination_flow_config=destination_flow_config,
            name=name,
            source_flow_config=source_flow_config,
            task=task,
            trigger_config=trigger_config,
            description=description,
            id=id,
            kms_arn=kms_arn,
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

    @jsii.member(jsii_name="putDestinationFlowConfig")
    def put_destination_flow_config(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AppflowFlowDestinationFlowConfig", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eed448eee19fd6120b079fccd55f64eafb67b0464723f2843b78ab5e18fb7b3b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDestinationFlowConfig", [value]))

    @jsii.member(jsii_name="putSourceFlowConfig")
    def put_source_flow_config(
        self,
        *,
        connector_type: builtins.str,
        source_connector_properties: typing.Union["AppflowFlowSourceFlowConfigSourceConnectorProperties", typing.Dict[builtins.str, typing.Any]],
        api_version: typing.Optional[builtins.str] = None,
        connector_profile_name: typing.Optional[builtins.str] = None,
        incremental_pull_config: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigIncrementalPullConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connector_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#connector_type AppflowFlow#connector_type}.
        :param source_connector_properties: source_connector_properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#source_connector_properties AppflowFlow#source_connector_properties}
        :param api_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#api_version AppflowFlow#api_version}.
        :param connector_profile_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#connector_profile_name AppflowFlow#connector_profile_name}.
        :param incremental_pull_config: incremental_pull_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#incremental_pull_config AppflowFlow#incremental_pull_config}
        '''
        value = AppflowFlowSourceFlowConfig(
            connector_type=connector_type,
            source_connector_properties=source_connector_properties,
            api_version=api_version,
            connector_profile_name=connector_profile_name,
            incremental_pull_config=incremental_pull_config,
        )

        return typing.cast(None, jsii.invoke(self, "putSourceFlowConfig", [value]))

    @jsii.member(jsii_name="putTask")
    def put_task(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AppflowFlowTask", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1a8d716f42d7616486476f065b0283d9615ea757e4fcbfe78c5f9e07ed19b6b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTask", [value]))

    @jsii.member(jsii_name="putTriggerConfig")
    def put_trigger_config(
        self,
        *,
        trigger_type: builtins.str,
        trigger_properties: typing.Optional[typing.Union["AppflowFlowTriggerConfigTriggerProperties", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param trigger_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#trigger_type AppflowFlow#trigger_type}.
        :param trigger_properties: trigger_properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#trigger_properties AppflowFlow#trigger_properties}
        '''
        value = AppflowFlowTriggerConfig(
            trigger_type=trigger_type, trigger_properties=trigger_properties
        )

        return typing.cast(None, jsii.invoke(self, "putTriggerConfig", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetKmsArn")
    def reset_kms_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsArn", []))

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
    @jsii.member(jsii_name="destinationFlowConfig")
    def destination_flow_config(self) -> "AppflowFlowDestinationFlowConfigList":
        return typing.cast("AppflowFlowDestinationFlowConfigList", jsii.get(self, "destinationFlowConfig"))

    @builtins.property
    @jsii.member(jsii_name="sourceFlowConfig")
    def source_flow_config(self) -> "AppflowFlowSourceFlowConfigOutputReference":
        return typing.cast("AppflowFlowSourceFlowConfigOutputReference", jsii.get(self, "sourceFlowConfig"))

    @builtins.property
    @jsii.member(jsii_name="task")
    def task(self) -> "AppflowFlowTaskList":
        return typing.cast("AppflowFlowTaskList", jsii.get(self, "task"))

    @builtins.property
    @jsii.member(jsii_name="triggerConfig")
    def trigger_config(self) -> "AppflowFlowTriggerConfigOutputReference":
        return typing.cast("AppflowFlowTriggerConfigOutputReference", jsii.get(self, "triggerConfig"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationFlowConfigInput")
    def destination_flow_config_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppflowFlowDestinationFlowConfig"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppflowFlowDestinationFlowConfig"]]], jsii.get(self, "destinationFlowConfigInput"))

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
    @jsii.member(jsii_name="sourceFlowConfigInput")
    def source_flow_config_input(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfig"]:
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfig"], jsii.get(self, "sourceFlowConfigInput"))

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
    @jsii.member(jsii_name="taskInput")
    def task_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppflowFlowTask"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppflowFlowTask"]]], jsii.get(self, "taskInput"))

    @builtins.property
    @jsii.member(jsii_name="triggerConfigInput")
    def trigger_config_input(self) -> typing.Optional["AppflowFlowTriggerConfig"]:
        return typing.cast(typing.Optional["AppflowFlowTriggerConfig"], jsii.get(self, "triggerConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__959255a5a4cbdf34a255cddd2444dfc2b2519b39c9f26239fb2e867bef2e8ff9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc8014ff3b3ef9c53e08a49a049c29511495e015254d6a34946120f1ab0c8abb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="kmsArn")
    def kms_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsArn"))

    @kms_arn.setter
    def kms_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0abdb9cf2033198a136fa533e92da4aac2f68cd86c5b4b48dee58dbac28ea83a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsArn", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3662c5d5a963e44bc47bdc0e8e58c584e410e32c1d3e7de5b60b8d429c0bf6af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95de1e8f9f2f36fcbf7ea6bed532a897505c6817811338c4ec0f9c9d941f03ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abc4cc562fc4a5ef08d6a1e36107d1ba2c35e315d8cff49faa9849eac621df1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "destination_flow_config": "destinationFlowConfig",
        "name": "name",
        "source_flow_config": "sourceFlowConfig",
        "task": "task",
        "trigger_config": "triggerConfig",
        "description": "description",
        "id": "id",
        "kms_arn": "kmsArn",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class AppflowFlowConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        destination_flow_config: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AppflowFlowDestinationFlowConfig", typing.Dict[builtins.str, typing.Any]]]],
        name: builtins.str,
        source_flow_config: typing.Union["AppflowFlowSourceFlowConfig", typing.Dict[builtins.str, typing.Any]],
        task: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AppflowFlowTask", typing.Dict[builtins.str, typing.Any]]]],
        trigger_config: typing.Union["AppflowFlowTriggerConfig", typing.Dict[builtins.str, typing.Any]],
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        kms_arn: typing.Optional[builtins.str] = None,
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
        :param destination_flow_config: destination_flow_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#destination_flow_config AppflowFlow#destination_flow_config}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#name AppflowFlow#name}.
        :param source_flow_config: source_flow_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#source_flow_config AppflowFlow#source_flow_config}
        :param task: task block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#task AppflowFlow#task}
        :param trigger_config: trigger_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#trigger_config AppflowFlow#trigger_config}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#description AppflowFlow#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#id AppflowFlow#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kms_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#kms_arn AppflowFlow#kms_arn}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#tags AppflowFlow#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#tags_all AppflowFlow#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(source_flow_config, dict):
            source_flow_config = AppflowFlowSourceFlowConfig(**source_flow_config)
        if isinstance(trigger_config, dict):
            trigger_config = AppflowFlowTriggerConfig(**trigger_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2254fa09fd787cadb62b3f7b10554beec5c354668649a224dbb438ab0e4b895d)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument destination_flow_config", value=destination_flow_config, expected_type=type_hints["destination_flow_config"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument source_flow_config", value=source_flow_config, expected_type=type_hints["source_flow_config"])
            check_type(argname="argument task", value=task, expected_type=type_hints["task"])
            check_type(argname="argument trigger_config", value=trigger_config, expected_type=type_hints["trigger_config"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument kms_arn", value=kms_arn, expected_type=type_hints["kms_arn"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination_flow_config": destination_flow_config,
            "name": name,
            "source_flow_config": source_flow_config,
            "task": task,
            "trigger_config": trigger_config,
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
        if kms_arn is not None:
            self._values["kms_arn"] = kms_arn
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
    def destination_flow_config(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppflowFlowDestinationFlowConfig"]]:
        '''destination_flow_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#destination_flow_config AppflowFlow#destination_flow_config}
        '''
        result = self._values.get("destination_flow_config")
        assert result is not None, "Required property 'destination_flow_config' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppflowFlowDestinationFlowConfig"]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#name AppflowFlow#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_flow_config(self) -> "AppflowFlowSourceFlowConfig":
        '''source_flow_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#source_flow_config AppflowFlow#source_flow_config}
        '''
        result = self._values.get("source_flow_config")
        assert result is not None, "Required property 'source_flow_config' is missing"
        return typing.cast("AppflowFlowSourceFlowConfig", result)

    @builtins.property
    def task(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppflowFlowTask"]]:
        '''task block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#task AppflowFlow#task}
        '''
        result = self._values.get("task")
        assert result is not None, "Required property 'task' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppflowFlowTask"]], result)

    @builtins.property
    def trigger_config(self) -> "AppflowFlowTriggerConfig":
        '''trigger_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#trigger_config AppflowFlow#trigger_config}
        '''
        result = self._values.get("trigger_config")
        assert result is not None, "Required property 'trigger_config' is missing"
        return typing.cast("AppflowFlowTriggerConfig", result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#description AppflowFlow#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#id AppflowFlow#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#kms_arn AppflowFlow#kms_arn}.'''
        result = self._values.get("kms_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#tags AppflowFlow#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#tags_all AppflowFlow#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfig",
    jsii_struct_bases=[],
    name_mapping={
        "connector_type": "connectorType",
        "destination_connector_properties": "destinationConnectorProperties",
        "api_version": "apiVersion",
        "connector_profile_name": "connectorProfileName",
    },
)
class AppflowFlowDestinationFlowConfig:
    def __init__(
        self,
        *,
        connector_type: builtins.str,
        destination_connector_properties: typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorProperties", typing.Dict[builtins.str, typing.Any]],
        api_version: typing.Optional[builtins.str] = None,
        connector_profile_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connector_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#connector_type AppflowFlow#connector_type}.
        :param destination_connector_properties: destination_connector_properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#destination_connector_properties AppflowFlow#destination_connector_properties}
        :param api_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#api_version AppflowFlow#api_version}.
        :param connector_profile_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#connector_profile_name AppflowFlow#connector_profile_name}.
        '''
        if isinstance(destination_connector_properties, dict):
            destination_connector_properties = AppflowFlowDestinationFlowConfigDestinationConnectorProperties(**destination_connector_properties)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8604fffeb1c50bc571738d80359061b9b51a5aead9b5948e68d8f9ed22f8e68)
            check_type(argname="argument connector_type", value=connector_type, expected_type=type_hints["connector_type"])
            check_type(argname="argument destination_connector_properties", value=destination_connector_properties, expected_type=type_hints["destination_connector_properties"])
            check_type(argname="argument api_version", value=api_version, expected_type=type_hints["api_version"])
            check_type(argname="argument connector_profile_name", value=connector_profile_name, expected_type=type_hints["connector_profile_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "connector_type": connector_type,
            "destination_connector_properties": destination_connector_properties,
        }
        if api_version is not None:
            self._values["api_version"] = api_version
        if connector_profile_name is not None:
            self._values["connector_profile_name"] = connector_profile_name

    @builtins.property
    def connector_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#connector_type AppflowFlow#connector_type}.'''
        result = self._values.get("connector_type")
        assert result is not None, "Required property 'connector_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def destination_connector_properties(
        self,
    ) -> "AppflowFlowDestinationFlowConfigDestinationConnectorProperties":
        '''destination_connector_properties block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#destination_connector_properties AppflowFlow#destination_connector_properties}
        '''
        result = self._values.get("destination_connector_properties")
        assert result is not None, "Required property 'destination_connector_properties' is missing"
        return typing.cast("AppflowFlowDestinationFlowConfigDestinationConnectorProperties", result)

    @builtins.property
    def api_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#api_version AppflowFlow#api_version}.'''
        result = self._values.get("api_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def connector_profile_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#connector_profile_name AppflowFlow#connector_profile_name}.'''
        result = self._values.get("connector_profile_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorProperties",
    jsii_struct_bases=[],
    name_mapping={
        "custom_connector": "customConnector",
        "customer_profiles": "customerProfiles",
        "event_bridge": "eventBridge",
        "honeycode": "honeycode",
        "lookout_metrics": "lookoutMetrics",
        "marketo": "marketo",
        "redshift": "redshift",
        "s3": "s3",
        "salesforce": "salesforce",
        "sapo_data": "sapoData",
        "snowflake": "snowflake",
        "upsolver": "upsolver",
        "zendesk": "zendesk",
    },
)
class AppflowFlowDestinationFlowConfigDestinationConnectorProperties:
    def __init__(
        self,
        *,
        custom_connector: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnector", typing.Dict[builtins.str, typing.Any]]] = None,
        customer_profiles: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfiles", typing.Dict[builtins.str, typing.Any]]] = None,
        event_bridge: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridge", typing.Dict[builtins.str, typing.Any]]] = None,
        honeycode: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycode", typing.Dict[builtins.str, typing.Any]]] = None,
        lookout_metrics: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetrics", typing.Dict[builtins.str, typing.Any]]] = None,
        marketo: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketo", typing.Dict[builtins.str, typing.Any]]] = None,
        redshift: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshift", typing.Dict[builtins.str, typing.Any]]] = None,
        s3: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3", typing.Dict[builtins.str, typing.Any]]] = None,
        salesforce: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforce", typing.Dict[builtins.str, typing.Any]]] = None,
        sapo_data: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoData", typing.Dict[builtins.str, typing.Any]]] = None,
        snowflake: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflake", typing.Dict[builtins.str, typing.Any]]] = None,
        upsolver: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolver", typing.Dict[builtins.str, typing.Any]]] = None,
        zendesk: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendesk", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param custom_connector: custom_connector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#custom_connector AppflowFlow#custom_connector}
        :param customer_profiles: customer_profiles block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#customer_profiles AppflowFlow#customer_profiles}
        :param event_bridge: event_bridge block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#event_bridge AppflowFlow#event_bridge}
        :param honeycode: honeycode block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#honeycode AppflowFlow#honeycode}
        :param lookout_metrics: lookout_metrics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#lookout_metrics AppflowFlow#lookout_metrics}
        :param marketo: marketo block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#marketo AppflowFlow#marketo}
        :param redshift: redshift block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#redshift AppflowFlow#redshift}
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#s3 AppflowFlow#s3}
        :param salesforce: salesforce block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#salesforce AppflowFlow#salesforce}
        :param sapo_data: sapo_data block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#sapo_data AppflowFlow#sapo_data}
        :param snowflake: snowflake block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#snowflake AppflowFlow#snowflake}
        :param upsolver: upsolver block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#upsolver AppflowFlow#upsolver}
        :param zendesk: zendesk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#zendesk AppflowFlow#zendesk}
        '''
        if isinstance(custom_connector, dict):
            custom_connector = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnector(**custom_connector)
        if isinstance(customer_profiles, dict):
            customer_profiles = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfiles(**customer_profiles)
        if isinstance(event_bridge, dict):
            event_bridge = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridge(**event_bridge)
        if isinstance(honeycode, dict):
            honeycode = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycode(**honeycode)
        if isinstance(lookout_metrics, dict):
            lookout_metrics = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetrics(**lookout_metrics)
        if isinstance(marketo, dict):
            marketo = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketo(**marketo)
        if isinstance(redshift, dict):
            redshift = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshift(**redshift)
        if isinstance(s3, dict):
            s3 = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3(**s3)
        if isinstance(salesforce, dict):
            salesforce = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforce(**salesforce)
        if isinstance(sapo_data, dict):
            sapo_data = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoData(**sapo_data)
        if isinstance(snowflake, dict):
            snowflake = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflake(**snowflake)
        if isinstance(upsolver, dict):
            upsolver = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolver(**upsolver)
        if isinstance(zendesk, dict):
            zendesk = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendesk(**zendesk)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42d8fd30b8f4a1daf79b13dfcbbe53fe6dbd7268f959e3be7ea1395f42c9161a)
            check_type(argname="argument custom_connector", value=custom_connector, expected_type=type_hints["custom_connector"])
            check_type(argname="argument customer_profiles", value=customer_profiles, expected_type=type_hints["customer_profiles"])
            check_type(argname="argument event_bridge", value=event_bridge, expected_type=type_hints["event_bridge"])
            check_type(argname="argument honeycode", value=honeycode, expected_type=type_hints["honeycode"])
            check_type(argname="argument lookout_metrics", value=lookout_metrics, expected_type=type_hints["lookout_metrics"])
            check_type(argname="argument marketo", value=marketo, expected_type=type_hints["marketo"])
            check_type(argname="argument redshift", value=redshift, expected_type=type_hints["redshift"])
            check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
            check_type(argname="argument salesforce", value=salesforce, expected_type=type_hints["salesforce"])
            check_type(argname="argument sapo_data", value=sapo_data, expected_type=type_hints["sapo_data"])
            check_type(argname="argument snowflake", value=snowflake, expected_type=type_hints["snowflake"])
            check_type(argname="argument upsolver", value=upsolver, expected_type=type_hints["upsolver"])
            check_type(argname="argument zendesk", value=zendesk, expected_type=type_hints["zendesk"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if custom_connector is not None:
            self._values["custom_connector"] = custom_connector
        if customer_profiles is not None:
            self._values["customer_profiles"] = customer_profiles
        if event_bridge is not None:
            self._values["event_bridge"] = event_bridge
        if honeycode is not None:
            self._values["honeycode"] = honeycode
        if lookout_metrics is not None:
            self._values["lookout_metrics"] = lookout_metrics
        if marketo is not None:
            self._values["marketo"] = marketo
        if redshift is not None:
            self._values["redshift"] = redshift
        if s3 is not None:
            self._values["s3"] = s3
        if salesforce is not None:
            self._values["salesforce"] = salesforce
        if sapo_data is not None:
            self._values["sapo_data"] = sapo_data
        if snowflake is not None:
            self._values["snowflake"] = snowflake
        if upsolver is not None:
            self._values["upsolver"] = upsolver
        if zendesk is not None:
            self._values["zendesk"] = zendesk

    @builtins.property
    def custom_connector(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnector"]:
        '''custom_connector block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#custom_connector AppflowFlow#custom_connector}
        '''
        result = self._values.get("custom_connector")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnector"], result)

    @builtins.property
    def customer_profiles(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfiles"]:
        '''customer_profiles block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#customer_profiles AppflowFlow#customer_profiles}
        '''
        result = self._values.get("customer_profiles")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfiles"], result)

    @builtins.property
    def event_bridge(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridge"]:
        '''event_bridge block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#event_bridge AppflowFlow#event_bridge}
        '''
        result = self._values.get("event_bridge")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridge"], result)

    @builtins.property
    def honeycode(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycode"]:
        '''honeycode block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#honeycode AppflowFlow#honeycode}
        '''
        result = self._values.get("honeycode")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycode"], result)

    @builtins.property
    def lookout_metrics(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetrics"]:
        '''lookout_metrics block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#lookout_metrics AppflowFlow#lookout_metrics}
        '''
        result = self._values.get("lookout_metrics")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetrics"], result)

    @builtins.property
    def marketo(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketo"]:
        '''marketo block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#marketo AppflowFlow#marketo}
        '''
        result = self._values.get("marketo")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketo"], result)

    @builtins.property
    def redshift(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshift"]:
        '''redshift block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#redshift AppflowFlow#redshift}
        '''
        result = self._values.get("redshift")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshift"], result)

    @builtins.property
    def s3(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3"]:
        '''s3 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#s3 AppflowFlow#s3}
        '''
        result = self._values.get("s3")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3"], result)

    @builtins.property
    def salesforce(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforce"]:
        '''salesforce block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#salesforce AppflowFlow#salesforce}
        '''
        result = self._values.get("salesforce")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforce"], result)

    @builtins.property
    def sapo_data(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoData"]:
        '''sapo_data block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#sapo_data AppflowFlow#sapo_data}
        '''
        result = self._values.get("sapo_data")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoData"], result)

    @builtins.property
    def snowflake(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflake"]:
        '''snowflake block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#snowflake AppflowFlow#snowflake}
        '''
        result = self._values.get("snowflake")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflake"], result)

    @builtins.property
    def upsolver(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolver"]:
        '''upsolver block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#upsolver AppflowFlow#upsolver}
        '''
        result = self._values.get("upsolver")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolver"], result)

    @builtins.property
    def zendesk(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendesk"]:
        '''zendesk block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#zendesk AppflowFlow#zendesk}
        '''
        result = self._values.get("zendesk")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendesk"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorProperties(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnector",
    jsii_struct_bases=[],
    name_mapping={
        "entity_name": "entityName",
        "custom_properties": "customProperties",
        "error_handling_config": "errorHandlingConfig",
        "id_field_names": "idFieldNames",
        "write_operation_type": "writeOperationType",
    },
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnector:
    def __init__(
        self,
        *,
        entity_name: builtins.str,
        custom_properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        error_handling_config: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        id_field_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        write_operation_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param entity_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#entity_name AppflowFlow#entity_name}.
        :param custom_properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#custom_properties AppflowFlow#custom_properties}.
        :param error_handling_config: error_handling_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        :param id_field_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#id_field_names AppflowFlow#id_field_names}.
        :param write_operation_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#write_operation_type AppflowFlow#write_operation_type}.
        '''
        if isinstance(error_handling_config, dict):
            error_handling_config = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfig(**error_handling_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb391a5cd3439d4671b618a7e1a20a1a9bab4aad8353d5bd0321c5c84658098f)
            check_type(argname="argument entity_name", value=entity_name, expected_type=type_hints["entity_name"])
            check_type(argname="argument custom_properties", value=custom_properties, expected_type=type_hints["custom_properties"])
            check_type(argname="argument error_handling_config", value=error_handling_config, expected_type=type_hints["error_handling_config"])
            check_type(argname="argument id_field_names", value=id_field_names, expected_type=type_hints["id_field_names"])
            check_type(argname="argument write_operation_type", value=write_operation_type, expected_type=type_hints["write_operation_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "entity_name": entity_name,
        }
        if custom_properties is not None:
            self._values["custom_properties"] = custom_properties
        if error_handling_config is not None:
            self._values["error_handling_config"] = error_handling_config
        if id_field_names is not None:
            self._values["id_field_names"] = id_field_names
        if write_operation_type is not None:
            self._values["write_operation_type"] = write_operation_type

    @builtins.property
    def entity_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#entity_name AppflowFlow#entity_name}.'''
        result = self._values.get("entity_name")
        assert result is not None, "Required property 'entity_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def custom_properties(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#custom_properties AppflowFlow#custom_properties}.'''
        result = self._values.get("custom_properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def error_handling_config(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfig"]:
        '''error_handling_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        '''
        result = self._values.get("error_handling_config")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfig"], result)

    @builtins.property
    def id_field_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#id_field_names AppflowFlow#id_field_names}.'''
        result = self._values.get("id_field_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def write_operation_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#write_operation_type AppflowFlow#write_operation_type}.'''
        result = self._values.get("write_operation_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfig",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "bucket_prefix": "bucketPrefix",
        "fail_on_first_destination_error": "failOnFirstDestinationError",
    },
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfig:
    def __init__(
        self,
        *,
        bucket_name: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param fail_on_first_destination_error: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bead7b889e70eaa0a07577d92cbc6a2a8c98600a829371f23ed2cf9063fde654)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
            check_type(argname="argument fail_on_first_destination_error", value=fail_on_first_destination_error, expected_type=type_hints["fail_on_first_destination_error"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if bucket_name is not None:
            self._values["bucket_name"] = bucket_name
        if bucket_prefix is not None:
            self._values["bucket_prefix"] = bucket_prefix
        if fail_on_first_destination_error is not None:
            self._values["fail_on_first_destination_error"] = fail_on_first_destination_error

    @builtins.property
    def bucket_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.'''
        result = self._values.get("bucket_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.'''
        result = self._values.get("bucket_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fail_on_first_destination_error(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.'''
        result = self._values.get("fail_on_first_destination_error")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5f54b5d158acfab6b1811c483af35edc02fe3eb39cf8a393de4b5146b0d2a6e8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBucketName")
    def reset_bucket_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketName", []))

    @jsii.member(jsii_name="resetBucketPrefix")
    def reset_bucket_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketPrefix", []))

    @jsii.member(jsii_name="resetFailOnFirstDestinationError")
    def reset_fail_on_first_destination_error(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailOnFirstDestinationError", []))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketPrefixInput")
    def bucket_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="failOnFirstDestinationErrorInput")
    def fail_on_first_destination_error_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "failOnFirstDestinationErrorInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c679b9e808835d3f244f43484415fa3efcf3b7cdcd37365f660e7fd1f7d28834)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="bucketPrefix")
    def bucket_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketPrefix"))

    @bucket_prefix.setter
    def bucket_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71dd6b17d67474d4d846df4ac1ca90432552778817de0ca11fa8f5e9a96a7157)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="failOnFirstDestinationError")
    def fail_on_first_destination_error(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "failOnFirstDestinationError"))

    @fail_on_first_destination_error.setter
    def fail_on_first_destination_error(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94532d3628b17764e554fcea55bb16ff812e4cc63a0d51b521945bf536f1a5ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failOnFirstDestinationError", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__847430025085d9f5665ba05d6198406872f96624c18f5d8df80e487134eff4ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e90d351226d1cd9e57558f42a17be55d97ce09709fcd827f55c1e5117eef039b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putErrorHandlingConfig")
    def put_error_handling_config(
        self,
        *,
        bucket_name: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param fail_on_first_destination_error: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfig(
            bucket_name=bucket_name,
            bucket_prefix=bucket_prefix,
            fail_on_first_destination_error=fail_on_first_destination_error,
        )

        return typing.cast(None, jsii.invoke(self, "putErrorHandlingConfig", [value]))

    @jsii.member(jsii_name="resetCustomProperties")
    def reset_custom_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomProperties", []))

    @jsii.member(jsii_name="resetErrorHandlingConfig")
    def reset_error_handling_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetErrorHandlingConfig", []))

    @jsii.member(jsii_name="resetIdFieldNames")
    def reset_id_field_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdFieldNames", []))

    @jsii.member(jsii_name="resetWriteOperationType")
    def reset_write_operation_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWriteOperationType", []))

    @builtins.property
    @jsii.member(jsii_name="errorHandlingConfig")
    def error_handling_config(
        self,
    ) -> AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfigOutputReference:
        return typing.cast(AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfigOutputReference, jsii.get(self, "errorHandlingConfig"))

    @builtins.property
    @jsii.member(jsii_name="customPropertiesInput")
    def custom_properties_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "customPropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="entityNameInput")
    def entity_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "entityNameInput"))

    @builtins.property
    @jsii.member(jsii_name="errorHandlingConfigInput")
    def error_handling_config_input(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfig], jsii.get(self, "errorHandlingConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="idFieldNamesInput")
    def id_field_names_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "idFieldNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="writeOperationTypeInput")
    def write_operation_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "writeOperationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="customProperties")
    def custom_properties(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "customProperties"))

    @custom_properties.setter
    def custom_properties(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08451f778a951a04ce4ec6e4f1e700c11d5490aca41f13936c0c1036c00d5e2e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customProperties", value)

    @builtins.property
    @jsii.member(jsii_name="entityName")
    def entity_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "entityName"))

    @entity_name.setter
    def entity_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54abf8fd0e6ff0aba06be4d0c546c4559b620a5c02d8a0611b111fdacc7ea691)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "entityName", value)

    @builtins.property
    @jsii.member(jsii_name="idFieldNames")
    def id_field_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "idFieldNames"))

    @id_field_names.setter
    def id_field_names(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1391a1cc817dd79d9ec764d5156595f410ec8c6769ae37a3c5522fe07879171)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idFieldNames", value)

    @builtins.property
    @jsii.member(jsii_name="writeOperationType")
    def write_operation_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "writeOperationType"))

    @write_operation_type.setter
    def write_operation_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43a81522a972a572846b7b1c7eb502796480e88693755c820199576c756b422c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "writeOperationType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnector]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnector], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnector],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__423c4eda543d65d4086de28dc88c836c2aef6ae61d30aa5c16651a1fc8d87a45)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfiles",
    jsii_struct_bases=[],
    name_mapping={"domain_name": "domainName", "object_type_name": "objectTypeName"},
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfiles:
    def __init__(
        self,
        *,
        domain_name: builtins.str,
        object_type_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#domain_name AppflowFlow#domain_name}.
        :param object_type_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object_type_name AppflowFlow#object_type_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__429c47cc24ab75431afd897c801f977f56aaec630156c5bc0dfb86ced171d797)
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument object_type_name", value=object_type_name, expected_type=type_hints["object_type_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_name": domain_name,
        }
        if object_type_name is not None:
            self._values["object_type_name"] = object_type_name

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#domain_name AppflowFlow#domain_name}.'''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def object_type_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object_type_name AppflowFlow#object_type_name}.'''
        result = self._values.get("object_type_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfiles(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfilesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfilesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__33a9255fc287c95ba820fab8eaf843925d4033315f0b4f8ac1cb269428a6936b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetObjectTypeName")
    def reset_object_type_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetObjectTypeName", []))

    @builtins.property
    @jsii.member(jsii_name="domainNameInput")
    def domain_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainNameInput"))

    @builtins.property
    @jsii.member(jsii_name="objectTypeNameInput")
    def object_type_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectTypeNameInput"))

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9eb2b8941245145a7f823a22dcb5ac57329e83ba94360b52de8800babee067c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value)

    @builtins.property
    @jsii.member(jsii_name="objectTypeName")
    def object_type_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "objectTypeName"))

    @object_type_name.setter
    def object_type_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2d8e76c0931b138253bdae46851ed85a7152b1fa7b294c93f6f33c19b1e6eaf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectTypeName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfiles]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfiles], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfiles],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78ff742668016f2f323e74cf9e371a8ac7d9090f32b2ea63f831aa6a846818cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridge",
    jsii_struct_bases=[],
    name_mapping={"object": "object", "error_handling_config": "errorHandlingConfig"},
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridge:
    def __init__(
        self,
        *,
        object: builtins.str,
        error_handling_config: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        :param error_handling_config: error_handling_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        '''
        if isinstance(error_handling_config, dict):
            error_handling_config = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfig(**error_handling_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfa8ca51fd6553cd7108945080e2dba16bfcf80118b8f7f5d8c19d951baa9b1b)
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
            check_type(argname="argument error_handling_config", value=error_handling_config, expected_type=type_hints["error_handling_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "object": object,
        }
        if error_handling_config is not None:
            self._values["error_handling_config"] = error_handling_config

    @builtins.property
    def object(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.'''
        result = self._values.get("object")
        assert result is not None, "Required property 'object' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def error_handling_config(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfig"]:
        '''error_handling_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        '''
        result = self._values.get("error_handling_config")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridge(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfig",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "bucket_prefix": "bucketPrefix",
        "fail_on_first_destination_error": "failOnFirstDestinationError",
    },
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfig:
    def __init__(
        self,
        *,
        bucket_name: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param fail_on_first_destination_error: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18a6ba4aebd83dfe0d561a52865e8ff2329742070024f1b310dff4cd5046e2a5)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
            check_type(argname="argument fail_on_first_destination_error", value=fail_on_first_destination_error, expected_type=type_hints["fail_on_first_destination_error"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if bucket_name is not None:
            self._values["bucket_name"] = bucket_name
        if bucket_prefix is not None:
            self._values["bucket_prefix"] = bucket_prefix
        if fail_on_first_destination_error is not None:
            self._values["fail_on_first_destination_error"] = fail_on_first_destination_error

    @builtins.property
    def bucket_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.'''
        result = self._values.get("bucket_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.'''
        result = self._values.get("bucket_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fail_on_first_destination_error(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.'''
        result = self._values.get("fail_on_first_destination_error")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e55b1eb1f3655da97510cde333931a4773010b7b805a5e44baeaec2099c2bf0d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBucketName")
    def reset_bucket_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketName", []))

    @jsii.member(jsii_name="resetBucketPrefix")
    def reset_bucket_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketPrefix", []))

    @jsii.member(jsii_name="resetFailOnFirstDestinationError")
    def reset_fail_on_first_destination_error(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailOnFirstDestinationError", []))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketPrefixInput")
    def bucket_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="failOnFirstDestinationErrorInput")
    def fail_on_first_destination_error_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "failOnFirstDestinationErrorInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d320316c508f42c776919dfbcafdc536fa836ba9a289e64b25f3a7d581cd4e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="bucketPrefix")
    def bucket_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketPrefix"))

    @bucket_prefix.setter
    def bucket_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b7ca18cec3cefd1ee2c33318fee82ebe79ebbc0c15b487dd3dd8c42278dfbcf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="failOnFirstDestinationError")
    def fail_on_first_destination_error(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "failOnFirstDestinationError"))

    @fail_on_first_destination_error.setter
    def fail_on_first_destination_error(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab9da726ac35776f49794fa4d12a8d27740c6d4f9611e986f45cf7b97416af00)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failOnFirstDestinationError", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6a51293146c340718e4c7928019bf9a5cbabc023e5e755f2d6c59d9ecd6164e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__868e410705d0633313164cdf0d2b5ce3c35f6b558ef5bd0371d85ae3d43a79b3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putErrorHandlingConfig")
    def put_error_handling_config(
        self,
        *,
        bucket_name: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param fail_on_first_destination_error: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfig(
            bucket_name=bucket_name,
            bucket_prefix=bucket_prefix,
            fail_on_first_destination_error=fail_on_first_destination_error,
        )

        return typing.cast(None, jsii.invoke(self, "putErrorHandlingConfig", [value]))

    @jsii.member(jsii_name="resetErrorHandlingConfig")
    def reset_error_handling_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetErrorHandlingConfig", []))

    @builtins.property
    @jsii.member(jsii_name="errorHandlingConfig")
    def error_handling_config(
        self,
    ) -> AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfigOutputReference:
        return typing.cast(AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfigOutputReference, jsii.get(self, "errorHandlingConfig"))

    @builtins.property
    @jsii.member(jsii_name="errorHandlingConfigInput")
    def error_handling_config_input(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfig], jsii.get(self, "errorHandlingConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="objectInput")
    def object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "object"))

    @object.setter
    def object(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e23834d96dcdbb186fc5e8785ce82fbbc2dbfb542f41f3d15cb80dfcfc4dcf0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "object", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridge]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridge], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridge],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed0dff519639125d8b82d24062444bd304aed498b53e76e2e120687be7260142)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycode",
    jsii_struct_bases=[],
    name_mapping={"object": "object", "error_handling_config": "errorHandlingConfig"},
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycode:
    def __init__(
        self,
        *,
        object: builtins.str,
        error_handling_config: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        :param error_handling_config: error_handling_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        '''
        if isinstance(error_handling_config, dict):
            error_handling_config = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfig(**error_handling_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8178942c23e0013761979ec005db3742768f7afdcd987842b0f584f65aa5f758)
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
            check_type(argname="argument error_handling_config", value=error_handling_config, expected_type=type_hints["error_handling_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "object": object,
        }
        if error_handling_config is not None:
            self._values["error_handling_config"] = error_handling_config

    @builtins.property
    def object(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.'''
        result = self._values.get("object")
        assert result is not None, "Required property 'object' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def error_handling_config(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfig"]:
        '''error_handling_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        '''
        result = self._values.get("error_handling_config")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycode(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfig",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "bucket_prefix": "bucketPrefix",
        "fail_on_first_destination_error": "failOnFirstDestinationError",
    },
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfig:
    def __init__(
        self,
        *,
        bucket_name: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param fail_on_first_destination_error: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7648cc52c43f8082b603dcf5f2c6bfa4cad0bfc940b9269bd42a32ed5c21b3b)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
            check_type(argname="argument fail_on_first_destination_error", value=fail_on_first_destination_error, expected_type=type_hints["fail_on_first_destination_error"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if bucket_name is not None:
            self._values["bucket_name"] = bucket_name
        if bucket_prefix is not None:
            self._values["bucket_prefix"] = bucket_prefix
        if fail_on_first_destination_error is not None:
            self._values["fail_on_first_destination_error"] = fail_on_first_destination_error

    @builtins.property
    def bucket_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.'''
        result = self._values.get("bucket_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.'''
        result = self._values.get("bucket_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fail_on_first_destination_error(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.'''
        result = self._values.get("fail_on_first_destination_error")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7a6232feda1fee0d67a0fb02c314a78709cfbc8350a48e958be41cbcb3f251c6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBucketName")
    def reset_bucket_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketName", []))

    @jsii.member(jsii_name="resetBucketPrefix")
    def reset_bucket_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketPrefix", []))

    @jsii.member(jsii_name="resetFailOnFirstDestinationError")
    def reset_fail_on_first_destination_error(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailOnFirstDestinationError", []))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketPrefixInput")
    def bucket_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="failOnFirstDestinationErrorInput")
    def fail_on_first_destination_error_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "failOnFirstDestinationErrorInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39a99edb57032c61a0fe1b100c6b2bcce5fb68de26f91696cdea72b490a30630)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="bucketPrefix")
    def bucket_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketPrefix"))

    @bucket_prefix.setter
    def bucket_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__347e1877d9a0d7d827982512eaf788e85c2f0bda84c2a3e8a7fe3f4537d49d77)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="failOnFirstDestinationError")
    def fail_on_first_destination_error(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "failOnFirstDestinationError"))

    @fail_on_first_destination_error.setter
    def fail_on_first_destination_error(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ccc72b819a5910c80d631c9504df6907cacb505fd6c2696f8dffeea091253d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failOnFirstDestinationError", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d316e6a2eba63b48b9cd67a0b98750c9bb0bdcec754b749c0f3a5a04893e4c91)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2f89d06c1d4b3b73b4be3034f3881e1d5657b7215ad998db2f145e973f47196b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putErrorHandlingConfig")
    def put_error_handling_config(
        self,
        *,
        bucket_name: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param fail_on_first_destination_error: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfig(
            bucket_name=bucket_name,
            bucket_prefix=bucket_prefix,
            fail_on_first_destination_error=fail_on_first_destination_error,
        )

        return typing.cast(None, jsii.invoke(self, "putErrorHandlingConfig", [value]))

    @jsii.member(jsii_name="resetErrorHandlingConfig")
    def reset_error_handling_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetErrorHandlingConfig", []))

    @builtins.property
    @jsii.member(jsii_name="errorHandlingConfig")
    def error_handling_config(
        self,
    ) -> AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfigOutputReference:
        return typing.cast(AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfigOutputReference, jsii.get(self, "errorHandlingConfig"))

    @builtins.property
    @jsii.member(jsii_name="errorHandlingConfigInput")
    def error_handling_config_input(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfig], jsii.get(self, "errorHandlingConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="objectInput")
    def object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "object"))

    @object.setter
    def object(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__715f44ca76d5c106dddc56fdffc1b7bc88cc09b91a5332600eadef73c4fef9e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "object", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycode]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycode], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycode],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f11fbb585f8d5e565ee7713d8a2b547bdc06f8794f41c6a6498f2272be56232)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetrics",
    jsii_struct_bases=[],
    name_mapping={},
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetrics:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetrics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetricsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetricsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__63471c0503e11a8143f462ccb8eed132050c99bb068a6f0e0d3e39fadbb515ea)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetrics]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetrics], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetrics],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1324e0aa5141f0e6a3ce2a0a75926ac534f71a9c171961831b2e872e70ee62c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketo",
    jsii_struct_bases=[],
    name_mapping={"object": "object", "error_handling_config": "errorHandlingConfig"},
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketo:
    def __init__(
        self,
        *,
        object: builtins.str,
        error_handling_config: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        :param error_handling_config: error_handling_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        '''
        if isinstance(error_handling_config, dict):
            error_handling_config = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfig(**error_handling_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afc149d202b55bbfd3420e8375f8880946e97ac6ed1b34ec8059615c520b9d5b)
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
            check_type(argname="argument error_handling_config", value=error_handling_config, expected_type=type_hints["error_handling_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "object": object,
        }
        if error_handling_config is not None:
            self._values["error_handling_config"] = error_handling_config

    @builtins.property
    def object(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.'''
        result = self._values.get("object")
        assert result is not None, "Required property 'object' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def error_handling_config(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfig"]:
        '''error_handling_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        '''
        result = self._values.get("error_handling_config")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfig",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "bucket_prefix": "bucketPrefix",
        "fail_on_first_destination_error": "failOnFirstDestinationError",
    },
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfig:
    def __init__(
        self,
        *,
        bucket_name: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param fail_on_first_destination_error: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27f7269878a1b038ba95d4aeb89052da0dbd16c0d78caa0ca45e106d26465017)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
            check_type(argname="argument fail_on_first_destination_error", value=fail_on_first_destination_error, expected_type=type_hints["fail_on_first_destination_error"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if bucket_name is not None:
            self._values["bucket_name"] = bucket_name
        if bucket_prefix is not None:
            self._values["bucket_prefix"] = bucket_prefix
        if fail_on_first_destination_error is not None:
            self._values["fail_on_first_destination_error"] = fail_on_first_destination_error

    @builtins.property
    def bucket_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.'''
        result = self._values.get("bucket_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.'''
        result = self._values.get("bucket_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fail_on_first_destination_error(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.'''
        result = self._values.get("fail_on_first_destination_error")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__379bb9b27b87c9bb1327d97d6d74fcef45ddbe41d304ef7d4ebfb4e48a8f2e84)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBucketName")
    def reset_bucket_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketName", []))

    @jsii.member(jsii_name="resetBucketPrefix")
    def reset_bucket_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketPrefix", []))

    @jsii.member(jsii_name="resetFailOnFirstDestinationError")
    def reset_fail_on_first_destination_error(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailOnFirstDestinationError", []))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketPrefixInput")
    def bucket_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="failOnFirstDestinationErrorInput")
    def fail_on_first_destination_error_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "failOnFirstDestinationErrorInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02f05bcedf15a1911a58c123947dd409de5adb9a42557265313179ca070e6d9c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="bucketPrefix")
    def bucket_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketPrefix"))

    @bucket_prefix.setter
    def bucket_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__389509348fbb21138aba326fbb7c83050ef1a6d4e6ba726676f939b632696422)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="failOnFirstDestinationError")
    def fail_on_first_destination_error(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "failOnFirstDestinationError"))

    @fail_on_first_destination_error.setter
    def fail_on_first_destination_error(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb4513e32d92f7f6f5ef877fdf09896826539d88e7ee1ee3b927745473e8fe46)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failOnFirstDestinationError", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c161b1854ef95c5f358620e25a15bedefc47b5d69900f0e41088552fa13333d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__be5901325a41811039efaf7b7775a08d46b19c487e4e40b33c92417082695e1b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putErrorHandlingConfig")
    def put_error_handling_config(
        self,
        *,
        bucket_name: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param fail_on_first_destination_error: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfig(
            bucket_name=bucket_name,
            bucket_prefix=bucket_prefix,
            fail_on_first_destination_error=fail_on_first_destination_error,
        )

        return typing.cast(None, jsii.invoke(self, "putErrorHandlingConfig", [value]))

    @jsii.member(jsii_name="resetErrorHandlingConfig")
    def reset_error_handling_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetErrorHandlingConfig", []))

    @builtins.property
    @jsii.member(jsii_name="errorHandlingConfig")
    def error_handling_config(
        self,
    ) -> AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfigOutputReference:
        return typing.cast(AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfigOutputReference, jsii.get(self, "errorHandlingConfig"))

    @builtins.property
    @jsii.member(jsii_name="errorHandlingConfigInput")
    def error_handling_config_input(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfig], jsii.get(self, "errorHandlingConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="objectInput")
    def object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "object"))

    @object.setter
    def object(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00256face2a2c835ea9cb402f3b7963c1c6d8c83be22321ab57ab2875ef1f13f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "object", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketo]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketo],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aba863f5e8e56e8768e11322dbac739a410e6ac96ce2902ffd4713b4f4ca3a52)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f44c5da04925cf90022961d85f219a98bc83eef975a85973c2064b429d3ae1f8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCustomConnector")
    def put_custom_connector(
        self,
        *,
        entity_name: builtins.str,
        custom_properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        error_handling_config: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        id_field_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        write_operation_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param entity_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#entity_name AppflowFlow#entity_name}.
        :param custom_properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#custom_properties AppflowFlow#custom_properties}.
        :param error_handling_config: error_handling_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        :param id_field_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#id_field_names AppflowFlow#id_field_names}.
        :param write_operation_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#write_operation_type AppflowFlow#write_operation_type}.
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnector(
            entity_name=entity_name,
            custom_properties=custom_properties,
            error_handling_config=error_handling_config,
            id_field_names=id_field_names,
            write_operation_type=write_operation_type,
        )

        return typing.cast(None, jsii.invoke(self, "putCustomConnector", [value]))

    @jsii.member(jsii_name="putCustomerProfiles")
    def put_customer_profiles(
        self,
        *,
        domain_name: builtins.str,
        object_type_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#domain_name AppflowFlow#domain_name}.
        :param object_type_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object_type_name AppflowFlow#object_type_name}.
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfiles(
            domain_name=domain_name, object_type_name=object_type_name
        )

        return typing.cast(None, jsii.invoke(self, "putCustomerProfiles", [value]))

    @jsii.member(jsii_name="putEventBridge")
    def put_event_bridge(
        self,
        *,
        object: builtins.str,
        error_handling_config: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        :param error_handling_config: error_handling_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridge(
            object=object, error_handling_config=error_handling_config
        )

        return typing.cast(None, jsii.invoke(self, "putEventBridge", [value]))

    @jsii.member(jsii_name="putHoneycode")
    def put_honeycode(
        self,
        *,
        object: builtins.str,
        error_handling_config: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        :param error_handling_config: error_handling_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycode(
            object=object, error_handling_config=error_handling_config
        )

        return typing.cast(None, jsii.invoke(self, "putHoneycode", [value]))

    @jsii.member(jsii_name="putLookoutMetrics")
    def put_lookout_metrics(self) -> None:
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetrics()

        return typing.cast(None, jsii.invoke(self, "putLookoutMetrics", [value]))

    @jsii.member(jsii_name="putMarketo")
    def put_marketo(
        self,
        *,
        object: builtins.str,
        error_handling_config: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        :param error_handling_config: error_handling_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketo(
            object=object, error_handling_config=error_handling_config
        )

        return typing.cast(None, jsii.invoke(self, "putMarketo", [value]))

    @jsii.member(jsii_name="putRedshift")
    def put_redshift(
        self,
        *,
        intermediate_bucket_name: builtins.str,
        object: builtins.str,
        bucket_prefix: typing.Optional[builtins.str] = None,
        error_handling_config: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param intermediate_bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#intermediate_bucket_name AppflowFlow#intermediate_bucket_name}.
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param error_handling_config: error_handling_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshift(
            intermediate_bucket_name=intermediate_bucket_name,
            object=object,
            bucket_prefix=bucket_prefix,
            error_handling_config=error_handling_config,
        )

        return typing.cast(None, jsii.invoke(self, "putRedshift", [value]))

    @jsii.member(jsii_name="putS3")
    def put_s3(
        self,
        *,
        bucket_name: builtins.str,
        bucket_prefix: typing.Optional[builtins.str] = None,
        s3_output_format_config: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param s3_output_format_config: s3_output_format_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#s3_output_format_config AppflowFlow#s3_output_format_config}
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3(
            bucket_name=bucket_name,
            bucket_prefix=bucket_prefix,
            s3_output_format_config=s3_output_format_config,
        )

        return typing.cast(None, jsii.invoke(self, "putS3", [value]))

    @jsii.member(jsii_name="putSalesforce")
    def put_salesforce(
        self,
        *,
        object: builtins.str,
        error_handling_config: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        id_field_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        write_operation_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        :param error_handling_config: error_handling_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        :param id_field_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#id_field_names AppflowFlow#id_field_names}.
        :param write_operation_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#write_operation_type AppflowFlow#write_operation_type}.
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforce(
            object=object,
            error_handling_config=error_handling_config,
            id_field_names=id_field_names,
            write_operation_type=write_operation_type,
        )

        return typing.cast(None, jsii.invoke(self, "putSalesforce", [value]))

    @jsii.member(jsii_name="putSapoData")
    def put_sapo_data(
        self,
        *,
        object_path: builtins.str,
        error_handling_config: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        id_field_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        success_response_handling_config: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        write_operation_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param object_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object_path AppflowFlow#object_path}.
        :param error_handling_config: error_handling_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        :param id_field_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#id_field_names AppflowFlow#id_field_names}.
        :param success_response_handling_config: success_response_handling_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#success_response_handling_config AppflowFlow#success_response_handling_config}
        :param write_operation_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#write_operation_type AppflowFlow#write_operation_type}.
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoData(
            object_path=object_path,
            error_handling_config=error_handling_config,
            id_field_names=id_field_names,
            success_response_handling_config=success_response_handling_config,
            write_operation_type=write_operation_type,
        )

        return typing.cast(None, jsii.invoke(self, "putSapoData", [value]))

    @jsii.member(jsii_name="putSnowflake")
    def put_snowflake(
        self,
        *,
        intermediate_bucket_name: builtins.str,
        object: builtins.str,
        bucket_prefix: typing.Optional[builtins.str] = None,
        error_handling_config: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param intermediate_bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#intermediate_bucket_name AppflowFlow#intermediate_bucket_name}.
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param error_handling_config: error_handling_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflake(
            intermediate_bucket_name=intermediate_bucket_name,
            object=object,
            bucket_prefix=bucket_prefix,
            error_handling_config=error_handling_config,
        )

        return typing.cast(None, jsii.invoke(self, "putSnowflake", [value]))

    @jsii.member(jsii_name="putUpsolver")
    def put_upsolver(
        self,
        *,
        bucket_name: builtins.str,
        s3_output_format_config: typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfig", typing.Dict[builtins.str, typing.Any]],
        bucket_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param s3_output_format_config: s3_output_format_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#s3_output_format_config AppflowFlow#s3_output_format_config}
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolver(
            bucket_name=bucket_name,
            s3_output_format_config=s3_output_format_config,
            bucket_prefix=bucket_prefix,
        )

        return typing.cast(None, jsii.invoke(self, "putUpsolver", [value]))

    @jsii.member(jsii_name="putZendesk")
    def put_zendesk(
        self,
        *,
        object: builtins.str,
        error_handling_config: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        id_field_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        write_operation_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        :param error_handling_config: error_handling_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        :param id_field_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#id_field_names AppflowFlow#id_field_names}.
        :param write_operation_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#write_operation_type AppflowFlow#write_operation_type}.
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendesk(
            object=object,
            error_handling_config=error_handling_config,
            id_field_names=id_field_names,
            write_operation_type=write_operation_type,
        )

        return typing.cast(None, jsii.invoke(self, "putZendesk", [value]))

    @jsii.member(jsii_name="resetCustomConnector")
    def reset_custom_connector(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomConnector", []))

    @jsii.member(jsii_name="resetCustomerProfiles")
    def reset_customer_profiles(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomerProfiles", []))

    @jsii.member(jsii_name="resetEventBridge")
    def reset_event_bridge(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventBridge", []))

    @jsii.member(jsii_name="resetHoneycode")
    def reset_honeycode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHoneycode", []))

    @jsii.member(jsii_name="resetLookoutMetrics")
    def reset_lookout_metrics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLookoutMetrics", []))

    @jsii.member(jsii_name="resetMarketo")
    def reset_marketo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMarketo", []))

    @jsii.member(jsii_name="resetRedshift")
    def reset_redshift(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedshift", []))

    @jsii.member(jsii_name="resetS3")
    def reset_s3(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3", []))

    @jsii.member(jsii_name="resetSalesforce")
    def reset_salesforce(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSalesforce", []))

    @jsii.member(jsii_name="resetSapoData")
    def reset_sapo_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSapoData", []))

    @jsii.member(jsii_name="resetSnowflake")
    def reset_snowflake(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSnowflake", []))

    @jsii.member(jsii_name="resetUpsolver")
    def reset_upsolver(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpsolver", []))

    @jsii.member(jsii_name="resetZendesk")
    def reset_zendesk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZendesk", []))

    @builtins.property
    @jsii.member(jsii_name="customConnector")
    def custom_connector(
        self,
    ) -> AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorOutputReference:
        return typing.cast(AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorOutputReference, jsii.get(self, "customConnector"))

    @builtins.property
    @jsii.member(jsii_name="customerProfiles")
    def customer_profiles(
        self,
    ) -> AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfilesOutputReference:
        return typing.cast(AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfilesOutputReference, jsii.get(self, "customerProfiles"))

    @builtins.property
    @jsii.member(jsii_name="eventBridge")
    def event_bridge(
        self,
    ) -> AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeOutputReference:
        return typing.cast(AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeOutputReference, jsii.get(self, "eventBridge"))

    @builtins.property
    @jsii.member(jsii_name="honeycode")
    def honeycode(
        self,
    ) -> AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeOutputReference:
        return typing.cast(AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeOutputReference, jsii.get(self, "honeycode"))

    @builtins.property
    @jsii.member(jsii_name="lookoutMetrics")
    def lookout_metrics(
        self,
    ) -> AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetricsOutputReference:
        return typing.cast(AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetricsOutputReference, jsii.get(self, "lookoutMetrics"))

    @builtins.property
    @jsii.member(jsii_name="marketo")
    def marketo(
        self,
    ) -> AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoOutputReference:
        return typing.cast(AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoOutputReference, jsii.get(self, "marketo"))

    @builtins.property
    @jsii.member(jsii_name="redshift")
    def redshift(
        self,
    ) -> "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftOutputReference":
        return typing.cast("AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftOutputReference", jsii.get(self, "redshift"))

    @builtins.property
    @jsii.member(jsii_name="s3")
    def s3(
        self,
    ) -> "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3OutputReference":
        return typing.cast("AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3OutputReference", jsii.get(self, "s3"))

    @builtins.property
    @jsii.member(jsii_name="salesforce")
    def salesforce(
        self,
    ) -> "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceOutputReference":
        return typing.cast("AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceOutputReference", jsii.get(self, "salesforce"))

    @builtins.property
    @jsii.member(jsii_name="sapoData")
    def sapo_data(
        self,
    ) -> "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataOutputReference":
        return typing.cast("AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataOutputReference", jsii.get(self, "sapoData"))

    @builtins.property
    @jsii.member(jsii_name="snowflake")
    def snowflake(
        self,
    ) -> "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeOutputReference":
        return typing.cast("AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeOutputReference", jsii.get(self, "snowflake"))

    @builtins.property
    @jsii.member(jsii_name="upsolver")
    def upsolver(
        self,
    ) -> "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverOutputReference":
        return typing.cast("AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverOutputReference", jsii.get(self, "upsolver"))

    @builtins.property
    @jsii.member(jsii_name="zendesk")
    def zendesk(
        self,
    ) -> "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskOutputReference":
        return typing.cast("AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskOutputReference", jsii.get(self, "zendesk"))

    @builtins.property
    @jsii.member(jsii_name="customConnectorInput")
    def custom_connector_input(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnector]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnector], jsii.get(self, "customConnectorInput"))

    @builtins.property
    @jsii.member(jsii_name="customerProfilesInput")
    def customer_profiles_input(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfiles]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfiles], jsii.get(self, "customerProfilesInput"))

    @builtins.property
    @jsii.member(jsii_name="eventBridgeInput")
    def event_bridge_input(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridge]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridge], jsii.get(self, "eventBridgeInput"))

    @builtins.property
    @jsii.member(jsii_name="honeycodeInput")
    def honeycode_input(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycode]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycode], jsii.get(self, "honeycodeInput"))

    @builtins.property
    @jsii.member(jsii_name="lookoutMetricsInput")
    def lookout_metrics_input(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetrics]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetrics], jsii.get(self, "lookoutMetricsInput"))

    @builtins.property
    @jsii.member(jsii_name="marketoInput")
    def marketo_input(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketo]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketo], jsii.get(self, "marketoInput"))

    @builtins.property
    @jsii.member(jsii_name="redshiftInput")
    def redshift_input(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshift"]:
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshift"], jsii.get(self, "redshiftInput"))

    @builtins.property
    @jsii.member(jsii_name="s3Input")
    def s3_input(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3"]:
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3"], jsii.get(self, "s3Input"))

    @builtins.property
    @jsii.member(jsii_name="salesforceInput")
    def salesforce_input(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforce"]:
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforce"], jsii.get(self, "salesforceInput"))

    @builtins.property
    @jsii.member(jsii_name="sapoDataInput")
    def sapo_data_input(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoData"]:
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoData"], jsii.get(self, "sapoDataInput"))

    @builtins.property
    @jsii.member(jsii_name="snowflakeInput")
    def snowflake_input(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflake"]:
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflake"], jsii.get(self, "snowflakeInput"))

    @builtins.property
    @jsii.member(jsii_name="upsolverInput")
    def upsolver_input(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolver"]:
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolver"], jsii.get(self, "upsolverInput"))

    @builtins.property
    @jsii.member(jsii_name="zendeskInput")
    def zendesk_input(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendesk"]:
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendesk"], jsii.get(self, "zendeskInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorProperties]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorProperties], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorProperties],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea10b27aa08f452650f57d8b60305f582d8f4fe4e7c6e5e748b1d57df55906ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshift",
    jsii_struct_bases=[],
    name_mapping={
        "intermediate_bucket_name": "intermediateBucketName",
        "object": "object",
        "bucket_prefix": "bucketPrefix",
        "error_handling_config": "errorHandlingConfig",
    },
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshift:
    def __init__(
        self,
        *,
        intermediate_bucket_name: builtins.str,
        object: builtins.str,
        bucket_prefix: typing.Optional[builtins.str] = None,
        error_handling_config: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param intermediate_bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#intermediate_bucket_name AppflowFlow#intermediate_bucket_name}.
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param error_handling_config: error_handling_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        '''
        if isinstance(error_handling_config, dict):
            error_handling_config = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfig(**error_handling_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aed8f50d43a2c8c41fdc3a258bce8a31ab18dcb52d84b1ddc862c52ff25079a9)
            check_type(argname="argument intermediate_bucket_name", value=intermediate_bucket_name, expected_type=type_hints["intermediate_bucket_name"])
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
            check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
            check_type(argname="argument error_handling_config", value=error_handling_config, expected_type=type_hints["error_handling_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "intermediate_bucket_name": intermediate_bucket_name,
            "object": object,
        }
        if bucket_prefix is not None:
            self._values["bucket_prefix"] = bucket_prefix
        if error_handling_config is not None:
            self._values["error_handling_config"] = error_handling_config

    @builtins.property
    def intermediate_bucket_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#intermediate_bucket_name AppflowFlow#intermediate_bucket_name}.'''
        result = self._values.get("intermediate_bucket_name")
        assert result is not None, "Required property 'intermediate_bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def object(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.'''
        result = self._values.get("object")
        assert result is not None, "Required property 'object' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bucket_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.'''
        result = self._values.get("bucket_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def error_handling_config(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfig"]:
        '''error_handling_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        '''
        result = self._values.get("error_handling_config")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshift(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfig",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "bucket_prefix": "bucketPrefix",
        "fail_on_first_destination_error": "failOnFirstDestinationError",
    },
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfig:
    def __init__(
        self,
        *,
        bucket_name: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param fail_on_first_destination_error: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4f49f71ee6d4665429292155ee1ca5d42a5c986e8075d1fd6df2bbd6c4d43ed)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
            check_type(argname="argument fail_on_first_destination_error", value=fail_on_first_destination_error, expected_type=type_hints["fail_on_first_destination_error"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if bucket_name is not None:
            self._values["bucket_name"] = bucket_name
        if bucket_prefix is not None:
            self._values["bucket_prefix"] = bucket_prefix
        if fail_on_first_destination_error is not None:
            self._values["fail_on_first_destination_error"] = fail_on_first_destination_error

    @builtins.property
    def bucket_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.'''
        result = self._values.get("bucket_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.'''
        result = self._values.get("bucket_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fail_on_first_destination_error(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.'''
        result = self._values.get("fail_on_first_destination_error")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0f35a76bf9cf1ac6a4a3cc2a6e17e43172059252097e1721dc8f96122dd83f07)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBucketName")
    def reset_bucket_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketName", []))

    @jsii.member(jsii_name="resetBucketPrefix")
    def reset_bucket_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketPrefix", []))

    @jsii.member(jsii_name="resetFailOnFirstDestinationError")
    def reset_fail_on_first_destination_error(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailOnFirstDestinationError", []))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketPrefixInput")
    def bucket_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="failOnFirstDestinationErrorInput")
    def fail_on_first_destination_error_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "failOnFirstDestinationErrorInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ae74c4475f78ec1d811c42efa68add7653ef0e9fa854232820c33dc12a8de1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="bucketPrefix")
    def bucket_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketPrefix"))

    @bucket_prefix.setter
    def bucket_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dee7cad114c318283f0dd55c1df1732f75fc692c659c086a0272652bf2b92bb6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="failOnFirstDestinationError")
    def fail_on_first_destination_error(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "failOnFirstDestinationError"))

    @fail_on_first_destination_error.setter
    def fail_on_first_destination_error(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c6fc7d7c908dc1e4efed81e50ca85274ab70fef9a7e0bb3eaf5f6175f646468)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failOnFirstDestinationError", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ea2d654629d16a5dad48731ae1148b1bfd4242138bc0e3a462e34b60ac01c0e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d2a0aad7c3ae038fd4d7410d64fc392dd786f1f84e7045c5a9d247f760e75c57)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putErrorHandlingConfig")
    def put_error_handling_config(
        self,
        *,
        bucket_name: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param fail_on_first_destination_error: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfig(
            bucket_name=bucket_name,
            bucket_prefix=bucket_prefix,
            fail_on_first_destination_error=fail_on_first_destination_error,
        )

        return typing.cast(None, jsii.invoke(self, "putErrorHandlingConfig", [value]))

    @jsii.member(jsii_name="resetBucketPrefix")
    def reset_bucket_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketPrefix", []))

    @jsii.member(jsii_name="resetErrorHandlingConfig")
    def reset_error_handling_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetErrorHandlingConfig", []))

    @builtins.property
    @jsii.member(jsii_name="errorHandlingConfig")
    def error_handling_config(
        self,
    ) -> AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfigOutputReference:
        return typing.cast(AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfigOutputReference, jsii.get(self, "errorHandlingConfig"))

    @builtins.property
    @jsii.member(jsii_name="bucketPrefixInput")
    def bucket_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="errorHandlingConfigInput")
    def error_handling_config_input(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfig], jsii.get(self, "errorHandlingConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="intermediateBucketNameInput")
    def intermediate_bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "intermediateBucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="objectInput")
    def object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketPrefix")
    def bucket_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketPrefix"))

    @bucket_prefix.setter
    def bucket_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8a5abf489fec1308ecc2b62b3010c0b178ff3be70319f2ee4fd68c287ac4bd6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="intermediateBucketName")
    def intermediate_bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "intermediateBucketName"))

    @intermediate_bucket_name.setter
    def intermediate_bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d496d0ead7ea37d4bafa163d5004cd53488c11e15c66eae1b101d9649878441b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intermediateBucketName", value)

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "object"))

    @object.setter
    def object(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be814dee091f39e1b992519e8b3dbe843de17379af6bea14a1964c6b6dc56072)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "object", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshift]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshift], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshift],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b7d328363fac27a3442ef968090bcb597b810674644518ba6fbfa745068e4bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "bucket_prefix": "bucketPrefix",
        "s3_output_format_config": "s3OutputFormatConfig",
    },
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3:
    def __init__(
        self,
        *,
        bucket_name: builtins.str,
        bucket_prefix: typing.Optional[builtins.str] = None,
        s3_output_format_config: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param s3_output_format_config: s3_output_format_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#s3_output_format_config AppflowFlow#s3_output_format_config}
        '''
        if isinstance(s3_output_format_config, dict):
            s3_output_format_config = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfig(**s3_output_format_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e273014bdd759433a94ebe42703c32af793417bfb167da0315b1e81a22926db)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
            check_type(argname="argument s3_output_format_config", value=s3_output_format_config, expected_type=type_hints["s3_output_format_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket_name": bucket_name,
        }
        if bucket_prefix is not None:
            self._values["bucket_prefix"] = bucket_prefix
        if s3_output_format_config is not None:
            self._values["s3_output_format_config"] = s3_output_format_config

    @builtins.property
    def bucket_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.'''
        result = self._values.get("bucket_name")
        assert result is not None, "Required property 'bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bucket_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.'''
        result = self._values.get("bucket_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_output_format_config(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfig"]:
        '''s3_output_format_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#s3_output_format_config AppflowFlow#s3_output_format_config}
        '''
        result = self._values.get("s3_output_format_config")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3OutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3OutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5807e6162dedffce3ed35bd65d9ebbce1f4808acd01a9f91eb2516c337802207)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putS3OutputFormatConfig")
    def put_s3_output_format_config(
        self,
        *,
        aggregation_config: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        file_type: typing.Optional[builtins.str] = None,
        prefix_config: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param aggregation_config: aggregation_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#aggregation_config AppflowFlow#aggregation_config}
        :param file_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#file_type AppflowFlow#file_type}.
        :param prefix_config: prefix_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#prefix_config AppflowFlow#prefix_config}
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfig(
            aggregation_config=aggregation_config,
            file_type=file_type,
            prefix_config=prefix_config,
        )

        return typing.cast(None, jsii.invoke(self, "putS3OutputFormatConfig", [value]))

    @jsii.member(jsii_name="resetBucketPrefix")
    def reset_bucket_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketPrefix", []))

    @jsii.member(jsii_name="resetS3OutputFormatConfig")
    def reset_s3_output_format_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3OutputFormatConfig", []))

    @builtins.property
    @jsii.member(jsii_name="s3OutputFormatConfig")
    def s3_output_format_config(
        self,
    ) -> "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigOutputReference":
        return typing.cast("AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigOutputReference", jsii.get(self, "s3OutputFormatConfig"))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketPrefixInput")
    def bucket_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="s3OutputFormatConfigInput")
    def s3_output_format_config_input(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfig"]:
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfig"], jsii.get(self, "s3OutputFormatConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3368eb212baa51b73df6fd7f805a5671c739560df441bc4c77fd946102e00e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="bucketPrefix")
    def bucket_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketPrefix"))

    @bucket_prefix.setter
    def bucket_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3adcadb3fee554e3881a6e174b57d1385e7ec32abdb1f0d60dad67f2099b7f33)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdaab4fa19eabeeab5f60a60f738bcf08ff1b57767c495945564a174565e6c58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfig",
    jsii_struct_bases=[],
    name_mapping={
        "aggregation_config": "aggregationConfig",
        "file_type": "fileType",
        "prefix_config": "prefixConfig",
    },
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfig:
    def __init__(
        self,
        *,
        aggregation_config: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        file_type: typing.Optional[builtins.str] = None,
        prefix_config: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param aggregation_config: aggregation_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#aggregation_config AppflowFlow#aggregation_config}
        :param file_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#file_type AppflowFlow#file_type}.
        :param prefix_config: prefix_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#prefix_config AppflowFlow#prefix_config}
        '''
        if isinstance(aggregation_config, dict):
            aggregation_config = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfig(**aggregation_config)
        if isinstance(prefix_config, dict):
            prefix_config = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfig(**prefix_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84d7dd2d316975595178bca0a1c98fcc99b9b6275118078f93dc68a65b79f687)
            check_type(argname="argument aggregation_config", value=aggregation_config, expected_type=type_hints["aggregation_config"])
            check_type(argname="argument file_type", value=file_type, expected_type=type_hints["file_type"])
            check_type(argname="argument prefix_config", value=prefix_config, expected_type=type_hints["prefix_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if aggregation_config is not None:
            self._values["aggregation_config"] = aggregation_config
        if file_type is not None:
            self._values["file_type"] = file_type
        if prefix_config is not None:
            self._values["prefix_config"] = prefix_config

    @builtins.property
    def aggregation_config(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfig"]:
        '''aggregation_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#aggregation_config AppflowFlow#aggregation_config}
        '''
        result = self._values.get("aggregation_config")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfig"], result)

    @builtins.property
    def file_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#file_type AppflowFlow#file_type}.'''
        result = self._values.get("file_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix_config(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfig"]:
        '''prefix_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#prefix_config AppflowFlow#prefix_config}
        '''
        result = self._values.get("prefix_config")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfig",
    jsii_struct_bases=[],
    name_mapping={"aggregation_type": "aggregationType"},
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfig:
    def __init__(
        self,
        *,
        aggregation_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aggregation_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#aggregation_type AppflowFlow#aggregation_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3a7806405d7ce6e8e549b8db4b9b3d14a803c2930add6893b5b8e3c1e414665)
            check_type(argname="argument aggregation_type", value=aggregation_type, expected_type=type_hints["aggregation_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if aggregation_type is not None:
            self._values["aggregation_type"] = aggregation_type

    @builtins.property
    def aggregation_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#aggregation_type AppflowFlow#aggregation_type}.'''
        result = self._values.get("aggregation_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__870449877fad7f137840d2f42aee96b4036e9c3aff6689579a123fb0aaa37962)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAggregationType")
    def reset_aggregation_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAggregationType", []))

    @builtins.property
    @jsii.member(jsii_name="aggregationTypeInput")
    def aggregation_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aggregationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="aggregationType")
    def aggregation_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "aggregationType"))

    @aggregation_type.setter
    def aggregation_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75914161b691bddc19c8e9e0cd2fc48143fbd874ea4b338316faf698b11f00fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aggregationType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3cefded4a8f4a06b7c2330e4514b378910afeccb1ff76e65c51707f8b7b3e8f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__094baf95cae858221d42517ccc83bda464ca0e9760e1886bf1e17f99d20751d6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAggregationConfig")
    def put_aggregation_config(
        self,
        *,
        aggregation_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aggregation_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#aggregation_type AppflowFlow#aggregation_type}.
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfig(
            aggregation_type=aggregation_type
        )

        return typing.cast(None, jsii.invoke(self, "putAggregationConfig", [value]))

    @jsii.member(jsii_name="putPrefixConfig")
    def put_prefix_config(
        self,
        *,
        prefix_format: typing.Optional[builtins.str] = None,
        prefix_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param prefix_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#prefix_format AppflowFlow#prefix_format}.
        :param prefix_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#prefix_type AppflowFlow#prefix_type}.
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfig(
            prefix_format=prefix_format, prefix_type=prefix_type
        )

        return typing.cast(None, jsii.invoke(self, "putPrefixConfig", [value]))

    @jsii.member(jsii_name="resetAggregationConfig")
    def reset_aggregation_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAggregationConfig", []))

    @jsii.member(jsii_name="resetFileType")
    def reset_file_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileType", []))

    @jsii.member(jsii_name="resetPrefixConfig")
    def reset_prefix_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefixConfig", []))

    @builtins.property
    @jsii.member(jsii_name="aggregationConfig")
    def aggregation_config(
        self,
    ) -> AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfigOutputReference:
        return typing.cast(AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfigOutputReference, jsii.get(self, "aggregationConfig"))

    @builtins.property
    @jsii.member(jsii_name="prefixConfig")
    def prefix_config(
        self,
    ) -> "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfigOutputReference":
        return typing.cast("AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfigOutputReference", jsii.get(self, "prefixConfig"))

    @builtins.property
    @jsii.member(jsii_name="aggregationConfigInput")
    def aggregation_config_input(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfig], jsii.get(self, "aggregationConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="fileTypeInput")
    def file_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixConfigInput")
    def prefix_config_input(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfig"]:
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfig"], jsii.get(self, "prefixConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="fileType")
    def file_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileType"))

    @file_type.setter
    def file_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48cc01f3a2357ee75dfa5ca721ec0dbbb1b270b94458bce3cfd53a639346ec87)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0cf6a1e4eac4f50b7a445c8277ac474e8e84f0e7d5fcec6a6bd6e8945cda0c6a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfig",
    jsii_struct_bases=[],
    name_mapping={"prefix_format": "prefixFormat", "prefix_type": "prefixType"},
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfig:
    def __init__(
        self,
        *,
        prefix_format: typing.Optional[builtins.str] = None,
        prefix_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param prefix_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#prefix_format AppflowFlow#prefix_format}.
        :param prefix_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#prefix_type AppflowFlow#prefix_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abd30ab6554c9f12ae426fce3f6868221acd166f42d6c770598e869cce1657b6)
            check_type(argname="argument prefix_format", value=prefix_format, expected_type=type_hints["prefix_format"])
            check_type(argname="argument prefix_type", value=prefix_type, expected_type=type_hints["prefix_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if prefix_format is not None:
            self._values["prefix_format"] = prefix_format
        if prefix_type is not None:
            self._values["prefix_type"] = prefix_type

    @builtins.property
    def prefix_format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#prefix_format AppflowFlow#prefix_format}.'''
        result = self._values.get("prefix_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#prefix_type AppflowFlow#prefix_type}.'''
        result = self._values.get("prefix_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b7d4f80a98d68d0ed01ced1fbafa1bbe1bb9409524745aa9d81946f5161ffff9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPrefixFormat")
    def reset_prefix_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefixFormat", []))

    @jsii.member(jsii_name="resetPrefixType")
    def reset_prefix_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefixType", []))

    @builtins.property
    @jsii.member(jsii_name="prefixFormatInput")
    def prefix_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixTypeInput")
    def prefix_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixFormat")
    def prefix_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefixFormat"))

    @prefix_format.setter
    def prefix_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28a50bcc1dfa586a2700dd8abecba839fbf2a5a90ed412f3a48cb8b70d57bfc8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefixFormat", value)

    @builtins.property
    @jsii.member(jsii_name="prefixType")
    def prefix_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefixType"))

    @prefix_type.setter
    def prefix_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b407a313b6e6cdf75f11973cf166427340ce48229bc64dc1a248f6288a25689)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefixType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__884b5b4c53006e2132182124372f7601a77a18b70b7ec166e57eb6870bbd9445)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforce",
    jsii_struct_bases=[],
    name_mapping={
        "object": "object",
        "error_handling_config": "errorHandlingConfig",
        "id_field_names": "idFieldNames",
        "write_operation_type": "writeOperationType",
    },
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforce:
    def __init__(
        self,
        *,
        object: builtins.str,
        error_handling_config: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        id_field_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        write_operation_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        :param error_handling_config: error_handling_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        :param id_field_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#id_field_names AppflowFlow#id_field_names}.
        :param write_operation_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#write_operation_type AppflowFlow#write_operation_type}.
        '''
        if isinstance(error_handling_config, dict):
            error_handling_config = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfig(**error_handling_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35d855f1d39130210d226d545edd7adaa02ecdffa58564a01b98dfc585da9886)
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
            check_type(argname="argument error_handling_config", value=error_handling_config, expected_type=type_hints["error_handling_config"])
            check_type(argname="argument id_field_names", value=id_field_names, expected_type=type_hints["id_field_names"])
            check_type(argname="argument write_operation_type", value=write_operation_type, expected_type=type_hints["write_operation_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "object": object,
        }
        if error_handling_config is not None:
            self._values["error_handling_config"] = error_handling_config
        if id_field_names is not None:
            self._values["id_field_names"] = id_field_names
        if write_operation_type is not None:
            self._values["write_operation_type"] = write_operation_type

    @builtins.property
    def object(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.'''
        result = self._values.get("object")
        assert result is not None, "Required property 'object' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def error_handling_config(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfig"]:
        '''error_handling_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        '''
        result = self._values.get("error_handling_config")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfig"], result)

    @builtins.property
    def id_field_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#id_field_names AppflowFlow#id_field_names}.'''
        result = self._values.get("id_field_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def write_operation_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#write_operation_type AppflowFlow#write_operation_type}.'''
        result = self._values.get("write_operation_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforce(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfig",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "bucket_prefix": "bucketPrefix",
        "fail_on_first_destination_error": "failOnFirstDestinationError",
    },
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfig:
    def __init__(
        self,
        *,
        bucket_name: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param fail_on_first_destination_error: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d84acdae301b19ec65333de30e0616a5fbb06a1a54d43b0069991c1be66c1182)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
            check_type(argname="argument fail_on_first_destination_error", value=fail_on_first_destination_error, expected_type=type_hints["fail_on_first_destination_error"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if bucket_name is not None:
            self._values["bucket_name"] = bucket_name
        if bucket_prefix is not None:
            self._values["bucket_prefix"] = bucket_prefix
        if fail_on_first_destination_error is not None:
            self._values["fail_on_first_destination_error"] = fail_on_first_destination_error

    @builtins.property
    def bucket_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.'''
        result = self._values.get("bucket_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.'''
        result = self._values.get("bucket_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fail_on_first_destination_error(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.'''
        result = self._values.get("fail_on_first_destination_error")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6fb19f8635083e7846eae9ccc838a0e5739d46dd1edc7eb26cd065572b69ff88)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBucketName")
    def reset_bucket_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketName", []))

    @jsii.member(jsii_name="resetBucketPrefix")
    def reset_bucket_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketPrefix", []))

    @jsii.member(jsii_name="resetFailOnFirstDestinationError")
    def reset_fail_on_first_destination_error(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailOnFirstDestinationError", []))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketPrefixInput")
    def bucket_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="failOnFirstDestinationErrorInput")
    def fail_on_first_destination_error_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "failOnFirstDestinationErrorInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91125db0cc4662fd82d76c995270b19802a63a51735a5058d74e995d315edabf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="bucketPrefix")
    def bucket_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketPrefix"))

    @bucket_prefix.setter
    def bucket_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88394aebabde376d483697ec8da1264ce6f7627b25c0922a1959471e33658a64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="failOnFirstDestinationError")
    def fail_on_first_destination_error(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "failOnFirstDestinationError"))

    @fail_on_first_destination_error.setter
    def fail_on_first_destination_error(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c699f2f97c88d525f2224850be5866f58414ffbf5bc501dc02911a998986cca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failOnFirstDestinationError", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5747905e07e918c0afcced86478ea1e863b8e0946ce85c28b674e7cdf6991613)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__58df4bb8fb4ee625b1ee205c6ff082e5b73415194c13a979199b04e0ff6b9f0f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putErrorHandlingConfig")
    def put_error_handling_config(
        self,
        *,
        bucket_name: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param fail_on_first_destination_error: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfig(
            bucket_name=bucket_name,
            bucket_prefix=bucket_prefix,
            fail_on_first_destination_error=fail_on_first_destination_error,
        )

        return typing.cast(None, jsii.invoke(self, "putErrorHandlingConfig", [value]))

    @jsii.member(jsii_name="resetErrorHandlingConfig")
    def reset_error_handling_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetErrorHandlingConfig", []))

    @jsii.member(jsii_name="resetIdFieldNames")
    def reset_id_field_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdFieldNames", []))

    @jsii.member(jsii_name="resetWriteOperationType")
    def reset_write_operation_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWriteOperationType", []))

    @builtins.property
    @jsii.member(jsii_name="errorHandlingConfig")
    def error_handling_config(
        self,
    ) -> AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfigOutputReference:
        return typing.cast(AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfigOutputReference, jsii.get(self, "errorHandlingConfig"))

    @builtins.property
    @jsii.member(jsii_name="errorHandlingConfigInput")
    def error_handling_config_input(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfig], jsii.get(self, "errorHandlingConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="idFieldNamesInput")
    def id_field_names_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "idFieldNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="objectInput")
    def object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="writeOperationTypeInput")
    def write_operation_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "writeOperationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="idFieldNames")
    def id_field_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "idFieldNames"))

    @id_field_names.setter
    def id_field_names(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__221af9aebd624086001a8302a51868a0a1ea665afe806e5c048b967736c0da97)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idFieldNames", value)

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "object"))

    @object.setter
    def object(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a36e8612ced04b0c055d4e74906299a3dd93c29f94cf75aa16cfa1ac0b1c8285)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "object", value)

    @builtins.property
    @jsii.member(jsii_name="writeOperationType")
    def write_operation_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "writeOperationType"))

    @write_operation_type.setter
    def write_operation_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81f3725a140ace4858ab32157826756e8b5c0258cea8d587cf780af48e5cf193)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "writeOperationType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforce]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforce], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforce],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88b130aa307078afa3af28740a776c858c35b1bff36134bdb60a6fdf089989ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoData",
    jsii_struct_bases=[],
    name_mapping={
        "object_path": "objectPath",
        "error_handling_config": "errorHandlingConfig",
        "id_field_names": "idFieldNames",
        "success_response_handling_config": "successResponseHandlingConfig",
        "write_operation_type": "writeOperationType",
    },
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoData:
    def __init__(
        self,
        *,
        object_path: builtins.str,
        error_handling_config: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        id_field_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        success_response_handling_config: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        write_operation_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param object_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object_path AppflowFlow#object_path}.
        :param error_handling_config: error_handling_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        :param id_field_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#id_field_names AppflowFlow#id_field_names}.
        :param success_response_handling_config: success_response_handling_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#success_response_handling_config AppflowFlow#success_response_handling_config}
        :param write_operation_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#write_operation_type AppflowFlow#write_operation_type}.
        '''
        if isinstance(error_handling_config, dict):
            error_handling_config = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfig(**error_handling_config)
        if isinstance(success_response_handling_config, dict):
            success_response_handling_config = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfig(**success_response_handling_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05c09efed61510f3adb34d941640d24eea7df839ed9e004433d98dc65b0ffb16)
            check_type(argname="argument object_path", value=object_path, expected_type=type_hints["object_path"])
            check_type(argname="argument error_handling_config", value=error_handling_config, expected_type=type_hints["error_handling_config"])
            check_type(argname="argument id_field_names", value=id_field_names, expected_type=type_hints["id_field_names"])
            check_type(argname="argument success_response_handling_config", value=success_response_handling_config, expected_type=type_hints["success_response_handling_config"])
            check_type(argname="argument write_operation_type", value=write_operation_type, expected_type=type_hints["write_operation_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "object_path": object_path,
        }
        if error_handling_config is not None:
            self._values["error_handling_config"] = error_handling_config
        if id_field_names is not None:
            self._values["id_field_names"] = id_field_names
        if success_response_handling_config is not None:
            self._values["success_response_handling_config"] = success_response_handling_config
        if write_operation_type is not None:
            self._values["write_operation_type"] = write_operation_type

    @builtins.property
    def object_path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object_path AppflowFlow#object_path}.'''
        result = self._values.get("object_path")
        assert result is not None, "Required property 'object_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def error_handling_config(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfig"]:
        '''error_handling_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        '''
        result = self._values.get("error_handling_config")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfig"], result)

    @builtins.property
    def id_field_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#id_field_names AppflowFlow#id_field_names}.'''
        result = self._values.get("id_field_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def success_response_handling_config(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfig"]:
        '''success_response_handling_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#success_response_handling_config AppflowFlow#success_response_handling_config}
        '''
        result = self._values.get("success_response_handling_config")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfig"], result)

    @builtins.property
    def write_operation_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#write_operation_type AppflowFlow#write_operation_type}.'''
        result = self._values.get("write_operation_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoData(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfig",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "bucket_prefix": "bucketPrefix",
        "fail_on_first_destination_error": "failOnFirstDestinationError",
    },
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfig:
    def __init__(
        self,
        *,
        bucket_name: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param fail_on_first_destination_error: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad6573a4b6df04d95d38e73b15ee5e1a67884441ec760618c9331ce02bafd3f5)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
            check_type(argname="argument fail_on_first_destination_error", value=fail_on_first_destination_error, expected_type=type_hints["fail_on_first_destination_error"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if bucket_name is not None:
            self._values["bucket_name"] = bucket_name
        if bucket_prefix is not None:
            self._values["bucket_prefix"] = bucket_prefix
        if fail_on_first_destination_error is not None:
            self._values["fail_on_first_destination_error"] = fail_on_first_destination_error

    @builtins.property
    def bucket_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.'''
        result = self._values.get("bucket_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.'''
        result = self._values.get("bucket_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fail_on_first_destination_error(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.'''
        result = self._values.get("fail_on_first_destination_error")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9ed2c27d6a36cbc68676fdd746d7542b04f65fba497b36e7d1fd5c20db49f4e5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBucketName")
    def reset_bucket_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketName", []))

    @jsii.member(jsii_name="resetBucketPrefix")
    def reset_bucket_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketPrefix", []))

    @jsii.member(jsii_name="resetFailOnFirstDestinationError")
    def reset_fail_on_first_destination_error(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailOnFirstDestinationError", []))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketPrefixInput")
    def bucket_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="failOnFirstDestinationErrorInput")
    def fail_on_first_destination_error_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "failOnFirstDestinationErrorInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5a820bb812863bb8f40f269922316ad32a9f9eec9891762990aa2b6bd56b907)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="bucketPrefix")
    def bucket_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketPrefix"))

    @bucket_prefix.setter
    def bucket_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75802ca2616d2ead59afefa67e162e78afbad08c057c22707fa880786a540efc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="failOnFirstDestinationError")
    def fail_on_first_destination_error(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "failOnFirstDestinationError"))

    @fail_on_first_destination_error.setter
    def fail_on_first_destination_error(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3077f1f78abc11abd275123a4481f77d9baf328f76f3b074b4829217a8adc52)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failOnFirstDestinationError", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7bb37ab610623e44b5b0dc218d56797ee188db21ac38d27bc54a9b411a11a677)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__27111f78cba85f549462bf32681693f999f68bd4db9073cdddd249d5dde26af8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putErrorHandlingConfig")
    def put_error_handling_config(
        self,
        *,
        bucket_name: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param fail_on_first_destination_error: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfig(
            bucket_name=bucket_name,
            bucket_prefix=bucket_prefix,
            fail_on_first_destination_error=fail_on_first_destination_error,
        )

        return typing.cast(None, jsii.invoke(self, "putErrorHandlingConfig", [value]))

    @jsii.member(jsii_name="putSuccessResponseHandlingConfig")
    def put_success_response_handling_config(
        self,
        *,
        bucket_name: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfig(
            bucket_name=bucket_name, bucket_prefix=bucket_prefix
        )

        return typing.cast(None, jsii.invoke(self, "putSuccessResponseHandlingConfig", [value]))

    @jsii.member(jsii_name="resetErrorHandlingConfig")
    def reset_error_handling_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetErrorHandlingConfig", []))

    @jsii.member(jsii_name="resetIdFieldNames")
    def reset_id_field_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdFieldNames", []))

    @jsii.member(jsii_name="resetSuccessResponseHandlingConfig")
    def reset_success_response_handling_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSuccessResponseHandlingConfig", []))

    @jsii.member(jsii_name="resetWriteOperationType")
    def reset_write_operation_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWriteOperationType", []))

    @builtins.property
    @jsii.member(jsii_name="errorHandlingConfig")
    def error_handling_config(
        self,
    ) -> AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfigOutputReference:
        return typing.cast(AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfigOutputReference, jsii.get(self, "errorHandlingConfig"))

    @builtins.property
    @jsii.member(jsii_name="successResponseHandlingConfig")
    def success_response_handling_config(
        self,
    ) -> "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfigOutputReference":
        return typing.cast("AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfigOutputReference", jsii.get(self, "successResponseHandlingConfig"))

    @builtins.property
    @jsii.member(jsii_name="errorHandlingConfigInput")
    def error_handling_config_input(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfig], jsii.get(self, "errorHandlingConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="idFieldNamesInput")
    def id_field_names_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "idFieldNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="objectPathInput")
    def object_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectPathInput"))

    @builtins.property
    @jsii.member(jsii_name="successResponseHandlingConfigInput")
    def success_response_handling_config_input(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfig"]:
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfig"], jsii.get(self, "successResponseHandlingConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="writeOperationTypeInput")
    def write_operation_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "writeOperationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="idFieldNames")
    def id_field_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "idFieldNames"))

    @id_field_names.setter
    def id_field_names(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03e33572c15ca8ea22cbe610a263a9b058c320f71c73011cd9733f960baf10d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idFieldNames", value)

    @builtins.property
    @jsii.member(jsii_name="objectPath")
    def object_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "objectPath"))

    @object_path.setter
    def object_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e41636ddc949df588bde0c4f60602d049d8c5168eb89a22d793c193cdcb5f90)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectPath", value)

    @builtins.property
    @jsii.member(jsii_name="writeOperationType")
    def write_operation_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "writeOperationType"))

    @write_operation_type.setter
    def write_operation_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db2fd34505711423460d61a03a2893ff6837b1e4af275d41cb52356ebc6782d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "writeOperationType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoData]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoData], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoData],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51b43884a869a876ba7f28d3d1314f0c13c9319ef53824e2d6e7f3a44c9b34bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfig",
    jsii_struct_bases=[],
    name_mapping={"bucket_name": "bucketName", "bucket_prefix": "bucketPrefix"},
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfig:
    def __init__(
        self,
        *,
        bucket_name: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19fd2065656fcd950aea2879baf1bdf3102c625be99d2bf33234de04315d1d5f)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if bucket_name is not None:
            self._values["bucket_name"] = bucket_name
        if bucket_prefix is not None:
            self._values["bucket_prefix"] = bucket_prefix

    @builtins.property
    def bucket_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.'''
        result = self._values.get("bucket_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.'''
        result = self._values.get("bucket_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e32467f60a1b1a26b277cb6fe61a0374d24696af39af21d3dc3793c52b0ebbe7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBucketName")
    def reset_bucket_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketName", []))

    @jsii.member(jsii_name="resetBucketPrefix")
    def reset_bucket_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketPrefix", []))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketPrefixInput")
    def bucket_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81cc3ec95bd5fde78f1e6a6ca479bcd7ad848ab8bffc3f68a050d35e4cdbeae9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="bucketPrefix")
    def bucket_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketPrefix"))

    @bucket_prefix.setter
    def bucket_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a723a3a712a16238369fc5b8191d422f8518cbc4dec52e55f9a767bf8ab15a8a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2d13757751af4378d7729950cb7e89b46fc126e3284ac67a4327f57c1e7c1e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflake",
    jsii_struct_bases=[],
    name_mapping={
        "intermediate_bucket_name": "intermediateBucketName",
        "object": "object",
        "bucket_prefix": "bucketPrefix",
        "error_handling_config": "errorHandlingConfig",
    },
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflake:
    def __init__(
        self,
        *,
        intermediate_bucket_name: builtins.str,
        object: builtins.str,
        bucket_prefix: typing.Optional[builtins.str] = None,
        error_handling_config: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param intermediate_bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#intermediate_bucket_name AppflowFlow#intermediate_bucket_name}.
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param error_handling_config: error_handling_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        '''
        if isinstance(error_handling_config, dict):
            error_handling_config = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfig(**error_handling_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__674cf34d8d62ddd75c3b9a0fc9f6f1f61e4ace000114ec49ebac87ea1b925bf3)
            check_type(argname="argument intermediate_bucket_name", value=intermediate_bucket_name, expected_type=type_hints["intermediate_bucket_name"])
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
            check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
            check_type(argname="argument error_handling_config", value=error_handling_config, expected_type=type_hints["error_handling_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "intermediate_bucket_name": intermediate_bucket_name,
            "object": object,
        }
        if bucket_prefix is not None:
            self._values["bucket_prefix"] = bucket_prefix
        if error_handling_config is not None:
            self._values["error_handling_config"] = error_handling_config

    @builtins.property
    def intermediate_bucket_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#intermediate_bucket_name AppflowFlow#intermediate_bucket_name}.'''
        result = self._values.get("intermediate_bucket_name")
        assert result is not None, "Required property 'intermediate_bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def object(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.'''
        result = self._values.get("object")
        assert result is not None, "Required property 'object' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bucket_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.'''
        result = self._values.get("bucket_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def error_handling_config(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfig"]:
        '''error_handling_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        '''
        result = self._values.get("error_handling_config")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflake(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfig",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "bucket_prefix": "bucketPrefix",
        "fail_on_first_destination_error": "failOnFirstDestinationError",
    },
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfig:
    def __init__(
        self,
        *,
        bucket_name: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param fail_on_first_destination_error: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32a51b60a5d2abc2a7722c4d2d3004215dfdb301621b25ba83d71db5816024e5)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
            check_type(argname="argument fail_on_first_destination_error", value=fail_on_first_destination_error, expected_type=type_hints["fail_on_first_destination_error"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if bucket_name is not None:
            self._values["bucket_name"] = bucket_name
        if bucket_prefix is not None:
            self._values["bucket_prefix"] = bucket_prefix
        if fail_on_first_destination_error is not None:
            self._values["fail_on_first_destination_error"] = fail_on_first_destination_error

    @builtins.property
    def bucket_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.'''
        result = self._values.get("bucket_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.'''
        result = self._values.get("bucket_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fail_on_first_destination_error(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.'''
        result = self._values.get("fail_on_first_destination_error")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ce35ae397c6d010d999b6e5bd4492ad5fa6727e730f3df128f73e62f0aa17b3a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBucketName")
    def reset_bucket_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketName", []))

    @jsii.member(jsii_name="resetBucketPrefix")
    def reset_bucket_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketPrefix", []))

    @jsii.member(jsii_name="resetFailOnFirstDestinationError")
    def reset_fail_on_first_destination_error(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailOnFirstDestinationError", []))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketPrefixInput")
    def bucket_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="failOnFirstDestinationErrorInput")
    def fail_on_first_destination_error_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "failOnFirstDestinationErrorInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf39b918c0acf82e48ab1637b3e7d6caffcee98110870354b6d08fed0c5a0543)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="bucketPrefix")
    def bucket_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketPrefix"))

    @bucket_prefix.setter
    def bucket_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7b00c879244698f8783a41ee682c83633f762498d44dfdfc2b37a79a051e29c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="failOnFirstDestinationError")
    def fail_on_first_destination_error(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "failOnFirstDestinationError"))

    @fail_on_first_destination_error.setter
    def fail_on_first_destination_error(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08592e430d024f66a878507b2dcb78783b6f01954f0ee3c23391fddf23a0404f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failOnFirstDestinationError", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d4a8cde216ddeccb029f2ab4fd08905c752b4dafe6ac51f57c734a4d0cb629d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__816fabdbc5811b68d70a54f8f053959710ad3fbbe0c01e52ff6c7a2fd58c974f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putErrorHandlingConfig")
    def put_error_handling_config(
        self,
        *,
        bucket_name: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param fail_on_first_destination_error: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfig(
            bucket_name=bucket_name,
            bucket_prefix=bucket_prefix,
            fail_on_first_destination_error=fail_on_first_destination_error,
        )

        return typing.cast(None, jsii.invoke(self, "putErrorHandlingConfig", [value]))

    @jsii.member(jsii_name="resetBucketPrefix")
    def reset_bucket_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketPrefix", []))

    @jsii.member(jsii_name="resetErrorHandlingConfig")
    def reset_error_handling_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetErrorHandlingConfig", []))

    @builtins.property
    @jsii.member(jsii_name="errorHandlingConfig")
    def error_handling_config(
        self,
    ) -> AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfigOutputReference:
        return typing.cast(AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfigOutputReference, jsii.get(self, "errorHandlingConfig"))

    @builtins.property
    @jsii.member(jsii_name="bucketPrefixInput")
    def bucket_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="errorHandlingConfigInput")
    def error_handling_config_input(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfig], jsii.get(self, "errorHandlingConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="intermediateBucketNameInput")
    def intermediate_bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "intermediateBucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="objectInput")
    def object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketPrefix")
    def bucket_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketPrefix"))

    @bucket_prefix.setter
    def bucket_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__939cccdccad259cf498e6a33b05d0e22d38be6fae713acab66873fda7fcd4e26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="intermediateBucketName")
    def intermediate_bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "intermediateBucketName"))

    @intermediate_bucket_name.setter
    def intermediate_bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8de59a0494091d55450369a696ece7a5b185835a46cc91ae8bd26064e5c860df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intermediateBucketName", value)

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "object"))

    @object.setter
    def object(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e171561ee10e6eeb3005cd1f49e6a5f37b0b4b9639aafa88909471e33dd78654)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "object", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflake]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflake], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflake],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae730e659f195dac5f9f8956fa224083a4b506b58e5b670bceeee358ffcd42e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolver",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "s3_output_format_config": "s3OutputFormatConfig",
        "bucket_prefix": "bucketPrefix",
    },
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolver:
    def __init__(
        self,
        *,
        bucket_name: builtins.str,
        s3_output_format_config: typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfig", typing.Dict[builtins.str, typing.Any]],
        bucket_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param s3_output_format_config: s3_output_format_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#s3_output_format_config AppflowFlow#s3_output_format_config}
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        '''
        if isinstance(s3_output_format_config, dict):
            s3_output_format_config = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfig(**s3_output_format_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8840f37373b3ca5d2e1740dbaab71d75d494c24d4719049074491f5a140787a5)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument s3_output_format_config", value=s3_output_format_config, expected_type=type_hints["s3_output_format_config"])
            check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket_name": bucket_name,
            "s3_output_format_config": s3_output_format_config,
        }
        if bucket_prefix is not None:
            self._values["bucket_prefix"] = bucket_prefix

    @builtins.property
    def bucket_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.'''
        result = self._values.get("bucket_name")
        assert result is not None, "Required property 'bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def s3_output_format_config(
        self,
    ) -> "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfig":
        '''s3_output_format_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#s3_output_format_config AppflowFlow#s3_output_format_config}
        '''
        result = self._values.get("s3_output_format_config")
        assert result is not None, "Required property 's3_output_format_config' is missing"
        return typing.cast("AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfig", result)

    @builtins.property
    def bucket_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.'''
        result = self._values.get("bucket_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolver(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5e44da0e1e62584834a42ad8835c988b37fb752002eb6fed14cb8cce58c38ac0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putS3OutputFormatConfig")
    def put_s3_output_format_config(
        self,
        *,
        prefix_config: typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfig", typing.Dict[builtins.str, typing.Any]],
        aggregation_config: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        file_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param prefix_config: prefix_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#prefix_config AppflowFlow#prefix_config}
        :param aggregation_config: aggregation_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#aggregation_config AppflowFlow#aggregation_config}
        :param file_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#file_type AppflowFlow#file_type}.
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfig(
            prefix_config=prefix_config,
            aggregation_config=aggregation_config,
            file_type=file_type,
        )

        return typing.cast(None, jsii.invoke(self, "putS3OutputFormatConfig", [value]))

    @jsii.member(jsii_name="resetBucketPrefix")
    def reset_bucket_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketPrefix", []))

    @builtins.property
    @jsii.member(jsii_name="s3OutputFormatConfig")
    def s3_output_format_config(
        self,
    ) -> "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigOutputReference":
        return typing.cast("AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigOutputReference", jsii.get(self, "s3OutputFormatConfig"))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketPrefixInput")
    def bucket_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="s3OutputFormatConfigInput")
    def s3_output_format_config_input(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfig"]:
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfig"], jsii.get(self, "s3OutputFormatConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1dfc731ad368c4011a4919fed05d6641971c0b79e6d17df7d0a4a237282546e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="bucketPrefix")
    def bucket_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketPrefix"))

    @bucket_prefix.setter
    def bucket_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a34091d04c842c45768288a67a0cce81f6b34e696b3cb739adfad85120783125)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolver]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolver], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolver],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d550b168d9583650fd3e81db00a1d19b546963cfd6de4181f05917d9716e91a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfig",
    jsii_struct_bases=[],
    name_mapping={
        "prefix_config": "prefixConfig",
        "aggregation_config": "aggregationConfig",
        "file_type": "fileType",
    },
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfig:
    def __init__(
        self,
        *,
        prefix_config: typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfig", typing.Dict[builtins.str, typing.Any]],
        aggregation_config: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        file_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param prefix_config: prefix_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#prefix_config AppflowFlow#prefix_config}
        :param aggregation_config: aggregation_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#aggregation_config AppflowFlow#aggregation_config}
        :param file_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#file_type AppflowFlow#file_type}.
        '''
        if isinstance(prefix_config, dict):
            prefix_config = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfig(**prefix_config)
        if isinstance(aggregation_config, dict):
            aggregation_config = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfig(**aggregation_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b2e301b01a26c816bcaba7e5178e62504d762b3bb6c895a689e36f5c9b859f8)
            check_type(argname="argument prefix_config", value=prefix_config, expected_type=type_hints["prefix_config"])
            check_type(argname="argument aggregation_config", value=aggregation_config, expected_type=type_hints["aggregation_config"])
            check_type(argname="argument file_type", value=file_type, expected_type=type_hints["file_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "prefix_config": prefix_config,
        }
        if aggregation_config is not None:
            self._values["aggregation_config"] = aggregation_config
        if file_type is not None:
            self._values["file_type"] = file_type

    @builtins.property
    def prefix_config(
        self,
    ) -> "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfig":
        '''prefix_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#prefix_config AppflowFlow#prefix_config}
        '''
        result = self._values.get("prefix_config")
        assert result is not None, "Required property 'prefix_config' is missing"
        return typing.cast("AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfig", result)

    @builtins.property
    def aggregation_config(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfig"]:
        '''aggregation_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#aggregation_config AppflowFlow#aggregation_config}
        '''
        result = self._values.get("aggregation_config")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfig"], result)

    @builtins.property
    def file_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#file_type AppflowFlow#file_type}.'''
        result = self._values.get("file_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfig",
    jsii_struct_bases=[],
    name_mapping={"aggregation_type": "aggregationType"},
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfig:
    def __init__(
        self,
        *,
        aggregation_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aggregation_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#aggregation_type AppflowFlow#aggregation_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93d07f17f8d1c467184ecaffea487b7007f64a4489e13461a761958128bb3057)
            check_type(argname="argument aggregation_type", value=aggregation_type, expected_type=type_hints["aggregation_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if aggregation_type is not None:
            self._values["aggregation_type"] = aggregation_type

    @builtins.property
    def aggregation_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#aggregation_type AppflowFlow#aggregation_type}.'''
        result = self._values.get("aggregation_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6ac2a7c6ca11ed2bcd587227afc2079480c1f23abac7d44c622db3e0fa18190a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAggregationType")
    def reset_aggregation_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAggregationType", []))

    @builtins.property
    @jsii.member(jsii_name="aggregationTypeInput")
    def aggregation_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aggregationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="aggregationType")
    def aggregation_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "aggregationType"))

    @aggregation_type.setter
    def aggregation_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f61986ccaf849dea33c0b0cb260d682274a6db4dfcfa3b62ed5cdcbd80a5426)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aggregationType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a26d49a5e2f807acf269adedc75b200f694368aed0a5b1bc6f6f095213de10e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__26682c1772d88e9fc62676033953f2d081d5b2bf471d10f6b387423a5996a7ec)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAggregationConfig")
    def put_aggregation_config(
        self,
        *,
        aggregation_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aggregation_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#aggregation_type AppflowFlow#aggregation_type}.
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfig(
            aggregation_type=aggregation_type
        )

        return typing.cast(None, jsii.invoke(self, "putAggregationConfig", [value]))

    @jsii.member(jsii_name="putPrefixConfig")
    def put_prefix_config(
        self,
        *,
        prefix_type: builtins.str,
        prefix_format: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param prefix_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#prefix_type AppflowFlow#prefix_type}.
        :param prefix_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#prefix_format AppflowFlow#prefix_format}.
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfig(
            prefix_type=prefix_type, prefix_format=prefix_format
        )

        return typing.cast(None, jsii.invoke(self, "putPrefixConfig", [value]))

    @jsii.member(jsii_name="resetAggregationConfig")
    def reset_aggregation_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAggregationConfig", []))

    @jsii.member(jsii_name="resetFileType")
    def reset_file_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileType", []))

    @builtins.property
    @jsii.member(jsii_name="aggregationConfig")
    def aggregation_config(
        self,
    ) -> AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfigOutputReference:
        return typing.cast(AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfigOutputReference, jsii.get(self, "aggregationConfig"))

    @builtins.property
    @jsii.member(jsii_name="prefixConfig")
    def prefix_config(
        self,
    ) -> "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfigOutputReference":
        return typing.cast("AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfigOutputReference", jsii.get(self, "prefixConfig"))

    @builtins.property
    @jsii.member(jsii_name="aggregationConfigInput")
    def aggregation_config_input(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfig], jsii.get(self, "aggregationConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="fileTypeInput")
    def file_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixConfigInput")
    def prefix_config_input(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfig"]:
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfig"], jsii.get(self, "prefixConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="fileType")
    def file_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileType"))

    @file_type.setter
    def file_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7dd13984bdaba355094b60434aaacfdc219f10cabd964405a0d735e00ad127bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d6b60cf5aa42fa77b49eff0683b69259a71b0186b5696866f2c9f66edb640fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfig",
    jsii_struct_bases=[],
    name_mapping={"prefix_type": "prefixType", "prefix_format": "prefixFormat"},
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfig:
    def __init__(
        self,
        *,
        prefix_type: builtins.str,
        prefix_format: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param prefix_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#prefix_type AppflowFlow#prefix_type}.
        :param prefix_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#prefix_format AppflowFlow#prefix_format}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0aeda194743ac3acf58ca228c8b1271a0462827ba7cadc9960d7bf80cb38b0c9)
            check_type(argname="argument prefix_type", value=prefix_type, expected_type=type_hints["prefix_type"])
            check_type(argname="argument prefix_format", value=prefix_format, expected_type=type_hints["prefix_format"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "prefix_type": prefix_type,
        }
        if prefix_format is not None:
            self._values["prefix_format"] = prefix_format

    @builtins.property
    def prefix_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#prefix_type AppflowFlow#prefix_type}.'''
        result = self._values.get("prefix_type")
        assert result is not None, "Required property 'prefix_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def prefix_format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#prefix_format AppflowFlow#prefix_format}.'''
        result = self._values.get("prefix_format")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0c8cfceb3a3e333bfda73819ae3255348378c4186afcd3aeef29f14a37c1af1e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPrefixFormat")
    def reset_prefix_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefixFormat", []))

    @builtins.property
    @jsii.member(jsii_name="prefixFormatInput")
    def prefix_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixTypeInput")
    def prefix_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixFormat")
    def prefix_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefixFormat"))

    @prefix_format.setter
    def prefix_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86e4f70a84e7b9353b65b043ae54753d5c6b029450a8829a12fa74f57a58b2b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefixFormat", value)

    @builtins.property
    @jsii.member(jsii_name="prefixType")
    def prefix_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefixType"))

    @prefix_type.setter
    def prefix_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ada9f58a637301ae9c8d03628a153ca714cc2ded9c23a77be1ceabc8ad488ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefixType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2a547ccf2234f9c1dd928d56d2241b60a2755eba2b13a4d1fbd135cbb71a068)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendesk",
    jsii_struct_bases=[],
    name_mapping={
        "object": "object",
        "error_handling_config": "errorHandlingConfig",
        "id_field_names": "idFieldNames",
        "write_operation_type": "writeOperationType",
    },
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendesk:
    def __init__(
        self,
        *,
        object: builtins.str,
        error_handling_config: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        id_field_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        write_operation_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        :param error_handling_config: error_handling_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        :param id_field_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#id_field_names AppflowFlow#id_field_names}.
        :param write_operation_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#write_operation_type AppflowFlow#write_operation_type}.
        '''
        if isinstance(error_handling_config, dict):
            error_handling_config = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfig(**error_handling_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4c0e68e3f96015e12c266468c3f010c25f97a60879c61dc2b54189ec163d0d1)
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
            check_type(argname="argument error_handling_config", value=error_handling_config, expected_type=type_hints["error_handling_config"])
            check_type(argname="argument id_field_names", value=id_field_names, expected_type=type_hints["id_field_names"])
            check_type(argname="argument write_operation_type", value=write_operation_type, expected_type=type_hints["write_operation_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "object": object,
        }
        if error_handling_config is not None:
            self._values["error_handling_config"] = error_handling_config
        if id_field_names is not None:
            self._values["id_field_names"] = id_field_names
        if write_operation_type is not None:
            self._values["write_operation_type"] = write_operation_type

    @builtins.property
    def object(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.'''
        result = self._values.get("object")
        assert result is not None, "Required property 'object' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def error_handling_config(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfig"]:
        '''error_handling_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        '''
        result = self._values.get("error_handling_config")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfig"], result)

    @builtins.property
    def id_field_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#id_field_names AppflowFlow#id_field_names}.'''
        result = self._values.get("id_field_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def write_operation_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#write_operation_type AppflowFlow#write_operation_type}.'''
        result = self._values.get("write_operation_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendesk(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfig",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "bucket_prefix": "bucketPrefix",
        "fail_on_first_destination_error": "failOnFirstDestinationError",
    },
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfig:
    def __init__(
        self,
        *,
        bucket_name: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param fail_on_first_destination_error: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7107d562e77597f27a71f3a78a93eb55fa803a1029144b2721be3df5f9805f6e)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
            check_type(argname="argument fail_on_first_destination_error", value=fail_on_first_destination_error, expected_type=type_hints["fail_on_first_destination_error"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if bucket_name is not None:
            self._values["bucket_name"] = bucket_name
        if bucket_prefix is not None:
            self._values["bucket_prefix"] = bucket_prefix
        if fail_on_first_destination_error is not None:
            self._values["fail_on_first_destination_error"] = fail_on_first_destination_error

    @builtins.property
    def bucket_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.'''
        result = self._values.get("bucket_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.'''
        result = self._values.get("bucket_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fail_on_first_destination_error(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.'''
        result = self._values.get("fail_on_first_destination_error")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3ecfa4cf37281ad02a2b6f0a6cbf0ad5050ce74286635ccff03eb825654ba837)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBucketName")
    def reset_bucket_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketName", []))

    @jsii.member(jsii_name="resetBucketPrefix")
    def reset_bucket_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketPrefix", []))

    @jsii.member(jsii_name="resetFailOnFirstDestinationError")
    def reset_fail_on_first_destination_error(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailOnFirstDestinationError", []))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketPrefixInput")
    def bucket_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="failOnFirstDestinationErrorInput")
    def fail_on_first_destination_error_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "failOnFirstDestinationErrorInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2e0c00268e34b0cfea5b2b07d01342f0385d6392646760f0ea48bb9b3d1bd39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="bucketPrefix")
    def bucket_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketPrefix"))

    @bucket_prefix.setter
    def bucket_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd870d731047edad8e9e47b7fbd0e4f68c6cb447497142a5aeeb545dcb58049f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="failOnFirstDestinationError")
    def fail_on_first_destination_error(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "failOnFirstDestinationError"))

    @fail_on_first_destination_error.setter
    def fail_on_first_destination_error(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84abd74c7601ba88f4fe20989471611197943b4d2c4cc7d5ee56bcffd05b8cbe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failOnFirstDestinationError", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38c7bc7207576851ed73925cb701faa7317591fcf06181d3a4ef24af8e5fb1d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__489f52aec612e1e4ecb7a03a115333a84621f3830e2cbf209d66827a93037497)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putErrorHandlingConfig")
    def put_error_handling_config(
        self,
        *,
        bucket_name: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param fail_on_first_destination_error: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfig(
            bucket_name=bucket_name,
            bucket_prefix=bucket_prefix,
            fail_on_first_destination_error=fail_on_first_destination_error,
        )

        return typing.cast(None, jsii.invoke(self, "putErrorHandlingConfig", [value]))

    @jsii.member(jsii_name="resetErrorHandlingConfig")
    def reset_error_handling_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetErrorHandlingConfig", []))

    @jsii.member(jsii_name="resetIdFieldNames")
    def reset_id_field_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdFieldNames", []))

    @jsii.member(jsii_name="resetWriteOperationType")
    def reset_write_operation_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWriteOperationType", []))

    @builtins.property
    @jsii.member(jsii_name="errorHandlingConfig")
    def error_handling_config(
        self,
    ) -> AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfigOutputReference:
        return typing.cast(AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfigOutputReference, jsii.get(self, "errorHandlingConfig"))

    @builtins.property
    @jsii.member(jsii_name="errorHandlingConfigInput")
    def error_handling_config_input(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfig], jsii.get(self, "errorHandlingConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="idFieldNamesInput")
    def id_field_names_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "idFieldNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="objectInput")
    def object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="writeOperationTypeInput")
    def write_operation_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "writeOperationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="idFieldNames")
    def id_field_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "idFieldNames"))

    @id_field_names.setter
    def id_field_names(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3381f01d2c42f36ba41bd62636b7a27be9e16c00b97125a0c88ba8bc189fad91)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idFieldNames", value)

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "object"))

    @object.setter
    def object(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3921503a5f298d75880aca47a83623ddd2da87a7c56c1e1f2c3f793886f87f0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "object", value)

    @builtins.property
    @jsii.member(jsii_name="writeOperationType")
    def write_operation_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "writeOperationType"))

    @write_operation_type.setter
    def write_operation_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a55d1d2762c2c9744fc1570571883c78a64c0ab6ef32fe932337f43c27bc033)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "writeOperationType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendesk]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendesk], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendesk],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb42324c8574298e4ed66b1326301b7ff3dc25149cd3e6890225e757667a03f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowFlowDestinationFlowConfigList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4835374e57b48cd60eb54a99440f38dcd51baffb6ac77cd5ea274893347d941e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "AppflowFlowDestinationFlowConfigOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5b9d746f9c472678d1619da4a6e7835ae7dc0126c3d6a981fb0e1bc529b2428)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppflowFlowDestinationFlowConfigOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1105703cc0ffee420adbff03699ce33292f82ab0a0ee44ebec4edcd64fce846d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__776cc2bdc826cde47ccf653f24619a5cc0c2e905c67b11d8c7e6661f92993c94)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ca00516121b617d176f67eed4a4487a145041de4c66defa0ca0c1d1a27970948)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppflowFlowDestinationFlowConfig]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppflowFlowDestinationFlowConfig]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppflowFlowDestinationFlowConfig]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98e35ab120a95e86021a2d404a9c6c0118808ffc6c04f7a66850dd36573830fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowFlowDestinationFlowConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowDestinationFlowConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ce2451bdb68cab283e27363f505e9eaec337ace9b7af4a791693a78b81fb9e89)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putDestinationConnectorProperties")
    def put_destination_connector_properties(
        self,
        *,
        custom_connector: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnector, typing.Dict[builtins.str, typing.Any]]] = None,
        customer_profiles: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfiles, typing.Dict[builtins.str, typing.Any]]] = None,
        event_bridge: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridge, typing.Dict[builtins.str, typing.Any]]] = None,
        honeycode: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycode, typing.Dict[builtins.str, typing.Any]]] = None,
        lookout_metrics: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetrics, typing.Dict[builtins.str, typing.Any]]] = None,
        marketo: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketo, typing.Dict[builtins.str, typing.Any]]] = None,
        redshift: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshift, typing.Dict[builtins.str, typing.Any]]] = None,
        s3: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3, typing.Dict[builtins.str, typing.Any]]] = None,
        salesforce: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforce, typing.Dict[builtins.str, typing.Any]]] = None,
        sapo_data: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoData, typing.Dict[builtins.str, typing.Any]]] = None,
        snowflake: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflake, typing.Dict[builtins.str, typing.Any]]] = None,
        upsolver: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolver, typing.Dict[builtins.str, typing.Any]]] = None,
        zendesk: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendesk, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param custom_connector: custom_connector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#custom_connector AppflowFlow#custom_connector}
        :param customer_profiles: customer_profiles block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#customer_profiles AppflowFlow#customer_profiles}
        :param event_bridge: event_bridge block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#event_bridge AppflowFlow#event_bridge}
        :param honeycode: honeycode block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#honeycode AppflowFlow#honeycode}
        :param lookout_metrics: lookout_metrics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#lookout_metrics AppflowFlow#lookout_metrics}
        :param marketo: marketo block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#marketo AppflowFlow#marketo}
        :param redshift: redshift block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#redshift AppflowFlow#redshift}
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#s3 AppflowFlow#s3}
        :param salesforce: salesforce block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#salesforce AppflowFlow#salesforce}
        :param sapo_data: sapo_data block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#sapo_data AppflowFlow#sapo_data}
        :param snowflake: snowflake block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#snowflake AppflowFlow#snowflake}
        :param upsolver: upsolver block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#upsolver AppflowFlow#upsolver}
        :param zendesk: zendesk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#zendesk AppflowFlow#zendesk}
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorProperties(
            custom_connector=custom_connector,
            customer_profiles=customer_profiles,
            event_bridge=event_bridge,
            honeycode=honeycode,
            lookout_metrics=lookout_metrics,
            marketo=marketo,
            redshift=redshift,
            s3=s3,
            salesforce=salesforce,
            sapo_data=sapo_data,
            snowflake=snowflake,
            upsolver=upsolver,
            zendesk=zendesk,
        )

        return typing.cast(None, jsii.invoke(self, "putDestinationConnectorProperties", [value]))

    @jsii.member(jsii_name="resetApiVersion")
    def reset_api_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiVersion", []))

    @jsii.member(jsii_name="resetConnectorProfileName")
    def reset_connector_profile_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectorProfileName", []))

    @builtins.property
    @jsii.member(jsii_name="destinationConnectorProperties")
    def destination_connector_properties(
        self,
    ) -> AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesOutputReference:
        return typing.cast(AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesOutputReference, jsii.get(self, "destinationConnectorProperties"))

    @builtins.property
    @jsii.member(jsii_name="apiVersionInput")
    def api_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="connectorProfileNameInput")
    def connector_profile_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectorProfileNameInput"))

    @builtins.property
    @jsii.member(jsii_name="connectorTypeInput")
    def connector_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectorTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationConnectorPropertiesInput")
    def destination_connector_properties_input(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorProperties]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorProperties], jsii.get(self, "destinationConnectorPropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="apiVersion")
    def api_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiVersion"))

    @api_version.setter
    def api_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__810d26b549f0783623500638c2a63bc866d93547680a999df3c7b8887e89e431)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiVersion", value)

    @builtins.property
    @jsii.member(jsii_name="connectorProfileName")
    def connector_profile_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectorProfileName"))

    @connector_profile_name.setter
    def connector_profile_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7e19c26b990bbe4e99049b99d55c1be4978dbb61233e0a813613c563b00770c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectorProfileName", value)

    @builtins.property
    @jsii.member(jsii_name="connectorType")
    def connector_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectorType"))

    @connector_type.setter
    def connector_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97923149f1b92148788243d745129fe5aa8c1ad9aaa2625563569181f688eab6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectorType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppflowFlowDestinationFlowConfig, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppflowFlowDestinationFlowConfig, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfig, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a56b7a0f75125f2079e677d2cc3e88239a7bca7241828583419a0b17d595cce8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowSourceFlowConfig",
    jsii_struct_bases=[],
    name_mapping={
        "connector_type": "connectorType",
        "source_connector_properties": "sourceConnectorProperties",
        "api_version": "apiVersion",
        "connector_profile_name": "connectorProfileName",
        "incremental_pull_config": "incrementalPullConfig",
    },
)
class AppflowFlowSourceFlowConfig:
    def __init__(
        self,
        *,
        connector_type: builtins.str,
        source_connector_properties: typing.Union["AppflowFlowSourceFlowConfigSourceConnectorProperties", typing.Dict[builtins.str, typing.Any]],
        api_version: typing.Optional[builtins.str] = None,
        connector_profile_name: typing.Optional[builtins.str] = None,
        incremental_pull_config: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigIncrementalPullConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connector_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#connector_type AppflowFlow#connector_type}.
        :param source_connector_properties: source_connector_properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#source_connector_properties AppflowFlow#source_connector_properties}
        :param api_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#api_version AppflowFlow#api_version}.
        :param connector_profile_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#connector_profile_name AppflowFlow#connector_profile_name}.
        :param incremental_pull_config: incremental_pull_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#incremental_pull_config AppflowFlow#incremental_pull_config}
        '''
        if isinstance(source_connector_properties, dict):
            source_connector_properties = AppflowFlowSourceFlowConfigSourceConnectorProperties(**source_connector_properties)
        if isinstance(incremental_pull_config, dict):
            incremental_pull_config = AppflowFlowSourceFlowConfigIncrementalPullConfig(**incremental_pull_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce547e06a2051ca336319ed88317d3f218336581be8b722f2493d09f6ed59f85)
            check_type(argname="argument connector_type", value=connector_type, expected_type=type_hints["connector_type"])
            check_type(argname="argument source_connector_properties", value=source_connector_properties, expected_type=type_hints["source_connector_properties"])
            check_type(argname="argument api_version", value=api_version, expected_type=type_hints["api_version"])
            check_type(argname="argument connector_profile_name", value=connector_profile_name, expected_type=type_hints["connector_profile_name"])
            check_type(argname="argument incremental_pull_config", value=incremental_pull_config, expected_type=type_hints["incremental_pull_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "connector_type": connector_type,
            "source_connector_properties": source_connector_properties,
        }
        if api_version is not None:
            self._values["api_version"] = api_version
        if connector_profile_name is not None:
            self._values["connector_profile_name"] = connector_profile_name
        if incremental_pull_config is not None:
            self._values["incremental_pull_config"] = incremental_pull_config

    @builtins.property
    def connector_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#connector_type AppflowFlow#connector_type}.'''
        result = self._values.get("connector_type")
        assert result is not None, "Required property 'connector_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_connector_properties(
        self,
    ) -> "AppflowFlowSourceFlowConfigSourceConnectorProperties":
        '''source_connector_properties block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#source_connector_properties AppflowFlow#source_connector_properties}
        '''
        result = self._values.get("source_connector_properties")
        assert result is not None, "Required property 'source_connector_properties' is missing"
        return typing.cast("AppflowFlowSourceFlowConfigSourceConnectorProperties", result)

    @builtins.property
    def api_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#api_version AppflowFlow#api_version}.'''
        result = self._values.get("api_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def connector_profile_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#connector_profile_name AppflowFlow#connector_profile_name}.'''
        result = self._values.get("connector_profile_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def incremental_pull_config(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigIncrementalPullConfig"]:
        '''incremental_pull_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#incremental_pull_config AppflowFlow#incremental_pull_config}
        '''
        result = self._values.get("incremental_pull_config")
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigIncrementalPullConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowSourceFlowConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowSourceFlowConfigIncrementalPullConfig",
    jsii_struct_bases=[],
    name_mapping={"datetime_type_field_name": "datetimeTypeFieldName"},
)
class AppflowFlowSourceFlowConfigIncrementalPullConfig:
    def __init__(
        self,
        *,
        datetime_type_field_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param datetime_type_field_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#datetime_type_field_name AppflowFlow#datetime_type_field_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2321d8ed3602781728fa5b16bec40274daa8e75e5c648d7284891a7ee5dfe65d)
            check_type(argname="argument datetime_type_field_name", value=datetime_type_field_name, expected_type=type_hints["datetime_type_field_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if datetime_type_field_name is not None:
            self._values["datetime_type_field_name"] = datetime_type_field_name

    @builtins.property
    def datetime_type_field_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#datetime_type_field_name AppflowFlow#datetime_type_field_name}.'''
        result = self._values.get("datetime_type_field_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowSourceFlowConfigIncrementalPullConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowSourceFlowConfigIncrementalPullConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowSourceFlowConfigIncrementalPullConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0ef36e04c9d63b905f7f57b8e9ff132eeb489f39417896ad5533b2681b96e05e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDatetimeTypeFieldName")
    def reset_datetime_type_field_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatetimeTypeFieldName", []))

    @builtins.property
    @jsii.member(jsii_name="datetimeTypeFieldNameInput")
    def datetime_type_field_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datetimeTypeFieldNameInput"))

    @builtins.property
    @jsii.member(jsii_name="datetimeTypeFieldName")
    def datetime_type_field_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datetimeTypeFieldName"))

    @datetime_type_field_name.setter
    def datetime_type_field_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3bf2b09568c31115e3a32cfb233fe44163e5296eb65430b31578f9ccae46502)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datetimeTypeFieldName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigIncrementalPullConfig]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigIncrementalPullConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowSourceFlowConfigIncrementalPullConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__988406aeb3d4ab545ef5f5410a20c151a94cba71d7506c4129a9406e38ef2e02)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowFlowSourceFlowConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowSourceFlowConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fa1b23f4e269563269bc74962fe981502fb9d9d1e7278444b6a4cc12755d499e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putIncrementalPullConfig")
    def put_incremental_pull_config(
        self,
        *,
        datetime_type_field_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param datetime_type_field_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#datetime_type_field_name AppflowFlow#datetime_type_field_name}.
        '''
        value = AppflowFlowSourceFlowConfigIncrementalPullConfig(
            datetime_type_field_name=datetime_type_field_name
        )

        return typing.cast(None, jsii.invoke(self, "putIncrementalPullConfig", [value]))

    @jsii.member(jsii_name="putSourceConnectorProperties")
    def put_source_connector_properties(
        self,
        *,
        amplitude: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesAmplitude", typing.Dict[builtins.str, typing.Any]]] = None,
        custom_connector: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesCustomConnector", typing.Dict[builtins.str, typing.Any]]] = None,
        datadog: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesDatadog", typing.Dict[builtins.str, typing.Any]]] = None,
        dynatrace: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesDynatrace", typing.Dict[builtins.str, typing.Any]]] = None,
        google_analytics: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalytics", typing.Dict[builtins.str, typing.Any]]] = None,
        infor_nexus: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesInforNexus", typing.Dict[builtins.str, typing.Any]]] = None,
        marketo: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesMarketo", typing.Dict[builtins.str, typing.Any]]] = None,
        s3: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3", typing.Dict[builtins.str, typing.Any]]] = None,
        salesforce: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesSalesforce", typing.Dict[builtins.str, typing.Any]]] = None,
        sapo_data: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesSapoData", typing.Dict[builtins.str, typing.Any]]] = None,
        service_now: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesServiceNow", typing.Dict[builtins.str, typing.Any]]] = None,
        singular: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesSingular", typing.Dict[builtins.str, typing.Any]]] = None,
        slack: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesSlack", typing.Dict[builtins.str, typing.Any]]] = None,
        trendmicro: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesTrendmicro", typing.Dict[builtins.str, typing.Any]]] = None,
        veeva: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesVeeva", typing.Dict[builtins.str, typing.Any]]] = None,
        zendesk: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesZendesk", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param amplitude: amplitude block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#amplitude AppflowFlow#amplitude}
        :param custom_connector: custom_connector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#custom_connector AppflowFlow#custom_connector}
        :param datadog: datadog block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#datadog AppflowFlow#datadog}
        :param dynatrace: dynatrace block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#dynatrace AppflowFlow#dynatrace}
        :param google_analytics: google_analytics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#google_analytics AppflowFlow#google_analytics}
        :param infor_nexus: infor_nexus block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#infor_nexus AppflowFlow#infor_nexus}
        :param marketo: marketo block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#marketo AppflowFlow#marketo}
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#s3 AppflowFlow#s3}
        :param salesforce: salesforce block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#salesforce AppflowFlow#salesforce}
        :param sapo_data: sapo_data block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#sapo_data AppflowFlow#sapo_data}
        :param service_now: service_now block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#service_now AppflowFlow#service_now}
        :param singular: singular block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#singular AppflowFlow#singular}
        :param slack: slack block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#slack AppflowFlow#slack}
        :param trendmicro: trendmicro block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#trendmicro AppflowFlow#trendmicro}
        :param veeva: veeva block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#veeva AppflowFlow#veeva}
        :param zendesk: zendesk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#zendesk AppflowFlow#zendesk}
        '''
        value = AppflowFlowSourceFlowConfigSourceConnectorProperties(
            amplitude=amplitude,
            custom_connector=custom_connector,
            datadog=datadog,
            dynatrace=dynatrace,
            google_analytics=google_analytics,
            infor_nexus=infor_nexus,
            marketo=marketo,
            s3=s3,
            salesforce=salesforce,
            sapo_data=sapo_data,
            service_now=service_now,
            singular=singular,
            slack=slack,
            trendmicro=trendmicro,
            veeva=veeva,
            zendesk=zendesk,
        )

        return typing.cast(None, jsii.invoke(self, "putSourceConnectorProperties", [value]))

    @jsii.member(jsii_name="resetApiVersion")
    def reset_api_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiVersion", []))

    @jsii.member(jsii_name="resetConnectorProfileName")
    def reset_connector_profile_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectorProfileName", []))

    @jsii.member(jsii_name="resetIncrementalPullConfig")
    def reset_incremental_pull_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncrementalPullConfig", []))

    @builtins.property
    @jsii.member(jsii_name="incrementalPullConfig")
    def incremental_pull_config(
        self,
    ) -> AppflowFlowSourceFlowConfigIncrementalPullConfigOutputReference:
        return typing.cast(AppflowFlowSourceFlowConfigIncrementalPullConfigOutputReference, jsii.get(self, "incrementalPullConfig"))

    @builtins.property
    @jsii.member(jsii_name="sourceConnectorProperties")
    def source_connector_properties(
        self,
    ) -> "AppflowFlowSourceFlowConfigSourceConnectorPropertiesOutputReference":
        return typing.cast("AppflowFlowSourceFlowConfigSourceConnectorPropertiesOutputReference", jsii.get(self, "sourceConnectorProperties"))

    @builtins.property
    @jsii.member(jsii_name="apiVersionInput")
    def api_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="connectorProfileNameInput")
    def connector_profile_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectorProfileNameInput"))

    @builtins.property
    @jsii.member(jsii_name="connectorTypeInput")
    def connector_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectorTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="incrementalPullConfigInput")
    def incremental_pull_config_input(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigIncrementalPullConfig]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigIncrementalPullConfig], jsii.get(self, "incrementalPullConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceConnectorPropertiesInput")
    def source_connector_properties_input(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorProperties"]:
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorProperties"], jsii.get(self, "sourceConnectorPropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="apiVersion")
    def api_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiVersion"))

    @api_version.setter
    def api_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be957c3f328450eafb8e8837557171642752da422394c7791fa7a4c2a75f5b31)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiVersion", value)

    @builtins.property
    @jsii.member(jsii_name="connectorProfileName")
    def connector_profile_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectorProfileName"))

    @connector_profile_name.setter
    def connector_profile_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06d28d949a050c1189293b6eb42df4234f603d867027436294f8ea1aa4920d25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectorProfileName", value)

    @builtins.property
    @jsii.member(jsii_name="connectorType")
    def connector_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectorType"))

    @connector_type.setter
    def connector_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f36c789f7cc9ed014a60c08c309f1bd5fccc26292641b67b79e9615339d5878)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectorType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppflowFlowSourceFlowConfig]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowSourceFlowConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7d1fa6d015847acb471824e5c7a9e932305b8080660e0ea34393d464c2f107b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorProperties",
    jsii_struct_bases=[],
    name_mapping={
        "amplitude": "amplitude",
        "custom_connector": "customConnector",
        "datadog": "datadog",
        "dynatrace": "dynatrace",
        "google_analytics": "googleAnalytics",
        "infor_nexus": "inforNexus",
        "marketo": "marketo",
        "s3": "s3",
        "salesforce": "salesforce",
        "sapo_data": "sapoData",
        "service_now": "serviceNow",
        "singular": "singular",
        "slack": "slack",
        "trendmicro": "trendmicro",
        "veeva": "veeva",
        "zendesk": "zendesk",
    },
)
class AppflowFlowSourceFlowConfigSourceConnectorProperties:
    def __init__(
        self,
        *,
        amplitude: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesAmplitude", typing.Dict[builtins.str, typing.Any]]] = None,
        custom_connector: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesCustomConnector", typing.Dict[builtins.str, typing.Any]]] = None,
        datadog: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesDatadog", typing.Dict[builtins.str, typing.Any]]] = None,
        dynatrace: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesDynatrace", typing.Dict[builtins.str, typing.Any]]] = None,
        google_analytics: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalytics", typing.Dict[builtins.str, typing.Any]]] = None,
        infor_nexus: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesInforNexus", typing.Dict[builtins.str, typing.Any]]] = None,
        marketo: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesMarketo", typing.Dict[builtins.str, typing.Any]]] = None,
        s3: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3", typing.Dict[builtins.str, typing.Any]]] = None,
        salesforce: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesSalesforce", typing.Dict[builtins.str, typing.Any]]] = None,
        sapo_data: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesSapoData", typing.Dict[builtins.str, typing.Any]]] = None,
        service_now: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesServiceNow", typing.Dict[builtins.str, typing.Any]]] = None,
        singular: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesSingular", typing.Dict[builtins.str, typing.Any]]] = None,
        slack: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesSlack", typing.Dict[builtins.str, typing.Any]]] = None,
        trendmicro: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesTrendmicro", typing.Dict[builtins.str, typing.Any]]] = None,
        veeva: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesVeeva", typing.Dict[builtins.str, typing.Any]]] = None,
        zendesk: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesZendesk", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param amplitude: amplitude block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#amplitude AppflowFlow#amplitude}
        :param custom_connector: custom_connector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#custom_connector AppflowFlow#custom_connector}
        :param datadog: datadog block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#datadog AppflowFlow#datadog}
        :param dynatrace: dynatrace block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#dynatrace AppflowFlow#dynatrace}
        :param google_analytics: google_analytics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#google_analytics AppflowFlow#google_analytics}
        :param infor_nexus: infor_nexus block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#infor_nexus AppflowFlow#infor_nexus}
        :param marketo: marketo block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#marketo AppflowFlow#marketo}
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#s3 AppflowFlow#s3}
        :param salesforce: salesforce block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#salesforce AppflowFlow#salesforce}
        :param sapo_data: sapo_data block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#sapo_data AppflowFlow#sapo_data}
        :param service_now: service_now block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#service_now AppflowFlow#service_now}
        :param singular: singular block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#singular AppflowFlow#singular}
        :param slack: slack block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#slack AppflowFlow#slack}
        :param trendmicro: trendmicro block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#trendmicro AppflowFlow#trendmicro}
        :param veeva: veeva block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#veeva AppflowFlow#veeva}
        :param zendesk: zendesk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#zendesk AppflowFlow#zendesk}
        '''
        if isinstance(amplitude, dict):
            amplitude = AppflowFlowSourceFlowConfigSourceConnectorPropertiesAmplitude(**amplitude)
        if isinstance(custom_connector, dict):
            custom_connector = AppflowFlowSourceFlowConfigSourceConnectorPropertiesCustomConnector(**custom_connector)
        if isinstance(datadog, dict):
            datadog = AppflowFlowSourceFlowConfigSourceConnectorPropertiesDatadog(**datadog)
        if isinstance(dynatrace, dict):
            dynatrace = AppflowFlowSourceFlowConfigSourceConnectorPropertiesDynatrace(**dynatrace)
        if isinstance(google_analytics, dict):
            google_analytics = AppflowFlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalytics(**google_analytics)
        if isinstance(infor_nexus, dict):
            infor_nexus = AppflowFlowSourceFlowConfigSourceConnectorPropertiesInforNexus(**infor_nexus)
        if isinstance(marketo, dict):
            marketo = AppflowFlowSourceFlowConfigSourceConnectorPropertiesMarketo(**marketo)
        if isinstance(s3, dict):
            s3 = AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3(**s3)
        if isinstance(salesforce, dict):
            salesforce = AppflowFlowSourceFlowConfigSourceConnectorPropertiesSalesforce(**salesforce)
        if isinstance(sapo_data, dict):
            sapo_data = AppflowFlowSourceFlowConfigSourceConnectorPropertiesSapoData(**sapo_data)
        if isinstance(service_now, dict):
            service_now = AppflowFlowSourceFlowConfigSourceConnectorPropertiesServiceNow(**service_now)
        if isinstance(singular, dict):
            singular = AppflowFlowSourceFlowConfigSourceConnectorPropertiesSingular(**singular)
        if isinstance(slack, dict):
            slack = AppflowFlowSourceFlowConfigSourceConnectorPropertiesSlack(**slack)
        if isinstance(trendmicro, dict):
            trendmicro = AppflowFlowSourceFlowConfigSourceConnectorPropertiesTrendmicro(**trendmicro)
        if isinstance(veeva, dict):
            veeva = AppflowFlowSourceFlowConfigSourceConnectorPropertiesVeeva(**veeva)
        if isinstance(zendesk, dict):
            zendesk = AppflowFlowSourceFlowConfigSourceConnectorPropertiesZendesk(**zendesk)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e7ea0597897f3c6b757dded98bd088c6998b303f2c2c642319290a4eab1bb3a)
            check_type(argname="argument amplitude", value=amplitude, expected_type=type_hints["amplitude"])
            check_type(argname="argument custom_connector", value=custom_connector, expected_type=type_hints["custom_connector"])
            check_type(argname="argument datadog", value=datadog, expected_type=type_hints["datadog"])
            check_type(argname="argument dynatrace", value=dynatrace, expected_type=type_hints["dynatrace"])
            check_type(argname="argument google_analytics", value=google_analytics, expected_type=type_hints["google_analytics"])
            check_type(argname="argument infor_nexus", value=infor_nexus, expected_type=type_hints["infor_nexus"])
            check_type(argname="argument marketo", value=marketo, expected_type=type_hints["marketo"])
            check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
            check_type(argname="argument salesforce", value=salesforce, expected_type=type_hints["salesforce"])
            check_type(argname="argument sapo_data", value=sapo_data, expected_type=type_hints["sapo_data"])
            check_type(argname="argument service_now", value=service_now, expected_type=type_hints["service_now"])
            check_type(argname="argument singular", value=singular, expected_type=type_hints["singular"])
            check_type(argname="argument slack", value=slack, expected_type=type_hints["slack"])
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
        if infor_nexus is not None:
            self._values["infor_nexus"] = infor_nexus
        if marketo is not None:
            self._values["marketo"] = marketo
        if s3 is not None:
            self._values["s3"] = s3
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
        if trendmicro is not None:
            self._values["trendmicro"] = trendmicro
        if veeva is not None:
            self._values["veeva"] = veeva
        if zendesk is not None:
            self._values["zendesk"] = zendesk

    @builtins.property
    def amplitude(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesAmplitude"]:
        '''amplitude block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#amplitude AppflowFlow#amplitude}
        '''
        result = self._values.get("amplitude")
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesAmplitude"], result)

    @builtins.property
    def custom_connector(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesCustomConnector"]:
        '''custom_connector block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#custom_connector AppflowFlow#custom_connector}
        '''
        result = self._values.get("custom_connector")
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesCustomConnector"], result)

    @builtins.property
    def datadog(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesDatadog"]:
        '''datadog block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#datadog AppflowFlow#datadog}
        '''
        result = self._values.get("datadog")
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesDatadog"], result)

    @builtins.property
    def dynatrace(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesDynatrace"]:
        '''dynatrace block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#dynatrace AppflowFlow#dynatrace}
        '''
        result = self._values.get("dynatrace")
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesDynatrace"], result)

    @builtins.property
    def google_analytics(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalytics"]:
        '''google_analytics block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#google_analytics AppflowFlow#google_analytics}
        '''
        result = self._values.get("google_analytics")
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalytics"], result)

    @builtins.property
    def infor_nexus(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesInforNexus"]:
        '''infor_nexus block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#infor_nexus AppflowFlow#infor_nexus}
        '''
        result = self._values.get("infor_nexus")
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesInforNexus"], result)

    @builtins.property
    def marketo(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesMarketo"]:
        '''marketo block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#marketo AppflowFlow#marketo}
        '''
        result = self._values.get("marketo")
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesMarketo"], result)

    @builtins.property
    def s3(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3"]:
        '''s3 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#s3 AppflowFlow#s3}
        '''
        result = self._values.get("s3")
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3"], result)

    @builtins.property
    def salesforce(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesSalesforce"]:
        '''salesforce block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#salesforce AppflowFlow#salesforce}
        '''
        result = self._values.get("salesforce")
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesSalesforce"], result)

    @builtins.property
    def sapo_data(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesSapoData"]:
        '''sapo_data block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#sapo_data AppflowFlow#sapo_data}
        '''
        result = self._values.get("sapo_data")
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesSapoData"], result)

    @builtins.property
    def service_now(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesServiceNow"]:
        '''service_now block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#service_now AppflowFlow#service_now}
        '''
        result = self._values.get("service_now")
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesServiceNow"], result)

    @builtins.property
    def singular(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesSingular"]:
        '''singular block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#singular AppflowFlow#singular}
        '''
        result = self._values.get("singular")
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesSingular"], result)

    @builtins.property
    def slack(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesSlack"]:
        '''slack block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#slack AppflowFlow#slack}
        '''
        result = self._values.get("slack")
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesSlack"], result)

    @builtins.property
    def trendmicro(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesTrendmicro"]:
        '''trendmicro block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#trendmicro AppflowFlow#trendmicro}
        '''
        result = self._values.get("trendmicro")
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesTrendmicro"], result)

    @builtins.property
    def veeva(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesVeeva"]:
        '''veeva block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#veeva AppflowFlow#veeva}
        '''
        result = self._values.get("veeva")
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesVeeva"], result)

    @builtins.property
    def zendesk(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesZendesk"]:
        '''zendesk block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#zendesk AppflowFlow#zendesk}
        '''
        result = self._values.get("zendesk")
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesZendesk"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowSourceFlowConfigSourceConnectorProperties(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesAmplitude",
    jsii_struct_bases=[],
    name_mapping={"object": "object"},
)
class AppflowFlowSourceFlowConfigSourceConnectorPropertiesAmplitude:
    def __init__(self, *, object: builtins.str) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__313a41e7f6563d41145bf4583a7b3ad73372f363a115f27c25ed60fc41fb1117)
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "object": object,
        }

    @builtins.property
    def object(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.'''
        result = self._values.get("object")
        assert result is not None, "Required property 'object' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowSourceFlowConfigSourceConnectorPropertiesAmplitude(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowSourceFlowConfigSourceConnectorPropertiesAmplitudeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesAmplitudeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1b20de641b47d63bdc1e049c9f5c782d36645e94e3b0a76f469ac6178ed3289e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="objectInput")
    def object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "object"))

    @object.setter
    def object(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d3d5d52a0c07cff545302d28f2cf35334114c3836516ba9304dfc175181ccf3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "object", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesAmplitude]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesAmplitude], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesAmplitude],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff3d001bb9a1c228ba3c001a6ea400733d0689e31fb8185556f3957511673a7f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesCustomConnector",
    jsii_struct_bases=[],
    name_mapping={
        "entity_name": "entityName",
        "custom_properties": "customProperties",
    },
)
class AppflowFlowSourceFlowConfigSourceConnectorPropertiesCustomConnector:
    def __init__(
        self,
        *,
        entity_name: builtins.str,
        custom_properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param entity_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#entity_name AppflowFlow#entity_name}.
        :param custom_properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#custom_properties AppflowFlow#custom_properties}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d421cd0d8118776bd2383dafa414c36b1a0037661acb5408d456555d5b65ad00)
            check_type(argname="argument entity_name", value=entity_name, expected_type=type_hints["entity_name"])
            check_type(argname="argument custom_properties", value=custom_properties, expected_type=type_hints["custom_properties"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "entity_name": entity_name,
        }
        if custom_properties is not None:
            self._values["custom_properties"] = custom_properties

    @builtins.property
    def entity_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#entity_name AppflowFlow#entity_name}.'''
        result = self._values.get("entity_name")
        assert result is not None, "Required property 'entity_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def custom_properties(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#custom_properties AppflowFlow#custom_properties}.'''
        result = self._values.get("custom_properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowSourceFlowConfigSourceConnectorPropertiesCustomConnector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowSourceFlowConfigSourceConnectorPropertiesCustomConnectorOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesCustomConnectorOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e9dc41f9d628a7593ee11035d566eb516400f06fa23d65dcb32830edbe22ad98)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCustomProperties")
    def reset_custom_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomProperties", []))

    @builtins.property
    @jsii.member(jsii_name="customPropertiesInput")
    def custom_properties_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "customPropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="entityNameInput")
    def entity_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "entityNameInput"))

    @builtins.property
    @jsii.member(jsii_name="customProperties")
    def custom_properties(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "customProperties"))

    @custom_properties.setter
    def custom_properties(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48ae880a30c9e480c94ec3568288cb8ecfc8005697f06965e07a57185058604d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customProperties", value)

    @builtins.property
    @jsii.member(jsii_name="entityName")
    def entity_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "entityName"))

    @entity_name.setter
    def entity_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0b27985a2a4f50617b6b6c8df70a18bf3b3aae4210fef4cf26a30ff8e830893)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "entityName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesCustomConnector]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesCustomConnector], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesCustomConnector],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e13e17c0d47d0ec92684bbdb7a51a1ee69b825d3c59cf960ae6338c2b1b95f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesDatadog",
    jsii_struct_bases=[],
    name_mapping={"object": "object"},
)
class AppflowFlowSourceFlowConfigSourceConnectorPropertiesDatadog:
    def __init__(self, *, object: builtins.str) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5923e712001b9604785e2ba6a592e958d155fc2af9fbd6e0112c97415bf303b5)
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "object": object,
        }

    @builtins.property
    def object(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.'''
        result = self._values.get("object")
        assert result is not None, "Required property 'object' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowSourceFlowConfigSourceConnectorPropertiesDatadog(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowSourceFlowConfigSourceConnectorPropertiesDatadogOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesDatadogOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__10b88781d36e2d7c5f49216517838d0457437c36ac3856843807bc0e14d134ea)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="objectInput")
    def object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "object"))

    @object.setter
    def object(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccd37e5134679468d3104f3ec70b47c56a620eb0d57628f49f6a673661d68e22)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "object", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesDatadog]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesDatadog], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesDatadog],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b91cdbfec7c6e41a5dcde39d473eb5d6cd3eb9403ded9a1f66a3e7ec11f0ad94)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesDynatrace",
    jsii_struct_bases=[],
    name_mapping={"object": "object"},
)
class AppflowFlowSourceFlowConfigSourceConnectorPropertiesDynatrace:
    def __init__(self, *, object: builtins.str) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba9e5d28a9ab161b56194ec840e8e5a8539be3e23ad87a0314eccd3ca531e5ae)
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "object": object,
        }

    @builtins.property
    def object(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.'''
        result = self._values.get("object")
        assert result is not None, "Required property 'object' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowSourceFlowConfigSourceConnectorPropertiesDynatrace(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowSourceFlowConfigSourceConnectorPropertiesDynatraceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesDynatraceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3d19abdea4d788b7be1236c9a2a5efc8238ca00d1e7a3e84cc04666b2599f2e4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="objectInput")
    def object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "object"))

    @object.setter
    def object(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eee32d4b134ebe159a79ca548a451549b53cead22852fc7d98ccfc1e057afd63)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "object", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesDynatrace]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesDynatrace], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesDynatrace],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f3091d872232e828a79e6e53d426bc5300cf3eef9ecaffebf79ff1ce5cfc57d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalytics",
    jsii_struct_bases=[],
    name_mapping={"object": "object"},
)
class AppflowFlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalytics:
    def __init__(self, *, object: builtins.str) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac43f824241a31a8cce56574601922c425cd1ab2e5b6f3725c94005c371609b1)
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "object": object,
        }

    @builtins.property
    def object(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.'''
        result = self._values.get("object")
        assert result is not None, "Required property 'object' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalytics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalyticsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalyticsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__82a329040d67c8b9634708784f20d484bcd7f09f3a7ad3cc22024313f68aaa88)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="objectInput")
    def object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "object"))

    @object.setter
    def object(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c385e86541dae5eb13858e713e026bff8827ab3e1179da53661f918ac160f17)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "object", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalytics]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalytics], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalytics],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23f3305814eb995a28f85449f5f0a38012ec1a4e572a2da199498d05aa68cc9d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesInforNexus",
    jsii_struct_bases=[],
    name_mapping={"object": "object"},
)
class AppflowFlowSourceFlowConfigSourceConnectorPropertiesInforNexus:
    def __init__(self, *, object: builtins.str) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7e5977a145ad6010c5067b8398bffe37a4b39b692b2025ee0b00a6228c192d1)
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "object": object,
        }

    @builtins.property
    def object(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.'''
        result = self._values.get("object")
        assert result is not None, "Required property 'object' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowSourceFlowConfigSourceConnectorPropertiesInforNexus(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowSourceFlowConfigSourceConnectorPropertiesInforNexusOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesInforNexusOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__225c4e397b8d864e8520a74d5813849b0d5e66cc01a9fe6ccdb20625ae507f8d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="objectInput")
    def object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "object"))

    @object.setter
    def object(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d56181ff258a8738ff6715bd737501741463807af122e440931efc3b768abb71)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "object", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesInforNexus]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesInforNexus], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesInforNexus],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e03c854a79317d654dd8004742a5bff4f0bc6ec36f20d26457efdae521408329)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesMarketo",
    jsii_struct_bases=[],
    name_mapping={"object": "object"},
)
class AppflowFlowSourceFlowConfigSourceConnectorPropertiesMarketo:
    def __init__(self, *, object: builtins.str) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__face3f520d057155d23e57c965cef25d8786c298c2ecbbec516e1adb48c94a7a)
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "object": object,
        }

    @builtins.property
    def object(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.'''
        result = self._values.get("object")
        assert result is not None, "Required property 'object' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowSourceFlowConfigSourceConnectorPropertiesMarketo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowSourceFlowConfigSourceConnectorPropertiesMarketoOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesMarketoOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__16d5338aed64a02109ceeaa617a06fe0cc03c0b87920caebc6b28c7c53c69b7c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="objectInput")
    def object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "object"))

    @object.setter
    def object(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61ca09d1ebf3efc8c26f05906199aa4f5fb39776c29ac36f29292845cbdebe6e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "object", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesMarketo]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesMarketo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesMarketo],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d35a8ad3192fb9c582893f02c11b59df2dc3ca2149b416107e902274693f52b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowFlowSourceFlowConfigSourceConnectorPropertiesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c602a89048f3b41d08aeaa483a25a37a0bc8db26fe855e276b5332027064c95c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAmplitude")
    def put_amplitude(self, *, object: builtins.str) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        '''
        value = AppflowFlowSourceFlowConfigSourceConnectorPropertiesAmplitude(
            object=object
        )

        return typing.cast(None, jsii.invoke(self, "putAmplitude", [value]))

    @jsii.member(jsii_name="putCustomConnector")
    def put_custom_connector(
        self,
        *,
        entity_name: builtins.str,
        custom_properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param entity_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#entity_name AppflowFlow#entity_name}.
        :param custom_properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#custom_properties AppflowFlow#custom_properties}.
        '''
        value = AppflowFlowSourceFlowConfigSourceConnectorPropertiesCustomConnector(
            entity_name=entity_name, custom_properties=custom_properties
        )

        return typing.cast(None, jsii.invoke(self, "putCustomConnector", [value]))

    @jsii.member(jsii_name="putDatadog")
    def put_datadog(self, *, object: builtins.str) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        '''
        value = AppflowFlowSourceFlowConfigSourceConnectorPropertiesDatadog(
            object=object
        )

        return typing.cast(None, jsii.invoke(self, "putDatadog", [value]))

    @jsii.member(jsii_name="putDynatrace")
    def put_dynatrace(self, *, object: builtins.str) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        '''
        value = AppflowFlowSourceFlowConfigSourceConnectorPropertiesDynatrace(
            object=object
        )

        return typing.cast(None, jsii.invoke(self, "putDynatrace", [value]))

    @jsii.member(jsii_name="putGoogleAnalytics")
    def put_google_analytics(self, *, object: builtins.str) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        '''
        value = AppflowFlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalytics(
            object=object
        )

        return typing.cast(None, jsii.invoke(self, "putGoogleAnalytics", [value]))

    @jsii.member(jsii_name="putInforNexus")
    def put_infor_nexus(self, *, object: builtins.str) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        '''
        value = AppflowFlowSourceFlowConfigSourceConnectorPropertiesInforNexus(
            object=object
        )

        return typing.cast(None, jsii.invoke(self, "putInforNexus", [value]))

    @jsii.member(jsii_name="putMarketo")
    def put_marketo(self, *, object: builtins.str) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        '''
        value = AppflowFlowSourceFlowConfigSourceConnectorPropertiesMarketo(
            object=object
        )

        return typing.cast(None, jsii.invoke(self, "putMarketo", [value]))

    @jsii.member(jsii_name="putS3")
    def put_s3(
        self,
        *,
        bucket_name: builtins.str,
        bucket_prefix: typing.Optional[builtins.str] = None,
        s3_input_format_config: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param s3_input_format_config: s3_input_format_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#s3_input_format_config AppflowFlow#s3_input_format_config}
        '''
        value = AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3(
            bucket_name=bucket_name,
            bucket_prefix=bucket_prefix,
            s3_input_format_config=s3_input_format_config,
        )

        return typing.cast(None, jsii.invoke(self, "putS3", [value]))

    @jsii.member(jsii_name="putSalesforce")
    def put_salesforce(
        self,
        *,
        object: builtins.str,
        enable_dynamic_field_update: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        include_deleted_records: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        :param enable_dynamic_field_update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#enable_dynamic_field_update AppflowFlow#enable_dynamic_field_update}.
        :param include_deleted_records: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#include_deleted_records AppflowFlow#include_deleted_records}.
        '''
        value = AppflowFlowSourceFlowConfigSourceConnectorPropertiesSalesforce(
            object=object,
            enable_dynamic_field_update=enable_dynamic_field_update,
            include_deleted_records=include_deleted_records,
        )

        return typing.cast(None, jsii.invoke(self, "putSalesforce", [value]))

    @jsii.member(jsii_name="putSapoData")
    def put_sapo_data(self, *, object: builtins.str) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        '''
        value = AppflowFlowSourceFlowConfigSourceConnectorPropertiesSapoData(
            object=object
        )

        return typing.cast(None, jsii.invoke(self, "putSapoData", [value]))

    @jsii.member(jsii_name="putServiceNow")
    def put_service_now(self, *, object: builtins.str) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        '''
        value = AppflowFlowSourceFlowConfigSourceConnectorPropertiesServiceNow(
            object=object
        )

        return typing.cast(None, jsii.invoke(self, "putServiceNow", [value]))

    @jsii.member(jsii_name="putSingular")
    def put_singular(self, *, object: builtins.str) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        '''
        value = AppflowFlowSourceFlowConfigSourceConnectorPropertiesSingular(
            object=object
        )

        return typing.cast(None, jsii.invoke(self, "putSingular", [value]))

    @jsii.member(jsii_name="putSlack")
    def put_slack(self, *, object: builtins.str) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        '''
        value = AppflowFlowSourceFlowConfigSourceConnectorPropertiesSlack(
            object=object
        )

        return typing.cast(None, jsii.invoke(self, "putSlack", [value]))

    @jsii.member(jsii_name="putTrendmicro")
    def put_trendmicro(self, *, object: builtins.str) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        '''
        value = AppflowFlowSourceFlowConfigSourceConnectorPropertiesTrendmicro(
            object=object
        )

        return typing.cast(None, jsii.invoke(self, "putTrendmicro", [value]))

    @jsii.member(jsii_name="putVeeva")
    def put_veeva(
        self,
        *,
        object: builtins.str,
        document_type: typing.Optional[builtins.str] = None,
        include_all_versions: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        include_renditions: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        include_source_files: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        :param document_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#document_type AppflowFlow#document_type}.
        :param include_all_versions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#include_all_versions AppflowFlow#include_all_versions}.
        :param include_renditions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#include_renditions AppflowFlow#include_renditions}.
        :param include_source_files: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#include_source_files AppflowFlow#include_source_files}.
        '''
        value = AppflowFlowSourceFlowConfigSourceConnectorPropertiesVeeva(
            object=object,
            document_type=document_type,
            include_all_versions=include_all_versions,
            include_renditions=include_renditions,
            include_source_files=include_source_files,
        )

        return typing.cast(None, jsii.invoke(self, "putVeeva", [value]))

    @jsii.member(jsii_name="putZendesk")
    def put_zendesk(self, *, object: builtins.str) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        '''
        value = AppflowFlowSourceFlowConfigSourceConnectorPropertiesZendesk(
            object=object
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

    @jsii.member(jsii_name="resetInforNexus")
    def reset_infor_nexus(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInforNexus", []))

    @jsii.member(jsii_name="resetMarketo")
    def reset_marketo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMarketo", []))

    @jsii.member(jsii_name="resetS3")
    def reset_s3(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3", []))

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
    ) -> AppflowFlowSourceFlowConfigSourceConnectorPropertiesAmplitudeOutputReference:
        return typing.cast(AppflowFlowSourceFlowConfigSourceConnectorPropertiesAmplitudeOutputReference, jsii.get(self, "amplitude"))

    @builtins.property
    @jsii.member(jsii_name="customConnector")
    def custom_connector(
        self,
    ) -> AppflowFlowSourceFlowConfigSourceConnectorPropertiesCustomConnectorOutputReference:
        return typing.cast(AppflowFlowSourceFlowConfigSourceConnectorPropertiesCustomConnectorOutputReference, jsii.get(self, "customConnector"))

    @builtins.property
    @jsii.member(jsii_name="datadog")
    def datadog(
        self,
    ) -> AppflowFlowSourceFlowConfigSourceConnectorPropertiesDatadogOutputReference:
        return typing.cast(AppflowFlowSourceFlowConfigSourceConnectorPropertiesDatadogOutputReference, jsii.get(self, "datadog"))

    @builtins.property
    @jsii.member(jsii_name="dynatrace")
    def dynatrace(
        self,
    ) -> AppflowFlowSourceFlowConfigSourceConnectorPropertiesDynatraceOutputReference:
        return typing.cast(AppflowFlowSourceFlowConfigSourceConnectorPropertiesDynatraceOutputReference, jsii.get(self, "dynatrace"))

    @builtins.property
    @jsii.member(jsii_name="googleAnalytics")
    def google_analytics(
        self,
    ) -> AppflowFlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalyticsOutputReference:
        return typing.cast(AppflowFlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalyticsOutputReference, jsii.get(self, "googleAnalytics"))

    @builtins.property
    @jsii.member(jsii_name="inforNexus")
    def infor_nexus(
        self,
    ) -> AppflowFlowSourceFlowConfigSourceConnectorPropertiesInforNexusOutputReference:
        return typing.cast(AppflowFlowSourceFlowConfigSourceConnectorPropertiesInforNexusOutputReference, jsii.get(self, "inforNexus"))

    @builtins.property
    @jsii.member(jsii_name="marketo")
    def marketo(
        self,
    ) -> AppflowFlowSourceFlowConfigSourceConnectorPropertiesMarketoOutputReference:
        return typing.cast(AppflowFlowSourceFlowConfigSourceConnectorPropertiesMarketoOutputReference, jsii.get(self, "marketo"))

    @builtins.property
    @jsii.member(jsii_name="s3")
    def s3(
        self,
    ) -> "AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3OutputReference":
        return typing.cast("AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3OutputReference", jsii.get(self, "s3"))

    @builtins.property
    @jsii.member(jsii_name="salesforce")
    def salesforce(
        self,
    ) -> "AppflowFlowSourceFlowConfigSourceConnectorPropertiesSalesforceOutputReference":
        return typing.cast("AppflowFlowSourceFlowConfigSourceConnectorPropertiesSalesforceOutputReference", jsii.get(self, "salesforce"))

    @builtins.property
    @jsii.member(jsii_name="sapoData")
    def sapo_data(
        self,
    ) -> "AppflowFlowSourceFlowConfigSourceConnectorPropertiesSapoDataOutputReference":
        return typing.cast("AppflowFlowSourceFlowConfigSourceConnectorPropertiesSapoDataOutputReference", jsii.get(self, "sapoData"))

    @builtins.property
    @jsii.member(jsii_name="serviceNow")
    def service_now(
        self,
    ) -> "AppflowFlowSourceFlowConfigSourceConnectorPropertiesServiceNowOutputReference":
        return typing.cast("AppflowFlowSourceFlowConfigSourceConnectorPropertiesServiceNowOutputReference", jsii.get(self, "serviceNow"))

    @builtins.property
    @jsii.member(jsii_name="singular")
    def singular(
        self,
    ) -> "AppflowFlowSourceFlowConfigSourceConnectorPropertiesSingularOutputReference":
        return typing.cast("AppflowFlowSourceFlowConfigSourceConnectorPropertiesSingularOutputReference", jsii.get(self, "singular"))

    @builtins.property
    @jsii.member(jsii_name="slack")
    def slack(
        self,
    ) -> "AppflowFlowSourceFlowConfigSourceConnectorPropertiesSlackOutputReference":
        return typing.cast("AppflowFlowSourceFlowConfigSourceConnectorPropertiesSlackOutputReference", jsii.get(self, "slack"))

    @builtins.property
    @jsii.member(jsii_name="trendmicro")
    def trendmicro(
        self,
    ) -> "AppflowFlowSourceFlowConfigSourceConnectorPropertiesTrendmicroOutputReference":
        return typing.cast("AppflowFlowSourceFlowConfigSourceConnectorPropertiesTrendmicroOutputReference", jsii.get(self, "trendmicro"))

    @builtins.property
    @jsii.member(jsii_name="veeva")
    def veeva(
        self,
    ) -> "AppflowFlowSourceFlowConfigSourceConnectorPropertiesVeevaOutputReference":
        return typing.cast("AppflowFlowSourceFlowConfigSourceConnectorPropertiesVeevaOutputReference", jsii.get(self, "veeva"))

    @builtins.property
    @jsii.member(jsii_name="zendesk")
    def zendesk(
        self,
    ) -> "AppflowFlowSourceFlowConfigSourceConnectorPropertiesZendeskOutputReference":
        return typing.cast("AppflowFlowSourceFlowConfigSourceConnectorPropertiesZendeskOutputReference", jsii.get(self, "zendesk"))

    @builtins.property
    @jsii.member(jsii_name="amplitudeInput")
    def amplitude_input(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesAmplitude]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesAmplitude], jsii.get(self, "amplitudeInput"))

    @builtins.property
    @jsii.member(jsii_name="customConnectorInput")
    def custom_connector_input(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesCustomConnector]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesCustomConnector], jsii.get(self, "customConnectorInput"))

    @builtins.property
    @jsii.member(jsii_name="datadogInput")
    def datadog_input(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesDatadog]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesDatadog], jsii.get(self, "datadogInput"))

    @builtins.property
    @jsii.member(jsii_name="dynatraceInput")
    def dynatrace_input(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesDynatrace]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesDynatrace], jsii.get(self, "dynatraceInput"))

    @builtins.property
    @jsii.member(jsii_name="googleAnalyticsInput")
    def google_analytics_input(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalytics]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalytics], jsii.get(self, "googleAnalyticsInput"))

    @builtins.property
    @jsii.member(jsii_name="inforNexusInput")
    def infor_nexus_input(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesInforNexus]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesInforNexus], jsii.get(self, "inforNexusInput"))

    @builtins.property
    @jsii.member(jsii_name="marketoInput")
    def marketo_input(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesMarketo]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesMarketo], jsii.get(self, "marketoInput"))

    @builtins.property
    @jsii.member(jsii_name="s3Input")
    def s3_input(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3"]:
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3"], jsii.get(self, "s3Input"))

    @builtins.property
    @jsii.member(jsii_name="salesforceInput")
    def salesforce_input(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesSalesforce"]:
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesSalesforce"], jsii.get(self, "salesforceInput"))

    @builtins.property
    @jsii.member(jsii_name="sapoDataInput")
    def sapo_data_input(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesSapoData"]:
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesSapoData"], jsii.get(self, "sapoDataInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceNowInput")
    def service_now_input(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesServiceNow"]:
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesServiceNow"], jsii.get(self, "serviceNowInput"))

    @builtins.property
    @jsii.member(jsii_name="singularInput")
    def singular_input(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesSingular"]:
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesSingular"], jsii.get(self, "singularInput"))

    @builtins.property
    @jsii.member(jsii_name="slackInput")
    def slack_input(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesSlack"]:
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesSlack"], jsii.get(self, "slackInput"))

    @builtins.property
    @jsii.member(jsii_name="trendmicroInput")
    def trendmicro_input(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesTrendmicro"]:
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesTrendmicro"], jsii.get(self, "trendmicroInput"))

    @builtins.property
    @jsii.member(jsii_name="veevaInput")
    def veeva_input(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesVeeva"]:
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesVeeva"], jsii.get(self, "veevaInput"))

    @builtins.property
    @jsii.member(jsii_name="zendeskInput")
    def zendesk_input(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesZendesk"]:
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesZendesk"], jsii.get(self, "zendeskInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorProperties]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorProperties], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorProperties],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ce9b3cc1ebdb06b5bb9d44b3c3c97a5ae117e174068fc2f0055212a0d473bae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "bucket_prefix": "bucketPrefix",
        "s3_input_format_config": "s3InputFormatConfig",
    },
)
class AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3:
    def __init__(
        self,
        *,
        bucket_name: builtins.str,
        bucket_prefix: typing.Optional[builtins.str] = None,
        s3_input_format_config: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param s3_input_format_config: s3_input_format_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#s3_input_format_config AppflowFlow#s3_input_format_config}
        '''
        if isinstance(s3_input_format_config, dict):
            s3_input_format_config = AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfig(**s3_input_format_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b4026e5a258d7cd1c6fe23fa9bb33c72ac9f40f95cec82dd0bddb814e9a9ff0)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
            check_type(argname="argument s3_input_format_config", value=s3_input_format_config, expected_type=type_hints["s3_input_format_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket_name": bucket_name,
        }
        if bucket_prefix is not None:
            self._values["bucket_prefix"] = bucket_prefix
        if s3_input_format_config is not None:
            self._values["s3_input_format_config"] = s3_input_format_config

    @builtins.property
    def bucket_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.'''
        result = self._values.get("bucket_name")
        assert result is not None, "Required property 'bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bucket_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.'''
        result = self._values.get("bucket_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_input_format_config(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfig"]:
        '''s3_input_format_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#s3_input_format_config AppflowFlow#s3_input_format_config}
        '''
        result = self._values.get("s3_input_format_config")
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3OutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3OutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__92bf967637dbd819d4ed6670439242a98ef56e73b2727a71c0d2371fb8a70ad2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putS3InputFormatConfig")
    def put_s3_input_format_config(
        self,
        *,
        s3_input_file_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param s3_input_file_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#s3_input_file_type AppflowFlow#s3_input_file_type}.
        '''
        value = AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfig(
            s3_input_file_type=s3_input_file_type
        )

        return typing.cast(None, jsii.invoke(self, "putS3InputFormatConfig", [value]))

    @jsii.member(jsii_name="resetBucketPrefix")
    def reset_bucket_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketPrefix", []))

    @jsii.member(jsii_name="resetS3InputFormatConfig")
    def reset_s3_input_format_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3InputFormatConfig", []))

    @builtins.property
    @jsii.member(jsii_name="s3InputFormatConfig")
    def s3_input_format_config(
        self,
    ) -> "AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfigOutputReference":
        return typing.cast("AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfigOutputReference", jsii.get(self, "s3InputFormatConfig"))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketPrefixInput")
    def bucket_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="s3InputFormatConfigInput")
    def s3_input_format_config_input(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfig"]:
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfig"], jsii.get(self, "s3InputFormatConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7aa5417c8e0e4d62c8b6d326b58278c3fbd136f74ac1e6350a7c63bdfaeeed0f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="bucketPrefix")
    def bucket_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketPrefix"))

    @bucket_prefix.setter
    def bucket_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8c62ef8f5d7b062f9d088c1f1b1919bef2045d9f059236ea881512dc1623260)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8800a76f95368c91d4175902e25ceb0a2d013676c16ed444aadce4aee7df024)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfig",
    jsii_struct_bases=[],
    name_mapping={"s3_input_file_type": "s3InputFileType"},
)
class AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfig:
    def __init__(
        self,
        *,
        s3_input_file_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param s3_input_file_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#s3_input_file_type AppflowFlow#s3_input_file_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a002120fd1131e020794638ac20aadca7b459fddc50118cd9cbe2aac41f5bfa4)
            check_type(argname="argument s3_input_file_type", value=s3_input_file_type, expected_type=type_hints["s3_input_file_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if s3_input_file_type is not None:
            self._values["s3_input_file_type"] = s3_input_file_type

    @builtins.property
    def s3_input_file_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#s3_input_file_type AppflowFlow#s3_input_file_type}.'''
        result = self._values.get("s3_input_file_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__48ce85ee744b1b1a335fa2ba371ed9fc4d631ebb204b640e4b42a111bf645586)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetS3InputFileType")
    def reset_s3_input_file_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3InputFileType", []))

    @builtins.property
    @jsii.member(jsii_name="s3InputFileTypeInput")
    def s3_input_file_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3InputFileTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="s3InputFileType")
    def s3_input_file_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3InputFileType"))

    @s3_input_file_type.setter
    def s3_input_file_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ce5a4f608982576f8fceca1ff34213816b7d0e16cb99bb1c632c82e975a0308)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3InputFileType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfig]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf0c8c347635ac843d320fe1dec39704ddce58ffb50748ac637404e9f0e927d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesSalesforce",
    jsii_struct_bases=[],
    name_mapping={
        "object": "object",
        "enable_dynamic_field_update": "enableDynamicFieldUpdate",
        "include_deleted_records": "includeDeletedRecords",
    },
)
class AppflowFlowSourceFlowConfigSourceConnectorPropertiesSalesforce:
    def __init__(
        self,
        *,
        object: builtins.str,
        enable_dynamic_field_update: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        include_deleted_records: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        :param enable_dynamic_field_update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#enable_dynamic_field_update AppflowFlow#enable_dynamic_field_update}.
        :param include_deleted_records: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#include_deleted_records AppflowFlow#include_deleted_records}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7701fa60cdc6dcff83073827d8a16ee4bf38489f81aa0c6981eeb0c70abcf1c)
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
            check_type(argname="argument enable_dynamic_field_update", value=enable_dynamic_field_update, expected_type=type_hints["enable_dynamic_field_update"])
            check_type(argname="argument include_deleted_records", value=include_deleted_records, expected_type=type_hints["include_deleted_records"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "object": object,
        }
        if enable_dynamic_field_update is not None:
            self._values["enable_dynamic_field_update"] = enable_dynamic_field_update
        if include_deleted_records is not None:
            self._values["include_deleted_records"] = include_deleted_records

    @builtins.property
    def object(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.'''
        result = self._values.get("object")
        assert result is not None, "Required property 'object' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enable_dynamic_field_update(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#enable_dynamic_field_update AppflowFlow#enable_dynamic_field_update}.'''
        result = self._values.get("enable_dynamic_field_update")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def include_deleted_records(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#include_deleted_records AppflowFlow#include_deleted_records}.'''
        result = self._values.get("include_deleted_records")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowSourceFlowConfigSourceConnectorPropertiesSalesforce(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowSourceFlowConfigSourceConnectorPropertiesSalesforceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesSalesforceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9905973b1b51588ae7fd47305b6c2464cfd602e42b584de02bc27b383b44f4cd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnableDynamicFieldUpdate")
    def reset_enable_dynamic_field_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableDynamicFieldUpdate", []))

    @jsii.member(jsii_name="resetIncludeDeletedRecords")
    def reset_include_deleted_records(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeDeletedRecords", []))

    @builtins.property
    @jsii.member(jsii_name="enableDynamicFieldUpdateInput")
    def enable_dynamic_field_update_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableDynamicFieldUpdateInput"))

    @builtins.property
    @jsii.member(jsii_name="includeDeletedRecordsInput")
    def include_deleted_records_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "includeDeletedRecordsInput"))

    @builtins.property
    @jsii.member(jsii_name="objectInput")
    def object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="enableDynamicFieldUpdate")
    def enable_dynamic_field_update(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableDynamicFieldUpdate"))

    @enable_dynamic_field_update.setter
    def enable_dynamic_field_update(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec3cb7c8805f8061e6f33072fe025be8d6f1c789196ffd3550ab2499c9513998)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableDynamicFieldUpdate", value)

    @builtins.property
    @jsii.member(jsii_name="includeDeletedRecords")
    def include_deleted_records(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "includeDeletedRecords"))

    @include_deleted_records.setter
    def include_deleted_records(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c69745f9bcdb4a98737ecfa4beb6484791433a88272f9dc62d26dde9fb0efd9e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeDeletedRecords", value)

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "object"))

    @object.setter
    def object(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8275062e40e846a5d39b5619f078bf965d4b31d318b461996eecaba30b54984e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "object", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesSalesforce]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesSalesforce], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesSalesforce],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44f25390e269f882d5fcf4c68c0264d3108691c3f128d41dcc6b98e0f3f9c84a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesSapoData",
    jsii_struct_bases=[],
    name_mapping={"object": "object"},
)
class AppflowFlowSourceFlowConfigSourceConnectorPropertiesSapoData:
    def __init__(self, *, object: builtins.str) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d04e62c29ab455578c96db4e4faaf6e874aba450dadd168f4e63fd8a9fe4579e)
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "object": object,
        }

    @builtins.property
    def object(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.'''
        result = self._values.get("object")
        assert result is not None, "Required property 'object' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowSourceFlowConfigSourceConnectorPropertiesSapoData(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowSourceFlowConfigSourceConnectorPropertiesSapoDataOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesSapoDataOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__62ebf0a32c078e39b09d10cfc0520ee526dd1dceaa664180d1ba2c771a5fd2c9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="objectInput")
    def object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "object"))

    @object.setter
    def object(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad4d74a02f909001408bd41b5fb8f3d4438ee544598b5c1957355bbda06239be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "object", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesSapoData]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesSapoData], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesSapoData],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0239ed79b6ee6d72f2d86a137590835d8931bf3891cf4c32182a787afd3c8a2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesServiceNow",
    jsii_struct_bases=[],
    name_mapping={"object": "object"},
)
class AppflowFlowSourceFlowConfigSourceConnectorPropertiesServiceNow:
    def __init__(self, *, object: builtins.str) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__031feb7d4713b5a68075b00d95ac88a1d5a0bf8e6c04d60e50c76a6b074b4a54)
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "object": object,
        }

    @builtins.property
    def object(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.'''
        result = self._values.get("object")
        assert result is not None, "Required property 'object' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowSourceFlowConfigSourceConnectorPropertiesServiceNow(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowSourceFlowConfigSourceConnectorPropertiesServiceNowOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesServiceNowOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9d62c690f8d673f8c800a8236d44322d9a4c14ccfa239947ee7672f8aa763ac0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="objectInput")
    def object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "object"))

    @object.setter
    def object(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a7739c0046874a85f0b2dbd9a6e699959c66f29574703637977a0976bfc67ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "object", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesServiceNow]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesServiceNow], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesServiceNow],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7118541e83f271fd74c69e323c63d8788bb6196677b7bea709123003be54e6bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesSingular",
    jsii_struct_bases=[],
    name_mapping={"object": "object"},
)
class AppflowFlowSourceFlowConfigSourceConnectorPropertiesSingular:
    def __init__(self, *, object: builtins.str) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1921f24b3b55bf2dfede826831cca69a279f7b17e87b85131d320b483a5ad2aa)
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "object": object,
        }

    @builtins.property
    def object(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.'''
        result = self._values.get("object")
        assert result is not None, "Required property 'object' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowSourceFlowConfigSourceConnectorPropertiesSingular(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowSourceFlowConfigSourceConnectorPropertiesSingularOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesSingularOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__91bc991278ebcac9a8f4a8f45475f1bba74fa5c8f9268e5de81997afb9a7e052)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="objectInput")
    def object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "object"))

    @object.setter
    def object(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11dd80a829485da7d3bdcd57a88f1487702089ce19154049ee5e41ae0117a91a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "object", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesSingular]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesSingular], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesSingular],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82a8be23ea2450de509ff444136ca05bf9c05fb9735eef3d33fd6ac02c9bc439)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesSlack",
    jsii_struct_bases=[],
    name_mapping={"object": "object"},
)
class AppflowFlowSourceFlowConfigSourceConnectorPropertiesSlack:
    def __init__(self, *, object: builtins.str) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e4abe7f73381c8cd0007198df2b05e0639c85492bdeada4ddd386cb1d5636aa)
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "object": object,
        }

    @builtins.property
    def object(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.'''
        result = self._values.get("object")
        assert result is not None, "Required property 'object' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowSourceFlowConfigSourceConnectorPropertiesSlack(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowSourceFlowConfigSourceConnectorPropertiesSlackOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesSlackOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5da4a5acb11bb5a04cbf1890588db1d3b6805d00244f24a9fe9b5e377a9a5063)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="objectInput")
    def object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "object"))

    @object.setter
    def object(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a53050bc3706abbb931fb7bceb10eeaed23523834174e0917ac6fbdddd60adcf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "object", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesSlack]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesSlack], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesSlack],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a491833880c74674727d92f3debe4f230101dae4209980403f041685b382ce2e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesTrendmicro",
    jsii_struct_bases=[],
    name_mapping={"object": "object"},
)
class AppflowFlowSourceFlowConfigSourceConnectorPropertiesTrendmicro:
    def __init__(self, *, object: builtins.str) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__868bffa5ecf992097896ad19dbb548d2e8f304400ca194823bef21ca0baa4a04)
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "object": object,
        }

    @builtins.property
    def object(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.'''
        result = self._values.get("object")
        assert result is not None, "Required property 'object' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowSourceFlowConfigSourceConnectorPropertiesTrendmicro(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowSourceFlowConfigSourceConnectorPropertiesTrendmicroOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesTrendmicroOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e244f917995e5183de25e5f6402224fd9b20d4953a8871c2a95a8030cf7690a5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="objectInput")
    def object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "object"))

    @object.setter
    def object(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a95103c804e0af53ea7d1f15ad3e11c4f482404778cdbb76f9bcdcf660c6b4bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "object", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesTrendmicro]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesTrendmicro], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesTrendmicro],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3277706d3fbb4d6e41a371993a37ef206c2a1d3d43e0d8a14c82821f35ffcf08)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesVeeva",
    jsii_struct_bases=[],
    name_mapping={
        "object": "object",
        "document_type": "documentType",
        "include_all_versions": "includeAllVersions",
        "include_renditions": "includeRenditions",
        "include_source_files": "includeSourceFiles",
    },
)
class AppflowFlowSourceFlowConfigSourceConnectorPropertiesVeeva:
    def __init__(
        self,
        *,
        object: builtins.str,
        document_type: typing.Optional[builtins.str] = None,
        include_all_versions: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        include_renditions: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        include_source_files: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        :param document_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#document_type AppflowFlow#document_type}.
        :param include_all_versions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#include_all_versions AppflowFlow#include_all_versions}.
        :param include_renditions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#include_renditions AppflowFlow#include_renditions}.
        :param include_source_files: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#include_source_files AppflowFlow#include_source_files}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78b189d8c7241ee62e7393086633761d4d54d57a234d9e1409bcc0fdba75c460)
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
            check_type(argname="argument document_type", value=document_type, expected_type=type_hints["document_type"])
            check_type(argname="argument include_all_versions", value=include_all_versions, expected_type=type_hints["include_all_versions"])
            check_type(argname="argument include_renditions", value=include_renditions, expected_type=type_hints["include_renditions"])
            check_type(argname="argument include_source_files", value=include_source_files, expected_type=type_hints["include_source_files"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "object": object,
        }
        if document_type is not None:
            self._values["document_type"] = document_type
        if include_all_versions is not None:
            self._values["include_all_versions"] = include_all_versions
        if include_renditions is not None:
            self._values["include_renditions"] = include_renditions
        if include_source_files is not None:
            self._values["include_source_files"] = include_source_files

    @builtins.property
    def object(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.'''
        result = self._values.get("object")
        assert result is not None, "Required property 'object' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def document_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#document_type AppflowFlow#document_type}.'''
        result = self._values.get("document_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def include_all_versions(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#include_all_versions AppflowFlow#include_all_versions}.'''
        result = self._values.get("include_all_versions")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def include_renditions(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#include_renditions AppflowFlow#include_renditions}.'''
        result = self._values.get("include_renditions")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def include_source_files(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#include_source_files AppflowFlow#include_source_files}.'''
        result = self._values.get("include_source_files")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowSourceFlowConfigSourceConnectorPropertiesVeeva(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowSourceFlowConfigSourceConnectorPropertiesVeevaOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesVeevaOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__33255bf2b53ce588ddaa8d3bdc7fc85d46d4d0dbd7ad374ca499de44b32f240a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDocumentType")
    def reset_document_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDocumentType", []))

    @jsii.member(jsii_name="resetIncludeAllVersions")
    def reset_include_all_versions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeAllVersions", []))

    @jsii.member(jsii_name="resetIncludeRenditions")
    def reset_include_renditions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeRenditions", []))

    @jsii.member(jsii_name="resetIncludeSourceFiles")
    def reset_include_source_files(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeSourceFiles", []))

    @builtins.property
    @jsii.member(jsii_name="documentTypeInput")
    def document_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "documentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="includeAllVersionsInput")
    def include_all_versions_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "includeAllVersionsInput"))

    @builtins.property
    @jsii.member(jsii_name="includeRenditionsInput")
    def include_renditions_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "includeRenditionsInput"))

    @builtins.property
    @jsii.member(jsii_name="includeSourceFilesInput")
    def include_source_files_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "includeSourceFilesInput"))

    @builtins.property
    @jsii.member(jsii_name="objectInput")
    def object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="documentType")
    def document_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "documentType"))

    @document_type.setter
    def document_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b2a8e8dd2df39f2966f4270f2b4878b102e99cb7e5f0d544561b55c99662611)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "documentType", value)

    @builtins.property
    @jsii.member(jsii_name="includeAllVersions")
    def include_all_versions(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "includeAllVersions"))

    @include_all_versions.setter
    def include_all_versions(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6745eee579e525d117f0c1fae256cb447826fafe86030ec6c957300b53b04ebd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeAllVersions", value)

    @builtins.property
    @jsii.member(jsii_name="includeRenditions")
    def include_renditions(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "includeRenditions"))

    @include_renditions.setter
    def include_renditions(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71632c65ec8847d6ce3710b1245a4a038c0a6190558efd82ec0ab31acc516976)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeRenditions", value)

    @builtins.property
    @jsii.member(jsii_name="includeSourceFiles")
    def include_source_files(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "includeSourceFiles"))

    @include_source_files.setter
    def include_source_files(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1eb03d24ccdcdaddf4f0ba07564d0eb5a550314611a31a8a5fa4fadd6aebaff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeSourceFiles", value)

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "object"))

    @object.setter
    def object(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d4ced147932821483886c0bfc497b7a103939b7a77fa9b73ceef58977b9acd8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "object", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesVeeva]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesVeeva], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesVeeva],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06fa52a1fdca7baaa8a6cfca42a9c7259a5fc85a4911b534868de290f396c66a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesZendesk",
    jsii_struct_bases=[],
    name_mapping={"object": "object"},
)
class AppflowFlowSourceFlowConfigSourceConnectorPropertiesZendesk:
    def __init__(self, *, object: builtins.str) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb6068701dfec92112200922d8061b39786b65872b756830e7912f5178f67e2b)
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "object": object,
        }

    @builtins.property
    def object(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.'''
        result = self._values.get("object")
        assert result is not None, "Required property 'object' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowSourceFlowConfigSourceConnectorPropertiesZendesk(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowSourceFlowConfigSourceConnectorPropertiesZendeskOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesZendeskOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cbc6be6ba66b80b1d4e1a94e7d98e1833e4f4c23060ecb6c579606aff715d33c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="objectInput")
    def object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "object"))

    @object.setter
    def object(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d24e6f69d907ab5b9a330bf906d9a0de60ff7d88a57c57dba6268585b5e38ab6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "object", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesZendesk]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesZendesk], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesZendesk],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51abf2295c943effbb4034b6cf20c9ff193bf578d65806e34440d90afd64d8ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowTask",
    jsii_struct_bases=[],
    name_mapping={
        "source_fields": "sourceFields",
        "task_type": "taskType",
        "connector_operator": "connectorOperator",
        "destination_field": "destinationField",
        "task_properties": "taskProperties",
    },
)
class AppflowFlowTask:
    def __init__(
        self,
        *,
        source_fields: typing.Sequence[builtins.str],
        task_type: builtins.str,
        connector_operator: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AppflowFlowTaskConnectorOperator", typing.Dict[builtins.str, typing.Any]]]]] = None,
        destination_field: typing.Optional[builtins.str] = None,
        task_properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param source_fields: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#source_fields AppflowFlow#source_fields}.
        :param task_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#task_type AppflowFlow#task_type}.
        :param connector_operator: connector_operator block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#connector_operator AppflowFlow#connector_operator}
        :param destination_field: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#destination_field AppflowFlow#destination_field}.
        :param task_properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#task_properties AppflowFlow#task_properties}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5099b4a163451ab76e8e852a03f9625dd10c16a679891a8290eeb8a761d11a4d)
            check_type(argname="argument source_fields", value=source_fields, expected_type=type_hints["source_fields"])
            check_type(argname="argument task_type", value=task_type, expected_type=type_hints["task_type"])
            check_type(argname="argument connector_operator", value=connector_operator, expected_type=type_hints["connector_operator"])
            check_type(argname="argument destination_field", value=destination_field, expected_type=type_hints["destination_field"])
            check_type(argname="argument task_properties", value=task_properties, expected_type=type_hints["task_properties"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "source_fields": source_fields,
            "task_type": task_type,
        }
        if connector_operator is not None:
            self._values["connector_operator"] = connector_operator
        if destination_field is not None:
            self._values["destination_field"] = destination_field
        if task_properties is not None:
            self._values["task_properties"] = task_properties

    @builtins.property
    def source_fields(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#source_fields AppflowFlow#source_fields}.'''
        result = self._values.get("source_fields")
        assert result is not None, "Required property 'source_fields' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def task_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#task_type AppflowFlow#task_type}.'''
        result = self._values.get("task_type")
        assert result is not None, "Required property 'task_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def connector_operator(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppflowFlowTaskConnectorOperator"]]]:
        '''connector_operator block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#connector_operator AppflowFlow#connector_operator}
        '''
        result = self._values.get("connector_operator")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppflowFlowTaskConnectorOperator"]]], result)

    @builtins.property
    def destination_field(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#destination_field AppflowFlow#destination_field}.'''
        result = self._values.get("destination_field")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def task_properties(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#task_properties AppflowFlow#task_properties}.'''
        result = self._values.get("task_properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowTask(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowTaskConnectorOperator",
    jsii_struct_bases=[],
    name_mapping={
        "amplitude": "amplitude",
        "custom_connector": "customConnector",
        "datadog": "datadog",
        "dynatrace": "dynatrace",
        "google_analytics": "googleAnalytics",
        "infor_nexus": "inforNexus",
        "marketo": "marketo",
        "s3": "s3",
        "salesforce": "salesforce",
        "sapo_data": "sapoData",
        "service_now": "serviceNow",
        "singular": "singular",
        "slack": "slack",
        "trendmicro": "trendmicro",
        "veeva": "veeva",
        "zendesk": "zendesk",
    },
)
class AppflowFlowTaskConnectorOperator:
    def __init__(
        self,
        *,
        amplitude: typing.Optional[builtins.str] = None,
        custom_connector: typing.Optional[builtins.str] = None,
        datadog: typing.Optional[builtins.str] = None,
        dynatrace: typing.Optional[builtins.str] = None,
        google_analytics: typing.Optional[builtins.str] = None,
        infor_nexus: typing.Optional[builtins.str] = None,
        marketo: typing.Optional[builtins.str] = None,
        s3: typing.Optional[builtins.str] = None,
        salesforce: typing.Optional[builtins.str] = None,
        sapo_data: typing.Optional[builtins.str] = None,
        service_now: typing.Optional[builtins.str] = None,
        singular: typing.Optional[builtins.str] = None,
        slack: typing.Optional[builtins.str] = None,
        trendmicro: typing.Optional[builtins.str] = None,
        veeva: typing.Optional[builtins.str] = None,
        zendesk: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param amplitude: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#amplitude AppflowFlow#amplitude}.
        :param custom_connector: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#custom_connector AppflowFlow#custom_connector}.
        :param datadog: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#datadog AppflowFlow#datadog}.
        :param dynatrace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#dynatrace AppflowFlow#dynatrace}.
        :param google_analytics: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#google_analytics AppflowFlow#google_analytics}.
        :param infor_nexus: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#infor_nexus AppflowFlow#infor_nexus}.
        :param marketo: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#marketo AppflowFlow#marketo}.
        :param s3: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#s3 AppflowFlow#s3}.
        :param salesforce: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#salesforce AppflowFlow#salesforce}.
        :param sapo_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#sapo_data AppflowFlow#sapo_data}.
        :param service_now: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#service_now AppflowFlow#service_now}.
        :param singular: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#singular AppflowFlow#singular}.
        :param slack: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#slack AppflowFlow#slack}.
        :param trendmicro: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#trendmicro AppflowFlow#trendmicro}.
        :param veeva: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#veeva AppflowFlow#veeva}.
        :param zendesk: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#zendesk AppflowFlow#zendesk}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36369d725074a475edd65ec430781139e47ad30fd654d676aea04db26bc44164)
            check_type(argname="argument amplitude", value=amplitude, expected_type=type_hints["amplitude"])
            check_type(argname="argument custom_connector", value=custom_connector, expected_type=type_hints["custom_connector"])
            check_type(argname="argument datadog", value=datadog, expected_type=type_hints["datadog"])
            check_type(argname="argument dynatrace", value=dynatrace, expected_type=type_hints["dynatrace"])
            check_type(argname="argument google_analytics", value=google_analytics, expected_type=type_hints["google_analytics"])
            check_type(argname="argument infor_nexus", value=infor_nexus, expected_type=type_hints["infor_nexus"])
            check_type(argname="argument marketo", value=marketo, expected_type=type_hints["marketo"])
            check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
            check_type(argname="argument salesforce", value=salesforce, expected_type=type_hints["salesforce"])
            check_type(argname="argument sapo_data", value=sapo_data, expected_type=type_hints["sapo_data"])
            check_type(argname="argument service_now", value=service_now, expected_type=type_hints["service_now"])
            check_type(argname="argument singular", value=singular, expected_type=type_hints["singular"])
            check_type(argname="argument slack", value=slack, expected_type=type_hints["slack"])
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
        if infor_nexus is not None:
            self._values["infor_nexus"] = infor_nexus
        if marketo is not None:
            self._values["marketo"] = marketo
        if s3 is not None:
            self._values["s3"] = s3
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
        if trendmicro is not None:
            self._values["trendmicro"] = trendmicro
        if veeva is not None:
            self._values["veeva"] = veeva
        if zendesk is not None:
            self._values["zendesk"] = zendesk

    @builtins.property
    def amplitude(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#amplitude AppflowFlow#amplitude}.'''
        result = self._values.get("amplitude")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_connector(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#custom_connector AppflowFlow#custom_connector}.'''
        result = self._values.get("custom_connector")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def datadog(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#datadog AppflowFlow#datadog}.'''
        result = self._values.get("datadog")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dynatrace(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#dynatrace AppflowFlow#dynatrace}.'''
        result = self._values.get("dynatrace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def google_analytics(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#google_analytics AppflowFlow#google_analytics}.'''
        result = self._values.get("google_analytics")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def infor_nexus(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#infor_nexus AppflowFlow#infor_nexus}.'''
        result = self._values.get("infor_nexus")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def marketo(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#marketo AppflowFlow#marketo}.'''
        result = self._values.get("marketo")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#s3 AppflowFlow#s3}.'''
        result = self._values.get("s3")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def salesforce(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#salesforce AppflowFlow#salesforce}.'''
        result = self._values.get("salesforce")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sapo_data(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#sapo_data AppflowFlow#sapo_data}.'''
        result = self._values.get("sapo_data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_now(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#service_now AppflowFlow#service_now}.'''
        result = self._values.get("service_now")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def singular(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#singular AppflowFlow#singular}.'''
        result = self._values.get("singular")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def slack(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#slack AppflowFlow#slack}.'''
        result = self._values.get("slack")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def trendmicro(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#trendmicro AppflowFlow#trendmicro}.'''
        result = self._values.get("trendmicro")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def veeva(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#veeva AppflowFlow#veeva}.'''
        result = self._values.get("veeva")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def zendesk(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#zendesk AppflowFlow#zendesk}.'''
        result = self._values.get("zendesk")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowTaskConnectorOperator(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowTaskConnectorOperatorList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowTaskConnectorOperatorList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__07830e0a565c359260c0e954f87f3aa2bc6e0722ae525769d63202d707d834c0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "AppflowFlowTaskConnectorOperatorOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5dfd155462b35dba3354710790fad0c022357f103eda91821ea33ee84c9bda71)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppflowFlowTaskConnectorOperatorOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85cbc7aa555f6c388c9f274c59c534d7b485fd97a26172cff5cf25373c478f3b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__272d4b5446f72f2487992c13db1b909551f33e5acd5cfcade5f1f06381f94843)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b35c550114293d3e68bd87db74ece6edd7a5af1a68b0437636783d37da5dfcd7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppflowFlowTaskConnectorOperator]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppflowFlowTaskConnectorOperator]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppflowFlowTaskConnectorOperator]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e195e7d61ca22de49f5f48e10e1fe868241d59936d922527aad39b4ab5ffe21b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowFlowTaskConnectorOperatorOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowTaskConnectorOperatorOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d5d05e0f42ffd8808a4623818e1e34e380ccfa550e9f835e2639b63cb75b194a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

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

    @jsii.member(jsii_name="resetInforNexus")
    def reset_infor_nexus(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInforNexus", []))

    @jsii.member(jsii_name="resetMarketo")
    def reset_marketo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMarketo", []))

    @jsii.member(jsii_name="resetS3")
    def reset_s3(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3", []))

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
    @jsii.member(jsii_name="amplitudeInput")
    def amplitude_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "amplitudeInput"))

    @builtins.property
    @jsii.member(jsii_name="customConnectorInput")
    def custom_connector_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customConnectorInput"))

    @builtins.property
    @jsii.member(jsii_name="datadogInput")
    def datadog_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datadogInput"))

    @builtins.property
    @jsii.member(jsii_name="dynatraceInput")
    def dynatrace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dynatraceInput"))

    @builtins.property
    @jsii.member(jsii_name="googleAnalyticsInput")
    def google_analytics_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "googleAnalyticsInput"))

    @builtins.property
    @jsii.member(jsii_name="inforNexusInput")
    def infor_nexus_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "inforNexusInput"))

    @builtins.property
    @jsii.member(jsii_name="marketoInput")
    def marketo_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "marketoInput"))

    @builtins.property
    @jsii.member(jsii_name="s3Input")
    def s3_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3Input"))

    @builtins.property
    @jsii.member(jsii_name="salesforceInput")
    def salesforce_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "salesforceInput"))

    @builtins.property
    @jsii.member(jsii_name="sapoDataInput")
    def sapo_data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sapoDataInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceNowInput")
    def service_now_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceNowInput"))

    @builtins.property
    @jsii.member(jsii_name="singularInput")
    def singular_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "singularInput"))

    @builtins.property
    @jsii.member(jsii_name="slackInput")
    def slack_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "slackInput"))

    @builtins.property
    @jsii.member(jsii_name="trendmicroInput")
    def trendmicro_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "trendmicroInput"))

    @builtins.property
    @jsii.member(jsii_name="veevaInput")
    def veeva_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "veevaInput"))

    @builtins.property
    @jsii.member(jsii_name="zendeskInput")
    def zendesk_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zendeskInput"))

    @builtins.property
    @jsii.member(jsii_name="amplitude")
    def amplitude(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "amplitude"))

    @amplitude.setter
    def amplitude(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9647d58a393c47fd4aa1fbbd7c809d13e6e5a4630e1d489378276d889997af4c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "amplitude", value)

    @builtins.property
    @jsii.member(jsii_name="customConnector")
    def custom_connector(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customConnector"))

    @custom_connector.setter
    def custom_connector(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6e416ab4ba4549c2ed8eb9bfe12402434deb92c71128db770249d8bb46b09ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customConnector", value)

    @builtins.property
    @jsii.member(jsii_name="datadog")
    def datadog(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datadog"))

    @datadog.setter
    def datadog(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4f8433b57f8747ef450b667cb380a6eca734aea295db09a3e7cc430f87136d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datadog", value)

    @builtins.property
    @jsii.member(jsii_name="dynatrace")
    def dynatrace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dynatrace"))

    @dynatrace.setter
    def dynatrace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2723736b99dfde9047505f84e90fbd244f7c22f000a91c5cdfb190dda022d341)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dynatrace", value)

    @builtins.property
    @jsii.member(jsii_name="googleAnalytics")
    def google_analytics(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "googleAnalytics"))

    @google_analytics.setter
    def google_analytics(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4aacb639d2a4b010162da36845631ba063787267ecb700a9f61ca7f053f99ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "googleAnalytics", value)

    @builtins.property
    @jsii.member(jsii_name="inforNexus")
    def infor_nexus(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "inforNexus"))

    @infor_nexus.setter
    def infor_nexus(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4593ed3e169723f1257d215d590daa781e7caface5adb24f312dd73d79381ffa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inforNexus", value)

    @builtins.property
    @jsii.member(jsii_name="marketo")
    def marketo(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "marketo"))

    @marketo.setter
    def marketo(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d33c9d6e0d012ade707bcd0f7662a31decf3280d87688a74530ad0ce6f49f2b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "marketo", value)

    @builtins.property
    @jsii.member(jsii_name="s3")
    def s3(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3"))

    @s3.setter
    def s3(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3e4040fd8b3d8b06635871c2388145c0cc25690346d9997ebc9cc9a9cf635fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3", value)

    @builtins.property
    @jsii.member(jsii_name="salesforce")
    def salesforce(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "salesforce"))

    @salesforce.setter
    def salesforce(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__191931824a47dfa914de78f0af5a0eb2451cd4bf918863ac861a1c547e3313bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "salesforce", value)

    @builtins.property
    @jsii.member(jsii_name="sapoData")
    def sapo_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sapoData"))

    @sapo_data.setter
    def sapo_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__950d10ce95710d4018c1b2aca48df5cfe0ad6662b74d030df231306a3d07a707)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sapoData", value)

    @builtins.property
    @jsii.member(jsii_name="serviceNow")
    def service_now(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceNow"))

    @service_now.setter
    def service_now(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05acd92461f65cb2c3b558397e6e64f3c9617ae227b6f468a9f93c5501a89894)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceNow", value)

    @builtins.property
    @jsii.member(jsii_name="singular")
    def singular(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "singular"))

    @singular.setter
    def singular(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5265d4e1163a1d5533bfcbe9850107696e060df0d9b7e1baf6f1083e98fc7e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "singular", value)

    @builtins.property
    @jsii.member(jsii_name="slack")
    def slack(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "slack"))

    @slack.setter
    def slack(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f04d3121ebfc3f5c45217ab4cb73d93266a61336be86a3f0de230aee15167b4f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "slack", value)

    @builtins.property
    @jsii.member(jsii_name="trendmicro")
    def trendmicro(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "trendmicro"))

    @trendmicro.setter
    def trendmicro(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__568549a5dc559c9391f5afcfe95345dcbbcf82cbb3392afc7233596ad65691d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trendmicro", value)

    @builtins.property
    @jsii.member(jsii_name="veeva")
    def veeva(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "veeva"))

    @veeva.setter
    def veeva(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9e15c5d109cb3372222549ee0a5b16fa21a96d7ba3df5ff7217239a044bbbd5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "veeva", value)

    @builtins.property
    @jsii.member(jsii_name="zendesk")
    def zendesk(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zendesk"))

    @zendesk.setter
    def zendesk(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e7af7b95071c9af441c71a7678cd8cf8e08ad6a0719dd03cd6d23d3cfcfe301)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zendesk", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppflowFlowTaskConnectorOperator, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppflowFlowTaskConnectorOperator, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppflowFlowTaskConnectorOperator, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c4f72343ac75ee5c1b1cb0c4c859bb3f5016679ebcc4775bdfcdd657f1a4db1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowFlowTaskList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowTaskList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e949c3c116fa403728e03d91a92b5bbc30ee3a030b0f036e7e8ac21283eae902)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AppflowFlowTaskOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50925ba1abe1f51aab0246ee8f124cd7f5127caebf56455dcf4d8c4905b060ad)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppflowFlowTaskOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae227f93bb5feb6e0489d56923940484d0f8957918721b6078e43bb32fb7c09a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__719153cc3d12db1ced04ac6e461174da62dcbad28d2959e15aac0bcb3185f3b6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f20ddbf934d31acd2c4924fa603a761b98b00efeecca4e927dd5902d18e6c4c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppflowFlowTask]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppflowFlowTask]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppflowFlowTask]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d4e280035920de824d0e7712931cf4e0873bfdccc441fbcee46bc42045dafd7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowFlowTaskOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowTaskOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ae84f9bb4025a97b07a08eea18fc981f76ec3506efd7cae12da7c1cbf058ad81)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putConnectorOperator")
    def put_connector_operator(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppflowFlowTaskConnectorOperator, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18fb3bcc636806069a5e3f7a0a21edd2df58c76426f42cde862680b409c72f5b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putConnectorOperator", [value]))

    @jsii.member(jsii_name="resetConnectorOperator")
    def reset_connector_operator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectorOperator", []))

    @jsii.member(jsii_name="resetDestinationField")
    def reset_destination_field(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationField", []))

    @jsii.member(jsii_name="resetTaskProperties")
    def reset_task_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTaskProperties", []))

    @builtins.property
    @jsii.member(jsii_name="connectorOperator")
    def connector_operator(self) -> AppflowFlowTaskConnectorOperatorList:
        return typing.cast(AppflowFlowTaskConnectorOperatorList, jsii.get(self, "connectorOperator"))

    @builtins.property
    @jsii.member(jsii_name="connectorOperatorInput")
    def connector_operator_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppflowFlowTaskConnectorOperator]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppflowFlowTaskConnectorOperator]]], jsii.get(self, "connectorOperatorInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationFieldInput")
    def destination_field_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationFieldInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceFieldsInput")
    def source_fields_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourceFieldsInput"))

    @builtins.property
    @jsii.member(jsii_name="taskPropertiesInput")
    def task_properties_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "taskPropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="taskTypeInput")
    def task_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "taskTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationField")
    def destination_field(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destinationField"))

    @destination_field.setter
    def destination_field(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b2acf205a984a438104852138bfeee89a9aaf4999ddd073eafe9dca7bcd6699)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationField", value)

    @builtins.property
    @jsii.member(jsii_name="sourceFields")
    def source_fields(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sourceFields"))

    @source_fields.setter
    def source_fields(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29d04fca2dcf13717625920f1836a864d8164f3777cc5590facef254608c8686)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceFields", value)

    @builtins.property
    @jsii.member(jsii_name="taskProperties")
    def task_properties(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "taskProperties"))

    @task_properties.setter
    def task_properties(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8e15f1151823ed8cb2414619dbf0e155718c2ae919d738b2d2736718dca5e09)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskProperties", value)

    @builtins.property
    @jsii.member(jsii_name="taskType")
    def task_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "taskType"))

    @task_type.setter
    def task_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66f0fe4e05b2c9f8f095e596d83782fb89790be0707327c385d25067d23c07a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppflowFlowTask, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppflowFlowTask, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppflowFlowTask, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0a58d43def83ec463c227eba7459967309f7aed3abada664bc326b02bbc59f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowTriggerConfig",
    jsii_struct_bases=[],
    name_mapping={
        "trigger_type": "triggerType",
        "trigger_properties": "triggerProperties",
    },
)
class AppflowFlowTriggerConfig:
    def __init__(
        self,
        *,
        trigger_type: builtins.str,
        trigger_properties: typing.Optional[typing.Union["AppflowFlowTriggerConfigTriggerProperties", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param trigger_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#trigger_type AppflowFlow#trigger_type}.
        :param trigger_properties: trigger_properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#trigger_properties AppflowFlow#trigger_properties}
        '''
        if isinstance(trigger_properties, dict):
            trigger_properties = AppflowFlowTriggerConfigTriggerProperties(**trigger_properties)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05235a507833fe56416ab2f2bba05df51f42832e8dc253f523f36f326d0c8733)
            check_type(argname="argument trigger_type", value=trigger_type, expected_type=type_hints["trigger_type"])
            check_type(argname="argument trigger_properties", value=trigger_properties, expected_type=type_hints["trigger_properties"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "trigger_type": trigger_type,
        }
        if trigger_properties is not None:
            self._values["trigger_properties"] = trigger_properties

    @builtins.property
    def trigger_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#trigger_type AppflowFlow#trigger_type}.'''
        result = self._values.get("trigger_type")
        assert result is not None, "Required property 'trigger_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def trigger_properties(
        self,
    ) -> typing.Optional["AppflowFlowTriggerConfigTriggerProperties"]:
        '''trigger_properties block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#trigger_properties AppflowFlow#trigger_properties}
        '''
        result = self._values.get("trigger_properties")
        return typing.cast(typing.Optional["AppflowFlowTriggerConfigTriggerProperties"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowTriggerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowTriggerConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowTriggerConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__10bb8cc3a6f6e5c3374561c4490ccba2c3ce80e932c0d31debc3870658c73589)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putTriggerProperties")
    def put_trigger_properties(
        self,
        *,
        scheduled: typing.Optional[typing.Union["AppflowFlowTriggerConfigTriggerPropertiesScheduled", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scheduled: scheduled block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#scheduled AppflowFlow#scheduled}
        '''
        value = AppflowFlowTriggerConfigTriggerProperties(scheduled=scheduled)

        return typing.cast(None, jsii.invoke(self, "putTriggerProperties", [value]))

    @jsii.member(jsii_name="resetTriggerProperties")
    def reset_trigger_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTriggerProperties", []))

    @builtins.property
    @jsii.member(jsii_name="triggerProperties")
    def trigger_properties(
        self,
    ) -> "AppflowFlowTriggerConfigTriggerPropertiesOutputReference":
        return typing.cast("AppflowFlowTriggerConfigTriggerPropertiesOutputReference", jsii.get(self, "triggerProperties"))

    @builtins.property
    @jsii.member(jsii_name="triggerPropertiesInput")
    def trigger_properties_input(
        self,
    ) -> typing.Optional["AppflowFlowTriggerConfigTriggerProperties"]:
        return typing.cast(typing.Optional["AppflowFlowTriggerConfigTriggerProperties"], jsii.get(self, "triggerPropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="triggerTypeInput")
    def trigger_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "triggerTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="triggerType")
    def trigger_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "triggerType"))

    @trigger_type.setter
    def trigger_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5bba6f8a44c411ed3b05b32475b5d880a5ea9e9862102f2367663e4a8baaac5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "triggerType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppflowFlowTriggerConfig]:
        return typing.cast(typing.Optional[AppflowFlowTriggerConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[AppflowFlowTriggerConfig]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__332d041ee75b6720b6b368788c7538105875284dd8c3d726708e6acbf53c2cdf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowTriggerConfigTriggerProperties",
    jsii_struct_bases=[],
    name_mapping={"scheduled": "scheduled"},
)
class AppflowFlowTriggerConfigTriggerProperties:
    def __init__(
        self,
        *,
        scheduled: typing.Optional[typing.Union["AppflowFlowTriggerConfigTriggerPropertiesScheduled", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scheduled: scheduled block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#scheduled AppflowFlow#scheduled}
        '''
        if isinstance(scheduled, dict):
            scheduled = AppflowFlowTriggerConfigTriggerPropertiesScheduled(**scheduled)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2931592b76a95a7f7d3379f17c773473758f1680b874ad8c28945956ad0da8b)
            check_type(argname="argument scheduled", value=scheduled, expected_type=type_hints["scheduled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if scheduled is not None:
            self._values["scheduled"] = scheduled

    @builtins.property
    def scheduled(
        self,
    ) -> typing.Optional["AppflowFlowTriggerConfigTriggerPropertiesScheduled"]:
        '''scheduled block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#scheduled AppflowFlow#scheduled}
        '''
        result = self._values.get("scheduled")
        return typing.cast(typing.Optional["AppflowFlowTriggerConfigTriggerPropertiesScheduled"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowTriggerConfigTriggerProperties(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowTriggerConfigTriggerPropertiesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowTriggerConfigTriggerPropertiesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5d8d8173626e40278c03bb1df457c6d044e8b910420ecb903830e3c17fd5a5e3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putScheduled")
    def put_scheduled(
        self,
        *,
        schedule_expression: builtins.str,
        data_pull_mode: typing.Optional[builtins.str] = None,
        first_execution_from: typing.Optional[builtins.str] = None,
        schedule_end_time: typing.Optional[builtins.str] = None,
        schedule_offset: typing.Optional[jsii.Number] = None,
        schedule_start_time: typing.Optional[builtins.str] = None,
        timezone: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param schedule_expression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#schedule_expression AppflowFlow#schedule_expression}.
        :param data_pull_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#data_pull_mode AppflowFlow#data_pull_mode}.
        :param first_execution_from: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#first_execution_from AppflowFlow#first_execution_from}.
        :param schedule_end_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#schedule_end_time AppflowFlow#schedule_end_time}.
        :param schedule_offset: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#schedule_offset AppflowFlow#schedule_offset}.
        :param schedule_start_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#schedule_start_time AppflowFlow#schedule_start_time}.
        :param timezone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#timezone AppflowFlow#timezone}.
        '''
        value = AppflowFlowTriggerConfigTriggerPropertiesScheduled(
            schedule_expression=schedule_expression,
            data_pull_mode=data_pull_mode,
            first_execution_from=first_execution_from,
            schedule_end_time=schedule_end_time,
            schedule_offset=schedule_offset,
            schedule_start_time=schedule_start_time,
            timezone=timezone,
        )

        return typing.cast(None, jsii.invoke(self, "putScheduled", [value]))

    @jsii.member(jsii_name="resetScheduled")
    def reset_scheduled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScheduled", []))

    @builtins.property
    @jsii.member(jsii_name="scheduled")
    def scheduled(
        self,
    ) -> "AppflowFlowTriggerConfigTriggerPropertiesScheduledOutputReference":
        return typing.cast("AppflowFlowTriggerConfigTriggerPropertiesScheduledOutputReference", jsii.get(self, "scheduled"))

    @builtins.property
    @jsii.member(jsii_name="scheduledInput")
    def scheduled_input(
        self,
    ) -> typing.Optional["AppflowFlowTriggerConfigTriggerPropertiesScheduled"]:
        return typing.cast(typing.Optional["AppflowFlowTriggerConfigTriggerPropertiesScheduled"], jsii.get(self, "scheduledInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowTriggerConfigTriggerProperties]:
        return typing.cast(typing.Optional[AppflowFlowTriggerConfigTriggerProperties], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowTriggerConfigTriggerProperties],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d51a09123497ae064dd2b27fe7ab82c52761c3cb7419cddb3be2b07abbe7f9ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appflowFlow.AppflowFlowTriggerConfigTriggerPropertiesScheduled",
    jsii_struct_bases=[],
    name_mapping={
        "schedule_expression": "scheduleExpression",
        "data_pull_mode": "dataPullMode",
        "first_execution_from": "firstExecutionFrom",
        "schedule_end_time": "scheduleEndTime",
        "schedule_offset": "scheduleOffset",
        "schedule_start_time": "scheduleStartTime",
        "timezone": "timezone",
    },
)
class AppflowFlowTriggerConfigTriggerPropertiesScheduled:
    def __init__(
        self,
        *,
        schedule_expression: builtins.str,
        data_pull_mode: typing.Optional[builtins.str] = None,
        first_execution_from: typing.Optional[builtins.str] = None,
        schedule_end_time: typing.Optional[builtins.str] = None,
        schedule_offset: typing.Optional[jsii.Number] = None,
        schedule_start_time: typing.Optional[builtins.str] = None,
        timezone: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param schedule_expression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#schedule_expression AppflowFlow#schedule_expression}.
        :param data_pull_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#data_pull_mode AppflowFlow#data_pull_mode}.
        :param first_execution_from: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#first_execution_from AppflowFlow#first_execution_from}.
        :param schedule_end_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#schedule_end_time AppflowFlow#schedule_end_time}.
        :param schedule_offset: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#schedule_offset AppflowFlow#schedule_offset}.
        :param schedule_start_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#schedule_start_time AppflowFlow#schedule_start_time}.
        :param timezone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#timezone AppflowFlow#timezone}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ef425d98e9fb19a22879f3c79aa1f179f26bf2ba9f8d4849dc7d19161ab2a33)
            check_type(argname="argument schedule_expression", value=schedule_expression, expected_type=type_hints["schedule_expression"])
            check_type(argname="argument data_pull_mode", value=data_pull_mode, expected_type=type_hints["data_pull_mode"])
            check_type(argname="argument first_execution_from", value=first_execution_from, expected_type=type_hints["first_execution_from"])
            check_type(argname="argument schedule_end_time", value=schedule_end_time, expected_type=type_hints["schedule_end_time"])
            check_type(argname="argument schedule_offset", value=schedule_offset, expected_type=type_hints["schedule_offset"])
            check_type(argname="argument schedule_start_time", value=schedule_start_time, expected_type=type_hints["schedule_start_time"])
            check_type(argname="argument timezone", value=timezone, expected_type=type_hints["timezone"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "schedule_expression": schedule_expression,
        }
        if data_pull_mode is not None:
            self._values["data_pull_mode"] = data_pull_mode
        if first_execution_from is not None:
            self._values["first_execution_from"] = first_execution_from
        if schedule_end_time is not None:
            self._values["schedule_end_time"] = schedule_end_time
        if schedule_offset is not None:
            self._values["schedule_offset"] = schedule_offset
        if schedule_start_time is not None:
            self._values["schedule_start_time"] = schedule_start_time
        if timezone is not None:
            self._values["timezone"] = timezone

    @builtins.property
    def schedule_expression(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#schedule_expression AppflowFlow#schedule_expression}.'''
        result = self._values.get("schedule_expression")
        assert result is not None, "Required property 'schedule_expression' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_pull_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#data_pull_mode AppflowFlow#data_pull_mode}.'''
        result = self._values.get("data_pull_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def first_execution_from(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#first_execution_from AppflowFlow#first_execution_from}.'''
        result = self._values.get("first_execution_from")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schedule_end_time(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#schedule_end_time AppflowFlow#schedule_end_time}.'''
        result = self._values.get("schedule_end_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schedule_offset(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#schedule_offset AppflowFlow#schedule_offset}.'''
        result = self._values.get("schedule_offset")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def schedule_start_time(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#schedule_start_time AppflowFlow#schedule_start_time}.'''
        result = self._values.get("schedule_start_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timezone(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#timezone AppflowFlow#timezone}.'''
        result = self._values.get("timezone")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowTriggerConfigTriggerPropertiesScheduled(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowTriggerConfigTriggerPropertiesScheduledOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appflowFlow.AppflowFlowTriggerConfigTriggerPropertiesScheduledOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d30dfd007b84d23d3c2f093b09592ad4e491ab8cb60704fe79f67700d133071a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDataPullMode")
    def reset_data_pull_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataPullMode", []))

    @jsii.member(jsii_name="resetFirstExecutionFrom")
    def reset_first_execution_from(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFirstExecutionFrom", []))

    @jsii.member(jsii_name="resetScheduleEndTime")
    def reset_schedule_end_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScheduleEndTime", []))

    @jsii.member(jsii_name="resetScheduleOffset")
    def reset_schedule_offset(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScheduleOffset", []))

    @jsii.member(jsii_name="resetScheduleStartTime")
    def reset_schedule_start_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScheduleStartTime", []))

    @jsii.member(jsii_name="resetTimezone")
    def reset_timezone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimezone", []))

    @builtins.property
    @jsii.member(jsii_name="dataPullModeInput")
    def data_pull_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataPullModeInput"))

    @builtins.property
    @jsii.member(jsii_name="firstExecutionFromInput")
    def first_execution_from_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "firstExecutionFromInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduleEndTimeInput")
    def schedule_end_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scheduleEndTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduleExpressionInput")
    def schedule_expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scheduleExpressionInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduleOffsetInput")
    def schedule_offset_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "scheduleOffsetInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduleStartTimeInput")
    def schedule_start_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scheduleStartTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="timezoneInput")
    def timezone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timezoneInput"))

    @builtins.property
    @jsii.member(jsii_name="dataPullMode")
    def data_pull_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataPullMode"))

    @data_pull_mode.setter
    def data_pull_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88c25b19b3deaf77966de2c0dfd3bf556d878aed9e29b9a1a36a87f0fa1e2993)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataPullMode", value)

    @builtins.property
    @jsii.member(jsii_name="firstExecutionFrom")
    def first_execution_from(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "firstExecutionFrom"))

    @first_execution_from.setter
    def first_execution_from(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da3c532891d1a8a5804e0f0376921b29fcaa9bad61d75e8d2b6d23714592a60d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firstExecutionFrom", value)

    @builtins.property
    @jsii.member(jsii_name="scheduleEndTime")
    def schedule_end_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scheduleEndTime"))

    @schedule_end_time.setter
    def schedule_end_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fc72389a2d2f60423158ccb45aa8dcda3b4639bc8b3ab6739e631a438084a9d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheduleEndTime", value)

    @builtins.property
    @jsii.member(jsii_name="scheduleExpression")
    def schedule_expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scheduleExpression"))

    @schedule_expression.setter
    def schedule_expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__006489b3c9763da4dcca2d89918cf2e3b1fb053e3ee11b98bd6d016f4a031f86)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheduleExpression", value)

    @builtins.property
    @jsii.member(jsii_name="scheduleOffset")
    def schedule_offset(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "scheduleOffset"))

    @schedule_offset.setter
    def schedule_offset(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c04f55d7c88a7cf404d21bee148b7f574cc3fc7c9264e8d9d025965bdfcf618e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheduleOffset", value)

    @builtins.property
    @jsii.member(jsii_name="scheduleStartTime")
    def schedule_start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scheduleStartTime"))

    @schedule_start_time.setter
    def schedule_start_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afe5fd897053370de1f21caaa85d8faacdc8f622f8b8fbf53a9c40a4746dad69)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheduleStartTime", value)

    @builtins.property
    @jsii.member(jsii_name="timezone")
    def timezone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timezone"))

    @timezone.setter
    def timezone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be74da71661986dec1e920eee49eafee3682320433cbcc2ba5846fd5947af8e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timezone", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowTriggerConfigTriggerPropertiesScheduled]:
        return typing.cast(typing.Optional[AppflowFlowTriggerConfigTriggerPropertiesScheduled], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowTriggerConfigTriggerPropertiesScheduled],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94e4e1b4ad4d74f4a29813f846f52aca5acb91b559043e6b020cd7971ac162ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "AppflowFlow",
    "AppflowFlowConfig",
    "AppflowFlowDestinationFlowConfig",
    "AppflowFlowDestinationFlowConfigDestinationConnectorProperties",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnector",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfig",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfigOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfiles",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfilesOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridge",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfig",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfigOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycode",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfig",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfigOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetrics",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetricsOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketo",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfig",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfigOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshift",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfig",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfigOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3OutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfig",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfig",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfigOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfig",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfigOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforce",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfig",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfigOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoData",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfig",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfigOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfig",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfigOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflake",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfig",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfigOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolver",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfig",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfig",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfigOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfig",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfigOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendesk",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfig",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfigOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskOutputReference",
    "AppflowFlowDestinationFlowConfigList",
    "AppflowFlowDestinationFlowConfigOutputReference",
    "AppflowFlowSourceFlowConfig",
    "AppflowFlowSourceFlowConfigIncrementalPullConfig",
    "AppflowFlowSourceFlowConfigIncrementalPullConfigOutputReference",
    "AppflowFlowSourceFlowConfigOutputReference",
    "AppflowFlowSourceFlowConfigSourceConnectorProperties",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesAmplitude",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesAmplitudeOutputReference",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesCustomConnector",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesCustomConnectorOutputReference",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesDatadog",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesDatadogOutputReference",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesDynatrace",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesDynatraceOutputReference",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalytics",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalyticsOutputReference",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesInforNexus",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesInforNexusOutputReference",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesMarketo",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesMarketoOutputReference",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesOutputReference",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3OutputReference",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfig",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfigOutputReference",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesSalesforce",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesSalesforceOutputReference",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesSapoData",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesSapoDataOutputReference",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesServiceNow",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesServiceNowOutputReference",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesSingular",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesSingularOutputReference",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesSlack",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesSlackOutputReference",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesTrendmicro",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesTrendmicroOutputReference",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesVeeva",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesVeevaOutputReference",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesZendesk",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesZendeskOutputReference",
    "AppflowFlowTask",
    "AppflowFlowTaskConnectorOperator",
    "AppflowFlowTaskConnectorOperatorList",
    "AppflowFlowTaskConnectorOperatorOutputReference",
    "AppflowFlowTaskList",
    "AppflowFlowTaskOutputReference",
    "AppflowFlowTriggerConfig",
    "AppflowFlowTriggerConfigOutputReference",
    "AppflowFlowTriggerConfigTriggerProperties",
    "AppflowFlowTriggerConfigTriggerPropertiesOutputReference",
    "AppflowFlowTriggerConfigTriggerPropertiesScheduled",
    "AppflowFlowTriggerConfigTriggerPropertiesScheduledOutputReference",
]

publication.publish()

def _typecheckingstub__05a923e7604d13822e0a12c550ed0d1bee650c17dfe0c4f8095e74a82c87a060(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    destination_flow_config: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppflowFlowDestinationFlowConfig, typing.Dict[builtins.str, typing.Any]]]],
    name: builtins.str,
    source_flow_config: typing.Union[AppflowFlowSourceFlowConfig, typing.Dict[builtins.str, typing.Any]],
    task: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppflowFlowTask, typing.Dict[builtins.str, typing.Any]]]],
    trigger_config: typing.Union[AppflowFlowTriggerConfig, typing.Dict[builtins.str, typing.Any]],
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    kms_arn: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__eed448eee19fd6120b079fccd55f64eafb67b0464723f2843b78ab5e18fb7b3b(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppflowFlowDestinationFlowConfig, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1a8d716f42d7616486476f065b0283d9615ea757e4fcbfe78c5f9e07ed19b6b(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppflowFlowTask, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__959255a5a4cbdf34a255cddd2444dfc2b2519b39c9f26239fb2e867bef2e8ff9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc8014ff3b3ef9c53e08a49a049c29511495e015254d6a34946120f1ab0c8abb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0abdb9cf2033198a136fa533e92da4aac2f68cd86c5b4b48dee58dbac28ea83a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3662c5d5a963e44bc47bdc0e8e58c584e410e32c1d3e7de5b60b8d429c0bf6af(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95de1e8f9f2f36fcbf7ea6bed532a897505c6817811338c4ec0f9c9d941f03ae(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abc4cc562fc4a5ef08d6a1e36107d1ba2c35e315d8cff49faa9849eac621df1a(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2254fa09fd787cadb62b3f7b10554beec5c354668649a224dbb438ab0e4b895d(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    destination_flow_config: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppflowFlowDestinationFlowConfig, typing.Dict[builtins.str, typing.Any]]]],
    name: builtins.str,
    source_flow_config: typing.Union[AppflowFlowSourceFlowConfig, typing.Dict[builtins.str, typing.Any]],
    task: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppflowFlowTask, typing.Dict[builtins.str, typing.Any]]]],
    trigger_config: typing.Union[AppflowFlowTriggerConfig, typing.Dict[builtins.str, typing.Any]],
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    kms_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8604fffeb1c50bc571738d80359061b9b51a5aead9b5948e68d8f9ed22f8e68(
    *,
    connector_type: builtins.str,
    destination_connector_properties: typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorProperties, typing.Dict[builtins.str, typing.Any]],
    api_version: typing.Optional[builtins.str] = None,
    connector_profile_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42d8fd30b8f4a1daf79b13dfcbbe53fe6dbd7268f959e3be7ea1395f42c9161a(
    *,
    custom_connector: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnector, typing.Dict[builtins.str, typing.Any]]] = None,
    customer_profiles: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfiles, typing.Dict[builtins.str, typing.Any]]] = None,
    event_bridge: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridge, typing.Dict[builtins.str, typing.Any]]] = None,
    honeycode: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycode, typing.Dict[builtins.str, typing.Any]]] = None,
    lookout_metrics: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetrics, typing.Dict[builtins.str, typing.Any]]] = None,
    marketo: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketo, typing.Dict[builtins.str, typing.Any]]] = None,
    redshift: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshift, typing.Dict[builtins.str, typing.Any]]] = None,
    s3: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3, typing.Dict[builtins.str, typing.Any]]] = None,
    salesforce: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforce, typing.Dict[builtins.str, typing.Any]]] = None,
    sapo_data: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoData, typing.Dict[builtins.str, typing.Any]]] = None,
    snowflake: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflake, typing.Dict[builtins.str, typing.Any]]] = None,
    upsolver: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolver, typing.Dict[builtins.str, typing.Any]]] = None,
    zendesk: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendesk, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb391a5cd3439d4671b618a7e1a20a1a9bab4aad8353d5bd0321c5c84658098f(
    *,
    entity_name: builtins.str,
    custom_properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    error_handling_config: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    id_field_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    write_operation_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bead7b889e70eaa0a07577d92cbc6a2a8c98600a829371f23ed2cf9063fde654(
    *,
    bucket_name: typing.Optional[builtins.str] = None,
    bucket_prefix: typing.Optional[builtins.str] = None,
    fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f54b5d158acfab6b1811c483af35edc02fe3eb39cf8a393de4b5146b0d2a6e8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c679b9e808835d3f244f43484415fa3efcf3b7cdcd37365f660e7fd1f7d28834(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71dd6b17d67474d4d846df4ac1ca90432552778817de0ca11fa8f5e9a96a7157(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94532d3628b17764e554fcea55bb16ff812e4cc63a0d51b521945bf536f1a5ae(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__847430025085d9f5665ba05d6198406872f96624c18f5d8df80e487134eff4ab(
    value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e90d351226d1cd9e57558f42a17be55d97ce09709fcd827f55c1e5117eef039b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08451f778a951a04ce4ec6e4f1e700c11d5490aca41f13936c0c1036c00d5e2e(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54abf8fd0e6ff0aba06be4d0c546c4559b620a5c02d8a0611b111fdacc7ea691(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1391a1cc817dd79d9ec764d5156595f410ec8c6769ae37a3c5522fe07879171(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43a81522a972a572846b7b1c7eb502796480e88693755c820199576c756b422c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__423c4eda543d65d4086de28dc88c836c2aef6ae61d30aa5c16651a1fc8d87a45(
    value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnector],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__429c47cc24ab75431afd897c801f977f56aaec630156c5bc0dfb86ced171d797(
    *,
    domain_name: builtins.str,
    object_type_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33a9255fc287c95ba820fab8eaf843925d4033315f0b4f8ac1cb269428a6936b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9eb2b8941245145a7f823a22dcb5ac57329e83ba94360b52de8800babee067c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2d8e76c0931b138253bdae46851ed85a7152b1fa7b294c93f6f33c19b1e6eaf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78ff742668016f2f323e74cf9e371a8ac7d9090f32b2ea63f831aa6a846818cd(
    value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfiles],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfa8ca51fd6553cd7108945080e2dba16bfcf80118b8f7f5d8c19d951baa9b1b(
    *,
    object: builtins.str,
    error_handling_config: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18a6ba4aebd83dfe0d561a52865e8ff2329742070024f1b310dff4cd5046e2a5(
    *,
    bucket_name: typing.Optional[builtins.str] = None,
    bucket_prefix: typing.Optional[builtins.str] = None,
    fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e55b1eb1f3655da97510cde333931a4773010b7b805a5e44baeaec2099c2bf0d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d320316c508f42c776919dfbcafdc536fa836ba9a289e64b25f3a7d581cd4e3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b7ca18cec3cefd1ee2c33318fee82ebe79ebbc0c15b487dd3dd8c42278dfbcf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab9da726ac35776f49794fa4d12a8d27740c6d4f9611e986f45cf7b97416af00(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6a51293146c340718e4c7928019bf9a5cbabc023e5e755f2d6c59d9ecd6164e(
    value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__868e410705d0633313164cdf0d2b5ce3c35f6b558ef5bd0371d85ae3d43a79b3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e23834d96dcdbb186fc5e8785ce82fbbc2dbfb542f41f3d15cb80dfcfc4dcf0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed0dff519639125d8b82d24062444bd304aed498b53e76e2e120687be7260142(
    value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridge],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8178942c23e0013761979ec005db3742768f7afdcd987842b0f584f65aa5f758(
    *,
    object: builtins.str,
    error_handling_config: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7648cc52c43f8082b603dcf5f2c6bfa4cad0bfc940b9269bd42a32ed5c21b3b(
    *,
    bucket_name: typing.Optional[builtins.str] = None,
    bucket_prefix: typing.Optional[builtins.str] = None,
    fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a6232feda1fee0d67a0fb02c314a78709cfbc8350a48e958be41cbcb3f251c6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39a99edb57032c61a0fe1b100c6b2bcce5fb68de26f91696cdea72b490a30630(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__347e1877d9a0d7d827982512eaf788e85c2f0bda84c2a3e8a7fe3f4537d49d77(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ccc72b819a5910c80d631c9504df6907cacb505fd6c2696f8dffeea091253d4(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d316e6a2eba63b48b9cd67a0b98750c9bb0bdcec754b749c0f3a5a04893e4c91(
    value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f89d06c1d4b3b73b4be3034f3881e1d5657b7215ad998db2f145e973f47196b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__715f44ca76d5c106dddc56fdffc1b7bc88cc09b91a5332600eadef73c4fef9e1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f11fbb585f8d5e565ee7713d8a2b547bdc06f8794f41c6a6498f2272be56232(
    value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycode],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63471c0503e11a8143f462ccb8eed132050c99bb068a6f0e0d3e39fadbb515ea(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1324e0aa5141f0e6a3ce2a0a75926ac534f71a9c171961831b2e872e70ee62c9(
    value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetrics],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afc149d202b55bbfd3420e8375f8880946e97ac6ed1b34ec8059615c520b9d5b(
    *,
    object: builtins.str,
    error_handling_config: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27f7269878a1b038ba95d4aeb89052da0dbd16c0d78caa0ca45e106d26465017(
    *,
    bucket_name: typing.Optional[builtins.str] = None,
    bucket_prefix: typing.Optional[builtins.str] = None,
    fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__379bb9b27b87c9bb1327d97d6d74fcef45ddbe41d304ef7d4ebfb4e48a8f2e84(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02f05bcedf15a1911a58c123947dd409de5adb9a42557265313179ca070e6d9c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__389509348fbb21138aba326fbb7c83050ef1a6d4e6ba726676f939b632696422(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb4513e32d92f7f6f5ef877fdf09896826539d88e7ee1ee3b927745473e8fe46(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c161b1854ef95c5f358620e25a15bedefc47b5d69900f0e41088552fa13333d(
    value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be5901325a41811039efaf7b7775a08d46b19c487e4e40b33c92417082695e1b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00256face2a2c835ea9cb402f3b7963c1c6d8c83be22321ab57ab2875ef1f13f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aba863f5e8e56e8768e11322dbac739a410e6ac96ce2902ffd4713b4f4ca3a52(
    value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketo],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f44c5da04925cf90022961d85f219a98bc83eef975a85973c2064b429d3ae1f8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea10b27aa08f452650f57d8b60305f582d8f4fe4e7c6e5e748b1d57df55906ce(
    value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorProperties],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aed8f50d43a2c8c41fdc3a258bce8a31ab18dcb52d84b1ddc862c52ff25079a9(
    *,
    intermediate_bucket_name: builtins.str,
    object: builtins.str,
    bucket_prefix: typing.Optional[builtins.str] = None,
    error_handling_config: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4f49f71ee6d4665429292155ee1ca5d42a5c986e8075d1fd6df2bbd6c4d43ed(
    *,
    bucket_name: typing.Optional[builtins.str] = None,
    bucket_prefix: typing.Optional[builtins.str] = None,
    fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f35a76bf9cf1ac6a4a3cc2a6e17e43172059252097e1721dc8f96122dd83f07(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ae74c4475f78ec1d811c42efa68add7653ef0e9fa854232820c33dc12a8de1a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dee7cad114c318283f0dd55c1df1732f75fc692c659c086a0272652bf2b92bb6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c6fc7d7c908dc1e4efed81e50ca85274ab70fef9a7e0bb3eaf5f6175f646468(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ea2d654629d16a5dad48731ae1148b1bfd4242138bc0e3a462e34b60ac01c0e(
    value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2a0aad7c3ae038fd4d7410d64fc392dd786f1f84e7045c5a9d247f760e75c57(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8a5abf489fec1308ecc2b62b3010c0b178ff3be70319f2ee4fd68c287ac4bd6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d496d0ead7ea37d4bafa163d5004cd53488c11e15c66eae1b101d9649878441b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be814dee091f39e1b992519e8b3dbe843de17379af6bea14a1964c6b6dc56072(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b7d328363fac27a3442ef968090bcb597b810674644518ba6fbfa745068e4bc(
    value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshift],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e273014bdd759433a94ebe42703c32af793417bfb167da0315b1e81a22926db(
    *,
    bucket_name: builtins.str,
    bucket_prefix: typing.Optional[builtins.str] = None,
    s3_output_format_config: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5807e6162dedffce3ed35bd65d9ebbce1f4808acd01a9f91eb2516c337802207(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3368eb212baa51b73df6fd7f805a5671c739560df441bc4c77fd946102e00e1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3adcadb3fee554e3881a6e174b57d1385e7ec32abdb1f0d60dad67f2099b7f33(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdaab4fa19eabeeab5f60a60f738bcf08ff1b57767c495945564a174565e6c58(
    value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84d7dd2d316975595178bca0a1c98fcc99b9b6275118078f93dc68a65b79f687(
    *,
    aggregation_config: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    file_type: typing.Optional[builtins.str] = None,
    prefix_config: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3a7806405d7ce6e8e549b8db4b9b3d14a803c2930add6893b5b8e3c1e414665(
    *,
    aggregation_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__870449877fad7f137840d2f42aee96b4036e9c3aff6689579a123fb0aaa37962(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75914161b691bddc19c8e9e0cd2fc48143fbd874ea4b338316faf698b11f00fb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cefded4a8f4a06b7c2330e4514b378910afeccb1ff76e65c51707f8b7b3e8f4(
    value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__094baf95cae858221d42517ccc83bda464ca0e9760e1886bf1e17f99d20751d6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48cc01f3a2357ee75dfa5ca721ec0dbbb1b270b94458bce3cfd53a639346ec87(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cf6a1e4eac4f50b7a445c8277ac474e8e84f0e7d5fcec6a6bd6e8945cda0c6a(
    value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abd30ab6554c9f12ae426fce3f6868221acd166f42d6c770598e869cce1657b6(
    *,
    prefix_format: typing.Optional[builtins.str] = None,
    prefix_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7d4f80a98d68d0ed01ced1fbafa1bbe1bb9409524745aa9d81946f5161ffff9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28a50bcc1dfa586a2700dd8abecba839fbf2a5a90ed412f3a48cb8b70d57bfc8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b407a313b6e6cdf75f11973cf166427340ce48229bc64dc1a248f6288a25689(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__884b5b4c53006e2132182124372f7601a77a18b70b7ec166e57eb6870bbd9445(
    value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35d855f1d39130210d226d545edd7adaa02ecdffa58564a01b98dfc585da9886(
    *,
    object: builtins.str,
    error_handling_config: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    id_field_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    write_operation_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d84acdae301b19ec65333de30e0616a5fbb06a1a54d43b0069991c1be66c1182(
    *,
    bucket_name: typing.Optional[builtins.str] = None,
    bucket_prefix: typing.Optional[builtins.str] = None,
    fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fb19f8635083e7846eae9ccc838a0e5739d46dd1edc7eb26cd065572b69ff88(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91125db0cc4662fd82d76c995270b19802a63a51735a5058d74e995d315edabf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88394aebabde376d483697ec8da1264ce6f7627b25c0922a1959471e33658a64(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c699f2f97c88d525f2224850be5866f58414ffbf5bc501dc02911a998986cca(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5747905e07e918c0afcced86478ea1e863b8e0946ce85c28b674e7cdf6991613(
    value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58df4bb8fb4ee625b1ee205c6ff082e5b73415194c13a979199b04e0ff6b9f0f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__221af9aebd624086001a8302a51868a0a1ea665afe806e5c048b967736c0da97(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a36e8612ced04b0c055d4e74906299a3dd93c29f94cf75aa16cfa1ac0b1c8285(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81f3725a140ace4858ab32157826756e8b5c0258cea8d587cf780af48e5cf193(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88b130aa307078afa3af28740a776c858c35b1bff36134bdb60a6fdf089989ff(
    value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforce],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05c09efed61510f3adb34d941640d24eea7df839ed9e004433d98dc65b0ffb16(
    *,
    object_path: builtins.str,
    error_handling_config: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    id_field_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    success_response_handling_config: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    write_operation_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad6573a4b6df04d95d38e73b15ee5e1a67884441ec760618c9331ce02bafd3f5(
    *,
    bucket_name: typing.Optional[builtins.str] = None,
    bucket_prefix: typing.Optional[builtins.str] = None,
    fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ed2c27d6a36cbc68676fdd746d7542b04f65fba497b36e7d1fd5c20db49f4e5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5a820bb812863bb8f40f269922316ad32a9f9eec9891762990aa2b6bd56b907(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75802ca2616d2ead59afefa67e162e78afbad08c057c22707fa880786a540efc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3077f1f78abc11abd275123a4481f77d9baf328f76f3b074b4829217a8adc52(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7bb37ab610623e44b5b0dc218d56797ee188db21ac38d27bc54a9b411a11a677(
    value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27111f78cba85f549462bf32681693f999f68bd4db9073cdddd249d5dde26af8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03e33572c15ca8ea22cbe610a263a9b058c320f71c73011cd9733f960baf10d0(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e41636ddc949df588bde0c4f60602d049d8c5168eb89a22d793c193cdcb5f90(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db2fd34505711423460d61a03a2893ff6837b1e4af275d41cb52356ebc6782d3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51b43884a869a876ba7f28d3d1314f0c13c9319ef53824e2d6e7f3a44c9b34bd(
    value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoData],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19fd2065656fcd950aea2879baf1bdf3102c625be99d2bf33234de04315d1d5f(
    *,
    bucket_name: typing.Optional[builtins.str] = None,
    bucket_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e32467f60a1b1a26b277cb6fe61a0374d24696af39af21d3dc3793c52b0ebbe7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81cc3ec95bd5fde78f1e6a6ca479bcd7ad848ab8bffc3f68a050d35e4cdbeae9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a723a3a712a16238369fc5b8191d422f8518cbc4dec52e55f9a767bf8ab15a8a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2d13757751af4378d7729950cb7e89b46fc126e3284ac67a4327f57c1e7c1e3(
    value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__674cf34d8d62ddd75c3b9a0fc9f6f1f61e4ace000114ec49ebac87ea1b925bf3(
    *,
    intermediate_bucket_name: builtins.str,
    object: builtins.str,
    bucket_prefix: typing.Optional[builtins.str] = None,
    error_handling_config: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32a51b60a5d2abc2a7722c4d2d3004215dfdb301621b25ba83d71db5816024e5(
    *,
    bucket_name: typing.Optional[builtins.str] = None,
    bucket_prefix: typing.Optional[builtins.str] = None,
    fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce35ae397c6d010d999b6e5bd4492ad5fa6727e730f3df128f73e62f0aa17b3a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf39b918c0acf82e48ab1637b3e7d6caffcee98110870354b6d08fed0c5a0543(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7b00c879244698f8783a41ee682c83633f762498d44dfdfc2b37a79a051e29c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08592e430d024f66a878507b2dcb78783b6f01954f0ee3c23391fddf23a0404f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d4a8cde216ddeccb029f2ab4fd08905c752b4dafe6ac51f57c734a4d0cb629d(
    value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__816fabdbc5811b68d70a54f8f053959710ad3fbbe0c01e52ff6c7a2fd58c974f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__939cccdccad259cf498e6a33b05d0e22d38be6fae713acab66873fda7fcd4e26(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8de59a0494091d55450369a696ece7a5b185835a46cc91ae8bd26064e5c860df(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e171561ee10e6eeb3005cd1f49e6a5f37b0b4b9639aafa88909471e33dd78654(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae730e659f195dac5f9f8956fa224083a4b506b58e5b670bceeee358ffcd42e0(
    value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflake],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8840f37373b3ca5d2e1740dbaab71d75d494c24d4719049074491f5a140787a5(
    *,
    bucket_name: builtins.str,
    s3_output_format_config: typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfig, typing.Dict[builtins.str, typing.Any]],
    bucket_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e44da0e1e62584834a42ad8835c988b37fb752002eb6fed14cb8cce58c38ac0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1dfc731ad368c4011a4919fed05d6641971c0b79e6d17df7d0a4a237282546e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a34091d04c842c45768288a67a0cce81f6b34e696b3cb739adfad85120783125(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d550b168d9583650fd3e81db00a1d19b546963cfd6de4181f05917d9716e91a(
    value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolver],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b2e301b01a26c816bcaba7e5178e62504d762b3bb6c895a689e36f5c9b859f8(
    *,
    prefix_config: typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfig, typing.Dict[builtins.str, typing.Any]],
    aggregation_config: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    file_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93d07f17f8d1c467184ecaffea487b7007f64a4489e13461a761958128bb3057(
    *,
    aggregation_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ac2a7c6ca11ed2bcd587227afc2079480c1f23abac7d44c622db3e0fa18190a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f61986ccaf849dea33c0b0cb260d682274a6db4dfcfa3b62ed5cdcbd80a5426(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a26d49a5e2f807acf269adedc75b200f694368aed0a5b1bc6f6f095213de10e0(
    value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26682c1772d88e9fc62676033953f2d081d5b2bf471d10f6b387423a5996a7ec(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7dd13984bdaba355094b60434aaacfdc219f10cabd964405a0d735e00ad127bd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d6b60cf5aa42fa77b49eff0683b69259a71b0186b5696866f2c9f66edb640fe(
    value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0aeda194743ac3acf58ca228c8b1271a0462827ba7cadc9960d7bf80cb38b0c9(
    *,
    prefix_type: builtins.str,
    prefix_format: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c8cfceb3a3e333bfda73819ae3255348378c4186afcd3aeef29f14a37c1af1e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86e4f70a84e7b9353b65b043ae54753d5c6b029450a8829a12fa74f57a58b2b9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ada9f58a637301ae9c8d03628a153ca714cc2ded9c23a77be1ceabc8ad488ad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2a547ccf2234f9c1dd928d56d2241b60a2755eba2b13a4d1fbd135cbb71a068(
    value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4c0e68e3f96015e12c266468c3f010c25f97a60879c61dc2b54189ec163d0d1(
    *,
    object: builtins.str,
    error_handling_config: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    id_field_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    write_operation_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7107d562e77597f27a71f3a78a93eb55fa803a1029144b2721be3df5f9805f6e(
    *,
    bucket_name: typing.Optional[builtins.str] = None,
    bucket_prefix: typing.Optional[builtins.str] = None,
    fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ecfa4cf37281ad02a2b6f0a6cbf0ad5050ce74286635ccff03eb825654ba837(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2e0c00268e34b0cfea5b2b07d01342f0385d6392646760f0ea48bb9b3d1bd39(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd870d731047edad8e9e47b7fbd0e4f68c6cb447497142a5aeeb545dcb58049f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84abd74c7601ba88f4fe20989471611197943b4d2c4cc7d5ee56bcffd05b8cbe(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38c7bc7207576851ed73925cb701faa7317591fcf06181d3a4ef24af8e5fb1d3(
    value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__489f52aec612e1e4ecb7a03a115333a84621f3830e2cbf209d66827a93037497(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3381f01d2c42f36ba41bd62636b7a27be9e16c00b97125a0c88ba8bc189fad91(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3921503a5f298d75880aca47a83623ddd2da87a7c56c1e1f2c3f793886f87f0c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a55d1d2762c2c9744fc1570571883c78a64c0ab6ef32fe932337f43c27bc033(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb42324c8574298e4ed66b1326301b7ff3dc25149cd3e6890225e757667a03f2(
    value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendesk],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4835374e57b48cd60eb54a99440f38dcd51baffb6ac77cd5ea274893347d941e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5b9d746f9c472678d1619da4a6e7835ae7dc0126c3d6a981fb0e1bc529b2428(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1105703cc0ffee420adbff03699ce33292f82ab0a0ee44ebec4edcd64fce846d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__776cc2bdc826cde47ccf653f24619a5cc0c2e905c67b11d8c7e6661f92993c94(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca00516121b617d176f67eed4a4487a145041de4c66defa0ca0c1d1a27970948(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98e35ab120a95e86021a2d404a9c6c0118808ffc6c04f7a66850dd36573830fe(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppflowFlowDestinationFlowConfig]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce2451bdb68cab283e27363f505e9eaec337ace9b7af4a791693a78b81fb9e89(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__810d26b549f0783623500638c2a63bc866d93547680a999df3c7b8887e89e431(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7e19c26b990bbe4e99049b99d55c1be4978dbb61233e0a813613c563b00770c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97923149f1b92148788243d745129fe5aa8c1ad9aaa2625563569181f688eab6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a56b7a0f75125f2079e677d2cc3e88239a7bca7241828583419a0b17d595cce8(
    value: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfig, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce547e06a2051ca336319ed88317d3f218336581be8b722f2493d09f6ed59f85(
    *,
    connector_type: builtins.str,
    source_connector_properties: typing.Union[AppflowFlowSourceFlowConfigSourceConnectorProperties, typing.Dict[builtins.str, typing.Any]],
    api_version: typing.Optional[builtins.str] = None,
    connector_profile_name: typing.Optional[builtins.str] = None,
    incremental_pull_config: typing.Optional[typing.Union[AppflowFlowSourceFlowConfigIncrementalPullConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2321d8ed3602781728fa5b16bec40274daa8e75e5c648d7284891a7ee5dfe65d(
    *,
    datetime_type_field_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ef36e04c9d63b905f7f57b8e9ff132eeb489f39417896ad5533b2681b96e05e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3bf2b09568c31115e3a32cfb233fe44163e5296eb65430b31578f9ccae46502(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__988406aeb3d4ab545ef5f5410a20c151a94cba71d7506c4129a9406e38ef2e02(
    value: typing.Optional[AppflowFlowSourceFlowConfigIncrementalPullConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa1b23f4e269563269bc74962fe981502fb9d9d1e7278444b6a4cc12755d499e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be957c3f328450eafb8e8837557171642752da422394c7791fa7a4c2a75f5b31(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06d28d949a050c1189293b6eb42df4234f603d867027436294f8ea1aa4920d25(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f36c789f7cc9ed014a60c08c309f1bd5fccc26292641b67b79e9615339d5878(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7d1fa6d015847acb471824e5c7a9e932305b8080660e0ea34393d464c2f107b(
    value: typing.Optional[AppflowFlowSourceFlowConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e7ea0597897f3c6b757dded98bd088c6998b303f2c2c642319290a4eab1bb3a(
    *,
    amplitude: typing.Optional[typing.Union[AppflowFlowSourceFlowConfigSourceConnectorPropertiesAmplitude, typing.Dict[builtins.str, typing.Any]]] = None,
    custom_connector: typing.Optional[typing.Union[AppflowFlowSourceFlowConfigSourceConnectorPropertiesCustomConnector, typing.Dict[builtins.str, typing.Any]]] = None,
    datadog: typing.Optional[typing.Union[AppflowFlowSourceFlowConfigSourceConnectorPropertiesDatadog, typing.Dict[builtins.str, typing.Any]]] = None,
    dynatrace: typing.Optional[typing.Union[AppflowFlowSourceFlowConfigSourceConnectorPropertiesDynatrace, typing.Dict[builtins.str, typing.Any]]] = None,
    google_analytics: typing.Optional[typing.Union[AppflowFlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalytics, typing.Dict[builtins.str, typing.Any]]] = None,
    infor_nexus: typing.Optional[typing.Union[AppflowFlowSourceFlowConfigSourceConnectorPropertiesInforNexus, typing.Dict[builtins.str, typing.Any]]] = None,
    marketo: typing.Optional[typing.Union[AppflowFlowSourceFlowConfigSourceConnectorPropertiesMarketo, typing.Dict[builtins.str, typing.Any]]] = None,
    s3: typing.Optional[typing.Union[AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3, typing.Dict[builtins.str, typing.Any]]] = None,
    salesforce: typing.Optional[typing.Union[AppflowFlowSourceFlowConfigSourceConnectorPropertiesSalesforce, typing.Dict[builtins.str, typing.Any]]] = None,
    sapo_data: typing.Optional[typing.Union[AppflowFlowSourceFlowConfigSourceConnectorPropertiesSapoData, typing.Dict[builtins.str, typing.Any]]] = None,
    service_now: typing.Optional[typing.Union[AppflowFlowSourceFlowConfigSourceConnectorPropertiesServiceNow, typing.Dict[builtins.str, typing.Any]]] = None,
    singular: typing.Optional[typing.Union[AppflowFlowSourceFlowConfigSourceConnectorPropertiesSingular, typing.Dict[builtins.str, typing.Any]]] = None,
    slack: typing.Optional[typing.Union[AppflowFlowSourceFlowConfigSourceConnectorPropertiesSlack, typing.Dict[builtins.str, typing.Any]]] = None,
    trendmicro: typing.Optional[typing.Union[AppflowFlowSourceFlowConfigSourceConnectorPropertiesTrendmicro, typing.Dict[builtins.str, typing.Any]]] = None,
    veeva: typing.Optional[typing.Union[AppflowFlowSourceFlowConfigSourceConnectorPropertiesVeeva, typing.Dict[builtins.str, typing.Any]]] = None,
    zendesk: typing.Optional[typing.Union[AppflowFlowSourceFlowConfigSourceConnectorPropertiesZendesk, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__313a41e7f6563d41145bf4583a7b3ad73372f363a115f27c25ed60fc41fb1117(
    *,
    object: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b20de641b47d63bdc1e049c9f5c782d36645e94e3b0a76f469ac6178ed3289e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d3d5d52a0c07cff545302d28f2cf35334114c3836516ba9304dfc175181ccf3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff3d001bb9a1c228ba3c001a6ea400733d0689e31fb8185556f3957511673a7f(
    value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesAmplitude],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d421cd0d8118776bd2383dafa414c36b1a0037661acb5408d456555d5b65ad00(
    *,
    entity_name: builtins.str,
    custom_properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9dc41f9d628a7593ee11035d566eb516400f06fa23d65dcb32830edbe22ad98(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48ae880a30c9e480c94ec3568288cb8ecfc8005697f06965e07a57185058604d(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0b27985a2a4f50617b6b6c8df70a18bf3b3aae4210fef4cf26a30ff8e830893(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e13e17c0d47d0ec92684bbdb7a51a1ee69b825d3c59cf960ae6338c2b1b95f8(
    value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesCustomConnector],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5923e712001b9604785e2ba6a592e958d155fc2af9fbd6e0112c97415bf303b5(
    *,
    object: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10b88781d36e2d7c5f49216517838d0457437c36ac3856843807bc0e14d134ea(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccd37e5134679468d3104f3ec70b47c56a620eb0d57628f49f6a673661d68e22(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b91cdbfec7c6e41a5dcde39d473eb5d6cd3eb9403ded9a1f66a3e7ec11f0ad94(
    value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesDatadog],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba9e5d28a9ab161b56194ec840e8e5a8539be3e23ad87a0314eccd3ca531e5ae(
    *,
    object: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d19abdea4d788b7be1236c9a2a5efc8238ca00d1e7a3e84cc04666b2599f2e4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eee32d4b134ebe159a79ca548a451549b53cead22852fc7d98ccfc1e057afd63(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f3091d872232e828a79e6e53d426bc5300cf3eef9ecaffebf79ff1ce5cfc57d(
    value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesDynatrace],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac43f824241a31a8cce56574601922c425cd1ab2e5b6f3725c94005c371609b1(
    *,
    object: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82a329040d67c8b9634708784f20d484bcd7f09f3a7ad3cc22024313f68aaa88(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c385e86541dae5eb13858e713e026bff8827ab3e1179da53661f918ac160f17(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23f3305814eb995a28f85449f5f0a38012ec1a4e572a2da199498d05aa68cc9d(
    value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalytics],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7e5977a145ad6010c5067b8398bffe37a4b39b692b2025ee0b00a6228c192d1(
    *,
    object: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__225c4e397b8d864e8520a74d5813849b0d5e66cc01a9fe6ccdb20625ae507f8d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d56181ff258a8738ff6715bd737501741463807af122e440931efc3b768abb71(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e03c854a79317d654dd8004742a5bff4f0bc6ec36f20d26457efdae521408329(
    value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesInforNexus],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__face3f520d057155d23e57c965cef25d8786c298c2ecbbec516e1adb48c94a7a(
    *,
    object: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16d5338aed64a02109ceeaa617a06fe0cc03c0b87920caebc6b28c7c53c69b7c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61ca09d1ebf3efc8c26f05906199aa4f5fb39776c29ac36f29292845cbdebe6e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d35a8ad3192fb9c582893f02c11b59df2dc3ca2149b416107e902274693f52b(
    value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesMarketo],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c602a89048f3b41d08aeaa483a25a37a0bc8db26fe855e276b5332027064c95c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ce9b3cc1ebdb06b5bb9d44b3c3c97a5ae117e174068fc2f0055212a0d473bae(
    value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorProperties],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b4026e5a258d7cd1c6fe23fa9bb33c72ac9f40f95cec82dd0bddb814e9a9ff0(
    *,
    bucket_name: builtins.str,
    bucket_prefix: typing.Optional[builtins.str] = None,
    s3_input_format_config: typing.Optional[typing.Union[AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92bf967637dbd819d4ed6670439242a98ef56e73b2727a71c0d2371fb8a70ad2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7aa5417c8e0e4d62c8b6d326b58278c3fbd136f74ac1e6350a7c63bdfaeeed0f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8c62ef8f5d7b062f9d088c1f1b1919bef2045d9f059236ea881512dc1623260(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8800a76f95368c91d4175902e25ceb0a2d013676c16ed444aadce4aee7df024(
    value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a002120fd1131e020794638ac20aadca7b459fddc50118cd9cbe2aac41f5bfa4(
    *,
    s3_input_file_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48ce85ee744b1b1a335fa2ba371ed9fc4d631ebb204b640e4b42a111bf645586(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ce5a4f608982576f8fceca1ff34213816b7d0e16cb99bb1c632c82e975a0308(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf0c8c347635ac843d320fe1dec39704ddce58ffb50748ac637404e9f0e927d4(
    value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7701fa60cdc6dcff83073827d8a16ee4bf38489f81aa0c6981eeb0c70abcf1c(
    *,
    object: builtins.str,
    enable_dynamic_field_update: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    include_deleted_records: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9905973b1b51588ae7fd47305b6c2464cfd602e42b584de02bc27b383b44f4cd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec3cb7c8805f8061e6f33072fe025be8d6f1c789196ffd3550ab2499c9513998(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c69745f9bcdb4a98737ecfa4beb6484791433a88272f9dc62d26dde9fb0efd9e(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8275062e40e846a5d39b5619f078bf965d4b31d318b461996eecaba30b54984e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44f25390e269f882d5fcf4c68c0264d3108691c3f128d41dcc6b98e0f3f9c84a(
    value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesSalesforce],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d04e62c29ab455578c96db4e4faaf6e874aba450dadd168f4e63fd8a9fe4579e(
    *,
    object: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62ebf0a32c078e39b09d10cfc0520ee526dd1dceaa664180d1ba2c771a5fd2c9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad4d74a02f909001408bd41b5fb8f3d4438ee544598b5c1957355bbda06239be(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0239ed79b6ee6d72f2d86a137590835d8931bf3891cf4c32182a787afd3c8a2d(
    value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesSapoData],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__031feb7d4713b5a68075b00d95ac88a1d5a0bf8e6c04d60e50c76a6b074b4a54(
    *,
    object: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d62c690f8d673f8c800a8236d44322d9a4c14ccfa239947ee7672f8aa763ac0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a7739c0046874a85f0b2dbd9a6e699959c66f29574703637977a0976bfc67ea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7118541e83f271fd74c69e323c63d8788bb6196677b7bea709123003be54e6bc(
    value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesServiceNow],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1921f24b3b55bf2dfede826831cca69a279f7b17e87b85131d320b483a5ad2aa(
    *,
    object: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91bc991278ebcac9a8f4a8f45475f1bba74fa5c8f9268e5de81997afb9a7e052(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11dd80a829485da7d3bdcd57a88f1487702089ce19154049ee5e41ae0117a91a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82a8be23ea2450de509ff444136ca05bf9c05fb9735eef3d33fd6ac02c9bc439(
    value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesSingular],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e4abe7f73381c8cd0007198df2b05e0639c85492bdeada4ddd386cb1d5636aa(
    *,
    object: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5da4a5acb11bb5a04cbf1890588db1d3b6805d00244f24a9fe9b5e377a9a5063(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a53050bc3706abbb931fb7bceb10eeaed23523834174e0917ac6fbdddd60adcf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a491833880c74674727d92f3debe4f230101dae4209980403f041685b382ce2e(
    value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesSlack],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__868bffa5ecf992097896ad19dbb548d2e8f304400ca194823bef21ca0baa4a04(
    *,
    object: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e244f917995e5183de25e5f6402224fd9b20d4953a8871c2a95a8030cf7690a5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a95103c804e0af53ea7d1f15ad3e11c4f482404778cdbb76f9bcdcf660c6b4bc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3277706d3fbb4d6e41a371993a37ef206c2a1d3d43e0d8a14c82821f35ffcf08(
    value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesTrendmicro],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78b189d8c7241ee62e7393086633761d4d54d57a234d9e1409bcc0fdba75c460(
    *,
    object: builtins.str,
    document_type: typing.Optional[builtins.str] = None,
    include_all_versions: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    include_renditions: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    include_source_files: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33255bf2b53ce588ddaa8d3bdc7fc85d46d4d0dbd7ad374ca499de44b32f240a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b2a8e8dd2df39f2966f4270f2b4878b102e99cb7e5f0d544561b55c99662611(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6745eee579e525d117f0c1fae256cb447826fafe86030ec6c957300b53b04ebd(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71632c65ec8847d6ce3710b1245a4a038c0a6190558efd82ec0ab31acc516976(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1eb03d24ccdcdaddf4f0ba07564d0eb5a550314611a31a8a5fa4fadd6aebaff(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d4ced147932821483886c0bfc497b7a103939b7a77fa9b73ceef58977b9acd8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06fa52a1fdca7baaa8a6cfca42a9c7259a5fc85a4911b534868de290f396c66a(
    value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesVeeva],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb6068701dfec92112200922d8061b39786b65872b756830e7912f5178f67e2b(
    *,
    object: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbc6be6ba66b80b1d4e1a94e7d98e1833e4f4c23060ecb6c579606aff715d33c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d24e6f69d907ab5b9a330bf906d9a0de60ff7d88a57c57dba6268585b5e38ab6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51abf2295c943effbb4034b6cf20c9ff193bf578d65806e34440d90afd64d8ae(
    value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesZendesk],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5099b4a163451ab76e8e852a03f9625dd10c16a679891a8290eeb8a761d11a4d(
    *,
    source_fields: typing.Sequence[builtins.str],
    task_type: builtins.str,
    connector_operator: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppflowFlowTaskConnectorOperator, typing.Dict[builtins.str, typing.Any]]]]] = None,
    destination_field: typing.Optional[builtins.str] = None,
    task_properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36369d725074a475edd65ec430781139e47ad30fd654d676aea04db26bc44164(
    *,
    amplitude: typing.Optional[builtins.str] = None,
    custom_connector: typing.Optional[builtins.str] = None,
    datadog: typing.Optional[builtins.str] = None,
    dynatrace: typing.Optional[builtins.str] = None,
    google_analytics: typing.Optional[builtins.str] = None,
    infor_nexus: typing.Optional[builtins.str] = None,
    marketo: typing.Optional[builtins.str] = None,
    s3: typing.Optional[builtins.str] = None,
    salesforce: typing.Optional[builtins.str] = None,
    sapo_data: typing.Optional[builtins.str] = None,
    service_now: typing.Optional[builtins.str] = None,
    singular: typing.Optional[builtins.str] = None,
    slack: typing.Optional[builtins.str] = None,
    trendmicro: typing.Optional[builtins.str] = None,
    veeva: typing.Optional[builtins.str] = None,
    zendesk: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07830e0a565c359260c0e954f87f3aa2bc6e0722ae525769d63202d707d834c0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dfd155462b35dba3354710790fad0c022357f103eda91821ea33ee84c9bda71(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85cbc7aa555f6c388c9f274c59c534d7b485fd97a26172cff5cf25373c478f3b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__272d4b5446f72f2487992c13db1b909551f33e5acd5cfcade5f1f06381f94843(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b35c550114293d3e68bd87db74ece6edd7a5af1a68b0437636783d37da5dfcd7(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e195e7d61ca22de49f5f48e10e1fe868241d59936d922527aad39b4ab5ffe21b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppflowFlowTaskConnectorOperator]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5d05e0f42ffd8808a4623818e1e34e380ccfa550e9f835e2639b63cb75b194a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9647d58a393c47fd4aa1fbbd7c809d13e6e5a4630e1d489378276d889997af4c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6e416ab4ba4549c2ed8eb9bfe12402434deb92c71128db770249d8bb46b09ef(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4f8433b57f8747ef450b667cb380a6eca734aea295db09a3e7cc430f87136d9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2723736b99dfde9047505f84e90fbd244f7c22f000a91c5cdfb190dda022d341(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4aacb639d2a4b010162da36845631ba063787267ecb700a9f61ca7f053f99ac(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4593ed3e169723f1257d215d590daa781e7caface5adb24f312dd73d79381ffa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d33c9d6e0d012ade707bcd0f7662a31decf3280d87688a74530ad0ce6f49f2b4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3e4040fd8b3d8b06635871c2388145c0cc25690346d9997ebc9cc9a9cf635fb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__191931824a47dfa914de78f0af5a0eb2451cd4bf918863ac861a1c547e3313bc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__950d10ce95710d4018c1b2aca48df5cfe0ad6662b74d030df231306a3d07a707(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05acd92461f65cb2c3b558397e6e64f3c9617ae227b6f468a9f93c5501a89894(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5265d4e1163a1d5533bfcbe9850107696e060df0d9b7e1baf6f1083e98fc7e3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f04d3121ebfc3f5c45217ab4cb73d93266a61336be86a3f0de230aee15167b4f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__568549a5dc559c9391f5afcfe95345dcbbcf82cbb3392afc7233596ad65691d5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9e15c5d109cb3372222549ee0a5b16fa21a96d7ba3df5ff7217239a044bbbd5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e7af7b95071c9af441c71a7678cd8cf8e08ad6a0719dd03cd6d23d3cfcfe301(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c4f72343ac75ee5c1b1cb0c4c859bb3f5016679ebcc4775bdfcdd657f1a4db1(
    value: typing.Optional[typing.Union[AppflowFlowTaskConnectorOperator, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e949c3c116fa403728e03d91a92b5bbc30ee3a030b0f036e7e8ac21283eae902(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50925ba1abe1f51aab0246ee8f124cd7f5127caebf56455dcf4d8c4905b060ad(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae227f93bb5feb6e0489d56923940484d0f8957918721b6078e43bb32fb7c09a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__719153cc3d12db1ced04ac6e461174da62dcbad28d2959e15aac0bcb3185f3b6(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f20ddbf934d31acd2c4924fa603a761b98b00efeecca4e927dd5902d18e6c4c4(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d4e280035920de824d0e7712931cf4e0873bfdccc441fbcee46bc42045dafd7(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppflowFlowTask]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae84f9bb4025a97b07a08eea18fc981f76ec3506efd7cae12da7c1cbf058ad81(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18fb3bcc636806069a5e3f7a0a21edd2df58c76426f42cde862680b409c72f5b(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppflowFlowTaskConnectorOperator, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b2acf205a984a438104852138bfeee89a9aaf4999ddd073eafe9dca7bcd6699(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29d04fca2dcf13717625920f1836a864d8164f3777cc5590facef254608c8686(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8e15f1151823ed8cb2414619dbf0e155718c2ae919d738b2d2736718dca5e09(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66f0fe4e05b2c9f8f095e596d83782fb89790be0707327c385d25067d23c07a3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0a58d43def83ec463c227eba7459967309f7aed3abada664bc326b02bbc59f8(
    value: typing.Optional[typing.Union[AppflowFlowTask, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05235a507833fe56416ab2f2bba05df51f42832e8dc253f523f36f326d0c8733(
    *,
    trigger_type: builtins.str,
    trigger_properties: typing.Optional[typing.Union[AppflowFlowTriggerConfigTriggerProperties, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10bb8cc3a6f6e5c3374561c4490ccba2c3ce80e932c0d31debc3870658c73589(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5bba6f8a44c411ed3b05b32475b5d880a5ea9e9862102f2367663e4a8baaac5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__332d041ee75b6720b6b368788c7538105875284dd8c3d726708e6acbf53c2cdf(
    value: typing.Optional[AppflowFlowTriggerConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2931592b76a95a7f7d3379f17c773473758f1680b874ad8c28945956ad0da8b(
    *,
    scheduled: typing.Optional[typing.Union[AppflowFlowTriggerConfigTriggerPropertiesScheduled, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d8d8173626e40278c03bb1df457c6d044e8b910420ecb903830e3c17fd5a5e3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d51a09123497ae064dd2b27fe7ab82c52761c3cb7419cddb3be2b07abbe7f9ed(
    value: typing.Optional[AppflowFlowTriggerConfigTriggerProperties],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ef425d98e9fb19a22879f3c79aa1f179f26bf2ba9f8d4849dc7d19161ab2a33(
    *,
    schedule_expression: builtins.str,
    data_pull_mode: typing.Optional[builtins.str] = None,
    first_execution_from: typing.Optional[builtins.str] = None,
    schedule_end_time: typing.Optional[builtins.str] = None,
    schedule_offset: typing.Optional[jsii.Number] = None,
    schedule_start_time: typing.Optional[builtins.str] = None,
    timezone: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d30dfd007b84d23d3c2f093b09592ad4e491ab8cb60704fe79f67700d133071a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88c25b19b3deaf77966de2c0dfd3bf556d878aed9e29b9a1a36a87f0fa1e2993(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da3c532891d1a8a5804e0f0376921b29fcaa9bad61d75e8d2b6d23714592a60d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fc72389a2d2f60423158ccb45aa8dcda3b4639bc8b3ab6739e631a438084a9d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__006489b3c9763da4dcca2d89918cf2e3b1fb053e3ee11b98bd6d016f4a031f86(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c04f55d7c88a7cf404d21bee148b7f574cc3fc7c9264e8d9d025965bdfcf618e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afe5fd897053370de1f21caaa85d8faacdc8f622f8b8fbf53a9c40a4746dad69(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be74da71661986dec1e920eee49eafee3682320433cbcc2ba5846fd5947af8e7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94e4e1b4ad4d74f4a29813f846f52aca5acb91b559043e6b020cd7971ac162ae(
    value: typing.Optional[AppflowFlowTriggerConfigTriggerPropertiesScheduled],
) -> None:
    """Type checking stubs"""
    pass
