'''
# `aws_s3_bucket_inventory`

Refer to the Terraform Registory for docs: [`aws_s3_bucket_inventory`](https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory).
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


class S3BucketInventory(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketInventory.S3BucketInventory",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory aws_s3_bucket_inventory}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        bucket: builtins.str,
        destination: typing.Union["S3BucketInventoryDestination", typing.Dict[builtins.str, typing.Any]],
        included_object_versions: builtins.str,
        name: builtins.str,
        schedule: typing.Union["S3BucketInventorySchedule", typing.Dict[builtins.str, typing.Any]],
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        filter: typing.Optional[typing.Union["S3BucketInventoryFilter", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        optional_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory aws_s3_bucket_inventory} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#bucket S3BucketInventory#bucket}.
        :param destination: destination block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#destination S3BucketInventory#destination}
        :param included_object_versions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#included_object_versions S3BucketInventory#included_object_versions}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#name S3BucketInventory#name}.
        :param schedule: schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#schedule S3BucketInventory#schedule}
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#enabled S3BucketInventory#enabled}.
        :param filter: filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#filter S3BucketInventory#filter}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#id S3BucketInventory#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param optional_fields: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#optional_fields S3BucketInventory#optional_fields}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57e08c33acb4f12a2b7fe3e71caa2a0af2f88952113234dee21b8216afb97213)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = S3BucketInventoryConfig(
            bucket=bucket,
            destination=destination,
            included_object_versions=included_object_versions,
            name=name,
            schedule=schedule,
            enabled=enabled,
            filter=filter,
            id=id,
            optional_fields=optional_fields,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putDestination")
    def put_destination(
        self,
        *,
        bucket: typing.Union["S3BucketInventoryDestinationBucket", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param bucket: bucket block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#bucket S3BucketInventory#bucket}
        '''
        value = S3BucketInventoryDestination(bucket=bucket)

        return typing.cast(None, jsii.invoke(self, "putDestination", [value]))

    @jsii.member(jsii_name="putFilter")
    def put_filter(self, *, prefix: typing.Optional[builtins.str] = None) -> None:
        '''
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#prefix S3BucketInventory#prefix}.
        '''
        value = S3BucketInventoryFilter(prefix=prefix)

        return typing.cast(None, jsii.invoke(self, "putFilter", [value]))

    @jsii.member(jsii_name="putSchedule")
    def put_schedule(self, *, frequency: builtins.str) -> None:
        '''
        :param frequency: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#frequency S3BucketInventory#frequency}.
        '''
        value = S3BucketInventorySchedule(frequency=frequency)

        return typing.cast(None, jsii.invoke(self, "putSchedule", [value]))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetFilter")
    def reset_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilter", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetOptionalFields")
    def reset_optional_fields(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOptionalFields", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(self) -> "S3BucketInventoryDestinationOutputReference":
        return typing.cast("S3BucketInventoryDestinationOutputReference", jsii.get(self, "destination"))

    @builtins.property
    @jsii.member(jsii_name="filter")
    def filter(self) -> "S3BucketInventoryFilterOutputReference":
        return typing.cast("S3BucketInventoryFilterOutputReference", jsii.get(self, "filter"))

    @builtins.property
    @jsii.member(jsii_name="schedule")
    def schedule(self) -> "S3BucketInventoryScheduleOutputReference":
        return typing.cast("S3BucketInventoryScheduleOutputReference", jsii.get(self, "schedule"))

    @builtins.property
    @jsii.member(jsii_name="bucketInput")
    def bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationInput")
    def destination_input(self) -> typing.Optional["S3BucketInventoryDestination"]:
        return typing.cast(typing.Optional["S3BucketInventoryDestination"], jsii.get(self, "destinationInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="filterInput")
    def filter_input(self) -> typing.Optional["S3BucketInventoryFilter"]:
        return typing.cast(typing.Optional["S3BucketInventoryFilter"], jsii.get(self, "filterInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="includedObjectVersionsInput")
    def included_object_versions_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "includedObjectVersionsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="optionalFieldsInput")
    def optional_fields_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "optionalFieldsInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduleInput")
    def schedule_input(self) -> typing.Optional["S3BucketInventorySchedule"]:
        return typing.cast(typing.Optional["S3BucketInventorySchedule"], jsii.get(self, "scheduleInput"))

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c459acb6906f6fdbb56bde44bd6ad96deb617fc95b409db11e8af4384f25a965)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucket", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__8c12e23f07f0d365475797cc548361bca23858d11461efdcf11dceba608c65a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba4121ec59b13440edae687339f96e7268d1def747c2512250e897c16287dc4a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="includedObjectVersions")
    def included_object_versions(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "includedObjectVersions"))

    @included_object_versions.setter
    def included_object_versions(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__394cf761ccf0bb416d943993ac6e35cb4eb0c032885efb0a4f71ca08d911ecbe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includedObjectVersions", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60709fe2682c9a5afde2634d94837ab05326724a8c0cc48b65e00cb4a4683cc4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="optionalFields")
    def optional_fields(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "optionalFields"))

    @optional_fields.setter
    def optional_fields(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da9ea8ea9c722dac017888467ab00ba65a5936f85c437a15feb8375fefd7e0e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "optionalFields", value)


@jsii.data_type(
    jsii_type="aws.s3BucketInventory.S3BucketInventoryConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "bucket": "bucket",
        "destination": "destination",
        "included_object_versions": "includedObjectVersions",
        "name": "name",
        "schedule": "schedule",
        "enabled": "enabled",
        "filter": "filter",
        "id": "id",
        "optional_fields": "optionalFields",
    },
)
class S3BucketInventoryConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        bucket: builtins.str,
        destination: typing.Union["S3BucketInventoryDestination", typing.Dict[builtins.str, typing.Any]],
        included_object_versions: builtins.str,
        name: builtins.str,
        schedule: typing.Union["S3BucketInventorySchedule", typing.Dict[builtins.str, typing.Any]],
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        filter: typing.Optional[typing.Union["S3BucketInventoryFilter", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        optional_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#bucket S3BucketInventory#bucket}.
        :param destination: destination block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#destination S3BucketInventory#destination}
        :param included_object_versions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#included_object_versions S3BucketInventory#included_object_versions}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#name S3BucketInventory#name}.
        :param schedule: schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#schedule S3BucketInventory#schedule}
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#enabled S3BucketInventory#enabled}.
        :param filter: filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#filter S3BucketInventory#filter}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#id S3BucketInventory#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param optional_fields: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#optional_fields S3BucketInventory#optional_fields}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(destination, dict):
            destination = S3BucketInventoryDestination(**destination)
        if isinstance(schedule, dict):
            schedule = S3BucketInventorySchedule(**schedule)
        if isinstance(filter, dict):
            filter = S3BucketInventoryFilter(**filter)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e88a0f93306d6024e48cf2e3bfb6a9c22a45556a78daf5ff321bab4d246e1c75)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
            check_type(argname="argument included_object_versions", value=included_object_versions, expected_type=type_hints["included_object_versions"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument optional_fields", value=optional_fields, expected_type=type_hints["optional_fields"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket": bucket,
            "destination": destination,
            "included_object_versions": included_object_versions,
            "name": name,
            "schedule": schedule,
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
        if enabled is not None:
            self._values["enabled"] = enabled
        if filter is not None:
            self._values["filter"] = filter
        if id is not None:
            self._values["id"] = id
        if optional_fields is not None:
            self._values["optional_fields"] = optional_fields

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
    def bucket(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#bucket S3BucketInventory#bucket}.'''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def destination(self) -> "S3BucketInventoryDestination":
        '''destination block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#destination S3BucketInventory#destination}
        '''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast("S3BucketInventoryDestination", result)

    @builtins.property
    def included_object_versions(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#included_object_versions S3BucketInventory#included_object_versions}.'''
        result = self._values.get("included_object_versions")
        assert result is not None, "Required property 'included_object_versions' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#name S3BucketInventory#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schedule(self) -> "S3BucketInventorySchedule":
        '''schedule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#schedule S3BucketInventory#schedule}
        '''
        result = self._values.get("schedule")
        assert result is not None, "Required property 'schedule' is missing"
        return typing.cast("S3BucketInventorySchedule", result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#enabled S3BucketInventory#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def filter(self) -> typing.Optional["S3BucketInventoryFilter"]:
        '''filter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#filter S3BucketInventory#filter}
        '''
        result = self._values.get("filter")
        return typing.cast(typing.Optional["S3BucketInventoryFilter"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#id S3BucketInventory#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def optional_fields(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#optional_fields S3BucketInventory#optional_fields}.'''
        result = self._values.get("optional_fields")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketInventoryConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.s3BucketInventory.S3BucketInventoryDestination",
    jsii_struct_bases=[],
    name_mapping={"bucket": "bucket"},
)
class S3BucketInventoryDestination:
    def __init__(
        self,
        *,
        bucket: typing.Union["S3BucketInventoryDestinationBucket", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param bucket: bucket block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#bucket S3BucketInventory#bucket}
        '''
        if isinstance(bucket, dict):
            bucket = S3BucketInventoryDestinationBucket(**bucket)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b64b4d4597fe7fcb13a9c4bb5cf8f27abc9427774bbc4caad3e949de0e6c4298)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket": bucket,
        }

    @builtins.property
    def bucket(self) -> "S3BucketInventoryDestinationBucket":
        '''bucket block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#bucket S3BucketInventory#bucket}
        '''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast("S3BucketInventoryDestinationBucket", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketInventoryDestination(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.s3BucketInventory.S3BucketInventoryDestinationBucket",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_arn": "bucketArn",
        "format": "format",
        "account_id": "accountId",
        "encryption": "encryption",
        "prefix": "prefix",
    },
)
class S3BucketInventoryDestinationBucket:
    def __init__(
        self,
        *,
        bucket_arn: builtins.str,
        format: builtins.str,
        account_id: typing.Optional[builtins.str] = None,
        encryption: typing.Optional[typing.Union["S3BucketInventoryDestinationBucketEncryption", typing.Dict[builtins.str, typing.Any]]] = None,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#bucket_arn S3BucketInventory#bucket_arn}.
        :param format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#format S3BucketInventory#format}.
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#account_id S3BucketInventory#account_id}.
        :param encryption: encryption block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#encryption S3BucketInventory#encryption}
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#prefix S3BucketInventory#prefix}.
        '''
        if isinstance(encryption, dict):
            encryption = S3BucketInventoryDestinationBucketEncryption(**encryption)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68f93d5dab01599168d891021b9a3c2587f466ae6b490676164e0c1856a51a09)
            check_type(argname="argument bucket_arn", value=bucket_arn, expected_type=type_hints["bucket_arn"])
            check_type(argname="argument format", value=format, expected_type=type_hints["format"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument encryption", value=encryption, expected_type=type_hints["encryption"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket_arn": bucket_arn,
            "format": format,
        }
        if account_id is not None:
            self._values["account_id"] = account_id
        if encryption is not None:
            self._values["encryption"] = encryption
        if prefix is not None:
            self._values["prefix"] = prefix

    @builtins.property
    def bucket_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#bucket_arn S3BucketInventory#bucket_arn}.'''
        result = self._values.get("bucket_arn")
        assert result is not None, "Required property 'bucket_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def format(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#format S3BucketInventory#format}.'''
        result = self._values.get("format")
        assert result is not None, "Required property 'format' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#account_id S3BucketInventory#account_id}.'''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption(
        self,
    ) -> typing.Optional["S3BucketInventoryDestinationBucketEncryption"]:
        '''encryption block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#encryption S3BucketInventory#encryption}
        '''
        result = self._values.get("encryption")
        return typing.cast(typing.Optional["S3BucketInventoryDestinationBucketEncryption"], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#prefix S3BucketInventory#prefix}.'''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketInventoryDestinationBucket(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.s3BucketInventory.S3BucketInventoryDestinationBucketEncryption",
    jsii_struct_bases=[],
    name_mapping={"sse_kms": "sseKms", "sse_s3": "sseS3"},
)
class S3BucketInventoryDestinationBucketEncryption:
    def __init__(
        self,
        *,
        sse_kms: typing.Optional[typing.Union["S3BucketInventoryDestinationBucketEncryptionSseKms", typing.Dict[builtins.str, typing.Any]]] = None,
        sse_s3: typing.Optional[typing.Union["S3BucketInventoryDestinationBucketEncryptionSseS3", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param sse_kms: sse_kms block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#sse_kms S3BucketInventory#sse_kms}
        :param sse_s3: sse_s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#sse_s3 S3BucketInventory#sse_s3}
        '''
        if isinstance(sse_kms, dict):
            sse_kms = S3BucketInventoryDestinationBucketEncryptionSseKms(**sse_kms)
        if isinstance(sse_s3, dict):
            sse_s3 = S3BucketInventoryDestinationBucketEncryptionSseS3(**sse_s3)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33a1d821fc02cee9fed7468f3f6b41fe7f477cb3a69e6295035403fd1f374217)
            check_type(argname="argument sse_kms", value=sse_kms, expected_type=type_hints["sse_kms"])
            check_type(argname="argument sse_s3", value=sse_s3, expected_type=type_hints["sse_s3"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if sse_kms is not None:
            self._values["sse_kms"] = sse_kms
        if sse_s3 is not None:
            self._values["sse_s3"] = sse_s3

    @builtins.property
    def sse_kms(
        self,
    ) -> typing.Optional["S3BucketInventoryDestinationBucketEncryptionSseKms"]:
        '''sse_kms block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#sse_kms S3BucketInventory#sse_kms}
        '''
        result = self._values.get("sse_kms")
        return typing.cast(typing.Optional["S3BucketInventoryDestinationBucketEncryptionSseKms"], result)

    @builtins.property
    def sse_s3(
        self,
    ) -> typing.Optional["S3BucketInventoryDestinationBucketEncryptionSseS3"]:
        '''sse_s3 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#sse_s3 S3BucketInventory#sse_s3}
        '''
        result = self._values.get("sse_s3")
        return typing.cast(typing.Optional["S3BucketInventoryDestinationBucketEncryptionSseS3"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketInventoryDestinationBucketEncryption(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketInventoryDestinationBucketEncryptionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketInventory.S3BucketInventoryDestinationBucketEncryptionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b92913f97b28a9576925e6c88dab4d5e6d0c965327175b6391f5b4d55c0d375e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSseKms")
    def put_sse_kms(self, *, key_id: builtins.str) -> None:
        '''
        :param key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#key_id S3BucketInventory#key_id}.
        '''
        value = S3BucketInventoryDestinationBucketEncryptionSseKms(key_id=key_id)

        return typing.cast(None, jsii.invoke(self, "putSseKms", [value]))

    @jsii.member(jsii_name="putSseS3")
    def put_sse_s3(self) -> None:
        value = S3BucketInventoryDestinationBucketEncryptionSseS3()

        return typing.cast(None, jsii.invoke(self, "putSseS3", [value]))

    @jsii.member(jsii_name="resetSseKms")
    def reset_sse_kms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSseKms", []))

    @jsii.member(jsii_name="resetSseS3")
    def reset_sse_s3(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSseS3", []))

    @builtins.property
    @jsii.member(jsii_name="sseKms")
    def sse_kms(
        self,
    ) -> "S3BucketInventoryDestinationBucketEncryptionSseKmsOutputReference":
        return typing.cast("S3BucketInventoryDestinationBucketEncryptionSseKmsOutputReference", jsii.get(self, "sseKms"))

    @builtins.property
    @jsii.member(jsii_name="sseS3")
    def sse_s3(
        self,
    ) -> "S3BucketInventoryDestinationBucketEncryptionSseS3OutputReference":
        return typing.cast("S3BucketInventoryDestinationBucketEncryptionSseS3OutputReference", jsii.get(self, "sseS3"))

    @builtins.property
    @jsii.member(jsii_name="sseKmsInput")
    def sse_kms_input(
        self,
    ) -> typing.Optional["S3BucketInventoryDestinationBucketEncryptionSseKms"]:
        return typing.cast(typing.Optional["S3BucketInventoryDestinationBucketEncryptionSseKms"], jsii.get(self, "sseKmsInput"))

    @builtins.property
    @jsii.member(jsii_name="sseS3Input")
    def sse_s3_input(
        self,
    ) -> typing.Optional["S3BucketInventoryDestinationBucketEncryptionSseS3"]:
        return typing.cast(typing.Optional["S3BucketInventoryDestinationBucketEncryptionSseS3"], jsii.get(self, "sseS3Input"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketInventoryDestinationBucketEncryption]:
        return typing.cast(typing.Optional[S3BucketInventoryDestinationBucketEncryption], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketInventoryDestinationBucketEncryption],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56cafc32ccb20a39fff1a77be3793a968773902d75b22548ee655d6a9e89fc8a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3BucketInventory.S3BucketInventoryDestinationBucketEncryptionSseKms",
    jsii_struct_bases=[],
    name_mapping={"key_id": "keyId"},
)
class S3BucketInventoryDestinationBucketEncryptionSseKms:
    def __init__(self, *, key_id: builtins.str) -> None:
        '''
        :param key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#key_id S3BucketInventory#key_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1812249aff525eea6cb8d1f530ceb6aeaf58d1436a5f908a49594027518bf7a4)
            check_type(argname="argument key_id", value=key_id, expected_type=type_hints["key_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key_id": key_id,
        }

    @builtins.property
    def key_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#key_id S3BucketInventory#key_id}.'''
        result = self._values.get("key_id")
        assert result is not None, "Required property 'key_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketInventoryDestinationBucketEncryptionSseKms(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketInventoryDestinationBucketEncryptionSseKmsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketInventory.S3BucketInventoryDestinationBucketEncryptionSseKmsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9486f20e2cbe388e720c36aa8c44f667247f2af16e0c5593bb8efdbf767a9ee1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="keyIdInput")
    def key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="keyId")
    def key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyId"))

    @key_id.setter
    def key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d78b10cce9c7e9af3c01a7e7b05560b54866d92e66fddb75e182c9511fe550af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketInventoryDestinationBucketEncryptionSseKms]:
        return typing.cast(typing.Optional[S3BucketInventoryDestinationBucketEncryptionSseKms], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketInventoryDestinationBucketEncryptionSseKms],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cffeed97010f1495b1f5435cf01ab2b0649a5bd5298c1a17e1b98ee19120d05e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3BucketInventory.S3BucketInventoryDestinationBucketEncryptionSseS3",
    jsii_struct_bases=[],
    name_mapping={},
)
class S3BucketInventoryDestinationBucketEncryptionSseS3:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketInventoryDestinationBucketEncryptionSseS3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketInventoryDestinationBucketEncryptionSseS3OutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketInventory.S3BucketInventoryDestinationBucketEncryptionSseS3OutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__47c1e997ae1d2d1ce65c1fd91945866196ea7d2793e43596fb0c8366c8bfd2b4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketInventoryDestinationBucketEncryptionSseS3]:
        return typing.cast(typing.Optional[S3BucketInventoryDestinationBucketEncryptionSseS3], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketInventoryDestinationBucketEncryptionSseS3],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04c4b7090c0f76dfa9a62c16d61da03da87e61dc9479f348fcd7568347af89b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3BucketInventoryDestinationBucketOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketInventory.S3BucketInventoryDestinationBucketOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__af2fa66a73f92aa7aa3dbb6daba47f7628e572691001bf81091a51cab776ff5d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putEncryption")
    def put_encryption(
        self,
        *,
        sse_kms: typing.Optional[typing.Union[S3BucketInventoryDestinationBucketEncryptionSseKms, typing.Dict[builtins.str, typing.Any]]] = None,
        sse_s3: typing.Optional[typing.Union[S3BucketInventoryDestinationBucketEncryptionSseS3, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param sse_kms: sse_kms block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#sse_kms S3BucketInventory#sse_kms}
        :param sse_s3: sse_s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#sse_s3 S3BucketInventory#sse_s3}
        '''
        value = S3BucketInventoryDestinationBucketEncryption(
            sse_kms=sse_kms, sse_s3=sse_s3
        )

        return typing.cast(None, jsii.invoke(self, "putEncryption", [value]))

    @jsii.member(jsii_name="resetAccountId")
    def reset_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountId", []))

    @jsii.member(jsii_name="resetEncryption")
    def reset_encryption(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryption", []))

    @jsii.member(jsii_name="resetPrefix")
    def reset_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefix", []))

    @builtins.property
    @jsii.member(jsii_name="encryption")
    def encryption(self) -> S3BucketInventoryDestinationBucketEncryptionOutputReference:
        return typing.cast(S3BucketInventoryDestinationBucketEncryptionOutputReference, jsii.get(self, "encryption"))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketArnInput")
    def bucket_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketArnInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionInput")
    def encryption_input(
        self,
    ) -> typing.Optional[S3BucketInventoryDestinationBucketEncryption]:
        return typing.cast(typing.Optional[S3BucketInventoryDestinationBucketEncryption], jsii.get(self, "encryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="formatInput")
    def format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "formatInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eccae8d057fb3394cd046c52d965e03a36f761a575defd42cb156723dbfcb227)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="bucketArn")
    def bucket_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketArn"))

    @bucket_arn.setter
    def bucket_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4816072d08847b5536e89c245d98bf1b3c8865cf57a3d10ee4964f93ac0a3371)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketArn", value)

    @builtins.property
    @jsii.member(jsii_name="format")
    def format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "format"))

    @format.setter
    def format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76292a19ba3181869b8b4e9c8b110c989fead47dcecdbd4332596dd7859acf48)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "format", value)

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d34ebdd1e52c44dfd2cc9504e777d1b260ef087674213707565ba8adc698efe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[S3BucketInventoryDestinationBucket]:
        return typing.cast(typing.Optional[S3BucketInventoryDestinationBucket], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketInventoryDestinationBucket],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3045244bdab6b6bd706103940bfa0272cb9e69a6093cece53280a7753a77744)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3BucketInventoryDestinationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketInventory.S3BucketInventoryDestinationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__359d4d69ba6c6f3ec9232ca993fc9b34c31b63828551f47a2115057177c13e50)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putBucket")
    def put_bucket(
        self,
        *,
        bucket_arn: builtins.str,
        format: builtins.str,
        account_id: typing.Optional[builtins.str] = None,
        encryption: typing.Optional[typing.Union[S3BucketInventoryDestinationBucketEncryption, typing.Dict[builtins.str, typing.Any]]] = None,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#bucket_arn S3BucketInventory#bucket_arn}.
        :param format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#format S3BucketInventory#format}.
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#account_id S3BucketInventory#account_id}.
        :param encryption: encryption block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#encryption S3BucketInventory#encryption}
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#prefix S3BucketInventory#prefix}.
        '''
        value = S3BucketInventoryDestinationBucket(
            bucket_arn=bucket_arn,
            format=format,
            account_id=account_id,
            encryption=encryption,
            prefix=prefix,
        )

        return typing.cast(None, jsii.invoke(self, "putBucket", [value]))

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> S3BucketInventoryDestinationBucketOutputReference:
        return typing.cast(S3BucketInventoryDestinationBucketOutputReference, jsii.get(self, "bucket"))

    @builtins.property
    @jsii.member(jsii_name="bucketInput")
    def bucket_input(self) -> typing.Optional[S3BucketInventoryDestinationBucket]:
        return typing.cast(typing.Optional[S3BucketInventoryDestinationBucket], jsii.get(self, "bucketInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[S3BucketInventoryDestination]:
        return typing.cast(typing.Optional[S3BucketInventoryDestination], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketInventoryDestination],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f6338f17514a48c59f3e1ca583bf40ce4b8c7d35bdcfdea538376d12e4b2176)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3BucketInventory.S3BucketInventoryFilter",
    jsii_struct_bases=[],
    name_mapping={"prefix": "prefix"},
)
class S3BucketInventoryFilter:
    def __init__(self, *, prefix: typing.Optional[builtins.str] = None) -> None:
        '''
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#prefix S3BucketInventory#prefix}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7bfa16ab2d970753ca41e43e4fe52ee5092215be98917e30df585d13475f82b2)
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if prefix is not None:
            self._values["prefix"] = prefix

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#prefix S3BucketInventory#prefix}.'''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketInventoryFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketInventoryFilterOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketInventory.S3BucketInventoryFilterOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__99ec393556436796d34bf45030e7d6b168eef1adf9956b68a76dad8a380fd25b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPrefix")
    def reset_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefix", []))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bd8126113793d500eab8f6e3a41288127bddde4104f61ef3e08de6dcbd7f353)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[S3BucketInventoryFilter]:
        return typing.cast(typing.Optional[S3BucketInventoryFilter], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[S3BucketInventoryFilter]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19a98c42a9ec9c7b456d0d3a846a5597864d216d1febcb70d876189f22a7422b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3BucketInventory.S3BucketInventorySchedule",
    jsii_struct_bases=[],
    name_mapping={"frequency": "frequency"},
)
class S3BucketInventorySchedule:
    def __init__(self, *, frequency: builtins.str) -> None:
        '''
        :param frequency: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#frequency S3BucketInventory#frequency}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cec104387208fb1dcd2fe8ec62abf29d40947918804aeb70095471ea37f0c112)
            check_type(argname="argument frequency", value=frequency, expected_type=type_hints["frequency"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "frequency": frequency,
        }

    @builtins.property
    def frequency(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#frequency S3BucketInventory#frequency}.'''
        result = self._values.get("frequency")
        assert result is not None, "Required property 'frequency' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketInventorySchedule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketInventoryScheduleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketInventory.S3BucketInventoryScheduleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6008d001308b2ee52d5bbdc08842af7217f58b9940f747a07da9b364f4f8057f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="frequencyInput")
    def frequency_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "frequencyInput"))

    @builtins.property
    @jsii.member(jsii_name="frequency")
    def frequency(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "frequency"))

    @frequency.setter
    def frequency(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be58d92c4af7af615aa1e0a98f2211e876e4e8741ee55a0d15dd61e70bb5c46e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frequency", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[S3BucketInventorySchedule]:
        return typing.cast(typing.Optional[S3BucketInventorySchedule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[S3BucketInventorySchedule]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae804c2449f348faa43d5f52ff290c0201b1f815c9758913031f8ec1a7e68a23)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "S3BucketInventory",
    "S3BucketInventoryConfig",
    "S3BucketInventoryDestination",
    "S3BucketInventoryDestinationBucket",
    "S3BucketInventoryDestinationBucketEncryption",
    "S3BucketInventoryDestinationBucketEncryptionOutputReference",
    "S3BucketInventoryDestinationBucketEncryptionSseKms",
    "S3BucketInventoryDestinationBucketEncryptionSseKmsOutputReference",
    "S3BucketInventoryDestinationBucketEncryptionSseS3",
    "S3BucketInventoryDestinationBucketEncryptionSseS3OutputReference",
    "S3BucketInventoryDestinationBucketOutputReference",
    "S3BucketInventoryDestinationOutputReference",
    "S3BucketInventoryFilter",
    "S3BucketInventoryFilterOutputReference",
    "S3BucketInventorySchedule",
    "S3BucketInventoryScheduleOutputReference",
]

publication.publish()

def _typecheckingstub__57e08c33acb4f12a2b7fe3e71caa2a0af2f88952113234dee21b8216afb97213(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    bucket: builtins.str,
    destination: typing.Union[S3BucketInventoryDestination, typing.Dict[builtins.str, typing.Any]],
    included_object_versions: builtins.str,
    name: builtins.str,
    schedule: typing.Union[S3BucketInventorySchedule, typing.Dict[builtins.str, typing.Any]],
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    filter: typing.Optional[typing.Union[S3BucketInventoryFilter, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    optional_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
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

def _typecheckingstub__c459acb6906f6fdbb56bde44bd6ad96deb617fc95b409db11e8af4384f25a965(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c12e23f07f0d365475797cc548361bca23858d11461efdcf11dceba608c65a1(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba4121ec59b13440edae687339f96e7268d1def747c2512250e897c16287dc4a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__394cf761ccf0bb416d943993ac6e35cb4eb0c032885efb0a4f71ca08d911ecbe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60709fe2682c9a5afde2634d94837ab05326724a8c0cc48b65e00cb4a4683cc4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da9ea8ea9c722dac017888467ab00ba65a5936f85c437a15feb8375fefd7e0e6(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e88a0f93306d6024e48cf2e3bfb6a9c22a45556a78daf5ff321bab4d246e1c75(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    bucket: builtins.str,
    destination: typing.Union[S3BucketInventoryDestination, typing.Dict[builtins.str, typing.Any]],
    included_object_versions: builtins.str,
    name: builtins.str,
    schedule: typing.Union[S3BucketInventorySchedule, typing.Dict[builtins.str, typing.Any]],
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    filter: typing.Optional[typing.Union[S3BucketInventoryFilter, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    optional_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b64b4d4597fe7fcb13a9c4bb5cf8f27abc9427774bbc4caad3e949de0e6c4298(
    *,
    bucket: typing.Union[S3BucketInventoryDestinationBucket, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68f93d5dab01599168d891021b9a3c2587f466ae6b490676164e0c1856a51a09(
    *,
    bucket_arn: builtins.str,
    format: builtins.str,
    account_id: typing.Optional[builtins.str] = None,
    encryption: typing.Optional[typing.Union[S3BucketInventoryDestinationBucketEncryption, typing.Dict[builtins.str, typing.Any]]] = None,
    prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33a1d821fc02cee9fed7468f3f6b41fe7f477cb3a69e6295035403fd1f374217(
    *,
    sse_kms: typing.Optional[typing.Union[S3BucketInventoryDestinationBucketEncryptionSseKms, typing.Dict[builtins.str, typing.Any]]] = None,
    sse_s3: typing.Optional[typing.Union[S3BucketInventoryDestinationBucketEncryptionSseS3, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b92913f97b28a9576925e6c88dab4d5e6d0c965327175b6391f5b4d55c0d375e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56cafc32ccb20a39fff1a77be3793a968773902d75b22548ee655d6a9e89fc8a(
    value: typing.Optional[S3BucketInventoryDestinationBucketEncryption],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1812249aff525eea6cb8d1f530ceb6aeaf58d1436a5f908a49594027518bf7a4(
    *,
    key_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9486f20e2cbe388e720c36aa8c44f667247f2af16e0c5593bb8efdbf767a9ee1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d78b10cce9c7e9af3c01a7e7b05560b54866d92e66fddb75e182c9511fe550af(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cffeed97010f1495b1f5435cf01ab2b0649a5bd5298c1a17e1b98ee19120d05e(
    value: typing.Optional[S3BucketInventoryDestinationBucketEncryptionSseKms],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47c1e997ae1d2d1ce65c1fd91945866196ea7d2793e43596fb0c8366c8bfd2b4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04c4b7090c0f76dfa9a62c16d61da03da87e61dc9479f348fcd7568347af89b5(
    value: typing.Optional[S3BucketInventoryDestinationBucketEncryptionSseS3],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af2fa66a73f92aa7aa3dbb6daba47f7628e572691001bf81091a51cab776ff5d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eccae8d057fb3394cd046c52d965e03a36f761a575defd42cb156723dbfcb227(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4816072d08847b5536e89c245d98bf1b3c8865cf57a3d10ee4964f93ac0a3371(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76292a19ba3181869b8b4e9c8b110c989fead47dcecdbd4332596dd7859acf48(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d34ebdd1e52c44dfd2cc9504e777d1b260ef087674213707565ba8adc698efe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3045244bdab6b6bd706103940bfa0272cb9e69a6093cece53280a7753a77744(
    value: typing.Optional[S3BucketInventoryDestinationBucket],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__359d4d69ba6c6f3ec9232ca993fc9b34c31b63828551f47a2115057177c13e50(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f6338f17514a48c59f3e1ca583bf40ce4b8c7d35bdcfdea538376d12e4b2176(
    value: typing.Optional[S3BucketInventoryDestination],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7bfa16ab2d970753ca41e43e4fe52ee5092215be98917e30df585d13475f82b2(
    *,
    prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99ec393556436796d34bf45030e7d6b168eef1adf9956b68a76dad8a380fd25b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bd8126113793d500eab8f6e3a41288127bddde4104f61ef3e08de6dcbd7f353(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19a98c42a9ec9c7b456d0d3a846a5597864d216d1febcb70d876189f22a7422b(
    value: typing.Optional[S3BucketInventoryFilter],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cec104387208fb1dcd2fe8ec62abf29d40947918804aeb70095471ea37f0c112(
    *,
    frequency: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6008d001308b2ee52d5bbdc08842af7217f58b9940f747a07da9b364f4f8057f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be58d92c4af7af615aa1e0a98f2211e876e4e8741ee55a0d15dd61e70bb5c46e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae804c2449f348faa43d5f52ff290c0201b1f815c9758913031f8ec1a7e68a23(
    value: typing.Optional[S3BucketInventorySchedule],
) -> None:
    """Type checking stubs"""
    pass
