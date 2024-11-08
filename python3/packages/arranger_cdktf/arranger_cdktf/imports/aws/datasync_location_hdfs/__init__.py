'''
# `aws_datasync_location_hdfs`

Refer to the Terraform Registory for docs: [`aws_datasync_location_hdfs`](https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs).
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


class DatasyncLocationHdfs(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.datasyncLocationHdfs.DatasyncLocationHdfs",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs aws_datasync_location_hdfs}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        agent_arns: typing.Sequence[builtins.str],
        name_node: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DatasyncLocationHdfsNameNode", typing.Dict[builtins.str, typing.Any]]]],
        authentication_type: typing.Optional[builtins.str] = None,
        block_size: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        kerberos_keytab: typing.Optional[builtins.str] = None,
        kerberos_krb5_conf: typing.Optional[builtins.str] = None,
        kerberos_principal: typing.Optional[builtins.str] = None,
        kms_key_provider_uri: typing.Optional[builtins.str] = None,
        qop_configuration: typing.Optional[typing.Union["DatasyncLocationHdfsQopConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        replication_factor: typing.Optional[jsii.Number] = None,
        simple_user: typing.Optional[builtins.str] = None,
        subdirectory: typing.Optional[builtins.str] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs aws_datasync_location_hdfs} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param agent_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#agent_arns DatasyncLocationHdfs#agent_arns}.
        :param name_node: name_node block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#name_node DatasyncLocationHdfs#name_node}
        :param authentication_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#authentication_type DatasyncLocationHdfs#authentication_type}.
        :param block_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#block_size DatasyncLocationHdfs#block_size}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#id DatasyncLocationHdfs#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kerberos_keytab: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#kerberos_keytab DatasyncLocationHdfs#kerberos_keytab}.
        :param kerberos_krb5_conf: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#kerberos_krb5_conf DatasyncLocationHdfs#kerberos_krb5_conf}.
        :param kerberos_principal: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#kerberos_principal DatasyncLocationHdfs#kerberos_principal}.
        :param kms_key_provider_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#kms_key_provider_uri DatasyncLocationHdfs#kms_key_provider_uri}.
        :param qop_configuration: qop_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#qop_configuration DatasyncLocationHdfs#qop_configuration}
        :param replication_factor: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#replication_factor DatasyncLocationHdfs#replication_factor}.
        :param simple_user: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#simple_user DatasyncLocationHdfs#simple_user}.
        :param subdirectory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#subdirectory DatasyncLocationHdfs#subdirectory}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#tags DatasyncLocationHdfs#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#tags_all DatasyncLocationHdfs#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae5e7e291327332c4bd66cf1afcee8c993aae47029acc0f6a72feaf50995c9fd)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DatasyncLocationHdfsConfig(
            agent_arns=agent_arns,
            name_node=name_node,
            authentication_type=authentication_type,
            block_size=block_size,
            id=id,
            kerberos_keytab=kerberos_keytab,
            kerberos_krb5_conf=kerberos_krb5_conf,
            kerberos_principal=kerberos_principal,
            kms_key_provider_uri=kms_key_provider_uri,
            qop_configuration=qop_configuration,
            replication_factor=replication_factor,
            simple_user=simple_user,
            subdirectory=subdirectory,
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

    @jsii.member(jsii_name="putNameNode")
    def put_name_node(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DatasyncLocationHdfsNameNode", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1403d0eecf91bccf270a522aed24e1873c9202f028f971b4dda75a77b650ec7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNameNode", [value]))

    @jsii.member(jsii_name="putQopConfiguration")
    def put_qop_configuration(
        self,
        *,
        data_transfer_protection: typing.Optional[builtins.str] = None,
        rpc_protection: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param data_transfer_protection: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#data_transfer_protection DatasyncLocationHdfs#data_transfer_protection}.
        :param rpc_protection: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#rpc_protection DatasyncLocationHdfs#rpc_protection}.
        '''
        value = DatasyncLocationHdfsQopConfiguration(
            data_transfer_protection=data_transfer_protection,
            rpc_protection=rpc_protection,
        )

        return typing.cast(None, jsii.invoke(self, "putQopConfiguration", [value]))

    @jsii.member(jsii_name="resetAuthenticationType")
    def reset_authentication_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthenticationType", []))

    @jsii.member(jsii_name="resetBlockSize")
    def reset_block_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBlockSize", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetKerberosKeytab")
    def reset_kerberos_keytab(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKerberosKeytab", []))

    @jsii.member(jsii_name="resetKerberosKrb5Conf")
    def reset_kerberos_krb5_conf(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKerberosKrb5Conf", []))

    @jsii.member(jsii_name="resetKerberosPrincipal")
    def reset_kerberos_principal(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKerberosPrincipal", []))

    @jsii.member(jsii_name="resetKmsKeyProviderUri")
    def reset_kms_key_provider_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyProviderUri", []))

    @jsii.member(jsii_name="resetQopConfiguration")
    def reset_qop_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQopConfiguration", []))

    @jsii.member(jsii_name="resetReplicationFactor")
    def reset_replication_factor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReplicationFactor", []))

    @jsii.member(jsii_name="resetSimpleUser")
    def reset_simple_user(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSimpleUser", []))

    @jsii.member(jsii_name="resetSubdirectory")
    def reset_subdirectory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubdirectory", []))

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
    @jsii.member(jsii_name="nameNode")
    def name_node(self) -> "DatasyncLocationHdfsNameNodeList":
        return typing.cast("DatasyncLocationHdfsNameNodeList", jsii.get(self, "nameNode"))

    @builtins.property
    @jsii.member(jsii_name="qopConfiguration")
    def qop_configuration(
        self,
    ) -> "DatasyncLocationHdfsQopConfigurationOutputReference":
        return typing.cast("DatasyncLocationHdfsQopConfigurationOutputReference", jsii.get(self, "qopConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="uri")
    def uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uri"))

    @builtins.property
    @jsii.member(jsii_name="agentArnsInput")
    def agent_arns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "agentArnsInput"))

    @builtins.property
    @jsii.member(jsii_name="authenticationTypeInput")
    def authentication_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authenticationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="blockSizeInput")
    def block_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "blockSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="kerberosKeytabInput")
    def kerberos_keytab_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kerberosKeytabInput"))

    @builtins.property
    @jsii.member(jsii_name="kerberosKrb5ConfInput")
    def kerberos_krb5_conf_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kerberosKrb5ConfInput"))

    @builtins.property
    @jsii.member(jsii_name="kerberosPrincipalInput")
    def kerberos_principal_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kerberosPrincipalInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyProviderUriInput")
    def kms_key_provider_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyProviderUriInput"))

    @builtins.property
    @jsii.member(jsii_name="nameNodeInput")
    def name_node_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DatasyncLocationHdfsNameNode"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DatasyncLocationHdfsNameNode"]]], jsii.get(self, "nameNodeInput"))

    @builtins.property
    @jsii.member(jsii_name="qopConfigurationInput")
    def qop_configuration_input(
        self,
    ) -> typing.Optional["DatasyncLocationHdfsQopConfiguration"]:
        return typing.cast(typing.Optional["DatasyncLocationHdfsQopConfiguration"], jsii.get(self, "qopConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="replicationFactorInput")
    def replication_factor_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "replicationFactorInput"))

    @builtins.property
    @jsii.member(jsii_name="simpleUserInput")
    def simple_user_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "simpleUserInput"))

    @builtins.property
    @jsii.member(jsii_name="subdirectoryInput")
    def subdirectory_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subdirectoryInput"))

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
    @jsii.member(jsii_name="agentArns")
    def agent_arns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "agentArns"))

    @agent_arns.setter
    def agent_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__feb496a351b1828dd41a8e070146f2b683690a574d72c92ba4f3bf924240cca2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "agentArns", value)

    @builtins.property
    @jsii.member(jsii_name="authenticationType")
    def authentication_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authenticationType"))

    @authentication_type.setter
    def authentication_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01680b2fb8e1ef3660cee50f64b3e95714d089b5fc1497d75e3b04278b38e984)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authenticationType", value)

    @builtins.property
    @jsii.member(jsii_name="blockSize")
    def block_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "blockSize"))

    @block_size.setter
    def block_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01f6fafd24564140a9dbbd8c3acc39d8ced2e8d912eb3baf40967b38984492c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blockSize", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b96486ebee39e03240efa9fd78f7dfe31a0e1aa4b4fe9bcda43ecd850240e55)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="kerberosKeytab")
    def kerberos_keytab(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kerberosKeytab"))

    @kerberos_keytab.setter
    def kerberos_keytab(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d03b5f43e1c46908b5bfca9a0e56304f7a80aab7f26bc14be27812c7b2fc5b43)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kerberosKeytab", value)

    @builtins.property
    @jsii.member(jsii_name="kerberosKrb5Conf")
    def kerberos_krb5_conf(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kerberosKrb5Conf"))

    @kerberos_krb5_conf.setter
    def kerberos_krb5_conf(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76776d73353aad751edea1ff900ab212427b42052410cb962de2a7e6f2fd308a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kerberosKrb5Conf", value)

    @builtins.property
    @jsii.member(jsii_name="kerberosPrincipal")
    def kerberos_principal(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kerberosPrincipal"))

    @kerberos_principal.setter
    def kerberos_principal(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34035613978062052427787e7cf8c60eacfdd7fe8e2fd7cd25dcb793aa125179)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kerberosPrincipal", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyProviderUri")
    def kms_key_provider_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyProviderUri"))

    @kms_key_provider_uri.setter
    def kms_key_provider_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__011146f8acc6353d18e3ef526467f9d92b8f4506baee31e2eab956ec52db958e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyProviderUri", value)

    @builtins.property
    @jsii.member(jsii_name="replicationFactor")
    def replication_factor(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "replicationFactor"))

    @replication_factor.setter
    def replication_factor(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c853d2c47691e53d1bfcad7c8d4fe1185dec91c358e066356e8e2341b41b2cba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicationFactor", value)

    @builtins.property
    @jsii.member(jsii_name="simpleUser")
    def simple_user(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "simpleUser"))

    @simple_user.setter
    def simple_user(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67172c925cd532cb67c2579bb6db166555e151398c95d2b2b908b7d6ec73da60)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "simpleUser", value)

    @builtins.property
    @jsii.member(jsii_name="subdirectory")
    def subdirectory(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subdirectory"))

    @subdirectory.setter
    def subdirectory(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4d4426b4f78330803df92b60c025ac1dd61b32d62237e24f1fdf6683e46941c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subdirectory", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__677cee85109bb399d1008f1fad7414c3d21f4d8c40e1fe6e0d5ba8bda3bc79c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cee293fedb65ca9fc38afc4dad685bc5d73b957e9ad187a43226187f585d4a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.datasyncLocationHdfs.DatasyncLocationHdfsConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "agent_arns": "agentArns",
        "name_node": "nameNode",
        "authentication_type": "authenticationType",
        "block_size": "blockSize",
        "id": "id",
        "kerberos_keytab": "kerberosKeytab",
        "kerberos_krb5_conf": "kerberosKrb5Conf",
        "kerberos_principal": "kerberosPrincipal",
        "kms_key_provider_uri": "kmsKeyProviderUri",
        "qop_configuration": "qopConfiguration",
        "replication_factor": "replicationFactor",
        "simple_user": "simpleUser",
        "subdirectory": "subdirectory",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class DatasyncLocationHdfsConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        agent_arns: typing.Sequence[builtins.str],
        name_node: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DatasyncLocationHdfsNameNode", typing.Dict[builtins.str, typing.Any]]]],
        authentication_type: typing.Optional[builtins.str] = None,
        block_size: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        kerberos_keytab: typing.Optional[builtins.str] = None,
        kerberos_krb5_conf: typing.Optional[builtins.str] = None,
        kerberos_principal: typing.Optional[builtins.str] = None,
        kms_key_provider_uri: typing.Optional[builtins.str] = None,
        qop_configuration: typing.Optional[typing.Union["DatasyncLocationHdfsQopConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        replication_factor: typing.Optional[jsii.Number] = None,
        simple_user: typing.Optional[builtins.str] = None,
        subdirectory: typing.Optional[builtins.str] = None,
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
        :param agent_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#agent_arns DatasyncLocationHdfs#agent_arns}.
        :param name_node: name_node block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#name_node DatasyncLocationHdfs#name_node}
        :param authentication_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#authentication_type DatasyncLocationHdfs#authentication_type}.
        :param block_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#block_size DatasyncLocationHdfs#block_size}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#id DatasyncLocationHdfs#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kerberos_keytab: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#kerberos_keytab DatasyncLocationHdfs#kerberos_keytab}.
        :param kerberos_krb5_conf: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#kerberos_krb5_conf DatasyncLocationHdfs#kerberos_krb5_conf}.
        :param kerberos_principal: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#kerberos_principal DatasyncLocationHdfs#kerberos_principal}.
        :param kms_key_provider_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#kms_key_provider_uri DatasyncLocationHdfs#kms_key_provider_uri}.
        :param qop_configuration: qop_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#qop_configuration DatasyncLocationHdfs#qop_configuration}
        :param replication_factor: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#replication_factor DatasyncLocationHdfs#replication_factor}.
        :param simple_user: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#simple_user DatasyncLocationHdfs#simple_user}.
        :param subdirectory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#subdirectory DatasyncLocationHdfs#subdirectory}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#tags DatasyncLocationHdfs#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#tags_all DatasyncLocationHdfs#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(qop_configuration, dict):
            qop_configuration = DatasyncLocationHdfsQopConfiguration(**qop_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60125c1276be0720497c7c86810d97311598424c62e26f78bb6a71e467d754a6)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument agent_arns", value=agent_arns, expected_type=type_hints["agent_arns"])
            check_type(argname="argument name_node", value=name_node, expected_type=type_hints["name_node"])
            check_type(argname="argument authentication_type", value=authentication_type, expected_type=type_hints["authentication_type"])
            check_type(argname="argument block_size", value=block_size, expected_type=type_hints["block_size"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument kerberos_keytab", value=kerberos_keytab, expected_type=type_hints["kerberos_keytab"])
            check_type(argname="argument kerberos_krb5_conf", value=kerberos_krb5_conf, expected_type=type_hints["kerberos_krb5_conf"])
            check_type(argname="argument kerberos_principal", value=kerberos_principal, expected_type=type_hints["kerberos_principal"])
            check_type(argname="argument kms_key_provider_uri", value=kms_key_provider_uri, expected_type=type_hints["kms_key_provider_uri"])
            check_type(argname="argument qop_configuration", value=qop_configuration, expected_type=type_hints["qop_configuration"])
            check_type(argname="argument replication_factor", value=replication_factor, expected_type=type_hints["replication_factor"])
            check_type(argname="argument simple_user", value=simple_user, expected_type=type_hints["simple_user"])
            check_type(argname="argument subdirectory", value=subdirectory, expected_type=type_hints["subdirectory"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "agent_arns": agent_arns,
            "name_node": name_node,
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
        if authentication_type is not None:
            self._values["authentication_type"] = authentication_type
        if block_size is not None:
            self._values["block_size"] = block_size
        if id is not None:
            self._values["id"] = id
        if kerberos_keytab is not None:
            self._values["kerberos_keytab"] = kerberos_keytab
        if kerberos_krb5_conf is not None:
            self._values["kerberos_krb5_conf"] = kerberos_krb5_conf
        if kerberos_principal is not None:
            self._values["kerberos_principal"] = kerberos_principal
        if kms_key_provider_uri is not None:
            self._values["kms_key_provider_uri"] = kms_key_provider_uri
        if qop_configuration is not None:
            self._values["qop_configuration"] = qop_configuration
        if replication_factor is not None:
            self._values["replication_factor"] = replication_factor
        if simple_user is not None:
            self._values["simple_user"] = simple_user
        if subdirectory is not None:
            self._values["subdirectory"] = subdirectory
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
    def agent_arns(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#agent_arns DatasyncLocationHdfs#agent_arns}.'''
        result = self._values.get("agent_arns")
        assert result is not None, "Required property 'agent_arns' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def name_node(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DatasyncLocationHdfsNameNode"]]:
        '''name_node block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#name_node DatasyncLocationHdfs#name_node}
        '''
        result = self._values.get("name_node")
        assert result is not None, "Required property 'name_node' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DatasyncLocationHdfsNameNode"]], result)

    @builtins.property
    def authentication_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#authentication_type DatasyncLocationHdfs#authentication_type}.'''
        result = self._values.get("authentication_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def block_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#block_size DatasyncLocationHdfs#block_size}.'''
        result = self._values.get("block_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#id DatasyncLocationHdfs#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kerberos_keytab(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#kerberos_keytab DatasyncLocationHdfs#kerberos_keytab}.'''
        result = self._values.get("kerberos_keytab")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kerberos_krb5_conf(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#kerberos_krb5_conf DatasyncLocationHdfs#kerberos_krb5_conf}.'''
        result = self._values.get("kerberos_krb5_conf")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kerberos_principal(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#kerberos_principal DatasyncLocationHdfs#kerberos_principal}.'''
        result = self._values.get("kerberos_principal")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_provider_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#kms_key_provider_uri DatasyncLocationHdfs#kms_key_provider_uri}.'''
        result = self._values.get("kms_key_provider_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def qop_configuration(
        self,
    ) -> typing.Optional["DatasyncLocationHdfsQopConfiguration"]:
        '''qop_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#qop_configuration DatasyncLocationHdfs#qop_configuration}
        '''
        result = self._values.get("qop_configuration")
        return typing.cast(typing.Optional["DatasyncLocationHdfsQopConfiguration"], result)

    @builtins.property
    def replication_factor(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#replication_factor DatasyncLocationHdfs#replication_factor}.'''
        result = self._values.get("replication_factor")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def simple_user(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#simple_user DatasyncLocationHdfs#simple_user}.'''
        result = self._values.get("simple_user")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subdirectory(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#subdirectory DatasyncLocationHdfs#subdirectory}.'''
        result = self._values.get("subdirectory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#tags DatasyncLocationHdfs#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#tags_all DatasyncLocationHdfs#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatasyncLocationHdfsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.datasyncLocationHdfs.DatasyncLocationHdfsNameNode",
    jsii_struct_bases=[],
    name_mapping={"hostname": "hostname", "port": "port"},
)
class DatasyncLocationHdfsNameNode:
    def __init__(self, *, hostname: builtins.str, port: jsii.Number) -> None:
        '''
        :param hostname: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#hostname DatasyncLocationHdfs#hostname}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#port DatasyncLocationHdfs#port}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2adf2ed859cfe85a8d740fd59fcc12782a2f20674ca6785e881a2fd3f69b30ca)
            check_type(argname="argument hostname", value=hostname, expected_type=type_hints["hostname"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "hostname": hostname,
            "port": port,
        }

    @builtins.property
    def hostname(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#hostname DatasyncLocationHdfs#hostname}.'''
        result = self._values.get("hostname")
        assert result is not None, "Required property 'hostname' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#port DatasyncLocationHdfs#port}.'''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatasyncLocationHdfsNameNode(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatasyncLocationHdfsNameNodeList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.datasyncLocationHdfs.DatasyncLocationHdfsNameNodeList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3bce7813be0b98dd71a3e7afa109c376b0a622e1c6250558c6d75cce88a45527)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DatasyncLocationHdfsNameNodeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75b6d4a6cbbfe349362373a3ca2ef0606f9af901da4c49493a523681855ac474)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DatasyncLocationHdfsNameNodeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91dd8aa726fc619464b37b3fcb2a296188abeaefadb40685f48d843996294c6c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__77c50d1cd3546c8a53f152bd70c3a2cf5774282d6958d6bc5f17540e61b62d43)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ecac463745974e5e041ebf0565ef7fa7858b611bad33ecd587f4067dfeeba397)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatasyncLocationHdfsNameNode]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatasyncLocationHdfsNameNode]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatasyncLocationHdfsNameNode]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c171832e9d3bc92d257e647ad5f8a721beb2b66d5a184c25367ea4c1b41cdbb8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DatasyncLocationHdfsNameNodeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.datasyncLocationHdfs.DatasyncLocationHdfsNameNodeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__651053e99e7d68153a34d920281ef203916b9c4fd90c650917c74e7e16d04a71)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="hostnameInput")
    def hostname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostnameInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="hostname")
    def hostname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostname"))

    @hostname.setter
    def hostname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3953070f5110ee17b900e390d16c6caf32cbf42aa81e1331381ebac7f9caff3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostname", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4df60b0df26779ff204f8280a8aa32904ddc299f8147c9bc99e466146304386f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DatasyncLocationHdfsNameNode, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DatasyncLocationHdfsNameNode, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DatasyncLocationHdfsNameNode, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03b0538b3d887c8a9079fa2184aa9d653604e0dc1130fae1e9c476a45c76038d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.datasyncLocationHdfs.DatasyncLocationHdfsQopConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "data_transfer_protection": "dataTransferProtection",
        "rpc_protection": "rpcProtection",
    },
)
class DatasyncLocationHdfsQopConfiguration:
    def __init__(
        self,
        *,
        data_transfer_protection: typing.Optional[builtins.str] = None,
        rpc_protection: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param data_transfer_protection: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#data_transfer_protection DatasyncLocationHdfs#data_transfer_protection}.
        :param rpc_protection: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#rpc_protection DatasyncLocationHdfs#rpc_protection}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__648bcec24838baa2b2431adecd40e96d1dacf970d01a22b697fc3e58debb5599)
            check_type(argname="argument data_transfer_protection", value=data_transfer_protection, expected_type=type_hints["data_transfer_protection"])
            check_type(argname="argument rpc_protection", value=rpc_protection, expected_type=type_hints["rpc_protection"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if data_transfer_protection is not None:
            self._values["data_transfer_protection"] = data_transfer_protection
        if rpc_protection is not None:
            self._values["rpc_protection"] = rpc_protection

    @builtins.property
    def data_transfer_protection(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#data_transfer_protection DatasyncLocationHdfs#data_transfer_protection}.'''
        result = self._values.get("data_transfer_protection")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rpc_protection(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_hdfs#rpc_protection DatasyncLocationHdfs#rpc_protection}.'''
        result = self._values.get("rpc_protection")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatasyncLocationHdfsQopConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatasyncLocationHdfsQopConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.datasyncLocationHdfs.DatasyncLocationHdfsQopConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4deb2f6e0ed8cdfedb2785c4469a9aeac807bd13928dd4320833eb0a813b485a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDataTransferProtection")
    def reset_data_transfer_protection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataTransferProtection", []))

    @jsii.member(jsii_name="resetRpcProtection")
    def reset_rpc_protection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRpcProtection", []))

    @builtins.property
    @jsii.member(jsii_name="dataTransferProtectionInput")
    def data_transfer_protection_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataTransferProtectionInput"))

    @builtins.property
    @jsii.member(jsii_name="rpcProtectionInput")
    def rpc_protection_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rpcProtectionInput"))

    @builtins.property
    @jsii.member(jsii_name="dataTransferProtection")
    def data_transfer_protection(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataTransferProtection"))

    @data_transfer_protection.setter
    def data_transfer_protection(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b44eb6198e82113241b73eccb3f7f25ae2a313cb2646fdc9696215cc35ea708)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataTransferProtection", value)

    @builtins.property
    @jsii.member(jsii_name="rpcProtection")
    def rpc_protection(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rpcProtection"))

    @rpc_protection.setter
    def rpc_protection(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02c72123eb9ae36bda388c7284320ade7e4caa3d1a7dfb6d971dd4640e987e91)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rpcProtection", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DatasyncLocationHdfsQopConfiguration]:
        return typing.cast(typing.Optional[DatasyncLocationHdfsQopConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatasyncLocationHdfsQopConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f4d25082251b1390fc31d2f574198e684da00dd9dc89381279ec1f8b371d136)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DatasyncLocationHdfs",
    "DatasyncLocationHdfsConfig",
    "DatasyncLocationHdfsNameNode",
    "DatasyncLocationHdfsNameNodeList",
    "DatasyncLocationHdfsNameNodeOutputReference",
    "DatasyncLocationHdfsQopConfiguration",
    "DatasyncLocationHdfsQopConfigurationOutputReference",
]

publication.publish()

def _typecheckingstub__ae5e7e291327332c4bd66cf1afcee8c993aae47029acc0f6a72feaf50995c9fd(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    agent_arns: typing.Sequence[builtins.str],
    name_node: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DatasyncLocationHdfsNameNode, typing.Dict[builtins.str, typing.Any]]]],
    authentication_type: typing.Optional[builtins.str] = None,
    block_size: typing.Optional[jsii.Number] = None,
    id: typing.Optional[builtins.str] = None,
    kerberos_keytab: typing.Optional[builtins.str] = None,
    kerberos_krb5_conf: typing.Optional[builtins.str] = None,
    kerberos_principal: typing.Optional[builtins.str] = None,
    kms_key_provider_uri: typing.Optional[builtins.str] = None,
    qop_configuration: typing.Optional[typing.Union[DatasyncLocationHdfsQopConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    replication_factor: typing.Optional[jsii.Number] = None,
    simple_user: typing.Optional[builtins.str] = None,
    subdirectory: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__b1403d0eecf91bccf270a522aed24e1873c9202f028f971b4dda75a77b650ec7(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DatasyncLocationHdfsNameNode, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__feb496a351b1828dd41a8e070146f2b683690a574d72c92ba4f3bf924240cca2(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01680b2fb8e1ef3660cee50f64b3e95714d089b5fc1497d75e3b04278b38e984(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01f6fafd24564140a9dbbd8c3acc39d8ced2e8d912eb3baf40967b38984492c6(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b96486ebee39e03240efa9fd78f7dfe31a0e1aa4b4fe9bcda43ecd850240e55(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d03b5f43e1c46908b5bfca9a0e56304f7a80aab7f26bc14be27812c7b2fc5b43(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76776d73353aad751edea1ff900ab212427b42052410cb962de2a7e6f2fd308a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34035613978062052427787e7cf8c60eacfdd7fe8e2fd7cd25dcb793aa125179(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__011146f8acc6353d18e3ef526467f9d92b8f4506baee31e2eab956ec52db958e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c853d2c47691e53d1bfcad7c8d4fe1185dec91c358e066356e8e2341b41b2cba(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67172c925cd532cb67c2579bb6db166555e151398c95d2b2b908b7d6ec73da60(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4d4426b4f78330803df92b60c025ac1dd61b32d62237e24f1fdf6683e46941c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__677cee85109bb399d1008f1fad7414c3d21f4d8c40e1fe6e0d5ba8bda3bc79c2(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cee293fedb65ca9fc38afc4dad685bc5d73b957e9ad187a43226187f585d4a2(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60125c1276be0720497c7c86810d97311598424c62e26f78bb6a71e467d754a6(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    agent_arns: typing.Sequence[builtins.str],
    name_node: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DatasyncLocationHdfsNameNode, typing.Dict[builtins.str, typing.Any]]]],
    authentication_type: typing.Optional[builtins.str] = None,
    block_size: typing.Optional[jsii.Number] = None,
    id: typing.Optional[builtins.str] = None,
    kerberos_keytab: typing.Optional[builtins.str] = None,
    kerberos_krb5_conf: typing.Optional[builtins.str] = None,
    kerberos_principal: typing.Optional[builtins.str] = None,
    kms_key_provider_uri: typing.Optional[builtins.str] = None,
    qop_configuration: typing.Optional[typing.Union[DatasyncLocationHdfsQopConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    replication_factor: typing.Optional[jsii.Number] = None,
    simple_user: typing.Optional[builtins.str] = None,
    subdirectory: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2adf2ed859cfe85a8d740fd59fcc12782a2f20674ca6785e881a2fd3f69b30ca(
    *,
    hostname: builtins.str,
    port: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bce7813be0b98dd71a3e7afa109c376b0a622e1c6250558c6d75cce88a45527(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75b6d4a6cbbfe349362373a3ca2ef0606f9af901da4c49493a523681855ac474(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91dd8aa726fc619464b37b3fcb2a296188abeaefadb40685f48d843996294c6c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77c50d1cd3546c8a53f152bd70c3a2cf5774282d6958d6bc5f17540e61b62d43(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecac463745974e5e041ebf0565ef7fa7858b611bad33ecd587f4067dfeeba397(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c171832e9d3bc92d257e647ad5f8a721beb2b66d5a184c25367ea4c1b41cdbb8(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatasyncLocationHdfsNameNode]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__651053e99e7d68153a34d920281ef203916b9c4fd90c650917c74e7e16d04a71(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3953070f5110ee17b900e390d16c6caf32cbf42aa81e1331381ebac7f9caff3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4df60b0df26779ff204f8280a8aa32904ddc299f8147c9bc99e466146304386f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03b0538b3d887c8a9079fa2184aa9d653604e0dc1130fae1e9c476a45c76038d(
    value: typing.Optional[typing.Union[DatasyncLocationHdfsNameNode, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__648bcec24838baa2b2431adecd40e96d1dacf970d01a22b697fc3e58debb5599(
    *,
    data_transfer_protection: typing.Optional[builtins.str] = None,
    rpc_protection: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4deb2f6e0ed8cdfedb2785c4469a9aeac807bd13928dd4320833eb0a813b485a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b44eb6198e82113241b73eccb3f7f25ae2a313cb2646fdc9696215cc35ea708(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02c72123eb9ae36bda388c7284320ade7e4caa3d1a7dfb6d971dd4640e987e91(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f4d25082251b1390fc31d2f574198e684da00dd9dc89381279ec1f8b371d136(
    value: typing.Optional[DatasyncLocationHdfsQopConfiguration],
) -> None:
    """Type checking stubs"""
    pass
