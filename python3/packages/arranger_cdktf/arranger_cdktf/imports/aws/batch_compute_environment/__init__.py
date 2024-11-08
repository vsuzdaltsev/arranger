'''
# `aws_batch_compute_environment`

Refer to the Terraform Registory for docs: [`aws_batch_compute_environment`](https://www.terraform.io/docs/providers/aws/r/batch_compute_environment).
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


class BatchComputeEnvironment(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.batchComputeEnvironment.BatchComputeEnvironment",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment aws_batch_compute_environment}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        type: builtins.str,
        compute_environment_name: typing.Optional[builtins.str] = None,
        compute_environment_name_prefix: typing.Optional[builtins.str] = None,
        compute_resources: typing.Optional[typing.Union["BatchComputeEnvironmentComputeResources", typing.Dict[builtins.str, typing.Any]]] = None,
        eks_configuration: typing.Optional[typing.Union["BatchComputeEnvironmentEksConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        service_role: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment aws_batch_compute_environment} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#type BatchComputeEnvironment#type}.
        :param compute_environment_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#compute_environment_name BatchComputeEnvironment#compute_environment_name}.
        :param compute_environment_name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#compute_environment_name_prefix BatchComputeEnvironment#compute_environment_name_prefix}.
        :param compute_resources: compute_resources block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#compute_resources BatchComputeEnvironment#compute_resources}
        :param eks_configuration: eks_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#eks_configuration BatchComputeEnvironment#eks_configuration}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#id BatchComputeEnvironment#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param service_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#service_role BatchComputeEnvironment#service_role}.
        :param state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#state BatchComputeEnvironment#state}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#tags BatchComputeEnvironment#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#tags_all BatchComputeEnvironment#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99a336e293fc81503d25c2fb7504768001e8ffa105f343b79b8154be862c0fb7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = BatchComputeEnvironmentConfig(
            type=type,
            compute_environment_name=compute_environment_name,
            compute_environment_name_prefix=compute_environment_name_prefix,
            compute_resources=compute_resources,
            eks_configuration=eks_configuration,
            id=id,
            service_role=service_role,
            state=state,
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

    @jsii.member(jsii_name="putComputeResources")
    def put_compute_resources(
        self,
        *,
        max_vcpus: jsii.Number,
        subnets: typing.Sequence[builtins.str],
        type: builtins.str,
        allocation_strategy: typing.Optional[builtins.str] = None,
        bid_percentage: typing.Optional[jsii.Number] = None,
        desired_vcpus: typing.Optional[jsii.Number] = None,
        ec2_configuration: typing.Optional[typing.Union["BatchComputeEnvironmentComputeResourcesEc2Configuration", typing.Dict[builtins.str, typing.Any]]] = None,
        ec2_key_pair: typing.Optional[builtins.str] = None,
        image_id: typing.Optional[builtins.str] = None,
        instance_role: typing.Optional[builtins.str] = None,
        instance_type: typing.Optional[typing.Sequence[builtins.str]] = None,
        launch_template: typing.Optional[typing.Union["BatchComputeEnvironmentComputeResourcesLaunchTemplate", typing.Dict[builtins.str, typing.Any]]] = None,
        min_vcpus: typing.Optional[jsii.Number] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        spot_iam_fleet_role: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param max_vcpus: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#max_vcpus BatchComputeEnvironment#max_vcpus}.
        :param subnets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#subnets BatchComputeEnvironment#subnets}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#type BatchComputeEnvironment#type}.
        :param allocation_strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#allocation_strategy BatchComputeEnvironment#allocation_strategy}.
        :param bid_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#bid_percentage BatchComputeEnvironment#bid_percentage}.
        :param desired_vcpus: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#desired_vcpus BatchComputeEnvironment#desired_vcpus}.
        :param ec2_configuration: ec2_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#ec2_configuration BatchComputeEnvironment#ec2_configuration}
        :param ec2_key_pair: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#ec2_key_pair BatchComputeEnvironment#ec2_key_pair}.
        :param image_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#image_id BatchComputeEnvironment#image_id}.
        :param instance_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#instance_role BatchComputeEnvironment#instance_role}.
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#instance_type BatchComputeEnvironment#instance_type}.
        :param launch_template: launch_template block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#launch_template BatchComputeEnvironment#launch_template}
        :param min_vcpus: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#min_vcpus BatchComputeEnvironment#min_vcpus}.
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#security_group_ids BatchComputeEnvironment#security_group_ids}.
        :param spot_iam_fleet_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#spot_iam_fleet_role BatchComputeEnvironment#spot_iam_fleet_role}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#tags BatchComputeEnvironment#tags}.
        '''
        value = BatchComputeEnvironmentComputeResources(
            max_vcpus=max_vcpus,
            subnets=subnets,
            type=type,
            allocation_strategy=allocation_strategy,
            bid_percentage=bid_percentage,
            desired_vcpus=desired_vcpus,
            ec2_configuration=ec2_configuration,
            ec2_key_pair=ec2_key_pair,
            image_id=image_id,
            instance_role=instance_role,
            instance_type=instance_type,
            launch_template=launch_template,
            min_vcpus=min_vcpus,
            security_group_ids=security_group_ids,
            spot_iam_fleet_role=spot_iam_fleet_role,
            tags=tags,
        )

        return typing.cast(None, jsii.invoke(self, "putComputeResources", [value]))

    @jsii.member(jsii_name="putEksConfiguration")
    def put_eks_configuration(
        self,
        *,
        eks_cluster_arn: builtins.str,
        kubernetes_namespace: builtins.str,
    ) -> None:
        '''
        :param eks_cluster_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#eks_cluster_arn BatchComputeEnvironment#eks_cluster_arn}.
        :param kubernetes_namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#kubernetes_namespace BatchComputeEnvironment#kubernetes_namespace}.
        '''
        value = BatchComputeEnvironmentEksConfiguration(
            eks_cluster_arn=eks_cluster_arn, kubernetes_namespace=kubernetes_namespace
        )

        return typing.cast(None, jsii.invoke(self, "putEksConfiguration", [value]))

    @jsii.member(jsii_name="resetComputeEnvironmentName")
    def reset_compute_environment_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComputeEnvironmentName", []))

    @jsii.member(jsii_name="resetComputeEnvironmentNamePrefix")
    def reset_compute_environment_name_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComputeEnvironmentNamePrefix", []))

    @jsii.member(jsii_name="resetComputeResources")
    def reset_compute_resources(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComputeResources", []))

    @jsii.member(jsii_name="resetEksConfiguration")
    def reset_eks_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEksConfiguration", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetServiceRole")
    def reset_service_role(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceRole", []))

    @jsii.member(jsii_name="resetState")
    def reset_state(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetState", []))

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
    @jsii.member(jsii_name="computeResources")
    def compute_resources(
        self,
    ) -> "BatchComputeEnvironmentComputeResourcesOutputReference":
        return typing.cast("BatchComputeEnvironmentComputeResourcesOutputReference", jsii.get(self, "computeResources"))

    @builtins.property
    @jsii.member(jsii_name="ecsClusterArn")
    def ecs_cluster_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ecsClusterArn"))

    @builtins.property
    @jsii.member(jsii_name="eksConfiguration")
    def eks_configuration(
        self,
    ) -> "BatchComputeEnvironmentEksConfigurationOutputReference":
        return typing.cast("BatchComputeEnvironmentEksConfigurationOutputReference", jsii.get(self, "eksConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="statusReason")
    def status_reason(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "statusReason"))

    @builtins.property
    @jsii.member(jsii_name="computeEnvironmentNameInput")
    def compute_environment_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "computeEnvironmentNameInput"))

    @builtins.property
    @jsii.member(jsii_name="computeEnvironmentNamePrefixInput")
    def compute_environment_name_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "computeEnvironmentNamePrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="computeResourcesInput")
    def compute_resources_input(
        self,
    ) -> typing.Optional["BatchComputeEnvironmentComputeResources"]:
        return typing.cast(typing.Optional["BatchComputeEnvironmentComputeResources"], jsii.get(self, "computeResourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="eksConfigurationInput")
    def eks_configuration_input(
        self,
    ) -> typing.Optional["BatchComputeEnvironmentEksConfiguration"]:
        return typing.cast(typing.Optional["BatchComputeEnvironmentEksConfiguration"], jsii.get(self, "eksConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceRoleInput")
    def service_role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceRoleInput"))

    @builtins.property
    @jsii.member(jsii_name="stateInput")
    def state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stateInput"))

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
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="computeEnvironmentName")
    def compute_environment_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "computeEnvironmentName"))

    @compute_environment_name.setter
    def compute_environment_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9dddd54195eab8d2b22b4684fc217f5166ede7f5443ca05e4638699fd6743c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "computeEnvironmentName", value)

    @builtins.property
    @jsii.member(jsii_name="computeEnvironmentNamePrefix")
    def compute_environment_name_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "computeEnvironmentNamePrefix"))

    @compute_environment_name_prefix.setter
    def compute_environment_name_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72358f6cb10e41fd73e6c3b8cbea6abd6b8b64dce579b6ec6ed84506d5f53727)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "computeEnvironmentNamePrefix", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37bb5bb45d5931b8d3b20c3ddef9eed9791c86bb7c0668582f116527a9fa8323)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="serviceRole")
    def service_role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceRole"))

    @service_role.setter
    def service_role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2213080914d7ba80a00d26fbff933ed5c3a5aea874079fac54cd81c36666b994)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceRole", value)

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @state.setter
    def state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62c129d3e7309a68d0b6e41e736ef2b71f32b7a774621fc510a7809a1f965236)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "state", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__543838d3ff5567fbe59e55c96c0469ea59388e56b5f023e750450d297977ed7c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29d9170043646a1d227edcc1396b490b212814b38d11db118d36d73b41dd400c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64bcf9a13708b346fe9450881002d7494c1230a85f2ed25588f4d0d87ddc6336)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)


