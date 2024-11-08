'''
# `aws_macie2_classification_job`

Refer to the Terraform Registory for docs: [`aws_macie2_classification_job`](https://www.terraform.io/docs/providers/aws/r/macie2_classification_job).
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


class Macie2ClassificationJob(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJob",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job aws_macie2_classification_job}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        job_type: builtins.str,
        s3_job_definition: typing.Union["Macie2ClassificationJobS3JobDefinition", typing.Dict[builtins.str, typing.Any]],
        custom_data_identifier_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        initial_run: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        job_status: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        name_prefix: typing.Optional[builtins.str] = None,
        sampling_percentage: typing.Optional[jsii.Number] = None,
        schedule_frequency: typing.Optional[typing.Union["Macie2ClassificationJobScheduleFrequency", typing.Dict[builtins.str, typing.Any]]] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job aws_macie2_classification_job} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param job_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#job_type Macie2ClassificationJob#job_type}.
        :param s3_job_definition: s3_job_definition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#s3_job_definition Macie2ClassificationJob#s3_job_definition}
        :param custom_data_identifier_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#custom_data_identifier_ids Macie2ClassificationJob#custom_data_identifier_ids}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#description Macie2ClassificationJob#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#id Macie2ClassificationJob#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param initial_run: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#initial_run Macie2ClassificationJob#initial_run}.
        :param job_status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#job_status Macie2ClassificationJob#job_status}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#name Macie2ClassificationJob#name}.
        :param name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#name_prefix Macie2ClassificationJob#name_prefix}.
        :param sampling_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#sampling_percentage Macie2ClassificationJob#sampling_percentage}.
        :param schedule_frequency: schedule_frequency block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#schedule_frequency Macie2ClassificationJob#schedule_frequency}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tags Macie2ClassificationJob#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tags_all Macie2ClassificationJob#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c60608cdd135982815c6aead769e77b1a2c641a6ea5b15189cd07728a81f4d4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = Macie2ClassificationJobConfig(
            job_type=job_type,
            s3_job_definition=s3_job_definition,
            custom_data_identifier_ids=custom_data_identifier_ids,
            description=description,
            id=id,
            initial_run=initial_run,
            job_status=job_status,
            name=name,
            name_prefix=name_prefix,
            sampling_percentage=sampling_percentage,
            schedule_frequency=schedule_frequency,
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

    @jsii.member(jsii_name="putS3JobDefinition")
    def put_s3_job_definition(
        self,
        *,
        bucket_criteria: typing.Optional[typing.Union["Macie2ClassificationJobS3JobDefinitionBucketCriteria", typing.Dict[builtins.str, typing.Any]]] = None,
        bucket_definitions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["Macie2ClassificationJobS3JobDefinitionBucketDefinitions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        scoping: typing.Optional[typing.Union["Macie2ClassificationJobS3JobDefinitionScoping", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param bucket_criteria: bucket_criteria block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#bucket_criteria Macie2ClassificationJob#bucket_criteria}
        :param bucket_definitions: bucket_definitions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#bucket_definitions Macie2ClassificationJob#bucket_definitions}
        :param scoping: scoping block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#scoping Macie2ClassificationJob#scoping}
        '''
        value = Macie2ClassificationJobS3JobDefinition(
            bucket_criteria=bucket_criteria,
            bucket_definitions=bucket_definitions,
            scoping=scoping,
        )

        return typing.cast(None, jsii.invoke(self, "putS3JobDefinition", [value]))

    @jsii.member(jsii_name="putScheduleFrequency")
    def put_schedule_frequency(
        self,
        *,
        daily_schedule: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        monthly_schedule: typing.Optional[jsii.Number] = None,
        weekly_schedule: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param daily_schedule: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#daily_schedule Macie2ClassificationJob#daily_schedule}.
        :param monthly_schedule: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#monthly_schedule Macie2ClassificationJob#monthly_schedule}.
        :param weekly_schedule: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#weekly_schedule Macie2ClassificationJob#weekly_schedule}.
        '''
        value = Macie2ClassificationJobScheduleFrequency(
            daily_schedule=daily_schedule,
            monthly_schedule=monthly_schedule,
            weekly_schedule=weekly_schedule,
        )

        return typing.cast(None, jsii.invoke(self, "putScheduleFrequency", [value]))

    @jsii.member(jsii_name="resetCustomDataIdentifierIds")
    def reset_custom_data_identifier_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomDataIdentifierIds", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInitialRun")
    def reset_initial_run(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitialRun", []))

    @jsii.member(jsii_name="resetJobStatus")
    def reset_job_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJobStatus", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamePrefix")
    def reset_name_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamePrefix", []))

    @jsii.member(jsii_name="resetSamplingPercentage")
    def reset_sampling_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSamplingPercentage", []))

    @jsii.member(jsii_name="resetScheduleFrequency")
    def reset_schedule_frequency(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScheduleFrequency", []))

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
    @jsii.member(jsii_name="createdAt")
    def created_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdAt"))

    @builtins.property
    @jsii.member(jsii_name="jobArn")
    def job_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jobArn"))

    @builtins.property
    @jsii.member(jsii_name="jobId")
    def job_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jobId"))

    @builtins.property
    @jsii.member(jsii_name="s3JobDefinition")
    def s3_job_definition(
        self,
    ) -> "Macie2ClassificationJobS3JobDefinitionOutputReference":
        return typing.cast("Macie2ClassificationJobS3JobDefinitionOutputReference", jsii.get(self, "s3JobDefinition"))

    @builtins.property
    @jsii.member(jsii_name="scheduleFrequency")
    def schedule_frequency(
        self,
    ) -> "Macie2ClassificationJobScheduleFrequencyOutputReference":
        return typing.cast("Macie2ClassificationJobScheduleFrequencyOutputReference", jsii.get(self, "scheduleFrequency"))

    @builtins.property
    @jsii.member(jsii_name="userPausedDetails")
    def user_paused_details(self) -> "Macie2ClassificationJobUserPausedDetailsList":
        return typing.cast("Macie2ClassificationJobUserPausedDetailsList", jsii.get(self, "userPausedDetails"))

    @builtins.property
    @jsii.member(jsii_name="customDataIdentifierIdsInput")
    def custom_data_identifier_ids_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "customDataIdentifierIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="initialRunInput")
    def initial_run_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "initialRunInput"))

    @builtins.property
    @jsii.member(jsii_name="jobStatusInput")
    def job_status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jobStatusInput"))

    @builtins.property
    @jsii.member(jsii_name="jobTypeInput")
    def job_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jobTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namePrefixInput")
    def name_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namePrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="s3JobDefinitionInput")
    def s3_job_definition_input(
        self,
    ) -> typing.Optional["Macie2ClassificationJobS3JobDefinition"]:
        return typing.cast(typing.Optional["Macie2ClassificationJobS3JobDefinition"], jsii.get(self, "s3JobDefinitionInput"))

    @builtins.property
    @jsii.member(jsii_name="samplingPercentageInput")
    def sampling_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "samplingPercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduleFrequencyInput")
    def schedule_frequency_input(
        self,
    ) -> typing.Optional["Macie2ClassificationJobScheduleFrequency"]:
        return typing.cast(typing.Optional["Macie2ClassificationJobScheduleFrequency"], jsii.get(self, "scheduleFrequencyInput"))

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
    @jsii.member(jsii_name="customDataIdentifierIds")
    def custom_data_identifier_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "customDataIdentifierIds"))

    @custom_data_identifier_ids.setter
    def custom_data_identifier_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__246db55292490e495687a674321e3a4ab8cc2e9ad105efe5d832f9aea48c0987)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customDataIdentifierIds", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__566543b99f28defde976a8123bc284500b953814d089b5be1d929ccc2eeaf8cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__812c557f42398edd1275b4d28d58bc992dfb745aebbbbe8329d8c7b81d5cf88e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="initialRun")
    def initial_run(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "initialRun"))

    @initial_run.setter
    def initial_run(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ea1a93ca9d9feae381ed91d0725247c3afe482a637c400871806e994c7f37d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initialRun", value)

    @builtins.property
    @jsii.member(jsii_name="jobStatus")
    def job_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jobStatus"))

    @job_status.setter
    def job_status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a93468f4a7bfca255e5a0c6a504d141286a0161de45b00104b6230400ad8be0e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobStatus", value)

    @builtins.property
    @jsii.member(jsii_name="jobType")
    def job_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jobType"))

    @job_type.setter
    def job_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34b98ab1d4aa35157626bbb44e1e4c0b16a7cc0ac61f5747627289747a6cba06)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobType", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4538d1d9abd5c8d9e1474541bac86a51b3f0a3298effbf3bb87f265bf0f4197)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namePrefix")
    def name_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namePrefix"))

    @name_prefix.setter
    def name_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__096253b063d628cbab50b72c6e89d665580a2b9f519f0f0961388a0f0aada687)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namePrefix", value)

    @builtins.property
    @jsii.member(jsii_name="samplingPercentage")
    def sampling_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "samplingPercentage"))

    @sampling_percentage.setter
    def sampling_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4db7c4d101b5d9873a97b2457a0c4e40c3988290f00bd37a7cbbabe8b765f3c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "samplingPercentage", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40990567144066848d837796118c240980f4d58ab1f12a12ecbb3aa187d6a231)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4dc087767d1c78cb56e8bc404a5f2c3394738e61c97b619d2e635782d1e13f95)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "job_type": "jobType",
        "s3_job_definition": "s3JobDefinition",
        "custom_data_identifier_ids": "customDataIdentifierIds",
        "description": "description",
        "id": "id",
        "initial_run": "initialRun",
        "job_status": "jobStatus",
        "name": "name",
        "name_prefix": "namePrefix",
        "sampling_percentage": "samplingPercentage",
        "schedule_frequency": "scheduleFrequency",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class Macie2ClassificationJobConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        job_type: builtins.str,
        s3_job_definition: typing.Union["Macie2ClassificationJobS3JobDefinition", typing.Dict[builtins.str, typing.Any]],
        custom_data_identifier_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        initial_run: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        job_status: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        name_prefix: typing.Optional[builtins.str] = None,
        sampling_percentage: typing.Optional[jsii.Number] = None,
        schedule_frequency: typing.Optional[typing.Union["Macie2ClassificationJobScheduleFrequency", typing.Dict[builtins.str, typing.Any]]] = None,
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
        :param job_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#job_type Macie2ClassificationJob#job_type}.
        :param s3_job_definition: s3_job_definition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#s3_job_definition Macie2ClassificationJob#s3_job_definition}
        :param custom_data_identifier_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#custom_data_identifier_ids Macie2ClassificationJob#custom_data_identifier_ids}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#description Macie2ClassificationJob#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#id Macie2ClassificationJob#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param initial_run: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#initial_run Macie2ClassificationJob#initial_run}.
        :param job_status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#job_status Macie2ClassificationJob#job_status}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#name Macie2ClassificationJob#name}.
        :param name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#name_prefix Macie2ClassificationJob#name_prefix}.
        :param sampling_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#sampling_percentage Macie2ClassificationJob#sampling_percentage}.
        :param schedule_frequency: schedule_frequency block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#schedule_frequency Macie2ClassificationJob#schedule_frequency}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tags Macie2ClassificationJob#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tags_all Macie2ClassificationJob#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(s3_job_definition, dict):
            s3_job_definition = Macie2ClassificationJobS3JobDefinition(**s3_job_definition)
        if isinstance(schedule_frequency, dict):
            schedule_frequency = Macie2ClassificationJobScheduleFrequency(**schedule_frequency)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68d84991a1ca5cfa5330567874a105f9c96eec75fa5ac4348173f37215a1ab29)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument job_type", value=job_type, expected_type=type_hints["job_type"])
            check_type(argname="argument s3_job_definition", value=s3_job_definition, expected_type=type_hints["s3_job_definition"])
            check_type(argname="argument custom_data_identifier_ids", value=custom_data_identifier_ids, expected_type=type_hints["custom_data_identifier_ids"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument initial_run", value=initial_run, expected_type=type_hints["initial_run"])
            check_type(argname="argument job_status", value=job_status, expected_type=type_hints["job_status"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument name_prefix", value=name_prefix, expected_type=type_hints["name_prefix"])
            check_type(argname="argument sampling_percentage", value=sampling_percentage, expected_type=type_hints["sampling_percentage"])
            check_type(argname="argument schedule_frequency", value=schedule_frequency, expected_type=type_hints["schedule_frequency"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "job_type": job_type,
            "s3_job_definition": s3_job_definition,
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
        if custom_data_identifier_ids is not None:
            self._values["custom_data_identifier_ids"] = custom_data_identifier_ids
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if initial_run is not None:
            self._values["initial_run"] = initial_run
        if job_status is not None:
            self._values["job_status"] = job_status
        if name is not None:
            self._values["name"] = name
        if name_prefix is not None:
            self._values["name_prefix"] = name_prefix
        if sampling_percentage is not None:
            self._values["sampling_percentage"] = sampling_percentage
        if schedule_frequency is not None:
            self._values["schedule_frequency"] = schedule_frequency
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
    def job_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#job_type Macie2ClassificationJob#job_type}.'''
        result = self._values.get("job_type")
        assert result is not None, "Required property 'job_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def s3_job_definition(self) -> "Macie2ClassificationJobS3JobDefinition":
        '''s3_job_definition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#s3_job_definition Macie2ClassificationJob#s3_job_definition}
        '''
        result = self._values.get("s3_job_definition")
        assert result is not None, "Required property 's3_job_definition' is missing"
        return typing.cast("Macie2ClassificationJobS3JobDefinition", result)

    @builtins.property
    def custom_data_identifier_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#custom_data_identifier_ids Macie2ClassificationJob#custom_data_identifier_ids}.'''
        result = self._values.get("custom_data_identifier_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#description Macie2ClassificationJob#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#id Macie2ClassificationJob#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def initial_run(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#initial_run Macie2ClassificationJob#initial_run}.'''
        result = self._values.get("initial_run")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def job_status(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#job_status Macie2ClassificationJob#job_status}.'''
        result = self._values.get("job_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#name Macie2ClassificationJob#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#name_prefix Macie2ClassificationJob#name_prefix}.'''
        result = self._values.get("name_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sampling_percentage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#sampling_percentage Macie2ClassificationJob#sampling_percentage}.'''
        result = self._values.get("sampling_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def schedule_frequency(
        self,
    ) -> typing.Optional["Macie2ClassificationJobScheduleFrequency"]:
        '''schedule_frequency block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#schedule_frequency Macie2ClassificationJob#schedule_frequency}
        '''
        result = self._values.get("schedule_frequency")
        return typing.cast(typing.Optional["Macie2ClassificationJobScheduleFrequency"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tags Macie2ClassificationJob#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tags_all Macie2ClassificationJob#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinition",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_criteria": "bucketCriteria",
        "bucket_definitions": "bucketDefinitions",
        "scoping": "scoping",
    },
)
class Macie2ClassificationJobS3JobDefinition:
    def __init__(
        self,
        *,
        bucket_criteria: typing.Optional[typing.Union["Macie2ClassificationJobS3JobDefinitionBucketCriteria", typing.Dict[builtins.str, typing.Any]]] = None,
        bucket_definitions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["Macie2ClassificationJobS3JobDefinitionBucketDefinitions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        scoping: typing.Optional[typing.Union["Macie2ClassificationJobS3JobDefinitionScoping", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param bucket_criteria: bucket_criteria block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#bucket_criteria Macie2ClassificationJob#bucket_criteria}
        :param bucket_definitions: bucket_definitions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#bucket_definitions Macie2ClassificationJob#bucket_definitions}
        :param scoping: scoping block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#scoping Macie2ClassificationJob#scoping}
        '''
        if isinstance(bucket_criteria, dict):
            bucket_criteria = Macie2ClassificationJobS3JobDefinitionBucketCriteria(**bucket_criteria)
        if isinstance(scoping, dict):
            scoping = Macie2ClassificationJobS3JobDefinitionScoping(**scoping)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__299e0be4b73b7706d5edd9ad17d7d84df687cc396d57e0c4e3da38826b5e48c6)
            check_type(argname="argument bucket_criteria", value=bucket_criteria, expected_type=type_hints["bucket_criteria"])
            check_type(argname="argument bucket_definitions", value=bucket_definitions, expected_type=type_hints["bucket_definitions"])
            check_type(argname="argument scoping", value=scoping, expected_type=type_hints["scoping"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if bucket_criteria is not None:
            self._values["bucket_criteria"] = bucket_criteria
        if bucket_definitions is not None:
            self._values["bucket_definitions"] = bucket_definitions
        if scoping is not None:
            self._values["scoping"] = scoping

    @builtins.property
    def bucket_criteria(
        self,
    ) -> typing.Optional["Macie2ClassificationJobS3JobDefinitionBucketCriteria"]:
        '''bucket_criteria block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#bucket_criteria Macie2ClassificationJob#bucket_criteria}
        '''
        result = self._values.get("bucket_criteria")
        return typing.cast(typing.Optional["Macie2ClassificationJobS3JobDefinitionBucketCriteria"], result)

    @builtins.property
    def bucket_definitions(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionBucketDefinitions"]]]:
        '''bucket_definitions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#bucket_definitions Macie2ClassificationJob#bucket_definitions}
        '''
        result = self._values.get("bucket_definitions")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionBucketDefinitions"]]], result)

    @builtins.property
    def scoping(
        self,
    ) -> typing.Optional["Macie2ClassificationJobS3JobDefinitionScoping"]:
        '''scoping block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#scoping Macie2ClassificationJob#scoping}
        '''
        result = self._values.get("scoping")
        return typing.cast(typing.Optional["Macie2ClassificationJobS3JobDefinitionScoping"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobS3JobDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteria",
    jsii_struct_bases=[],
    name_mapping={"excludes": "excludes", "includes": "includes"},
)
class Macie2ClassificationJobS3JobDefinitionBucketCriteria:
    def __init__(
        self,
        *,
        excludes: typing.Optional[typing.Union["Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludes", typing.Dict[builtins.str, typing.Any]]] = None,
        includes: typing.Optional[typing.Union["Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludes", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param excludes: excludes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#excludes Macie2ClassificationJob#excludes}
        :param includes: includes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#includes Macie2ClassificationJob#includes}
        '''
        if isinstance(excludes, dict):
            excludes = Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludes(**excludes)
        if isinstance(includes, dict):
            includes = Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludes(**includes)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b967abe6dd80dee428d8fbbd912ecd626341f52d7918a873a3261afd0c5ca5cb)
            check_type(argname="argument excludes", value=excludes, expected_type=type_hints["excludes"])
            check_type(argname="argument includes", value=includes, expected_type=type_hints["includes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if excludes is not None:
            self._values["excludes"] = excludes
        if includes is not None:
            self._values["includes"] = includes

    @builtins.property
    def excludes(
        self,
    ) -> typing.Optional["Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludes"]:
        '''excludes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#excludes Macie2ClassificationJob#excludes}
        '''
        result = self._values.get("excludes")
        return typing.cast(typing.Optional["Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludes"], result)

    @builtins.property
    def includes(
        self,
    ) -> typing.Optional["Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludes"]:
        '''includes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#includes Macie2ClassificationJob#includes}
        '''
        result = self._values.get("includes")
        return typing.cast(typing.Optional["Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludes"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobS3JobDefinitionBucketCriteria(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludes",
    jsii_struct_bases=[],
    name_mapping={"and_": "and"},
)
class Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludes:
    def __init__(
        self,
        *,
        and_: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAnd", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param and_: and block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#and Macie2ClassificationJob#and}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10f235eb87fd8d2bd659fa8c65503d40b1f9a2bc945618b44039439f6340d514)
            check_type(argname="argument and_", value=and_, expected_type=type_hints["and_"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if and_ is not None:
            self._values["and_"] = and_

    @builtins.property
    def and_(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAnd"]]]:
        '''and block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#and Macie2ClassificationJob#and}
        '''
        result = self._values.get("and_")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAnd"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAnd",
    jsii_struct_bases=[],
    name_mapping={
        "simple_criterion": "simpleCriterion",
        "tag_criterion": "tagCriterion",
    },
)
class Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAnd:
    def __init__(
        self,
        *,
        simple_criterion: typing.Optional[typing.Union["Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterion", typing.Dict[builtins.str, typing.Any]]] = None,
        tag_criterion: typing.Optional[typing.Union["Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterion", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param simple_criterion: simple_criterion block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#simple_criterion Macie2ClassificationJob#simple_criterion}
        :param tag_criterion: tag_criterion block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tag_criterion Macie2ClassificationJob#tag_criterion}
        '''
        if isinstance(simple_criterion, dict):
            simple_criterion = Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterion(**simple_criterion)
        if isinstance(tag_criterion, dict):
            tag_criterion = Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterion(**tag_criterion)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34e793860c01868187bebbef381c8291f6b5596669978886028a534293614710)
            check_type(argname="argument simple_criterion", value=simple_criterion, expected_type=type_hints["simple_criterion"])
            check_type(argname="argument tag_criterion", value=tag_criterion, expected_type=type_hints["tag_criterion"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if simple_criterion is not None:
            self._values["simple_criterion"] = simple_criterion
        if tag_criterion is not None:
            self._values["tag_criterion"] = tag_criterion

    @builtins.property
    def simple_criterion(
        self,
    ) -> typing.Optional["Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterion"]:
        '''simple_criterion block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#simple_criterion Macie2ClassificationJob#simple_criterion}
        '''
        result = self._values.get("simple_criterion")
        return typing.cast(typing.Optional["Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterion"], result)

    @builtins.property
    def tag_criterion(
        self,
    ) -> typing.Optional["Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterion"]:
        '''tag_criterion block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tag_criterion Macie2ClassificationJob#tag_criterion}
        '''
        result = self._values.get("tag_criterion")
        return typing.cast(typing.Optional["Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterion"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAnd(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bceb8803ceb9f035b85cb0f0fd623a752a65db1e45c300e1f989e55f62727e03)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4edb837628fb01e2c2dfffbf20777f2561e63d4c5e6a623b64a44689a76dae5)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41c7966dd61874c2b954a6e883a600872ac82a194b1888b2d85ff662a1b6f343)
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
            type_hints = typing.get_type_hints(_typecheckingstub__dfc80802b5aa955124bf38f428e3d0b479c0192de3925aa3e42c8ceecc79add4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9786af677c1f66c8ef035a220937a7df91cd16ed58ff5c775b417490ca67a593)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAnd]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAnd]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAnd]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb07ed31777bd6a551e3bad4000b77cbdc8f964b8cb9e7ee01b3e2cdb214e76f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__47b14003235d1583d6675dff67d695ebbd39dcef8dad45fd043cc1bb7e7a8387)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putSimpleCriterion")
    def put_simple_criterion(
        self,
        *,
        comparator: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param comparator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#comparator Macie2ClassificationJob#comparator}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#values Macie2ClassificationJob#values}.
        '''
        value = Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterion(
            comparator=comparator, key=key, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putSimpleCriterion", [value]))

    @jsii.member(jsii_name="putTagCriterion")
    def put_tag_criterion(
        self,
        *,
        comparator: typing.Optional[builtins.str] = None,
        tag_values: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValues", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param comparator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#comparator Macie2ClassificationJob#comparator}.
        :param tag_values: tag_values block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tag_values Macie2ClassificationJob#tag_values}
        '''
        value = Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterion(
            comparator=comparator, tag_values=tag_values
        )

        return typing.cast(None, jsii.invoke(self, "putTagCriterion", [value]))

    @jsii.member(jsii_name="resetSimpleCriterion")
    def reset_simple_criterion(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSimpleCriterion", []))

    @jsii.member(jsii_name="resetTagCriterion")
    def reset_tag_criterion(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagCriterion", []))

    @builtins.property
    @jsii.member(jsii_name="simpleCriterion")
    def simple_criterion(
        self,
    ) -> "Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterionOutputReference":
        return typing.cast("Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterionOutputReference", jsii.get(self, "simpleCriterion"))

    @builtins.property
    @jsii.member(jsii_name="tagCriterion")
    def tag_criterion(
        self,
    ) -> "Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionOutputReference":
        return typing.cast("Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionOutputReference", jsii.get(self, "tagCriterion"))

    @builtins.property
    @jsii.member(jsii_name="simpleCriterionInput")
    def simple_criterion_input(
        self,
    ) -> typing.Optional["Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterion"]:
        return typing.cast(typing.Optional["Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterion"], jsii.get(self, "simpleCriterionInput"))

    @builtins.property
    @jsii.member(jsii_name="tagCriterionInput")
    def tag_criterion_input(
        self,
    ) -> typing.Optional["Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterion"]:
        return typing.cast(typing.Optional["Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterion"], jsii.get(self, "tagCriterionInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAnd, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAnd, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAnd, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59fbcad040e0c5875bae44488639932d8ed9ea01d4a3161d4af2c30e6a11e9fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterion",
    jsii_struct_bases=[],
    name_mapping={"comparator": "comparator", "key": "key", "values": "values"},
)
class Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterion:
    def __init__(
        self,
        *,
        comparator: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param comparator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#comparator Macie2ClassificationJob#comparator}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#values Macie2ClassificationJob#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12f4faa91f1fa270ee55957690dd526ee51df7e9f90d50f5929e425276070b47)
            check_type(argname="argument comparator", value=comparator, expected_type=type_hints["comparator"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if comparator is not None:
            self._values["comparator"] = comparator
        if key is not None:
            self._values["key"] = key
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def comparator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#comparator Macie2ClassificationJob#comparator}.'''
        result = self._values.get("comparator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#values Macie2ClassificationJob#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__eacf8747df322bac3645ebd753831d8db90073c7095efcfcee22d41badd131a1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetComparator")
    def reset_comparator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComparator", []))

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="comparatorInput")
    def comparator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "comparatorInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="comparator")
    def comparator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comparator"))

    @comparator.setter
    def comparator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b610a6e7dfacb3bb8c4dffc5388ab6fb0ff22b1df22b9ea606c62fb78f6bc950)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comparator", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__393175a56d7b67e0e92e2eb21f2578c4c6df90fdfc0df5644548f99a982aac05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12574c001ccbee3ab5c61920ed8c832b96873d3da46d42d61ea9701af0c431b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterion]:
        return typing.cast(typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterion], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterion],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25b6c646fc1a6208287ae9e58de75cbe67253e15a26fc306629942dc0503efa6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterion",
    jsii_struct_bases=[],
    name_mapping={"comparator": "comparator", "tag_values": "tagValues"},
)
class Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterion:
    def __init__(
        self,
        *,
        comparator: typing.Optional[builtins.str] = None,
        tag_values: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValues", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param comparator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#comparator Macie2ClassificationJob#comparator}.
        :param tag_values: tag_values block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tag_values Macie2ClassificationJob#tag_values}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1e26fe7b2a5af7add9ae9908568a7972417f2c093db03f3129d6d137f645306)
            check_type(argname="argument comparator", value=comparator, expected_type=type_hints["comparator"])
            check_type(argname="argument tag_values", value=tag_values, expected_type=type_hints["tag_values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if comparator is not None:
            self._values["comparator"] = comparator
        if tag_values is not None:
            self._values["tag_values"] = tag_values

    @builtins.property
    def comparator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#comparator Macie2ClassificationJob#comparator}.'''
        result = self._values.get("comparator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag_values(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValues"]]]:
        '''tag_values block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tag_values Macie2ClassificationJob#tag_values}
        '''
        result = self._values.get("tag_values")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValues"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4ac2fbc1d9f20581516b3b40ea0d60088118306cb8bb421b34b93a741293d59e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putTagValues")
    def put_tag_values(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValues", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a9774a6ecf025908499bb39a8e668464269cbdeb65862d55f92e4b357f67683)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTagValues", [value]))

    @jsii.member(jsii_name="resetComparator")
    def reset_comparator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComparator", []))

    @jsii.member(jsii_name="resetTagValues")
    def reset_tag_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagValues", []))

    @builtins.property
    @jsii.member(jsii_name="tagValues")
    def tag_values(
        self,
    ) -> "Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValuesList":
        return typing.cast("Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValuesList", jsii.get(self, "tagValues"))

    @builtins.property
    @jsii.member(jsii_name="comparatorInput")
    def comparator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "comparatorInput"))

    @builtins.property
    @jsii.member(jsii_name="tagValuesInput")
    def tag_values_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValues"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValues"]]], jsii.get(self, "tagValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="comparator")
    def comparator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comparator"))

    @comparator.setter
    def comparator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98c4a8b4682ba0b5aa6f1c0ec585c5a21ff26686880777e28fd92c9ab30ba6ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comparator", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterion]:
        return typing.cast(typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterion], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterion],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55c5c560d28e2e6767bb8c3b13ed7202d6bd5c08349c989a7ef033831e8cf761)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValues",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValues:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#value Macie2ClassificationJob#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d1c5857c1ed00a1aa0b535755c57ff1637da456c6a6d65b01e14faa47efed88)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#value Macie2ClassificationJob#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValues(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValuesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValuesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__dac37afbb1b0d9ad9401d8735468c1b4ab7eeeb1b11da6bc6d5f33d7fd68a9b5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValuesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b3da7620b6496bf9d21588f6eb36d854e5a877db619e3baaa4a2d194a94b873)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValuesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82511a0fe1f839aa63a1df261f5f50ad00875b8a71464f0c8a081dfc410b07c8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d8f5c87d9634a71ddbc521fb1aeca76cd6d9f1b4d826489a59829ebdb9361434)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d575af88282ea7329d000328344215039d4f896f15b854487fd497955ec6ec8f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValues]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValues]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValues]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0729f8e449649252559f015b923a02a671988344071acf1ba4347ffe116fb58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValuesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValuesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__38a8d736919ed7b5f4be61e9bdb1f4f1fb5883818f975b3dca55235bb0f3f567)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75a0584e0eda5d930967ee00e055fe1f8a1895e8520dbdf50512f8f0f8141830)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19a43f6a20e6400f6dfb61aa3de5eacaf0c14052e41db57187b156eefec25eec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValues, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValues, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValues, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9743b6cba2357c3cc7107abfc2bea4b31f74a99cc4f14cc61513eb5095a54da7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__dcb42fec85b4927e00c9a6a543866d5e4b4a8a75e5b70ff0098f15713a733885)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAnd")
    def put_and(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAnd, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bca0084c68d6aac4e74ff610f3930a3b8969341f4b0645aa8a75643cb826fec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAnd", [value]))

    @jsii.member(jsii_name="resetAnd")
    def reset_and(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnd", []))

    @builtins.property
    @jsii.member(jsii_name="and")
    def and_(
        self,
    ) -> Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndList:
        return typing.cast(Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndList, jsii.get(self, "and"))

    @builtins.property
    @jsii.member(jsii_name="andInput")
    def and_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAnd]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAnd]]], jsii.get(self, "andInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludes]:
        return typing.cast(typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludes],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4683c4d9bcbb5b522463542ec61f0fa611764ae6081de75ec976bf6a14f3d31f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludes",
    jsii_struct_bases=[],
    name_mapping={"and_": "and"},
)
class Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludes:
    def __init__(
        self,
        *,
        and_: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAnd", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param and_: and block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#and Macie2ClassificationJob#and}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f096f1c4f5ef744c3d9dbe0f48cab00c3ef3470ba78ca2fd715e4ca8fbf2bbc)
            check_type(argname="argument and_", value=and_, expected_type=type_hints["and_"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if and_ is not None:
            self._values["and_"] = and_

    @builtins.property
    def and_(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAnd"]]]:
        '''and block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#and Macie2ClassificationJob#and}
        '''
        result = self._values.get("and_")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAnd"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAnd",
    jsii_struct_bases=[],
    name_mapping={
        "simple_criterion": "simpleCriterion",
        "tag_criterion": "tagCriterion",
    },
)
class Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAnd:
    def __init__(
        self,
        *,
        simple_criterion: typing.Optional[typing.Union["Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterion", typing.Dict[builtins.str, typing.Any]]] = None,
        tag_criterion: typing.Optional[typing.Union["Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterion", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param simple_criterion: simple_criterion block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#simple_criterion Macie2ClassificationJob#simple_criterion}
        :param tag_criterion: tag_criterion block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tag_criterion Macie2ClassificationJob#tag_criterion}
        '''
        if isinstance(simple_criterion, dict):
            simple_criterion = Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterion(**simple_criterion)
        if isinstance(tag_criterion, dict):
            tag_criterion = Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterion(**tag_criterion)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1df810c7d279cd8031ebfe0811094de80563dc8cdaa1d4c9adbec46c7cd387eb)
            check_type(argname="argument simple_criterion", value=simple_criterion, expected_type=type_hints["simple_criterion"])
            check_type(argname="argument tag_criterion", value=tag_criterion, expected_type=type_hints["tag_criterion"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if simple_criterion is not None:
            self._values["simple_criterion"] = simple_criterion
        if tag_criterion is not None:
            self._values["tag_criterion"] = tag_criterion

    @builtins.property
    def simple_criterion(
        self,
    ) -> typing.Optional["Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterion"]:
        '''simple_criterion block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#simple_criterion Macie2ClassificationJob#simple_criterion}
        '''
        result = self._values.get("simple_criterion")
        return typing.cast(typing.Optional["Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterion"], result)

    @builtins.property
    def tag_criterion(
        self,
    ) -> typing.Optional["Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterion"]:
        '''tag_criterion block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tag_criterion Macie2ClassificationJob#tag_criterion}
        '''
        result = self._values.get("tag_criterion")
        return typing.cast(typing.Optional["Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterion"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAnd(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5ea05f92b1bfbe0701748d547ea4177cafc9bd078c3707722776abceef19cc9f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d19409d954e05922523c7184e74ca52b80637f544462f90ce3f24479432a18b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc64aa24ec06a43ee894df5577a4887b8e28c996c7bc1ad2cacb09adf6964583)
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
            type_hints = typing.get_type_hints(_typecheckingstub__76fa5899d5a972f88d89427f5c6e7ea3b8f354272a79faa374e57a96aa11c882)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7ad001115bb57b0530fac641d4299af5e09fcbbcecb39180cf3d20cf2116e558)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAnd]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAnd]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAnd]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03ab8fddda5facfe0c312c3b325839ba9820b64c91db29bd8c71ca7a11f5cd4f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f2ff3fabd254fcce24c18c947d0d5e9d7e29bbcd97e8b2e95311bc5b1b405372)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putSimpleCriterion")
    def put_simple_criterion(
        self,
        *,
        comparator: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param comparator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#comparator Macie2ClassificationJob#comparator}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#values Macie2ClassificationJob#values}.
        '''
        value = Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterion(
            comparator=comparator, key=key, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putSimpleCriterion", [value]))

    @jsii.member(jsii_name="putTagCriterion")
    def put_tag_criterion(
        self,
        *,
        comparator: typing.Optional[builtins.str] = None,
        tag_values: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValues", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param comparator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#comparator Macie2ClassificationJob#comparator}.
        :param tag_values: tag_values block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tag_values Macie2ClassificationJob#tag_values}
        '''
        value = Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterion(
            comparator=comparator, tag_values=tag_values
        )

        return typing.cast(None, jsii.invoke(self, "putTagCriterion", [value]))

    @jsii.member(jsii_name="resetSimpleCriterion")
    def reset_simple_criterion(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSimpleCriterion", []))

    @jsii.member(jsii_name="resetTagCriterion")
    def reset_tag_criterion(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagCriterion", []))

    @builtins.property
    @jsii.member(jsii_name="simpleCriterion")
    def simple_criterion(
        self,
    ) -> "Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterionOutputReference":
        return typing.cast("Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterionOutputReference", jsii.get(self, "simpleCriterion"))

    @builtins.property
    @jsii.member(jsii_name="tagCriterion")
    def tag_criterion(
        self,
    ) -> "Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionOutputReference":
        return typing.cast("Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionOutputReference", jsii.get(self, "tagCriterion"))

    @builtins.property
    @jsii.member(jsii_name="simpleCriterionInput")
    def simple_criterion_input(
        self,
    ) -> typing.Optional["Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterion"]:
        return typing.cast(typing.Optional["Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterion"], jsii.get(self, "simpleCriterionInput"))

    @builtins.property
    @jsii.member(jsii_name="tagCriterionInput")
    def tag_criterion_input(
        self,
    ) -> typing.Optional["Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterion"]:
        return typing.cast(typing.Optional["Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterion"], jsii.get(self, "tagCriterionInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAnd, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAnd, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAnd, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7f3322170422115c11584b2afd244b63fc87417e6d784b44897771add390f09)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterion",
    jsii_struct_bases=[],
    name_mapping={"comparator": "comparator", "key": "key", "values": "values"},
)
class Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterion:
    def __init__(
        self,
        *,
        comparator: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param comparator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#comparator Macie2ClassificationJob#comparator}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#values Macie2ClassificationJob#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__521249f8cd606a4bf3b49d72ece182a520e449a3824b7acb3d6c5f7a9dfea75e)
            check_type(argname="argument comparator", value=comparator, expected_type=type_hints["comparator"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if comparator is not None:
            self._values["comparator"] = comparator
        if key is not None:
            self._values["key"] = key
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def comparator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#comparator Macie2ClassificationJob#comparator}.'''
        result = self._values.get("comparator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#values Macie2ClassificationJob#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7246cb2c7f72cb46b42d6dcdcf8d96888c7e4dfecae44e6f8c723ae92f4578cd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetComparator")
    def reset_comparator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComparator", []))

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="comparatorInput")
    def comparator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "comparatorInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="comparator")
    def comparator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comparator"))

    @comparator.setter
    def comparator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c93be186a0fe811669d55bc251c2b44e50a4b0d34fb1d3a8675a335e07142643)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comparator", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae9210c26b95d4a8da3422779650b0b150e24bb4ac572d4ac591e7716a6ee8dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bab60789f86de021634fcd613c8f77cd2a2e0f9659c8ddf6ce3d50e8de598277)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterion]:
        return typing.cast(typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterion], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterion],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73d798f7a70387ca0ecdac121b192a77e247d9de123878735a6672ef4fca7adc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterion",
    jsii_struct_bases=[],
    name_mapping={"comparator": "comparator", "tag_values": "tagValues"},
)
class Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterion:
    def __init__(
        self,
        *,
        comparator: typing.Optional[builtins.str] = None,
        tag_values: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValues", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param comparator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#comparator Macie2ClassificationJob#comparator}.
        :param tag_values: tag_values block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tag_values Macie2ClassificationJob#tag_values}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1be5327d5f9656b7a962422b0f3f911abea8a7041f9e8fcbc00393d1cd302e0)
            check_type(argname="argument comparator", value=comparator, expected_type=type_hints["comparator"])
            check_type(argname="argument tag_values", value=tag_values, expected_type=type_hints["tag_values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if comparator is not None:
            self._values["comparator"] = comparator
        if tag_values is not None:
            self._values["tag_values"] = tag_values

    @builtins.property
    def comparator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#comparator Macie2ClassificationJob#comparator}.'''
        result = self._values.get("comparator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag_values(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValues"]]]:
        '''tag_values block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tag_values Macie2ClassificationJob#tag_values}
        '''
        result = self._values.get("tag_values")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValues"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f40aa6486b25d9b2e65179634b09ba5c68fcb586ead5640d6f8e75127f0559fe)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putTagValues")
    def put_tag_values(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValues", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a35b6676beb6660dea0f332d7af61fb8633cfe61a8fa0a32482564abaff41d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTagValues", [value]))

    @jsii.member(jsii_name="resetComparator")
    def reset_comparator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComparator", []))

    @jsii.member(jsii_name="resetTagValues")
    def reset_tag_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagValues", []))

    @builtins.property
    @jsii.member(jsii_name="tagValues")
    def tag_values(
        self,
    ) -> "Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValuesList":
        return typing.cast("Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValuesList", jsii.get(self, "tagValues"))

    @builtins.property
    @jsii.member(jsii_name="comparatorInput")
    def comparator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "comparatorInput"))

    @builtins.property
    @jsii.member(jsii_name="tagValuesInput")
    def tag_values_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValues"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValues"]]], jsii.get(self, "tagValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="comparator")
    def comparator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comparator"))

    @comparator.setter
    def comparator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25dca5a8d805d1560e2c5647b708fc775eb3bcbdbaf239f3376e8bae73496c37)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comparator", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterion]:
        return typing.cast(typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterion], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterion],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__993b126fb5cc5f3f339a1c6211383a036d9a4a573d9097a1767f6d6dc02d5e08)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValues",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValues:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#value Macie2ClassificationJob#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36dec0f8be75976f659445070b34938f30ab44076086c55a15822c30ce1ebe71)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#value Macie2ClassificationJob#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValues(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValuesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValuesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b950b8b5605aa483fb9c61b6841cac97818b468d12a72223e7497ab28f63c8dc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValuesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0802966037690a1f3c5d98fcbe7fa5da3625572b87b44d4c305861b9f1a5939c)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValuesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24b4cb3bbed190aba800763d168aabe2319075dc098b9baafc42fed06f489e59)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b06ce0d63905571808ff0d4286abcb9faf012bd01653e4681ed102eb9a2fba7b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ac6b8fa58f3bd17e820197dbd0ab37ee8726cab728231c170435c6fd11646b07)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValues]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValues]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValues]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9058dd8eba63251ef97730d319733abc46d5eeb2250ec54b7aa1cd3328bc24fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValuesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValuesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2ecdf198ae7bda2fbc77a7ce8696e759f62da77cf0b8529b5dc318886b0c85b8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc078da59b5525e661314a1ef0687e333e76159408635a9c3c5b8193c3a13260)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1fd66476af4aba2da2679d56066ee098cd2e658bc604564abf15a5c2ae0cf4f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValues, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValues, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValues, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bfad72aa0a0bfb7728043a74e38751a8e399ffd37205910818c7690e69e1df8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3f41b5139771fbe8362fabd8b3d9ccda0294afb7323deff3c7b006e2c6e82d42)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAnd")
    def put_and(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAnd, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72c043225f11263f02e88c2f89824d4bc5083261f1504d9f2217e6c4442f79c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAnd", [value]))

    @jsii.member(jsii_name="resetAnd")
    def reset_and(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnd", []))

    @builtins.property
    @jsii.member(jsii_name="and")
    def and_(
        self,
    ) -> Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndList:
        return typing.cast(Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndList, jsii.get(self, "and"))

    @builtins.property
    @jsii.member(jsii_name="andInput")
    def and_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAnd]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAnd]]], jsii.get(self, "andInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludes]:
        return typing.cast(typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludes],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5edac7d6d88975541d0b4c96cb7857821b679ddbd57959dd985ef1e8d371ce9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Macie2ClassificationJobS3JobDefinitionBucketCriteriaOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteriaOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b3fc0fc9197148e7b2e70f24b9860fc55098133735abccd37cea6ab7f1a53c34)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putExcludes")
    def put_excludes(
        self,
        *,
        and_: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAnd, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param and_: and block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#and Macie2ClassificationJob#and}
        '''
        value = Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludes(and_=and_)

        return typing.cast(None, jsii.invoke(self, "putExcludes", [value]))

    @jsii.member(jsii_name="putIncludes")
    def put_includes(
        self,
        *,
        and_: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAnd, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param and_: and block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#and Macie2ClassificationJob#and}
        '''
        value = Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludes(and_=and_)

        return typing.cast(None, jsii.invoke(self, "putIncludes", [value]))

    @jsii.member(jsii_name="resetExcludes")
    def reset_excludes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcludes", []))

    @jsii.member(jsii_name="resetIncludes")
    def reset_includes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludes", []))

    @builtins.property
    @jsii.member(jsii_name="excludes")
    def excludes(
        self,
    ) -> Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesOutputReference:
        return typing.cast(Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesOutputReference, jsii.get(self, "excludes"))

    @builtins.property
    @jsii.member(jsii_name="includes")
    def includes(
        self,
    ) -> Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesOutputReference:
        return typing.cast(Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesOutputReference, jsii.get(self, "includes"))

    @builtins.property
    @jsii.member(jsii_name="excludesInput")
    def excludes_input(
        self,
    ) -> typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludes]:
        return typing.cast(typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludes], jsii.get(self, "excludesInput"))

    @builtins.property
    @jsii.member(jsii_name="includesInput")
    def includes_input(
        self,
    ) -> typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludes]:
        return typing.cast(typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludes], jsii.get(self, "includesInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteria]:
        return typing.cast(typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteria], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteria],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2083860869af831b88132587ec986ae4c896847a23c5ba222c4e79eea471ff4f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketDefinitions",
    jsii_struct_bases=[],
    name_mapping={"account_id": "accountId", "buckets": "buckets"},
)
class Macie2ClassificationJobS3JobDefinitionBucketDefinitions:
    def __init__(
        self,
        *,
        account_id: builtins.str,
        buckets: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#account_id Macie2ClassificationJob#account_id}.
        :param buckets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#buckets Macie2ClassificationJob#buckets}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__949b094635f62b35ac156294d4e00ef1c0d1c2bd36f80c92456c5aaa563af5e5)
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument buckets", value=buckets, expected_type=type_hints["buckets"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account_id": account_id,
            "buckets": buckets,
        }

    @builtins.property
    def account_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#account_id Macie2ClassificationJob#account_id}.'''
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def buckets(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#buckets Macie2ClassificationJob#buckets}.'''
        result = self._values.get("buckets")
        assert result is not None, "Required property 'buckets' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobS3JobDefinitionBucketDefinitions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Macie2ClassificationJobS3JobDefinitionBucketDefinitionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketDefinitionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__827eeee482924af7e04458eee4f0d41e1077b79b8eb2112c39b4bd1ad49fd196)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Macie2ClassificationJobS3JobDefinitionBucketDefinitionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aff908f2ae46e689ffc9cf1ef0991a4ea9b418d3b10cbd8e916e9475b0ce30c4)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Macie2ClassificationJobS3JobDefinitionBucketDefinitionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dec0a4bd3ea4c6dd51ad83f9f85ba8120af52b345687b739fd770da942ccf015)
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
            type_hints = typing.get_type_hints(_typecheckingstub__21a235b68506ede23423917d6f3d75fc470fe920a24f054ce66263c84ef9420a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__78bcafecde60cc872055d64cf901b88d94339f7b3600d5c5442454cbf8d14242)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketDefinitions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketDefinitions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketDefinitions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__408952b23479c875701d78ef366cdb80318a28d79e92faa6b1f02070c014ea4f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Macie2ClassificationJobS3JobDefinitionBucketDefinitionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketDefinitionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8408f1865e1532900701bf904da6858721fbee34cf244bd43efc541352518da5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketsInput")
    def buckets_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "bucketsInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26157eb24634030b03e9562008c4060b42a150e5738de3fb5653de026044cd63)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="buckets")
    def buckets(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "buckets"))

    @buckets.setter
    def buckets(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63b31d11a4d4c3db103288e75eb612b0cc66a88c907dd0392a12195470cd22c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "buckets", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketDefinitions, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketDefinitions, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketDefinitions, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01fb53968967191b486093e539e6e868709d922dce5ae1508eec7fe5796e8dce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Macie2ClassificationJobS3JobDefinitionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7198db672485d06126033ed1d8928f0d61cad30b55935e47c526de10d1719bdc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putBucketCriteria")
    def put_bucket_criteria(
        self,
        *,
        excludes: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludes, typing.Dict[builtins.str, typing.Any]]] = None,
        includes: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludes, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param excludes: excludes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#excludes Macie2ClassificationJob#excludes}
        :param includes: includes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#includes Macie2ClassificationJob#includes}
        '''
        value = Macie2ClassificationJobS3JobDefinitionBucketCriteria(
            excludes=excludes, includes=includes
        )

        return typing.cast(None, jsii.invoke(self, "putBucketCriteria", [value]))

    @jsii.member(jsii_name="putBucketDefinitions")
    def put_bucket_definitions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketDefinitions, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5af5c86ade2e2488350a1c5e5b76d33b1151eb760317e0c02a353e51fedab31c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putBucketDefinitions", [value]))

    @jsii.member(jsii_name="putScoping")
    def put_scoping(
        self,
        *,
        excludes: typing.Optional[typing.Union["Macie2ClassificationJobS3JobDefinitionScopingExcludes", typing.Dict[builtins.str, typing.Any]]] = None,
        includes: typing.Optional[typing.Union["Macie2ClassificationJobS3JobDefinitionScopingIncludes", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param excludes: excludes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#excludes Macie2ClassificationJob#excludes}
        :param includes: includes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#includes Macie2ClassificationJob#includes}
        '''
        value = Macie2ClassificationJobS3JobDefinitionScoping(
            excludes=excludes, includes=includes
        )

        return typing.cast(None, jsii.invoke(self, "putScoping", [value]))

    @jsii.member(jsii_name="resetBucketCriteria")
    def reset_bucket_criteria(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketCriteria", []))

    @jsii.member(jsii_name="resetBucketDefinitions")
    def reset_bucket_definitions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketDefinitions", []))

    @jsii.member(jsii_name="resetScoping")
    def reset_scoping(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScoping", []))

    @builtins.property
    @jsii.member(jsii_name="bucketCriteria")
    def bucket_criteria(
        self,
    ) -> Macie2ClassificationJobS3JobDefinitionBucketCriteriaOutputReference:
        return typing.cast(Macie2ClassificationJobS3JobDefinitionBucketCriteriaOutputReference, jsii.get(self, "bucketCriteria"))

    @builtins.property
    @jsii.member(jsii_name="bucketDefinitions")
    def bucket_definitions(
        self,
    ) -> Macie2ClassificationJobS3JobDefinitionBucketDefinitionsList:
        return typing.cast(Macie2ClassificationJobS3JobDefinitionBucketDefinitionsList, jsii.get(self, "bucketDefinitions"))

    @builtins.property
    @jsii.member(jsii_name="scoping")
    def scoping(self) -> "Macie2ClassificationJobS3JobDefinitionScopingOutputReference":
        return typing.cast("Macie2ClassificationJobS3JobDefinitionScopingOutputReference", jsii.get(self, "scoping"))

    @builtins.property
    @jsii.member(jsii_name="bucketCriteriaInput")
    def bucket_criteria_input(
        self,
    ) -> typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteria]:
        return typing.cast(typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteria], jsii.get(self, "bucketCriteriaInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketDefinitionsInput")
    def bucket_definitions_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketDefinitions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketDefinitions]]], jsii.get(self, "bucketDefinitionsInput"))

    @builtins.property
    @jsii.member(jsii_name="scopingInput")
    def scoping_input(
        self,
    ) -> typing.Optional["Macie2ClassificationJobS3JobDefinitionScoping"]:
        return typing.cast(typing.Optional["Macie2ClassificationJobS3JobDefinitionScoping"], jsii.get(self, "scopingInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[Macie2ClassificationJobS3JobDefinition]:
        return typing.cast(typing.Optional[Macie2ClassificationJobS3JobDefinition], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Macie2ClassificationJobS3JobDefinition],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37d2937424ecfb8a0010c1af6c09a0d7af93b73601df30058275d1d29c21810d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScoping",
    jsii_struct_bases=[],
    name_mapping={"excludes": "excludes", "includes": "includes"},
)
class Macie2ClassificationJobS3JobDefinitionScoping:
    def __init__(
        self,
        *,
        excludes: typing.Optional[typing.Union["Macie2ClassificationJobS3JobDefinitionScopingExcludes", typing.Dict[builtins.str, typing.Any]]] = None,
        includes: typing.Optional[typing.Union["Macie2ClassificationJobS3JobDefinitionScopingIncludes", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param excludes: excludes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#excludes Macie2ClassificationJob#excludes}
        :param includes: includes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#includes Macie2ClassificationJob#includes}
        '''
        if isinstance(excludes, dict):
            excludes = Macie2ClassificationJobS3JobDefinitionScopingExcludes(**excludes)
        if isinstance(includes, dict):
            includes = Macie2ClassificationJobS3JobDefinitionScopingIncludes(**includes)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddf5bb27ee23f2cb701964453e01dc0d886666dca7586e48a71a00eff41ca8d1)
            check_type(argname="argument excludes", value=excludes, expected_type=type_hints["excludes"])
            check_type(argname="argument includes", value=includes, expected_type=type_hints["includes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if excludes is not None:
            self._values["excludes"] = excludes
        if includes is not None:
            self._values["includes"] = includes

    @builtins.property
    def excludes(
        self,
    ) -> typing.Optional["Macie2ClassificationJobS3JobDefinitionScopingExcludes"]:
        '''excludes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#excludes Macie2ClassificationJob#excludes}
        '''
        result = self._values.get("excludes")
        return typing.cast(typing.Optional["Macie2ClassificationJobS3JobDefinitionScopingExcludes"], result)

    @builtins.property
    def includes(
        self,
    ) -> typing.Optional["Macie2ClassificationJobS3JobDefinitionScopingIncludes"]:
        '''includes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#includes Macie2ClassificationJob#includes}
        '''
        result = self._values.get("includes")
        return typing.cast(typing.Optional["Macie2ClassificationJobS3JobDefinitionScopingIncludes"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobS3JobDefinitionScoping(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScopingExcludes",
    jsii_struct_bases=[],
    name_mapping={"and_": "and"},
)
class Macie2ClassificationJobS3JobDefinitionScopingExcludes:
    def __init__(
        self,
        *,
        and_: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["Macie2ClassificationJobS3JobDefinitionScopingExcludesAnd", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param and_: and block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#and Macie2ClassificationJob#and}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9c62acb84226daa72411ac239e6a971074b8baad32af4a3e057f8df302bd6b1)
            check_type(argname="argument and_", value=and_, expected_type=type_hints["and_"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if and_ is not None:
            self._values["and_"] = and_

    @builtins.property
    def and_(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionScopingExcludesAnd"]]]:
        '''and block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#and Macie2ClassificationJob#and}
        '''
        result = self._values.get("and_")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionScopingExcludesAnd"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobS3JobDefinitionScopingExcludes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScopingExcludesAnd",
    jsii_struct_bases=[],
    name_mapping={
        "simple_scope_term": "simpleScopeTerm",
        "tag_scope_term": "tagScopeTerm",
    },
)
class Macie2ClassificationJobS3JobDefinitionScopingExcludesAnd:
    def __init__(
        self,
        *,
        simple_scope_term: typing.Optional[typing.Union["Macie2ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTerm", typing.Dict[builtins.str, typing.Any]]] = None,
        tag_scope_term: typing.Optional[typing.Union["Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTerm", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param simple_scope_term: simple_scope_term block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#simple_scope_term Macie2ClassificationJob#simple_scope_term}
        :param tag_scope_term: tag_scope_term block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tag_scope_term Macie2ClassificationJob#tag_scope_term}
        '''
        if isinstance(simple_scope_term, dict):
            simple_scope_term = Macie2ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTerm(**simple_scope_term)
        if isinstance(tag_scope_term, dict):
            tag_scope_term = Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTerm(**tag_scope_term)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cac7696b55e5ebcb03ab150fe9a1bc74bb324296ca3de2ca7dc118330bd29411)
            check_type(argname="argument simple_scope_term", value=simple_scope_term, expected_type=type_hints["simple_scope_term"])
            check_type(argname="argument tag_scope_term", value=tag_scope_term, expected_type=type_hints["tag_scope_term"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if simple_scope_term is not None:
            self._values["simple_scope_term"] = simple_scope_term
        if tag_scope_term is not None:
            self._values["tag_scope_term"] = tag_scope_term

    @builtins.property
    def simple_scope_term(
        self,
    ) -> typing.Optional["Macie2ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTerm"]:
        '''simple_scope_term block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#simple_scope_term Macie2ClassificationJob#simple_scope_term}
        '''
        result = self._values.get("simple_scope_term")
        return typing.cast(typing.Optional["Macie2ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTerm"], result)

    @builtins.property
    def tag_scope_term(
        self,
    ) -> typing.Optional["Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTerm"]:
        '''tag_scope_term block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tag_scope_term Macie2ClassificationJob#tag_scope_term}
        '''
        result = self._values.get("tag_scope_term")
        return typing.cast(typing.Optional["Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTerm"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobS3JobDefinitionScopingExcludesAnd(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Macie2ClassificationJobS3JobDefinitionScopingExcludesAndList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScopingExcludesAndList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a727a814d840b2749f6d6e89e5da52a92d42b0a5400ba8024f08f6f7bc6aabf2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Macie2ClassificationJobS3JobDefinitionScopingExcludesAndOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__300fbc1d5307084e3149863389f49b3e9ddfc5e2e57a4a9de4b3a9c717c9b43f)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Macie2ClassificationJobS3JobDefinitionScopingExcludesAndOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8cc56fdfb10ccb4e92bfb710619abf8ad1db18c4341cfa13b0bfc56906e5483b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cb8a5c0a3800b70552f85f90dd6e11d9ea560d8b7db24f313c1b40abc1fb0bd8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__57dfab36deb7b9b1251963026739f29e230d09de2e7822dcbd759d439b3f1809)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionScopingExcludesAnd]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionScopingExcludesAnd]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionScopingExcludesAnd]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24e6e007d9bca1d3fee5ce3aff552290218385b88513987d678511685746712d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Macie2ClassificationJobS3JobDefinitionScopingExcludesAndOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScopingExcludesAndOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d6f5fcdbfb9613248fd9855a8ab587cfaaa547557c94d956c180dd7b117e0258)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putSimpleScopeTerm")
    def put_simple_scope_term(
        self,
        *,
        comparator: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param comparator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#comparator Macie2ClassificationJob#comparator}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#values Macie2ClassificationJob#values}.
        '''
        value = Macie2ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTerm(
            comparator=comparator, key=key, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putSimpleScopeTerm", [value]))

    @jsii.member(jsii_name="putTagScopeTerm")
    def put_tag_scope_term(
        self,
        *,
        comparator: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
        tag_values: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValues", typing.Dict[builtins.str, typing.Any]]]]] = None,
        target: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param comparator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#comparator Macie2ClassificationJob#comparator}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.
        :param tag_values: tag_values block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tag_values Macie2ClassificationJob#tag_values}
        :param target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#target Macie2ClassificationJob#target}.
        '''
        value = Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTerm(
            comparator=comparator, key=key, tag_values=tag_values, target=target
        )

        return typing.cast(None, jsii.invoke(self, "putTagScopeTerm", [value]))

    @jsii.member(jsii_name="resetSimpleScopeTerm")
    def reset_simple_scope_term(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSimpleScopeTerm", []))

    @jsii.member(jsii_name="resetTagScopeTerm")
    def reset_tag_scope_term(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagScopeTerm", []))

    @builtins.property
    @jsii.member(jsii_name="simpleScopeTerm")
    def simple_scope_term(
        self,
    ) -> "Macie2ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTermOutputReference":
        return typing.cast("Macie2ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTermOutputReference", jsii.get(self, "simpleScopeTerm"))

    @builtins.property
    @jsii.member(jsii_name="tagScopeTerm")
    def tag_scope_term(
        self,
    ) -> "Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermOutputReference":
        return typing.cast("Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermOutputReference", jsii.get(self, "tagScopeTerm"))

    @builtins.property
    @jsii.member(jsii_name="simpleScopeTermInput")
    def simple_scope_term_input(
        self,
    ) -> typing.Optional["Macie2ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTerm"]:
        return typing.cast(typing.Optional["Macie2ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTerm"], jsii.get(self, "simpleScopeTermInput"))

    @builtins.property
    @jsii.member(jsii_name="tagScopeTermInput")
    def tag_scope_term_input(
        self,
    ) -> typing.Optional["Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTerm"]:
        return typing.cast(typing.Optional["Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTerm"], jsii.get(self, "tagScopeTermInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingExcludesAnd, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingExcludesAnd, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingExcludesAnd, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e32bee87e23cdf766651d9a9fb442226ec5dd172cb11ef3df48d2a8840f17951)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTerm",
    jsii_struct_bases=[],
    name_mapping={"comparator": "comparator", "key": "key", "values": "values"},
)
class Macie2ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTerm:
    def __init__(
        self,
        *,
        comparator: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param comparator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#comparator Macie2ClassificationJob#comparator}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#values Macie2ClassificationJob#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ecd05e9cc6f937c1fbd65518d9cdb71fcf3665d590dcc86f7df72d8128d0830e)
            check_type(argname="argument comparator", value=comparator, expected_type=type_hints["comparator"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if comparator is not None:
            self._values["comparator"] = comparator
        if key is not None:
            self._values["key"] = key
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def comparator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#comparator Macie2ClassificationJob#comparator}.'''
        result = self._values.get("comparator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#values Macie2ClassificationJob#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTerm(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Macie2ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTermOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTermOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7823db2e427fcb29f19da1ad7e60c7a8d8fcea7e554e2164496366104f0e4fdf)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetComparator")
    def reset_comparator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComparator", []))

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="comparatorInput")
    def comparator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "comparatorInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="comparator")
    def comparator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comparator"))

    @comparator.setter
    def comparator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c219010d45d5bf6fd7351a08f94b31f07b5ba14985867c9331ccdf6c01606990)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comparator", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c181fd0bdd1d6de522ef8636d96393e4843037652f5ac97af3b0b60723a2e5e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c88040eb63ad57cfc24fd58b2e0da0673193b8b440935e0dfeb668e9a791fb8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTerm]:
        return typing.cast(typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTerm], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTerm],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56a832fd8d729c3c0511acdc8cd6ea2d1c4214560c75a462a2f7083238034f9a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTerm",
    jsii_struct_bases=[],
    name_mapping={
        "comparator": "comparator",
        "key": "key",
        "tag_values": "tagValues",
        "target": "target",
    },
)
class Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTerm:
    def __init__(
        self,
        *,
        comparator: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
        tag_values: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValues", typing.Dict[builtins.str, typing.Any]]]]] = None,
        target: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param comparator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#comparator Macie2ClassificationJob#comparator}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.
        :param tag_values: tag_values block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tag_values Macie2ClassificationJob#tag_values}
        :param target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#target Macie2ClassificationJob#target}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__287f22cc49b92c9808e0d3385efee53dcbe5fb2de5575417f2f0f9c9f6dbc8b8)
            check_type(argname="argument comparator", value=comparator, expected_type=type_hints["comparator"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument tag_values", value=tag_values, expected_type=type_hints["tag_values"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if comparator is not None:
            self._values["comparator"] = comparator
        if key is not None:
            self._values["key"] = key
        if tag_values is not None:
            self._values["tag_values"] = tag_values
        if target is not None:
            self._values["target"] = target

    @builtins.property
    def comparator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#comparator Macie2ClassificationJob#comparator}.'''
        result = self._values.get("comparator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag_values(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValues"]]]:
        '''tag_values block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tag_values Macie2ClassificationJob#tag_values}
        '''
        result = self._values.get("tag_values")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValues"]]], result)

    @builtins.property
    def target(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#target Macie2ClassificationJob#target}.'''
        result = self._values.get("target")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTerm(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6672553f331f0d3e54345d24c8e343a8e780d67d45d32333a69933fe95bd89c7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putTagValues")
    def put_tag_values(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValues", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6459f8f9254d5cfb46573475c382bb43d262f74c8c92ef8507490daee9ff4c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTagValues", [value]))

    @jsii.member(jsii_name="resetComparator")
    def reset_comparator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComparator", []))

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetTagValues")
    def reset_tag_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagValues", []))

    @jsii.member(jsii_name="resetTarget")
    def reset_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTarget", []))

    @builtins.property
    @jsii.member(jsii_name="tagValues")
    def tag_values(
        self,
    ) -> "Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValuesList":
        return typing.cast("Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValuesList", jsii.get(self, "tagValues"))

    @builtins.property
    @jsii.member(jsii_name="comparatorInput")
    def comparator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "comparatorInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="tagValuesInput")
    def tag_values_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValues"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValues"]]], jsii.get(self, "tagValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="comparator")
    def comparator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comparator"))

    @comparator.setter
    def comparator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ee7693f33680c27a043e0c44deb23013e0c4e05510a1d0dc304931a81cb4d2e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comparator", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08e55154317ea3ea50ffefd850adedeab5f1139744318b2ccfe93c1fafab943b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ae2fd1f06b1d710efaf79f9cc76224efc3bd3e401b886177aeb7edcb6f55518)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTerm]:
        return typing.cast(typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTerm], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTerm],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f56f736b26c1cd90b9ceae8d3741bdf230262932de54e63bd162c8d72bf024e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValues",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValues:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#value Macie2ClassificationJob#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1e7dc8d96338febea036773a477493ae51918ca4e2e090dbfee658f0c8e5d59)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#value Macie2ClassificationJob#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValues(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValuesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValuesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d1fa0e640e0520cee49b72e68349d42fb4c8de7f5dfd483d14a801cd8f37c351)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValuesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45c2ad0ab59b37bcfd3ee3c640a3b4b99b22d3865da477e614701463912e0034)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValuesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2d5efebab1baa039e86566b5216f4221b6114541ca60896b977e4df31833d83)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4e5c35a8a63eca3c029d0011a5763addfe9d35982190f621fa3d4140869172dd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7f3623623b00ac195c2ec166a3a17e6fd1b71c3a23867ab11d06a5e4b918e5a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValues]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValues]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValues]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1bb50028bdf3677b9b412918d81432c8c03d19758ce8ae4109d96ee1b66e5911)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValuesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValuesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1b25274174a3689e5169fb637b2f37314b3d8d86ccf0dcac0c4d9e24eb3f4e5b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c533683d30dba2ddc94300fbe5ba91a4584e8f82da5fc280baf09e1e31f60f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a4dbafb887b33becf826aff036f9332567780ee9e14c48666dcabeab0d6afee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValues, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValues, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValues, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb5f78561a808de06673a27d1d1022d2adac860b76f704dc68ecdfd9dbb4a32c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Macie2ClassificationJobS3JobDefinitionScopingExcludesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScopingExcludesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d0831a515a36533fff49100fe5e3c578bc4142f88dc4e0f0a41934f33ef44579)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAnd")
    def put_and(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingExcludesAnd, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d01ad69551529706a89a2832b5d85ae67d8fb6cc5e58a28bbf725d3a02b7d83e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAnd", [value]))

    @jsii.member(jsii_name="resetAnd")
    def reset_and(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnd", []))

    @builtins.property
    @jsii.member(jsii_name="and")
    def and_(self) -> Macie2ClassificationJobS3JobDefinitionScopingExcludesAndList:
        return typing.cast(Macie2ClassificationJobS3JobDefinitionScopingExcludesAndList, jsii.get(self, "and"))

    @builtins.property
    @jsii.member(jsii_name="andInput")
    def and_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionScopingExcludesAnd]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionScopingExcludesAnd]]], jsii.get(self, "andInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingExcludes]:
        return typing.cast(typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingExcludes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingExcludes],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fd55fd082a51e3699b84e4bd14e5e4f5220f7c1f47c23ba3e8cb75370cc5ae9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScopingIncludes",
    jsii_struct_bases=[],
    name_mapping={"and_": "and"},
)
class Macie2ClassificationJobS3JobDefinitionScopingIncludes:
    def __init__(
        self,
        *,
        and_: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["Macie2ClassificationJobS3JobDefinitionScopingIncludesAnd", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param and_: and block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#and Macie2ClassificationJob#and}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06842369ca619917cae9e02d036d96282a7251875ac65779f6953036b0867436)
            check_type(argname="argument and_", value=and_, expected_type=type_hints["and_"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if and_ is not None:
            self._values["and_"] = and_

    @builtins.property
    def and_(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionScopingIncludesAnd"]]]:
        '''and block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#and Macie2ClassificationJob#and}
        '''
        result = self._values.get("and_")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionScopingIncludesAnd"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobS3JobDefinitionScopingIncludes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScopingIncludesAnd",
    jsii_struct_bases=[],
    name_mapping={
        "simple_scope_term": "simpleScopeTerm",
        "tag_scope_term": "tagScopeTerm",
    },
)
class Macie2ClassificationJobS3JobDefinitionScopingIncludesAnd:
    def __init__(
        self,
        *,
        simple_scope_term: typing.Optional[typing.Union["Macie2ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTerm", typing.Dict[builtins.str, typing.Any]]] = None,
        tag_scope_term: typing.Optional[typing.Union["Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTerm", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param simple_scope_term: simple_scope_term block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#simple_scope_term Macie2ClassificationJob#simple_scope_term}
        :param tag_scope_term: tag_scope_term block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tag_scope_term Macie2ClassificationJob#tag_scope_term}
        '''
        if isinstance(simple_scope_term, dict):
            simple_scope_term = Macie2ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTerm(**simple_scope_term)
        if isinstance(tag_scope_term, dict):
            tag_scope_term = Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTerm(**tag_scope_term)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a04aacd2936816f655cb2b5915a6b81ff7d0aae62e5a14ef943e531adb931f0)
            check_type(argname="argument simple_scope_term", value=simple_scope_term, expected_type=type_hints["simple_scope_term"])
            check_type(argname="argument tag_scope_term", value=tag_scope_term, expected_type=type_hints["tag_scope_term"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if simple_scope_term is not None:
            self._values["simple_scope_term"] = simple_scope_term
        if tag_scope_term is not None:
            self._values["tag_scope_term"] = tag_scope_term

    @builtins.property
    def simple_scope_term(
        self,
    ) -> typing.Optional["Macie2ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTerm"]:
        '''simple_scope_term block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#simple_scope_term Macie2ClassificationJob#simple_scope_term}
        '''
        result = self._values.get("simple_scope_term")
        return typing.cast(typing.Optional["Macie2ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTerm"], result)

    @builtins.property
    def tag_scope_term(
        self,
    ) -> typing.Optional["Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTerm"]:
        '''tag_scope_term block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tag_scope_term Macie2ClassificationJob#tag_scope_term}
        '''
        result = self._values.get("tag_scope_term")
        return typing.cast(typing.Optional["Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTerm"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobS3JobDefinitionScopingIncludesAnd(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Macie2ClassificationJobS3JobDefinitionScopingIncludesAndList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScopingIncludesAndList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__631da54bd682a59944f85a52a6afd26afae5c9b5b9360d42e4d77f51f0b01841)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Macie2ClassificationJobS3JobDefinitionScopingIncludesAndOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b484790a14b8b7b073cc3a849b29283722fbdb28872706e1d9603b774b10d72b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Macie2ClassificationJobS3JobDefinitionScopingIncludesAndOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28f28ad30ccc7eb11068c4e278f39da89b1931958ea8321bfbc399135e8c0977)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8339da166dec7bffb66baf48b57cba6aaee2e4878f788b33252005498899fbda)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ffc88483b1f7ca07c012be3287e942682696b08c53042db362f251968e5ad502)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionScopingIncludesAnd]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionScopingIncludesAnd]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionScopingIncludesAnd]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24962052a9f70bbb56ebdfa51b330a0da87b8c483746cc4ee774fcadc962bd0d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Macie2ClassificationJobS3JobDefinitionScopingIncludesAndOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScopingIncludesAndOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__14d63279d2ef8ac87dd17054638c8a0738c486e57fbf1514b11554fc9c84e9b2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putSimpleScopeTerm")
    def put_simple_scope_term(
        self,
        *,
        comparator: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param comparator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#comparator Macie2ClassificationJob#comparator}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#values Macie2ClassificationJob#values}.
        '''
        value = Macie2ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTerm(
            comparator=comparator, key=key, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putSimpleScopeTerm", [value]))

    @jsii.member(jsii_name="putTagScopeTerm")
    def put_tag_scope_term(
        self,
        *,
        comparator: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
        tag_values: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValues", typing.Dict[builtins.str, typing.Any]]]]] = None,
        target: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param comparator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#comparator Macie2ClassificationJob#comparator}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.
        :param tag_values: tag_values block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tag_values Macie2ClassificationJob#tag_values}
        :param target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#target Macie2ClassificationJob#target}.
        '''
        value = Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTerm(
            comparator=comparator, key=key, tag_values=tag_values, target=target
        )

        return typing.cast(None, jsii.invoke(self, "putTagScopeTerm", [value]))

    @jsii.member(jsii_name="resetSimpleScopeTerm")
    def reset_simple_scope_term(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSimpleScopeTerm", []))

    @jsii.member(jsii_name="resetTagScopeTerm")
    def reset_tag_scope_term(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagScopeTerm", []))

    @builtins.property
    @jsii.member(jsii_name="simpleScopeTerm")
    def simple_scope_term(
        self,
    ) -> "Macie2ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTermOutputReference":
        return typing.cast("Macie2ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTermOutputReference", jsii.get(self, "simpleScopeTerm"))

    @builtins.property
    @jsii.member(jsii_name="tagScopeTerm")
    def tag_scope_term(
        self,
    ) -> "Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermOutputReference":
        return typing.cast("Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermOutputReference", jsii.get(self, "tagScopeTerm"))

    @builtins.property
    @jsii.member(jsii_name="simpleScopeTermInput")
    def simple_scope_term_input(
        self,
    ) -> typing.Optional["Macie2ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTerm"]:
        return typing.cast(typing.Optional["Macie2ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTerm"], jsii.get(self, "simpleScopeTermInput"))

    @builtins.property
    @jsii.member(jsii_name="tagScopeTermInput")
    def tag_scope_term_input(
        self,
    ) -> typing.Optional["Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTerm"]:
        return typing.cast(typing.Optional["Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTerm"], jsii.get(self, "tagScopeTermInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingIncludesAnd, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingIncludesAnd, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingIncludesAnd, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06f359f4b52d012214913b567217182e175210b128971490afd426f02b2e8fb0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTerm",
    jsii_struct_bases=[],
    name_mapping={"comparator": "comparator", "key": "key", "values": "values"},
)
class Macie2ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTerm:
    def __init__(
        self,
        *,
        comparator: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param comparator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#comparator Macie2ClassificationJob#comparator}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#values Macie2ClassificationJob#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73636fc09fdc635d9559951c7757e0675606d54965fe0952ebe99d8ab5b256e4)
            check_type(argname="argument comparator", value=comparator, expected_type=type_hints["comparator"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if comparator is not None:
            self._values["comparator"] = comparator
        if key is not None:
            self._values["key"] = key
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def comparator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#comparator Macie2ClassificationJob#comparator}.'''
        result = self._values.get("comparator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#values Macie2ClassificationJob#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTerm(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Macie2ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTermOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTermOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8c20f977b74fcaf49623c024d5ef2e791ca3da997d201bd7f61f85e271bc4bfb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetComparator")
    def reset_comparator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComparator", []))

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="comparatorInput")
    def comparator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "comparatorInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="comparator")
    def comparator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comparator"))

    @comparator.setter
    def comparator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__198737af9a6efc6aa05c604513ad660a6ec3f6201976fd9b0e7631afb31d64ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comparator", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__093ceb7a75df38a66bc90a19a2106be22c47654d5a7e32919580bfb4dcb844fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c49a49a4b6cce01301acd1bb9c69b0ac9b01f4ad339312bd5e066053438f974)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTerm]:
        return typing.cast(typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTerm], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTerm],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c08f786bacc0a81530d00e84505c0234206e8f60600c90189210874252888171)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTerm",
    jsii_struct_bases=[],
    name_mapping={
        "comparator": "comparator",
        "key": "key",
        "tag_values": "tagValues",
        "target": "target",
    },
)
class Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTerm:
    def __init__(
        self,
        *,
        comparator: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
        tag_values: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValues", typing.Dict[builtins.str, typing.Any]]]]] = None,
        target: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param comparator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#comparator Macie2ClassificationJob#comparator}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.
        :param tag_values: tag_values block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tag_values Macie2ClassificationJob#tag_values}
        :param target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#target Macie2ClassificationJob#target}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26614fee4ef5ffe2dc84206a86683009a4e9850cea901757388efe52c76a30e3)
            check_type(argname="argument comparator", value=comparator, expected_type=type_hints["comparator"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument tag_values", value=tag_values, expected_type=type_hints["tag_values"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if comparator is not None:
            self._values["comparator"] = comparator
        if key is not None:
            self._values["key"] = key
        if tag_values is not None:
            self._values["tag_values"] = tag_values
        if target is not None:
            self._values["target"] = target

    @builtins.property
    def comparator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#comparator Macie2ClassificationJob#comparator}.'''
        result = self._values.get("comparator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag_values(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValues"]]]:
        '''tag_values block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tag_values Macie2ClassificationJob#tag_values}
        '''
        result = self._values.get("tag_values")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValues"]]], result)

    @builtins.property
    def target(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#target Macie2ClassificationJob#target}.'''
        result = self._values.get("target")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTerm(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__80ca8c015b88b7b47b484e63155470a2b7b750ef336838a45d5066997db304fa)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putTagValues")
    def put_tag_values(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValues", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e7b4be4aaefdc697fd38ab987d8f179e517ba4a7b5b2f0dd8cf348163f1b471)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTagValues", [value]))

    @jsii.member(jsii_name="resetComparator")
    def reset_comparator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComparator", []))

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetTagValues")
    def reset_tag_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagValues", []))

    @jsii.member(jsii_name="resetTarget")
    def reset_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTarget", []))

    @builtins.property
    @jsii.member(jsii_name="tagValues")
    def tag_values(
        self,
    ) -> "Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValuesList":
        return typing.cast("Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValuesList", jsii.get(self, "tagValues"))

    @builtins.property
    @jsii.member(jsii_name="comparatorInput")
    def comparator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "comparatorInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="tagValuesInput")
    def tag_values_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValues"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValues"]]], jsii.get(self, "tagValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="comparator")
    def comparator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comparator"))

    @comparator.setter
    def comparator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c08cd9029085f142d0134d0ced45dc86afd1ae90cc5eaeda3f1ae06d0854cf5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comparator", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf6329b5f6159f227492bd6a0a1fa6f14cb5e656611722edc043a96dab9caf1d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcad91a4f2fccc1d1de58be6add8d3c6339f6b70aa82e65cfb21611b80d9f37e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTerm]:
        return typing.cast(typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTerm], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTerm],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69e7d7c54154fdac233032aad08de3174efc96f8405d360371a17250c93b1aa1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValues",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValues:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#value Macie2ClassificationJob#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be89ae5bfa844ad021c2eb24830b63cba0e86ed8144f4c8d3a2789800a3b4ca1)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#value Macie2ClassificationJob#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValues(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValuesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValuesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6d309cefce9a6e40bb0c66ca3e83c260358d7cdf10b7f4eef96e09a56f70f2d4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValuesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26051d24aec3481fad573c91bfaf5d95709822a85bbd26a55fcf0a43b9acb751)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValuesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__888486e6a983f3e0192e03c5e75fe03f75680e7e4d2ef536cd61bfcac3d5cc9a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8b14265c7371d31a50d5bc16985f12193d3067370b524736e235706cee5374fb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__75967fa4b24981c42d641bac3ec094614977cf5d656bee1ac96fcb371d50b152)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValues]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValues]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValues]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6fba78e9da0ca084788a5ae2c99de296b00e8a87256908dfe15baaaba7c486e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValuesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValuesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__27dfb408acabb5e01cc2078e99564cb2ea90ea939d76a367a97b33a004a39a40)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0408ed3e94ce74d58b7511e7d8ab0e0ae5624a7d97e95e1d598cf53aa1b0f441)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccb592adb19f39b774a521413f155c8ff5df910e427803e4cb1c4e1a026bb257)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValues, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValues, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValues, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd2c82fbbe7c99e645a4f64ecebc74f1c730c834da6bb7c72a6f7f9633e01866)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Macie2ClassificationJobS3JobDefinitionScopingIncludesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScopingIncludesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__994ffc89e4d05b4dfe6f1e7d1f837ac973b53e3dae4c85cb9f9e1f68d33a5cc5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAnd")
    def put_and(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingIncludesAnd, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__569639261bf3aac3d8669941b6c33bbe65536821728ddb61dd8ef02637685409)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAnd", [value]))

    @jsii.member(jsii_name="resetAnd")
    def reset_and(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnd", []))

    @builtins.property
    @jsii.member(jsii_name="and")
    def and_(self) -> Macie2ClassificationJobS3JobDefinitionScopingIncludesAndList:
        return typing.cast(Macie2ClassificationJobS3JobDefinitionScopingIncludesAndList, jsii.get(self, "and"))

    @builtins.property
    @jsii.member(jsii_name="andInput")
    def and_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionScopingIncludesAnd]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionScopingIncludesAnd]]], jsii.get(self, "andInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingIncludes]:
        return typing.cast(typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingIncludes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingIncludes],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3380e2c6fd9dd18dfeeca2343a5ad8c42ad8c0cd20abaee08f1b53f07d3ac245)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Macie2ClassificationJobS3JobDefinitionScopingOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScopingOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__14daa3eb05efadb9cf1f37f1c2b04e5a09c8e40adb95987a22d6b88837e65b04)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putExcludes")
    def put_excludes(
        self,
        *,
        and_: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingExcludesAnd, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param and_: and block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#and Macie2ClassificationJob#and}
        '''
        value = Macie2ClassificationJobS3JobDefinitionScopingExcludes(and_=and_)

        return typing.cast(None, jsii.invoke(self, "putExcludes", [value]))

    @jsii.member(jsii_name="putIncludes")
    def put_includes(
        self,
        *,
        and_: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingIncludesAnd, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param and_: and block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#and Macie2ClassificationJob#and}
        '''
        value = Macie2ClassificationJobS3JobDefinitionScopingIncludes(and_=and_)

        return typing.cast(None, jsii.invoke(self, "putIncludes", [value]))

    @jsii.member(jsii_name="resetExcludes")
    def reset_excludes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcludes", []))

    @jsii.member(jsii_name="resetIncludes")
    def reset_includes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludes", []))

    @builtins.property
    @jsii.member(jsii_name="excludes")
    def excludes(
        self,
    ) -> Macie2ClassificationJobS3JobDefinitionScopingExcludesOutputReference:
        return typing.cast(Macie2ClassificationJobS3JobDefinitionScopingExcludesOutputReference, jsii.get(self, "excludes"))

    @builtins.property
    @jsii.member(jsii_name="includes")
    def includes(
        self,
    ) -> Macie2ClassificationJobS3JobDefinitionScopingIncludesOutputReference:
        return typing.cast(Macie2ClassificationJobS3JobDefinitionScopingIncludesOutputReference, jsii.get(self, "includes"))

    @builtins.property
    @jsii.member(jsii_name="excludesInput")
    def excludes_input(
        self,
    ) -> typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingExcludes]:
        return typing.cast(typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingExcludes], jsii.get(self, "excludesInput"))

    @builtins.property
    @jsii.member(jsii_name="includesInput")
    def includes_input(
        self,
    ) -> typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingIncludes]:
        return typing.cast(typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingIncludes], jsii.get(self, "includesInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Macie2ClassificationJobS3JobDefinitionScoping]:
        return typing.cast(typing.Optional[Macie2ClassificationJobS3JobDefinitionScoping], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Macie2ClassificationJobS3JobDefinitionScoping],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5deb29cb553e2e0e7cec21464ac22d4b7bc0a20f512be372ce02f07793543377)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobScheduleFrequency",
    jsii_struct_bases=[],
    name_mapping={
        "daily_schedule": "dailySchedule",
        "monthly_schedule": "monthlySchedule",
        "weekly_schedule": "weeklySchedule",
    },
)
class Macie2ClassificationJobScheduleFrequency:
    def __init__(
        self,
        *,
        daily_schedule: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        monthly_schedule: typing.Optional[jsii.Number] = None,
        weekly_schedule: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param daily_schedule: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#daily_schedule Macie2ClassificationJob#daily_schedule}.
        :param monthly_schedule: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#monthly_schedule Macie2ClassificationJob#monthly_schedule}.
        :param weekly_schedule: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#weekly_schedule Macie2ClassificationJob#weekly_schedule}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae5b87cde2ef005ab0ca67021c81f5589eea53fd4bd9df06a19d9b80c669148d)
            check_type(argname="argument daily_schedule", value=daily_schedule, expected_type=type_hints["daily_schedule"])
            check_type(argname="argument monthly_schedule", value=monthly_schedule, expected_type=type_hints["monthly_schedule"])
            check_type(argname="argument weekly_schedule", value=weekly_schedule, expected_type=type_hints["weekly_schedule"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if daily_schedule is not None:
            self._values["daily_schedule"] = daily_schedule
        if monthly_schedule is not None:
            self._values["monthly_schedule"] = monthly_schedule
        if weekly_schedule is not None:
            self._values["weekly_schedule"] = weekly_schedule

    @builtins.property
    def daily_schedule(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#daily_schedule Macie2ClassificationJob#daily_schedule}.'''
        result = self._values.get("daily_schedule")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def monthly_schedule(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#monthly_schedule Macie2ClassificationJob#monthly_schedule}.'''
        result = self._values.get("monthly_schedule")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def weekly_schedule(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#weekly_schedule Macie2ClassificationJob#weekly_schedule}.'''
        result = self._values.get("weekly_schedule")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobScheduleFrequency(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Macie2ClassificationJobScheduleFrequencyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobScheduleFrequencyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cfb105334eb32b4cc713895882e8e76b006496ee9c472fc2964cedc03a8903fe)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDailySchedule")
    def reset_daily_schedule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDailySchedule", []))

    @jsii.member(jsii_name="resetMonthlySchedule")
    def reset_monthly_schedule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMonthlySchedule", []))

    @jsii.member(jsii_name="resetWeeklySchedule")
    def reset_weekly_schedule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeeklySchedule", []))

    @builtins.property
    @jsii.member(jsii_name="dailyScheduleInput")
    def daily_schedule_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "dailyScheduleInput"))

    @builtins.property
    @jsii.member(jsii_name="monthlyScheduleInput")
    def monthly_schedule_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "monthlyScheduleInput"))

    @builtins.property
    @jsii.member(jsii_name="weeklyScheduleInput")
    def weekly_schedule_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "weeklyScheduleInput"))

    @builtins.property
    @jsii.member(jsii_name="dailySchedule")
    def daily_schedule(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "dailySchedule"))

    @daily_schedule.setter
    def daily_schedule(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af7df7b4c8188973a9421e72e7185ce547a3e82afdf3573dfbd3dcc5c8c2c385)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dailySchedule", value)

    @builtins.property
    @jsii.member(jsii_name="monthlySchedule")
    def monthly_schedule(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "monthlySchedule"))

    @monthly_schedule.setter
    def monthly_schedule(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7df020595cad9fb059f362af7a9212fc4654faa9b2ec13d25b51990fe0ee37b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "monthlySchedule", value)

    @builtins.property
    @jsii.member(jsii_name="weeklySchedule")
    def weekly_schedule(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "weeklySchedule"))

    @weekly_schedule.setter
    def weekly_schedule(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d6ae1cb8e24af7c3d1fdf8a352c49bedd1670f4c42b34f0a1ae38361d57d408)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weeklySchedule", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Macie2ClassificationJobScheduleFrequency]:
        return typing.cast(typing.Optional[Macie2ClassificationJobScheduleFrequency], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Macie2ClassificationJobScheduleFrequency],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca3ffd1fac104e3788d5e5d0baf18695d09d135dd4be9975929aca39c8323d4b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobUserPausedDetails",
    jsii_struct_bases=[],
    name_mapping={},
)
class Macie2ClassificationJobUserPausedDetails:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobUserPausedDetails(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Macie2ClassificationJobUserPausedDetailsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobUserPausedDetailsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d81ab2ea6fb1a496dcfea7928f0ee4372af664828e7e0960fdd3ca4bef5b3c2e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Macie2ClassificationJobUserPausedDetailsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24f7c68772a55ba6f085b7549105826a3afe60bc6149c456c7b78f43a7502be1)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Macie2ClassificationJobUserPausedDetailsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c6a8814a4b31c3e7335437a315b2c84e60769d0297e217da54f6df2e7103091)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e6521e198f09902194bd40eaa3c850c2789b1b2269aaf53bd8e96736439920c1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c000a9bfe7f0f9fad94e236a8a690ee9859d142194b851320065e82a233e0e54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Macie2ClassificationJobUserPausedDetailsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.macie2ClassificationJob.Macie2ClassificationJobUserPausedDetailsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e55d2cf82623480f25e8cb353efc24f9006492cdd977e0d3bd497627c958a17b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="jobExpiresAt")
    def job_expires_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jobExpiresAt"))

    @builtins.property
    @jsii.member(jsii_name="jobImminentExpirationHealthEventArn")
    def job_imminent_expiration_health_event_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jobImminentExpirationHealthEventArn"))

    @builtins.property
    @jsii.member(jsii_name="jobPausedAt")
    def job_paused_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jobPausedAt"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Macie2ClassificationJobUserPausedDetails]:
        return typing.cast(typing.Optional[Macie2ClassificationJobUserPausedDetails], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Macie2ClassificationJobUserPausedDetails],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d5f781393d75439ae251923df6c0b272a1078cfa91af731ca9d418a90cdb0f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Macie2ClassificationJob",
    "Macie2ClassificationJobConfig",
    "Macie2ClassificationJobS3JobDefinition",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteria",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludes",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAnd",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndList",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndOutputReference",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterion",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterionOutputReference",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterion",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionOutputReference",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValues",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValuesList",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValuesOutputReference",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesOutputReference",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludes",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAnd",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndList",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndOutputReference",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterion",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterionOutputReference",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterion",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionOutputReference",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValues",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValuesList",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValuesOutputReference",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesOutputReference",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteriaOutputReference",
    "Macie2ClassificationJobS3JobDefinitionBucketDefinitions",
    "Macie2ClassificationJobS3JobDefinitionBucketDefinitionsList",
    "Macie2ClassificationJobS3JobDefinitionBucketDefinitionsOutputReference",
    "Macie2ClassificationJobS3JobDefinitionOutputReference",
    "Macie2ClassificationJobS3JobDefinitionScoping",
    "Macie2ClassificationJobS3JobDefinitionScopingExcludes",
    "Macie2ClassificationJobS3JobDefinitionScopingExcludesAnd",
    "Macie2ClassificationJobS3JobDefinitionScopingExcludesAndList",
    "Macie2ClassificationJobS3JobDefinitionScopingExcludesAndOutputReference",
    "Macie2ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTerm",
    "Macie2ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTermOutputReference",
    "Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTerm",
    "Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermOutputReference",
    "Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValues",
    "Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValuesList",
    "Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValuesOutputReference",
    "Macie2ClassificationJobS3JobDefinitionScopingExcludesOutputReference",
    "Macie2ClassificationJobS3JobDefinitionScopingIncludes",
    "Macie2ClassificationJobS3JobDefinitionScopingIncludesAnd",
    "Macie2ClassificationJobS3JobDefinitionScopingIncludesAndList",
    "Macie2ClassificationJobS3JobDefinitionScopingIncludesAndOutputReference",
    "Macie2ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTerm",
    "Macie2ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTermOutputReference",
    "Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTerm",
    "Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermOutputReference",
    "Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValues",
    "Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValuesList",
    "Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValuesOutputReference",
    "Macie2ClassificationJobS3JobDefinitionScopingIncludesOutputReference",
    "Macie2ClassificationJobS3JobDefinitionScopingOutputReference",
    "Macie2ClassificationJobScheduleFrequency",
    "Macie2ClassificationJobScheduleFrequencyOutputReference",
    "Macie2ClassificationJobUserPausedDetails",
    "Macie2ClassificationJobUserPausedDetailsList",
    "Macie2ClassificationJobUserPausedDetailsOutputReference",
]

