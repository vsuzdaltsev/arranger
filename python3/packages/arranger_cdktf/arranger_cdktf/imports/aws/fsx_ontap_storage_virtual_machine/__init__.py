'''
# `aws_fsx_ontap_storage_virtual_machine`

Refer to the Terraform Registory for docs: [`aws_fsx_ontap_storage_virtual_machine`](https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine).
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


class FsxOntapStorageVirtualMachine(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.fsxOntapStorageVirtualMachine.FsxOntapStorageVirtualMachine",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine aws_fsx_ontap_storage_virtual_machine}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        file_system_id: builtins.str,
        name: builtins.str,
        active_directory_configuration: typing.Optional[typing.Union["FsxOntapStorageVirtualMachineActiveDirectoryConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        root_volume_security_style: typing.Optional[builtins.str] = None,
        svm_admin_password: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["FsxOntapStorageVirtualMachineTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine aws_fsx_ontap_storage_virtual_machine} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param file_system_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#file_system_id FsxOntapStorageVirtualMachine#file_system_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#name FsxOntapStorageVirtualMachine#name}.
        :param active_directory_configuration: active_directory_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#active_directory_configuration FsxOntapStorageVirtualMachine#active_directory_configuration}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#id FsxOntapStorageVirtualMachine#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param root_volume_security_style: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#root_volume_security_style FsxOntapStorageVirtualMachine#root_volume_security_style}.
        :param svm_admin_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#svm_admin_password FsxOntapStorageVirtualMachine#svm_admin_password}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#tags FsxOntapStorageVirtualMachine#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#tags_all FsxOntapStorageVirtualMachine#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#timeouts FsxOntapStorageVirtualMachine#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e24503767bec89896ba921db7eff2320cc7d4def24a486f37c41d78c8a428d9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = FsxOntapStorageVirtualMachineConfig(
            file_system_id=file_system_id,
            name=name,
            active_directory_configuration=active_directory_configuration,
            id=id,
            root_volume_security_style=root_volume_security_style,
            svm_admin_password=svm_admin_password,
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

    @jsii.member(jsii_name="putActiveDirectoryConfiguration")
    def put_active_directory_configuration(
        self,
        *,
        netbios_name: typing.Optional[builtins.str] = None,
        self_managed_active_directory_configuration: typing.Optional[typing.Union["FsxOntapStorageVirtualMachineActiveDirectoryConfigurationSelfManagedActiveDirectoryConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param netbios_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#netbios_name FsxOntapStorageVirtualMachine#netbios_name}.
        :param self_managed_active_directory_configuration: self_managed_active_directory_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#self_managed_active_directory_configuration FsxOntapStorageVirtualMachine#self_managed_active_directory_configuration}
        '''
        value = FsxOntapStorageVirtualMachineActiveDirectoryConfiguration(
            netbios_name=netbios_name,
            self_managed_active_directory_configuration=self_managed_active_directory_configuration,
        )

        return typing.cast(None, jsii.invoke(self, "putActiveDirectoryConfiguration", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#create FsxOntapStorageVirtualMachine#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#delete FsxOntapStorageVirtualMachine#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#update FsxOntapStorageVirtualMachine#update}.
        '''
        value = FsxOntapStorageVirtualMachineTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetActiveDirectoryConfiguration")
    def reset_active_directory_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActiveDirectoryConfiguration", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetRootVolumeSecurityStyle")
    def reset_root_volume_security_style(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRootVolumeSecurityStyle", []))

    @jsii.member(jsii_name="resetSvmAdminPassword")
    def reset_svm_admin_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSvmAdminPassword", []))

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
    @jsii.member(jsii_name="activeDirectoryConfiguration")
    def active_directory_configuration(
        self,
    ) -> "FsxOntapStorageVirtualMachineActiveDirectoryConfigurationOutputReference":
        return typing.cast("FsxOntapStorageVirtualMachineActiveDirectoryConfigurationOutputReference", jsii.get(self, "activeDirectoryConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="endpoints")
    def endpoints(self) -> "FsxOntapStorageVirtualMachineEndpointsList":
        return typing.cast("FsxOntapStorageVirtualMachineEndpointsList", jsii.get(self, "endpoints"))

    @builtins.property
    @jsii.member(jsii_name="subtype")
    def subtype(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subtype"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "FsxOntapStorageVirtualMachineTimeoutsOutputReference":
        return typing.cast("FsxOntapStorageVirtualMachineTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="uuid")
    def uuid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uuid"))

    @builtins.property
    @jsii.member(jsii_name="activeDirectoryConfigurationInput")
    def active_directory_configuration_input(
        self,
    ) -> typing.Optional["FsxOntapStorageVirtualMachineActiveDirectoryConfiguration"]:
        return typing.cast(typing.Optional["FsxOntapStorageVirtualMachineActiveDirectoryConfiguration"], jsii.get(self, "activeDirectoryConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="fileSystemIdInput")
    def file_system_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileSystemIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="rootVolumeSecurityStyleInput")
    def root_volume_security_style_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rootVolumeSecurityStyleInput"))

    @builtins.property
    @jsii.member(jsii_name="svmAdminPasswordInput")
    def svm_admin_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "svmAdminPasswordInput"))

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
    ) -> typing.Optional[typing.Union["FsxOntapStorageVirtualMachineTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["FsxOntapStorageVirtualMachineTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="fileSystemId")
    def file_system_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileSystemId"))

    @file_system_id.setter
    def file_system_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cebf8966d4379c4a0894fd76452230c1ee8ea05cbb4ad7f1411571080611df4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileSystemId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__952b856fea820c1eb05d8e39a232a0a3ab6dbf5dae93e2df74eda54580a81b9e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4cac4dae35b5d7206e9cbea3f82f6fa5e79737ce83e4b3c924a1c4f444b1ab76)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="rootVolumeSecurityStyle")
    def root_volume_security_style(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rootVolumeSecurityStyle"))

    @root_volume_security_style.setter
    def root_volume_security_style(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44329d02ab3ad5b04e2e89772b28edd78a9ebe8ed8abdf1ef1b909882c0608be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rootVolumeSecurityStyle", value)

    @builtins.property
    @jsii.member(jsii_name="svmAdminPassword")
    def svm_admin_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "svmAdminPassword"))

    @svm_admin_password.setter
    def svm_admin_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db2c89dbe4b7f916838f0291fdd4d076dd095b4049e21a98b93a77bfec717c06)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "svmAdminPassword", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55de663d8cae95378448d409806ee1c49d1bc051d365166e782c8f43fa87dd7f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73cfedb958dcd7f875a2321725b093024347d296645e4d33ddcdde6617f03a42)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.fsxOntapStorageVirtualMachine.FsxOntapStorageVirtualMachineActiveDirectoryConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "netbios_name": "netbiosName",
        "self_managed_active_directory_configuration": "selfManagedActiveDirectoryConfiguration",
    },
)
class FsxOntapStorageVirtualMachineActiveDirectoryConfiguration:
    def __init__(
        self,
        *,
        netbios_name: typing.Optional[builtins.str] = None,
        self_managed_active_directory_configuration: typing.Optional[typing.Union["FsxOntapStorageVirtualMachineActiveDirectoryConfigurationSelfManagedActiveDirectoryConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param netbios_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#netbios_name FsxOntapStorageVirtualMachine#netbios_name}.
        :param self_managed_active_directory_configuration: self_managed_active_directory_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#self_managed_active_directory_configuration FsxOntapStorageVirtualMachine#self_managed_active_directory_configuration}
        '''
        if isinstance(self_managed_active_directory_configuration, dict):
            self_managed_active_directory_configuration = FsxOntapStorageVirtualMachineActiveDirectoryConfigurationSelfManagedActiveDirectoryConfiguration(**self_managed_active_directory_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e87cf9307342280e2c601104cd57c9a287751345fe7be896798d403b339a8cf1)
            check_type(argname="argument netbios_name", value=netbios_name, expected_type=type_hints["netbios_name"])
            check_type(argname="argument self_managed_active_directory_configuration", value=self_managed_active_directory_configuration, expected_type=type_hints["self_managed_active_directory_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if netbios_name is not None:
            self._values["netbios_name"] = netbios_name
        if self_managed_active_directory_configuration is not None:
            self._values["self_managed_active_directory_configuration"] = self_managed_active_directory_configuration

    @builtins.property
    def netbios_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#netbios_name FsxOntapStorageVirtualMachine#netbios_name}.'''
        result = self._values.get("netbios_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def self_managed_active_directory_configuration(
        self,
    ) -> typing.Optional["FsxOntapStorageVirtualMachineActiveDirectoryConfigurationSelfManagedActiveDirectoryConfiguration"]:
        '''self_managed_active_directory_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#self_managed_active_directory_configuration FsxOntapStorageVirtualMachine#self_managed_active_directory_configuration}
        '''
        result = self._values.get("self_managed_active_directory_configuration")
        return typing.cast(typing.Optional["FsxOntapStorageVirtualMachineActiveDirectoryConfigurationSelfManagedActiveDirectoryConfiguration"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FsxOntapStorageVirtualMachineActiveDirectoryConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FsxOntapStorageVirtualMachineActiveDirectoryConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.fsxOntapStorageVirtualMachine.FsxOntapStorageVirtualMachineActiveDirectoryConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__28dcc6a910b39d2aed5d7a34c41bc3f36dc3df299387e693719c12b740b9eca1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSelfManagedActiveDirectoryConfiguration")
    def put_self_managed_active_directory_configuration(
        self,
        *,
        dns_ips: typing.Sequence[builtins.str],
        domain_name: builtins.str,
        password: builtins.str,
        username: builtins.str,
        file_system_administrators_group: typing.Optional[builtins.str] = None,
        organizational_unit_distinguished_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param dns_ips: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#dns_ips FsxOntapStorageVirtualMachine#dns_ips}.
        :param domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#domain_name FsxOntapStorageVirtualMachine#domain_name}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#password FsxOntapStorageVirtualMachine#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#username FsxOntapStorageVirtualMachine#username}.
        :param file_system_administrators_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#file_system_administrators_group FsxOntapStorageVirtualMachine#file_system_administrators_group}.
        :param organizational_unit_distinguished_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#organizational_unit_distinguished_name FsxOntapStorageVirtualMachine#organizational_unit_distinguished_name}.
        '''
        value = FsxOntapStorageVirtualMachineActiveDirectoryConfigurationSelfManagedActiveDirectoryConfiguration(
            dns_ips=dns_ips,
            domain_name=domain_name,
            password=password,
            username=username,
            file_system_administrators_group=file_system_administrators_group,
            organizational_unit_distinguished_name=organizational_unit_distinguished_name,
        )

        return typing.cast(None, jsii.invoke(self, "putSelfManagedActiveDirectoryConfiguration", [value]))

    @jsii.member(jsii_name="resetNetbiosName")
    def reset_netbios_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetbiosName", []))

    @jsii.member(jsii_name="resetSelfManagedActiveDirectoryConfiguration")
    def reset_self_managed_active_directory_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSelfManagedActiveDirectoryConfiguration", []))

    @builtins.property
    @jsii.member(jsii_name="selfManagedActiveDirectoryConfiguration")
    def self_managed_active_directory_configuration(
        self,
    ) -> "FsxOntapStorageVirtualMachineActiveDirectoryConfigurationSelfManagedActiveDirectoryConfigurationOutputReference":
        return typing.cast("FsxOntapStorageVirtualMachineActiveDirectoryConfigurationSelfManagedActiveDirectoryConfigurationOutputReference", jsii.get(self, "selfManagedActiveDirectoryConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="netbiosNameInput")
    def netbios_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "netbiosNameInput"))

    @builtins.property
    @jsii.member(jsii_name="selfManagedActiveDirectoryConfigurationInput")
    def self_managed_active_directory_configuration_input(
        self,
    ) -> typing.Optional["FsxOntapStorageVirtualMachineActiveDirectoryConfigurationSelfManagedActiveDirectoryConfiguration"]:
        return typing.cast(typing.Optional["FsxOntapStorageVirtualMachineActiveDirectoryConfigurationSelfManagedActiveDirectoryConfiguration"], jsii.get(self, "selfManagedActiveDirectoryConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="netbiosName")
    def netbios_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "netbiosName"))

    @netbios_name.setter
    def netbios_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8cdb472f19f55a4fac799ba267ede6335a76778315ad9562737c205116399366)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "netbiosName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[FsxOntapStorageVirtualMachineActiveDirectoryConfiguration]:
        return typing.cast(typing.Optional[FsxOntapStorageVirtualMachineActiveDirectoryConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[FsxOntapStorageVirtualMachineActiveDirectoryConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d5b98516af425040761a9690453d4de7780f5d0f2c4bfc52eb93619507b3454)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.fsxOntapStorageVirtualMachine.FsxOntapStorageVirtualMachineActiveDirectoryConfigurationSelfManagedActiveDirectoryConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "dns_ips": "dnsIps",
        "domain_name": "domainName",
        "password": "password",
        "username": "username",
        "file_system_administrators_group": "fileSystemAdministratorsGroup",
        "organizational_unit_distinguished_name": "organizationalUnitDistinguishedName",
    },
)
class FsxOntapStorageVirtualMachineActiveDirectoryConfigurationSelfManagedActiveDirectoryConfiguration:
    def __init__(
        self,
        *,
        dns_ips: typing.Sequence[builtins.str],
        domain_name: builtins.str,
        password: builtins.str,
        username: builtins.str,
        file_system_administrators_group: typing.Optional[builtins.str] = None,
        organizational_unit_distinguished_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param dns_ips: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#dns_ips FsxOntapStorageVirtualMachine#dns_ips}.
        :param domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#domain_name FsxOntapStorageVirtualMachine#domain_name}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#password FsxOntapStorageVirtualMachine#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#username FsxOntapStorageVirtualMachine#username}.
        :param file_system_administrators_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#file_system_administrators_group FsxOntapStorageVirtualMachine#file_system_administrators_group}.
        :param organizational_unit_distinguished_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#organizational_unit_distinguished_name FsxOntapStorageVirtualMachine#organizational_unit_distinguished_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a6dc31b6e7b05ba5cdff3c1a6a4f079c7b2a43a223a57d58b9f69242010cc9c)
            check_type(argname="argument dns_ips", value=dns_ips, expected_type=type_hints["dns_ips"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument file_system_administrators_group", value=file_system_administrators_group, expected_type=type_hints["file_system_administrators_group"])
            check_type(argname="argument organizational_unit_distinguished_name", value=organizational_unit_distinguished_name, expected_type=type_hints["organizational_unit_distinguished_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dns_ips": dns_ips,
            "domain_name": domain_name,
            "password": password,
            "username": username,
        }
        if file_system_administrators_group is not None:
            self._values["file_system_administrators_group"] = file_system_administrators_group
        if organizational_unit_distinguished_name is not None:
            self._values["organizational_unit_distinguished_name"] = organizational_unit_distinguished_name

    @builtins.property
    def dns_ips(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#dns_ips FsxOntapStorageVirtualMachine#dns_ips}.'''
        result = self._values.get("dns_ips")
        assert result is not None, "Required property 'dns_ips' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#domain_name FsxOntapStorageVirtualMachine#domain_name}.'''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#password FsxOntapStorageVirtualMachine#password}.'''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#username FsxOntapStorageVirtualMachine#username}.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def file_system_administrators_group(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#file_system_administrators_group FsxOntapStorageVirtualMachine#file_system_administrators_group}.'''
        result = self._values.get("file_system_administrators_group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def organizational_unit_distinguished_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#organizational_unit_distinguished_name FsxOntapStorageVirtualMachine#organizational_unit_distinguished_name}.'''
        result = self._values.get("organizational_unit_distinguished_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FsxOntapStorageVirtualMachineActiveDirectoryConfigurationSelfManagedActiveDirectoryConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FsxOntapStorageVirtualMachineActiveDirectoryConfigurationSelfManagedActiveDirectoryConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.fsxOntapStorageVirtualMachine.FsxOntapStorageVirtualMachineActiveDirectoryConfigurationSelfManagedActiveDirectoryConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d6232fb6e15d3ac8c7565eac0f41ecee9df8fc43f49aa0bafa54f57f447dfce0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFileSystemAdministratorsGroup")
    def reset_file_system_administrators_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileSystemAdministratorsGroup", []))

    @jsii.member(jsii_name="resetOrganizationalUnitDistinguishedName")
    def reset_organizational_unit_distinguished_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrganizationalUnitDistinguishedName", []))

    @builtins.property
    @jsii.member(jsii_name="dnsIpsInput")
    def dns_ips_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dnsIpsInput"))

    @builtins.property
    @jsii.member(jsii_name="domainNameInput")
    def domain_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainNameInput"))

    @builtins.property
    @jsii.member(jsii_name="fileSystemAdministratorsGroupInput")
    def file_system_administrators_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileSystemAdministratorsGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="organizationalUnitDistinguishedNameInput")
    def organizational_unit_distinguished_name_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "organizationalUnitDistinguishedNameInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsIps")
    def dns_ips(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "dnsIps"))

    @dns_ips.setter
    def dns_ips(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8608ffedaed4a39270cafa59f5e83f7eb27b425dd8a2059f8b9d3ed303a1f24)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dnsIps", value)

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31da3a337e3601a5449b8749fe228d24435f74fa93d245600591ec0aa5752394)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value)

    @builtins.property
    @jsii.member(jsii_name="fileSystemAdministratorsGroup")
    def file_system_administrators_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileSystemAdministratorsGroup"))

    @file_system_administrators_group.setter
    def file_system_administrators_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4f9ab97ec96800753b62f9077ba39ef3ab12a3fa97b54f3165abd61fbf5baa4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileSystemAdministratorsGroup", value)

    @builtins.property
    @jsii.member(jsii_name="organizationalUnitDistinguishedName")
    def organizational_unit_distinguished_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "organizationalUnitDistinguishedName"))

    @organizational_unit_distinguished_name.setter
    def organizational_unit_distinguished_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c5d9b17c04eecc2e3de6eada2d2b807fb62c98aad4ed7f69f71b7f34d9afba4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organizationalUnitDistinguishedName", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c40ce387ae96e4e20ea2c0f3552d2baed1ab65bef96d730beedffabf96d2809)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c12970badbebc3b0a0cf60d5f7eeba1f9d6ba923884932468c052f9829be72d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[FsxOntapStorageVirtualMachineActiveDirectoryConfigurationSelfManagedActiveDirectoryConfiguration]:
        return typing.cast(typing.Optional[FsxOntapStorageVirtualMachineActiveDirectoryConfigurationSelfManagedActiveDirectoryConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[FsxOntapStorageVirtualMachineActiveDirectoryConfigurationSelfManagedActiveDirectoryConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80931f87bca653761681da869184f3b695b6ab5a1865774a59f90225bf6e440b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.fsxOntapStorageVirtualMachine.FsxOntapStorageVirtualMachineConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "file_system_id": "fileSystemId",
        "name": "name",
        "active_directory_configuration": "activeDirectoryConfiguration",
        "id": "id",
        "root_volume_security_style": "rootVolumeSecurityStyle",
        "svm_admin_password": "svmAdminPassword",
        "tags": "tags",
        "tags_all": "tagsAll",
        "timeouts": "timeouts",
    },
)
class FsxOntapStorageVirtualMachineConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        file_system_id: builtins.str,
        name: builtins.str,
        active_directory_configuration: typing.Optional[typing.Union[FsxOntapStorageVirtualMachineActiveDirectoryConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        root_volume_security_style: typing.Optional[builtins.str] = None,
        svm_admin_password: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["FsxOntapStorageVirtualMachineTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param file_system_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#file_system_id FsxOntapStorageVirtualMachine#file_system_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#name FsxOntapStorageVirtualMachine#name}.
        :param active_directory_configuration: active_directory_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#active_directory_configuration FsxOntapStorageVirtualMachine#active_directory_configuration}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#id FsxOntapStorageVirtualMachine#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param root_volume_security_style: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#root_volume_security_style FsxOntapStorageVirtualMachine#root_volume_security_style}.
        :param svm_admin_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#svm_admin_password FsxOntapStorageVirtualMachine#svm_admin_password}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#tags FsxOntapStorageVirtualMachine#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#tags_all FsxOntapStorageVirtualMachine#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#timeouts FsxOntapStorageVirtualMachine#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(active_directory_configuration, dict):
            active_directory_configuration = FsxOntapStorageVirtualMachineActiveDirectoryConfiguration(**active_directory_configuration)
        if isinstance(timeouts, dict):
            timeouts = FsxOntapStorageVirtualMachineTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b356cf1aa012577f7c0042d0f5f04c569658eb14b8c08088d84f52e0c141697d)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument file_system_id", value=file_system_id, expected_type=type_hints["file_system_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument active_directory_configuration", value=active_directory_configuration, expected_type=type_hints["active_directory_configuration"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument root_volume_security_style", value=root_volume_security_style, expected_type=type_hints["root_volume_security_style"])
            check_type(argname="argument svm_admin_password", value=svm_admin_password, expected_type=type_hints["svm_admin_password"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "file_system_id": file_system_id,
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
        if active_directory_configuration is not None:
            self._values["active_directory_configuration"] = active_directory_configuration
        if id is not None:
            self._values["id"] = id
        if root_volume_security_style is not None:
            self._values["root_volume_security_style"] = root_volume_security_style
        if svm_admin_password is not None:
            self._values["svm_admin_password"] = svm_admin_password
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
    def file_system_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#file_system_id FsxOntapStorageVirtualMachine#file_system_id}.'''
        result = self._values.get("file_system_id")
        assert result is not None, "Required property 'file_system_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#name FsxOntapStorageVirtualMachine#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def active_directory_configuration(
        self,
    ) -> typing.Optional[FsxOntapStorageVirtualMachineActiveDirectoryConfiguration]:
        '''active_directory_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#active_directory_configuration FsxOntapStorageVirtualMachine#active_directory_configuration}
        '''
        result = self._values.get("active_directory_configuration")
        return typing.cast(typing.Optional[FsxOntapStorageVirtualMachineActiveDirectoryConfiguration], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#id FsxOntapStorageVirtualMachine#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def root_volume_security_style(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#root_volume_security_style FsxOntapStorageVirtualMachine#root_volume_security_style}.'''
        result = self._values.get("root_volume_security_style")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def svm_admin_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#svm_admin_password FsxOntapStorageVirtualMachine#svm_admin_password}.'''
        result = self._values.get("svm_admin_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#tags FsxOntapStorageVirtualMachine#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#tags_all FsxOntapStorageVirtualMachine#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["FsxOntapStorageVirtualMachineTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#timeouts FsxOntapStorageVirtualMachine#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["FsxOntapStorageVirtualMachineTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FsxOntapStorageVirtualMachineConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.fsxOntapStorageVirtualMachine.FsxOntapStorageVirtualMachineEndpoints",
    jsii_struct_bases=[],
    name_mapping={},
)
class FsxOntapStorageVirtualMachineEndpoints:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FsxOntapStorageVirtualMachineEndpoints(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.fsxOntapStorageVirtualMachine.FsxOntapStorageVirtualMachineEndpointsIscsi",
    jsii_struct_bases=[],
    name_mapping={},
)
class FsxOntapStorageVirtualMachineEndpointsIscsi:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FsxOntapStorageVirtualMachineEndpointsIscsi(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FsxOntapStorageVirtualMachineEndpointsIscsiList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.fsxOntapStorageVirtualMachine.FsxOntapStorageVirtualMachineEndpointsIscsiList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__62d5babce06e10b739314402c0c686dc540a1464c1e13d444db16a34ced3f8a9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "FsxOntapStorageVirtualMachineEndpointsIscsiOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef5340063bfdcc52d421405ba7cf20ae602e569f909d13eaf583b75edef5367a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("FsxOntapStorageVirtualMachineEndpointsIscsiOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de064815fafadda224f83a05d885ed8d3191c657bad0f784852ad946621a5ede)
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
            type_hints = typing.get_type_hints(_typecheckingstub__71e162e2b503700490bf2b8aafada95099c79d9fa4963850572756c6984a7742)
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
            type_hints = typing.get_type_hints(_typecheckingstub__08ba1e6ae7175a8bac6e52bc9c1d4d249097c10dddf61b0b1d8748f8a3153918)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class FsxOntapStorageVirtualMachineEndpointsIscsiOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.fsxOntapStorageVirtualMachine.FsxOntapStorageVirtualMachineEndpointsIscsiOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7f0312d6a08750dbe32fa33d6d814951bbb6a6f35f1cd691aa0010ca7e365285)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="dnsName")
    def dns_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dnsName"))

    @builtins.property
    @jsii.member(jsii_name="ipAddresses")
    def ip_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ipAddresses"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[FsxOntapStorageVirtualMachineEndpointsIscsi]:
        return typing.cast(typing.Optional[FsxOntapStorageVirtualMachineEndpointsIscsi], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[FsxOntapStorageVirtualMachineEndpointsIscsi],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf45ec6bfe7e7da8fd4ceb5c4b8fd9d1ab05d3d0092d72c239c2212c44d33101)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class FsxOntapStorageVirtualMachineEndpointsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.fsxOntapStorageVirtualMachine.FsxOntapStorageVirtualMachineEndpointsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ea1c02865352f3ded9732066a790c36f15d74fbee9e210b4b30dd2cb725c3f0a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "FsxOntapStorageVirtualMachineEndpointsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__399d9414a279cacf21a5581370f1e9fa6da1e7cb8b6485582d69300d705adc8e)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("FsxOntapStorageVirtualMachineEndpointsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b69569fd512072be947e4a5c844be867cad201cd2e01cc9ebc4870851e85b2e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__043a4f85015969a76df68a8b50c5241369ba36385dce72a60d8be5fc4eda052c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a023d762790147c6650ff2910a7d90be1c1b63fd33863f5eeb150a128f5473f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


@jsii.data_type(
    jsii_type="aws.fsxOntapStorageVirtualMachine.FsxOntapStorageVirtualMachineEndpointsManagement",
    jsii_struct_bases=[],
    name_mapping={},
)
class FsxOntapStorageVirtualMachineEndpointsManagement:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FsxOntapStorageVirtualMachineEndpointsManagement(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FsxOntapStorageVirtualMachineEndpointsManagementList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.fsxOntapStorageVirtualMachine.FsxOntapStorageVirtualMachineEndpointsManagementList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3aa108e72450a03f2cfdeb09c74f6a9eedd4bdb751eeaabd7a5b4d831269dba9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "FsxOntapStorageVirtualMachineEndpointsManagementOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26a44af4166c978fac92f76ad0a6a1b89e92059e20a17287e0547ee5e76a084f)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("FsxOntapStorageVirtualMachineEndpointsManagementOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a06e21efd8cf71ffd12130ba012fb726eac92505e00a014593adf1e61aea53db)
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
            type_hints = typing.get_type_hints(_typecheckingstub__24430048f5c0074e9277a335429aac57d2df1187ef5a5ac3b8b6da806af3c832)
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
            type_hints = typing.get_type_hints(_typecheckingstub__df3371de1866ddfca8d9b7f302ed66460eb050ac54ce033693c84a3489e6d83c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class FsxOntapStorageVirtualMachineEndpointsManagementOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.fsxOntapStorageVirtualMachine.FsxOntapStorageVirtualMachineEndpointsManagementOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__33d4ae0d1a4dc3a840ca7c1863de2575d68ad1785444f10a61cf20feb731cee0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="dnsName")
    def dns_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dnsName"))

    @builtins.property
    @jsii.member(jsii_name="ipAddresses")
    def ip_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ipAddresses"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[FsxOntapStorageVirtualMachineEndpointsManagement]:
        return typing.cast(typing.Optional[FsxOntapStorageVirtualMachineEndpointsManagement], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[FsxOntapStorageVirtualMachineEndpointsManagement],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32bb7b3a779dfd0ccc8e72484c2f21014fea33e198379735c8a78fc887d4cee5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.fsxOntapStorageVirtualMachine.FsxOntapStorageVirtualMachineEndpointsNfs",
    jsii_struct_bases=[],
    name_mapping={},
)
class FsxOntapStorageVirtualMachineEndpointsNfs:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FsxOntapStorageVirtualMachineEndpointsNfs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FsxOntapStorageVirtualMachineEndpointsNfsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.fsxOntapStorageVirtualMachine.FsxOntapStorageVirtualMachineEndpointsNfsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0cf2d7798f90b768ee839173e21864aa3022f70606bc15bf2f25ec93f3e1583c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "FsxOntapStorageVirtualMachineEndpointsNfsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bdaecd300f676f85b8fe21f557617f73f63e5d0108b7ff70cb028c09c97ad687)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("FsxOntapStorageVirtualMachineEndpointsNfsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d885a1fe1d425d1e8b35efc6cd530d2920725fa3075f9a7a18b32cba4b876860)
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
            type_hints = typing.get_type_hints(_typecheckingstub__78415870258f49fa95e62fcb738f0da7dcaa1dd5b440593a935bb10fcc46772a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__54e7f6edfdcc176cf9a91d5b44201acf553529351b986df8096bc9d7d2808079)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class FsxOntapStorageVirtualMachineEndpointsNfsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.fsxOntapStorageVirtualMachine.FsxOntapStorageVirtualMachineEndpointsNfsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__423fe838f88ef436e5490fc10fa85b2ef45d6ead45ea390f61c304c69aea4ea7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="dnsName")
    def dns_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dnsName"))

    @builtins.property
    @jsii.member(jsii_name="ipAddresses")
    def ip_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ipAddresses"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[FsxOntapStorageVirtualMachineEndpointsNfs]:
        return typing.cast(typing.Optional[FsxOntapStorageVirtualMachineEndpointsNfs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[FsxOntapStorageVirtualMachineEndpointsNfs],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d95dba46696148419ffcb7c62fdabf1e35cd5d11bdf3533e4d16ceed7a76d2f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class FsxOntapStorageVirtualMachineEndpointsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.fsxOntapStorageVirtualMachine.FsxOntapStorageVirtualMachineEndpointsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d13485242fb0089ff89889424cca33ad4b5191d68416063075ba58e1921634fc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="iscsi")
    def iscsi(self) -> FsxOntapStorageVirtualMachineEndpointsIscsiList:
        return typing.cast(FsxOntapStorageVirtualMachineEndpointsIscsiList, jsii.get(self, "iscsi"))

    @builtins.property
    @jsii.member(jsii_name="management")
    def management(self) -> FsxOntapStorageVirtualMachineEndpointsManagementList:
        return typing.cast(FsxOntapStorageVirtualMachineEndpointsManagementList, jsii.get(self, "management"))

    @builtins.property
    @jsii.member(jsii_name="nfs")
    def nfs(self) -> FsxOntapStorageVirtualMachineEndpointsNfsList:
        return typing.cast(FsxOntapStorageVirtualMachineEndpointsNfsList, jsii.get(self, "nfs"))

    @builtins.property
    @jsii.member(jsii_name="smb")
    def smb(self) -> "FsxOntapStorageVirtualMachineEndpointsSmbList":
        return typing.cast("FsxOntapStorageVirtualMachineEndpointsSmbList", jsii.get(self, "smb"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[FsxOntapStorageVirtualMachineEndpoints]:
        return typing.cast(typing.Optional[FsxOntapStorageVirtualMachineEndpoints], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[FsxOntapStorageVirtualMachineEndpoints],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd827a34a1ffa6d1f8645e2b9ded7ff42effe9bb66a7d8d111083dd2c9137078)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.fsxOntapStorageVirtualMachine.FsxOntapStorageVirtualMachineEndpointsSmb",
    jsii_struct_bases=[],
    name_mapping={},
)
class FsxOntapStorageVirtualMachineEndpointsSmb:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FsxOntapStorageVirtualMachineEndpointsSmb(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FsxOntapStorageVirtualMachineEndpointsSmbList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.fsxOntapStorageVirtualMachine.FsxOntapStorageVirtualMachineEndpointsSmbList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__daabe2d8cdc97ce4e1bf696d77a5618ec0f1d16773ad262ccbbce99baf38ab10)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "FsxOntapStorageVirtualMachineEndpointsSmbOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e987ac0fa2eb3732896170ee9ecb74f390644a5a0eda3e2c9f2bd9d589a3d26)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("FsxOntapStorageVirtualMachineEndpointsSmbOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__543f49278af3ac0a846f5f04f9b19b869a62acb5ba3bbf65e77547de70c2dee6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bedbb18fffe4462a6828c7f90a2f46eaf9d80859a31823af7160650489cea8f9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f2075e324816635e1c1d78279b270746c0035b0802dc02616d4ce5f25f3e501b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class FsxOntapStorageVirtualMachineEndpointsSmbOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.fsxOntapStorageVirtualMachine.FsxOntapStorageVirtualMachineEndpointsSmbOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__442b77be9d0a98a6b64eb54eebdd0d1e4e7d2731909c3555bbcd266588862ab4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="dnsName")
    def dns_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dnsName"))

    @builtins.property
    @jsii.member(jsii_name="ipAddresses")
    def ip_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ipAddresses"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[FsxOntapStorageVirtualMachineEndpointsSmb]:
        return typing.cast(typing.Optional[FsxOntapStorageVirtualMachineEndpointsSmb], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[FsxOntapStorageVirtualMachineEndpointsSmb],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca405f10f2145e9de5c3a849cd1e13ccf6f55d89c4686500a98306d9906dd7ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.fsxOntapStorageVirtualMachine.FsxOntapStorageVirtualMachineTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class FsxOntapStorageVirtualMachineTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#create FsxOntapStorageVirtualMachine#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#delete FsxOntapStorageVirtualMachine#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#update FsxOntapStorageVirtualMachine#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21a09378ce0d5169b689a5729c9c6ff7c213b135126ee5fb3630d13ef09ac55d)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#create FsxOntapStorageVirtualMachine#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#delete FsxOntapStorageVirtualMachine#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_ontap_storage_virtual_machine#update FsxOntapStorageVirtualMachine#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FsxOntapStorageVirtualMachineTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FsxOntapStorageVirtualMachineTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.fsxOntapStorageVirtualMachine.FsxOntapStorageVirtualMachineTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e78039a1271f1bc5f0d27f73ae8972dc50c1fac1566fcebd3b93319b3dd6eb1f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__34a4479e68d56dde587db453446e7db43faaf5809b33984f9c4174fe873cbb9e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77352255d1792ac14da82a48a24b54b19ae1e136240554fec5e1bae4dd51ce83)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23866a50193ab5f299df4b7905cb9a1ba75b92de803cdd31bb691dac8c669693)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[FsxOntapStorageVirtualMachineTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[FsxOntapStorageVirtualMachineTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[FsxOntapStorageVirtualMachineTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f7e7fc67254f8548dc356cbea7085f8cd51eed84095b9d5e73eba6061038a3a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "FsxOntapStorageVirtualMachine",
    "FsxOntapStorageVirtualMachineActiveDirectoryConfiguration",
    "FsxOntapStorageVirtualMachineActiveDirectoryConfigurationOutputReference",
    "FsxOntapStorageVirtualMachineActiveDirectoryConfigurationSelfManagedActiveDirectoryConfiguration",
    "FsxOntapStorageVirtualMachineActiveDirectoryConfigurationSelfManagedActiveDirectoryConfigurationOutputReference",
    "FsxOntapStorageVirtualMachineConfig",
    "FsxOntapStorageVirtualMachineEndpoints",
    "FsxOntapStorageVirtualMachineEndpointsIscsi",
    "FsxOntapStorageVirtualMachineEndpointsIscsiList",
    "FsxOntapStorageVirtualMachineEndpointsIscsiOutputReference",
    "FsxOntapStorageVirtualMachineEndpointsList",
    "FsxOntapStorageVirtualMachineEndpointsManagement",
    "FsxOntapStorageVirtualMachineEndpointsManagementList",
    "FsxOntapStorageVirtualMachineEndpointsManagementOutputReference",
    "FsxOntapStorageVirtualMachineEndpointsNfs",
    "FsxOntapStorageVirtualMachineEndpointsNfsList",
    "FsxOntapStorageVirtualMachineEndpointsNfsOutputReference",
    "FsxOntapStorageVirtualMachineEndpointsOutputReference",
    "FsxOntapStorageVirtualMachineEndpointsSmb",
    "FsxOntapStorageVirtualMachineEndpointsSmbList",
    "FsxOntapStorageVirtualMachineEndpointsSmbOutputReference",
    "FsxOntapStorageVirtualMachineTimeouts",
    "FsxOntapStorageVirtualMachineTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__5e24503767bec89896ba921db7eff2320cc7d4def24a486f37c41d78c8a428d9(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    file_system_id: builtins.str,
    name: builtins.str,
    active_directory_configuration: typing.Optional[typing.Union[FsxOntapStorageVirtualMachineActiveDirectoryConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    root_volume_security_style: typing.Optional[builtins.str] = None,
    svm_admin_password: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[FsxOntapStorageVirtualMachineTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__cebf8966d4379c4a0894fd76452230c1ee8ea05cbb4ad7f1411571080611df4e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__952b856fea820c1eb05d8e39a232a0a3ab6dbf5dae93e2df74eda54580a81b9e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cac4dae35b5d7206e9cbea3f82f6fa5e79737ce83e4b3c924a1c4f444b1ab76(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44329d02ab3ad5b04e2e89772b28edd78a9ebe8ed8abdf1ef1b909882c0608be(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db2c89dbe4b7f916838f0291fdd4d076dd095b4049e21a98b93a77bfec717c06(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55de663d8cae95378448d409806ee1c49d1bc051d365166e782c8f43fa87dd7f(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73cfedb958dcd7f875a2321725b093024347d296645e4d33ddcdde6617f03a42(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e87cf9307342280e2c601104cd57c9a287751345fe7be896798d403b339a8cf1(
    *,
    netbios_name: typing.Optional[builtins.str] = None,
    self_managed_active_directory_configuration: typing.Optional[typing.Union[FsxOntapStorageVirtualMachineActiveDirectoryConfigurationSelfManagedActiveDirectoryConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28dcc6a910b39d2aed5d7a34c41bc3f36dc3df299387e693719c12b740b9eca1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cdb472f19f55a4fac799ba267ede6335a76778315ad9562737c205116399366(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d5b98516af425040761a9690453d4de7780f5d0f2c4bfc52eb93619507b3454(
    value: typing.Optional[FsxOntapStorageVirtualMachineActiveDirectoryConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a6dc31b6e7b05ba5cdff3c1a6a4f079c7b2a43a223a57d58b9f69242010cc9c(
    *,
    dns_ips: typing.Sequence[builtins.str],
    domain_name: builtins.str,
    password: builtins.str,
    username: builtins.str,
    file_system_administrators_group: typing.Optional[builtins.str] = None,
    organizational_unit_distinguished_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6232fb6e15d3ac8c7565eac0f41ecee9df8fc43f49aa0bafa54f57f447dfce0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8608ffedaed4a39270cafa59f5e83f7eb27b425dd8a2059f8b9d3ed303a1f24(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31da3a337e3601a5449b8749fe228d24435f74fa93d245600591ec0aa5752394(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4f9ab97ec96800753b62f9077ba39ef3ab12a3fa97b54f3165abd61fbf5baa4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c5d9b17c04eecc2e3de6eada2d2b807fb62c98aad4ed7f69f71b7f34d9afba4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c40ce387ae96e4e20ea2c0f3552d2baed1ab65bef96d730beedffabf96d2809(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c12970badbebc3b0a0cf60d5f7eeba1f9d6ba923884932468c052f9829be72d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80931f87bca653761681da869184f3b695b6ab5a1865774a59f90225bf6e440b(
    value: typing.Optional[FsxOntapStorageVirtualMachineActiveDirectoryConfigurationSelfManagedActiveDirectoryConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b356cf1aa012577f7c0042d0f5f04c569658eb14b8c08088d84f52e0c141697d(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    file_system_id: builtins.str,
    name: builtins.str,
    active_directory_configuration: typing.Optional[typing.Union[FsxOntapStorageVirtualMachineActiveDirectoryConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    root_volume_security_style: typing.Optional[builtins.str] = None,
    svm_admin_password: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[FsxOntapStorageVirtualMachineTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62d5babce06e10b739314402c0c686dc540a1464c1e13d444db16a34ced3f8a9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef5340063bfdcc52d421405ba7cf20ae602e569f909d13eaf583b75edef5367a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de064815fafadda224f83a05d885ed8d3191c657bad0f784852ad946621a5ede(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71e162e2b503700490bf2b8aafada95099c79d9fa4963850572756c6984a7742(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08ba1e6ae7175a8bac6e52bc9c1d4d249097c10dddf61b0b1d8748f8a3153918(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f0312d6a08750dbe32fa33d6d814951bbb6a6f35f1cd691aa0010ca7e365285(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf45ec6bfe7e7da8fd4ceb5c4b8fd9d1ab05d3d0092d72c239c2212c44d33101(
    value: typing.Optional[FsxOntapStorageVirtualMachineEndpointsIscsi],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea1c02865352f3ded9732066a790c36f15d74fbee9e210b4b30dd2cb725c3f0a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__399d9414a279cacf21a5581370f1e9fa6da1e7cb8b6485582d69300d705adc8e(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b69569fd512072be947e4a5c844be867cad201cd2e01cc9ebc4870851e85b2e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__043a4f85015969a76df68a8b50c5241369ba36385dce72a60d8be5fc4eda052c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a023d762790147c6650ff2910a7d90be1c1b63fd33863f5eeb150a128f5473f9(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3aa108e72450a03f2cfdeb09c74f6a9eedd4bdb751eeaabd7a5b4d831269dba9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26a44af4166c978fac92f76ad0a6a1b89e92059e20a17287e0547ee5e76a084f(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a06e21efd8cf71ffd12130ba012fb726eac92505e00a014593adf1e61aea53db(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24430048f5c0074e9277a335429aac57d2df1187ef5a5ac3b8b6da806af3c832(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df3371de1866ddfca8d9b7f302ed66460eb050ac54ce033693c84a3489e6d83c(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33d4ae0d1a4dc3a840ca7c1863de2575d68ad1785444f10a61cf20feb731cee0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32bb7b3a779dfd0ccc8e72484c2f21014fea33e198379735c8a78fc887d4cee5(
    value: typing.Optional[FsxOntapStorageVirtualMachineEndpointsManagement],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cf2d7798f90b768ee839173e21864aa3022f70606bc15bf2f25ec93f3e1583c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdaecd300f676f85b8fe21f557617f73f63e5d0108b7ff70cb028c09c97ad687(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d885a1fe1d425d1e8b35efc6cd530d2920725fa3075f9a7a18b32cba4b876860(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78415870258f49fa95e62fcb738f0da7dcaa1dd5b440593a935bb10fcc46772a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54e7f6edfdcc176cf9a91d5b44201acf553529351b986df8096bc9d7d2808079(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__423fe838f88ef436e5490fc10fa85b2ef45d6ead45ea390f61c304c69aea4ea7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d95dba46696148419ffcb7c62fdabf1e35cd5d11bdf3533e4d16ceed7a76d2f(
    value: typing.Optional[FsxOntapStorageVirtualMachineEndpointsNfs],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d13485242fb0089ff89889424cca33ad4b5191d68416063075ba58e1921634fc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd827a34a1ffa6d1f8645e2b9ded7ff42effe9bb66a7d8d111083dd2c9137078(
    value: typing.Optional[FsxOntapStorageVirtualMachineEndpoints],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__daabe2d8cdc97ce4e1bf696d77a5618ec0f1d16773ad262ccbbce99baf38ab10(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e987ac0fa2eb3732896170ee9ecb74f390644a5a0eda3e2c9f2bd9d589a3d26(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__543f49278af3ac0a846f5f04f9b19b869a62acb5ba3bbf65e77547de70c2dee6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bedbb18fffe4462a6828c7f90a2f46eaf9d80859a31823af7160650489cea8f9(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2075e324816635e1c1d78279b270746c0035b0802dc02616d4ce5f25f3e501b(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__442b77be9d0a98a6b64eb54eebdd0d1e4e7d2731909c3555bbcd266588862ab4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca405f10f2145e9de5c3a849cd1e13ccf6f55d89c4686500a98306d9906dd7ad(
    value: typing.Optional[FsxOntapStorageVirtualMachineEndpointsSmb],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21a09378ce0d5169b689a5729c9c6ff7c213b135126ee5fb3630d13ef09ac55d(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e78039a1271f1bc5f0d27f73ae8972dc50c1fac1566fcebd3b93319b3dd6eb1f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34a4479e68d56dde587db453446e7db43faaf5809b33984f9c4174fe873cbb9e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77352255d1792ac14da82a48a24b54b19ae1e136240554fec5e1bae4dd51ce83(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23866a50193ab5f299df4b7905cb9a1ba75b92de803cdd31bb691dac8c669693(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f7e7fc67254f8548dc356cbea7085f8cd51eed84095b9d5e73eba6061038a3a(
    value: typing.Optional[typing.Union[FsxOntapStorageVirtualMachineTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
