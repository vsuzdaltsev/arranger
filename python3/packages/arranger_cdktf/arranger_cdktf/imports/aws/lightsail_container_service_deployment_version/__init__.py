'''
# `aws_lightsail_container_service_deployment_version`

Refer to the Terraform Registory for docs: [`aws_lightsail_container_service_deployment_version`](https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version).
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


class LightsailContainerServiceDeploymentVersion(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lightsailContainerServiceDeploymentVersion.LightsailContainerServiceDeploymentVersion",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version aws_lightsail_container_service_deployment_version}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        container: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LightsailContainerServiceDeploymentVersionContainer", typing.Dict[builtins.str, typing.Any]]]],
        service_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        public_endpoint: typing.Optional[typing.Union["LightsailContainerServiceDeploymentVersionPublicEndpoint", typing.Dict[builtins.str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["LightsailContainerServiceDeploymentVersionTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version aws_lightsail_container_service_deployment_version} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param container: container block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#container LightsailContainerServiceDeploymentVersion#container}
        :param service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#service_name LightsailContainerServiceDeploymentVersion#service_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#id LightsailContainerServiceDeploymentVersion#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param public_endpoint: public_endpoint block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#public_endpoint LightsailContainerServiceDeploymentVersion#public_endpoint}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#timeouts LightsailContainerServiceDeploymentVersion#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6affd0ad8b74d77e1cc9203365fd3b81bf56dc8ba025c98b30801d5ddaf30268)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = LightsailContainerServiceDeploymentVersionConfig(
            container=container,
            service_name=service_name,
            id=id,
            public_endpoint=public_endpoint,
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

    @jsii.member(jsii_name="putContainer")
    def put_container(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LightsailContainerServiceDeploymentVersionContainer", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a832f1521bdf638c58dee84b92d9faef640b6f5bdae61446c8d9cfb27c667828)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putContainer", [value]))

    @jsii.member(jsii_name="putPublicEndpoint")
    def put_public_endpoint(
        self,
        *,
        container_name: builtins.str,
        container_port: jsii.Number,
        health_check: typing.Union["LightsailContainerServiceDeploymentVersionPublicEndpointHealthCheck", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#container_name LightsailContainerServiceDeploymentVersion#container_name}.
        :param container_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#container_port LightsailContainerServiceDeploymentVersion#container_port}.
        :param health_check: health_check block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#health_check LightsailContainerServiceDeploymentVersion#health_check}
        '''
        value = LightsailContainerServiceDeploymentVersionPublicEndpoint(
            container_name=container_name,
            container_port=container_port,
            health_check=health_check,
        )

        return typing.cast(None, jsii.invoke(self, "putPublicEndpoint", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(self, *, create: typing.Optional[builtins.str] = None) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#create LightsailContainerServiceDeploymentVersion#create}.
        '''
        value = LightsailContainerServiceDeploymentVersionTimeouts(create=create)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPublicEndpoint")
    def reset_public_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicEndpoint", []))

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
    @jsii.member(jsii_name="container")
    def container(self) -> "LightsailContainerServiceDeploymentVersionContainerList":
        return typing.cast("LightsailContainerServiceDeploymentVersionContainerList", jsii.get(self, "container"))

    @builtins.property
    @jsii.member(jsii_name="createdAt")
    def created_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdAt"))

    @builtins.property
    @jsii.member(jsii_name="publicEndpoint")
    def public_endpoint(
        self,
    ) -> "LightsailContainerServiceDeploymentVersionPublicEndpointOutputReference":
        return typing.cast("LightsailContainerServiceDeploymentVersionPublicEndpointOutputReference", jsii.get(self, "publicEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(
        self,
    ) -> "LightsailContainerServiceDeploymentVersionTimeoutsOutputReference":
        return typing.cast("LightsailContainerServiceDeploymentVersionTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "version"))

    @builtins.property
    @jsii.member(jsii_name="containerInput")
    def container_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LightsailContainerServiceDeploymentVersionContainer"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LightsailContainerServiceDeploymentVersionContainer"]]], jsii.get(self, "containerInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="publicEndpointInput")
    def public_endpoint_input(
        self,
    ) -> typing.Optional["LightsailContainerServiceDeploymentVersionPublicEndpoint"]:
        return typing.cast(typing.Optional["LightsailContainerServiceDeploymentVersionPublicEndpoint"], jsii.get(self, "publicEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceNameInput")
    def service_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["LightsailContainerServiceDeploymentVersionTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["LightsailContainerServiceDeploymentVersionTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2875ecaa9a5aa84f81da08763ae07a04a44ef40afefe6a0f86289ee6e9f52ec1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="serviceName")
    def service_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceName"))

    @service_name.setter
    def service_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc8d2c8c20129fd7fe8fa261cedeb0d8788fc4ade20ba12827d2c3ab1f3b8cec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceName", value)


@jsii.data_type(
    jsii_type="aws.lightsailContainerServiceDeploymentVersion.LightsailContainerServiceDeploymentVersionConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "container": "container",
        "service_name": "serviceName",
        "id": "id",
        "public_endpoint": "publicEndpoint",
        "timeouts": "timeouts",
    },
)
class LightsailContainerServiceDeploymentVersionConfig(
    _cdktf_9a9027ec.TerraformMetaArguments,
):
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
        container: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LightsailContainerServiceDeploymentVersionContainer", typing.Dict[builtins.str, typing.Any]]]],
        service_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        public_endpoint: typing.Optional[typing.Union["LightsailContainerServiceDeploymentVersionPublicEndpoint", typing.Dict[builtins.str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["LightsailContainerServiceDeploymentVersionTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param container: container block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#container LightsailContainerServiceDeploymentVersion#container}
        :param service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#service_name LightsailContainerServiceDeploymentVersion#service_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#id LightsailContainerServiceDeploymentVersion#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param public_endpoint: public_endpoint block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#public_endpoint LightsailContainerServiceDeploymentVersion#public_endpoint}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#timeouts LightsailContainerServiceDeploymentVersion#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(public_endpoint, dict):
            public_endpoint = LightsailContainerServiceDeploymentVersionPublicEndpoint(**public_endpoint)
        if isinstance(timeouts, dict):
            timeouts = LightsailContainerServiceDeploymentVersionTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__165518acbcf620d21fcf0059fb98794a5d607ddd0f435f95df6b70b3993b6c53)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument container", value=container, expected_type=type_hints["container"])
            check_type(argname="argument service_name", value=service_name, expected_type=type_hints["service_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument public_endpoint", value=public_endpoint, expected_type=type_hints["public_endpoint"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "container": container,
            "service_name": service_name,
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
        if id is not None:
            self._values["id"] = id
        if public_endpoint is not None:
            self._values["public_endpoint"] = public_endpoint
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
    def container(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LightsailContainerServiceDeploymentVersionContainer"]]:
        '''container block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#container LightsailContainerServiceDeploymentVersion#container}
        '''
        result = self._values.get("container")
        assert result is not None, "Required property 'container' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LightsailContainerServiceDeploymentVersionContainer"]], result)

    @builtins.property
    def service_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#service_name LightsailContainerServiceDeploymentVersion#service_name}.'''
        result = self._values.get("service_name")
        assert result is not None, "Required property 'service_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#id LightsailContainerServiceDeploymentVersion#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_endpoint(
        self,
    ) -> typing.Optional["LightsailContainerServiceDeploymentVersionPublicEndpoint"]:
        '''public_endpoint block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#public_endpoint LightsailContainerServiceDeploymentVersion#public_endpoint}
        '''
        result = self._values.get("public_endpoint")
        return typing.cast(typing.Optional["LightsailContainerServiceDeploymentVersionPublicEndpoint"], result)

    @builtins.property
    def timeouts(
        self,
    ) -> typing.Optional["LightsailContainerServiceDeploymentVersionTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#timeouts LightsailContainerServiceDeploymentVersion#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["LightsailContainerServiceDeploymentVersionTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LightsailContainerServiceDeploymentVersionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.lightsailContainerServiceDeploymentVersion.LightsailContainerServiceDeploymentVersionContainer",
    jsii_struct_bases=[],
    name_mapping={
        "container_name": "containerName",
        "image": "image",
        "command": "command",
        "environment": "environment",
        "ports": "ports",
    },
)
class LightsailContainerServiceDeploymentVersionContainer:
    def __init__(
        self,
        *,
        container_name: builtins.str,
        image: builtins.str,
        command: typing.Optional[typing.Sequence[builtins.str]] = None,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        ports: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#container_name LightsailContainerServiceDeploymentVersion#container_name}.
        :param image: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#image LightsailContainerServiceDeploymentVersion#image}.
        :param command: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#command LightsailContainerServiceDeploymentVersion#command}.
        :param environment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#environment LightsailContainerServiceDeploymentVersion#environment}.
        :param ports: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#ports LightsailContainerServiceDeploymentVersion#ports}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75f4ea876a2a058fb965151f058be167bfaebd0cf6e05361f5d2c460853ec255)
            check_type(argname="argument container_name", value=container_name, expected_type=type_hints["container_name"])
            check_type(argname="argument image", value=image, expected_type=type_hints["image"])
            check_type(argname="argument command", value=command, expected_type=type_hints["command"])
            check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
            check_type(argname="argument ports", value=ports, expected_type=type_hints["ports"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "container_name": container_name,
            "image": image,
        }
        if command is not None:
            self._values["command"] = command
        if environment is not None:
            self._values["environment"] = environment
        if ports is not None:
            self._values["ports"] = ports

    @builtins.property
    def container_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#container_name LightsailContainerServiceDeploymentVersion#container_name}.'''
        result = self._values.get("container_name")
        assert result is not None, "Required property 'container_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def image(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#image LightsailContainerServiceDeploymentVersion#image}.'''
        result = self._values.get("image")
        assert result is not None, "Required property 'image' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def command(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#command LightsailContainerServiceDeploymentVersion#command}.'''
        result = self._values.get("command")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def environment(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#environment LightsailContainerServiceDeploymentVersion#environment}.'''
        result = self._values.get("environment")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def ports(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#ports LightsailContainerServiceDeploymentVersion#ports}.'''
        result = self._values.get("ports")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LightsailContainerServiceDeploymentVersionContainer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LightsailContainerServiceDeploymentVersionContainerList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lightsailContainerServiceDeploymentVersion.LightsailContainerServiceDeploymentVersionContainerList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b83ebdf0236d4a5f8b460200d1221c8a0d44953789088b3d60814ebe237a5bc0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LightsailContainerServiceDeploymentVersionContainerOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f51bc6848292e94ac7aa9063f993e4a738a343530d118e732a251c6218b8b03)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LightsailContainerServiceDeploymentVersionContainerOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7445635b9b3f8713352a3a52fc7b1612d9300a140a889197a67308f932ef995)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a8c72170ecc437bed0e9cbb5d841f6c3a010e96930f67770f610d0b6be9eadac)
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
            type_hints = typing.get_type_hints(_typecheckingstub__05b3031719dccfc16be025182c5732061601d79d9af3382d48ea9ae5cf266ba3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LightsailContainerServiceDeploymentVersionContainer]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LightsailContainerServiceDeploymentVersionContainer]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LightsailContainerServiceDeploymentVersionContainer]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc3d75b761be22923b9863651e7cbe0b707158f31e5c638562bb9d00704adcff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LightsailContainerServiceDeploymentVersionContainerOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lightsailContainerServiceDeploymentVersion.LightsailContainerServiceDeploymentVersionContainerOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a72155aa84c865473943badba2f380c08a3898e97d55f9528545853bad73a514)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCommand")
    def reset_command(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCommand", []))

    @jsii.member(jsii_name="resetEnvironment")
    def reset_environment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnvironment", []))

    @jsii.member(jsii_name="resetPorts")
    def reset_ports(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPorts", []))

    @builtins.property
    @jsii.member(jsii_name="commandInput")
    def command_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "commandInput"))

    @builtins.property
    @jsii.member(jsii_name="containerNameInput")
    def container_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="environmentInput")
    def environment_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "environmentInput"))

    @builtins.property
    @jsii.member(jsii_name="imageInput")
    def image_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageInput"))

    @builtins.property
    @jsii.member(jsii_name="portsInput")
    def ports_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "portsInput"))

    @builtins.property
    @jsii.member(jsii_name="command")
    def command(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "command"))

    @command.setter
    def command(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fffeb0062546c04f3c13bd936d3185687e8523cbb1668c0b92cedbed48dcd7e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "command", value)

    @builtins.property
    @jsii.member(jsii_name="containerName")
    def container_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "containerName"))

    @container_name.setter
    def container_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d38c90d14de47d4aa7441e3e4720696d428114bd6e5e959d75e22dc842ff968e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerName", value)

    @builtins.property
    @jsii.member(jsii_name="environment")
    def environment(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "environment"))

    @environment.setter
    def environment(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__faf6d5f369495b1dffbd2f37aa093bd994ea1dceb8786446778198a9e3ce3c0f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environment", value)

    @builtins.property
    @jsii.member(jsii_name="image")
    def image(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "image"))

    @image.setter
    def image(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5f5e195bd708387128966593c010498085de873d1e39218359faa51f6046d39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "image", value)

    @builtins.property
    @jsii.member(jsii_name="ports")
    def ports(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "ports"))

    @ports.setter
    def ports(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e5bb7a3f22e2d2751b1fcb760b34c7e99ea0b56553b07f774495f79c72ba5e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ports", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LightsailContainerServiceDeploymentVersionContainer, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LightsailContainerServiceDeploymentVersionContainer, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LightsailContainerServiceDeploymentVersionContainer, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96903631cb0e3c334ebbc1963e7da2f5c53a487353b67a390823490a7f814727)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.lightsailContainerServiceDeploymentVersion.LightsailContainerServiceDeploymentVersionPublicEndpoint",
    jsii_struct_bases=[],
    name_mapping={
        "container_name": "containerName",
        "container_port": "containerPort",
        "health_check": "healthCheck",
    },
)
class LightsailContainerServiceDeploymentVersionPublicEndpoint:
    def __init__(
        self,
        *,
        container_name: builtins.str,
        container_port: jsii.Number,
        health_check: typing.Union["LightsailContainerServiceDeploymentVersionPublicEndpointHealthCheck", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#container_name LightsailContainerServiceDeploymentVersion#container_name}.
        :param container_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#container_port LightsailContainerServiceDeploymentVersion#container_port}.
        :param health_check: health_check block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#health_check LightsailContainerServiceDeploymentVersion#health_check}
        '''
        if isinstance(health_check, dict):
            health_check = LightsailContainerServiceDeploymentVersionPublicEndpointHealthCheck(**health_check)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5895d7ba2714dedadb3de33b8468fef5d2225235ae62b1f7c735aa8112176a87)
            check_type(argname="argument container_name", value=container_name, expected_type=type_hints["container_name"])
            check_type(argname="argument container_port", value=container_port, expected_type=type_hints["container_port"])
            check_type(argname="argument health_check", value=health_check, expected_type=type_hints["health_check"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "container_name": container_name,
            "container_port": container_port,
            "health_check": health_check,
        }

    @builtins.property
    def container_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#container_name LightsailContainerServiceDeploymentVersion#container_name}.'''
        result = self._values.get("container_name")
        assert result is not None, "Required property 'container_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def container_port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#container_port LightsailContainerServiceDeploymentVersion#container_port}.'''
        result = self._values.get("container_port")
        assert result is not None, "Required property 'container_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def health_check(
        self,
    ) -> "LightsailContainerServiceDeploymentVersionPublicEndpointHealthCheck":
        '''health_check block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#health_check LightsailContainerServiceDeploymentVersion#health_check}
        '''
        result = self._values.get("health_check")
        assert result is not None, "Required property 'health_check' is missing"
        return typing.cast("LightsailContainerServiceDeploymentVersionPublicEndpointHealthCheck", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LightsailContainerServiceDeploymentVersionPublicEndpoint(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.lightsailContainerServiceDeploymentVersion.LightsailContainerServiceDeploymentVersionPublicEndpointHealthCheck",
    jsii_struct_bases=[],
    name_mapping={
        "healthy_threshold": "healthyThreshold",
        "interval_seconds": "intervalSeconds",
        "path": "path",
        "success_codes": "successCodes",
        "timeout_seconds": "timeoutSeconds",
        "unhealthy_threshold": "unhealthyThreshold",
    },
)
class LightsailContainerServiceDeploymentVersionPublicEndpointHealthCheck:
    def __init__(
        self,
        *,
        healthy_threshold: typing.Optional[jsii.Number] = None,
        interval_seconds: typing.Optional[jsii.Number] = None,
        path: typing.Optional[builtins.str] = None,
        success_codes: typing.Optional[builtins.str] = None,
        timeout_seconds: typing.Optional[jsii.Number] = None,
        unhealthy_threshold: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param healthy_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#healthy_threshold LightsailContainerServiceDeploymentVersion#healthy_threshold}.
        :param interval_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#interval_seconds LightsailContainerServiceDeploymentVersion#interval_seconds}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#path LightsailContainerServiceDeploymentVersion#path}.
        :param success_codes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#success_codes LightsailContainerServiceDeploymentVersion#success_codes}.
        :param timeout_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#timeout_seconds LightsailContainerServiceDeploymentVersion#timeout_seconds}.
        :param unhealthy_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#unhealthy_threshold LightsailContainerServiceDeploymentVersion#unhealthy_threshold}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77d9271f091dc2dbca6f3d1f70ba3eacb38831998962d62eb4893b1bc2d5156b)
            check_type(argname="argument healthy_threshold", value=healthy_threshold, expected_type=type_hints["healthy_threshold"])
            check_type(argname="argument interval_seconds", value=interval_seconds, expected_type=type_hints["interval_seconds"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument success_codes", value=success_codes, expected_type=type_hints["success_codes"])
            check_type(argname="argument timeout_seconds", value=timeout_seconds, expected_type=type_hints["timeout_seconds"])
            check_type(argname="argument unhealthy_threshold", value=unhealthy_threshold, expected_type=type_hints["unhealthy_threshold"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if healthy_threshold is not None:
            self._values["healthy_threshold"] = healthy_threshold
        if interval_seconds is not None:
            self._values["interval_seconds"] = interval_seconds
        if path is not None:
            self._values["path"] = path
        if success_codes is not None:
            self._values["success_codes"] = success_codes
        if timeout_seconds is not None:
            self._values["timeout_seconds"] = timeout_seconds
        if unhealthy_threshold is not None:
            self._values["unhealthy_threshold"] = unhealthy_threshold

    @builtins.property
    def healthy_threshold(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#healthy_threshold LightsailContainerServiceDeploymentVersion#healthy_threshold}.'''
        result = self._values.get("healthy_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def interval_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#interval_seconds LightsailContainerServiceDeploymentVersion#interval_seconds}.'''
        result = self._values.get("interval_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#path LightsailContainerServiceDeploymentVersion#path}.'''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def success_codes(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#success_codes LightsailContainerServiceDeploymentVersion#success_codes}.'''
        result = self._values.get("success_codes")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeout_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#timeout_seconds LightsailContainerServiceDeploymentVersion#timeout_seconds}.'''
        result = self._values.get("timeout_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def unhealthy_threshold(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#unhealthy_threshold LightsailContainerServiceDeploymentVersion#unhealthy_threshold}.'''
        result = self._values.get("unhealthy_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LightsailContainerServiceDeploymentVersionPublicEndpointHealthCheck(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LightsailContainerServiceDeploymentVersionPublicEndpointHealthCheckOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lightsailContainerServiceDeploymentVersion.LightsailContainerServiceDeploymentVersionPublicEndpointHealthCheckOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a16583e01360a051b084317f8a29e7d0bbaa28e59c71ed4806e0866d75165dd3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetHealthyThreshold")
    def reset_healthy_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthyThreshold", []))

    @jsii.member(jsii_name="resetIntervalSeconds")
    def reset_interval_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIntervalSeconds", []))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetSuccessCodes")
    def reset_success_codes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSuccessCodes", []))

    @jsii.member(jsii_name="resetTimeoutSeconds")
    def reset_timeout_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeoutSeconds", []))

    @jsii.member(jsii_name="resetUnhealthyThreshold")
    def reset_unhealthy_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnhealthyThreshold", []))

    @builtins.property
    @jsii.member(jsii_name="healthyThresholdInput")
    def healthy_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "healthyThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalSecondsInput")
    def interval_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "intervalSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="successCodesInput")
    def success_codes_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "successCodesInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutSecondsInput")
    def timeout_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="unhealthyThresholdInput")
    def unhealthy_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "unhealthyThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="healthyThreshold")
    def healthy_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "healthyThreshold"))

    @healthy_threshold.setter
    def healthy_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35608882e849b408b8038d9eb402e7e40ea11bbfc7c777db65768822a6625cbd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthyThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="intervalSeconds")
    def interval_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "intervalSeconds"))

    @interval_seconds.setter
    def interval_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__176f98afdb0a9943b086e1c7d8640ce0fb91324f1684fcc9d7f5a2907b2041f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intervalSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69f798e3af0974d5625d0c888de92e9085ac8bfadc294dc990a714567828daea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="successCodes")
    def success_codes(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "successCodes"))

    @success_codes.setter
    def success_codes(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b9f08ba699de748b21f37b4b654056f2e430cf08823ea80c67e7b93c2f965e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "successCodes", value)

    @builtins.property
    @jsii.member(jsii_name="timeoutSeconds")
    def timeout_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeoutSeconds"))

    @timeout_seconds.setter
    def timeout_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3da4fc79b072be4fac5ce628f2318e6679e1c92e1b6cf514bc8fbc9799f3fb1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="unhealthyThreshold")
    def unhealthy_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "unhealthyThreshold"))

    @unhealthy_threshold.setter
    def unhealthy_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89e5be52892f8cdac3e7d53b6de9bd4bf7aa50d4a29e4906345fd8c145f4c6f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unhealthyThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LightsailContainerServiceDeploymentVersionPublicEndpointHealthCheck]:
        return typing.cast(typing.Optional[LightsailContainerServiceDeploymentVersionPublicEndpointHealthCheck], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LightsailContainerServiceDeploymentVersionPublicEndpointHealthCheck],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e73217888803ecbe8e658ed9a512238c72c99a52fe9580e9d1bb4b0c7fa18158)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LightsailContainerServiceDeploymentVersionPublicEndpointOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lightsailContainerServiceDeploymentVersion.LightsailContainerServiceDeploymentVersionPublicEndpointOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__414f4e110a2d76283d795a6102e871217eda46389478373a1a41c607bacffe58)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putHealthCheck")
    def put_health_check(
        self,
        *,
        healthy_threshold: typing.Optional[jsii.Number] = None,
        interval_seconds: typing.Optional[jsii.Number] = None,
        path: typing.Optional[builtins.str] = None,
        success_codes: typing.Optional[builtins.str] = None,
        timeout_seconds: typing.Optional[jsii.Number] = None,
        unhealthy_threshold: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param healthy_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#healthy_threshold LightsailContainerServiceDeploymentVersion#healthy_threshold}.
        :param interval_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#interval_seconds LightsailContainerServiceDeploymentVersion#interval_seconds}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#path LightsailContainerServiceDeploymentVersion#path}.
        :param success_codes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#success_codes LightsailContainerServiceDeploymentVersion#success_codes}.
        :param timeout_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#timeout_seconds LightsailContainerServiceDeploymentVersion#timeout_seconds}.
        :param unhealthy_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#unhealthy_threshold LightsailContainerServiceDeploymentVersion#unhealthy_threshold}.
        '''
        value = LightsailContainerServiceDeploymentVersionPublicEndpointHealthCheck(
            healthy_threshold=healthy_threshold,
            interval_seconds=interval_seconds,
            path=path,
            success_codes=success_codes,
            timeout_seconds=timeout_seconds,
            unhealthy_threshold=unhealthy_threshold,
        )

        return typing.cast(None, jsii.invoke(self, "putHealthCheck", [value]))

    @builtins.property
    @jsii.member(jsii_name="healthCheck")
    def health_check(
        self,
    ) -> LightsailContainerServiceDeploymentVersionPublicEndpointHealthCheckOutputReference:
        return typing.cast(LightsailContainerServiceDeploymentVersionPublicEndpointHealthCheckOutputReference, jsii.get(self, "healthCheck"))

    @builtins.property
    @jsii.member(jsii_name="containerNameInput")
    def container_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="containerPortInput")
    def container_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "containerPortInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckInput")
    def health_check_input(
        self,
    ) -> typing.Optional[LightsailContainerServiceDeploymentVersionPublicEndpointHealthCheck]:
        return typing.cast(typing.Optional[LightsailContainerServiceDeploymentVersionPublicEndpointHealthCheck], jsii.get(self, "healthCheckInput"))

    @builtins.property
    @jsii.member(jsii_name="containerName")
    def container_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "containerName"))

    @container_name.setter
    def container_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__106240b8f190e2bd0302488328a0d27e88c0a4722e439a7775068d0e131bd07b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerName", value)

    @builtins.property
    @jsii.member(jsii_name="containerPort")
    def container_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "containerPort"))

    @container_port.setter
    def container_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e01bfce6597cc5f4701ab6b35e442a059c514d9180d5393f410a1543723b245)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerPort", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LightsailContainerServiceDeploymentVersionPublicEndpoint]:
        return typing.cast(typing.Optional[LightsailContainerServiceDeploymentVersionPublicEndpoint], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LightsailContainerServiceDeploymentVersionPublicEndpoint],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69f184eb08f5be783fdcf1518ee6152cac092af6da9a213801c86d39c5462204)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.lightsailContainerServiceDeploymentVersion.LightsailContainerServiceDeploymentVersionTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create"},
)
class LightsailContainerServiceDeploymentVersionTimeouts:
    def __init__(self, *, create: typing.Optional[builtins.str] = None) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#create LightsailContainerServiceDeploymentVersion#create}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28e51b4e6b482bbd73a4ef4ff8b26d12c69b69d01ce070715d64bc2d776b6129)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lightsail_container_service_deployment_version#create LightsailContainerServiceDeploymentVersion#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LightsailContainerServiceDeploymentVersionTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LightsailContainerServiceDeploymentVersionTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lightsailContainerServiceDeploymentVersion.LightsailContainerServiceDeploymentVersionTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__966038a31cccdcc24f8fa93a6f41be470879b632ebac322150d664dcd8523edb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e830af92172fde6a59455efa309caabafc9b7c7483b9ca313de6ad93b8da5f97)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LightsailContainerServiceDeploymentVersionTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LightsailContainerServiceDeploymentVersionTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LightsailContainerServiceDeploymentVersionTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6bb90ba1af94fa26ec05c1122faac6cca82fe593fd4616415d12acd120995ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "LightsailContainerServiceDeploymentVersion",
    "LightsailContainerServiceDeploymentVersionConfig",
    "LightsailContainerServiceDeploymentVersionContainer",
    "LightsailContainerServiceDeploymentVersionContainerList",
    "LightsailContainerServiceDeploymentVersionContainerOutputReference",
    "LightsailContainerServiceDeploymentVersionPublicEndpoint",
    "LightsailContainerServiceDeploymentVersionPublicEndpointHealthCheck",
    "LightsailContainerServiceDeploymentVersionPublicEndpointHealthCheckOutputReference",
    "LightsailContainerServiceDeploymentVersionPublicEndpointOutputReference",
    "LightsailContainerServiceDeploymentVersionTimeouts",
    "LightsailContainerServiceDeploymentVersionTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__6affd0ad8b74d77e1cc9203365fd3b81bf56dc8ba025c98b30801d5ddaf30268(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    container: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LightsailContainerServiceDeploymentVersionContainer, typing.Dict[builtins.str, typing.Any]]]],
    service_name: builtins.str,
    id: typing.Optional[builtins.str] = None,
    public_endpoint: typing.Optional[typing.Union[LightsailContainerServiceDeploymentVersionPublicEndpoint, typing.Dict[builtins.str, typing.Any]]] = None,
    timeouts: typing.Optional[typing.Union[LightsailContainerServiceDeploymentVersionTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__a832f1521bdf638c58dee84b92d9faef640b6f5bdae61446c8d9cfb27c667828(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LightsailContainerServiceDeploymentVersionContainer, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2875ecaa9a5aa84f81da08763ae07a04a44ef40afefe6a0f86289ee6e9f52ec1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc8d2c8c20129fd7fe8fa261cedeb0d8788fc4ade20ba12827d2c3ab1f3b8cec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__165518acbcf620d21fcf0059fb98794a5d607ddd0f435f95df6b70b3993b6c53(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    container: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LightsailContainerServiceDeploymentVersionContainer, typing.Dict[builtins.str, typing.Any]]]],
    service_name: builtins.str,
    id: typing.Optional[builtins.str] = None,
    public_endpoint: typing.Optional[typing.Union[LightsailContainerServiceDeploymentVersionPublicEndpoint, typing.Dict[builtins.str, typing.Any]]] = None,
    timeouts: typing.Optional[typing.Union[LightsailContainerServiceDeploymentVersionTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75f4ea876a2a058fb965151f058be167bfaebd0cf6e05361f5d2c460853ec255(
    *,
    container_name: builtins.str,
    image: builtins.str,
    command: typing.Optional[typing.Sequence[builtins.str]] = None,
    environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ports: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b83ebdf0236d4a5f8b460200d1221c8a0d44953789088b3d60814ebe237a5bc0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f51bc6848292e94ac7aa9063f993e4a738a343530d118e732a251c6218b8b03(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7445635b9b3f8713352a3a52fc7b1612d9300a140a889197a67308f932ef995(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8c72170ecc437bed0e9cbb5d841f6c3a010e96930f67770f610d0b6be9eadac(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05b3031719dccfc16be025182c5732061601d79d9af3382d48ea9ae5cf266ba3(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc3d75b761be22923b9863651e7cbe0b707158f31e5c638562bb9d00704adcff(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LightsailContainerServiceDeploymentVersionContainer]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a72155aa84c865473943badba2f380c08a3898e97d55f9528545853bad73a514(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fffeb0062546c04f3c13bd936d3185687e8523cbb1668c0b92cedbed48dcd7e8(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d38c90d14de47d4aa7441e3e4720696d428114bd6e5e959d75e22dc842ff968e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__faf6d5f369495b1dffbd2f37aa093bd994ea1dceb8786446778198a9e3ce3c0f(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5f5e195bd708387128966593c010498085de873d1e39218359faa51f6046d39(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e5bb7a3f22e2d2751b1fcb760b34c7e99ea0b56553b07f774495f79c72ba5e9(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96903631cb0e3c334ebbc1963e7da2f5c53a487353b67a390823490a7f814727(
    value: typing.Optional[typing.Union[LightsailContainerServiceDeploymentVersionContainer, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5895d7ba2714dedadb3de33b8468fef5d2225235ae62b1f7c735aa8112176a87(
    *,
    container_name: builtins.str,
    container_port: jsii.Number,
    health_check: typing.Union[LightsailContainerServiceDeploymentVersionPublicEndpointHealthCheck, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77d9271f091dc2dbca6f3d1f70ba3eacb38831998962d62eb4893b1bc2d5156b(
    *,
    healthy_threshold: typing.Optional[jsii.Number] = None,
    interval_seconds: typing.Optional[jsii.Number] = None,
    path: typing.Optional[builtins.str] = None,
    success_codes: typing.Optional[builtins.str] = None,
    timeout_seconds: typing.Optional[jsii.Number] = None,
    unhealthy_threshold: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a16583e01360a051b084317f8a29e7d0bbaa28e59c71ed4806e0866d75165dd3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35608882e849b408b8038d9eb402e7e40ea11bbfc7c777db65768822a6625cbd(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__176f98afdb0a9943b086e1c7d8640ce0fb91324f1684fcc9d7f5a2907b2041f8(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69f798e3af0974d5625d0c888de92e9085ac8bfadc294dc990a714567828daea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b9f08ba699de748b21f37b4b654056f2e430cf08823ea80c67e7b93c2f965e1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3da4fc79b072be4fac5ce628f2318e6679e1c92e1b6cf514bc8fbc9799f3fb1(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89e5be52892f8cdac3e7d53b6de9bd4bf7aa50d4a29e4906345fd8c145f4c6f8(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e73217888803ecbe8e658ed9a512238c72c99a52fe9580e9d1bb4b0c7fa18158(
    value: typing.Optional[LightsailContainerServiceDeploymentVersionPublicEndpointHealthCheck],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__414f4e110a2d76283d795a6102e871217eda46389478373a1a41c607bacffe58(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__106240b8f190e2bd0302488328a0d27e88c0a4722e439a7775068d0e131bd07b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e01bfce6597cc5f4701ab6b35e442a059c514d9180d5393f410a1543723b245(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69f184eb08f5be783fdcf1518ee6152cac092af6da9a213801c86d39c5462204(
    value: typing.Optional[LightsailContainerServiceDeploymentVersionPublicEndpoint],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28e51b4e6b482bbd73a4ef4ff8b26d12c69b69d01ce070715d64bc2d776b6129(
    *,
    create: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__966038a31cccdcc24f8fa93a6f41be470879b632ebac322150d664dcd8523edb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e830af92172fde6a59455efa309caabafc9b7c7483b9ca313de6ad93b8da5f97(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6bb90ba1af94fa26ec05c1122faac6cca82fe593fd4616415d12acd120995ab(
    value: typing.Optional[typing.Union[LightsailContainerServiceDeploymentVersionTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
