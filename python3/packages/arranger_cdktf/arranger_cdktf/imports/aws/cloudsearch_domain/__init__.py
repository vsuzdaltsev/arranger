'''
# `aws_cloudsearch_domain`

Refer to the Terraform Registory for docs: [`aws_cloudsearch_domain`](https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain).
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


class CloudsearchDomain(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudsearchDomain.CloudsearchDomain",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain aws_cloudsearch_domain}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        endpoint_options: typing.Optional[typing.Union["CloudsearchDomainEndpointOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        index_field: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CloudsearchDomainIndexField", typing.Dict[builtins.str, typing.Any]]]]] = None,
        multi_az: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        scaling_parameters: typing.Optional[typing.Union["CloudsearchDomainScalingParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["CloudsearchDomainTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain aws_cloudsearch_domain} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#name CloudsearchDomain#name}.
        :param endpoint_options: endpoint_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#endpoint_options CloudsearchDomain#endpoint_options}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#id CloudsearchDomain#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param index_field: index_field block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#index_field CloudsearchDomain#index_field}
        :param multi_az: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#multi_az CloudsearchDomain#multi_az}.
        :param scaling_parameters: scaling_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#scaling_parameters CloudsearchDomain#scaling_parameters}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#timeouts CloudsearchDomain#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d8b750f17559b5ced0db7d7fc38f179979ae072ccd5f4908f8ccb6a80baa775)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CloudsearchDomainConfig(
            name=name,
            endpoint_options=endpoint_options,
            id=id,
            index_field=index_field,
            multi_az=multi_az,
            scaling_parameters=scaling_parameters,
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

    @jsii.member(jsii_name="putEndpointOptions")
    def put_endpoint_options(
        self,
        *,
        enforce_https: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        tls_security_policy: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enforce_https: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#enforce_https CloudsearchDomain#enforce_https}.
        :param tls_security_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#tls_security_policy CloudsearchDomain#tls_security_policy}.
        '''
        value = CloudsearchDomainEndpointOptions(
            enforce_https=enforce_https, tls_security_policy=tls_security_policy
        )

        return typing.cast(None, jsii.invoke(self, "putEndpointOptions", [value]))

    @jsii.member(jsii_name="putIndexField")
    def put_index_field(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CloudsearchDomainIndexField", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7eb2712ce013b6556ae496fbbadb2226e767548b05962433b94ff796351477e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putIndexField", [value]))

    @jsii.member(jsii_name="putScalingParameters")
    def put_scaling_parameters(
        self,
        *,
        desired_instance_type: typing.Optional[builtins.str] = None,
        desired_partition_count: typing.Optional[jsii.Number] = None,
        desired_replication_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param desired_instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#desired_instance_type CloudsearchDomain#desired_instance_type}.
        :param desired_partition_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#desired_partition_count CloudsearchDomain#desired_partition_count}.
        :param desired_replication_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#desired_replication_count CloudsearchDomain#desired_replication_count}.
        '''
        value = CloudsearchDomainScalingParameters(
            desired_instance_type=desired_instance_type,
            desired_partition_count=desired_partition_count,
            desired_replication_count=desired_replication_count,
        )

        return typing.cast(None, jsii.invoke(self, "putScalingParameters", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#create CloudsearchDomain#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#delete CloudsearchDomain#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#update CloudsearchDomain#update}.
        '''
        value = CloudsearchDomainTimeouts(create=create, delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetEndpointOptions")
    def reset_endpoint_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndpointOptions", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIndexField")
    def reset_index_field(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIndexField", []))

    @jsii.member(jsii_name="resetMultiAz")
    def reset_multi_az(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMultiAz", []))

    @jsii.member(jsii_name="resetScalingParameters")
    def reset_scaling_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScalingParameters", []))

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
    @jsii.member(jsii_name="documentServiceEndpoint")
    def document_service_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "documentServiceEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="domainId")
    def domain_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainId"))

    @builtins.property
    @jsii.member(jsii_name="endpointOptions")
    def endpoint_options(self) -> "CloudsearchDomainEndpointOptionsOutputReference":
        return typing.cast("CloudsearchDomainEndpointOptionsOutputReference", jsii.get(self, "endpointOptions"))

    @builtins.property
    @jsii.member(jsii_name="indexField")
    def index_field(self) -> "CloudsearchDomainIndexFieldList":
        return typing.cast("CloudsearchDomainIndexFieldList", jsii.get(self, "indexField"))

    @builtins.property
    @jsii.member(jsii_name="scalingParameters")
    def scaling_parameters(self) -> "CloudsearchDomainScalingParametersOutputReference":
        return typing.cast("CloudsearchDomainScalingParametersOutputReference", jsii.get(self, "scalingParameters"))

    @builtins.property
    @jsii.member(jsii_name="searchServiceEndpoint")
    def search_service_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "searchServiceEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "CloudsearchDomainTimeoutsOutputReference":
        return typing.cast("CloudsearchDomainTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="endpointOptionsInput")
    def endpoint_options_input(
        self,
    ) -> typing.Optional["CloudsearchDomainEndpointOptions"]:
        return typing.cast(typing.Optional["CloudsearchDomainEndpointOptions"], jsii.get(self, "endpointOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="indexFieldInput")
    def index_field_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudsearchDomainIndexField"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudsearchDomainIndexField"]]], jsii.get(self, "indexFieldInput"))

    @builtins.property
    @jsii.member(jsii_name="multiAzInput")
    def multi_az_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "multiAzInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="scalingParametersInput")
    def scaling_parameters_input(
        self,
    ) -> typing.Optional["CloudsearchDomainScalingParameters"]:
        return typing.cast(typing.Optional["CloudsearchDomainScalingParameters"], jsii.get(self, "scalingParametersInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["CloudsearchDomainTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["CloudsearchDomainTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc1236afc03ec2c91613221663479a3b5a5ca2f0092bdf58d3562a5a17285b27)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="multiAz")
    def multi_az(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "multiAz"))

    @multi_az.setter
    def multi_az(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c9163728b41e70ab1bbcf22a18eee1b0c43fc3a1a0bc684f957633df91a111c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "multiAz", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1e4bab20e369ca3a85eec2a8f1d302eb252aed9f3644dda28cee0d905fb2cd6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="aws.cloudsearchDomain.CloudsearchDomainConfig",
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
        "endpoint_options": "endpointOptions",
        "id": "id",
        "index_field": "indexField",
        "multi_az": "multiAz",
        "scaling_parameters": "scalingParameters",
        "timeouts": "timeouts",
    },
)
class CloudsearchDomainConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        endpoint_options: typing.Optional[typing.Union["CloudsearchDomainEndpointOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        index_field: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CloudsearchDomainIndexField", typing.Dict[builtins.str, typing.Any]]]]] = None,
        multi_az: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        scaling_parameters: typing.Optional[typing.Union["CloudsearchDomainScalingParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["CloudsearchDomainTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#name CloudsearchDomain#name}.
        :param endpoint_options: endpoint_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#endpoint_options CloudsearchDomain#endpoint_options}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#id CloudsearchDomain#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param index_field: index_field block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#index_field CloudsearchDomain#index_field}
        :param multi_az: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#multi_az CloudsearchDomain#multi_az}.
        :param scaling_parameters: scaling_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#scaling_parameters CloudsearchDomain#scaling_parameters}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#timeouts CloudsearchDomain#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(endpoint_options, dict):
            endpoint_options = CloudsearchDomainEndpointOptions(**endpoint_options)
        if isinstance(scaling_parameters, dict):
            scaling_parameters = CloudsearchDomainScalingParameters(**scaling_parameters)
        if isinstance(timeouts, dict):
            timeouts = CloudsearchDomainTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fdcf0bac4141eefc773623d8cd2f99f50d5d19bfe31a39a36c036353af76fb30)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument endpoint_options", value=endpoint_options, expected_type=type_hints["endpoint_options"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument index_field", value=index_field, expected_type=type_hints["index_field"])
            check_type(argname="argument multi_az", value=multi_az, expected_type=type_hints["multi_az"])
            check_type(argname="argument scaling_parameters", value=scaling_parameters, expected_type=type_hints["scaling_parameters"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
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
        if endpoint_options is not None:
            self._values["endpoint_options"] = endpoint_options
        if id is not None:
            self._values["id"] = id
        if index_field is not None:
            self._values["index_field"] = index_field
        if multi_az is not None:
            self._values["multi_az"] = multi_az
        if scaling_parameters is not None:
            self._values["scaling_parameters"] = scaling_parameters
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
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#name CloudsearchDomain#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def endpoint_options(self) -> typing.Optional["CloudsearchDomainEndpointOptions"]:
        '''endpoint_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#endpoint_options CloudsearchDomain#endpoint_options}
        '''
        result = self._values.get("endpoint_options")
        return typing.cast(typing.Optional["CloudsearchDomainEndpointOptions"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#id CloudsearchDomain#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def index_field(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudsearchDomainIndexField"]]]:
        '''index_field block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#index_field CloudsearchDomain#index_field}
        '''
        result = self._values.get("index_field")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudsearchDomainIndexField"]]], result)

    @builtins.property
    def multi_az(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#multi_az CloudsearchDomain#multi_az}.'''
        result = self._values.get("multi_az")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def scaling_parameters(
        self,
    ) -> typing.Optional["CloudsearchDomainScalingParameters"]:
        '''scaling_parameters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#scaling_parameters CloudsearchDomain#scaling_parameters}
        '''
        result = self._values.get("scaling_parameters")
        return typing.cast(typing.Optional["CloudsearchDomainScalingParameters"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["CloudsearchDomainTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#timeouts CloudsearchDomain#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["CloudsearchDomainTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudsearchDomainConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.cloudsearchDomain.CloudsearchDomainEndpointOptions",
    jsii_struct_bases=[],
    name_mapping={
        "enforce_https": "enforceHttps",
        "tls_security_policy": "tlsSecurityPolicy",
    },
)
class CloudsearchDomainEndpointOptions:
    def __init__(
        self,
        *,
        enforce_https: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        tls_security_policy: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enforce_https: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#enforce_https CloudsearchDomain#enforce_https}.
        :param tls_security_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#tls_security_policy CloudsearchDomain#tls_security_policy}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94e31a3516782a3009342a95a11923595ac24465d7783d10c32f88bb4816089b)
            check_type(argname="argument enforce_https", value=enforce_https, expected_type=type_hints["enforce_https"])
            check_type(argname="argument tls_security_policy", value=tls_security_policy, expected_type=type_hints["tls_security_policy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enforce_https is not None:
            self._values["enforce_https"] = enforce_https
        if tls_security_policy is not None:
            self._values["tls_security_policy"] = tls_security_policy

    @builtins.property
    def enforce_https(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#enforce_https CloudsearchDomain#enforce_https}.'''
        result = self._values.get("enforce_https")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def tls_security_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#tls_security_policy CloudsearchDomain#tls_security_policy}.'''
        result = self._values.get("tls_security_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudsearchDomainEndpointOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudsearchDomainEndpointOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudsearchDomain.CloudsearchDomainEndpointOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a0b88a5781210617562d69ee9d2f0ba7f665c7c3f23032c76c0dd0f0d958507c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnforceHttps")
    def reset_enforce_https(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnforceHttps", []))

    @jsii.member(jsii_name="resetTlsSecurityPolicy")
    def reset_tls_security_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsSecurityPolicy", []))

    @builtins.property
    @jsii.member(jsii_name="enforceHttpsInput")
    def enforce_https_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enforceHttpsInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsSecurityPolicyInput")
    def tls_security_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tlsSecurityPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="enforceHttps")
    def enforce_https(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enforceHttps"))

    @enforce_https.setter
    def enforce_https(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb5d9cbf58b88c975570c216463e877c9c6e2f3f41d60208b5bdde0912b71512)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enforceHttps", value)

    @builtins.property
    @jsii.member(jsii_name="tlsSecurityPolicy")
    def tls_security_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tlsSecurityPolicy"))

    @tls_security_policy.setter
    def tls_security_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8929176d01e354faf7ad8e3a5a07bc71cfd68311f7c656cbcec20bf011a8644a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsSecurityPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudsearchDomainEndpointOptions]:
        return typing.cast(typing.Optional[CloudsearchDomainEndpointOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudsearchDomainEndpointOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53ad71beedc0f4737f92c968117e74606a34c4c385fc03869c8881e17d186bf2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cloudsearchDomain.CloudsearchDomainIndexField",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "type": "type",
        "analysis_scheme": "analysisScheme",
        "default_value": "defaultValue",
        "facet": "facet",
        "highlight": "highlight",
        "return_": "return",
        "search": "search",
        "sort": "sort",
        "source_fields": "sourceFields",
    },
)
class CloudsearchDomainIndexField:
    def __init__(
        self,
        *,
        name: builtins.str,
        type: builtins.str,
        analysis_scheme: typing.Optional[builtins.str] = None,
        default_value: typing.Optional[builtins.str] = None,
        facet: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        highlight: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        return_: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        search: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        sort: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        source_fields: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#name CloudsearchDomain#name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#type CloudsearchDomain#type}.
        :param analysis_scheme: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#analysis_scheme CloudsearchDomain#analysis_scheme}.
        :param default_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#default_value CloudsearchDomain#default_value}.
        :param facet: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#facet CloudsearchDomain#facet}.
        :param highlight: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#highlight CloudsearchDomain#highlight}.
        :param return_: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#return CloudsearchDomain#return}.
        :param search: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#search CloudsearchDomain#search}.
        :param sort: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#sort CloudsearchDomain#sort}.
        :param source_fields: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#source_fields CloudsearchDomain#source_fields}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1825c7fae1b8bc89047830cd06ca5c2fee0107a906289e69468b05ac248397b8)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument analysis_scheme", value=analysis_scheme, expected_type=type_hints["analysis_scheme"])
            check_type(argname="argument default_value", value=default_value, expected_type=type_hints["default_value"])
            check_type(argname="argument facet", value=facet, expected_type=type_hints["facet"])
            check_type(argname="argument highlight", value=highlight, expected_type=type_hints["highlight"])
            check_type(argname="argument return_", value=return_, expected_type=type_hints["return_"])
            check_type(argname="argument search", value=search, expected_type=type_hints["search"])
            check_type(argname="argument sort", value=sort, expected_type=type_hints["sort"])
            check_type(argname="argument source_fields", value=source_fields, expected_type=type_hints["source_fields"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "type": type,
        }
        if analysis_scheme is not None:
            self._values["analysis_scheme"] = analysis_scheme
        if default_value is not None:
            self._values["default_value"] = default_value
        if facet is not None:
            self._values["facet"] = facet
        if highlight is not None:
            self._values["highlight"] = highlight
        if return_ is not None:
            self._values["return_"] = return_
        if search is not None:
            self._values["search"] = search
        if sort is not None:
            self._values["sort"] = sort
        if source_fields is not None:
            self._values["source_fields"] = source_fields

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#name CloudsearchDomain#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#type CloudsearchDomain#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def analysis_scheme(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#analysis_scheme CloudsearchDomain#analysis_scheme}.'''
        result = self._values.get("analysis_scheme")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#default_value CloudsearchDomain#default_value}.'''
        result = self._values.get("default_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def facet(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#facet CloudsearchDomain#facet}.'''
        result = self._values.get("facet")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def highlight(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#highlight CloudsearchDomain#highlight}.'''
        result = self._values.get("highlight")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def return_(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#return CloudsearchDomain#return}.'''
        result = self._values.get("return_")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def search(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#search CloudsearchDomain#search}.'''
        result = self._values.get("search")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def sort(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#sort CloudsearchDomain#sort}.'''
        result = self._values.get("sort")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def source_fields(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#source_fields CloudsearchDomain#source_fields}.'''
        result = self._values.get("source_fields")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudsearchDomainIndexField(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudsearchDomainIndexFieldList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudsearchDomain.CloudsearchDomainIndexFieldList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c76ff41c84d31f3612895b405ec6ef208b89dd5b78f5b96bbe273b737d8e0266)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "CloudsearchDomainIndexFieldOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fcdccb49b0e2d313ec0dda4309726d58958b1cd36ff24a98a082fcb9dbd580c6)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CloudsearchDomainIndexFieldOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1342a237831de206e0fecf71b656019abdfdcb4ad6ab214a7ecc3fedd51c147d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8452d9fa98ed5de1005af1bf03857463e898ca28e011fdb0aa601f91113c6263)
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
            type_hints = typing.get_type_hints(_typecheckingstub__05d611834d021568b3ee05f2a9f872f03387f30196f2f427ec2e3643809060b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudsearchDomainIndexField]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudsearchDomainIndexField]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudsearchDomainIndexField]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4958778d3bb244222f99d46037e4ccf592d4b1b729faa0ac8d33eeb6c1c0181a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudsearchDomainIndexFieldOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudsearchDomain.CloudsearchDomainIndexFieldOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0c75fcda15cbe2f5ecb65fd53d86e92a6039b40b230163fc2d154a6ffb248de0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAnalysisScheme")
    def reset_analysis_scheme(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnalysisScheme", []))

    @jsii.member(jsii_name="resetDefaultValue")
    def reset_default_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultValue", []))

    @jsii.member(jsii_name="resetFacet")
    def reset_facet(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFacet", []))

    @jsii.member(jsii_name="resetHighlight")
    def reset_highlight(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHighlight", []))

    @jsii.member(jsii_name="resetReturn")
    def reset_return(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReturn", []))

    @jsii.member(jsii_name="resetSearch")
    def reset_search(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSearch", []))

    @jsii.member(jsii_name="resetSort")
    def reset_sort(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSort", []))

    @jsii.member(jsii_name="resetSourceFields")
    def reset_source_fields(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceFields", []))

    @builtins.property
    @jsii.member(jsii_name="analysisSchemeInput")
    def analysis_scheme_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "analysisSchemeInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultValueInput")
    def default_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultValueInput"))

    @builtins.property
    @jsii.member(jsii_name="facetInput")
    def facet_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "facetInput"))

    @builtins.property
    @jsii.member(jsii_name="highlightInput")
    def highlight_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "highlightInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="returnInput")
    def return_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "returnInput"))

    @builtins.property
    @jsii.member(jsii_name="searchInput")
    def search_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "searchInput"))

    @builtins.property
    @jsii.member(jsii_name="sortInput")
    def sort_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "sortInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceFieldsInput")
    def source_fields_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceFieldsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="analysisScheme")
    def analysis_scheme(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "analysisScheme"))

    @analysis_scheme.setter
    def analysis_scheme(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6bfdf7a98fa42208b4c180a0d401732f50f7ab0831f6d3435436f2b521726147)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "analysisScheme", value)

    @builtins.property
    @jsii.member(jsii_name="defaultValue")
    def default_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultValue"))

    @default_value.setter
    def default_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__508c5d93f06e3baf4e62e1f0bfd59eba7320578a221b08768f49236cdaf26797)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultValue", value)

    @builtins.property
    @jsii.member(jsii_name="facet")
    def facet(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "facet"))

    @facet.setter
    def facet(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__430191a603b0092fd7a2181d1b9781a768287e53a7e96daf5e6457695b5da3cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "facet", value)

    @builtins.property
    @jsii.member(jsii_name="highlight")
    def highlight(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "highlight"))

    @highlight.setter
    def highlight(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80e69391cd5f377e2d81ffc3a2c077f0380396670b44c19e1792733d6234ff43)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "highlight", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b03ba7562bdbf9dce6985d4a121769121aaf7038e6976d21bef0f175970ad384)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="return")
    def return_(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "return"))

    @return_.setter
    def return_(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f8c35883d1d3f494fb4bbee57075264f116c553e0d12a3645e39c226d349e01)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "return", value)

    @builtins.property
    @jsii.member(jsii_name="search")
    def search(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "search"))

    @search.setter
    def search(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cefe7efb2412a7230b5b433d5465ed6479b50dd5659a73e17764b999cf451d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "search", value)

    @builtins.property
    @jsii.member(jsii_name="sort")
    def sort(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "sort"))

    @sort.setter
    def sort(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d2b72c5ccd4f6f7ed91798e558396bdda691dd773cd1451570179d2d755ae7a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sort", value)

    @builtins.property
    @jsii.member(jsii_name="sourceFields")
    def source_fields(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceFields"))

    @source_fields.setter
    def source_fields(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9a5c13559f67327bcbcd80433a9f0f3b24000470174b9b424377bd3fff66bbb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceFields", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__acbb8b099e0d5706e71bdb284fe298cd41d51ecfeb914c76dfa57713794dee9f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CloudsearchDomainIndexField, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CloudsearchDomainIndexField, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CloudsearchDomainIndexField, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3f598b61d858dc0d1e37dd0fb2018899aa2106fcf560e3e3aebe519a268f770)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cloudsearchDomain.CloudsearchDomainScalingParameters",
    jsii_struct_bases=[],
    name_mapping={
        "desired_instance_type": "desiredInstanceType",
        "desired_partition_count": "desiredPartitionCount",
        "desired_replication_count": "desiredReplicationCount",
    },
)
class CloudsearchDomainScalingParameters:
    def __init__(
        self,
        *,
        desired_instance_type: typing.Optional[builtins.str] = None,
        desired_partition_count: typing.Optional[jsii.Number] = None,
        desired_replication_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param desired_instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#desired_instance_type CloudsearchDomain#desired_instance_type}.
        :param desired_partition_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#desired_partition_count CloudsearchDomain#desired_partition_count}.
        :param desired_replication_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#desired_replication_count CloudsearchDomain#desired_replication_count}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__913ba150c125038f45436eb50e289b8d3c06fae56d2c55cda22905378e628255)
            check_type(argname="argument desired_instance_type", value=desired_instance_type, expected_type=type_hints["desired_instance_type"])
            check_type(argname="argument desired_partition_count", value=desired_partition_count, expected_type=type_hints["desired_partition_count"])
            check_type(argname="argument desired_replication_count", value=desired_replication_count, expected_type=type_hints["desired_replication_count"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if desired_instance_type is not None:
            self._values["desired_instance_type"] = desired_instance_type
        if desired_partition_count is not None:
            self._values["desired_partition_count"] = desired_partition_count
        if desired_replication_count is not None:
            self._values["desired_replication_count"] = desired_replication_count

    @builtins.property
    def desired_instance_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#desired_instance_type CloudsearchDomain#desired_instance_type}.'''
        result = self._values.get("desired_instance_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def desired_partition_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#desired_partition_count CloudsearchDomain#desired_partition_count}.'''
        result = self._values.get("desired_partition_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def desired_replication_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#desired_replication_count CloudsearchDomain#desired_replication_count}.'''
        result = self._values.get("desired_replication_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudsearchDomainScalingParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudsearchDomainScalingParametersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudsearchDomain.CloudsearchDomainScalingParametersOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__592937a86858340dc3901931a6737176e426f2a89f931961d18e3eb45e8e448d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDesiredInstanceType")
    def reset_desired_instance_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDesiredInstanceType", []))

    @jsii.member(jsii_name="resetDesiredPartitionCount")
    def reset_desired_partition_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDesiredPartitionCount", []))

    @jsii.member(jsii_name="resetDesiredReplicationCount")
    def reset_desired_replication_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDesiredReplicationCount", []))

    @builtins.property
    @jsii.member(jsii_name="desiredInstanceTypeInput")
    def desired_instance_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "desiredInstanceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="desiredPartitionCountInput")
    def desired_partition_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "desiredPartitionCountInput"))

    @builtins.property
    @jsii.member(jsii_name="desiredReplicationCountInput")
    def desired_replication_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "desiredReplicationCountInput"))

    @builtins.property
    @jsii.member(jsii_name="desiredInstanceType")
    def desired_instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "desiredInstanceType"))

    @desired_instance_type.setter
    def desired_instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f2566a46b9eabf585b6126f15676a3d9a8c3540188a02d49d5a6d82eeafb6ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "desiredInstanceType", value)

    @builtins.property
    @jsii.member(jsii_name="desiredPartitionCount")
    def desired_partition_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "desiredPartitionCount"))

    @desired_partition_count.setter
    def desired_partition_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a1c79a8621c02586567fc9c7502ebe2c09bd4bbb8b864c2fea23aa82b64edf7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "desiredPartitionCount", value)

    @builtins.property
    @jsii.member(jsii_name="desiredReplicationCount")
    def desired_replication_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "desiredReplicationCount"))

    @desired_replication_count.setter
    def desired_replication_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7060ccf1acbee047a991e266c05117bb36fece8a77964472b713548bcb0e61dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "desiredReplicationCount", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudsearchDomainScalingParameters]:
        return typing.cast(typing.Optional[CloudsearchDomainScalingParameters], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudsearchDomainScalingParameters],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f81d7e422895f9b80763a74a1f26d87dc1be1f9ac3ebeace1c7b375da486fb2b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cloudsearchDomain.CloudsearchDomainTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class CloudsearchDomainTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#create CloudsearchDomain#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#delete CloudsearchDomain#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#update CloudsearchDomain#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a590eb53f7851c45a25e9f22219d49bf8d7fe27a372f0eb598b7db7d08053aee)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#create CloudsearchDomain#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#delete CloudsearchDomain#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudsearch_domain#update CloudsearchDomain#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudsearchDomainTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudsearchDomainTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudsearchDomain.CloudsearchDomainTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__dd961c50edd8ce977569e0c690a263e98501c54c8d0a609de289f50973e5e934)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1f747de08c5f6d5610fe59b988385ceaaae1e7a11a4e9823b43857b5a2998069)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__573d49c2f548ef415fe765888d64341a992b22f937aa433c0107afbdcbded129)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d9f9b8ce221c646267767681f30eab1c88d77eb4af9b63aa4318e0071b89188)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CloudsearchDomainTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CloudsearchDomainTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CloudsearchDomainTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a957accb6479a01eda8f34e4e9d99f1677b7562b055fce543cae1ea7c215515)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CloudsearchDomain",
    "CloudsearchDomainConfig",
    "CloudsearchDomainEndpointOptions",
    "CloudsearchDomainEndpointOptionsOutputReference",
    "CloudsearchDomainIndexField",
    "CloudsearchDomainIndexFieldList",
    "CloudsearchDomainIndexFieldOutputReference",
    "CloudsearchDomainScalingParameters",
    "CloudsearchDomainScalingParametersOutputReference",
    "CloudsearchDomainTimeouts",
    "CloudsearchDomainTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__6d8b750f17559b5ced0db7d7fc38f179979ae072ccd5f4908f8ccb6a80baa775(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    endpoint_options: typing.Optional[typing.Union[CloudsearchDomainEndpointOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    index_field: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudsearchDomainIndexField, typing.Dict[builtins.str, typing.Any]]]]] = None,
    multi_az: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    scaling_parameters: typing.Optional[typing.Union[CloudsearchDomainScalingParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    timeouts: typing.Optional[typing.Union[CloudsearchDomainTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__7eb2712ce013b6556ae496fbbadb2226e767548b05962433b94ff796351477e8(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudsearchDomainIndexField, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc1236afc03ec2c91613221663479a3b5a5ca2f0092bdf58d3562a5a17285b27(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c9163728b41e70ab1bbcf22a18eee1b0c43fc3a1a0bc684f957633df91a111c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1e4bab20e369ca3a85eec2a8f1d302eb252aed9f3644dda28cee0d905fb2cd6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fdcf0bac4141eefc773623d8cd2f99f50d5d19bfe31a39a36c036353af76fb30(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    endpoint_options: typing.Optional[typing.Union[CloudsearchDomainEndpointOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    index_field: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudsearchDomainIndexField, typing.Dict[builtins.str, typing.Any]]]]] = None,
    multi_az: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    scaling_parameters: typing.Optional[typing.Union[CloudsearchDomainScalingParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    timeouts: typing.Optional[typing.Union[CloudsearchDomainTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94e31a3516782a3009342a95a11923595ac24465d7783d10c32f88bb4816089b(
    *,
    enforce_https: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    tls_security_policy: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0b88a5781210617562d69ee9d2f0ba7f665c7c3f23032c76c0dd0f0d958507c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb5d9cbf58b88c975570c216463e877c9c6e2f3f41d60208b5bdde0912b71512(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8929176d01e354faf7ad8e3a5a07bc71cfd68311f7c656cbcec20bf011a8644a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53ad71beedc0f4737f92c968117e74606a34c4c385fc03869c8881e17d186bf2(
    value: typing.Optional[CloudsearchDomainEndpointOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1825c7fae1b8bc89047830cd06ca5c2fee0107a906289e69468b05ac248397b8(
    *,
    name: builtins.str,
    type: builtins.str,
    analysis_scheme: typing.Optional[builtins.str] = None,
    default_value: typing.Optional[builtins.str] = None,
    facet: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    highlight: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    return_: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    search: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    sort: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    source_fields: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c76ff41c84d31f3612895b405ec6ef208b89dd5b78f5b96bbe273b737d8e0266(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcdccb49b0e2d313ec0dda4309726d58958b1cd36ff24a98a082fcb9dbd580c6(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1342a237831de206e0fecf71b656019abdfdcb4ad6ab214a7ecc3fedd51c147d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8452d9fa98ed5de1005af1bf03857463e898ca28e011fdb0aa601f91113c6263(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05d611834d021568b3ee05f2a9f872f03387f30196f2f427ec2e3643809060b6(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4958778d3bb244222f99d46037e4ccf592d4b1b729faa0ac8d33eeb6c1c0181a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudsearchDomainIndexField]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c75fcda15cbe2f5ecb65fd53d86e92a6039b40b230163fc2d154a6ffb248de0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bfdf7a98fa42208b4c180a0d401732f50f7ab0831f6d3435436f2b521726147(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__508c5d93f06e3baf4e62e1f0bfd59eba7320578a221b08768f49236cdaf26797(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__430191a603b0092fd7a2181d1b9781a768287e53a7e96daf5e6457695b5da3cf(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80e69391cd5f377e2d81ffc3a2c077f0380396670b44c19e1792733d6234ff43(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b03ba7562bdbf9dce6985d4a121769121aaf7038e6976d21bef0f175970ad384(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f8c35883d1d3f494fb4bbee57075264f116c553e0d12a3645e39c226d349e01(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cefe7efb2412a7230b5b433d5465ed6479b50dd5659a73e17764b999cf451d4(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d2b72c5ccd4f6f7ed91798e558396bdda691dd773cd1451570179d2d755ae7a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9a5c13559f67327bcbcd80433a9f0f3b24000470174b9b424377bd3fff66bbb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acbb8b099e0d5706e71bdb284fe298cd41d51ecfeb914c76dfa57713794dee9f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3f598b61d858dc0d1e37dd0fb2018899aa2106fcf560e3e3aebe519a268f770(
    value: typing.Optional[typing.Union[CloudsearchDomainIndexField, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__913ba150c125038f45436eb50e289b8d3c06fae56d2c55cda22905378e628255(
    *,
    desired_instance_type: typing.Optional[builtins.str] = None,
    desired_partition_count: typing.Optional[jsii.Number] = None,
    desired_replication_count: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__592937a86858340dc3901931a6737176e426f2a89f931961d18e3eb45e8e448d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f2566a46b9eabf585b6126f15676a3d9a8c3540188a02d49d5a6d82eeafb6ec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a1c79a8621c02586567fc9c7502ebe2c09bd4bbb8b864c2fea23aa82b64edf7(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7060ccf1acbee047a991e266c05117bb36fece8a77964472b713548bcb0e61dd(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f81d7e422895f9b80763a74a1f26d87dc1be1f9ac3ebeace1c7b375da486fb2b(
    value: typing.Optional[CloudsearchDomainScalingParameters],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a590eb53f7851c45a25e9f22219d49bf8d7fe27a372f0eb598b7db7d08053aee(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd961c50edd8ce977569e0c690a263e98501c54c8d0a609de289f50973e5e934(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f747de08c5f6d5610fe59b988385ceaaae1e7a11a4e9823b43857b5a2998069(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__573d49c2f548ef415fe765888d64341a992b22f937aa433c0107afbdcbded129(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d9f9b8ce221c646267767681f30eab1c88d77eb4af9b63aa4318e0071b89188(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a957accb6479a01eda8f34e4e9d99f1677b7562b055fce543cae1ea7c215515(
    value: typing.Optional[typing.Union[CloudsearchDomainTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
