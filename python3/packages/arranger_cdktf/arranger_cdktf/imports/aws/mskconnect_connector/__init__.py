'''
# `aws_mskconnect_connector`

Refer to the Terraform Registory for docs: [`aws_mskconnect_connector`](https://www.terraform.io/docs/providers/aws/r/mskconnect_connector).
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


class MskconnectConnector(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.mskconnectConnector.MskconnectConnector",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector aws_mskconnect_connector}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        capacity: typing.Union["MskconnectConnectorCapacity", typing.Dict[builtins.str, typing.Any]],
        connector_configuration: typing.Mapping[builtins.str, builtins.str],
        kafka_cluster: typing.Union["MskconnectConnectorKafkaCluster", typing.Dict[builtins.str, typing.Any]],
        kafka_cluster_client_authentication: typing.Union["MskconnectConnectorKafkaClusterClientAuthentication", typing.Dict[builtins.str, typing.Any]],
        kafka_cluster_encryption_in_transit: typing.Union["MskconnectConnectorKafkaClusterEncryptionInTransit", typing.Dict[builtins.str, typing.Any]],
        kafkaconnect_version: builtins.str,
        name: builtins.str,
        plugin: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["MskconnectConnectorPlugin", typing.Dict[builtins.str, typing.Any]]]],
        service_execution_role_arn: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        log_delivery: typing.Optional[typing.Union["MskconnectConnectorLogDelivery", typing.Dict[builtins.str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["MskconnectConnectorTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        worker_configuration: typing.Optional[typing.Union["MskconnectConnectorWorkerConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector aws_mskconnect_connector} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param capacity: capacity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#capacity MskconnectConnector#capacity}
        :param connector_configuration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#connector_configuration MskconnectConnector#connector_configuration}.
        :param kafka_cluster: kafka_cluster block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#kafka_cluster MskconnectConnector#kafka_cluster}
        :param kafka_cluster_client_authentication: kafka_cluster_client_authentication block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#kafka_cluster_client_authentication MskconnectConnector#kafka_cluster_client_authentication}
        :param kafka_cluster_encryption_in_transit: kafka_cluster_encryption_in_transit block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#kafka_cluster_encryption_in_transit MskconnectConnector#kafka_cluster_encryption_in_transit}
        :param kafkaconnect_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#kafkaconnect_version MskconnectConnector#kafkaconnect_version}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#name MskconnectConnector#name}.
        :param plugin: plugin block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#plugin MskconnectConnector#plugin}
        :param service_execution_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#service_execution_role_arn MskconnectConnector#service_execution_role_arn}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#description MskconnectConnector#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#id MskconnectConnector#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param log_delivery: log_delivery block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#log_delivery MskconnectConnector#log_delivery}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#timeouts MskconnectConnector#timeouts}
        :param worker_configuration: worker_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#worker_configuration MskconnectConnector#worker_configuration}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__731b2cc0a4fece4ad96ea3cd21295b285a457425f6b2a6cb03971682f7df4d57)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = MskconnectConnectorConfig(
            capacity=capacity,
            connector_configuration=connector_configuration,
            kafka_cluster=kafka_cluster,
            kafka_cluster_client_authentication=kafka_cluster_client_authentication,
            kafka_cluster_encryption_in_transit=kafka_cluster_encryption_in_transit,
            kafkaconnect_version=kafkaconnect_version,
            name=name,
            plugin=plugin,
            service_execution_role_arn=service_execution_role_arn,
            description=description,
            id=id,
            log_delivery=log_delivery,
            timeouts=timeouts,
            worker_configuration=worker_configuration,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCapacity")
    def put_capacity(
        self,
        *,
        autoscaling: typing.Optional[typing.Union["MskconnectConnectorCapacityAutoscaling", typing.Dict[builtins.str, typing.Any]]] = None,
        provisioned_capacity: typing.Optional[typing.Union["MskconnectConnectorCapacityProvisionedCapacity", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param autoscaling: autoscaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#autoscaling MskconnectConnector#autoscaling}
        :param provisioned_capacity: provisioned_capacity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#provisioned_capacity MskconnectConnector#provisioned_capacity}
        '''
        value = MskconnectConnectorCapacity(
            autoscaling=autoscaling, provisioned_capacity=provisioned_capacity
        )

        return typing.cast(None, jsii.invoke(self, "putCapacity", [value]))

    @jsii.member(jsii_name="putKafkaCluster")
    def put_kafka_cluster(
        self,
        *,
        apache_kafka_cluster: typing.Union["MskconnectConnectorKafkaClusterApacheKafkaCluster", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param apache_kafka_cluster: apache_kafka_cluster block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#apache_kafka_cluster MskconnectConnector#apache_kafka_cluster}
        '''
        value = MskconnectConnectorKafkaCluster(
            apache_kafka_cluster=apache_kafka_cluster
        )

        return typing.cast(None, jsii.invoke(self, "putKafkaCluster", [value]))

    @jsii.member(jsii_name="putKafkaClusterClientAuthentication")
    def put_kafka_cluster_client_authentication(
        self,
        *,
        authentication_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param authentication_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#authentication_type MskconnectConnector#authentication_type}.
        '''
        value = MskconnectConnectorKafkaClusterClientAuthentication(
            authentication_type=authentication_type
        )

        return typing.cast(None, jsii.invoke(self, "putKafkaClusterClientAuthentication", [value]))

    @jsii.member(jsii_name="putKafkaClusterEncryptionInTransit")
    def put_kafka_cluster_encryption_in_transit(
        self,
        *,
        encryption_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param encryption_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#encryption_type MskconnectConnector#encryption_type}.
        '''
        value = MskconnectConnectorKafkaClusterEncryptionInTransit(
            encryption_type=encryption_type
        )

        return typing.cast(None, jsii.invoke(self, "putKafkaClusterEncryptionInTransit", [value]))

    @jsii.member(jsii_name="putLogDelivery")
    def put_log_delivery(
        self,
        *,
        worker_log_delivery: typing.Union["MskconnectConnectorLogDeliveryWorkerLogDelivery", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param worker_log_delivery: worker_log_delivery block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#worker_log_delivery MskconnectConnector#worker_log_delivery}
        '''
        value = MskconnectConnectorLogDelivery(worker_log_delivery=worker_log_delivery)

        return typing.cast(None, jsii.invoke(self, "putLogDelivery", [value]))

    @jsii.member(jsii_name="putPlugin")
    def put_plugin(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["MskconnectConnectorPlugin", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d5b8e2b7283ed2100a70baec29e68a089626755120a0c3d8f4c48fdbd2c3233)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPlugin", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#create MskconnectConnector#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#delete MskconnectConnector#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#update MskconnectConnector#update}.
        '''
        value = MskconnectConnectorTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putWorkerConfiguration")
    def put_worker_configuration(
        self,
        *,
        arn: builtins.str,
        revision: jsii.Number,
    ) -> None:
        '''
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#arn MskconnectConnector#arn}.
        :param revision: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#revision MskconnectConnector#revision}.
        '''
        value = MskconnectConnectorWorkerConfiguration(arn=arn, revision=revision)

        return typing.cast(None, jsii.invoke(self, "putWorkerConfiguration", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLogDelivery")
    def reset_log_delivery(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogDelivery", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetWorkerConfiguration")
    def reset_worker_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkerConfiguration", []))

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
    @jsii.member(jsii_name="capacity")
    def capacity(self) -> "MskconnectConnectorCapacityOutputReference":
        return typing.cast("MskconnectConnectorCapacityOutputReference", jsii.get(self, "capacity"))

    @builtins.property
    @jsii.member(jsii_name="kafkaCluster")
    def kafka_cluster(self) -> "MskconnectConnectorKafkaClusterOutputReference":
        return typing.cast("MskconnectConnectorKafkaClusterOutputReference", jsii.get(self, "kafkaCluster"))

    @builtins.property
    @jsii.member(jsii_name="kafkaClusterClientAuthentication")
    def kafka_cluster_client_authentication(
        self,
    ) -> "MskconnectConnectorKafkaClusterClientAuthenticationOutputReference":
        return typing.cast("MskconnectConnectorKafkaClusterClientAuthenticationOutputReference", jsii.get(self, "kafkaClusterClientAuthentication"))

    @builtins.property
    @jsii.member(jsii_name="kafkaClusterEncryptionInTransit")
    def kafka_cluster_encryption_in_transit(
        self,
    ) -> "MskconnectConnectorKafkaClusterEncryptionInTransitOutputReference":
        return typing.cast("MskconnectConnectorKafkaClusterEncryptionInTransitOutputReference", jsii.get(self, "kafkaClusterEncryptionInTransit"))

    @builtins.property
    @jsii.member(jsii_name="logDelivery")
    def log_delivery(self) -> "MskconnectConnectorLogDeliveryOutputReference":
        return typing.cast("MskconnectConnectorLogDeliveryOutputReference", jsii.get(self, "logDelivery"))

    @builtins.property
    @jsii.member(jsii_name="plugin")
    def plugin(self) -> "MskconnectConnectorPluginList":
        return typing.cast("MskconnectConnectorPluginList", jsii.get(self, "plugin"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "MskconnectConnectorTimeoutsOutputReference":
        return typing.cast("MskconnectConnectorTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @builtins.property
    @jsii.member(jsii_name="workerConfiguration")
    def worker_configuration(
        self,
    ) -> "MskconnectConnectorWorkerConfigurationOutputReference":
        return typing.cast("MskconnectConnectorWorkerConfigurationOutputReference", jsii.get(self, "workerConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="capacityInput")
    def capacity_input(self) -> typing.Optional["MskconnectConnectorCapacity"]:
        return typing.cast(typing.Optional["MskconnectConnectorCapacity"], jsii.get(self, "capacityInput"))

    @builtins.property
    @jsii.member(jsii_name="connectorConfigurationInput")
    def connector_configuration_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "connectorConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="kafkaClusterClientAuthenticationInput")
    def kafka_cluster_client_authentication_input(
        self,
    ) -> typing.Optional["MskconnectConnectorKafkaClusterClientAuthentication"]:
        return typing.cast(typing.Optional["MskconnectConnectorKafkaClusterClientAuthentication"], jsii.get(self, "kafkaClusterClientAuthenticationInput"))

    @builtins.property
    @jsii.member(jsii_name="kafkaClusterEncryptionInTransitInput")
    def kafka_cluster_encryption_in_transit_input(
        self,
    ) -> typing.Optional["MskconnectConnectorKafkaClusterEncryptionInTransit"]:
        return typing.cast(typing.Optional["MskconnectConnectorKafkaClusterEncryptionInTransit"], jsii.get(self, "kafkaClusterEncryptionInTransitInput"))

    @builtins.property
    @jsii.member(jsii_name="kafkaClusterInput")
    def kafka_cluster_input(self) -> typing.Optional["MskconnectConnectorKafkaCluster"]:
        return typing.cast(typing.Optional["MskconnectConnectorKafkaCluster"], jsii.get(self, "kafkaClusterInput"))

    @builtins.property
    @jsii.member(jsii_name="kafkaconnectVersionInput")
    def kafkaconnect_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kafkaconnectVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="logDeliveryInput")
    def log_delivery_input(self) -> typing.Optional["MskconnectConnectorLogDelivery"]:
        return typing.cast(typing.Optional["MskconnectConnectorLogDelivery"], jsii.get(self, "logDeliveryInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="pluginInput")
    def plugin_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MskconnectConnectorPlugin"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MskconnectConnectorPlugin"]]], jsii.get(self, "pluginInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceExecutionRoleArnInput")
    def service_execution_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceExecutionRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["MskconnectConnectorTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["MskconnectConnectorTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="workerConfigurationInput")
    def worker_configuration_input(
        self,
    ) -> typing.Optional["MskconnectConnectorWorkerConfiguration"]:
        return typing.cast(typing.Optional["MskconnectConnectorWorkerConfiguration"], jsii.get(self, "workerConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="connectorConfiguration")
    def connector_configuration(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "connectorConfiguration"))

    @connector_configuration.setter
    def connector_configuration(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ed721e779fad824ffc9d755e143ecd734c1a134f826dcc325e15b6c20fedcc1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectorConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2de3b2e5496dfc94ff42b436da51d11a7ee90d90c0c82f46fedf9c3df10b4d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f4e73f8fe4d03bb528f6137b49d18e4f8c472179f1b60103001a1fc4ea817d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="kafkaconnectVersion")
    def kafkaconnect_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kafkaconnectVersion"))

    @kafkaconnect_version.setter
    def kafkaconnect_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e781af06a301f3f951499d72023f8252fff236e70b9febf536ce0f3a54c7def1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kafkaconnectVersion", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1e85fdc3a02bb00e552f36e825716887d49d35f4b758f85cb0fb9680228d85d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="serviceExecutionRoleArn")
    def service_execution_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceExecutionRoleArn"))

    @service_execution_role_arn.setter
    def service_execution_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60939422ea99eb01df56880c1d9f7a247270a69847818092b00409a51a326987)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceExecutionRoleArn", value)


@jsii.data_type(
    jsii_type="aws.mskconnectConnector.MskconnectConnectorCapacity",
    jsii_struct_bases=[],
    name_mapping={
        "autoscaling": "autoscaling",
        "provisioned_capacity": "provisionedCapacity",
    },
)
class MskconnectConnectorCapacity:
    def __init__(
        self,
        *,
        autoscaling: typing.Optional[typing.Union["MskconnectConnectorCapacityAutoscaling", typing.Dict[builtins.str, typing.Any]]] = None,
        provisioned_capacity: typing.Optional[typing.Union["MskconnectConnectorCapacityProvisionedCapacity", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param autoscaling: autoscaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#autoscaling MskconnectConnector#autoscaling}
        :param provisioned_capacity: provisioned_capacity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#provisioned_capacity MskconnectConnector#provisioned_capacity}
        '''
        if isinstance(autoscaling, dict):
            autoscaling = MskconnectConnectorCapacityAutoscaling(**autoscaling)
        if isinstance(provisioned_capacity, dict):
            provisioned_capacity = MskconnectConnectorCapacityProvisionedCapacity(**provisioned_capacity)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f86a17e83f2e45610ae80f94a4c8bf0df5c43bf17f3aa5ed9f19fb68fa8eeb51)
            check_type(argname="argument autoscaling", value=autoscaling, expected_type=type_hints["autoscaling"])
            check_type(argname="argument provisioned_capacity", value=provisioned_capacity, expected_type=type_hints["provisioned_capacity"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if autoscaling is not None:
            self._values["autoscaling"] = autoscaling
        if provisioned_capacity is not None:
            self._values["provisioned_capacity"] = provisioned_capacity

    @builtins.property
    def autoscaling(self) -> typing.Optional["MskconnectConnectorCapacityAutoscaling"]:
        '''autoscaling block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#autoscaling MskconnectConnector#autoscaling}
        '''
        result = self._values.get("autoscaling")
        return typing.cast(typing.Optional["MskconnectConnectorCapacityAutoscaling"], result)

    @builtins.property
    def provisioned_capacity(
        self,
    ) -> typing.Optional["MskconnectConnectorCapacityProvisionedCapacity"]:
        '''provisioned_capacity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#provisioned_capacity MskconnectConnector#provisioned_capacity}
        '''
        result = self._values.get("provisioned_capacity")
        return typing.cast(typing.Optional["MskconnectConnectorCapacityProvisionedCapacity"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskconnectConnectorCapacity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.mskconnectConnector.MskconnectConnectorCapacityAutoscaling",
    jsii_struct_bases=[],
    name_mapping={
        "max_worker_count": "maxWorkerCount",
        "min_worker_count": "minWorkerCount",
        "mcu_count": "mcuCount",
        "scale_in_policy": "scaleInPolicy",
        "scale_out_policy": "scaleOutPolicy",
    },
)
class MskconnectConnectorCapacityAutoscaling:
    def __init__(
        self,
        *,
        max_worker_count: jsii.Number,
        min_worker_count: jsii.Number,
        mcu_count: typing.Optional[jsii.Number] = None,
        scale_in_policy: typing.Optional[typing.Union["MskconnectConnectorCapacityAutoscalingScaleInPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        scale_out_policy: typing.Optional[typing.Union["MskconnectConnectorCapacityAutoscalingScaleOutPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param max_worker_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#max_worker_count MskconnectConnector#max_worker_count}.
        :param min_worker_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#min_worker_count MskconnectConnector#min_worker_count}.
        :param mcu_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#mcu_count MskconnectConnector#mcu_count}.
        :param scale_in_policy: scale_in_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#scale_in_policy MskconnectConnector#scale_in_policy}
        :param scale_out_policy: scale_out_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#scale_out_policy MskconnectConnector#scale_out_policy}
        '''
        if isinstance(scale_in_policy, dict):
            scale_in_policy = MskconnectConnectorCapacityAutoscalingScaleInPolicy(**scale_in_policy)
        if isinstance(scale_out_policy, dict):
            scale_out_policy = MskconnectConnectorCapacityAutoscalingScaleOutPolicy(**scale_out_policy)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e0a65a950591e8000c6b62e4530990c0dc5f4be3cd5a36a998a9b506d1d5ff5)
            check_type(argname="argument max_worker_count", value=max_worker_count, expected_type=type_hints["max_worker_count"])
            check_type(argname="argument min_worker_count", value=min_worker_count, expected_type=type_hints["min_worker_count"])
            check_type(argname="argument mcu_count", value=mcu_count, expected_type=type_hints["mcu_count"])
            check_type(argname="argument scale_in_policy", value=scale_in_policy, expected_type=type_hints["scale_in_policy"])
            check_type(argname="argument scale_out_policy", value=scale_out_policy, expected_type=type_hints["scale_out_policy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "max_worker_count": max_worker_count,
            "min_worker_count": min_worker_count,
        }
        if mcu_count is not None:
            self._values["mcu_count"] = mcu_count
        if scale_in_policy is not None:
            self._values["scale_in_policy"] = scale_in_policy
        if scale_out_policy is not None:
            self._values["scale_out_policy"] = scale_out_policy

    @builtins.property
    def max_worker_count(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#max_worker_count MskconnectConnector#max_worker_count}.'''
        result = self._values.get("max_worker_count")
        assert result is not None, "Required property 'max_worker_count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def min_worker_count(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#min_worker_count MskconnectConnector#min_worker_count}.'''
        result = self._values.get("min_worker_count")
        assert result is not None, "Required property 'min_worker_count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def mcu_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#mcu_count MskconnectConnector#mcu_count}.'''
        result = self._values.get("mcu_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def scale_in_policy(
        self,
    ) -> typing.Optional["MskconnectConnectorCapacityAutoscalingScaleInPolicy"]:
        '''scale_in_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#scale_in_policy MskconnectConnector#scale_in_policy}
        '''
        result = self._values.get("scale_in_policy")
        return typing.cast(typing.Optional["MskconnectConnectorCapacityAutoscalingScaleInPolicy"], result)

    @builtins.property
    def scale_out_policy(
        self,
    ) -> typing.Optional["MskconnectConnectorCapacityAutoscalingScaleOutPolicy"]:
        '''scale_out_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#scale_out_policy MskconnectConnector#scale_out_policy}
        '''
        result = self._values.get("scale_out_policy")
        return typing.cast(typing.Optional["MskconnectConnectorCapacityAutoscalingScaleOutPolicy"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskconnectConnectorCapacityAutoscaling(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MskconnectConnectorCapacityAutoscalingOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.mskconnectConnector.MskconnectConnectorCapacityAutoscalingOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4ee69c1d114b95496bd3b33c2d87288ec25cf3ab681178ee1d38ba652fe1e953)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putScaleInPolicy")
    def put_scale_in_policy(
        self,
        *,
        cpu_utilization_percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param cpu_utilization_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#cpu_utilization_percentage MskconnectConnector#cpu_utilization_percentage}.
        '''
        value = MskconnectConnectorCapacityAutoscalingScaleInPolicy(
            cpu_utilization_percentage=cpu_utilization_percentage
        )

        return typing.cast(None, jsii.invoke(self, "putScaleInPolicy", [value]))

    @jsii.member(jsii_name="putScaleOutPolicy")
    def put_scale_out_policy(
        self,
        *,
        cpu_utilization_percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param cpu_utilization_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#cpu_utilization_percentage MskconnectConnector#cpu_utilization_percentage}.
        '''
        value = MskconnectConnectorCapacityAutoscalingScaleOutPolicy(
            cpu_utilization_percentage=cpu_utilization_percentage
        )

        return typing.cast(None, jsii.invoke(self, "putScaleOutPolicy", [value]))

    @jsii.member(jsii_name="resetMcuCount")
    def reset_mcu_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMcuCount", []))

    @jsii.member(jsii_name="resetScaleInPolicy")
    def reset_scale_in_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScaleInPolicy", []))

    @jsii.member(jsii_name="resetScaleOutPolicy")
    def reset_scale_out_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScaleOutPolicy", []))

    @builtins.property
    @jsii.member(jsii_name="scaleInPolicy")
    def scale_in_policy(
        self,
    ) -> "MskconnectConnectorCapacityAutoscalingScaleInPolicyOutputReference":
        return typing.cast("MskconnectConnectorCapacityAutoscalingScaleInPolicyOutputReference", jsii.get(self, "scaleInPolicy"))

    @builtins.property
    @jsii.member(jsii_name="scaleOutPolicy")
    def scale_out_policy(
        self,
    ) -> "MskconnectConnectorCapacityAutoscalingScaleOutPolicyOutputReference":
        return typing.cast("MskconnectConnectorCapacityAutoscalingScaleOutPolicyOutputReference", jsii.get(self, "scaleOutPolicy"))

    @builtins.property
    @jsii.member(jsii_name="maxWorkerCountInput")
    def max_worker_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxWorkerCountInput"))

    @builtins.property
    @jsii.member(jsii_name="mcuCountInput")
    def mcu_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "mcuCountInput"))

    @builtins.property
    @jsii.member(jsii_name="minWorkerCountInput")
    def min_worker_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minWorkerCountInput"))

    @builtins.property
    @jsii.member(jsii_name="scaleInPolicyInput")
    def scale_in_policy_input(
        self,
    ) -> typing.Optional["MskconnectConnectorCapacityAutoscalingScaleInPolicy"]:
        return typing.cast(typing.Optional["MskconnectConnectorCapacityAutoscalingScaleInPolicy"], jsii.get(self, "scaleInPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="scaleOutPolicyInput")
    def scale_out_policy_input(
        self,
    ) -> typing.Optional["MskconnectConnectorCapacityAutoscalingScaleOutPolicy"]:
        return typing.cast(typing.Optional["MskconnectConnectorCapacityAutoscalingScaleOutPolicy"], jsii.get(self, "scaleOutPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="maxWorkerCount")
    def max_worker_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxWorkerCount"))

    @max_worker_count.setter
    def max_worker_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eff8e5a4da1caba5f6a99c4041a7236f127c13b9496b606280be4b77264cca6a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxWorkerCount", value)

    @builtins.property
    @jsii.member(jsii_name="mcuCount")
    def mcu_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "mcuCount"))

    @mcu_count.setter
    def mcu_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1343336d40988b626d1cc7a30c3bd1c36d65735d0217adc36c90c6d18517ae4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mcuCount", value)

    @builtins.property
    @jsii.member(jsii_name="minWorkerCount")
    def min_worker_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minWorkerCount"))

    @min_worker_count.setter
    def min_worker_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22ebc7bf15e8ac726ddace39f724ce144cc43ecec099c65f15c281720fea2de3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minWorkerCount", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MskconnectConnectorCapacityAutoscaling]:
        return typing.cast(typing.Optional[MskconnectConnectorCapacityAutoscaling], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskconnectConnectorCapacityAutoscaling],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f66d1b196e314c7cba2ff9be44441b67d8a519715eec9de9b115a2517bab2ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.mskconnectConnector.MskconnectConnectorCapacityAutoscalingScaleInPolicy",
    jsii_struct_bases=[],
    name_mapping={"cpu_utilization_percentage": "cpuUtilizationPercentage"},
)
class MskconnectConnectorCapacityAutoscalingScaleInPolicy:
    def __init__(
        self,
        *,
        cpu_utilization_percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param cpu_utilization_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#cpu_utilization_percentage MskconnectConnector#cpu_utilization_percentage}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4160f8c8fd2afaefcd3710ef1229ff249e7b05f9448f872c6367f55dfc79013)
            check_type(argname="argument cpu_utilization_percentage", value=cpu_utilization_percentage, expected_type=type_hints["cpu_utilization_percentage"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cpu_utilization_percentage is not None:
            self._values["cpu_utilization_percentage"] = cpu_utilization_percentage

    @builtins.property
    def cpu_utilization_percentage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#cpu_utilization_percentage MskconnectConnector#cpu_utilization_percentage}.'''
        result = self._values.get("cpu_utilization_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskconnectConnectorCapacityAutoscalingScaleInPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MskconnectConnectorCapacityAutoscalingScaleInPolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.mskconnectConnector.MskconnectConnectorCapacityAutoscalingScaleInPolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__21f3973036144c28991ae05aaa54e76f3ac65943ae1c7273b7ffaccf89ed35da)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCpuUtilizationPercentage")
    def reset_cpu_utilization_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpuUtilizationPercentage", []))

    @builtins.property
    @jsii.member(jsii_name="cpuUtilizationPercentageInput")
    def cpu_utilization_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cpuUtilizationPercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="cpuUtilizationPercentage")
    def cpu_utilization_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cpuUtilizationPercentage"))

    @cpu_utilization_percentage.setter
    def cpu_utilization_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fac08c0fe9f8cf8e61f2711337b5405f60fd5b2f086d2a1a84a4078f45449e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuUtilizationPercentage", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MskconnectConnectorCapacityAutoscalingScaleInPolicy]:
        return typing.cast(typing.Optional[MskconnectConnectorCapacityAutoscalingScaleInPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskconnectConnectorCapacityAutoscalingScaleInPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2440974937788b93b6be24c9228b2813f55340ee49f6db2c0f49fcadae90f310)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.mskconnectConnector.MskconnectConnectorCapacityAutoscalingScaleOutPolicy",
    jsii_struct_bases=[],
    name_mapping={"cpu_utilization_percentage": "cpuUtilizationPercentage"},
)
class MskconnectConnectorCapacityAutoscalingScaleOutPolicy:
    def __init__(
        self,
        *,
        cpu_utilization_percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param cpu_utilization_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#cpu_utilization_percentage MskconnectConnector#cpu_utilization_percentage}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f9510eb743eaabfd750beef734ab348b393aeb404e205494a17d8ff1204980a)
            check_type(argname="argument cpu_utilization_percentage", value=cpu_utilization_percentage, expected_type=type_hints["cpu_utilization_percentage"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cpu_utilization_percentage is not None:
            self._values["cpu_utilization_percentage"] = cpu_utilization_percentage

    @builtins.property
    def cpu_utilization_percentage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#cpu_utilization_percentage MskconnectConnector#cpu_utilization_percentage}.'''
        result = self._values.get("cpu_utilization_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskconnectConnectorCapacityAutoscalingScaleOutPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MskconnectConnectorCapacityAutoscalingScaleOutPolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.mskconnectConnector.MskconnectConnectorCapacityAutoscalingScaleOutPolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0786b9f33284fb40414a081a56396d13cfc966291ff563ed3f5e20fc53287fed)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCpuUtilizationPercentage")
    def reset_cpu_utilization_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpuUtilizationPercentage", []))

    @builtins.property
    @jsii.member(jsii_name="cpuUtilizationPercentageInput")
    def cpu_utilization_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cpuUtilizationPercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="cpuUtilizationPercentage")
    def cpu_utilization_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cpuUtilizationPercentage"))

    @cpu_utilization_percentage.setter
    def cpu_utilization_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a03164d36fcdb1990a299afef26d655b6542f34513e78e4b356d5da9bffc090f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuUtilizationPercentage", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MskconnectConnectorCapacityAutoscalingScaleOutPolicy]:
        return typing.cast(typing.Optional[MskconnectConnectorCapacityAutoscalingScaleOutPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskconnectConnectorCapacityAutoscalingScaleOutPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a189b897fed288e1354ca6849dc7223f9e688d09f90a462525ecf47d324863f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MskconnectConnectorCapacityOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.mskconnectConnector.MskconnectConnectorCapacityOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fda5b717ee3426ff1ab0bf5f6f007b2f84f973dbd863282d9d83e91e359fcf9b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAutoscaling")
    def put_autoscaling(
        self,
        *,
        max_worker_count: jsii.Number,
        min_worker_count: jsii.Number,
        mcu_count: typing.Optional[jsii.Number] = None,
        scale_in_policy: typing.Optional[typing.Union[MskconnectConnectorCapacityAutoscalingScaleInPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
        scale_out_policy: typing.Optional[typing.Union[MskconnectConnectorCapacityAutoscalingScaleOutPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param max_worker_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#max_worker_count MskconnectConnector#max_worker_count}.
        :param min_worker_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#min_worker_count MskconnectConnector#min_worker_count}.
        :param mcu_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#mcu_count MskconnectConnector#mcu_count}.
        :param scale_in_policy: scale_in_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#scale_in_policy MskconnectConnector#scale_in_policy}
        :param scale_out_policy: scale_out_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#scale_out_policy MskconnectConnector#scale_out_policy}
        '''
        value = MskconnectConnectorCapacityAutoscaling(
            max_worker_count=max_worker_count,
            min_worker_count=min_worker_count,
            mcu_count=mcu_count,
            scale_in_policy=scale_in_policy,
            scale_out_policy=scale_out_policy,
        )

        return typing.cast(None, jsii.invoke(self, "putAutoscaling", [value]))

    @jsii.member(jsii_name="putProvisionedCapacity")
    def put_provisioned_capacity(
        self,
        *,
        worker_count: jsii.Number,
        mcu_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param worker_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#worker_count MskconnectConnector#worker_count}.
        :param mcu_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#mcu_count MskconnectConnector#mcu_count}.
        '''
        value = MskconnectConnectorCapacityProvisionedCapacity(
            worker_count=worker_count, mcu_count=mcu_count
        )

        return typing.cast(None, jsii.invoke(self, "putProvisionedCapacity", [value]))

    @jsii.member(jsii_name="resetAutoscaling")
    def reset_autoscaling(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoscaling", []))

    @jsii.member(jsii_name="resetProvisionedCapacity")
    def reset_provisioned_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProvisionedCapacity", []))

    @builtins.property
    @jsii.member(jsii_name="autoscaling")
    def autoscaling(self) -> MskconnectConnectorCapacityAutoscalingOutputReference:
        return typing.cast(MskconnectConnectorCapacityAutoscalingOutputReference, jsii.get(self, "autoscaling"))

    @builtins.property
    @jsii.member(jsii_name="provisionedCapacity")
    def provisioned_capacity(
        self,
    ) -> "MskconnectConnectorCapacityProvisionedCapacityOutputReference":
        return typing.cast("MskconnectConnectorCapacityProvisionedCapacityOutputReference", jsii.get(self, "provisionedCapacity"))

    @builtins.property
    @jsii.member(jsii_name="autoscalingInput")
    def autoscaling_input(
        self,
    ) -> typing.Optional[MskconnectConnectorCapacityAutoscaling]:
        return typing.cast(typing.Optional[MskconnectConnectorCapacityAutoscaling], jsii.get(self, "autoscalingInput"))

    @builtins.property
    @jsii.member(jsii_name="provisionedCapacityInput")
    def provisioned_capacity_input(
        self,
    ) -> typing.Optional["MskconnectConnectorCapacityProvisionedCapacity"]:
        return typing.cast(typing.Optional["MskconnectConnectorCapacityProvisionedCapacity"], jsii.get(self, "provisionedCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MskconnectConnectorCapacity]:
        return typing.cast(typing.Optional[MskconnectConnectorCapacity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskconnectConnectorCapacity],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb23d293cbf14f8f413b272f6a99b033ddafa962a965c6a0c27d440f5dae5409)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.mskconnectConnector.MskconnectConnectorCapacityProvisionedCapacity",
    jsii_struct_bases=[],
    name_mapping={"worker_count": "workerCount", "mcu_count": "mcuCount"},
)
class MskconnectConnectorCapacityProvisionedCapacity:
    def __init__(
        self,
        *,
        worker_count: jsii.Number,
        mcu_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param worker_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#worker_count MskconnectConnector#worker_count}.
        :param mcu_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#mcu_count MskconnectConnector#mcu_count}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ba01fe8ef644460872cbf28a8b37d245d535e64c551eda76be98bb541b38f15)
            check_type(argname="argument worker_count", value=worker_count, expected_type=type_hints["worker_count"])
            check_type(argname="argument mcu_count", value=mcu_count, expected_type=type_hints["mcu_count"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "worker_count": worker_count,
        }
        if mcu_count is not None:
            self._values["mcu_count"] = mcu_count

    @builtins.property
    def worker_count(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#worker_count MskconnectConnector#worker_count}.'''
        result = self._values.get("worker_count")
        assert result is not None, "Required property 'worker_count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def mcu_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#mcu_count MskconnectConnector#mcu_count}.'''
        result = self._values.get("mcu_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskconnectConnectorCapacityProvisionedCapacity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MskconnectConnectorCapacityProvisionedCapacityOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.mskconnectConnector.MskconnectConnectorCapacityProvisionedCapacityOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__69521a51fd27cbc4e4803030c4fcaa5b3d8f5a684ddaffaad5d8dab596fd47bc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMcuCount")
    def reset_mcu_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMcuCount", []))

    @builtins.property
    @jsii.member(jsii_name="mcuCountInput")
    def mcu_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "mcuCountInput"))

    @builtins.property
    @jsii.member(jsii_name="workerCountInput")
    def worker_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "workerCountInput"))

    @builtins.property
    @jsii.member(jsii_name="mcuCount")
    def mcu_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "mcuCount"))

    @mcu_count.setter
    def mcu_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0bbe9859186f4ca7393a0a1283f1ce03ba987b01a547a110e1612517e2af2ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mcuCount", value)

    @builtins.property
    @jsii.member(jsii_name="workerCount")
    def worker_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "workerCount"))

    @worker_count.setter
    def worker_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5f1a86dc8b4670ec3f0297edc54e4a782768aa5403964a9e0197426e65c3e8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workerCount", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MskconnectConnectorCapacityProvisionedCapacity]:
        return typing.cast(typing.Optional[MskconnectConnectorCapacityProvisionedCapacity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskconnectConnectorCapacityProvisionedCapacity],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccc105bafab54dff8094403acfbae8dd377722e4c1ca969726baaf616855054e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.mskconnectConnector.MskconnectConnectorConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "capacity": "capacity",
        "connector_configuration": "connectorConfiguration",
        "kafka_cluster": "kafkaCluster",
        "kafka_cluster_client_authentication": "kafkaClusterClientAuthentication",
        "kafka_cluster_encryption_in_transit": "kafkaClusterEncryptionInTransit",
        "kafkaconnect_version": "kafkaconnectVersion",
        "name": "name",
        "plugin": "plugin",
        "service_execution_role_arn": "serviceExecutionRoleArn",
        "description": "description",
        "id": "id",
        "log_delivery": "logDelivery",
        "timeouts": "timeouts",
        "worker_configuration": "workerConfiguration",
    },
)
class MskconnectConnectorConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        capacity: typing.Union[MskconnectConnectorCapacity, typing.Dict[builtins.str, typing.Any]],
        connector_configuration: typing.Mapping[builtins.str, builtins.str],
        kafka_cluster: typing.Union["MskconnectConnectorKafkaCluster", typing.Dict[builtins.str, typing.Any]],
        kafka_cluster_client_authentication: typing.Union["MskconnectConnectorKafkaClusterClientAuthentication", typing.Dict[builtins.str, typing.Any]],
        kafka_cluster_encryption_in_transit: typing.Union["MskconnectConnectorKafkaClusterEncryptionInTransit", typing.Dict[builtins.str, typing.Any]],
        kafkaconnect_version: builtins.str,
        name: builtins.str,
        plugin: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["MskconnectConnectorPlugin", typing.Dict[builtins.str, typing.Any]]]],
        service_execution_role_arn: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        log_delivery: typing.Optional[typing.Union["MskconnectConnectorLogDelivery", typing.Dict[builtins.str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["MskconnectConnectorTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        worker_configuration: typing.Optional[typing.Union["MskconnectConnectorWorkerConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param capacity: capacity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#capacity MskconnectConnector#capacity}
        :param connector_configuration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#connector_configuration MskconnectConnector#connector_configuration}.
        :param kafka_cluster: kafka_cluster block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#kafka_cluster MskconnectConnector#kafka_cluster}
        :param kafka_cluster_client_authentication: kafka_cluster_client_authentication block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#kafka_cluster_client_authentication MskconnectConnector#kafka_cluster_client_authentication}
        :param kafka_cluster_encryption_in_transit: kafka_cluster_encryption_in_transit block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#kafka_cluster_encryption_in_transit MskconnectConnector#kafka_cluster_encryption_in_transit}
        :param kafkaconnect_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#kafkaconnect_version MskconnectConnector#kafkaconnect_version}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#name MskconnectConnector#name}.
        :param plugin: plugin block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#plugin MskconnectConnector#plugin}
        :param service_execution_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#service_execution_role_arn MskconnectConnector#service_execution_role_arn}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#description MskconnectConnector#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#id MskconnectConnector#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param log_delivery: log_delivery block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#log_delivery MskconnectConnector#log_delivery}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#timeouts MskconnectConnector#timeouts}
        :param worker_configuration: worker_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#worker_configuration MskconnectConnector#worker_configuration}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(capacity, dict):
            capacity = MskconnectConnectorCapacity(**capacity)
        if isinstance(kafka_cluster, dict):
            kafka_cluster = MskconnectConnectorKafkaCluster(**kafka_cluster)
        if isinstance(kafka_cluster_client_authentication, dict):
            kafka_cluster_client_authentication = MskconnectConnectorKafkaClusterClientAuthentication(**kafka_cluster_client_authentication)
        if isinstance(kafka_cluster_encryption_in_transit, dict):
            kafka_cluster_encryption_in_transit = MskconnectConnectorKafkaClusterEncryptionInTransit(**kafka_cluster_encryption_in_transit)
        if isinstance(log_delivery, dict):
            log_delivery = MskconnectConnectorLogDelivery(**log_delivery)
        if isinstance(timeouts, dict):
            timeouts = MskconnectConnectorTimeouts(**timeouts)
        if isinstance(worker_configuration, dict):
            worker_configuration = MskconnectConnectorWorkerConfiguration(**worker_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71f64c8a141f988ea121e2687ac8931bb6e2416b68b4431a63cc784784b8acd0)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument capacity", value=capacity, expected_type=type_hints["capacity"])
            check_type(argname="argument connector_configuration", value=connector_configuration, expected_type=type_hints["connector_configuration"])
            check_type(argname="argument kafka_cluster", value=kafka_cluster, expected_type=type_hints["kafka_cluster"])
            check_type(argname="argument kafka_cluster_client_authentication", value=kafka_cluster_client_authentication, expected_type=type_hints["kafka_cluster_client_authentication"])
            check_type(argname="argument kafka_cluster_encryption_in_transit", value=kafka_cluster_encryption_in_transit, expected_type=type_hints["kafka_cluster_encryption_in_transit"])
            check_type(argname="argument kafkaconnect_version", value=kafkaconnect_version, expected_type=type_hints["kafkaconnect_version"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument plugin", value=plugin, expected_type=type_hints["plugin"])
            check_type(argname="argument service_execution_role_arn", value=service_execution_role_arn, expected_type=type_hints["service_execution_role_arn"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument log_delivery", value=log_delivery, expected_type=type_hints["log_delivery"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument worker_configuration", value=worker_configuration, expected_type=type_hints["worker_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "capacity": capacity,
            "connector_configuration": connector_configuration,
            "kafka_cluster": kafka_cluster,
            "kafka_cluster_client_authentication": kafka_cluster_client_authentication,
            "kafka_cluster_encryption_in_transit": kafka_cluster_encryption_in_transit,
            "kafkaconnect_version": kafkaconnect_version,
            "name": name,
            "plugin": plugin,
            "service_execution_role_arn": service_execution_role_arn,
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
        if log_delivery is not None:
            self._values["log_delivery"] = log_delivery
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if worker_configuration is not None:
            self._values["worker_configuration"] = worker_configuration

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
    def capacity(self) -> MskconnectConnectorCapacity:
        '''capacity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#capacity MskconnectConnector#capacity}
        '''
        result = self._values.get("capacity")
        assert result is not None, "Required property 'capacity' is missing"
        return typing.cast(MskconnectConnectorCapacity, result)

    @builtins.property
    def connector_configuration(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#connector_configuration MskconnectConnector#connector_configuration}.'''
        result = self._values.get("connector_configuration")
        assert result is not None, "Required property 'connector_configuration' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    @builtins.property
    def kafka_cluster(self) -> "MskconnectConnectorKafkaCluster":
        '''kafka_cluster block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#kafka_cluster MskconnectConnector#kafka_cluster}
        '''
        result = self._values.get("kafka_cluster")
        assert result is not None, "Required property 'kafka_cluster' is missing"
        return typing.cast("MskconnectConnectorKafkaCluster", result)

    @builtins.property
    def kafka_cluster_client_authentication(
        self,
    ) -> "MskconnectConnectorKafkaClusterClientAuthentication":
        '''kafka_cluster_client_authentication block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#kafka_cluster_client_authentication MskconnectConnector#kafka_cluster_client_authentication}
        '''
        result = self._values.get("kafka_cluster_client_authentication")
        assert result is not None, "Required property 'kafka_cluster_client_authentication' is missing"
        return typing.cast("MskconnectConnectorKafkaClusterClientAuthentication", result)

    @builtins.property
    def kafka_cluster_encryption_in_transit(
        self,
    ) -> "MskconnectConnectorKafkaClusterEncryptionInTransit":
        '''kafka_cluster_encryption_in_transit block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#kafka_cluster_encryption_in_transit MskconnectConnector#kafka_cluster_encryption_in_transit}
        '''
        result = self._values.get("kafka_cluster_encryption_in_transit")
        assert result is not None, "Required property 'kafka_cluster_encryption_in_transit' is missing"
        return typing.cast("MskconnectConnectorKafkaClusterEncryptionInTransit", result)

    @builtins.property
    def kafkaconnect_version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#kafkaconnect_version MskconnectConnector#kafkaconnect_version}.'''
        result = self._values.get("kafkaconnect_version")
        assert result is not None, "Required property 'kafkaconnect_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#name MskconnectConnector#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def plugin(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MskconnectConnectorPlugin"]]:
        '''plugin block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#plugin MskconnectConnector#plugin}
        '''
        result = self._values.get("plugin")
        assert result is not None, "Required property 'plugin' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MskconnectConnectorPlugin"]], result)

    @builtins.property
    def service_execution_role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#service_execution_role_arn MskconnectConnector#service_execution_role_arn}.'''
        result = self._values.get("service_execution_role_arn")
        assert result is not None, "Required property 'service_execution_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#description MskconnectConnector#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#id MskconnectConnector#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_delivery(self) -> typing.Optional["MskconnectConnectorLogDelivery"]:
        '''log_delivery block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#log_delivery MskconnectConnector#log_delivery}
        '''
        result = self._values.get("log_delivery")
        return typing.cast(typing.Optional["MskconnectConnectorLogDelivery"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["MskconnectConnectorTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#timeouts MskconnectConnector#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["MskconnectConnectorTimeouts"], result)

    @builtins.property
    def worker_configuration(
        self,
    ) -> typing.Optional["MskconnectConnectorWorkerConfiguration"]:
        '''worker_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#worker_configuration MskconnectConnector#worker_configuration}
        '''
        result = self._values.get("worker_configuration")
        return typing.cast(typing.Optional["MskconnectConnectorWorkerConfiguration"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskconnectConnectorConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.mskconnectConnector.MskconnectConnectorKafkaCluster",
    jsii_struct_bases=[],
    name_mapping={"apache_kafka_cluster": "apacheKafkaCluster"},
)
class MskconnectConnectorKafkaCluster:
    def __init__(
        self,
        *,
        apache_kafka_cluster: typing.Union["MskconnectConnectorKafkaClusterApacheKafkaCluster", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param apache_kafka_cluster: apache_kafka_cluster block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#apache_kafka_cluster MskconnectConnector#apache_kafka_cluster}
        '''
        if isinstance(apache_kafka_cluster, dict):
            apache_kafka_cluster = MskconnectConnectorKafkaClusterApacheKafkaCluster(**apache_kafka_cluster)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52c82f0a996f092cf3a4e68b6e46a840fa8ee683051608ac7acf09f69367d6fe)
            check_type(argname="argument apache_kafka_cluster", value=apache_kafka_cluster, expected_type=type_hints["apache_kafka_cluster"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "apache_kafka_cluster": apache_kafka_cluster,
        }

    @builtins.property
    def apache_kafka_cluster(
        self,
    ) -> "MskconnectConnectorKafkaClusterApacheKafkaCluster":
        '''apache_kafka_cluster block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#apache_kafka_cluster MskconnectConnector#apache_kafka_cluster}
        '''
        result = self._values.get("apache_kafka_cluster")
        assert result is not None, "Required property 'apache_kafka_cluster' is missing"
        return typing.cast("MskconnectConnectorKafkaClusterApacheKafkaCluster", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskconnectConnectorKafkaCluster(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.mskconnectConnector.MskconnectConnectorKafkaClusterApacheKafkaCluster",
    jsii_struct_bases=[],
    name_mapping={"bootstrap_servers": "bootstrapServers", "vpc": "vpc"},
)
class MskconnectConnectorKafkaClusterApacheKafkaCluster:
    def __init__(
        self,
        *,
        bootstrap_servers: builtins.str,
        vpc: typing.Union["MskconnectConnectorKafkaClusterApacheKafkaClusterVpc", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param bootstrap_servers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#bootstrap_servers MskconnectConnector#bootstrap_servers}.
        :param vpc: vpc block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#vpc MskconnectConnector#vpc}
        '''
        if isinstance(vpc, dict):
            vpc = MskconnectConnectorKafkaClusterApacheKafkaClusterVpc(**vpc)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15ccf1283cf46eae4f71ccfa0c0461649c5daaaec1c3b4ec34e78a13e857613e)
            check_type(argname="argument bootstrap_servers", value=bootstrap_servers, expected_type=type_hints["bootstrap_servers"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bootstrap_servers": bootstrap_servers,
            "vpc": vpc,
        }

    @builtins.property
    def bootstrap_servers(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#bootstrap_servers MskconnectConnector#bootstrap_servers}.'''
        result = self._values.get("bootstrap_servers")
        assert result is not None, "Required property 'bootstrap_servers' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpc(self) -> "MskconnectConnectorKafkaClusterApacheKafkaClusterVpc":
        '''vpc block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#vpc MskconnectConnector#vpc}
        '''
        result = self._values.get("vpc")
        assert result is not None, "Required property 'vpc' is missing"
        return typing.cast("MskconnectConnectorKafkaClusterApacheKafkaClusterVpc", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskconnectConnectorKafkaClusterApacheKafkaCluster(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MskconnectConnectorKafkaClusterApacheKafkaClusterOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.mskconnectConnector.MskconnectConnectorKafkaClusterApacheKafkaClusterOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__435fa6695b5460c0814284e1bfc1681c4f9a5ec9f583791bdbe48e03f818b183)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putVpc")
    def put_vpc(
        self,
        *,
        security_groups: typing.Sequence[builtins.str],
        subnets: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#security_groups MskconnectConnector#security_groups}.
        :param subnets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#subnets MskconnectConnector#subnets}.
        '''
        value = MskconnectConnectorKafkaClusterApacheKafkaClusterVpc(
            security_groups=security_groups, subnets=subnets
        )

        return typing.cast(None, jsii.invoke(self, "putVpc", [value]))

    @builtins.property
    @jsii.member(jsii_name="vpc")
    def vpc(
        self,
    ) -> "MskconnectConnectorKafkaClusterApacheKafkaClusterVpcOutputReference":
        return typing.cast("MskconnectConnectorKafkaClusterApacheKafkaClusterVpcOutputReference", jsii.get(self, "vpc"))

    @builtins.property
    @jsii.member(jsii_name="bootstrapServersInput")
    def bootstrap_servers_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bootstrapServersInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcInput")
    def vpc_input(
        self,
    ) -> typing.Optional["MskconnectConnectorKafkaClusterApacheKafkaClusterVpc"]:
        return typing.cast(typing.Optional["MskconnectConnectorKafkaClusterApacheKafkaClusterVpc"], jsii.get(self, "vpcInput"))

    @builtins.property
    @jsii.member(jsii_name="bootstrapServers")
    def bootstrap_servers(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bootstrapServers"))

    @bootstrap_servers.setter
    def bootstrap_servers(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e64667c8f71a0980622d8f84548d7a89217e05e4684dcc58bc37a3e7189eead2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bootstrapServers", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MskconnectConnectorKafkaClusterApacheKafkaCluster]:
        return typing.cast(typing.Optional[MskconnectConnectorKafkaClusterApacheKafkaCluster], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskconnectConnectorKafkaClusterApacheKafkaCluster],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd4c882d540e0859db071fb4d8b5369a9f27a90bae48237a119b82810b69a38c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.mskconnectConnector.MskconnectConnectorKafkaClusterApacheKafkaClusterVpc",
    jsii_struct_bases=[],
    name_mapping={"security_groups": "securityGroups", "subnets": "subnets"},
)
class MskconnectConnectorKafkaClusterApacheKafkaClusterVpc:
    def __init__(
        self,
        *,
        security_groups: typing.Sequence[builtins.str],
        subnets: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#security_groups MskconnectConnector#security_groups}.
        :param subnets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#subnets MskconnectConnector#subnets}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e376f4a959d930e09c3aa29f222a24ec98dc7d16719c930cd487dbf34589a7b)
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            check_type(argname="argument subnets", value=subnets, expected_type=type_hints["subnets"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "security_groups": security_groups,
            "subnets": subnets,
        }

    @builtins.property
    def security_groups(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#security_groups MskconnectConnector#security_groups}.'''
        result = self._values.get("security_groups")
        assert result is not None, "Required property 'security_groups' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def subnets(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#subnets MskconnectConnector#subnets}.'''
        result = self._values.get("subnets")
        assert result is not None, "Required property 'subnets' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskconnectConnectorKafkaClusterApacheKafkaClusterVpc(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MskconnectConnectorKafkaClusterApacheKafkaClusterVpcOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.mskconnectConnector.MskconnectConnectorKafkaClusterApacheKafkaClusterVpcOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f4678ae6387dca256e7edf3b623a4cfc4b014e9cddee6a14915d1c87a08b552b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="securityGroupsInput")
    def security_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetsInput")
    def subnets_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetsInput"))

    @builtins.property
    @jsii.member(jsii_name="securityGroups")
    def security_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroups"))

    @security_groups.setter
    def security_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef6efa1afa4b61fa34050d49be31807e44915a01e350c784db53b1d18e93cf7f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroups", value)

    @builtins.property
    @jsii.member(jsii_name="subnets")
    def subnets(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnets"))

    @subnets.setter
    def subnets(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac5cb69ac931c333e85b0e85229afb6b2f724af29d4398edd9eaacb34162dd50)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnets", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MskconnectConnectorKafkaClusterApacheKafkaClusterVpc]:
        return typing.cast(typing.Optional[MskconnectConnectorKafkaClusterApacheKafkaClusterVpc], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskconnectConnectorKafkaClusterApacheKafkaClusterVpc],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1cfadf4814a3dbef3ed2e0f8c15dec966afba9449d256265e503c5830da62dd8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.mskconnectConnector.MskconnectConnectorKafkaClusterClientAuthentication",
    jsii_struct_bases=[],
    name_mapping={"authentication_type": "authenticationType"},
)
class MskconnectConnectorKafkaClusterClientAuthentication:
    def __init__(
        self,
        *,
        authentication_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param authentication_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#authentication_type MskconnectConnector#authentication_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__028551bd31674e1028d99279f312718f3f841f721f008aa149fc049e922c5759)
            check_type(argname="argument authentication_type", value=authentication_type, expected_type=type_hints["authentication_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if authentication_type is not None:
            self._values["authentication_type"] = authentication_type

    @builtins.property
    def authentication_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#authentication_type MskconnectConnector#authentication_type}.'''
        result = self._values.get("authentication_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskconnectConnectorKafkaClusterClientAuthentication(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MskconnectConnectorKafkaClusterClientAuthenticationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.mskconnectConnector.MskconnectConnectorKafkaClusterClientAuthenticationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f58e8be57210f4be3a4f2695cc206d21667b42681cee8fc4111ffe38b923be12)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAuthenticationType")
    def reset_authentication_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthenticationType", []))

    @builtins.property
    @jsii.member(jsii_name="authenticationTypeInput")
    def authentication_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authenticationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="authenticationType")
    def authentication_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authenticationType"))

    @authentication_type.setter
    def authentication_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__112bbd00de4d80a4a37b35b67ae989711984cc0e1ae0f56da6a2f194e9f488ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authenticationType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MskconnectConnectorKafkaClusterClientAuthentication]:
        return typing.cast(typing.Optional[MskconnectConnectorKafkaClusterClientAuthentication], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskconnectConnectorKafkaClusterClientAuthentication],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3fef87d7b180a540832c11b20a24d09eadf0eaa1928c5e2683674e16c07a8cd6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.mskconnectConnector.MskconnectConnectorKafkaClusterEncryptionInTransit",
    jsii_struct_bases=[],
    name_mapping={"encryption_type": "encryptionType"},
)
class MskconnectConnectorKafkaClusterEncryptionInTransit:
    def __init__(
        self,
        *,
        encryption_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param encryption_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#encryption_type MskconnectConnector#encryption_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3aa5c4e2d730892deead53c5cf14a740cee07a0773a1375d5ca12fec4fe3a3a)
            check_type(argname="argument encryption_type", value=encryption_type, expected_type=type_hints["encryption_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if encryption_type is not None:
            self._values["encryption_type"] = encryption_type

    @builtins.property
    def encryption_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#encryption_type MskconnectConnector#encryption_type}.'''
        result = self._values.get("encryption_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskconnectConnectorKafkaClusterEncryptionInTransit(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MskconnectConnectorKafkaClusterEncryptionInTransitOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.mskconnectConnector.MskconnectConnectorKafkaClusterEncryptionInTransitOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e7a927bc3c267e06d126120a34f7aa8320f0bc683d708a08b7ee672fa6fe481e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEncryptionType")
    def reset_encryption_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionType", []))

    @builtins.property
    @jsii.member(jsii_name="encryptionTypeInput")
    def encryption_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptionTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionType")
    def encryption_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encryptionType"))

    @encryption_type.setter
    def encryption_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42a7f83c3f6e59015fd376f6613beaad367b7e89582d225c35c16cb4959b05a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MskconnectConnectorKafkaClusterEncryptionInTransit]:
        return typing.cast(typing.Optional[MskconnectConnectorKafkaClusterEncryptionInTransit], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskconnectConnectorKafkaClusterEncryptionInTransit],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41b4ec9797d80a78c049532d725a0404333aef416dba1349e69e6a27d4e4445a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MskconnectConnectorKafkaClusterOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.mskconnectConnector.MskconnectConnectorKafkaClusterOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d3c9ecbfa89a9eeecce83fdea758aa64e6613acbe409599f07d1b30bef18de45)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putApacheKafkaCluster")
    def put_apache_kafka_cluster(
        self,
        *,
        bootstrap_servers: builtins.str,
        vpc: typing.Union[MskconnectConnectorKafkaClusterApacheKafkaClusterVpc, typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param bootstrap_servers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#bootstrap_servers MskconnectConnector#bootstrap_servers}.
        :param vpc: vpc block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#vpc MskconnectConnector#vpc}
        '''
        value = MskconnectConnectorKafkaClusterApacheKafkaCluster(
            bootstrap_servers=bootstrap_servers, vpc=vpc
        )

        return typing.cast(None, jsii.invoke(self, "putApacheKafkaCluster", [value]))

    @builtins.property
    @jsii.member(jsii_name="apacheKafkaCluster")
    def apache_kafka_cluster(
        self,
    ) -> MskconnectConnectorKafkaClusterApacheKafkaClusterOutputReference:
        return typing.cast(MskconnectConnectorKafkaClusterApacheKafkaClusterOutputReference, jsii.get(self, "apacheKafkaCluster"))

    @builtins.property
    @jsii.member(jsii_name="apacheKafkaClusterInput")
    def apache_kafka_cluster_input(
        self,
    ) -> typing.Optional[MskconnectConnectorKafkaClusterApacheKafkaCluster]:
        return typing.cast(typing.Optional[MskconnectConnectorKafkaClusterApacheKafkaCluster], jsii.get(self, "apacheKafkaClusterInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MskconnectConnectorKafkaCluster]:
        return typing.cast(typing.Optional[MskconnectConnectorKafkaCluster], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskconnectConnectorKafkaCluster],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e7ddecd767b2e12fdafc276889b264ce979f42d8101a7815bbef9117cc5a7b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.mskconnectConnector.MskconnectConnectorLogDelivery",
    jsii_struct_bases=[],
    name_mapping={"worker_log_delivery": "workerLogDelivery"},
)
class MskconnectConnectorLogDelivery:
    def __init__(
        self,
        *,
        worker_log_delivery: typing.Union["MskconnectConnectorLogDeliveryWorkerLogDelivery", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param worker_log_delivery: worker_log_delivery block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#worker_log_delivery MskconnectConnector#worker_log_delivery}
        '''
        if isinstance(worker_log_delivery, dict):
            worker_log_delivery = MskconnectConnectorLogDeliveryWorkerLogDelivery(**worker_log_delivery)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ff7f414742fed2884cae0b999fe0459ff0180b6a62dd29fc661d9fd78629b80)
            check_type(argname="argument worker_log_delivery", value=worker_log_delivery, expected_type=type_hints["worker_log_delivery"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "worker_log_delivery": worker_log_delivery,
        }

    @builtins.property
    def worker_log_delivery(self) -> "MskconnectConnectorLogDeliveryWorkerLogDelivery":
        '''worker_log_delivery block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#worker_log_delivery MskconnectConnector#worker_log_delivery}
        '''
        result = self._values.get("worker_log_delivery")
        assert result is not None, "Required property 'worker_log_delivery' is missing"
        return typing.cast("MskconnectConnectorLogDeliveryWorkerLogDelivery", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskconnectConnectorLogDelivery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MskconnectConnectorLogDeliveryOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.mskconnectConnector.MskconnectConnectorLogDeliveryOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__874733c25499655ab09076ff1e3570811879e10b4a006f96e2cfea2a7c15b55d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putWorkerLogDelivery")
    def put_worker_log_delivery(
        self,
        *,
        cloudwatch_logs: typing.Optional[typing.Union["MskconnectConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogs", typing.Dict[builtins.str, typing.Any]]] = None,
        firehose: typing.Optional[typing.Union["MskconnectConnectorLogDeliveryWorkerLogDeliveryFirehose", typing.Dict[builtins.str, typing.Any]]] = None,
        s3: typing.Optional[typing.Union["MskconnectConnectorLogDeliveryWorkerLogDeliveryS3", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cloudwatch_logs: cloudwatch_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#cloudwatch_logs MskconnectConnector#cloudwatch_logs}
        :param firehose: firehose block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#firehose MskconnectConnector#firehose}
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#s3 MskconnectConnector#s3}
        '''
        value = MskconnectConnectorLogDeliveryWorkerLogDelivery(
            cloudwatch_logs=cloudwatch_logs, firehose=firehose, s3=s3
        )

        return typing.cast(None, jsii.invoke(self, "putWorkerLogDelivery", [value]))

    @builtins.property
    @jsii.member(jsii_name="workerLogDelivery")
    def worker_log_delivery(
        self,
    ) -> "MskconnectConnectorLogDeliveryWorkerLogDeliveryOutputReference":
        return typing.cast("MskconnectConnectorLogDeliveryWorkerLogDeliveryOutputReference", jsii.get(self, "workerLogDelivery"))

    @builtins.property
    @jsii.member(jsii_name="workerLogDeliveryInput")
    def worker_log_delivery_input(
        self,
    ) -> typing.Optional["MskconnectConnectorLogDeliveryWorkerLogDelivery"]:
        return typing.cast(typing.Optional["MskconnectConnectorLogDeliveryWorkerLogDelivery"], jsii.get(self, "workerLogDeliveryInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MskconnectConnectorLogDelivery]:
        return typing.cast(typing.Optional[MskconnectConnectorLogDelivery], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskconnectConnectorLogDelivery],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7f4469fa3540c6fdb0bd46c8d2681952639ad75c340c12004116c2b60e03d31)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.mskconnectConnector.MskconnectConnectorLogDeliveryWorkerLogDelivery",
    jsii_struct_bases=[],
    name_mapping={
        "cloudwatch_logs": "cloudwatchLogs",
        "firehose": "firehose",
        "s3": "s3",
    },
)
class MskconnectConnectorLogDeliveryWorkerLogDelivery:
    def __init__(
        self,
        *,
        cloudwatch_logs: typing.Optional[typing.Union["MskconnectConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogs", typing.Dict[builtins.str, typing.Any]]] = None,
        firehose: typing.Optional[typing.Union["MskconnectConnectorLogDeliveryWorkerLogDeliveryFirehose", typing.Dict[builtins.str, typing.Any]]] = None,
        s3: typing.Optional[typing.Union["MskconnectConnectorLogDeliveryWorkerLogDeliveryS3", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cloudwatch_logs: cloudwatch_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#cloudwatch_logs MskconnectConnector#cloudwatch_logs}
        :param firehose: firehose block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#firehose MskconnectConnector#firehose}
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#s3 MskconnectConnector#s3}
        '''
        if isinstance(cloudwatch_logs, dict):
            cloudwatch_logs = MskconnectConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogs(**cloudwatch_logs)
        if isinstance(firehose, dict):
            firehose = MskconnectConnectorLogDeliveryWorkerLogDeliveryFirehose(**firehose)
        if isinstance(s3, dict):
            s3 = MskconnectConnectorLogDeliveryWorkerLogDeliveryS3(**s3)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5d88f12531316bc0d8833d700b2c10844107602e58a44407e24f90dd7948bb0)
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
    ) -> typing.Optional["MskconnectConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogs"]:
        '''cloudwatch_logs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#cloudwatch_logs MskconnectConnector#cloudwatch_logs}
        '''
        result = self._values.get("cloudwatch_logs")
        return typing.cast(typing.Optional["MskconnectConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogs"], result)

    @builtins.property
    def firehose(
        self,
    ) -> typing.Optional["MskconnectConnectorLogDeliveryWorkerLogDeliveryFirehose"]:
        '''firehose block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#firehose MskconnectConnector#firehose}
        '''
        result = self._values.get("firehose")
        return typing.cast(typing.Optional["MskconnectConnectorLogDeliveryWorkerLogDeliveryFirehose"], result)

    @builtins.property
    def s3(
        self,
    ) -> typing.Optional["MskconnectConnectorLogDeliveryWorkerLogDeliveryS3"]:
        '''s3 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#s3 MskconnectConnector#s3}
        '''
        result = self._values.get("s3")
        return typing.cast(typing.Optional["MskconnectConnectorLogDeliveryWorkerLogDeliveryS3"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskconnectConnectorLogDeliveryWorkerLogDelivery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.mskconnectConnector.MskconnectConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogs",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "log_group": "logGroup"},
)
class MskconnectConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogs:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        log_group: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#enabled MskconnectConnector#enabled}.
        :param log_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#log_group MskconnectConnector#log_group}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a53c05240f5403589f47ddb332aa996dd7b572fc057ed73d9bf0b362cf5e749b)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument log_group", value=log_group, expected_type=type_hints["log_group"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "enabled": enabled,
        }
        if log_group is not None:
            self._values["log_group"] = log_group

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#enabled MskconnectConnector#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def log_group(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#log_group MskconnectConnector#log_group}.'''
        result = self._values.get("log_group")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskconnectConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MskconnectConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.mskconnectConnector.MskconnectConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3a86844f0ab06926dc0e9be883b73c6b212c5a1e1c29dcf86485629444b97a85)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetLogGroup")
    def reset_log_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogGroup", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="logGroupInput")
    def log_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logGroupInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__a1173ecf5b3dd3cd6ec295b2459aa9bd9cf2231f07445f62b068c2814983ea08)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="logGroup")
    def log_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logGroup"))

    @log_group.setter
    def log_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6b6559c4993750cb20c89c9b0fe13ae31cfbab9d5f2b526b3ba1a0336f23c79)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logGroup", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MskconnectConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogs]:
        return typing.cast(typing.Optional[MskconnectConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskconnectConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogs],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9fb374e075145af974828b86d6ca60f47dee72b163fdf017f96e3573ffeae7e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.mskconnectConnector.MskconnectConnectorLogDeliveryWorkerLogDeliveryFirehose",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "delivery_stream": "deliveryStream"},
)
class MskconnectConnectorLogDeliveryWorkerLogDeliveryFirehose:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        delivery_stream: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#enabled MskconnectConnector#enabled}.
        :param delivery_stream: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#delivery_stream MskconnectConnector#delivery_stream}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67c808e5f5ebf9bd2b5b827822bd2d22c15cbce88a6759a66a3cc2b356612365)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument delivery_stream", value=delivery_stream, expected_type=type_hints["delivery_stream"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "enabled": enabled,
        }
        if delivery_stream is not None:
            self._values["delivery_stream"] = delivery_stream

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#enabled MskconnectConnector#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def delivery_stream(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#delivery_stream MskconnectConnector#delivery_stream}.'''
        result = self._values.get("delivery_stream")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskconnectConnectorLogDeliveryWorkerLogDeliveryFirehose(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MskconnectConnectorLogDeliveryWorkerLogDeliveryFirehoseOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.mskconnectConnector.MskconnectConnectorLogDeliveryWorkerLogDeliveryFirehoseOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4574ee523db815cad037b894e2e79335b72e042bb9b2f079a011b4c3f513f6c8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDeliveryStream")
    def reset_delivery_stream(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeliveryStream", []))

    @builtins.property
    @jsii.member(jsii_name="deliveryStreamInput")
    def delivery_stream_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deliveryStreamInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="deliveryStream")
    def delivery_stream(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deliveryStream"))

    @delivery_stream.setter
    def delivery_stream(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f23e05354bb92f06524ecbfc354667ed90142da022a6871ce97cdbc21de7ec2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deliveryStream", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__c19c90ca8141a6e55e3470fc431fb90ca3f7c1f97da0618d8a35c074607c3856)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MskconnectConnectorLogDeliveryWorkerLogDeliveryFirehose]:
        return typing.cast(typing.Optional[MskconnectConnectorLogDeliveryWorkerLogDeliveryFirehose], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskconnectConnectorLogDeliveryWorkerLogDeliveryFirehose],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bed1a0ad66e5bcd7a8dd9d925afd2377cb9c957e38791be638e53a6ed8ef4c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MskconnectConnectorLogDeliveryWorkerLogDeliveryOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.mskconnectConnector.MskconnectConnectorLogDeliveryWorkerLogDeliveryOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__adeb35220a1e30859c7ce3be885b7f8f5e2db4ee16867d1612c11dc7b37ee2d5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCloudwatchLogs")
    def put_cloudwatch_logs(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        log_group: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#enabled MskconnectConnector#enabled}.
        :param log_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#log_group MskconnectConnector#log_group}.
        '''
        value = MskconnectConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogs(
            enabled=enabled, log_group=log_group
        )

        return typing.cast(None, jsii.invoke(self, "putCloudwatchLogs", [value]))

    @jsii.member(jsii_name="putFirehose")
    def put_firehose(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        delivery_stream: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#enabled MskconnectConnector#enabled}.
        :param delivery_stream: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#delivery_stream MskconnectConnector#delivery_stream}.
        '''
        value = MskconnectConnectorLogDeliveryWorkerLogDeliveryFirehose(
            enabled=enabled, delivery_stream=delivery_stream
        )

        return typing.cast(None, jsii.invoke(self, "putFirehose", [value]))

    @jsii.member(jsii_name="putS3")
    def put_s3(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        bucket: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#enabled MskconnectConnector#enabled}.
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#bucket MskconnectConnector#bucket}.
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#prefix MskconnectConnector#prefix}.
        '''
        value = MskconnectConnectorLogDeliveryWorkerLogDeliveryS3(
            enabled=enabled, bucket=bucket, prefix=prefix
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
    ) -> MskconnectConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogsOutputReference:
        return typing.cast(MskconnectConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogsOutputReference, jsii.get(self, "cloudwatchLogs"))

    @builtins.property
    @jsii.member(jsii_name="firehose")
    def firehose(
        self,
    ) -> MskconnectConnectorLogDeliveryWorkerLogDeliveryFirehoseOutputReference:
        return typing.cast(MskconnectConnectorLogDeliveryWorkerLogDeliveryFirehoseOutputReference, jsii.get(self, "firehose"))

    @builtins.property
    @jsii.member(jsii_name="s3")
    def s3(self) -> "MskconnectConnectorLogDeliveryWorkerLogDeliveryS3OutputReference":
        return typing.cast("MskconnectConnectorLogDeliveryWorkerLogDeliveryS3OutputReference", jsii.get(self, "s3"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLogsInput")
    def cloudwatch_logs_input(
        self,
    ) -> typing.Optional[MskconnectConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogs]:
        return typing.cast(typing.Optional[MskconnectConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogs], jsii.get(self, "cloudwatchLogsInput"))

    @builtins.property
    @jsii.member(jsii_name="firehoseInput")
    def firehose_input(
        self,
    ) -> typing.Optional[MskconnectConnectorLogDeliveryWorkerLogDeliveryFirehose]:
        return typing.cast(typing.Optional[MskconnectConnectorLogDeliveryWorkerLogDeliveryFirehose], jsii.get(self, "firehoseInput"))

    @builtins.property
    @jsii.member(jsii_name="s3Input")
    def s3_input(
        self,
    ) -> typing.Optional["MskconnectConnectorLogDeliveryWorkerLogDeliveryS3"]:
        return typing.cast(typing.Optional["MskconnectConnectorLogDeliveryWorkerLogDeliveryS3"], jsii.get(self, "s3Input"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MskconnectConnectorLogDeliveryWorkerLogDelivery]:
        return typing.cast(typing.Optional[MskconnectConnectorLogDeliveryWorkerLogDelivery], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskconnectConnectorLogDeliveryWorkerLogDelivery],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87a30d352c55731939fcd73ba77b75409dd9a1fe86d155dc379e200b328acf01)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.mskconnectConnector.MskconnectConnectorLogDeliveryWorkerLogDeliveryS3",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "bucket": "bucket", "prefix": "prefix"},
)
class MskconnectConnectorLogDeliveryWorkerLogDeliveryS3:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        bucket: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#enabled MskconnectConnector#enabled}.
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#bucket MskconnectConnector#bucket}.
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#prefix MskconnectConnector#prefix}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07b8845816c19df3ab60f82e291c4160d553c29d1be701a0f12d1bff36a0504b)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "enabled": enabled,
        }
        if bucket is not None:
            self._values["bucket"] = bucket
        if prefix is not None:
            self._values["prefix"] = prefix

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#enabled MskconnectConnector#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def bucket(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#bucket MskconnectConnector#bucket}.'''
        result = self._values.get("bucket")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#prefix MskconnectConnector#prefix}.'''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskconnectConnectorLogDeliveryWorkerLogDeliveryS3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MskconnectConnectorLogDeliveryWorkerLogDeliveryS3OutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.mskconnectConnector.MskconnectConnectorLogDeliveryWorkerLogDeliveryS3OutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8d89ad151edf50c91b51f321d30ba58df0207621806601484b7f1a95b043b60f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBucket")
    def reset_bucket(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucket", []))

    @jsii.member(jsii_name="resetPrefix")
    def reset_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefix", []))

    @builtins.property
    @jsii.member(jsii_name="bucketInput")
    def bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__061ba98857632196cffade33e7a9e6f4e7f9d38835a313ad95c2af6958946dff)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8a43a00271f87f36c926f335f8bce31b35abc2880967b0308714ea7853effb3e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e789e1934c2a36012217b75f7184724186a2d5d05d793d3cbd0467ee96af16f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MskconnectConnectorLogDeliveryWorkerLogDeliveryS3]:
        return typing.cast(typing.Optional[MskconnectConnectorLogDeliveryWorkerLogDeliveryS3], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskconnectConnectorLogDeliveryWorkerLogDeliveryS3],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26687c3218e56263cfe4823677ae166dc93133266e88505b1521f743da54affe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.mskconnectConnector.MskconnectConnectorPlugin",
    jsii_struct_bases=[],
    name_mapping={"custom_plugin": "customPlugin"},
)
class MskconnectConnectorPlugin:
    def __init__(
        self,
        *,
        custom_plugin: typing.Union["MskconnectConnectorPluginCustomPlugin", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param custom_plugin: custom_plugin block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#custom_plugin MskconnectConnector#custom_plugin}
        '''
        if isinstance(custom_plugin, dict):
            custom_plugin = MskconnectConnectorPluginCustomPlugin(**custom_plugin)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80d4b75f18f83c6b3973dc8ffa63a4c1aae74345ba58485cc8ac961596f7fa5a)
            check_type(argname="argument custom_plugin", value=custom_plugin, expected_type=type_hints["custom_plugin"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "custom_plugin": custom_plugin,
        }

    @builtins.property
    def custom_plugin(self) -> "MskconnectConnectorPluginCustomPlugin":
        '''custom_plugin block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#custom_plugin MskconnectConnector#custom_plugin}
        '''
        result = self._values.get("custom_plugin")
        assert result is not None, "Required property 'custom_plugin' is missing"
        return typing.cast("MskconnectConnectorPluginCustomPlugin", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskconnectConnectorPlugin(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.mskconnectConnector.MskconnectConnectorPluginCustomPlugin",
    jsii_struct_bases=[],
    name_mapping={"arn": "arn", "revision": "revision"},
)
class MskconnectConnectorPluginCustomPlugin:
    def __init__(self, *, arn: builtins.str, revision: jsii.Number) -> None:
        '''
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#arn MskconnectConnector#arn}.
        :param revision: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#revision MskconnectConnector#revision}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cda9c5d2d4265663b3247d7c939a1facf52aa57a3e675862067e9622ea2c5a60)
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            check_type(argname="argument revision", value=revision, expected_type=type_hints["revision"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "arn": arn,
            "revision": revision,
        }

    @builtins.property
    def arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#arn MskconnectConnector#arn}.'''
        result = self._values.get("arn")
        assert result is not None, "Required property 'arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def revision(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#revision MskconnectConnector#revision}.'''
        result = self._values.get("revision")
        assert result is not None, "Required property 'revision' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskconnectConnectorPluginCustomPlugin(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MskconnectConnectorPluginCustomPluginOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.mskconnectConnector.MskconnectConnectorPluginCustomPluginOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d077b0a1d377aa71f26bb389902b3fa9dcb7f3761a79b8be7b3105e2eb47746d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="arnInput")
    def arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "arnInput"))

    @builtins.property
    @jsii.member(jsii_name="revisionInput")
    def revision_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "revisionInput"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @arn.setter
    def arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d7db8c5e9844a37d7ee0b90ed7d704824af5ac7d781e6367df579a416394d26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "arn", value)

    @builtins.property
    @jsii.member(jsii_name="revision")
    def revision(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "revision"))

    @revision.setter
    def revision(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__681f6fe6acb5399d57e77ae40128a66c313f7590ee0baea2712d04685aa6e515)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "revision", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MskconnectConnectorPluginCustomPlugin]:
        return typing.cast(typing.Optional[MskconnectConnectorPluginCustomPlugin], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskconnectConnectorPluginCustomPlugin],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3b41183003ab68aaa0a2c047a94d7d46d92aa57d2ff716e6f3e5955607e62af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MskconnectConnectorPluginList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.mskconnectConnector.MskconnectConnectorPluginList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b1cea16d9e6fc8d03757067b469e7589f593fbe7e9dabf29b21049dd8e786ea8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "MskconnectConnectorPluginOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65ac5f6bdc973fc847371ffc96f4e2de79908669245765e6b6dd809574a838b2)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MskconnectConnectorPluginOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1309fbfdfca47c8902e8445274028ec4f0f4ae5fa327c64654810f706c88b7c1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e3c39693d53be82aa52be5fbda6ba26a451330242122d2ea76bba41254ab5416)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4dd756b91741234298212769bda4f713d5a761dfd6e518b209feb5e3e0fd84eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MskconnectConnectorPlugin]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MskconnectConnectorPlugin]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MskconnectConnectorPlugin]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d69549cf43b1217b3d3cbbacec511c85c68af3a1e104fba318c0a3cd14c7ed9d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MskconnectConnectorPluginOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.mskconnectConnector.MskconnectConnectorPluginOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7f4e9f17b8b9ad325eb7fecd789535a879c5e8a9fbec7a8c31209e5927aa7ba7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putCustomPlugin")
    def put_custom_plugin(self, *, arn: builtins.str, revision: jsii.Number) -> None:
        '''
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#arn MskconnectConnector#arn}.
        :param revision: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#revision MskconnectConnector#revision}.
        '''
        value = MskconnectConnectorPluginCustomPlugin(arn=arn, revision=revision)

        return typing.cast(None, jsii.invoke(self, "putCustomPlugin", [value]))

    @builtins.property
    @jsii.member(jsii_name="customPlugin")
    def custom_plugin(self) -> MskconnectConnectorPluginCustomPluginOutputReference:
        return typing.cast(MskconnectConnectorPluginCustomPluginOutputReference, jsii.get(self, "customPlugin"))

    @builtins.property
    @jsii.member(jsii_name="customPluginInput")
    def custom_plugin_input(
        self,
    ) -> typing.Optional[MskconnectConnectorPluginCustomPlugin]:
        return typing.cast(typing.Optional[MskconnectConnectorPluginCustomPlugin], jsii.get(self, "customPluginInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MskconnectConnectorPlugin, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MskconnectConnectorPlugin, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MskconnectConnectorPlugin, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a20dc715da39009988e20f9211c4d5fbb4ec151806baf971d4d58081310cf051)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.mskconnectConnector.MskconnectConnectorTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class MskconnectConnectorTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#create MskconnectConnector#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#delete MskconnectConnector#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#update MskconnectConnector#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d810ce3abbca61fd3b587664dd32b2d6545e84ceb18690feeaae8f8dafd3ae9)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#create MskconnectConnector#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#delete MskconnectConnector#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#update MskconnectConnector#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskconnectConnectorTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MskconnectConnectorTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.mskconnectConnector.MskconnectConnectorTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3a3e4665ede8e1cc8eb056c6b673e32dad90257bef3cf56eba6495b5a4061e67)
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
            type_hints = typing.get_type_hints(_typecheckingstub__87f849088646abd433507fb3daa3888341921a42f02adba69b83ce9046ca757a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ce51ce36b9dd624916e016f6e97f148b9c8e809b5f7453f777ce2c622efeed2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d392bbd15669c10583f2928005acbe7f095797552a437d7f45b3fc5a7960464)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MskconnectConnectorTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MskconnectConnectorTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MskconnectConnectorTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31d6d201f8bb984e158c5bbc1c481231b4e7ed4ede8857167fc113b4ae485506)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.mskconnectConnector.MskconnectConnectorWorkerConfiguration",
    jsii_struct_bases=[],
    name_mapping={"arn": "arn", "revision": "revision"},
)
class MskconnectConnectorWorkerConfiguration:
    def __init__(self, *, arn: builtins.str, revision: jsii.Number) -> None:
        '''
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#arn MskconnectConnector#arn}.
        :param revision: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#revision MskconnectConnector#revision}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cee285e310e02d53261ab51597ca5fa3d05a01284c5e879a70e485ce9cdce4d)
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            check_type(argname="argument revision", value=revision, expected_type=type_hints["revision"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "arn": arn,
            "revision": revision,
        }

    @builtins.property
    def arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#arn MskconnectConnector#arn}.'''
        result = self._values.get("arn")
        assert result is not None, "Required property 'arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def revision(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#revision MskconnectConnector#revision}.'''
        result = self._values.get("revision")
        assert result is not None, "Required property 'revision' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskconnectConnectorWorkerConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MskconnectConnectorWorkerConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.mskconnectConnector.MskconnectConnectorWorkerConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f0af4b19df54971c47ec63dea436ea114fe108a22b8ce206ad62fd9a3e83f1b9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="arnInput")
    def arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "arnInput"))

    @builtins.property
    @jsii.member(jsii_name="revisionInput")
    def revision_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "revisionInput"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @arn.setter
    def arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ec2a93367b78ea1f9c1ff82fb46a2c76ff2fd0c6a51bd758dc40605a58663c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "arn", value)

    @builtins.property
    @jsii.member(jsii_name="revision")
    def revision(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "revision"))

    @revision.setter
    def revision(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b719a672b5cd6a960a0c8c1f5108b1b0aeee188c8ff062e266ba54b6200083b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "revision", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MskconnectConnectorWorkerConfiguration]:
        return typing.cast(typing.Optional[MskconnectConnectorWorkerConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskconnectConnectorWorkerConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cfdd4bf89236c30e50a7d3fec01c2931c0ec1e18bfd5488382ca0ba23d5e7d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "MskconnectConnector",
    "MskconnectConnectorCapacity",
    "MskconnectConnectorCapacityAutoscaling",
    "MskconnectConnectorCapacityAutoscalingOutputReference",
    "MskconnectConnectorCapacityAutoscalingScaleInPolicy",
    "MskconnectConnectorCapacityAutoscalingScaleInPolicyOutputReference",
    "MskconnectConnectorCapacityAutoscalingScaleOutPolicy",
    "MskconnectConnectorCapacityAutoscalingScaleOutPolicyOutputReference",
    "MskconnectConnectorCapacityOutputReference",
    "MskconnectConnectorCapacityProvisionedCapacity",
    "MskconnectConnectorCapacityProvisionedCapacityOutputReference",
    "MskconnectConnectorConfig",
    "MskconnectConnectorKafkaCluster",
    "MskconnectConnectorKafkaClusterApacheKafkaCluster",
    "MskconnectConnectorKafkaClusterApacheKafkaClusterOutputReference",
    "MskconnectConnectorKafkaClusterApacheKafkaClusterVpc",
    "MskconnectConnectorKafkaClusterApacheKafkaClusterVpcOutputReference",
    "MskconnectConnectorKafkaClusterClientAuthentication",
    "MskconnectConnectorKafkaClusterClientAuthenticationOutputReference",
    "MskconnectConnectorKafkaClusterEncryptionInTransit",
    "MskconnectConnectorKafkaClusterEncryptionInTransitOutputReference",
    "MskconnectConnectorKafkaClusterOutputReference",
    "MskconnectConnectorLogDelivery",
    "MskconnectConnectorLogDeliveryOutputReference",
    "MskconnectConnectorLogDeliveryWorkerLogDelivery",
    "MskconnectConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogs",
    "MskconnectConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogsOutputReference",
    "MskconnectConnectorLogDeliveryWorkerLogDeliveryFirehose",
    "MskconnectConnectorLogDeliveryWorkerLogDeliveryFirehoseOutputReference",
    "MskconnectConnectorLogDeliveryWorkerLogDeliveryOutputReference",
    "MskconnectConnectorLogDeliveryWorkerLogDeliveryS3",
    "MskconnectConnectorLogDeliveryWorkerLogDeliveryS3OutputReference",
    "MskconnectConnectorPlugin",
    "MskconnectConnectorPluginCustomPlugin",
    "MskconnectConnectorPluginCustomPluginOutputReference",
    "MskconnectConnectorPluginList",
    "MskconnectConnectorPluginOutputReference",
    "MskconnectConnectorTimeouts",
    "MskconnectConnectorTimeoutsOutputReference",
    "MskconnectConnectorWorkerConfiguration",
    "MskconnectConnectorWorkerConfigurationOutputReference",
]

publication.publish()

def _typecheckingstub__731b2cc0a4fece4ad96ea3cd21295b285a457425f6b2a6cb03971682f7df4d57(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    capacity: typing.Union[MskconnectConnectorCapacity, typing.Dict[builtins.str, typing.Any]],
    connector_configuration: typing.Mapping[builtins.str, builtins.str],
    kafka_cluster: typing.Union[MskconnectConnectorKafkaCluster, typing.Dict[builtins.str, typing.Any]],
    kafka_cluster_client_authentication: typing.Union[MskconnectConnectorKafkaClusterClientAuthentication, typing.Dict[builtins.str, typing.Any]],
    kafka_cluster_encryption_in_transit: typing.Union[MskconnectConnectorKafkaClusterEncryptionInTransit, typing.Dict[builtins.str, typing.Any]],
    kafkaconnect_version: builtins.str,
    name: builtins.str,
    plugin: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[MskconnectConnectorPlugin, typing.Dict[builtins.str, typing.Any]]]],
    service_execution_role_arn: builtins.str,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    log_delivery: typing.Optional[typing.Union[MskconnectConnectorLogDelivery, typing.Dict[builtins.str, typing.Any]]] = None,
    timeouts: typing.Optional[typing.Union[MskconnectConnectorTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    worker_configuration: typing.Optional[typing.Union[MskconnectConnectorWorkerConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__4d5b8e2b7283ed2100a70baec29e68a089626755120a0c3d8f4c48fdbd2c3233(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[MskconnectConnectorPlugin, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ed721e779fad824ffc9d755e143ecd734c1a134f826dcc325e15b6c20fedcc1(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2de3b2e5496dfc94ff42b436da51d11a7ee90d90c0c82f46fedf9c3df10b4d3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f4e73f8fe4d03bb528f6137b49d18e4f8c472179f1b60103001a1fc4ea817d1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e781af06a301f3f951499d72023f8252fff236e70b9febf536ce0f3a54c7def1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1e85fdc3a02bb00e552f36e825716887d49d35f4b758f85cb0fb9680228d85d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60939422ea99eb01df56880c1d9f7a247270a69847818092b00409a51a326987(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f86a17e83f2e45610ae80f94a4c8bf0df5c43bf17f3aa5ed9f19fb68fa8eeb51(
    *,
    autoscaling: typing.Optional[typing.Union[MskconnectConnectorCapacityAutoscaling, typing.Dict[builtins.str, typing.Any]]] = None,
    provisioned_capacity: typing.Optional[typing.Union[MskconnectConnectorCapacityProvisionedCapacity, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e0a65a950591e8000c6b62e4530990c0dc5f4be3cd5a36a998a9b506d1d5ff5(
    *,
    max_worker_count: jsii.Number,
    min_worker_count: jsii.Number,
    mcu_count: typing.Optional[jsii.Number] = None,
    scale_in_policy: typing.Optional[typing.Union[MskconnectConnectorCapacityAutoscalingScaleInPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    scale_out_policy: typing.Optional[typing.Union[MskconnectConnectorCapacityAutoscalingScaleOutPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ee69c1d114b95496bd3b33c2d87288ec25cf3ab681178ee1d38ba652fe1e953(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eff8e5a4da1caba5f6a99c4041a7236f127c13b9496b606280be4b77264cca6a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1343336d40988b626d1cc7a30c3bd1c36d65735d0217adc36c90c6d18517ae4(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22ebc7bf15e8ac726ddace39f724ce144cc43ecec099c65f15c281720fea2de3(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f66d1b196e314c7cba2ff9be44441b67d8a519715eec9de9b115a2517bab2ba(
    value: typing.Optional[MskconnectConnectorCapacityAutoscaling],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4160f8c8fd2afaefcd3710ef1229ff249e7b05f9448f872c6367f55dfc79013(
    *,
    cpu_utilization_percentage: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21f3973036144c28991ae05aaa54e76f3ac65943ae1c7273b7ffaccf89ed35da(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fac08c0fe9f8cf8e61f2711337b5405f60fd5b2f086d2a1a84a4078f45449e7(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2440974937788b93b6be24c9228b2813f55340ee49f6db2c0f49fcadae90f310(
    value: typing.Optional[MskconnectConnectorCapacityAutoscalingScaleInPolicy],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f9510eb743eaabfd750beef734ab348b393aeb404e205494a17d8ff1204980a(
    *,
    cpu_utilization_percentage: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0786b9f33284fb40414a081a56396d13cfc966291ff563ed3f5e20fc53287fed(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a03164d36fcdb1990a299afef26d655b6542f34513e78e4b356d5da9bffc090f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a189b897fed288e1354ca6849dc7223f9e688d09f90a462525ecf47d324863f(
    value: typing.Optional[MskconnectConnectorCapacityAutoscalingScaleOutPolicy],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fda5b717ee3426ff1ab0bf5f6f007b2f84f973dbd863282d9d83e91e359fcf9b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb23d293cbf14f8f413b272f6a99b033ddafa962a965c6a0c27d440f5dae5409(
    value: typing.Optional[MskconnectConnectorCapacity],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ba01fe8ef644460872cbf28a8b37d245d535e64c551eda76be98bb541b38f15(
    *,
    worker_count: jsii.Number,
    mcu_count: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69521a51fd27cbc4e4803030c4fcaa5b3d8f5a684ddaffaad5d8dab596fd47bc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0bbe9859186f4ca7393a0a1283f1ce03ba987b01a547a110e1612517e2af2ac(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5f1a86dc8b4670ec3f0297edc54e4a782768aa5403964a9e0197426e65c3e8d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccc105bafab54dff8094403acfbae8dd377722e4c1ca969726baaf616855054e(
    value: typing.Optional[MskconnectConnectorCapacityProvisionedCapacity],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71f64c8a141f988ea121e2687ac8931bb6e2416b68b4431a63cc784784b8acd0(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    capacity: typing.Union[MskconnectConnectorCapacity, typing.Dict[builtins.str, typing.Any]],
    connector_configuration: typing.Mapping[builtins.str, builtins.str],
    kafka_cluster: typing.Union[MskconnectConnectorKafkaCluster, typing.Dict[builtins.str, typing.Any]],
    kafka_cluster_client_authentication: typing.Union[MskconnectConnectorKafkaClusterClientAuthentication, typing.Dict[builtins.str, typing.Any]],
    kafka_cluster_encryption_in_transit: typing.Union[MskconnectConnectorKafkaClusterEncryptionInTransit, typing.Dict[builtins.str, typing.Any]],
    kafkaconnect_version: builtins.str,
    name: builtins.str,
    plugin: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[MskconnectConnectorPlugin, typing.Dict[builtins.str, typing.Any]]]],
    service_execution_role_arn: builtins.str,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    log_delivery: typing.Optional[typing.Union[MskconnectConnectorLogDelivery, typing.Dict[builtins.str, typing.Any]]] = None,
    timeouts: typing.Optional[typing.Union[MskconnectConnectorTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    worker_configuration: typing.Optional[typing.Union[MskconnectConnectorWorkerConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52c82f0a996f092cf3a4e68b6e46a840fa8ee683051608ac7acf09f69367d6fe(
    *,
    apache_kafka_cluster: typing.Union[MskconnectConnectorKafkaClusterApacheKafkaCluster, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15ccf1283cf46eae4f71ccfa0c0461649c5daaaec1c3b4ec34e78a13e857613e(
    *,
    bootstrap_servers: builtins.str,
    vpc: typing.Union[MskconnectConnectorKafkaClusterApacheKafkaClusterVpc, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__435fa6695b5460c0814284e1bfc1681c4f9a5ec9f583791bdbe48e03f818b183(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e64667c8f71a0980622d8f84548d7a89217e05e4684dcc58bc37a3e7189eead2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd4c882d540e0859db071fb4d8b5369a9f27a90bae48237a119b82810b69a38c(
    value: typing.Optional[MskconnectConnectorKafkaClusterApacheKafkaCluster],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e376f4a959d930e09c3aa29f222a24ec98dc7d16719c930cd487dbf34589a7b(
    *,
    security_groups: typing.Sequence[builtins.str],
    subnets: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4678ae6387dca256e7edf3b623a4cfc4b014e9cddee6a14915d1c87a08b552b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef6efa1afa4b61fa34050d49be31807e44915a01e350c784db53b1d18e93cf7f(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac5cb69ac931c333e85b0e85229afb6b2f724af29d4398edd9eaacb34162dd50(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cfadf4814a3dbef3ed2e0f8c15dec966afba9449d256265e503c5830da62dd8(
    value: typing.Optional[MskconnectConnectorKafkaClusterApacheKafkaClusterVpc],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__028551bd31674e1028d99279f312718f3f841f721f008aa149fc049e922c5759(
    *,
    authentication_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f58e8be57210f4be3a4f2695cc206d21667b42681cee8fc4111ffe38b923be12(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__112bbd00de4d80a4a37b35b67ae989711984cc0e1ae0f56da6a2f194e9f488ae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fef87d7b180a540832c11b20a24d09eadf0eaa1928c5e2683674e16c07a8cd6(
    value: typing.Optional[MskconnectConnectorKafkaClusterClientAuthentication],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3aa5c4e2d730892deead53c5cf14a740cee07a0773a1375d5ca12fec4fe3a3a(
    *,
    encryption_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7a927bc3c267e06d126120a34f7aa8320f0bc683d708a08b7ee672fa6fe481e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42a7f83c3f6e59015fd376f6613beaad367b7e89582d225c35c16cb4959b05a0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41b4ec9797d80a78c049532d725a0404333aef416dba1349e69e6a27d4e4445a(
    value: typing.Optional[MskconnectConnectorKafkaClusterEncryptionInTransit],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3c9ecbfa89a9eeecce83fdea758aa64e6613acbe409599f07d1b30bef18de45(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e7ddecd767b2e12fdafc276889b264ce979f42d8101a7815bbef9117cc5a7b1(
    value: typing.Optional[MskconnectConnectorKafkaCluster],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ff7f414742fed2884cae0b999fe0459ff0180b6a62dd29fc661d9fd78629b80(
    *,
    worker_log_delivery: typing.Union[MskconnectConnectorLogDeliveryWorkerLogDelivery, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__874733c25499655ab09076ff1e3570811879e10b4a006f96e2cfea2a7c15b55d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7f4469fa3540c6fdb0bd46c8d2681952639ad75c340c12004116c2b60e03d31(
    value: typing.Optional[MskconnectConnectorLogDelivery],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5d88f12531316bc0d8833d700b2c10844107602e58a44407e24f90dd7948bb0(
    *,
    cloudwatch_logs: typing.Optional[typing.Union[MskconnectConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogs, typing.Dict[builtins.str, typing.Any]]] = None,
    firehose: typing.Optional[typing.Union[MskconnectConnectorLogDeliveryWorkerLogDeliveryFirehose, typing.Dict[builtins.str, typing.Any]]] = None,
    s3: typing.Optional[typing.Union[MskconnectConnectorLogDeliveryWorkerLogDeliveryS3, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a53c05240f5403589f47ddb332aa996dd7b572fc057ed73d9bf0b362cf5e749b(
    *,
    enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    log_group: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a86844f0ab06926dc0e9be883b73c6b212c5a1e1c29dcf86485629444b97a85(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1173ecf5b3dd3cd6ec295b2459aa9bd9cf2231f07445f62b068c2814983ea08(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6b6559c4993750cb20c89c9b0fe13ae31cfbab9d5f2b526b3ba1a0336f23c79(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9fb374e075145af974828b86d6ca60f47dee72b163fdf017f96e3573ffeae7e(
    value: typing.Optional[MskconnectConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogs],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67c808e5f5ebf9bd2b5b827822bd2d22c15cbce88a6759a66a3cc2b356612365(
    *,
    enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    delivery_stream: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4574ee523db815cad037b894e2e79335b72e042bb9b2f079a011b4c3f513f6c8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f23e05354bb92f06524ecbfc354667ed90142da022a6871ce97cdbc21de7ec2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c19c90ca8141a6e55e3470fc431fb90ca3f7c1f97da0618d8a35c074607c3856(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bed1a0ad66e5bcd7a8dd9d925afd2377cb9c957e38791be638e53a6ed8ef4c8(
    value: typing.Optional[MskconnectConnectorLogDeliveryWorkerLogDeliveryFirehose],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adeb35220a1e30859c7ce3be885b7f8f5e2db4ee16867d1612c11dc7b37ee2d5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87a30d352c55731939fcd73ba77b75409dd9a1fe86d155dc379e200b328acf01(
    value: typing.Optional[MskconnectConnectorLogDeliveryWorkerLogDelivery],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07b8845816c19df3ab60f82e291c4160d553c29d1be701a0f12d1bff36a0504b(
    *,
    enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    bucket: typing.Optional[builtins.str] = None,
    prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d89ad151edf50c91b51f321d30ba58df0207621806601484b7f1a95b043b60f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__061ba98857632196cffade33e7a9e6f4e7f9d38835a313ad95c2af6958946dff(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a43a00271f87f36c926f335f8bce31b35abc2880967b0308714ea7853effb3e(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e789e1934c2a36012217b75f7184724186a2d5d05d793d3cbd0467ee96af16f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26687c3218e56263cfe4823677ae166dc93133266e88505b1521f743da54affe(
    value: typing.Optional[MskconnectConnectorLogDeliveryWorkerLogDeliveryS3],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80d4b75f18f83c6b3973dc8ffa63a4c1aae74345ba58485cc8ac961596f7fa5a(
    *,
    custom_plugin: typing.Union[MskconnectConnectorPluginCustomPlugin, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cda9c5d2d4265663b3247d7c939a1facf52aa57a3e675862067e9622ea2c5a60(
    *,
    arn: builtins.str,
    revision: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d077b0a1d377aa71f26bb389902b3fa9dcb7f3761a79b8be7b3105e2eb47746d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d7db8c5e9844a37d7ee0b90ed7d704824af5ac7d781e6367df579a416394d26(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__681f6fe6acb5399d57e77ae40128a66c313f7590ee0baea2712d04685aa6e515(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3b41183003ab68aaa0a2c047a94d7d46d92aa57d2ff716e6f3e5955607e62af(
    value: typing.Optional[MskconnectConnectorPluginCustomPlugin],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1cea16d9e6fc8d03757067b469e7589f593fbe7e9dabf29b21049dd8e786ea8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65ac5f6bdc973fc847371ffc96f4e2de79908669245765e6b6dd809574a838b2(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1309fbfdfca47c8902e8445274028ec4f0f4ae5fa327c64654810f706c88b7c1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3c39693d53be82aa52be5fbda6ba26a451330242122d2ea76bba41254ab5416(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4dd756b91741234298212769bda4f713d5a761dfd6e518b209feb5e3e0fd84eb(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d69549cf43b1217b3d3cbbacec511c85c68af3a1e104fba318c0a3cd14c7ed9d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MskconnectConnectorPlugin]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f4e9f17b8b9ad325eb7fecd789535a879c5e8a9fbec7a8c31209e5927aa7ba7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a20dc715da39009988e20f9211c4d5fbb4ec151806baf971d4d58081310cf051(
    value: typing.Optional[typing.Union[MskconnectConnectorPlugin, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d810ce3abbca61fd3b587664dd32b2d6545e84ceb18690feeaae8f8dafd3ae9(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a3e4665ede8e1cc8eb056c6b673e32dad90257bef3cf56eba6495b5a4061e67(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87f849088646abd433507fb3daa3888341921a42f02adba69b83ce9046ca757a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ce51ce36b9dd624916e016f6e97f148b9c8e809b5f7453f777ce2c622efeed2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d392bbd15669c10583f2928005acbe7f095797552a437d7f45b3fc5a7960464(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31d6d201f8bb984e158c5bbc1c481231b4e7ed4ede8857167fc113b4ae485506(
    value: typing.Optional[typing.Union[MskconnectConnectorTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cee285e310e02d53261ab51597ca5fa3d05a01284c5e879a70e485ce9cdce4d(
    *,
    arn: builtins.str,
    revision: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0af4b19df54971c47ec63dea436ea114fe108a22b8ce206ad62fd9a3e83f1b9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ec2a93367b78ea1f9c1ff82fb46a2c76ff2fd0c6a51bd758dc40605a58663c7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b719a672b5cd6a960a0c8c1f5108b1b0aeee188c8ff062e266ba54b6200083b0(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cfdd4bf89236c30e50a7d3fec01c2931c0ec1e18bfd5488382ca0ba23d5e7d4(
    value: typing.Optional[MskconnectConnectorWorkerConfiguration],
) -> None:
    """Type checking stubs"""
    pass