@jsii.data_type(
    jsii_type="aws.batchComputeEnvironment.BatchComputeEnvironmentComputeResources",
    jsii_struct_bases=[],
    name_mapping={
        "max_vcpus": "maxVcpus",
        "subnets": "subnets",
        "type": "type",
        "allocation_strategy": "allocationStrategy",
        "bid_percentage": "bidPercentage",
        "desired_vcpus": "desiredVcpus",
        "ec2_configuration": "ec2Configuration",
        "ec2_key_pair": "ec2KeyPair",
        "image_id": "imageId",
        "instance_role": "instanceRole",
        "instance_type": "instanceType",
        "launch_template": "launchTemplate",
        "min_vcpus": "minVcpus",
        "security_group_ids": "securityGroupIds",
        "spot_iam_fleet_role": "spotIamFleetRole",
        "tags": "tags",
    },
)
class BatchComputeEnvironmentComputeResources:
    def __init__(
        self,
        *,
        max_vcpus: jsii.Number,
        subnets: typing.Sequence[builtins.str],
        type: builtins.str,
        allocation_strategy: typing.Optional[builtins.str] = None,
        bid_percentage: typing.Optional[jsii.Number] = None,
        desired_vcpus: typing.Optional[jsii.Number] = None,
        ec2_configuration: typing.Optional[typing.Union["BatchComputeEnvironmentComputeResourcesEc2Configuration", typing.Dict[builtins.str, typing.Any]]] = None,
        ec2_key_pair: typing.Optional[builtins.str] = None,
        image_id: typing.Optional[builtins.str] = None,
        instance_role: typing.Optional[builtins.str] = None,
        instance_type: typing.Optional[typing.Sequence[builtins.str]] = None,
        launch_template: typing.Optional[typing.Union["BatchComputeEnvironmentComputeResourcesLaunchTemplate", typing.Dict[builtins.str, typing.Any]]] = None,
        min_vcpus: typing.Optional[jsii.Number] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        spot_iam_fleet_role: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param max_vcpus: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#max_vcpus BatchComputeEnvironment#max_vcpus}.
        :param subnets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#subnets BatchComputeEnvironment#subnets}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#type BatchComputeEnvironment#type}.
        :param allocation_strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#allocation_strategy BatchComputeEnvironment#allocation_strategy}.
        :param bid_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#bid_percentage BatchComputeEnvironment#bid_percentage}.
        :param desired_vcpus: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#desired_vcpus BatchComputeEnvironment#desired_vcpus}.
        :param ec2_configuration: ec2_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#ec2_configuration BatchComputeEnvironment#ec2_configuration}
        :param ec2_key_pair: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#ec2_key_pair BatchComputeEnvironment#ec2_key_pair}.
        :param image_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#image_id BatchComputeEnvironment#image_id}.
        :param instance_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#instance_role BatchComputeEnvironment#instance_role}.
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#instance_type BatchComputeEnvironment#instance_type}.
        :param launch_template: launch_template block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#launch_template BatchComputeEnvironment#launch_template}
        :param min_vcpus: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#min_vcpus BatchComputeEnvironment#min_vcpus}.
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#security_group_ids BatchComputeEnvironment#security_group_ids}.
        :param spot_iam_fleet_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#spot_iam_fleet_role BatchComputeEnvironment#spot_iam_fleet_role}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#tags BatchComputeEnvironment#tags}.
        '''
        if isinstance(ec2_configuration, dict):
            ec2_configuration = BatchComputeEnvironmentComputeResourcesEc2Configuration(**ec2_configuration)
        if isinstance(launch_template, dict):
            launch_template = BatchComputeEnvironmentComputeResourcesLaunchTemplate(**launch_template)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__978271b94dabe9354b8a1c5c390abedc76b1a389db1117467daf90bf94f1e28e)
            check_type(argname="argument max_vcpus", value=max_vcpus, expected_type=type_hints["max_vcpus"])
            check_type(argname="argument subnets", value=subnets, expected_type=type_hints["subnets"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument allocation_strategy", value=allocation_strategy, expected_type=type_hints["allocation_strategy"])
            check_type(argname="argument bid_percentage", value=bid_percentage, expected_type=type_hints["bid_percentage"])
            check_type(argname="argument desired_vcpus", value=desired_vcpus, expected_type=type_hints["desired_vcpus"])
            check_type(argname="argument ec2_configuration", value=ec2_configuration, expected_type=type_hints["ec2_configuration"])
            check_type(argname="argument ec2_key_pair", value=ec2_key_pair, expected_type=type_hints["ec2_key_pair"])
            check_type(argname="argument image_id", value=image_id, expected_type=type_hints["image_id"])
            check_type(argname="argument instance_role", value=instance_role, expected_type=type_hints["instance_role"])
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument launch_template", value=launch_template, expected_type=type_hints["launch_template"])
            check_type(argname="argument min_vcpus", value=min_vcpus, expected_type=type_hints["min_vcpus"])
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument spot_iam_fleet_role", value=spot_iam_fleet_role, expected_type=type_hints["spot_iam_fleet_role"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "max_vcpus": max_vcpus,
            "subnets": subnets,
            "type": type,
        }
        if allocation_strategy is not None:
            self._values["allocation_strategy"] = allocation_strategy
        if bid_percentage is not None:
            self._values["bid_percentage"] = bid_percentage
        if desired_vcpus is not None:
            self._values["desired_vcpus"] = desired_vcpus
        if ec2_configuration is not None:
            self._values["ec2_configuration"] = ec2_configuration
        if ec2_key_pair is not None:
            self._values["ec2_key_pair"] = ec2_key_pair
        if image_id is not None:
            self._values["image_id"] = image_id
        if instance_role is not None:
            self._values["instance_role"] = instance_role
        if instance_type is not None:
            self._values["instance_type"] = instance_type
        if launch_template is not None:
            self._values["launch_template"] = launch_template
        if min_vcpus is not None:
            self._values["min_vcpus"] = min_vcpus
        if security_group_ids is not None:
            self._values["security_group_ids"] = security_group_ids
        if spot_iam_fleet_role is not None:
            self._values["spot_iam_fleet_role"] = spot_iam_fleet_role
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def max_vcpus(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#max_vcpus BatchComputeEnvironment#max_vcpus}.'''
        result = self._values.get("max_vcpus")
        assert result is not None, "Required property 'max_vcpus' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def subnets(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#subnets BatchComputeEnvironment#subnets}.'''
        result = self._values.get("subnets")
        assert result is not None, "Required property 'subnets' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#type BatchComputeEnvironment#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allocation_strategy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#allocation_strategy BatchComputeEnvironment#allocation_strategy}.'''
        result = self._values.get("allocation_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bid_percentage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#bid_percentage BatchComputeEnvironment#bid_percentage}.'''
        result = self._values.get("bid_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def desired_vcpus(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#desired_vcpus BatchComputeEnvironment#desired_vcpus}.'''
        result = self._values.get("desired_vcpus")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ec2_configuration(
        self,
    ) -> typing.Optional["BatchComputeEnvironmentComputeResourcesEc2Configuration"]:
        '''ec2_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#ec2_configuration BatchComputeEnvironment#ec2_configuration}
        '''
        result = self._values.get("ec2_configuration")
        return typing.cast(typing.Optional["BatchComputeEnvironmentComputeResourcesEc2Configuration"], result)

    @builtins.property
    def ec2_key_pair(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#ec2_key_pair BatchComputeEnvironment#ec2_key_pair}.'''
        result = self._values.get("ec2_key_pair")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#image_id BatchComputeEnvironment#image_id}.'''
        result = self._values.get("image_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_role(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#instance_role BatchComputeEnvironment#instance_role}.'''
        result = self._values.get("instance_role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_type(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#instance_type BatchComputeEnvironment#instance_type}.'''
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def launch_template(
        self,
    ) -> typing.Optional["BatchComputeEnvironmentComputeResourcesLaunchTemplate"]:
        '''launch_template block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#launch_template BatchComputeEnvironment#launch_template}
        '''
        result = self._values.get("launch_template")
        return typing.cast(typing.Optional["BatchComputeEnvironmentComputeResourcesLaunchTemplate"], result)

    @builtins.property
    def min_vcpus(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#min_vcpus BatchComputeEnvironment#min_vcpus}.'''
        result = self._values.get("min_vcpus")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#security_group_ids BatchComputeEnvironment#security_group_ids}.'''
        result = self._values.get("security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def spot_iam_fleet_role(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#spot_iam_fleet_role BatchComputeEnvironment#spot_iam_fleet_role}.'''
        result = self._values.get("spot_iam_fleet_role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#tags BatchComputeEnvironment#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BatchComputeEnvironmentComputeResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.batchComputeEnvironment.BatchComputeEnvironmentComputeResourcesEc2Configuration",
    jsii_struct_bases=[],
    name_mapping={"image_id_override": "imageIdOverride", "image_type": "imageType"},
)
class BatchComputeEnvironmentComputeResourcesEc2Configuration:
    def __init__(
        self,
        *,
        image_id_override: typing.Optional[builtins.str] = None,
        image_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param image_id_override: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#image_id_override BatchComputeEnvironment#image_id_override}.
        :param image_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#image_type BatchComputeEnvironment#image_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4d1e8ddbf81dacc19fa5491900868be37787f4b2a3117da782578cf699fc029)
            check_type(argname="argument image_id_override", value=image_id_override, expected_type=type_hints["image_id_override"])
            check_type(argname="argument image_type", value=image_type, expected_type=type_hints["image_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if image_id_override is not None:
            self._values["image_id_override"] = image_id_override
        if image_type is not None:
            self._values["image_type"] = image_type

    @builtins.property
    def image_id_override(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#image_id_override BatchComputeEnvironment#image_id_override}.'''
        result = self._values.get("image_id_override")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#image_type BatchComputeEnvironment#image_type}.'''
        result = self._values.get("image_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BatchComputeEnvironmentComputeResourcesEc2Configuration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BatchComputeEnvironmentComputeResourcesEc2ConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.batchComputeEnvironment.BatchComputeEnvironmentComputeResourcesEc2ConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c4a15e686410029fd673bd4128d39ddab9bae59869705ad28796b880b658ed18)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetImageIdOverride")
    def reset_image_id_override(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImageIdOverride", []))

    @jsii.member(jsii_name="resetImageType")
    def reset_image_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImageType", []))

    @builtins.property
    @jsii.member(jsii_name="imageIdOverrideInput")
    def image_id_override_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageIdOverrideInput"))

    @builtins.property
    @jsii.member(jsii_name="imageTypeInput")
    def image_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="imageIdOverride")
    def image_id_override(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageIdOverride"))

    @image_id_override.setter
    def image_id_override(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ccd51b9de4e999a5a47e9be357d9cfd10ef0cb3e37a88a71224b9cfddd55117)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageIdOverride", value)

    @builtins.property
    @jsii.member(jsii_name="imageType")
    def image_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageType"))

    @image_type.setter
    def image_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__626cf56da5793cb6ae920b96231aa5edd4403a4e1d746ef0e438604667b649bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[BatchComputeEnvironmentComputeResourcesEc2Configuration]:
        return typing.cast(typing.Optional[BatchComputeEnvironmentComputeResourcesEc2Configuration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[BatchComputeEnvironmentComputeResourcesEc2Configuration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60564657a22269ce3ff116ebcf9c638e68cb30a69d52e2099cc9775343932c57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.batchComputeEnvironment.BatchComputeEnvironmentComputeResourcesLaunchTemplate",
    jsii_struct_bases=[],
    name_mapping={
        "launch_template_id": "launchTemplateId",
        "launch_template_name": "launchTemplateName",
        "version": "version",
    },
)
class BatchComputeEnvironmentComputeResourcesLaunchTemplate:
    def __init__(
        self,
        *,
        launch_template_id: typing.Optional[builtins.str] = None,
        launch_template_name: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param launch_template_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#launch_template_id BatchComputeEnvironment#launch_template_id}.
        :param launch_template_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#launch_template_name BatchComputeEnvironment#launch_template_name}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#version BatchComputeEnvironment#version}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8804298865ceccd347d27b18d644aae26edcbf3b20c38e5041bed0674ec6010c)
            check_type(argname="argument launch_template_id", value=launch_template_id, expected_type=type_hints["launch_template_id"])
            check_type(argname="argument launch_template_name", value=launch_template_name, expected_type=type_hints["launch_template_name"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if launch_template_id is not None:
            self._values["launch_template_id"] = launch_template_id
        if launch_template_name is not None:
            self._values["launch_template_name"] = launch_template_name
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def launch_template_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#launch_template_id BatchComputeEnvironment#launch_template_id}.'''
        result = self._values.get("launch_template_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def launch_template_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#launch_template_name BatchComputeEnvironment#launch_template_name}.'''
        result = self._values.get("launch_template_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#version BatchComputeEnvironment#version}.'''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BatchComputeEnvironmentComputeResourcesLaunchTemplate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BatchComputeEnvironmentComputeResourcesLaunchTemplateOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.batchComputeEnvironment.BatchComputeEnvironmentComputeResourcesLaunchTemplateOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cd94e61dfd05e853f21a088b72b12256259ba17eebe8be497dcc891c0895b7da)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetLaunchTemplateId")
    def reset_launch_template_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLaunchTemplateId", []))

    @jsii.member(jsii_name="resetLaunchTemplateName")
    def reset_launch_template_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLaunchTemplateName", []))

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

    @builtins.property
    @jsii.member(jsii_name="launchTemplateIdInput")
    def launch_template_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "launchTemplateIdInput"))

    @builtins.property
    @jsii.member(jsii_name="launchTemplateNameInput")
    def launch_template_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "launchTemplateNameInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="launchTemplateId")
    def launch_template_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "launchTemplateId"))

    @launch_template_id.setter
    def launch_template_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5a311a9566e94b7a495c2308bd39c3fdc447ff23a3eb3444d0a2bcad660886d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "launchTemplateId", value)

    @builtins.property
    @jsii.member(jsii_name="launchTemplateName")
    def launch_template_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "launchTemplateName"))

    @launch_template_name.setter
    def launch_template_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84d94cdd56449c72c35d52f08546bdb2d86ab2618b6fadc20ecd2ae21c6c99b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "launchTemplateName", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6bb218d5490fe823bd54254d3a75c128db79791f765c5f123f2da3e4e627cd76)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[BatchComputeEnvironmentComputeResourcesLaunchTemplate]:
        return typing.cast(typing.Optional[BatchComputeEnvironmentComputeResourcesLaunchTemplate], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[BatchComputeEnvironmentComputeResourcesLaunchTemplate],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db0a978da917576f1390850f2e1fd14629b58ef3ce2b102854dda282416a4391)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class BatchComputeEnvironmentComputeResourcesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.batchComputeEnvironment.BatchComputeEnvironmentComputeResourcesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__92669cd8381ad3876cdb12a954b8b383a5cf09602c7e87ee424419e4f421a103)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putEc2Configuration")
    def put_ec2_configuration(
        self,
        *,
        image_id_override: typing.Optional[builtins.str] = None,
        image_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param image_id_override: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#image_id_override BatchComputeEnvironment#image_id_override}.
        :param image_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#image_type BatchComputeEnvironment#image_type}.
        '''
        value = BatchComputeEnvironmentComputeResourcesEc2Configuration(
            image_id_override=image_id_override, image_type=image_type
        )

        return typing.cast(None, jsii.invoke(self, "putEc2Configuration", [value]))

    @jsii.member(jsii_name="putLaunchTemplate")
    def put_launch_template(
        self,
        *,
        launch_template_id: typing.Optional[builtins.str] = None,
        launch_template_name: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param launch_template_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#launch_template_id BatchComputeEnvironment#launch_template_id}.
        :param launch_template_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#launch_template_name BatchComputeEnvironment#launch_template_name}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#version BatchComputeEnvironment#version}.
        '''
        value = BatchComputeEnvironmentComputeResourcesLaunchTemplate(
            launch_template_id=launch_template_id,
            launch_template_name=launch_template_name,
            version=version,
        )

        return typing.cast(None, jsii.invoke(self, "putLaunchTemplate", [value]))

    @jsii.member(jsii_name="resetAllocationStrategy")
    def reset_allocation_strategy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllocationStrategy", []))

    @jsii.member(jsii_name="resetBidPercentage")
    def reset_bid_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBidPercentage", []))

    @jsii.member(jsii_name="resetDesiredVcpus")
    def reset_desired_vcpus(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDesiredVcpus", []))

    @jsii.member(jsii_name="resetEc2Configuration")
    def reset_ec2_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEc2Configuration", []))

    @jsii.member(jsii_name="resetEc2KeyPair")
    def reset_ec2_key_pair(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEc2KeyPair", []))

    @jsii.member(jsii_name="resetImageId")
    def reset_image_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImageId", []))

    @jsii.member(jsii_name="resetInstanceRole")
    def reset_instance_role(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceRole", []))

    @jsii.member(jsii_name="resetInstanceType")
    def reset_instance_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceType", []))

    @jsii.member(jsii_name="resetLaunchTemplate")
    def reset_launch_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLaunchTemplate", []))

    @jsii.member(jsii_name="resetMinVcpus")
    def reset_min_vcpus(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinVcpus", []))

    @jsii.member(jsii_name="resetSecurityGroupIds")
    def reset_security_group_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityGroupIds", []))

    @jsii.member(jsii_name="resetSpotIamFleetRole")
    def reset_spot_iam_fleet_role(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpotIamFleetRole", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @builtins.property
    @jsii.member(jsii_name="ec2Configuration")
    def ec2_configuration(
        self,
    ) -> BatchComputeEnvironmentComputeResourcesEc2ConfigurationOutputReference:
        return typing.cast(BatchComputeEnvironmentComputeResourcesEc2ConfigurationOutputReference, jsii.get(self, "ec2Configuration"))

    @builtins.property
    @jsii.member(jsii_name="launchTemplate")
    def launch_template(
        self,
    ) -> BatchComputeEnvironmentComputeResourcesLaunchTemplateOutputReference:
        return typing.cast(BatchComputeEnvironmentComputeResourcesLaunchTemplateOutputReference, jsii.get(self, "launchTemplate"))

    @builtins.property
    @jsii.member(jsii_name="allocationStrategyInput")
    def allocation_strategy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "allocationStrategyInput"))

    @builtins.property
    @jsii.member(jsii_name="bidPercentageInput")
    def bid_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bidPercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="desiredVcpusInput")
    def desired_vcpus_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "desiredVcpusInput"))

    @builtins.property
    @jsii.member(jsii_name="ec2ConfigurationInput")
    def ec2_configuration_input(
        self,
    ) -> typing.Optional[BatchComputeEnvironmentComputeResourcesEc2Configuration]:
        return typing.cast(typing.Optional[BatchComputeEnvironmentComputeResourcesEc2Configuration], jsii.get(self, "ec2ConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="ec2KeyPairInput")
    def ec2_key_pair_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ec2KeyPairInput"))

    @builtins.property
    @jsii.member(jsii_name="imageIdInput")
    def image_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageIdInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceRoleInput")
    def instance_role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceRoleInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceTypeInput")
    def instance_type_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "instanceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="launchTemplateInput")
    def launch_template_input(
        self,
    ) -> typing.Optional[BatchComputeEnvironmentComputeResourcesLaunchTemplate]:
        return typing.cast(typing.Optional[BatchComputeEnvironmentComputeResourcesLaunchTemplate], jsii.get(self, "launchTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="maxVcpusInput")
    def max_vcpus_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxVcpusInput"))

    @builtins.property
    @jsii.member(jsii_name="minVcpusInput")
    def min_vcpus_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minVcpusInput"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupIdsInput")
    def security_group_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="spotIamFleetRoleInput")
    def spot_iam_fleet_role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "spotIamFleetRoleInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetsInput")
    def subnets_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetsInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="allocationStrategy")
    def allocation_strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "allocationStrategy"))

    @allocation_strategy.setter
    def allocation_strategy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5017501dd55ef0857461150e2f0656966cb8348ef2bc4e1f56cc6e5437e5a5b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allocationStrategy", value)

    @builtins.property
    @jsii.member(jsii_name="bidPercentage")
    def bid_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bidPercentage"))

    @bid_percentage.setter
    def bid_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31742e1853b05afd9bb858eca021721982fa9ce510925bbe3c94a27e94f653c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bidPercentage", value)

    @builtins.property
    @jsii.member(jsii_name="desiredVcpus")
    def desired_vcpus(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "desiredVcpus"))

    @desired_vcpus.setter
    def desired_vcpus(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc69c11415e85cfe19e4ceb8b1286f25aa438a7a39ed90ebf1dd0d8a26c3279c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "desiredVcpus", value)

    @builtins.property
    @jsii.member(jsii_name="ec2KeyPair")
    def ec2_key_pair(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ec2KeyPair"))

    @ec2_key_pair.setter
    def ec2_key_pair(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f26a5ff9ea506f9e4219e4d94954fcafcb92340ab96ffafac4901580b625382)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ec2KeyPair", value)

    @builtins.property
    @jsii.member(jsii_name="imageId")
    def image_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageId"))

    @image_id.setter
    def image_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20c76fe1043217034ecd35bb4e4f07c1af3d7cd13c7de7068eec7f99c9cc1d28)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageId", value)

    @builtins.property
    @jsii.member(jsii_name="instanceRole")
    def instance_role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceRole"))

    @instance_role.setter
    def instance_role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3038f17f77a478a32af13f9f42406796a95ee18b0d1541cb974417fc7c805087)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceRole", value)

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c8901e9cdef9d95c3a37146aa007d84003dab434a92fd2a29c637d9c8ed88e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value)

    @builtins.property
    @jsii.member(jsii_name="maxVcpus")
    def max_vcpus(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxVcpus"))

    @max_vcpus.setter
    def max_vcpus(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13d34de2cc8c66f09d41293ae98dedd028e80fe8fc5f3ba7c063e7a3ca23a4d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxVcpus", value)

    @builtins.property
    @jsii.member(jsii_name="minVcpus")
    def min_vcpus(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minVcpus"))

    @min_vcpus.setter
    def min_vcpus(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aef6095c8226ae446df7cc3a9eeffe010fbe766e7213f8695258bfc78759d07e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minVcpus", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82f5fe7bfbf060f1eebcc78c13f2fb1aeffebd01fa8b32f12fad3a3799e96b15)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="spotIamFleetRole")
    def spot_iam_fleet_role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "spotIamFleetRole"))

    @spot_iam_fleet_role.setter
    def spot_iam_fleet_role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5148eaed4f34cf69841ce255f7163220e851bfdbad6bb86748eb8cce547e364)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spotIamFleetRole", value)

    @builtins.property
    @jsii.member(jsii_name="subnets")
    def subnets(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnets"))

    @subnets.setter
    def subnets(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82951e9284ebdc3d4c0d2c22124ed60cb80cc24bbf544851e7165dfa8b169e9d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnets", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__434fb5637f6ad9e0bf2a5e56900cf3b6b16639b4861248cbf7d76bd40be88ead)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b7d4b33016a9ff2fb3fcf912dc631e6b7ce3f12e5d3f1f5980981cf0ae2d917)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[BatchComputeEnvironmentComputeResources]:
        return typing.cast(typing.Optional[BatchComputeEnvironmentComputeResources], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[BatchComputeEnvironmentComputeResources],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__463efa1b30491dc5f1bce0eec7c456f12c1c63d2c49d1b3897f6352772ac93f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.batchComputeEnvironment.BatchComputeEnvironmentConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "type": "type",
        "compute_environment_name": "computeEnvironmentName",
        "compute_environment_name_prefix": "computeEnvironmentNamePrefix",
        "compute_resources": "computeResources",
        "eks_configuration": "eksConfiguration",
        "id": "id",
        "service_role": "serviceRole",
        "state": "state",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class BatchComputeEnvironmentConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        type: builtins.str,
        compute_environment_name: typing.Optional[builtins.str] = None,
        compute_environment_name_prefix: typing.Optional[builtins.str] = None,
        compute_resources: typing.Optional[typing.Union[BatchComputeEnvironmentComputeResources, typing.Dict[builtins.str, typing.Any]]] = None,
        eks_configuration: typing.Optional[typing.Union["BatchComputeEnvironmentEksConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        service_role: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
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
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#type BatchComputeEnvironment#type}.
        :param compute_environment_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#compute_environment_name BatchComputeEnvironment#compute_environment_name}.
        :param compute_environment_name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#compute_environment_name_prefix BatchComputeEnvironment#compute_environment_name_prefix}.
        :param compute_resources: compute_resources block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#compute_resources BatchComputeEnvironment#compute_resources}
        :param eks_configuration: eks_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#eks_configuration BatchComputeEnvironment#eks_configuration}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#id BatchComputeEnvironment#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param service_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#service_role BatchComputeEnvironment#service_role}.
        :param state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#state BatchComputeEnvironment#state}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#tags BatchComputeEnvironment#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#tags_all BatchComputeEnvironment#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(compute_resources, dict):
            compute_resources = BatchComputeEnvironmentComputeResources(**compute_resources)
        if isinstance(eks_configuration, dict):
            eks_configuration = BatchComputeEnvironmentEksConfiguration(**eks_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab188b4fa70309f2527aa327e6a601e936e890f16275efe027baa47f14cfd489)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument compute_environment_name", value=compute_environment_name, expected_type=type_hints["compute_environment_name"])
            check_type(argname="argument compute_environment_name_prefix", value=compute_environment_name_prefix, expected_type=type_hints["compute_environment_name_prefix"])
            check_type(argname="argument compute_resources", value=compute_resources, expected_type=type_hints["compute_resources"])
            check_type(argname="argument eks_configuration", value=eks_configuration, expected_type=type_hints["eks_configuration"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument service_role", value=service_role, expected_type=type_hints["service_role"])
            check_type(argname="argument state", value=state, expected_type=type_hints["state"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
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
        if compute_environment_name is not None:
            self._values["compute_environment_name"] = compute_environment_name
        if compute_environment_name_prefix is not None:
            self._values["compute_environment_name_prefix"] = compute_environment_name_prefix
        if compute_resources is not None:
            self._values["compute_resources"] = compute_resources
        if eks_configuration is not None:
            self._values["eks_configuration"] = eks_configuration
        if id is not None:
            self._values["id"] = id
        if service_role is not None:
            self._values["service_role"] = service_role
        if state is not None:
            self._values["state"] = state
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
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#type BatchComputeEnvironment#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def compute_environment_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#compute_environment_name BatchComputeEnvironment#compute_environment_name}.'''
        result = self._values.get("compute_environment_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def compute_environment_name_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#compute_environment_name_prefix BatchComputeEnvironment#compute_environment_name_prefix}.'''
        result = self._values.get("compute_environment_name_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def compute_resources(
        self,
    ) -> typing.Optional[BatchComputeEnvironmentComputeResources]:
        '''compute_resources block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#compute_resources BatchComputeEnvironment#compute_resources}
        '''
        result = self._values.get("compute_resources")
        return typing.cast(typing.Optional[BatchComputeEnvironmentComputeResources], result)

    @builtins.property
    def eks_configuration(
        self,
    ) -> typing.Optional["BatchComputeEnvironmentEksConfiguration"]:
        '''eks_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#eks_configuration BatchComputeEnvironment#eks_configuration}
        '''
        result = self._values.get("eks_configuration")
        return typing.cast(typing.Optional["BatchComputeEnvironmentEksConfiguration"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#id BatchComputeEnvironment#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_role(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#service_role BatchComputeEnvironment#service_role}.'''
        result = self._values.get("service_role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def state(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#state BatchComputeEnvironment#state}.'''
        result = self._values.get("state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#tags BatchComputeEnvironment#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#tags_all BatchComputeEnvironment#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BatchComputeEnvironmentConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.batchComputeEnvironment.BatchComputeEnvironmentEksConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "eks_cluster_arn": "eksClusterArn",
        "kubernetes_namespace": "kubernetesNamespace",
    },
)
class BatchComputeEnvironmentEksConfiguration:
    def __init__(
        self,
        *,
        eks_cluster_arn: builtins.str,
        kubernetes_namespace: builtins.str,
    ) -> None:
        '''
        :param eks_cluster_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#eks_cluster_arn BatchComputeEnvironment#eks_cluster_arn}.
        :param kubernetes_namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#kubernetes_namespace BatchComputeEnvironment#kubernetes_namespace}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbb93b7327237ad51b6163989024d7ba0f2b8c5e4d9650a46577fc7b31922bb0)
            check_type(argname="argument eks_cluster_arn", value=eks_cluster_arn, expected_type=type_hints["eks_cluster_arn"])
            check_type(argname="argument kubernetes_namespace", value=kubernetes_namespace, expected_type=type_hints["kubernetes_namespace"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "eks_cluster_arn": eks_cluster_arn,
            "kubernetes_namespace": kubernetes_namespace,
        }

    @builtins.property
    def eks_cluster_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#eks_cluster_arn BatchComputeEnvironment#eks_cluster_arn}.'''
        result = self._values.get("eks_cluster_arn")
        assert result is not None, "Required property 'eks_cluster_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def kubernetes_namespace(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/batch_compute_environment#kubernetes_namespace BatchComputeEnvironment#kubernetes_namespace}.'''
        result = self._values.get("kubernetes_namespace")
        assert result is not None, "Required property 'kubernetes_namespace' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BatchComputeEnvironmentEksConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BatchComputeEnvironmentEksConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.batchComputeEnvironment.BatchComputeEnvironmentEksConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7bd626317d574cfa0e88fee3c2ac152808f9dbc5198ca272504d4c09b1a6c495)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="eksClusterArnInput")
    def eks_cluster_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eksClusterArnInput"))

    @builtins.property
    @jsii.member(jsii_name="kubernetesNamespaceInput")
    def kubernetes_namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kubernetesNamespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="eksClusterArn")
    def eks_cluster_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eksClusterArn"))

    @eks_cluster_arn.setter
    def eks_cluster_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b62d6f8f0b76aa50c268d47e579f2c857ab619c917c6408e9e646017f51c5af7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eksClusterArn", value)

    @builtins.property
    @jsii.member(jsii_name="kubernetesNamespace")
    def kubernetes_namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kubernetesNamespace"))

    @kubernetes_namespace.setter
    def kubernetes_namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7e97135578b45b965013a238b844e31f989e37a75b41f4f5bb034ef2142fba4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kubernetesNamespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[BatchComputeEnvironmentEksConfiguration]:
        return typing.cast(typing.Optional[BatchComputeEnvironmentEksConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[BatchComputeEnvironmentEksConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__691e11f900e220db72f114beca1948bceeaebd10acb3d313d6c2d0cc0c98d727)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "BatchComputeEnvironment",
    "BatchComputeEnvironmentComputeResources",
    "BatchComputeEnvironmentComputeResourcesEc2Configuration",
    "BatchComputeEnvironmentComputeResourcesEc2ConfigurationOutputReference",
    "BatchComputeEnvironmentComputeResourcesLaunchTemplate",
    "BatchComputeEnvironmentComputeResourcesLaunchTemplateOutputReference",
    "BatchComputeEnvironmentComputeResourcesOutputReference",
    "BatchComputeEnvironmentConfig",
    "BatchComputeEnvironmentEksConfiguration",
    "BatchComputeEnvironmentEksConfigurationOutputReference",
]

publication.publish()

def _typecheckingstub__99a336e293fc81503d25c2fb7504768001e8ffa105f343b79b8154be862c0fb7(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    type: builtins.str,
    compute_environment_name: typing.Optional[builtins.str] = None,
    compute_environment_name_prefix: typing.Optional[builtins.str] = None,
    compute_resources: typing.Optional[typing.Union[BatchComputeEnvironmentComputeResources, typing.Dict[builtins.str, typing.Any]]] = None,
    eks_configuration: typing.Optional[typing.Union[BatchComputeEnvironmentEksConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    service_role: typing.Optional[builtins.str] = None,
    state: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__e9dddd54195eab8d2b22b4684fc217f5166ede7f5443ca05e4638699fd6743c0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72358f6cb10e41fd73e6c3b8cbea6abd6b8b64dce579b6ec6ed84506d5f53727(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37bb5bb45d5931b8d3b20c3ddef9eed9791c86bb7c0668582f116527a9fa8323(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2213080914d7ba80a00d26fbff933ed5c3a5aea874079fac54cd81c36666b994(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62c129d3e7309a68d0b6e41e736ef2b71f32b7a774621fc510a7809a1f965236(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__543838d3ff5567fbe59e55c96c0469ea59388e56b5f023e750450d297977ed7c(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29d9170043646a1d227edcc1396b490b212814b38d11db118d36d73b41dd400c(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64bcf9a13708b346fe9450881002d7494c1230a85f2ed25588f4d0d87ddc6336(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__978271b94dabe9354b8a1c5c390abedc76b1a389db1117467daf90bf94f1e28e(
    *,
    max_vcpus: jsii.Number,
    subnets: typing.Sequence[builtins.str],
    type: builtins.str,
    allocation_strategy: typing.Optional[builtins.str] = None,
    bid_percentage: typing.Optional[jsii.Number] = None,
    desired_vcpus: typing.Optional[jsii.Number] = None,
    ec2_configuration: typing.Optional[typing.Union[BatchComputeEnvironmentComputeResourcesEc2Configuration, typing.Dict[builtins.str, typing.Any]]] = None,
    ec2_key_pair: typing.Optional[builtins.str] = None,
    image_id: typing.Optional[builtins.str] = None,
    instance_role: typing.Optional[builtins.str] = None,
    instance_type: typing.Optional[typing.Sequence[builtins.str]] = None,
    launch_template: typing.Optional[typing.Union[BatchComputeEnvironmentComputeResourcesLaunchTemplate, typing.Dict[builtins.str, typing.Any]]] = None,
    min_vcpus: typing.Optional[jsii.Number] = None,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    spot_iam_fleet_role: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4d1e8ddbf81dacc19fa5491900868be37787f4b2a3117da782578cf699fc029(
    *,
    image_id_override: typing.Optional[builtins.str] = None,
    image_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4a15e686410029fd673bd4128d39ddab9bae59869705ad28796b880b658ed18(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ccd51b9de4e999a5a47e9be357d9cfd10ef0cb3e37a88a71224b9cfddd55117(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__626cf56da5793cb6ae920b96231aa5edd4403a4e1d746ef0e438604667b649bb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60564657a22269ce3ff116ebcf9c638e68cb30a69d52e2099cc9775343932c57(
    value: typing.Optional[BatchComputeEnvironmentComputeResourcesEc2Configuration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8804298865ceccd347d27b18d644aae26edcbf3b20c38e5041bed0674ec6010c(
    *,
    launch_template_id: typing.Optional[builtins.str] = None,
    launch_template_name: typing.Optional[builtins.str] = None,
    version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd94e61dfd05e853f21a088b72b12256259ba17eebe8be497dcc891c0895b7da(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5a311a9566e94b7a495c2308bd39c3fdc447ff23a3eb3444d0a2bcad660886d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84d94cdd56449c72c35d52f08546bdb2d86ab2618b6fadc20ecd2ae21c6c99b6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bb218d5490fe823bd54254d3a75c128db79791f765c5f123f2da3e4e627cd76(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db0a978da917576f1390850f2e1fd14629b58ef3ce2b102854dda282416a4391(
    value: typing.Optional[BatchComputeEnvironmentComputeResourcesLaunchTemplate],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92669cd8381ad3876cdb12a954b8b383a5cf09602c7e87ee424419e4f421a103(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5017501dd55ef0857461150e2f0656966cb8348ef2bc4e1f56cc6e5437e5a5b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31742e1853b05afd9bb858eca021721982fa9ce510925bbe3c94a27e94f653c0(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc69c11415e85cfe19e4ceb8b1286f25aa438a7a39ed90ebf1dd0d8a26c3279c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f26a5ff9ea506f9e4219e4d94954fcafcb92340ab96ffafac4901580b625382(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20c76fe1043217034ecd35bb4e4f07c1af3d7cd13c7de7068eec7f99c9cc1d28(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3038f17f77a478a32af13f9f42406796a95ee18b0d1541cb974417fc7c805087(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c8901e9cdef9d95c3a37146aa007d84003dab434a92fd2a29c637d9c8ed88e6(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13d34de2cc8c66f09d41293ae98dedd028e80fe8fc5f3ba7c063e7a3ca23a4d5(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aef6095c8226ae446df7cc3a9eeffe010fbe766e7213f8695258bfc78759d07e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82f5fe7bfbf060f1eebcc78c13f2fb1aeffebd01fa8b32f12fad3a3799e96b15(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5148eaed4f34cf69841ce255f7163220e851bfdbad6bb86748eb8cce547e364(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82951e9284ebdc3d4c0d2c22124ed60cb80cc24bbf544851e7165dfa8b169e9d(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__434fb5637f6ad9e0bf2a5e56900cf3b6b16639b4861248cbf7d76bd40be88ead(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b7d4b33016a9ff2fb3fcf912dc631e6b7ce3f12e5d3f1f5980981cf0ae2d917(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__463efa1b30491dc5f1bce0eec7c456f12c1c63d2c49d1b3897f6352772ac93f4(
    value: typing.Optional[BatchComputeEnvironmentComputeResources],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab188b4fa70309f2527aa327e6a601e936e890f16275efe027baa47f14cfd489(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    type: builtins.str,
    compute_environment_name: typing.Optional[builtins.str] = None,
    compute_environment_name_prefix: typing.Optional[builtins.str] = None,
    compute_resources: typing.Optional[typing.Union[BatchComputeEnvironmentComputeResources, typing.Dict[builtins.str, typing.Any]]] = None,
    eks_configuration: typing.Optional[typing.Union[BatchComputeEnvironmentEksConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    service_role: typing.Optional[builtins.str] = None,
    state: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbb93b7327237ad51b6163989024d7ba0f2b8c5e4d9650a46577fc7b31922bb0(
    *,
    eks_cluster_arn: builtins.str,
    kubernetes_namespace: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7bd626317d574cfa0e88fee3c2ac152808f9dbc5198ca272504d4c09b1a6c495(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b62d6f8f0b76aa50c268d47e579f2c857ab619c917c6408e9e646017f51c5af7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7e97135578b45b965013a238b844e31f989e37a75b41f4f5bb034ef2142fba4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__691e11f900e220db72f114beca1948bceeaebd10acb3d313d6c2d0cc0c98d727(
    value: typing.Optional[BatchComputeEnvironmentEksConfiguration],
) -> None:
    """Type checking stubs"""
    pass
