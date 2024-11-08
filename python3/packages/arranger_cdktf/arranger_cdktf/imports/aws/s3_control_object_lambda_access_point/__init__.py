'''
# `aws_s3control_object_lambda_access_point`

Refer to the Terraform Registory for docs: [`aws_s3control_object_lambda_access_point`](https://www.terraform.io/docs/providers/aws/r/s3control_object_lambda_access_point).
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


class S3ControlObjectLambdaAccessPoint(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3ControlObjectLambdaAccessPoint.S3ControlObjectLambdaAccessPoint",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/s3control_object_lambda_access_point aws_s3control_object_lambda_access_point}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        configuration: typing.Union["S3ControlObjectLambdaAccessPointConfiguration", typing.Dict[builtins.str, typing.Any]],
        name: builtins.str,
        account_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/s3control_object_lambda_access_point aws_s3control_object_lambda_access_point} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param configuration: configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_object_lambda_access_point#configuration S3ControlObjectLambdaAccessPoint#configuration}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_object_lambda_access_point#name S3ControlObjectLambdaAccessPoint#name}.
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_object_lambda_access_point#account_id S3ControlObjectLambdaAccessPoint#account_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_object_lambda_access_point#id S3ControlObjectLambdaAccessPoint#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21cf8e4f2d1f305f9582036bd7d472cab3b56722724933c9adf6bff859e22639)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = S3ControlObjectLambdaAccessPointConfig(
            configuration=configuration,
            name=name,
            account_id=account_id,
            id=id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putConfiguration")
    def put_configuration(
        self,
        *,
        supporting_access_point: builtins.str,
        transformation_configuration: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["S3ControlObjectLambdaAccessPointConfigurationTransformationConfiguration", typing.Dict[builtins.str, typing.Any]]]],
        allowed_features: typing.Optional[typing.Sequence[builtins.str]] = None,
        cloud_watch_metrics_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param supporting_access_point: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_object_lambda_access_point#supporting_access_point S3ControlObjectLambdaAccessPoint#supporting_access_point}.
        :param transformation_configuration: transformation_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_object_lambda_access_point#transformation_configuration S3ControlObjectLambdaAccessPoint#transformation_configuration}
        :param allowed_features: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_object_lambda_access_point#allowed_features S3ControlObjectLambdaAccessPoint#allowed_features}.
        :param cloud_watch_metrics_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_object_lambda_access_point#cloud_watch_metrics_enabled S3ControlObjectLambdaAccessPoint#cloud_watch_metrics_enabled}.
        '''
        value = S3ControlObjectLambdaAccessPointConfiguration(
            supporting_access_point=supporting_access_point,
            transformation_configuration=transformation_configuration,
            allowed_features=allowed_features,
            cloud_watch_metrics_enabled=cloud_watch_metrics_enabled,
        )

        return typing.cast(None, jsii.invoke(self, "putConfiguration", [value]))

    @jsii.member(jsii_name="resetAccountId")
    def reset_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountId", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

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
    @jsii.member(jsii_name="configuration")
    def configuration(
        self,
    ) -> "S3ControlObjectLambdaAccessPointConfigurationOutputReference":
        return typing.cast("S3ControlObjectLambdaAccessPointConfigurationOutputReference", jsii.get(self, "configuration"))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="configurationInput")
    def configuration_input(
        self,
    ) -> typing.Optional["S3ControlObjectLambdaAccessPointConfiguration"]:
        return typing.cast(typing.Optional["S3ControlObjectLambdaAccessPointConfiguration"], jsii.get(self, "configurationInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f01e15166de8861d2e5b2adc320ad08eb76c44101b414dfdf45c342bdc5c9c79)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad5e69930ef6ebc0fc182839c1edaee3701f44d4fbba41e5555b910c2fd8467d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd6434c54e3942d86d3ed40d9aa95e2632204579d1f38dd967d9d992a29ce98e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="aws.s3ControlObjectLambdaAccessPoint.S3ControlObjectLambdaAccessPointConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "configuration": "configuration",
        "name": "name",
        "account_id": "accountId",
        "id": "id",
    },
)
class S3ControlObjectLambdaAccessPointConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        configuration: typing.Union["S3ControlObjectLambdaAccessPointConfiguration", typing.Dict[builtins.str, typing.Any]],
        name: builtins.str,
        account_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param configuration: configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_object_lambda_access_point#configuration S3ControlObjectLambdaAccessPoint#configuration}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_object_lambda_access_point#name S3ControlObjectLambdaAccessPoint#name}.
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_object_lambda_access_point#account_id S3ControlObjectLambdaAccessPoint#account_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_object_lambda_access_point#id S3ControlObjectLambdaAccessPoint#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(configuration, dict):
            configuration = S3ControlObjectLambdaAccessPointConfiguration(**configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c831c8aed2d06d194ba175d881cb352e773be4991c695f7c812937e33989d498)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "configuration": configuration,
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
        if account_id is not None:
            self._values["account_id"] = account_id
        if id is not None:
            self._values["id"] = id

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
    def configuration(self) -> "S3ControlObjectLambdaAccessPointConfiguration":
        '''configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_object_lambda_access_point#configuration S3ControlObjectLambdaAccessPoint#configuration}
        '''
        result = self._values.get("configuration")
        assert result is not None, "Required property 'configuration' is missing"
        return typing.cast("S3ControlObjectLambdaAccessPointConfiguration", result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_object_lambda_access_point#name S3ControlObjectLambdaAccessPoint#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_object_lambda_access_point#account_id S3ControlObjectLambdaAccessPoint#account_id}.'''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_object_lambda_access_point#id S3ControlObjectLambdaAccessPoint#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlObjectLambdaAccessPointConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.s3ControlObjectLambdaAccessPoint.S3ControlObjectLambdaAccessPointConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "supporting_access_point": "supportingAccessPoint",
        "transformation_configuration": "transformationConfiguration",
        "allowed_features": "allowedFeatures",
        "cloud_watch_metrics_enabled": "cloudWatchMetricsEnabled",
    },
)
class S3ControlObjectLambdaAccessPointConfiguration:
    def __init__(
        self,
        *,
        supporting_access_point: builtins.str,
        transformation_configuration: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["S3ControlObjectLambdaAccessPointConfigurationTransformationConfiguration", typing.Dict[builtins.str, typing.Any]]]],
        allowed_features: typing.Optional[typing.Sequence[builtins.str]] = None,
        cloud_watch_metrics_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param supporting_access_point: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_object_lambda_access_point#supporting_access_point S3ControlObjectLambdaAccessPoint#supporting_access_point}.
        :param transformation_configuration: transformation_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_object_lambda_access_point#transformation_configuration S3ControlObjectLambdaAccessPoint#transformation_configuration}
        :param allowed_features: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_object_lambda_access_point#allowed_features S3ControlObjectLambdaAccessPoint#allowed_features}.
        :param cloud_watch_metrics_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_object_lambda_access_point#cloud_watch_metrics_enabled S3ControlObjectLambdaAccessPoint#cloud_watch_metrics_enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc94f9b77d66cb7d84d9f371a1f3d6423e2fbfd0699e1d73505b03d184596765)
            check_type(argname="argument supporting_access_point", value=supporting_access_point, expected_type=type_hints["supporting_access_point"])
            check_type(argname="argument transformation_configuration", value=transformation_configuration, expected_type=type_hints["transformation_configuration"])
            check_type(argname="argument allowed_features", value=allowed_features, expected_type=type_hints["allowed_features"])
            check_type(argname="argument cloud_watch_metrics_enabled", value=cloud_watch_metrics_enabled, expected_type=type_hints["cloud_watch_metrics_enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "supporting_access_point": supporting_access_point,
            "transformation_configuration": transformation_configuration,
        }
        if allowed_features is not None:
            self._values["allowed_features"] = allowed_features
        if cloud_watch_metrics_enabled is not None:
            self._values["cloud_watch_metrics_enabled"] = cloud_watch_metrics_enabled

    @builtins.property
    def supporting_access_point(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_object_lambda_access_point#supporting_access_point S3ControlObjectLambdaAccessPoint#supporting_access_point}.'''
        result = self._values.get("supporting_access_point")
        assert result is not None, "Required property 'supporting_access_point' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def transformation_configuration(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3ControlObjectLambdaAccessPointConfigurationTransformationConfiguration"]]:
        '''transformation_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_object_lambda_access_point#transformation_configuration S3ControlObjectLambdaAccessPoint#transformation_configuration}
        '''
        result = self._values.get("transformation_configuration")
        assert result is not None, "Required property 'transformation_configuration' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3ControlObjectLambdaAccessPointConfigurationTransformationConfiguration"]], result)

    @builtins.property
    def allowed_features(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_object_lambda_access_point#allowed_features S3ControlObjectLambdaAccessPoint#allowed_features}.'''
        result = self._values.get("allowed_features")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def cloud_watch_metrics_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_object_lambda_access_point#cloud_watch_metrics_enabled S3ControlObjectLambdaAccessPoint#cloud_watch_metrics_enabled}.'''
        result = self._values.get("cloud_watch_metrics_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlObjectLambdaAccessPointConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3ControlObjectLambdaAccessPointConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3ControlObjectLambdaAccessPoint.S3ControlObjectLambdaAccessPointConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3d07ede93c457b91488ac26d367c3db665bbc2cf9b84b8676cc6ebf0695dea75)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putTransformationConfiguration")
    def put_transformation_configuration(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["S3ControlObjectLambdaAccessPointConfigurationTransformationConfiguration", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__053accd987a0587be74f9a50ebfa3d8bcc9bf23f18566d5c8a26688a1822e592)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTransformationConfiguration", [value]))

    @jsii.member(jsii_name="resetAllowedFeatures")
    def reset_allowed_features(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedFeatures", []))

    @jsii.member(jsii_name="resetCloudWatchMetricsEnabled")
    def reset_cloud_watch_metrics_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudWatchMetricsEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="transformationConfiguration")
    def transformation_configuration(
        self,
    ) -> "S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationList":
        return typing.cast("S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationList", jsii.get(self, "transformationConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="allowedFeaturesInput")
    def allowed_features_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedFeaturesInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudWatchMetricsEnabledInput")
    def cloud_watch_metrics_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "cloudWatchMetricsEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="supportingAccessPointInput")
    def supporting_access_point_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "supportingAccessPointInput"))

    @builtins.property
    @jsii.member(jsii_name="transformationConfigurationInput")
    def transformation_configuration_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3ControlObjectLambdaAccessPointConfigurationTransformationConfiguration"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3ControlObjectLambdaAccessPointConfigurationTransformationConfiguration"]]], jsii.get(self, "transformationConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedFeatures")
    def allowed_features(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedFeatures"))

    @allowed_features.setter
    def allowed_features(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8baedb8922b9d831fb3d94d87c8ddc5886dc946a537e3e42ffc82cace13e5d40)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedFeatures", value)

    @builtins.property
    @jsii.member(jsii_name="cloudWatchMetricsEnabled")
    def cloud_watch_metrics_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "cloudWatchMetricsEnabled"))

    @cloud_watch_metrics_enabled.setter
    def cloud_watch_metrics_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8f30e36cb3e5602e76f109742511c62c444484916034d0aee7f460db99576e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudWatchMetricsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="supportingAccessPoint")
    def supporting_access_point(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "supportingAccessPoint"))

    @supporting_access_point.setter
    def supporting_access_point(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b55acd8ae6a7cb7da88d8a908a06415da221a799b65d40183fe95f4ef1aecf5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "supportingAccessPoint", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3ControlObjectLambdaAccessPointConfiguration]:
        return typing.cast(typing.Optional[S3ControlObjectLambdaAccessPointConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3ControlObjectLambdaAccessPointConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21cccbe1065ddeead8b3dfec73d8c6b7726662b5121d467a67caa95e5b3680e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3ControlObjectLambdaAccessPoint.S3ControlObjectLambdaAccessPointConfigurationTransformationConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "actions": "actions",
        "content_transformation": "contentTransformation",
    },
)
class S3ControlObjectLambdaAccessPointConfigurationTransformationConfiguration:
    def __init__(
        self,
        *,
        actions: typing.Sequence[builtins.str],
        content_transformation: typing.Union["S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformation", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param actions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_object_lambda_access_point#actions S3ControlObjectLambdaAccessPoint#actions}.
        :param content_transformation: content_transformation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_object_lambda_access_point#content_transformation S3ControlObjectLambdaAccessPoint#content_transformation}
        '''
        if isinstance(content_transformation, dict):
            content_transformation = S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformation(**content_transformation)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30e9053aeaf8703e0af064e31630329f76584a52f4694150a9878e882ec29045)
            check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
            check_type(argname="argument content_transformation", value=content_transformation, expected_type=type_hints["content_transformation"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "actions": actions,
            "content_transformation": content_transformation,
        }

    @builtins.property
    def actions(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_object_lambda_access_point#actions S3ControlObjectLambdaAccessPoint#actions}.'''
        result = self._values.get("actions")
        assert result is not None, "Required property 'actions' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def content_transformation(
        self,
    ) -> "S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformation":
        '''content_transformation block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_object_lambda_access_point#content_transformation S3ControlObjectLambdaAccessPoint#content_transformation}
        '''
        result = self._values.get("content_transformation")
        assert result is not None, "Required property 'content_transformation' is missing"
        return typing.cast("S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformation", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlObjectLambdaAccessPointConfigurationTransformationConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.s3ControlObjectLambdaAccessPoint.S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformation",
    jsii_struct_bases=[],
    name_mapping={"aws_lambda": "awsLambda"},
)
class S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformation:
    def __init__(
        self,
        *,
        aws_lambda: typing.Union["S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformationAwsLambda", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param aws_lambda: aws_lambda block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_object_lambda_access_point#aws_lambda S3ControlObjectLambdaAccessPoint#aws_lambda}
        '''
        if isinstance(aws_lambda, dict):
            aws_lambda = S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformationAwsLambda(**aws_lambda)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9941517147dbb3d98b067cc85ceeba391d68df1ffa96d154b9958e1f6cd3d49)
            check_type(argname="argument aws_lambda", value=aws_lambda, expected_type=type_hints["aws_lambda"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "aws_lambda": aws_lambda,
        }

    @builtins.property
    def aws_lambda(
        self,
    ) -> "S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformationAwsLambda":
        '''aws_lambda block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_object_lambda_access_point#aws_lambda S3ControlObjectLambdaAccessPoint#aws_lambda}
        '''
        result = self._values.get("aws_lambda")
        assert result is not None, "Required property 'aws_lambda' is missing"
        return typing.cast("S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformationAwsLambda", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.s3ControlObjectLambdaAccessPoint.S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformationAwsLambda",
    jsii_struct_bases=[],
    name_mapping={
        "function_arn": "functionArn",
        "function_payload": "functionPayload",
    },
)
class S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformationAwsLambda:
    def __init__(
        self,
        *,
        function_arn: builtins.str,
        function_payload: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param function_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_object_lambda_access_point#function_arn S3ControlObjectLambdaAccessPoint#function_arn}.
        :param function_payload: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_object_lambda_access_point#function_payload S3ControlObjectLambdaAccessPoint#function_payload}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a35e450756bcf1909cfcb68a185e6f6c4b58427bfcbc7a5613b9228b515f1f8)
            check_type(argname="argument function_arn", value=function_arn, expected_type=type_hints["function_arn"])
            check_type(argname="argument function_payload", value=function_payload, expected_type=type_hints["function_payload"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "function_arn": function_arn,
        }
        if function_payload is not None:
            self._values["function_payload"] = function_payload

    @builtins.property
    def function_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_object_lambda_access_point#function_arn S3ControlObjectLambdaAccessPoint#function_arn}.'''
        result = self._values.get("function_arn")
        assert result is not None, "Required property 'function_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def function_payload(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_object_lambda_access_point#function_payload S3ControlObjectLambdaAccessPoint#function_payload}.'''
        result = self._values.get("function_payload")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformationAwsLambda(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformationAwsLambdaOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3ControlObjectLambdaAccessPoint.S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformationAwsLambdaOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3381ae2f7bd919c9d4a97f2ebb46704663216e272fba54d49dcb61caaeb0b775)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFunctionPayload")
    def reset_function_payload(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFunctionPayload", []))

    @builtins.property
    @jsii.member(jsii_name="functionArnInput")
    def function_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "functionArnInput"))

    @builtins.property
    @jsii.member(jsii_name="functionPayloadInput")
    def function_payload_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "functionPayloadInput"))

    @builtins.property
    @jsii.member(jsii_name="functionArn")
    def function_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "functionArn"))

    @function_arn.setter
    def function_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1396988044e4849873793b939cb5103c14128fc129c31966f1b4d6bd7afb4fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "functionArn", value)

    @builtins.property
    @jsii.member(jsii_name="functionPayload")
    def function_payload(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "functionPayload"))

    @function_payload.setter
    def function_payload(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__064c89f7400347383e4d7d470d8e77e217632f03fc423335f5ed08127baa251c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "functionPayload", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformationAwsLambda]:
        return typing.cast(typing.Optional[S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformationAwsLambda], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformationAwsLambda],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dce339272913967f3b3c0e093e186656e316dd13a4a111aedcfe36a717e5f313)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3ControlObjectLambdaAccessPoint.S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d73ba7622bf6d94de10a670b0bb4d5aa9f1df0ef3c7df2685393f117f8a82e8b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAwsLambda")
    def put_aws_lambda(
        self,
        *,
        function_arn: builtins.str,
        function_payload: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param function_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_object_lambda_access_point#function_arn S3ControlObjectLambdaAccessPoint#function_arn}.
        :param function_payload: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_object_lambda_access_point#function_payload S3ControlObjectLambdaAccessPoint#function_payload}.
        '''
        value = S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformationAwsLambda(
            function_arn=function_arn, function_payload=function_payload
        )

        return typing.cast(None, jsii.invoke(self, "putAwsLambda", [value]))

    @builtins.property
    @jsii.member(jsii_name="awsLambda")
    def aws_lambda(
        self,
    ) -> S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformationAwsLambdaOutputReference:
        return typing.cast(S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformationAwsLambdaOutputReference, jsii.get(self, "awsLambda"))

    @builtins.property
    @jsii.member(jsii_name="awsLambdaInput")
    def aws_lambda_input(
        self,
    ) -> typing.Optional[S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformationAwsLambda]:
        return typing.cast(typing.Optional[S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformationAwsLambda], jsii.get(self, "awsLambdaInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformation]:
        return typing.cast(typing.Optional[S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformation],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c289f747e9a170a66e4deb336b307587fa10007ed0a00a9dc0223eecea163a5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3ControlObjectLambdaAccessPoint.S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__de1ff3e243c63fbc17f5c9820658285243407568485fc73b0ac13942d4dc668a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9803e43299f210c9294eac2194045677c3c1b950287f3e316644ad1b8c4dcf56)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec78a0b74ed5d7397f2f01e1bbf6d090f0875b89d8ba5613250b9edc8c03015a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__14ec9f05e3621dc51c8e6d93be423f8838fe98a23300cdca479d7d9ed79540c5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0ae658ead052997530ae400a5e54c23071c0d903fb68eba9423b2b9655bf1431)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3ControlObjectLambdaAccessPointConfigurationTransformationConfiguration]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3ControlObjectLambdaAccessPointConfigurationTransformationConfiguration]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3ControlObjectLambdaAccessPointConfigurationTransformationConfiguration]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3154ae9a91f49a86695786e2be151f258e1f16d6ae508c4c9e1e7020156bac00)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3ControlObjectLambdaAccessPoint.S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c532524520bfbb1abdd8a7d47623bc9605192dc31a02060438625c1e77531e05)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putContentTransformation")
    def put_content_transformation(
        self,
        *,
        aws_lambda: typing.Union[S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformationAwsLambda, typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param aws_lambda: aws_lambda block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_object_lambda_access_point#aws_lambda S3ControlObjectLambdaAccessPoint#aws_lambda}
        '''
        value = S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformation(
            aws_lambda=aws_lambda
        )

        return typing.cast(None, jsii.invoke(self, "putContentTransformation", [value]))

    @builtins.property
    @jsii.member(jsii_name="contentTransformation")
    def content_transformation(
        self,
    ) -> S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformationOutputReference:
        return typing.cast(S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformationOutputReference, jsii.get(self, "contentTransformation"))

    @builtins.property
    @jsii.member(jsii_name="actionsInput")
    def actions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "actionsInput"))

    @builtins.property
    @jsii.member(jsii_name="contentTransformationInput")
    def content_transformation_input(
        self,
    ) -> typing.Optional[S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformation]:
        return typing.cast(typing.Optional[S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformation], jsii.get(self, "contentTransformationInput"))

    @builtins.property
    @jsii.member(jsii_name="actions")
    def actions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "actions"))

    @actions.setter
    def actions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b546ee2b30dd2dc022c22c628d23d85d7b8d7d79d20e860392f39e20b6ffc596)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actions", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[S3ControlObjectLambdaAccessPointConfigurationTransformationConfiguration, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[S3ControlObjectLambdaAccessPointConfigurationTransformationConfiguration, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[S3ControlObjectLambdaAccessPointConfigurationTransformationConfiguration, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33042db3246ceef37d25bf88a66831e68048f3f230c576c9b7903806b7466141)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "S3ControlObjectLambdaAccessPoint",
    "S3ControlObjectLambdaAccessPointConfig",
    "S3ControlObjectLambdaAccessPointConfiguration",
    "S3ControlObjectLambdaAccessPointConfigurationOutputReference",
    "S3ControlObjectLambdaAccessPointConfigurationTransformationConfiguration",
    "S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformation",
    "S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformationAwsLambda",
    "S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformationAwsLambdaOutputReference",
    "S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformationOutputReference",
    "S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationList",
    "S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationOutputReference",
]

