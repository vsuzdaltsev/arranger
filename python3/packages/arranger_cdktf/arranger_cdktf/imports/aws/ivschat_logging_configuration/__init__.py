'''
# `aws_ivschat_logging_configuration`

Refer to the Terraform Registory for docs: [`aws_ivschat_logging_configuration`](https://www.terraform.io/docs/providers/aws/r/ivschat_logging_configuration).
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


class IvschatLoggingConfiguration(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ivschatLoggingConfiguration.IvschatLoggingConfiguration",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/ivschat_logging_configuration aws_ivschat_logging_configuration}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        destination_configuration: typing.Optional[typing.Union["IvschatLoggingConfigurationDestinationConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["IvschatLoggingConfigurationTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/ivschat_logging_configuration aws_ivschat_logging_configuration} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param destination_configuration: destination_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivschat_logging_configuration#destination_configuration IvschatLoggingConfiguration#destination_configuration}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivschat_logging_configuration#id IvschatLoggingConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivschat_logging_configuration#name IvschatLoggingConfiguration#name}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivschat_logging_configuration#tags IvschatLoggingConfiguration#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivschat_logging_configuration#tags_all IvschatLoggingConfiguration#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivschat_logging_configuration#timeouts IvschatLoggingConfiguration#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa92f3e623999a95853ef218fccb136d2c26c822b4584ab341fd43bd262b23c3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = IvschatLoggingConfigurationConfig(
            destination_configuration=destination_configuration,
            id=id,
            name=name,
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

    @jsii.member(jsii_name="putDestinationConfiguration")
    def put_destination_configuration(
        self,
        *,
        cloudwatch_logs: typing.Optional[typing.Union["IvschatLoggingConfigurationDestinationConfigurationCloudwatchLogs", typing.Dict[builtins.str, typing.Any]]] = None,
        firehose: typing.Optional[typing.Union["IvschatLoggingConfigurationDestinationConfigurationFirehose", typing.Dict[builtins.str, typing.Any]]] = None,
        s3: typing.Optional[typing.Union["IvschatLoggingConfigurationDestinationConfigurationS3", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cloudwatch_logs: cloudwatch_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivschat_logging_configuration#cloudwatch_logs IvschatLoggingConfiguration#cloudwatch_logs}
        :param firehose: firehose block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivschat_logging_configuration#firehose IvschatLoggingConfiguration#firehose}
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivschat_logging_configuration#s3 IvschatLoggingConfiguration#s3}
        '''
        value = IvschatLoggingConfigurationDestinationConfiguration(
            cloudwatch_logs=cloudwatch_logs, firehose=firehose, s3=s3
        )

        return typing.cast(None, jsii.invoke(self, "putDestinationConfiguration", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivschat_logging_configuration#create IvschatLoggingConfiguration#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivschat_logging_configuration#delete IvschatLoggingConfiguration#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivschat_logging_configuration#update IvschatLoggingConfiguration#update}.
        '''
        value = IvschatLoggingConfigurationTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDestinationConfiguration")
    def reset_destination_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationConfiguration", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

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
    @jsii.member(jsii_name="destinationConfiguration")
    def destination_configuration(
        self,
    ) -> "IvschatLoggingConfigurationDestinationConfigurationOutputReference":
        return typing.cast("IvschatLoggingConfigurationDestinationConfigurationOutputReference", jsii.get(self, "destinationConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "IvschatLoggingConfigurationTimeoutsOutputReference":
        return typing.cast("IvschatLoggingConfigurationTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="destinationConfigurationInput")
    def destination_configuration_input(
        self,
    ) -> typing.Optional["IvschatLoggingConfigurationDestinationConfiguration"]:
        return typing.cast(typing.Optional["IvschatLoggingConfigurationDestinationConfiguration"], jsii.get(self, "destinationConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

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
    ) -> typing.Optional[typing.Union["IvschatLoggingConfigurationTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["IvschatLoggingConfigurationTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25c2e50f111b11428e9676410a69269cb3cd7eb59651f4f3651254ceb2178970)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1588c34eec3191ab377f1f45e1c25e2d81b287791e9c7772390c07b5eb9b7efc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b2bb8597bf5d513054c8f17f315f54194ae9c5b68dbff1d6350754497859ad5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7e19a20ca503b0b57fcbe5666861cac5db780dace70e558b68e5e4b5da5abe4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.ivschatLoggingConfiguration.IvschatLoggingConfigurationConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "destination_configuration": "destinationConfiguration",
        "id": "id",
        "name": "name",
        "tags": "tags",
        "tags_all": "tagsAll",
        "timeouts": "timeouts",
    },
)
class IvschatLoggingConfigurationConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        destination_configuration: typing.Optional[typing.Union["IvschatLoggingConfigurationDestinationConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["IvschatLoggingConfigurationTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param destination_configuration: destination_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivschat_logging_configuration#destination_configuration IvschatLoggingConfiguration#destination_configuration}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivschat_logging_configuration#id IvschatLoggingConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivschat_logging_configuration#name IvschatLoggingConfiguration#name}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivschat_logging_configuration#tags IvschatLoggingConfiguration#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivschat_logging_configuration#tags_all IvschatLoggingConfiguration#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivschat_logging_configuration#timeouts IvschatLoggingConfiguration#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(destination_configuration, dict):
            destination_configuration = IvschatLoggingConfigurationDestinationConfiguration(**destination_configuration)
        if isinstance(timeouts, dict):
            timeouts = IvschatLoggingConfigurationTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c19575c2f43ccd35c7dbbe55cf31fff97823c316e60bdcd60abd01ba89021ab)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument destination_configuration", value=destination_configuration, expected_type=type_hints["destination_configuration"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
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
        if destination_configuration is not None:
            self._values["destination_configuration"] = destination_configuration
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name
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
    def destination_configuration(
        self,
    ) -> typing.Optional["IvschatLoggingConfigurationDestinationConfiguration"]:
        '''destination_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivschat_logging_configuration#destination_configuration IvschatLoggingConfiguration#destination_configuration}
        '''
        result = self._values.get("destination_configuration")
        return typing.cast(typing.Optional["IvschatLoggingConfigurationDestinationConfiguration"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivschat_logging_configuration#id IvschatLoggingConfiguration#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivschat_logging_configuration#name IvschatLoggingConfiguration#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivschat_logging_configuration#tags IvschatLoggingConfiguration#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivschat_logging_configuration#tags_all IvschatLoggingConfiguration#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["IvschatLoggingConfigurationTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivschat_logging_configuration#timeouts IvschatLoggingConfiguration#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["IvschatLoggingConfigurationTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IvschatLoggingConfigurationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.ivschatLoggingConfiguration.IvschatLoggingConfigurationDestinationConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "cloudwatch_logs": "cloudwatchLogs",
        "firehose": "firehose",
        "s3": "s3",
    },
)
class IvschatLoggingConfigurationDestinationConfiguration:
    def __init__(
        self,
        *,
        cloudwatch_logs: typing.Optional[typing.Union["IvschatLoggingConfigurationDestinationConfigurationCloudwatchLogs", typing.Dict[builtins.str, typing.Any]]] = None,
        firehose: typing.Optional[typing.Union["IvschatLoggingConfigurationDestinationConfigurationFirehose", typing.Dict[builtins.str, typing.Any]]] = None,
        s3: typing.Optional[typing.Union["IvschatLoggingConfigurationDestinationConfigurationS3", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cloudwatch_logs: cloudwatch_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivschat_logging_configuration#cloudwatch_logs IvschatLoggingConfiguration#cloudwatch_logs}
        :param firehose: firehose block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivschat_logging_configuration#firehose IvschatLoggingConfiguration#firehose}
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivschat_logging_configuration#s3 IvschatLoggingConfiguration#s3}
        '''
        if isinstance(cloudwatch_logs, dict):
            cloudwatch_logs = IvschatLoggingConfigurationDestinationConfigurationCloudwatchLogs(**cloudwatch_logs)
        if isinstance(firehose, dict):
            firehose = IvschatLoggingConfigurationDestinationConfigurationFirehose(**firehose)
        if isinstance(s3, dict):
            s3 = IvschatLoggingConfigurationDestinationConfigurationS3(**s3)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__268d55c3b0bd56c82d495e33d411fada74946f75749258126ec0ead98f7cee39)
            check_type(argname="argument cloudwatch_logs", value=cloudwatch_logs, expected_type=type_hints["cloudwatch_logs"])
            check_type(argname="argument firehose", value=firehose, expected_type=type_hints["firehose"])
            check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cloudwatch_logs is not None:
            self._values["cloudwatch_logs"] = cloudwatch_logs
        if firehose is not None:
            self._values["firehose"] = firehose
        if s3 is not None:
            self._values["s3"] = s3

    @builtins.property
    def cloudwatch_logs(
        self,
    ) -> typing.Optional["IvschatLoggingConfigurationDestinationConfigurationCloudwatchLogs"]:
        '''cloudwatch_logs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivschat_logging_configuration#cloudwatch_logs IvschatLoggingConfiguration#cloudwatch_logs}
        '''
        result = self._values.get("cloudwatch_logs")
        return typing.cast(typing.Optional["IvschatLoggingConfigurationDestinationConfigurationCloudwatchLogs"], result)

    @builtins.property
    def firehose(
        self,
    ) -> typing.Optional["IvschatLoggingConfigurationDestinationConfigurationFirehose"]:
        '''firehose block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivschat_logging_configuration#firehose IvschatLoggingConfiguration#firehose}
        '''
        result = self._values.get("firehose")
        return typing.cast(typing.Optional["IvschatLoggingConfigurationDestinationConfigurationFirehose"], result)

    @builtins.property
    def s3(
        self,
    ) -> typing.Optional["IvschatLoggingConfigurationDestinationConfigurationS3"]:
        '''s3 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivschat_logging_configuration#s3 IvschatLoggingConfiguration#s3}
        '''
        result = self._values.get("s3")
        return typing.cast(typing.Optional["IvschatLoggingConfigurationDestinationConfigurationS3"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IvschatLoggingConfigurationDestinationConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.ivschatLoggingConfiguration.IvschatLoggingConfigurationDestinationConfigurationCloudwatchLogs",
    jsii_struct_bases=[],
    name_mapping={"log_group_name": "logGroupName"},
)
class IvschatLoggingConfigurationDestinationConfigurationCloudwatchLogs:
    def __init__(self, *, log_group_name: builtins.str) -> None:
        '''
        :param log_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivschat_logging_configuration#log_group_name IvschatLoggingConfiguration#log_group_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90966883813a98b7f865ba61d39308d5669354a28b3898457d6a5674fa9a24d6)
            check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "log_group_name": log_group_name,
        }

    @builtins.property
    def log_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivschat_logging_configuration#log_group_name IvschatLoggingConfiguration#log_group_name}.'''
        result = self._values.get("log_group_name")
        assert result is not None, "Required property 'log_group_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IvschatLoggingConfigurationDestinationConfigurationCloudwatchLogs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IvschatLoggingConfigurationDestinationConfigurationCloudwatchLogsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ivschatLoggingConfiguration.IvschatLoggingConfigurationDestinationConfigurationCloudwatchLogsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6f1b1192111ed6de80d8b2a0ceef44ea5d40193e883a456ebceea7548d303932)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="logGroupNameInput")
    def log_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logGroupName"))

    @log_group_name.setter
    def log_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21fbe99d06994837a614918121b3cda0b1746a58e59c7c0c7cfdedd7111869d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[IvschatLoggingConfigurationDestinationConfigurationCloudwatchLogs]:
        return typing.cast(typing.Optional[IvschatLoggingConfigurationDestinationConfigurationCloudwatchLogs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IvschatLoggingConfigurationDestinationConfigurationCloudwatchLogs],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b0da47e118ed2e7b00c3419cd52bd8a72dac81403df33155270a24a7adda3e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ivschatLoggingConfiguration.IvschatLoggingConfigurationDestinationConfigurationFirehose",
    jsii_struct_bases=[],
    name_mapping={"delivery_stream_name": "deliveryStreamName"},
)
class IvschatLoggingConfigurationDestinationConfigurationFirehose:
    def __init__(self, *, delivery_stream_name: builtins.str) -> None:
        '''
        :param delivery_stream_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivschat_logging_configuration#delivery_stream_name IvschatLoggingConfiguration#delivery_stream_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96c84a2df65809134a6354dec376da40553698c6a1f06e0b74a8a0f422515bab)
            check_type(argname="argument delivery_stream_name", value=delivery_stream_name, expected_type=type_hints["delivery_stream_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "delivery_stream_name": delivery_stream_name,
        }

    @builtins.property
    def delivery_stream_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivschat_logging_configuration#delivery_stream_name IvschatLoggingConfiguration#delivery_stream_name}.'''
        result = self._values.get("delivery_stream_name")
        assert result is not None, "Required property 'delivery_stream_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IvschatLoggingConfigurationDestinationConfigurationFirehose(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IvschatLoggingConfigurationDestinationConfigurationFirehoseOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ivschatLoggingConfiguration.IvschatLoggingConfigurationDestinationConfigurationFirehoseOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7ac35369fb0d515844426e08e4432aa744f0abc24289e6383a71e8008a8821e7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="deliveryStreamNameInput")
    def delivery_stream_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deliveryStreamNameInput"))

    @builtins.property
    @jsii.member(jsii_name="deliveryStreamName")
    def delivery_stream_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deliveryStreamName"))

    @delivery_stream_name.setter
    def delivery_stream_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2314ff6a928cf5a99362a085ad5db80603585265d6b626903a6991ec3369f3b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deliveryStreamName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[IvschatLoggingConfigurationDestinationConfigurationFirehose]:
        return typing.cast(typing.Optional[IvschatLoggingConfigurationDestinationConfigurationFirehose], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IvschatLoggingConfigurationDestinationConfigurationFirehose],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99c30e2b8cf445fe668e178d30ae1fba2b9a3f994789781714fbc9742da9ec02)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IvschatLoggingConfigurationDestinationConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ivschatLoggingConfiguration.IvschatLoggingConfigurationDestinationConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__12f06ef16618f76ed67ef2b44001f55e9f35924d2a6e26d54e3ec66692f68755)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCloudwatchLogs")
    def put_cloudwatch_logs(self, *, log_group_name: builtins.str) -> None:
        '''
        :param log_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivschat_logging_configuration#log_group_name IvschatLoggingConfiguration#log_group_name}.
        '''
        value = IvschatLoggingConfigurationDestinationConfigurationCloudwatchLogs(
            log_group_name=log_group_name
        )

        return typing.cast(None, jsii.invoke(self, "putCloudwatchLogs", [value]))

    @jsii.member(jsii_name="putFirehose")
    def put_firehose(self, *, delivery_stream_name: builtins.str) -> None:
        '''
        :param delivery_stream_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivschat_logging_configuration#delivery_stream_name IvschatLoggingConfiguration#delivery_stream_name}.
        '''
        value = IvschatLoggingConfigurationDestinationConfigurationFirehose(
            delivery_stream_name=delivery_stream_name
        )

        return typing.cast(None, jsii.invoke(self, "putFirehose", [value]))

    @jsii.member(jsii_name="putS3")
    def put_s3(self, *, bucket_name: builtins.str) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivschat_logging_configuration#bucket_name IvschatLoggingConfiguration#bucket_name}.
        '''
        value = IvschatLoggingConfigurationDestinationConfigurationS3(
            bucket_name=bucket_name
        )

        return typing.cast(None, jsii.invoke(self, "putS3", [value]))

    @jsii.member(jsii_name="resetCloudwatchLogs")
    def reset_cloudwatch_logs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudwatchLogs", []))

    @jsii.member(jsii_name="resetFirehose")
    def reset_firehose(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFirehose", []))

    @jsii.member(jsii_name="resetS3")
    def reset_s3(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3", []))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLogs")
    def cloudwatch_logs(
        self,
    ) -> IvschatLoggingConfigurationDestinationConfigurationCloudwatchLogsOutputReference:
        return typing.cast(IvschatLoggingConfigurationDestinationConfigurationCloudwatchLogsOutputReference, jsii.get(self, "cloudwatchLogs"))

    @builtins.property
    @jsii.member(jsii_name="firehose")
    def firehose(
        self,
    ) -> IvschatLoggingConfigurationDestinationConfigurationFirehoseOutputReference:
        return typing.cast(IvschatLoggingConfigurationDestinationConfigurationFirehoseOutputReference, jsii.get(self, "firehose"))

    @builtins.property
    @jsii.member(jsii_name="s3")
    def s3(
        self,
    ) -> "IvschatLoggingConfigurationDestinationConfigurationS3OutputReference":
        return typing.cast("IvschatLoggingConfigurationDestinationConfigurationS3OutputReference", jsii.get(self, "s3"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLogsInput")
    def cloudwatch_logs_input(
        self,
    ) -> typing.Optional[IvschatLoggingConfigurationDestinationConfigurationCloudwatchLogs]:
        return typing.cast(typing.Optional[IvschatLoggingConfigurationDestinationConfigurationCloudwatchLogs], jsii.get(self, "cloudwatchLogsInput"))

    @builtins.property
    @jsii.member(jsii_name="firehoseInput")
    def firehose_input(
        self,
    ) -> typing.Optional[IvschatLoggingConfigurationDestinationConfigurationFirehose]:
        return typing.cast(typing.Optional[IvschatLoggingConfigurationDestinationConfigurationFirehose], jsii.get(self, "firehoseInput"))

    @builtins.property
    @jsii.member(jsii_name="s3Input")
    def s3_input(
        self,
    ) -> typing.Optional["IvschatLoggingConfigurationDestinationConfigurationS3"]:
        return typing.cast(typing.Optional["IvschatLoggingConfigurationDestinationConfigurationS3"], jsii.get(self, "s3Input"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[IvschatLoggingConfigurationDestinationConfiguration]:
        return typing.cast(typing.Optional[IvschatLoggingConfigurationDestinationConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IvschatLoggingConfigurationDestinationConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ee9aefe6df8ed9561742efb9577258d2f3b140b94b957e8162e24358fbcc3f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ivschatLoggingConfiguration.IvschatLoggingConfigurationDestinationConfigurationS3",
    jsii_struct_bases=[],
    name_mapping={"bucket_name": "bucketName"},
)
class IvschatLoggingConfigurationDestinationConfigurationS3:
    def __init__(self, *, bucket_name: builtins.str) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivschat_logging_configuration#bucket_name IvschatLoggingConfiguration#bucket_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bd9145ee97f0229eaf2a90423d22877ee44763b2d5e0ed3250edee493c53edd)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket_name": bucket_name,
        }

    @builtins.property
    def bucket_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivschat_logging_configuration#bucket_name IvschatLoggingConfiguration#bucket_name}.'''
        result = self._values.get("bucket_name")
        assert result is not None, "Required property 'bucket_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IvschatLoggingConfigurationDestinationConfigurationS3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IvschatLoggingConfigurationDestinationConfigurationS3OutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ivschatLoggingConfiguration.IvschatLoggingConfigurationDestinationConfigurationS3OutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__153568cea95f5b16758a53ba6f74f86fd123680c6ead2b1a38c86138268b4c21)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3fc48f5153d16aa54ef805ca2000af235045dfbe750ce5280a6a99206a5decc7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[IvschatLoggingConfigurationDestinationConfigurationS3]:
        return typing.cast(typing.Optional[IvschatLoggingConfigurationDestinationConfigurationS3], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IvschatLoggingConfigurationDestinationConfigurationS3],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d6bc38773c4d371e09d3cd1d55406aa9ade10137e6ac4e0e441b3bdb288efe3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ivschatLoggingConfiguration.IvschatLoggingConfigurationTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class IvschatLoggingConfigurationTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivschat_logging_configuration#create IvschatLoggingConfiguration#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivschat_logging_configuration#delete IvschatLoggingConfiguration#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivschat_logging_configuration#update IvschatLoggingConfiguration#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__414841ecabd6534fb60aca3f0995e6a250939c7be813aec8bf1ebf00850e1459)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivschat_logging_configuration#create IvschatLoggingConfiguration#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivschat_logging_configuration#delete IvschatLoggingConfiguration#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ivschat_logging_configuration#update IvschatLoggingConfiguration#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IvschatLoggingConfigurationTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IvschatLoggingConfigurationTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ivschatLoggingConfiguration.IvschatLoggingConfigurationTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__aa51b4018a1c0c09923628324e921e554342ca19e744733478bbce4eb274988a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__79d396e6d2912a113ac098a5418ac9193f1a31abcecac97ddc4562216022e953)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2b2fe75419c6b889aab7f180604e7b31821031941096b041e38eadc62a9b028)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4cab91e76f7da18bdfb30844ef7a5a7bea0f62cab878f1402b6d05f96b5414bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IvschatLoggingConfigurationTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IvschatLoggingConfigurationTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IvschatLoggingConfigurationTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68f7774b4ca4d688a43b8fa21d1b026eb645da6de035a24282692df781b2f902)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "IvschatLoggingConfiguration",
    "IvschatLoggingConfigurationConfig",
    "IvschatLoggingConfigurationDestinationConfiguration",
    "IvschatLoggingConfigurationDestinationConfigurationCloudwatchLogs",
    "IvschatLoggingConfigurationDestinationConfigurationCloudwatchLogsOutputReference",
    "IvschatLoggingConfigurationDestinationConfigurationFirehose",
    "IvschatLoggingConfigurationDestinationConfigurationFirehoseOutputReference",
    "IvschatLoggingConfigurationDestinationConfigurationOutputReference",
    "IvschatLoggingConfigurationDestinationConfigurationS3",
    "IvschatLoggingConfigurationDestinationConfigurationS3OutputReference",
    "IvschatLoggingConfigurationTimeouts",
    "IvschatLoggingConfigurationTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__aa92f3e623999a95853ef218fccb136d2c26c822b4584ab341fd43bd262b23c3(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    destination_configuration: typing.Optional[typing.Union[IvschatLoggingConfigurationDestinationConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[IvschatLoggingConfigurationTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__25c2e50f111b11428e9676410a69269cb3cd7eb59651f4f3651254ceb2178970(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1588c34eec3191ab377f1f45e1c25e2d81b287791e9c7772390c07b5eb9b7efc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b2bb8597bf5d513054c8f17f315f54194ae9c5b68dbff1d6350754497859ad5(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7e19a20ca503b0b57fcbe5666861cac5db780dace70e558b68e5e4b5da5abe4(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c19575c2f43ccd35c7dbbe55cf31fff97823c316e60bdcd60abd01ba89021ab(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    destination_configuration: typing.Optional[typing.Union[IvschatLoggingConfigurationDestinationConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[IvschatLoggingConfigurationTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__268d55c3b0bd56c82d495e33d411fada74946f75749258126ec0ead98f7cee39(
    *,
    cloudwatch_logs: typing.Optional[typing.Union[IvschatLoggingConfigurationDestinationConfigurationCloudwatchLogs, typing.Dict[builtins.str, typing.Any]]] = None,
    firehose: typing.Optional[typing.Union[IvschatLoggingConfigurationDestinationConfigurationFirehose, typing.Dict[builtins.str, typing.Any]]] = None,
    s3: typing.Optional[typing.Union[IvschatLoggingConfigurationDestinationConfigurationS3, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90966883813a98b7f865ba61d39308d5669354a28b3898457d6a5674fa9a24d6(
    *,
    log_group_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f1b1192111ed6de80d8b2a0ceef44ea5d40193e883a456ebceea7548d303932(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21fbe99d06994837a614918121b3cda0b1746a58e59c7c0c7cfdedd7111869d3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b0da47e118ed2e7b00c3419cd52bd8a72dac81403df33155270a24a7adda3e5(
    value: typing.Optional[IvschatLoggingConfigurationDestinationConfigurationCloudwatchLogs],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96c84a2df65809134a6354dec376da40553698c6a1f06e0b74a8a0f422515bab(
    *,
    delivery_stream_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ac35369fb0d515844426e08e4432aa744f0abc24289e6383a71e8008a8821e7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2314ff6a928cf5a99362a085ad5db80603585265d6b626903a6991ec3369f3b2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99c30e2b8cf445fe668e178d30ae1fba2b9a3f994789781714fbc9742da9ec02(
    value: typing.Optional[IvschatLoggingConfigurationDestinationConfigurationFirehose],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12f06ef16618f76ed67ef2b44001f55e9f35924d2a6e26d54e3ec66692f68755(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ee9aefe6df8ed9561742efb9577258d2f3b140b94b957e8162e24358fbcc3f9(
    value: typing.Optional[IvschatLoggingConfigurationDestinationConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bd9145ee97f0229eaf2a90423d22877ee44763b2d5e0ed3250edee493c53edd(
    *,
    bucket_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__153568cea95f5b16758a53ba6f74f86fd123680c6ead2b1a38c86138268b4c21(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fc48f5153d16aa54ef805ca2000af235045dfbe750ce5280a6a99206a5decc7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d6bc38773c4d371e09d3cd1d55406aa9ade10137e6ac4e0e441b3bdb288efe3(
    value: typing.Optional[IvschatLoggingConfigurationDestinationConfigurationS3],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__414841ecabd6534fb60aca3f0995e6a250939c7be813aec8bf1ebf00850e1459(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa51b4018a1c0c09923628324e921e554342ca19e744733478bbce4eb274988a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79d396e6d2912a113ac098a5418ac9193f1a31abcecac97ddc4562216022e953(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2b2fe75419c6b889aab7f180604e7b31821031941096b041e38eadc62a9b028(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cab91e76f7da18bdfb30844ef7a5a7bea0f62cab878f1402b6d05f96b5414bd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68f7774b4ca4d688a43b8fa21d1b026eb645da6de035a24282692df781b2f902(
    value: typing.Optional[typing.Union[IvschatLoggingConfigurationTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