publication.publish()

def _typecheckingstub__0c60608cdd135982815c6aead769e77b1a2c641a6ea5b15189cd07728a81f4d4(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    job_type: builtins.str,
    s3_job_definition: typing.Union[Macie2ClassificationJobS3JobDefinition, typing.Dict[builtins.str, typing.Any]],
    custom_data_identifier_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    initial_run: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    job_status: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    name_prefix: typing.Optional[builtins.str] = None,
    sampling_percentage: typing.Optional[jsii.Number] = None,
    schedule_frequency: typing.Optional[typing.Union[Macie2ClassificationJobScheduleFrequency, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__246db55292490e495687a674321e3a4ab8cc2e9ad105efe5d832f9aea48c0987(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__566543b99f28defde976a8123bc284500b953814d089b5be1d929ccc2eeaf8cf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__812c557f42398edd1275b4d28d58bc992dfb745aebbbbe8329d8c7b81d5cf88e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ea1a93ca9d9feae381ed91d0725247c3afe482a637c400871806e994c7f37d5(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a93468f4a7bfca255e5a0c6a504d141286a0161de45b00104b6230400ad8be0e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34b98ab1d4aa35157626bbb44e1e4c0b16a7cc0ac61f5747627289747a6cba06(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4538d1d9abd5c8d9e1474541bac86a51b3f0a3298effbf3bb87f265bf0f4197(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__096253b063d628cbab50b72c6e89d665580a2b9f519f0f0961388a0f0aada687(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4db7c4d101b5d9873a97b2457a0c4e40c3988290f00bd37a7cbbabe8b765f3c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40990567144066848d837796118c240980f4d58ab1f12a12ecbb3aa187d6a231(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4dc087767d1c78cb56e8bc404a5f2c3394738e61c97b619d2e635782d1e13f95(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68d84991a1ca5cfa5330567874a105f9c96eec75fa5ac4348173f37215a1ab29(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    job_type: builtins.str,
    s3_job_definition: typing.Union[Macie2ClassificationJobS3JobDefinition, typing.Dict[builtins.str, typing.Any]],
    custom_data_identifier_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    initial_run: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    job_status: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    name_prefix: typing.Optional[builtins.str] = None,
    sampling_percentage: typing.Optional[jsii.Number] = None,
    schedule_frequency: typing.Optional[typing.Union[Macie2ClassificationJobScheduleFrequency, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__299e0be4b73b7706d5edd9ad17d7d84df687cc396d57e0c4e3da38826b5e48c6(
    *,
    bucket_criteria: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteria, typing.Dict[builtins.str, typing.Any]]] = None,
    bucket_definitions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketDefinitions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    scoping: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionScoping, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b967abe6dd80dee428d8fbbd912ecd626341f52d7918a873a3261afd0c5ca5cb(
    *,
    excludes: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludes, typing.Dict[builtins.str, typing.Any]]] = None,
    includes: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludes, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10f235eb87fd8d2bd659fa8c65503d40b1f9a2bc945618b44039439f6340d514(
    *,
    and_: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAnd, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34e793860c01868187bebbef381c8291f6b5596669978886028a534293614710(
    *,
    simple_criterion: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterion, typing.Dict[builtins.str, typing.Any]]] = None,
    tag_criterion: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterion, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bceb8803ceb9f035b85cb0f0fd623a752a65db1e45c300e1f989e55f62727e03(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4edb837628fb01e2c2dfffbf20777f2561e63d4c5e6a623b64a44689a76dae5(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41c7966dd61874c2b954a6e883a600872ac82a194b1888b2d85ff662a1b6f343(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfc80802b5aa955124bf38f428e3d0b479c0192de3925aa3e42c8ceecc79add4(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9786af677c1f66c8ef035a220937a7df91cd16ed58ff5c775b417490ca67a593(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb07ed31777bd6a551e3bad4000b77cbdc8f964b8cb9e7ee01b3e2cdb214e76f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAnd]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47b14003235d1583d6675dff67d695ebbd39dcef8dad45fd043cc1bb7e7a8387(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59fbcad040e0c5875bae44488639932d8ed9ea01d4a3161d4af2c30e6a11e9fb(
    value: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAnd, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12f4faa91f1fa270ee55957690dd526ee51df7e9f90d50f5929e425276070b47(
    *,
    comparator: typing.Optional[builtins.str] = None,
    key: typing.Optional[builtins.str] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eacf8747df322bac3645ebd753831d8db90073c7095efcfcee22d41badd131a1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b610a6e7dfacb3bb8c4dffc5388ab6fb0ff22b1df22b9ea606c62fb78f6bc950(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__393175a56d7b67e0e92e2eb21f2578c4c6df90fdfc0df5644548f99a982aac05(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12574c001ccbee3ab5c61920ed8c832b96873d3da46d42d61ea9701af0c431b6(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25b6c646fc1a6208287ae9e58de75cbe67253e15a26fc306629942dc0503efa6(
    value: typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterion],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1e26fe7b2a5af7add9ae9908568a7972417f2c093db03f3129d6d137f645306(
    *,
    comparator: typing.Optional[builtins.str] = None,
    tag_values: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValues, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ac2fbc1d9f20581516b3b40ea0d60088118306cb8bb421b34b93a741293d59e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a9774a6ecf025908499bb39a8e668464269cbdeb65862d55f92e4b357f67683(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValues, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98c4a8b4682ba0b5aa6f1c0ec585c5a21ff26686880777e28fd92c9ab30ba6ed(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55c5c560d28e2e6767bb8c3b13ed7202d6bd5c08349c989a7ef033831e8cf761(
    value: typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterion],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d1c5857c1ed00a1aa0b535755c57ff1637da456c6a6d65b01e14faa47efed88(
    *,
    key: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dac37afbb1b0d9ad9401d8735468c1b4ab7eeeb1b11da6bc6d5f33d7fd68a9b5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b3da7620b6496bf9d21588f6eb36d854e5a877db619e3baaa4a2d194a94b873(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82511a0fe1f839aa63a1df261f5f50ad00875b8a71464f0c8a081dfc410b07c8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8f5c87d9634a71ddbc521fb1aeca76cd6d9f1b4d826489a59829ebdb9361434(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d575af88282ea7329d000328344215039d4f896f15b854487fd497955ec6ec8f(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0729f8e449649252559f015b923a02a671988344071acf1ba4347ffe116fb58(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValues]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38a8d736919ed7b5f4be61e9bdb1f4f1fb5883818f975b3dca55235bb0f3f567(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75a0584e0eda5d930967ee00e055fe1f8a1895e8520dbdf50512f8f0f8141830(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19a43f6a20e6400f6dfb61aa3de5eacaf0c14052e41db57187b156eefec25eec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9743b6cba2357c3cc7107abfc2bea4b31f74a99cc4f14cc61513eb5095a54da7(
    value: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValues, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcb42fec85b4927e00c9a6a543866d5e4b4a8a75e5b70ff0098f15713a733885(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bca0084c68d6aac4e74ff610f3930a3b8969341f4b0645aa8a75643cb826fec(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAnd, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4683c4d9bcbb5b522463542ec61f0fa611764ae6081de75ec976bf6a14f3d31f(
    value: typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludes],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f096f1c4f5ef744c3d9dbe0f48cab00c3ef3470ba78ca2fd715e4ca8fbf2bbc(
    *,
    and_: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAnd, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1df810c7d279cd8031ebfe0811094de80563dc8cdaa1d4c9adbec46c7cd387eb(
    *,
    simple_criterion: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterion, typing.Dict[builtins.str, typing.Any]]] = None,
    tag_criterion: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterion, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ea05f92b1bfbe0701748d547ea4177cafc9bd078c3707722776abceef19cc9f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d19409d954e05922523c7184e74ca52b80637f544462f90ce3f24479432a18b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc64aa24ec06a43ee894df5577a4887b8e28c996c7bc1ad2cacb09adf6964583(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76fa5899d5a972f88d89427f5c6e7ea3b8f354272a79faa374e57a96aa11c882(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ad001115bb57b0530fac641d4299af5e09fcbbcecb39180cf3d20cf2116e558(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03ab8fddda5facfe0c312c3b325839ba9820b64c91db29bd8c71ca7a11f5cd4f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAnd]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2ff3fabd254fcce24c18c947d0d5e9d7e29bbcd97e8b2e95311bc5b1b405372(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7f3322170422115c11584b2afd244b63fc87417e6d784b44897771add390f09(
    value: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAnd, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__521249f8cd606a4bf3b49d72ece182a520e449a3824b7acb3d6c5f7a9dfea75e(
    *,
    comparator: typing.Optional[builtins.str] = None,
    key: typing.Optional[builtins.str] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7246cb2c7f72cb46b42d6dcdcf8d96888c7e4dfecae44e6f8c723ae92f4578cd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c93be186a0fe811669d55bc251c2b44e50a4b0d34fb1d3a8675a335e07142643(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae9210c26b95d4a8da3422779650b0b150e24bb4ac572d4ac591e7716a6ee8dc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bab60789f86de021634fcd613c8f77cd2a2e0f9659c8ddf6ce3d50e8de598277(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73d798f7a70387ca0ecdac121b192a77e247d9de123878735a6672ef4fca7adc(
    value: typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterion],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1be5327d5f9656b7a962422b0f3f911abea8a7041f9e8fcbc00393d1cd302e0(
    *,
    comparator: typing.Optional[builtins.str] = None,
    tag_values: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValues, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f40aa6486b25d9b2e65179634b09ba5c68fcb586ead5640d6f8e75127f0559fe(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a35b6676beb6660dea0f332d7af61fb8633cfe61a8fa0a32482564abaff41d1(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValues, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25dca5a8d805d1560e2c5647b708fc775eb3bcbdbaf239f3376e8bae73496c37(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__993b126fb5cc5f3f339a1c6211383a036d9a4a573d9097a1767f6d6dc02d5e08(
    value: typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterion],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36dec0f8be75976f659445070b34938f30ab44076086c55a15822c30ce1ebe71(
    *,
    key: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b950b8b5605aa483fb9c61b6841cac97818b468d12a72223e7497ab28f63c8dc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0802966037690a1f3c5d98fcbe7fa5da3625572b87b44d4c305861b9f1a5939c(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24b4cb3bbed190aba800763d168aabe2319075dc098b9baafc42fed06f489e59(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b06ce0d63905571808ff0d4286abcb9faf012bd01653e4681ed102eb9a2fba7b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac6b8fa58f3bd17e820197dbd0ab37ee8726cab728231c170435c6fd11646b07(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9058dd8eba63251ef97730d319733abc46d5eeb2250ec54b7aa1cd3328bc24fb(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValues]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ecdf198ae7bda2fbc77a7ce8696e759f62da77cf0b8529b5dc318886b0c85b8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc078da59b5525e661314a1ef0687e333e76159408635a9c3c5b8193c3a13260(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1fd66476af4aba2da2679d56066ee098cd2e658bc604564abf15a5c2ae0cf4f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bfad72aa0a0bfb7728043a74e38751a8e399ffd37205910818c7690e69e1df8(
    value: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValues, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f41b5139771fbe8362fabd8b3d9ccda0294afb7323deff3c7b006e2c6e82d42(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72c043225f11263f02e88c2f89824d4bc5083261f1504d9f2217e6c4442f79c2(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAnd, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5edac7d6d88975541d0b4c96cb7857821b679ddbd57959dd985ef1e8d371ce9(
    value: typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludes],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3fc0fc9197148e7b2e70f24b9860fc55098133735abccd37cea6ab7f1a53c34(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2083860869af831b88132587ec986ae4c896847a23c5ba222c4e79eea471ff4f(
    value: typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteria],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__949b094635f62b35ac156294d4e00ef1c0d1c2bd36f80c92456c5aaa563af5e5(
    *,
    account_id: builtins.str,
    buckets: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__827eeee482924af7e04458eee4f0d41e1077b79b8eb2112c39b4bd1ad49fd196(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aff908f2ae46e689ffc9cf1ef0991a4ea9b418d3b10cbd8e916e9475b0ce30c4(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dec0a4bd3ea4c6dd51ad83f9f85ba8120af52b345687b739fd770da942ccf015(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21a235b68506ede23423917d6f3d75fc470fe920a24f054ce66263c84ef9420a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78bcafecde60cc872055d64cf901b88d94339f7b3600d5c5442454cbf8d14242(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__408952b23479c875701d78ef366cdb80318a28d79e92faa6b1f02070c014ea4f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketDefinitions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8408f1865e1532900701bf904da6858721fbee34cf244bd43efc541352518da5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26157eb24634030b03e9562008c4060b42a150e5738de3fb5653de026044cd63(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63b31d11a4d4c3db103288e75eb612b0cc66a88c907dd0392a12195470cd22c1(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01fb53968967191b486093e539e6e868709d922dce5ae1508eec7fe5796e8dce(
    value: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketDefinitions, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7198db672485d06126033ed1d8928f0d61cad30b55935e47c526de10d1719bdc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5af5c86ade2e2488350a1c5e5b76d33b1151eb760317e0c02a353e51fedab31c(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketDefinitions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37d2937424ecfb8a0010c1af6c09a0d7af93b73601df30058275d1d29c21810d(
    value: typing.Optional[Macie2ClassificationJobS3JobDefinition],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddf5bb27ee23f2cb701964453e01dc0d886666dca7586e48a71a00eff41ca8d1(
    *,
    excludes: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingExcludes, typing.Dict[builtins.str, typing.Any]]] = None,
    includes: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingIncludes, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9c62acb84226daa72411ac239e6a971074b8baad32af4a3e057f8df302bd6b1(
    *,
    and_: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingExcludesAnd, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cac7696b55e5ebcb03ab150fe9a1bc74bb324296ca3de2ca7dc118330bd29411(
    *,
    simple_scope_term: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTerm, typing.Dict[builtins.str, typing.Any]]] = None,
    tag_scope_term: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTerm, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a727a814d840b2749f6d6e89e5da52a92d42b0a5400ba8024f08f6f7bc6aabf2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__300fbc1d5307084e3149863389f49b3e9ddfc5e2e57a4a9de4b3a9c717c9b43f(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cc56fdfb10ccb4e92bfb710619abf8ad1db18c4341cfa13b0bfc56906e5483b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb8a5c0a3800b70552f85f90dd6e11d9ea560d8b7db24f313c1b40abc1fb0bd8(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57dfab36deb7b9b1251963026739f29e230d09de2e7822dcbd759d439b3f1809(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24e6e007d9bca1d3fee5ce3aff552290218385b88513987d678511685746712d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionScopingExcludesAnd]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6f5fcdbfb9613248fd9855a8ab587cfaaa547557c94d956c180dd7b117e0258(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e32bee87e23cdf766651d9a9fb442226ec5dd172cb11ef3df48d2a8840f17951(
    value: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingExcludesAnd, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecd05e9cc6f937c1fbd65518d9cdb71fcf3665d590dcc86f7df72d8128d0830e(
    *,
    comparator: typing.Optional[builtins.str] = None,
    key: typing.Optional[builtins.str] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7823db2e427fcb29f19da1ad7e60c7a8d8fcea7e554e2164496366104f0e4fdf(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c219010d45d5bf6fd7351a08f94b31f07b5ba14985867c9331ccdf6c01606990(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c181fd0bdd1d6de522ef8636d96393e4843037652f5ac97af3b0b60723a2e5e1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c88040eb63ad57cfc24fd58b2e0da0673193b8b440935e0dfeb668e9a791fb8(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56a832fd8d729c3c0511acdc8cd6ea2d1c4214560c75a462a2f7083238034f9a(
    value: typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTerm],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__287f22cc49b92c9808e0d3385efee53dcbe5fb2de5575417f2f0f9c9f6dbc8b8(
    *,
    comparator: typing.Optional[builtins.str] = None,
    key: typing.Optional[builtins.str] = None,
    tag_values: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValues, typing.Dict[builtins.str, typing.Any]]]]] = None,
    target: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6672553f331f0d3e54345d24c8e343a8e780d67d45d32333a69933fe95bd89c7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6459f8f9254d5cfb46573475c382bb43d262f74c8c92ef8507490daee9ff4c7(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValues, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ee7693f33680c27a043e0c44deb23013e0c4e05510a1d0dc304931a81cb4d2e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08e55154317ea3ea50ffefd850adedeab5f1139744318b2ccfe93c1fafab943b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ae2fd1f06b1d710efaf79f9cc76224efc3bd3e401b886177aeb7edcb6f55518(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f56f736b26c1cd90b9ceae8d3741bdf230262932de54e63bd162c8d72bf024e7(
    value: typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTerm],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1e7dc8d96338febea036773a477493ae51918ca4e2e090dbfee658f0c8e5d59(
    *,
    key: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1fa0e640e0520cee49b72e68349d42fb4c8de7f5dfd483d14a801cd8f37c351(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45c2ad0ab59b37bcfd3ee3c640a3b4b99b22d3865da477e614701463912e0034(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2d5efebab1baa039e86566b5216f4221b6114541ca60896b977e4df31833d83(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e5c35a8a63eca3c029d0011a5763addfe9d35982190f621fa3d4140869172dd(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f3623623b00ac195c2ec166a3a17e6fd1b71c3a23867ab11d06a5e4b918e5a4(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bb50028bdf3677b9b412918d81432c8c03d19758ce8ae4109d96ee1b66e5911(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValues]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b25274174a3689e5169fb637b2f37314b3d8d86ccf0dcac0c4d9e24eb3f4e5b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c533683d30dba2ddc94300fbe5ba91a4584e8f82da5fc280baf09e1e31f60f9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a4dbafb887b33becf826aff036f9332567780ee9e14c48666dcabeab0d6afee(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb5f78561a808de06673a27d1d1022d2adac860b76f704dc68ecdfd9dbb4a32c(
    value: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValues, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0831a515a36533fff49100fe5e3c578bc4142f88dc4e0f0a41934f33ef44579(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d01ad69551529706a89a2832b5d85ae67d8fb6cc5e58a28bbf725d3a02b7d83e(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingExcludesAnd, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fd55fd082a51e3699b84e4bd14e5e4f5220f7c1f47c23ba3e8cb75370cc5ae9(
    value: typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingExcludes],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06842369ca619917cae9e02d036d96282a7251875ac65779f6953036b0867436(
    *,
    and_: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingIncludesAnd, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a04aacd2936816f655cb2b5915a6b81ff7d0aae62e5a14ef943e531adb931f0(
    *,
    simple_scope_term: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTerm, typing.Dict[builtins.str, typing.Any]]] = None,
    tag_scope_term: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTerm, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__631da54bd682a59944f85a52a6afd26afae5c9b5b9360d42e4d77f51f0b01841(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b484790a14b8b7b073cc3a849b29283722fbdb28872706e1d9603b774b10d72b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28f28ad30ccc7eb11068c4e278f39da89b1931958ea8321bfbc399135e8c0977(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8339da166dec7bffb66baf48b57cba6aaee2e4878f788b33252005498899fbda(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffc88483b1f7ca07c012be3287e942682696b08c53042db362f251968e5ad502(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24962052a9f70bbb56ebdfa51b330a0da87b8c483746cc4ee774fcadc962bd0d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionScopingIncludesAnd]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14d63279d2ef8ac87dd17054638c8a0738c486e57fbf1514b11554fc9c84e9b2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06f359f4b52d012214913b567217182e175210b128971490afd426f02b2e8fb0(
    value: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingIncludesAnd, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73636fc09fdc635d9559951c7757e0675606d54965fe0952ebe99d8ab5b256e4(
    *,
    comparator: typing.Optional[builtins.str] = None,
    key: typing.Optional[builtins.str] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c20f977b74fcaf49623c024d5ef2e791ca3da997d201bd7f61f85e271bc4bfb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__198737af9a6efc6aa05c604513ad660a6ec3f6201976fd9b0e7631afb31d64ab(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__093ceb7a75df38a66bc90a19a2106be22c47654d5a7e32919580bfb4dcb844fb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c49a49a4b6cce01301acd1bb9c69b0ac9b01f4ad339312bd5e066053438f974(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c08f786bacc0a81530d00e84505c0234206e8f60600c90189210874252888171(
    value: typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTerm],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26614fee4ef5ffe2dc84206a86683009a4e9850cea901757388efe52c76a30e3(
    *,
    comparator: typing.Optional[builtins.str] = None,
    key: typing.Optional[builtins.str] = None,
    tag_values: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValues, typing.Dict[builtins.str, typing.Any]]]]] = None,
    target: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80ca8c015b88b7b47b484e63155470a2b7b750ef336838a45d5066997db304fa(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e7b4be4aaefdc697fd38ab987d8f179e517ba4a7b5b2f0dd8cf348163f1b471(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValues, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c08cd9029085f142d0134d0ced45dc86afd1ae90cc5eaeda3f1ae06d0854cf5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf6329b5f6159f227492bd6a0a1fa6f14cb5e656611722edc043a96dab9caf1d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcad91a4f2fccc1d1de58be6add8d3c6339f6b70aa82e65cfb21611b80d9f37e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69e7d7c54154fdac233032aad08de3174efc96f8405d360371a17250c93b1aa1(
    value: typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTerm],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be89ae5bfa844ad021c2eb24830b63cba0e86ed8144f4c8d3a2789800a3b4ca1(
    *,
    key: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d309cefce9a6e40bb0c66ca3e83c260358d7cdf10b7f4eef96e09a56f70f2d4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26051d24aec3481fad573c91bfaf5d95709822a85bbd26a55fcf0a43b9acb751(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__888486e6a983f3e0192e03c5e75fe03f75680e7e4d2ef536cd61bfcac3d5cc9a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b14265c7371d31a50d5bc16985f12193d3067370b524736e235706cee5374fb(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75967fa4b24981c42d641bac3ec094614977cf5d656bee1ac96fcb371d50b152(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6fba78e9da0ca084788a5ae2c99de296b00e8a87256908dfe15baaaba7c486e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValues]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27dfb408acabb5e01cc2078e99564cb2ea90ea939d76a367a97b33a004a39a40(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0408ed3e94ce74d58b7511e7d8ab0e0ae5624a7d97e95e1d598cf53aa1b0f441(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccb592adb19f39b774a521413f155c8ff5df910e427803e4cb1c4e1a026bb257(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd2c82fbbe7c99e645a4f64ecebc74f1c730c834da6bb7c72a6f7f9633e01866(
    value: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValues, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__994ffc89e4d05b4dfe6f1e7d1f837ac973b53e3dae4c85cb9f9e1f68d33a5cc5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__569639261bf3aac3d8669941b6c33bbe65536821728ddb61dd8ef02637685409(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingIncludesAnd, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3380e2c6fd9dd18dfeeca2343a5ad8c42ad8c0cd20abaee08f1b53f07d3ac245(
    value: typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingIncludes],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14daa3eb05efadb9cf1f37f1c2b04e5a09c8e40adb95987a22d6b88837e65b04(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5deb29cb553e2e0e7cec21464ac22d4b7bc0a20f512be372ce02f07793543377(
    value: typing.Optional[Macie2ClassificationJobS3JobDefinitionScoping],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae5b87cde2ef005ab0ca67021c81f5589eea53fd4bd9df06a19d9b80c669148d(
    *,
    daily_schedule: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    monthly_schedule: typing.Optional[jsii.Number] = None,
    weekly_schedule: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfb105334eb32b4cc713895882e8e76b006496ee9c472fc2964cedc03a8903fe(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af7df7b4c8188973a9421e72e7185ce547a3e82afdf3573dfbd3dcc5c8c2c385(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7df020595cad9fb059f362af7a9212fc4654faa9b2ec13d25b51990fe0ee37b0(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d6ae1cb8e24af7c3d1fdf8a352c49bedd1670f4c42b34f0a1ae38361d57d408(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca3ffd1fac104e3788d5e5d0baf18695d09d135dd4be9975929aca39c8323d4b(
    value: typing.Optional[Macie2ClassificationJobScheduleFrequency],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d81ab2ea6fb1a496dcfea7928f0ee4372af664828e7e0960fdd3ca4bef5b3c2e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24f7c68772a55ba6f085b7549105826a3afe60bc6149c456c7b78f43a7502be1(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c6a8814a4b31c3e7335437a315b2c84e60769d0297e217da54f6df2e7103091(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6521e198f09902194bd40eaa3c850c2789b1b2269aaf53bd8e96736439920c1(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c000a9bfe7f0f9fad94e236a8a690ee9859d142194b851320065e82a233e0e54(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e55d2cf82623480f25e8cb353efc24f9006492cdd977e0d3bd497627c958a17b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d5f781393d75439ae251923df6c0b272a1078cfa91af731ca9d418a90cdb0f9(
    value: typing.Optional[Macie2ClassificationJobUserPausedDetails],
) -> None:
    """Type checking stubs"""
    pass