publication.publish()

def _typecheckingstub__21cf8e4f2d1f305f9582036bd7d472cab3b56722724933c9adf6bff859e22639(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    configuration: typing.Union[S3ControlObjectLambdaAccessPointConfiguration, typing.Dict[builtins.str, typing.Any]],
    name: builtins.str,
    account_id: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__f01e15166de8861d2e5b2adc320ad08eb76c44101b414dfdf45c342bdc5c9c79(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad5e69930ef6ebc0fc182839c1edaee3701f44d4fbba41e5555b910c2fd8467d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd6434c54e3942d86d3ed40d9aa95e2632204579d1f38dd967d9d992a29ce98e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c831c8aed2d06d194ba175d881cb352e773be4991c695f7c812937e33989d498(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    configuration: typing.Union[S3ControlObjectLambdaAccessPointConfiguration, typing.Dict[builtins.str, typing.Any]],
    name: builtins.str,
    account_id: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc94f9b77d66cb7d84d9f371a1f3d6423e2fbfd0699e1d73505b03d184596765(
    *,
    supporting_access_point: builtins.str,
    transformation_configuration: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[S3ControlObjectLambdaAccessPointConfigurationTransformationConfiguration, typing.Dict[builtins.str, typing.Any]]]],
    allowed_features: typing.Optional[typing.Sequence[builtins.str]] = None,
    cloud_watch_metrics_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d07ede93c457b91488ac26d367c3db665bbc2cf9b84b8676cc6ebf0695dea75(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__053accd987a0587be74f9a50ebfa3d8bcc9bf23f18566d5c8a26688a1822e592(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[S3ControlObjectLambdaAccessPointConfigurationTransformationConfiguration, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8baedb8922b9d831fb3d94d87c8ddc5886dc946a537e3e42ffc82cace13e5d40(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8f30e36cb3e5602e76f109742511c62c444484916034d0aee7f460db99576e1(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b55acd8ae6a7cb7da88d8a908a06415da221a799b65d40183fe95f4ef1aecf5d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21cccbe1065ddeead8b3dfec73d8c6b7726662b5121d467a67caa95e5b3680e4(
    value: typing.Optional[S3ControlObjectLambdaAccessPointConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30e9053aeaf8703e0af064e31630329f76584a52f4694150a9878e882ec29045(
    *,
    actions: typing.Sequence[builtins.str],
    content_transformation: typing.Union[S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformation, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9941517147dbb3d98b067cc85ceeba391d68df1ffa96d154b9958e1f6cd3d49(
    *,
    aws_lambda: typing.Union[S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformationAwsLambda, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a35e450756bcf1909cfcb68a185e6f6c4b58427bfcbc7a5613b9228b515f1f8(
    *,
    function_arn: builtins.str,
    function_payload: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3381ae2f7bd919c9d4a97f2ebb46704663216e272fba54d49dcb61caaeb0b775(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1396988044e4849873793b939cb5103c14128fc129c31966f1b4d6bd7afb4fe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__064c89f7400347383e4d7d470d8e77e217632f03fc423335f5ed08127baa251c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dce339272913967f3b3c0e093e186656e316dd13a4a111aedcfe36a717e5f313(
    value: typing.Optional[S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformationAwsLambda],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d73ba7622bf6d94de10a670b0bb4d5aa9f1df0ef3c7df2685393f117f8a82e8b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c289f747e9a170a66e4deb336b307587fa10007ed0a00a9dc0223eecea163a5e(
    value: typing.Optional[S3ControlObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformation],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de1ff3e243c63fbc17f5c9820658285243407568485fc73b0ac13942d4dc668a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9803e43299f210c9294eac2194045677c3c1b950287f3e316644ad1b8c4dcf56(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec78a0b74ed5d7397f2f01e1bbf6d090f0875b89d8ba5613250b9edc8c03015a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14ec9f05e3621dc51c8e6d93be423f8838fe98a23300cdca479d7d9ed79540c5(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ae658ead052997530ae400a5e54c23071c0d903fb68eba9423b2b9655bf1431(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3154ae9a91f49a86695786e2be151f258e1f16d6ae508c4c9e1e7020156bac00(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3ControlObjectLambdaAccessPointConfigurationTransformationConfiguration]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c532524520bfbb1abdd8a7d47623bc9605192dc31a02060438625c1e77531e05(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b546ee2b30dd2dc022c22c628d23d85d7b8d7d79d20e860392f39e20b6ffc596(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33042db3246ceef37d25bf88a66831e68048f3f230c576c9b7903806b7466141(
    value: typing.Optional[typing.Union[S3ControlObjectLambdaAccessPointConfigurationTransformationConfiguration, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
