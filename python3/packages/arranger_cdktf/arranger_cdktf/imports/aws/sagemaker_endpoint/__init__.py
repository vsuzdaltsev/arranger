'''
# `aws_sagemaker_endpoint`

Refer to the Terraform Registory for docs: [`aws_sagemaker_endpoint`](https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint).
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


class SagemakerEndpoint(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerEndpoint.SagemakerEndpoint",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint aws_sagemaker_endpoint}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        endpoint_config_name: builtins.str,
        deployment_config: typing.Optional[typing.Union["SagemakerEndpointDeploymentConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint aws_sagemaker_endpoint} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param endpoint_config_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#endpoint_config_name SagemakerEndpoint#endpoint_config_name}.
        :param deployment_config: deployment_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#deployment_config SagemakerEndpoint#deployment_config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#id SagemakerEndpoint#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#name SagemakerEndpoint#name}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#tags SagemakerEndpoint#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#tags_all SagemakerEndpoint#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd6628419492667dde38ec8545b3885de5563465c58a70be46754c0102c74dda)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SagemakerEndpointConfig(
            endpoint_config_name=endpoint_config_name,
            deployment_config=deployment_config,
            id=id,
            name=name,
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

    @jsii.member(jsii_name="putDeploymentConfig")
    def put_deployment_config(
        self,
        *,
        blue_green_update_policy: typing.Union["SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicy", typing.Dict[builtins.str, typing.Any]],
        auto_rollback_configuration: typing.Optional[typing.Union["SagemakerEndpointDeploymentConfigAutoRollbackConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param blue_green_update_policy: blue_green_update_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#blue_green_update_policy SagemakerEndpoint#blue_green_update_policy}
        :param auto_rollback_configuration: auto_rollback_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#auto_rollback_configuration SagemakerEndpoint#auto_rollback_configuration}
        '''
        value = SagemakerEndpointDeploymentConfig(
            blue_green_update_policy=blue_green_update_policy,
            auto_rollback_configuration=auto_rollback_configuration,
        )

        return typing.cast(None, jsii.invoke(self, "putDeploymentConfig", [value]))

    @jsii.member(jsii_name="resetDeploymentConfig")
    def reset_deployment_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeploymentConfig", []))

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
    @jsii.member(jsii_name="deploymentConfig")
    def deployment_config(self) -> "SagemakerEndpointDeploymentConfigOutputReference":
        return typing.cast("SagemakerEndpointDeploymentConfigOutputReference", jsii.get(self, "deploymentConfig"))

    @builtins.property
    @jsii.member(jsii_name="deploymentConfigInput")
    def deployment_config_input(
        self,
    ) -> typing.Optional["SagemakerEndpointDeploymentConfig"]:
        return typing.cast(typing.Optional["SagemakerEndpointDeploymentConfig"], jsii.get(self, "deploymentConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointConfigNameInput")
    def endpoint_config_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointConfigNameInput"))

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
    @jsii.member(jsii_name="endpointConfigName")
    def endpoint_config_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpointConfigName"))

    @endpoint_config_name.setter
    def endpoint_config_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f91d62e65a6dd733a7ca47190ea35c2786fc0143b3203929345d14b215348fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointConfigName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eef01d5c09c87acd1fe2c2641cb9c947d8da7899756a5e876c5c2518d06f1306)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1a1a7540c9bd51f45e5ef8e5863ba9baf194566f3cff32e5932f2bd31b5e74d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0363aec3906be90d9a599431493b86c45030236d65c3b5d8e7b2c4e33d0a335c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7de8b3b40a2db5c63da5ba10b965b97515a5bd22d87e8dc9a022b3aba170dd6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.sagemakerEndpoint.SagemakerEndpointConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "endpoint_config_name": "endpointConfigName",
        "deployment_config": "deploymentConfig",
        "id": "id",
        "name": "name",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class SagemakerEndpointConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        endpoint_config_name: builtins.str,
        deployment_config: typing.Optional[typing.Union["SagemakerEndpointDeploymentConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
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
        :param endpoint_config_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#endpoint_config_name SagemakerEndpoint#endpoint_config_name}.
        :param deployment_config: deployment_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#deployment_config SagemakerEndpoint#deployment_config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#id SagemakerEndpoint#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#name SagemakerEndpoint#name}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#tags SagemakerEndpoint#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#tags_all SagemakerEndpoint#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(deployment_config, dict):
            deployment_config = SagemakerEndpointDeploymentConfig(**deployment_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e2850bea85504f2a87027a710269a6536595683cd274b299da028b2f970f613)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument endpoint_config_name", value=endpoint_config_name, expected_type=type_hints["endpoint_config_name"])
            check_type(argname="argument deployment_config", value=deployment_config, expected_type=type_hints["deployment_config"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "endpoint_config_name": endpoint_config_name,
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
        if deployment_config is not None:
            self._values["deployment_config"] = deployment_config
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name
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
    def endpoint_config_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#endpoint_config_name SagemakerEndpoint#endpoint_config_name}.'''
        result = self._values.get("endpoint_config_name")
        assert result is not None, "Required property 'endpoint_config_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def deployment_config(self) -> typing.Optional["SagemakerEndpointDeploymentConfig"]:
        '''deployment_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#deployment_config SagemakerEndpoint#deployment_config}
        '''
        result = self._values.get("deployment_config")
        return typing.cast(typing.Optional["SagemakerEndpointDeploymentConfig"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#id SagemakerEndpoint#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#name SagemakerEndpoint#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#tags SagemakerEndpoint#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#tags_all SagemakerEndpoint#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerEndpointConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.sagemakerEndpoint.SagemakerEndpointDeploymentConfig",
    jsii_struct_bases=[],
    name_mapping={
        "blue_green_update_policy": "blueGreenUpdatePolicy",
        "auto_rollback_configuration": "autoRollbackConfiguration",
    },
)
class SagemakerEndpointDeploymentConfig:
    def __init__(
        self,
        *,
        blue_green_update_policy: typing.Union["SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicy", typing.Dict[builtins.str, typing.Any]],
        auto_rollback_configuration: typing.Optional[typing.Union["SagemakerEndpointDeploymentConfigAutoRollbackConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param blue_green_update_policy: blue_green_update_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#blue_green_update_policy SagemakerEndpoint#blue_green_update_policy}
        :param auto_rollback_configuration: auto_rollback_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#auto_rollback_configuration SagemakerEndpoint#auto_rollback_configuration}
        '''
        if isinstance(blue_green_update_policy, dict):
            blue_green_update_policy = SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicy(**blue_green_update_policy)
        if isinstance(auto_rollback_configuration, dict):
            auto_rollback_configuration = SagemakerEndpointDeploymentConfigAutoRollbackConfiguration(**auto_rollback_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46881bac6b1b22a23292a4469be96963040496b2b3296726971e58a2628048eb)
            check_type(argname="argument blue_green_update_policy", value=blue_green_update_policy, expected_type=type_hints["blue_green_update_policy"])
            check_type(argname="argument auto_rollback_configuration", value=auto_rollback_configuration, expected_type=type_hints["auto_rollback_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "blue_green_update_policy": blue_green_update_policy,
        }
        if auto_rollback_configuration is not None:
            self._values["auto_rollback_configuration"] = auto_rollback_configuration

    @builtins.property
    def blue_green_update_policy(
        self,
    ) -> "SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicy":
        '''blue_green_update_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#blue_green_update_policy SagemakerEndpoint#blue_green_update_policy}
        '''
        result = self._values.get("blue_green_update_policy")
        assert result is not None, "Required property 'blue_green_update_policy' is missing"
        return typing.cast("SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicy", result)

    @builtins.property
    def auto_rollback_configuration(
        self,
    ) -> typing.Optional["SagemakerEndpointDeploymentConfigAutoRollbackConfiguration"]:
        '''auto_rollback_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#auto_rollback_configuration SagemakerEndpoint#auto_rollback_configuration}
        '''
        result = self._values.get("auto_rollback_configuration")
        return typing.cast(typing.Optional["SagemakerEndpointDeploymentConfigAutoRollbackConfiguration"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerEndpointDeploymentConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.sagemakerEndpoint.SagemakerEndpointDeploymentConfigAutoRollbackConfiguration",
    jsii_struct_bases=[],
    name_mapping={"alarms": "alarms"},
)
class SagemakerEndpointDeploymentConfigAutoRollbackConfiguration:
    def __init__(
        self,
        *,
        alarms: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SagemakerEndpointDeploymentConfigAutoRollbackConfigurationAlarms", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param alarms: alarms block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#alarms SagemakerEndpoint#alarms}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f14ca4014254751591198d6a6a583538858edc56d5e27330b414b417257fc41e)
            check_type(argname="argument alarms", value=alarms, expected_type=type_hints["alarms"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if alarms is not None:
            self._values["alarms"] = alarms

    @builtins.property
    def alarms(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerEndpointDeploymentConfigAutoRollbackConfigurationAlarms"]]]:
        '''alarms block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#alarms SagemakerEndpoint#alarms}
        '''
        result = self._values.get("alarms")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerEndpointDeploymentConfigAutoRollbackConfigurationAlarms"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerEndpointDeploymentConfigAutoRollbackConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.sagemakerEndpoint.SagemakerEndpointDeploymentConfigAutoRollbackConfigurationAlarms",
    jsii_struct_bases=[],
    name_mapping={"alarm_name": "alarmName"},
)
class SagemakerEndpointDeploymentConfigAutoRollbackConfigurationAlarms:
    def __init__(self, *, alarm_name: builtins.str) -> None:
        '''
        :param alarm_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#alarm_name SagemakerEndpoint#alarm_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1fe33649ae1c0ce8ae60a5fdc8f8b5539715dd8a88e347eea62d11776bb826f)
            check_type(argname="argument alarm_name", value=alarm_name, expected_type=type_hints["alarm_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "alarm_name": alarm_name,
        }

    @builtins.property
    def alarm_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#alarm_name SagemakerEndpoint#alarm_name}.'''
        result = self._values.get("alarm_name")
        assert result is not None, "Required property 'alarm_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerEndpointDeploymentConfigAutoRollbackConfigurationAlarms(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerEndpointDeploymentConfigAutoRollbackConfigurationAlarmsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerEndpoint.SagemakerEndpointDeploymentConfigAutoRollbackConfigurationAlarmsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__46969441ca36d5aed4bc8a011679a3ac9dc05d82207b48aa370fd4e9ab4ed35b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SagemakerEndpointDeploymentConfigAutoRollbackConfigurationAlarmsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16ec371f977ab1c24de785a11520f26da66e0fe88f3c165a3954ddc2ca17810a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SagemakerEndpointDeploymentConfigAutoRollbackConfigurationAlarmsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55e85b6e277e20c9de312c45f8c2fdb2fc1794fea12afa4038675b8ace0fd9c6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6580411fbfaf969659860cdff560ce3276690912ce2dff7c1ccaffd78d24b06a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b487da5297ad1bcd6055cf05988966420ddf265bf0a7f3ab4714f0c0c316e310)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerEndpointDeploymentConfigAutoRollbackConfigurationAlarms]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerEndpointDeploymentConfigAutoRollbackConfigurationAlarms]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerEndpointDeploymentConfigAutoRollbackConfigurationAlarms]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca10a1619b01dbdd6df6464ff11497ad9e389900f95ba11176a381b552f92672)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SagemakerEndpointDeploymentConfigAutoRollbackConfigurationAlarmsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerEndpoint.SagemakerEndpointDeploymentConfigAutoRollbackConfigurationAlarmsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5f563a4ce642c1ce9fc5f3c463e8815e1192ea43fd71db5eb47fc34dd480e970)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="alarmNameInput")
    def alarm_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alarmNameInput"))

    @builtins.property
    @jsii.member(jsii_name="alarmName")
    def alarm_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "alarmName"))

    @alarm_name.setter
    def alarm_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7214d15b45dc408dfc542644235a16b72b65f269d293067b48e3e215d6b48ba5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alarmName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SagemakerEndpointDeploymentConfigAutoRollbackConfigurationAlarms, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SagemakerEndpointDeploymentConfigAutoRollbackConfigurationAlarms, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SagemakerEndpointDeploymentConfigAutoRollbackConfigurationAlarms, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f58151527dd212c7509fe7a881d22e772afe7057c6c9139c80415bb13df43f69)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SagemakerEndpointDeploymentConfigAutoRollbackConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerEndpoint.SagemakerEndpointDeploymentConfigAutoRollbackConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__76d3e0e209dd2c2cbbb0dd769daf644f50a1a3ec05cd667d525d1e4bf49b0d51)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAlarms")
    def put_alarms(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerEndpointDeploymentConfigAutoRollbackConfigurationAlarms, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__619b85507df26759cbcde0ed0ab35deb4a70fc055a7fb0e45c00186a4665c048)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAlarms", [value]))

    @jsii.member(jsii_name="resetAlarms")
    def reset_alarms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlarms", []))

    @builtins.property
    @jsii.member(jsii_name="alarms")
    def alarms(
        self,
    ) -> SagemakerEndpointDeploymentConfigAutoRollbackConfigurationAlarmsList:
        return typing.cast(SagemakerEndpointDeploymentConfigAutoRollbackConfigurationAlarmsList, jsii.get(self, "alarms"))

    @builtins.property
    @jsii.member(jsii_name="alarmsInput")
    def alarms_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerEndpointDeploymentConfigAutoRollbackConfigurationAlarms]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerEndpointDeploymentConfigAutoRollbackConfigurationAlarms]]], jsii.get(self, "alarmsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerEndpointDeploymentConfigAutoRollbackConfiguration]:
        return typing.cast(typing.Optional[SagemakerEndpointDeploymentConfigAutoRollbackConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerEndpointDeploymentConfigAutoRollbackConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03e47537a0d6cecc6e60f0072059145f12248543f9b79f619bab2f86bc8e4ffb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.sagemakerEndpoint.SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicy",
    jsii_struct_bases=[],
    name_mapping={
        "traffic_routing_configuration": "trafficRoutingConfiguration",
        "maximum_execution_timeout_in_seconds": "maximumExecutionTimeoutInSeconds",
        "termination_wait_in_seconds": "terminationWaitInSeconds",
    },
)
class SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicy:
    def __init__(
        self,
        *,
        traffic_routing_configuration: typing.Union["SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfiguration", typing.Dict[builtins.str, typing.Any]],
        maximum_execution_timeout_in_seconds: typing.Optional[jsii.Number] = None,
        termination_wait_in_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param traffic_routing_configuration: traffic_routing_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#traffic_routing_configuration SagemakerEndpoint#traffic_routing_configuration}
        :param maximum_execution_timeout_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#maximum_execution_timeout_in_seconds SagemakerEndpoint#maximum_execution_timeout_in_seconds}.
        :param termination_wait_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#termination_wait_in_seconds SagemakerEndpoint#termination_wait_in_seconds}.
        '''
        if isinstance(traffic_routing_configuration, dict):
            traffic_routing_configuration = SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfiguration(**traffic_routing_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67b10435c89738b328d27b8c25e76152cdeb5e5e3f1a2ebd906e5b672a0fbc33)
            check_type(argname="argument traffic_routing_configuration", value=traffic_routing_configuration, expected_type=type_hints["traffic_routing_configuration"])
            check_type(argname="argument maximum_execution_timeout_in_seconds", value=maximum_execution_timeout_in_seconds, expected_type=type_hints["maximum_execution_timeout_in_seconds"])
            check_type(argname="argument termination_wait_in_seconds", value=termination_wait_in_seconds, expected_type=type_hints["termination_wait_in_seconds"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "traffic_routing_configuration": traffic_routing_configuration,
        }
        if maximum_execution_timeout_in_seconds is not None:
            self._values["maximum_execution_timeout_in_seconds"] = maximum_execution_timeout_in_seconds
        if termination_wait_in_seconds is not None:
            self._values["termination_wait_in_seconds"] = termination_wait_in_seconds

    @builtins.property
    def traffic_routing_configuration(
        self,
    ) -> "SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfiguration":
        '''traffic_routing_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#traffic_routing_configuration SagemakerEndpoint#traffic_routing_configuration}
        '''
        result = self._values.get("traffic_routing_configuration")
        assert result is not None, "Required property 'traffic_routing_configuration' is missing"
        return typing.cast("SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfiguration", result)

    @builtins.property
    def maximum_execution_timeout_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#maximum_execution_timeout_in_seconds SagemakerEndpoint#maximum_execution_timeout_in_seconds}.'''
        result = self._values.get("maximum_execution_timeout_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def termination_wait_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#termination_wait_in_seconds SagemakerEndpoint#termination_wait_in_seconds}.'''
        result = self._values.get("termination_wait_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerEndpoint.SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8e526f34b7a5c872c60f7bb1b16f4fe697fbe439ddfadf7ee0bf09dda3137dfc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putTrafficRoutingConfiguration")
    def put_traffic_routing_configuration(
        self,
        *,
        type: builtins.str,
        wait_interval_in_seconds: jsii.Number,
        canary_size: typing.Optional[typing.Union["SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationCanarySize", typing.Dict[builtins.str, typing.Any]]] = None,
        linear_step_size: typing.Optional[typing.Union["SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationLinearStepSize", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#type SagemakerEndpoint#type}.
        :param wait_interval_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#wait_interval_in_seconds SagemakerEndpoint#wait_interval_in_seconds}.
        :param canary_size: canary_size block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#canary_size SagemakerEndpoint#canary_size}
        :param linear_step_size: linear_step_size block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#linear_step_size SagemakerEndpoint#linear_step_size}
        '''
        value = SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfiguration(
            type=type,
            wait_interval_in_seconds=wait_interval_in_seconds,
            canary_size=canary_size,
            linear_step_size=linear_step_size,
        )

        return typing.cast(None, jsii.invoke(self, "putTrafficRoutingConfiguration", [value]))

    @jsii.member(jsii_name="resetMaximumExecutionTimeoutInSeconds")
    def reset_maximum_execution_timeout_in_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaximumExecutionTimeoutInSeconds", []))

    @jsii.member(jsii_name="resetTerminationWaitInSeconds")
    def reset_termination_wait_in_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTerminationWaitInSeconds", []))

    @builtins.property
    @jsii.member(jsii_name="trafficRoutingConfiguration")
    def traffic_routing_configuration(
        self,
    ) -> "SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationOutputReference":
        return typing.cast("SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationOutputReference", jsii.get(self, "trafficRoutingConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="maximumExecutionTimeoutInSecondsInput")
    def maximum_execution_timeout_in_seconds_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maximumExecutionTimeoutInSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="terminationWaitInSecondsInput")
    def termination_wait_in_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "terminationWaitInSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="trafficRoutingConfigurationInput")
    def traffic_routing_configuration_input(
        self,
    ) -> typing.Optional["SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfiguration"]:
        return typing.cast(typing.Optional["SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfiguration"], jsii.get(self, "trafficRoutingConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumExecutionTimeoutInSeconds")
    def maximum_execution_timeout_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maximumExecutionTimeoutInSeconds"))

    @maximum_execution_timeout_in_seconds.setter
    def maximum_execution_timeout_in_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13e084ca4f3a97c24c79b405b7d5c99eb16fda63045a0f715d52b39d949554bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumExecutionTimeoutInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="terminationWaitInSeconds")
    def termination_wait_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "terminationWaitInSeconds"))

    @termination_wait_in_seconds.setter
    def termination_wait_in_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b213ce897dc06665588d9eb24023de33c78ebb50143e38e3f7d85f6d5272443)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terminationWaitInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicy]:
        return typing.cast(typing.Optional[SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf0f5ad209ea5da2e6c4b7b22cfc5185fd7b1b4799ca2f31d3e729b54d844e3e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.sagemakerEndpoint.SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "wait_interval_in_seconds": "waitIntervalInSeconds",
        "canary_size": "canarySize",
        "linear_step_size": "linearStepSize",
    },
)
class SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfiguration:
    def __init__(
        self,
        *,
        type: builtins.str,
        wait_interval_in_seconds: jsii.Number,
        canary_size: typing.Optional[typing.Union["SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationCanarySize", typing.Dict[builtins.str, typing.Any]]] = None,
        linear_step_size: typing.Optional[typing.Union["SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationLinearStepSize", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#type SagemakerEndpoint#type}.
        :param wait_interval_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#wait_interval_in_seconds SagemakerEndpoint#wait_interval_in_seconds}.
        :param canary_size: canary_size block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#canary_size SagemakerEndpoint#canary_size}
        :param linear_step_size: linear_step_size block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#linear_step_size SagemakerEndpoint#linear_step_size}
        '''
        if isinstance(canary_size, dict):
            canary_size = SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationCanarySize(**canary_size)
        if isinstance(linear_step_size, dict):
            linear_step_size = SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationLinearStepSize(**linear_step_size)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__081d17b9787d856bb777ef38741cc58077dabaa8b92338af914b7c21c2d4cf36)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument wait_interval_in_seconds", value=wait_interval_in_seconds, expected_type=type_hints["wait_interval_in_seconds"])
            check_type(argname="argument canary_size", value=canary_size, expected_type=type_hints["canary_size"])
            check_type(argname="argument linear_step_size", value=linear_step_size, expected_type=type_hints["linear_step_size"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
            "wait_interval_in_seconds": wait_interval_in_seconds,
        }
        if canary_size is not None:
            self._values["canary_size"] = canary_size
        if linear_step_size is not None:
            self._values["linear_step_size"] = linear_step_size

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#type SagemakerEndpoint#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def wait_interval_in_seconds(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#wait_interval_in_seconds SagemakerEndpoint#wait_interval_in_seconds}.'''
        result = self._values.get("wait_interval_in_seconds")
        assert result is not None, "Required property 'wait_interval_in_seconds' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def canary_size(
        self,
    ) -> typing.Optional["SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationCanarySize"]:
        '''canary_size block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#canary_size SagemakerEndpoint#canary_size}
        '''
        result = self._values.get("canary_size")
        return typing.cast(typing.Optional["SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationCanarySize"], result)

    @builtins.property
    def linear_step_size(
        self,
    ) -> typing.Optional["SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationLinearStepSize"]:
        '''linear_step_size block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#linear_step_size SagemakerEndpoint#linear_step_size}
        '''
        result = self._values.get("linear_step_size")
        return typing.cast(typing.Optional["SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationLinearStepSize"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.sagemakerEndpoint.SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationCanarySize",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "value": "value"},
)
class SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationCanarySize:
    def __init__(self, *, type: builtins.str, value: jsii.Number) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#type SagemakerEndpoint#type}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#value SagemakerEndpoint#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a5f5e584a53a979f0510217f0f8d1c8cc53091a04d10e28f9f6e59f7e9e5ead)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
            "value": value,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#type SagemakerEndpoint#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#value SagemakerEndpoint#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationCanarySize(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationCanarySizeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerEndpoint.SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationCanarySizeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7a1b3492517e0ec02976fbd06df79001835aae93a26e1b157301cea621476917)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d9551c242c8649f85669ec69f6f2da5eb165d133882c5ea502122f038eb74b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3724d7e2ee90c10233a7dac39f0f85c2aec7a0e44d6ed3ddc2d74c354ab24db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationCanarySize]:
        return typing.cast(typing.Optional[SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationCanarySize], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationCanarySize],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__559e72ff52398e7b15ae1efbc6efe4715f86674a9966252ba3a9805dc5e9f2ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.sagemakerEndpoint.SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationLinearStepSize",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "value": "value"},
)
class SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationLinearStepSize:
    def __init__(self, *, type: builtins.str, value: jsii.Number) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#type SagemakerEndpoint#type}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#value SagemakerEndpoint#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__756a9d03b2c29162dbcdc77220ce61bf172dc7237ee10c3b5fd55b70a86f61a6)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
            "value": value,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#type SagemakerEndpoint#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#value SagemakerEndpoint#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationLinearStepSize(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationLinearStepSizeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerEndpoint.SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationLinearStepSizeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__600a58461472dc36c3bbde4fefdd55348e267970891ccdb4cca241847aafd4a1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d79180e2c440f70e4dccbb3859e4a418bde6f9353462d66db5ddc09386435bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5e62c257e92ea5997c433402be828c1d701e530c463a0c175ee49bab24666a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationLinearStepSize]:
        return typing.cast(typing.Optional[SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationLinearStepSize], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationLinearStepSize],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89f7b0a722e78df64725f5f89653ce7453f95d18ad0bdeeb55da56012dad6397)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerEndpoint.SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f9ef3c68e9aa7df83a66e3a82b269f2cb975f9b1a7c863fa34044105a438c32c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCanarySize")
    def put_canary_size(self, *, type: builtins.str, value: jsii.Number) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#type SagemakerEndpoint#type}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#value SagemakerEndpoint#value}.
        '''
        value_ = SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationCanarySize(
            type=type, value=value
        )

        return typing.cast(None, jsii.invoke(self, "putCanarySize", [value_]))

    @jsii.member(jsii_name="putLinearStepSize")
    def put_linear_step_size(self, *, type: builtins.str, value: jsii.Number) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#type SagemakerEndpoint#type}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#value SagemakerEndpoint#value}.
        '''
        value_ = SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationLinearStepSize(
            type=type, value=value
        )

        return typing.cast(None, jsii.invoke(self, "putLinearStepSize", [value_]))

    @jsii.member(jsii_name="resetCanarySize")
    def reset_canary_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCanarySize", []))

    @jsii.member(jsii_name="resetLinearStepSize")
    def reset_linear_step_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLinearStepSize", []))

    @builtins.property
    @jsii.member(jsii_name="canarySize")
    def canary_size(
        self,
    ) -> SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationCanarySizeOutputReference:
        return typing.cast(SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationCanarySizeOutputReference, jsii.get(self, "canarySize"))

    @builtins.property
    @jsii.member(jsii_name="linearStepSize")
    def linear_step_size(
        self,
    ) -> SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationLinearStepSizeOutputReference:
        return typing.cast(SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationLinearStepSizeOutputReference, jsii.get(self, "linearStepSize"))

    @builtins.property
    @jsii.member(jsii_name="canarySizeInput")
    def canary_size_input(
        self,
    ) -> typing.Optional[SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationCanarySize]:
        return typing.cast(typing.Optional[SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationCanarySize], jsii.get(self, "canarySizeInput"))

    @builtins.property
    @jsii.member(jsii_name="linearStepSizeInput")
    def linear_step_size_input(
        self,
    ) -> typing.Optional[SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationLinearStepSize]:
        return typing.cast(typing.Optional[SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationLinearStepSize], jsii.get(self, "linearStepSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="waitIntervalInSecondsInput")
    def wait_interval_in_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "waitIntervalInSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63fb7fb1a6ec906d5a46f0e4efbc75cac3a51ac9c00c0c29ee35e01cee27a609)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="waitIntervalInSeconds")
    def wait_interval_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "waitIntervalInSeconds"))

    @wait_interval_in_seconds.setter
    def wait_interval_in_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5e7db906fc406d795998f7064e722430f7600b20df4e0cc67c9fdc4bab23b62)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitIntervalInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfiguration]:
        return typing.cast(typing.Optional[SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a0ba7e619ccf067554ad81cee32b2b9d8f12999ad59cfcf8103bc5d4d9cae90)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SagemakerEndpointDeploymentConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerEndpoint.SagemakerEndpointDeploymentConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9be5487ee38d2184ca0f31092d58d7a609ef2a40525c07e3d6269e6ce49f4434)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAutoRollbackConfiguration")
    def put_auto_rollback_configuration(
        self,
        *,
        alarms: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerEndpointDeploymentConfigAutoRollbackConfigurationAlarms, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param alarms: alarms block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#alarms SagemakerEndpoint#alarms}
        '''
        value = SagemakerEndpointDeploymentConfigAutoRollbackConfiguration(
            alarms=alarms
        )

        return typing.cast(None, jsii.invoke(self, "putAutoRollbackConfiguration", [value]))

    @jsii.member(jsii_name="putBlueGreenUpdatePolicy")
    def put_blue_green_update_policy(
        self,
        *,
        traffic_routing_configuration: typing.Union[SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfiguration, typing.Dict[builtins.str, typing.Any]],
        maximum_execution_timeout_in_seconds: typing.Optional[jsii.Number] = None,
        termination_wait_in_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param traffic_routing_configuration: traffic_routing_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#traffic_routing_configuration SagemakerEndpoint#traffic_routing_configuration}
        :param maximum_execution_timeout_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#maximum_execution_timeout_in_seconds SagemakerEndpoint#maximum_execution_timeout_in_seconds}.
        :param termination_wait_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint#termination_wait_in_seconds SagemakerEndpoint#termination_wait_in_seconds}.
        '''
        value = SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicy(
            traffic_routing_configuration=traffic_routing_configuration,
            maximum_execution_timeout_in_seconds=maximum_execution_timeout_in_seconds,
            termination_wait_in_seconds=termination_wait_in_seconds,
        )

        return typing.cast(None, jsii.invoke(self, "putBlueGreenUpdatePolicy", [value]))

    @jsii.member(jsii_name="resetAutoRollbackConfiguration")
    def reset_auto_rollback_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoRollbackConfiguration", []))

    @builtins.property
    @jsii.member(jsii_name="autoRollbackConfiguration")
    def auto_rollback_configuration(
        self,
    ) -> SagemakerEndpointDeploymentConfigAutoRollbackConfigurationOutputReference:
        return typing.cast(SagemakerEndpointDeploymentConfigAutoRollbackConfigurationOutputReference, jsii.get(self, "autoRollbackConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="blueGreenUpdatePolicy")
    def blue_green_update_policy(
        self,
    ) -> SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyOutputReference:
        return typing.cast(SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyOutputReference, jsii.get(self, "blueGreenUpdatePolicy"))

    @builtins.property
    @jsii.member(jsii_name="autoRollbackConfigurationInput")
    def auto_rollback_configuration_input(
        self,
    ) -> typing.Optional[SagemakerEndpointDeploymentConfigAutoRollbackConfiguration]:
        return typing.cast(typing.Optional[SagemakerEndpointDeploymentConfigAutoRollbackConfiguration], jsii.get(self, "autoRollbackConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="blueGreenUpdatePolicyInput")
    def blue_green_update_policy_input(
        self,
    ) -> typing.Optional[SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicy]:
        return typing.cast(typing.Optional[SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicy], jsii.get(self, "blueGreenUpdatePolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SagemakerEndpointDeploymentConfig]:
        return typing.cast(typing.Optional[SagemakerEndpointDeploymentConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerEndpointDeploymentConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7518a340af3f40a1e6f3ef16aedc043826bb668a4eaa8649ef9c62334464f6af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SagemakerEndpoint",
    "SagemakerEndpointConfig",
    "SagemakerEndpointDeploymentConfig",
    "SagemakerEndpointDeploymentConfigAutoRollbackConfiguration",
    "SagemakerEndpointDeploymentConfigAutoRollbackConfigurationAlarms",
    "SagemakerEndpointDeploymentConfigAutoRollbackConfigurationAlarmsList",
    "SagemakerEndpointDeploymentConfigAutoRollbackConfigurationAlarmsOutputReference",
    "SagemakerEndpointDeploymentConfigAutoRollbackConfigurationOutputReference",
    "SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicy",
    "SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyOutputReference",
    "SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfiguration",
    "SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationCanarySize",
    "SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationCanarySizeOutputReference",
    "SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationLinearStepSize",
    "SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationLinearStepSizeOutputReference",
    "SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationOutputReference",
    "SagemakerEndpointDeploymentConfigOutputReference",
]

publication.publish()

def _typecheckingstub__fd6628419492667dde38ec8545b3885de5563465c58a70be46754c0102c74dda(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    endpoint_config_name: builtins.str,
    deployment_config: typing.Optional[typing.Union[SagemakerEndpointDeploymentConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__4f91d62e65a6dd733a7ca47190ea35c2786fc0143b3203929345d14b215348fb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eef01d5c09c87acd1fe2c2641cb9c947d8da7899756a5e876c5c2518d06f1306(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1a1a7540c9bd51f45e5ef8e5863ba9baf194566f3cff32e5932f2bd31b5e74d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0363aec3906be90d9a599431493b86c45030236d65c3b5d8e7b2c4e33d0a335c(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7de8b3b40a2db5c63da5ba10b965b97515a5bd22d87e8dc9a022b3aba170dd6(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e2850bea85504f2a87027a710269a6536595683cd274b299da028b2f970f613(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    endpoint_config_name: builtins.str,
    deployment_config: typing.Optional[typing.Union[SagemakerEndpointDeploymentConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46881bac6b1b22a23292a4469be96963040496b2b3296726971e58a2628048eb(
    *,
    blue_green_update_policy: typing.Union[SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicy, typing.Dict[builtins.str, typing.Any]],
    auto_rollback_configuration: typing.Optional[typing.Union[SagemakerEndpointDeploymentConfigAutoRollbackConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f14ca4014254751591198d6a6a583538858edc56d5e27330b414b417257fc41e(
    *,
    alarms: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerEndpointDeploymentConfigAutoRollbackConfigurationAlarms, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1fe33649ae1c0ce8ae60a5fdc8f8b5539715dd8a88e347eea62d11776bb826f(
    *,
    alarm_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46969441ca36d5aed4bc8a011679a3ac9dc05d82207b48aa370fd4e9ab4ed35b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16ec371f977ab1c24de785a11520f26da66e0fe88f3c165a3954ddc2ca17810a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55e85b6e277e20c9de312c45f8c2fdb2fc1794fea12afa4038675b8ace0fd9c6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6580411fbfaf969659860cdff560ce3276690912ce2dff7c1ccaffd78d24b06a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b487da5297ad1bcd6055cf05988966420ddf265bf0a7f3ab4714f0c0c316e310(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca10a1619b01dbdd6df6464ff11497ad9e389900f95ba11176a381b552f92672(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerEndpointDeploymentConfigAutoRollbackConfigurationAlarms]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f563a4ce642c1ce9fc5f3c463e8815e1192ea43fd71db5eb47fc34dd480e970(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7214d15b45dc408dfc542644235a16b72b65f269d293067b48e3e215d6b48ba5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f58151527dd212c7509fe7a881d22e772afe7057c6c9139c80415bb13df43f69(
    value: typing.Optional[typing.Union[SagemakerEndpointDeploymentConfigAutoRollbackConfigurationAlarms, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76d3e0e209dd2c2cbbb0dd769daf644f50a1a3ec05cd667d525d1e4bf49b0d51(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__619b85507df26759cbcde0ed0ab35deb4a70fc055a7fb0e45c00186a4665c048(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerEndpointDeploymentConfigAutoRollbackConfigurationAlarms, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03e47537a0d6cecc6e60f0072059145f12248543f9b79f619bab2f86bc8e4ffb(
    value: typing.Optional[SagemakerEndpointDeploymentConfigAutoRollbackConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67b10435c89738b328d27b8c25e76152cdeb5e5e3f1a2ebd906e5b672a0fbc33(
    *,
    traffic_routing_configuration: typing.Union[SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfiguration, typing.Dict[builtins.str, typing.Any]],
    maximum_execution_timeout_in_seconds: typing.Optional[jsii.Number] = None,
    termination_wait_in_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e526f34b7a5c872c60f7bb1b16f4fe697fbe439ddfadf7ee0bf09dda3137dfc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13e084ca4f3a97c24c79b405b7d5c99eb16fda63045a0f715d52b39d949554bf(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b213ce897dc06665588d9eb24023de33c78ebb50143e38e3f7d85f6d5272443(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf0f5ad209ea5da2e6c4b7b22cfc5185fd7b1b4799ca2f31d3e729b54d844e3e(
    value: typing.Optional[SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicy],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__081d17b9787d856bb777ef38741cc58077dabaa8b92338af914b7c21c2d4cf36(
    *,
    type: builtins.str,
    wait_interval_in_seconds: jsii.Number,
    canary_size: typing.Optional[typing.Union[SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationCanarySize, typing.Dict[builtins.str, typing.Any]]] = None,
    linear_step_size: typing.Optional[typing.Union[SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationLinearStepSize, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a5f5e584a53a979f0510217f0f8d1c8cc53091a04d10e28f9f6e59f7e9e5ead(
    *,
    type: builtins.str,
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a1b3492517e0ec02976fbd06df79001835aae93a26e1b157301cea621476917(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d9551c242c8649f85669ec69f6f2da5eb165d133882c5ea502122f038eb74b0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3724d7e2ee90c10233a7dac39f0f85c2aec7a0e44d6ed3ddc2d74c354ab24db(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__559e72ff52398e7b15ae1efbc6efe4715f86674a9966252ba3a9805dc5e9f2ab(
    value: typing.Optional[SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationCanarySize],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__756a9d03b2c29162dbcdc77220ce61bf172dc7237ee10c3b5fd55b70a86f61a6(
    *,
    type: builtins.str,
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__600a58461472dc36c3bbde4fefdd55348e267970891ccdb4cca241847aafd4a1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d79180e2c440f70e4dccbb3859e4a418bde6f9353462d66db5ddc09386435bd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5e62c257e92ea5997c433402be828c1d701e530c463a0c175ee49bab24666a3(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89f7b0a722e78df64725f5f89653ce7453f95d18ad0bdeeb55da56012dad6397(
    value: typing.Optional[SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationLinearStepSize],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9ef3c68e9aa7df83a66e3a82b269f2cb975f9b1a7c863fa34044105a438c32c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63fb7fb1a6ec906d5a46f0e4efbc75cac3a51ac9c00c0c29ee35e01cee27a609(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5e7db906fc406d795998f7064e722430f7600b20df4e0cc67c9fdc4bab23b62(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a0ba7e619ccf067554ad81cee32b2b9d8f12999ad59cfcf8103bc5d4d9cae90(
    value: typing.Optional[SagemakerEndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9be5487ee38d2184ca0f31092d58d7a609ef2a40525c07e3d6269e6ce49f4434(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7518a340af3f40a1e6f3ef16aedc043826bb668a4eaa8649ef9c62334464f6af(
    value: typing.Optional[SagemakerEndpointDeploymentConfig],
) -> None:
    """Type checking stubs"""
    pass
