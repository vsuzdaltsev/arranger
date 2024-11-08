'''
# `aws_fsx_data_repository_association`

Refer to the Terraform Registory for docs: [`aws_fsx_data_repository_association`](https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association).
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


class FsxDataRepositoryAssociation(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.fsxDataRepositoryAssociation.FsxDataRepositoryAssociation",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association aws_fsx_data_repository_association}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        data_repository_path: builtins.str,
        file_system_id: builtins.str,
        file_system_path: builtins.str,
        batch_import_meta_data_on_create: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        delete_data_in_filesystem: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        imported_file_chunk_size: typing.Optional[jsii.Number] = None,
        s3: typing.Optional[typing.Union["FsxDataRepositoryAssociationS3", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["FsxDataRepositoryAssociationTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association aws_fsx_data_repository_association} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param data_repository_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#data_repository_path FsxDataRepositoryAssociation#data_repository_path}.
        :param file_system_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#file_system_id FsxDataRepositoryAssociation#file_system_id}.
        :param file_system_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#file_system_path FsxDataRepositoryAssociation#file_system_path}.
        :param batch_import_meta_data_on_create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#batch_import_meta_data_on_create FsxDataRepositoryAssociation#batch_import_meta_data_on_create}.
        :param delete_data_in_filesystem: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#delete_data_in_filesystem FsxDataRepositoryAssociation#delete_data_in_filesystem}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#id FsxDataRepositoryAssociation#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param imported_file_chunk_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#imported_file_chunk_size FsxDataRepositoryAssociation#imported_file_chunk_size}.
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#s3 FsxDataRepositoryAssociation#s3}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#tags FsxDataRepositoryAssociation#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#tags_all FsxDataRepositoryAssociation#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#timeouts FsxDataRepositoryAssociation#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec90721a9e5929e55aaa194163a82ad752a1204608012bb9c19eead10095cf9c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = FsxDataRepositoryAssociationConfig(
            data_repository_path=data_repository_path,
            file_system_id=file_system_id,
            file_system_path=file_system_path,
            batch_import_meta_data_on_create=batch_import_meta_data_on_create,
            delete_data_in_filesystem=delete_data_in_filesystem,
            id=id,
            imported_file_chunk_size=imported_file_chunk_size,
            s3=s3,
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

    @jsii.member(jsii_name="putS3")
    def put_s3(
        self,
        *,
        auto_export_policy: typing.Optional[typing.Union["FsxDataRepositoryAssociationS3AutoExportPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        auto_import_policy: typing.Optional[typing.Union["FsxDataRepositoryAssociationS3AutoImportPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param auto_export_policy: auto_export_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#auto_export_policy FsxDataRepositoryAssociation#auto_export_policy}
        :param auto_import_policy: auto_import_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#auto_import_policy FsxDataRepositoryAssociation#auto_import_policy}
        '''
        value = FsxDataRepositoryAssociationS3(
            auto_export_policy=auto_export_policy,
            auto_import_policy=auto_import_policy,
        )

        return typing.cast(None, jsii.invoke(self, "putS3", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#create FsxDataRepositoryAssociation#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#delete FsxDataRepositoryAssociation#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#update FsxDataRepositoryAssociation#update}.
        '''
        value = FsxDataRepositoryAssociationTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetBatchImportMetaDataOnCreate")
    def reset_batch_import_meta_data_on_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBatchImportMetaDataOnCreate", []))

    @jsii.member(jsii_name="resetDeleteDataInFilesystem")
    def reset_delete_data_in_filesystem(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeleteDataInFilesystem", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetImportedFileChunkSize")
    def reset_imported_file_chunk_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImportedFileChunkSize", []))

    @jsii.member(jsii_name="resetS3")
    def reset_s3(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3", []))

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
    @jsii.member(jsii_name="associationId")
    def association_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "associationId"))

    @builtins.property
    @jsii.member(jsii_name="s3")
    def s3(self) -> "FsxDataRepositoryAssociationS3OutputReference":
        return typing.cast("FsxDataRepositoryAssociationS3OutputReference", jsii.get(self, "s3"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "FsxDataRepositoryAssociationTimeoutsOutputReference":
        return typing.cast("FsxDataRepositoryAssociationTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="batchImportMetaDataOnCreateInput")
    def batch_import_meta_data_on_create_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "batchImportMetaDataOnCreateInput"))

    @builtins.property
    @jsii.member(jsii_name="dataRepositoryPathInput")
    def data_repository_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataRepositoryPathInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteDataInFilesystemInput")
    def delete_data_in_filesystem_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "deleteDataInFilesystemInput"))

    @builtins.property
    @jsii.member(jsii_name="fileSystemIdInput")
    def file_system_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileSystemIdInput"))

    @builtins.property
    @jsii.member(jsii_name="fileSystemPathInput")
    def file_system_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileSystemPathInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="importedFileChunkSizeInput")
    def imported_file_chunk_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "importedFileChunkSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="s3Input")
    def s3_input(self) -> typing.Optional["FsxDataRepositoryAssociationS3"]:
        return typing.cast(typing.Optional["FsxDataRepositoryAssociationS3"], jsii.get(self, "s3Input"))

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
    ) -> typing.Optional[typing.Union["FsxDataRepositoryAssociationTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["FsxDataRepositoryAssociationTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="batchImportMetaDataOnCreate")
    def batch_import_meta_data_on_create(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "batchImportMetaDataOnCreate"))

    @batch_import_meta_data_on_create.setter
    def batch_import_meta_data_on_create(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a26def65633b33cda9e2ab46445752339dbfc00b5dd4bfa7d984995f4e82ac2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "batchImportMetaDataOnCreate", value)

    @builtins.property
    @jsii.member(jsii_name="dataRepositoryPath")
    def data_repository_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataRepositoryPath"))

    @data_repository_path.setter
    def data_repository_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26f6bd9b070e0d7e3423c50ffc0ae945824f3008acc399025f9d094863a49b84)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataRepositoryPath", value)

    @builtins.property
    @jsii.member(jsii_name="deleteDataInFilesystem")
    def delete_data_in_filesystem(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "deleteDataInFilesystem"))

    @delete_data_in_filesystem.setter
    def delete_data_in_filesystem(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__edadb69859ac887c0259a5c1cb46aaaf948d5a6767b58c3766a479557080e1df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteDataInFilesystem", value)

    @builtins.property
    @jsii.member(jsii_name="fileSystemId")
    def file_system_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileSystemId"))

    @file_system_id.setter
    def file_system_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b39c19a70bfc2ac8890dd575037b11db88cafa88caefd89e0eff3240a004a038)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileSystemId", value)

    @builtins.property
    @jsii.member(jsii_name="fileSystemPath")
    def file_system_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileSystemPath"))

    @file_system_path.setter
    def file_system_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57a5dd9f07465aed299c23dd5edab8f9821e9b3394248756c22293ea930aaaee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileSystemPath", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc3250d5ccbe25d2c4914013489697d8844feaaf9b8fa18678e9bd5a8d707d75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="importedFileChunkSize")
    def imported_file_chunk_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "importedFileChunkSize"))

    @imported_file_chunk_size.setter
    def imported_file_chunk_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6187aadb453e0b241ffa1ce1509ae8de9a7e200dd8615a975aebb8d1c1b7c16c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "importedFileChunkSize", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__293ddc5b0faff028583fd2c9add6a7c7e610e9da0509ab47ec4ae68c15844b36)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dfe794846a27560510176271728467c13cca754aebfc379ae1743d8d552dd4b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.fsxDataRepositoryAssociation.FsxDataRepositoryAssociationConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "data_repository_path": "dataRepositoryPath",
        "file_system_id": "fileSystemId",
        "file_system_path": "fileSystemPath",
        "batch_import_meta_data_on_create": "batchImportMetaDataOnCreate",
        "delete_data_in_filesystem": "deleteDataInFilesystem",
        "id": "id",
        "imported_file_chunk_size": "importedFileChunkSize",
        "s3": "s3",
        "tags": "tags",
        "tags_all": "tagsAll",
        "timeouts": "timeouts",
    },
)
class FsxDataRepositoryAssociationConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        data_repository_path: builtins.str,
        file_system_id: builtins.str,
        file_system_path: builtins.str,
        batch_import_meta_data_on_create: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        delete_data_in_filesystem: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        imported_file_chunk_size: typing.Optional[jsii.Number] = None,
        s3: typing.Optional[typing.Union["FsxDataRepositoryAssociationS3", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["FsxDataRepositoryAssociationTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param data_repository_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#data_repository_path FsxDataRepositoryAssociation#data_repository_path}.
        :param file_system_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#file_system_id FsxDataRepositoryAssociation#file_system_id}.
        :param file_system_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#file_system_path FsxDataRepositoryAssociation#file_system_path}.
        :param batch_import_meta_data_on_create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#batch_import_meta_data_on_create FsxDataRepositoryAssociation#batch_import_meta_data_on_create}.
        :param delete_data_in_filesystem: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#delete_data_in_filesystem FsxDataRepositoryAssociation#delete_data_in_filesystem}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#id FsxDataRepositoryAssociation#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param imported_file_chunk_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#imported_file_chunk_size FsxDataRepositoryAssociation#imported_file_chunk_size}.
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#s3 FsxDataRepositoryAssociation#s3}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#tags FsxDataRepositoryAssociation#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#tags_all FsxDataRepositoryAssociation#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#timeouts FsxDataRepositoryAssociation#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(s3, dict):
            s3 = FsxDataRepositoryAssociationS3(**s3)
        if isinstance(timeouts, dict):
            timeouts = FsxDataRepositoryAssociationTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__374da90fb4772e40caf8a590bf6b6bc629be348ff038f51113541d5a85158a4f)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument data_repository_path", value=data_repository_path, expected_type=type_hints["data_repository_path"])
            check_type(argname="argument file_system_id", value=file_system_id, expected_type=type_hints["file_system_id"])
            check_type(argname="argument file_system_path", value=file_system_path, expected_type=type_hints["file_system_path"])
            check_type(argname="argument batch_import_meta_data_on_create", value=batch_import_meta_data_on_create, expected_type=type_hints["batch_import_meta_data_on_create"])
            check_type(argname="argument delete_data_in_filesystem", value=delete_data_in_filesystem, expected_type=type_hints["delete_data_in_filesystem"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument imported_file_chunk_size", value=imported_file_chunk_size, expected_type=type_hints["imported_file_chunk_size"])
            check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "data_repository_path": data_repository_path,
            "file_system_id": file_system_id,
            "file_system_path": file_system_path,
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
        if batch_import_meta_data_on_create is not None:
            self._values["batch_import_meta_data_on_create"] = batch_import_meta_data_on_create
        if delete_data_in_filesystem is not None:
            self._values["delete_data_in_filesystem"] = delete_data_in_filesystem
        if id is not None:
            self._values["id"] = id
        if imported_file_chunk_size is not None:
            self._values["imported_file_chunk_size"] = imported_file_chunk_size
        if s3 is not None:
            self._values["s3"] = s3
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
    def data_repository_path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#data_repository_path FsxDataRepositoryAssociation#data_repository_path}.'''
        result = self._values.get("data_repository_path")
        assert result is not None, "Required property 'data_repository_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def file_system_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#file_system_id FsxDataRepositoryAssociation#file_system_id}.'''
        result = self._values.get("file_system_id")
        assert result is not None, "Required property 'file_system_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def file_system_path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#file_system_path FsxDataRepositoryAssociation#file_system_path}.'''
        result = self._values.get("file_system_path")
        assert result is not None, "Required property 'file_system_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def batch_import_meta_data_on_create(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#batch_import_meta_data_on_create FsxDataRepositoryAssociation#batch_import_meta_data_on_create}.'''
        result = self._values.get("batch_import_meta_data_on_create")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def delete_data_in_filesystem(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#delete_data_in_filesystem FsxDataRepositoryAssociation#delete_data_in_filesystem}.'''
        result = self._values.get("delete_data_in_filesystem")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#id FsxDataRepositoryAssociation#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def imported_file_chunk_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#imported_file_chunk_size FsxDataRepositoryAssociation#imported_file_chunk_size}.'''
        result = self._values.get("imported_file_chunk_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def s3(self) -> typing.Optional["FsxDataRepositoryAssociationS3"]:
        '''s3 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#s3 FsxDataRepositoryAssociation#s3}
        '''
        result = self._values.get("s3")
        return typing.cast(typing.Optional["FsxDataRepositoryAssociationS3"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#tags FsxDataRepositoryAssociation#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#tags_all FsxDataRepositoryAssociation#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["FsxDataRepositoryAssociationTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#timeouts FsxDataRepositoryAssociation#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["FsxDataRepositoryAssociationTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FsxDataRepositoryAssociationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.fsxDataRepositoryAssociation.FsxDataRepositoryAssociationS3",
    jsii_struct_bases=[],
    name_mapping={
        "auto_export_policy": "autoExportPolicy",
        "auto_import_policy": "autoImportPolicy",
    },
)
class FsxDataRepositoryAssociationS3:
    def __init__(
        self,
        *,
        auto_export_policy: typing.Optional[typing.Union["FsxDataRepositoryAssociationS3AutoExportPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        auto_import_policy: typing.Optional[typing.Union["FsxDataRepositoryAssociationS3AutoImportPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param auto_export_policy: auto_export_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#auto_export_policy FsxDataRepositoryAssociation#auto_export_policy}
        :param auto_import_policy: auto_import_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#auto_import_policy FsxDataRepositoryAssociation#auto_import_policy}
        '''
        if isinstance(auto_export_policy, dict):
            auto_export_policy = FsxDataRepositoryAssociationS3AutoExportPolicy(**auto_export_policy)
        if isinstance(auto_import_policy, dict):
            auto_import_policy = FsxDataRepositoryAssociationS3AutoImportPolicy(**auto_import_policy)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__079bf72df876f92e7ef4cdebb2fec566bb7fcf5227648a5ea35ccbb6b97d08b0)
            check_type(argname="argument auto_export_policy", value=auto_export_policy, expected_type=type_hints["auto_export_policy"])
            check_type(argname="argument auto_import_policy", value=auto_import_policy, expected_type=type_hints["auto_import_policy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if auto_export_policy is not None:
            self._values["auto_export_policy"] = auto_export_policy
        if auto_import_policy is not None:
            self._values["auto_import_policy"] = auto_import_policy

    @builtins.property
    def auto_export_policy(
        self,
    ) -> typing.Optional["FsxDataRepositoryAssociationS3AutoExportPolicy"]:
        '''auto_export_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#auto_export_policy FsxDataRepositoryAssociation#auto_export_policy}
        '''
        result = self._values.get("auto_export_policy")
        return typing.cast(typing.Optional["FsxDataRepositoryAssociationS3AutoExportPolicy"], result)

    @builtins.property
    def auto_import_policy(
        self,
    ) -> typing.Optional["FsxDataRepositoryAssociationS3AutoImportPolicy"]:
        '''auto_import_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#auto_import_policy FsxDataRepositoryAssociation#auto_import_policy}
        '''
        result = self._values.get("auto_import_policy")
        return typing.cast(typing.Optional["FsxDataRepositoryAssociationS3AutoImportPolicy"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FsxDataRepositoryAssociationS3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.fsxDataRepositoryAssociation.FsxDataRepositoryAssociationS3AutoExportPolicy",
    jsii_struct_bases=[],
    name_mapping={"events": "events"},
)
class FsxDataRepositoryAssociationS3AutoExportPolicy:
    def __init__(
        self,
        *,
        events: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param events: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#events FsxDataRepositoryAssociation#events}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4900b77620816f838c129bb9dcb3c90f682ee3fa51da93e7e0ddc7529f541e8f)
            check_type(argname="argument events", value=events, expected_type=type_hints["events"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if events is not None:
            self._values["events"] = events

    @builtins.property
    def events(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#events FsxDataRepositoryAssociation#events}.'''
        result = self._values.get("events")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FsxDataRepositoryAssociationS3AutoExportPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FsxDataRepositoryAssociationS3AutoExportPolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.fsxDataRepositoryAssociation.FsxDataRepositoryAssociationS3AutoExportPolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__29f697d5c41c45b257f661f25b4d06d189be6375c750e4b4142e056850e701cd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEvents")
    def reset_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEvents", []))

    @builtins.property
    @jsii.member(jsii_name="eventsInput")
    def events_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "eventsInput"))

    @builtins.property
    @jsii.member(jsii_name="events")
    def events(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "events"))

    @events.setter
    def events(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08b8d67c6b536f442dd5eee4686617e7fbe6e9f5cda1e337afccff56eccac01d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "events", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[FsxDataRepositoryAssociationS3AutoExportPolicy]:
        return typing.cast(typing.Optional[FsxDataRepositoryAssociationS3AutoExportPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[FsxDataRepositoryAssociationS3AutoExportPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cdbf364cba1097189cf07336ee3e699bf1d4aac7f7f5eb258cceceab3c2946d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.fsxDataRepositoryAssociation.FsxDataRepositoryAssociationS3AutoImportPolicy",
    jsii_struct_bases=[],
    name_mapping={"events": "events"},
)
class FsxDataRepositoryAssociationS3AutoImportPolicy:
    def __init__(
        self,
        *,
        events: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param events: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#events FsxDataRepositoryAssociation#events}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9ee6b996702aebb4bde09145ae4667318845ad85286271bb6b00e78cf0d270b)
            check_type(argname="argument events", value=events, expected_type=type_hints["events"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if events is not None:
            self._values["events"] = events

    @builtins.property
    def events(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#events FsxDataRepositoryAssociation#events}.'''
        result = self._values.get("events")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FsxDataRepositoryAssociationS3AutoImportPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FsxDataRepositoryAssociationS3AutoImportPolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.fsxDataRepositoryAssociation.FsxDataRepositoryAssociationS3AutoImportPolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0e52e88ac42a042300c4a9bab1bf947300787015e6868ca2df9c7632717b7120)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEvents")
    def reset_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEvents", []))

    @builtins.property
    @jsii.member(jsii_name="eventsInput")
    def events_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "eventsInput"))

    @builtins.property
    @jsii.member(jsii_name="events")
    def events(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "events"))

    @events.setter
    def events(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2d91b90f2a40e142c2d25097828c6e5fb0b0070111c8374628381708cc6aa65)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "events", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[FsxDataRepositoryAssociationS3AutoImportPolicy]:
        return typing.cast(typing.Optional[FsxDataRepositoryAssociationS3AutoImportPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[FsxDataRepositoryAssociationS3AutoImportPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__991ac2dee7a24090bfeb8d2afad0bf58fba98baa7bade39d5e74e80b5cfce42d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class FsxDataRepositoryAssociationS3OutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.fsxDataRepositoryAssociation.FsxDataRepositoryAssociationS3OutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__996c3b2e65b0186bc3f30ba790c57bd691944886a590d6214dfd9b1b1f3e72c3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAutoExportPolicy")
    def put_auto_export_policy(
        self,
        *,
        events: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param events: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#events FsxDataRepositoryAssociation#events}.
        '''
        value = FsxDataRepositoryAssociationS3AutoExportPolicy(events=events)

        return typing.cast(None, jsii.invoke(self, "putAutoExportPolicy", [value]))

    @jsii.member(jsii_name="putAutoImportPolicy")
    def put_auto_import_policy(
        self,
        *,
        events: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param events: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#events FsxDataRepositoryAssociation#events}.
        '''
        value = FsxDataRepositoryAssociationS3AutoImportPolicy(events=events)

        return typing.cast(None, jsii.invoke(self, "putAutoImportPolicy", [value]))

    @jsii.member(jsii_name="resetAutoExportPolicy")
    def reset_auto_export_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoExportPolicy", []))

    @jsii.member(jsii_name="resetAutoImportPolicy")
    def reset_auto_import_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoImportPolicy", []))

    @builtins.property
    @jsii.member(jsii_name="autoExportPolicy")
    def auto_export_policy(
        self,
    ) -> FsxDataRepositoryAssociationS3AutoExportPolicyOutputReference:
        return typing.cast(FsxDataRepositoryAssociationS3AutoExportPolicyOutputReference, jsii.get(self, "autoExportPolicy"))

    @builtins.property
    @jsii.member(jsii_name="autoImportPolicy")
    def auto_import_policy(
        self,
    ) -> FsxDataRepositoryAssociationS3AutoImportPolicyOutputReference:
        return typing.cast(FsxDataRepositoryAssociationS3AutoImportPolicyOutputReference, jsii.get(self, "autoImportPolicy"))

    @builtins.property
    @jsii.member(jsii_name="autoExportPolicyInput")
    def auto_export_policy_input(
        self,
    ) -> typing.Optional[FsxDataRepositoryAssociationS3AutoExportPolicy]:
        return typing.cast(typing.Optional[FsxDataRepositoryAssociationS3AutoExportPolicy], jsii.get(self, "autoExportPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="autoImportPolicyInput")
    def auto_import_policy_input(
        self,
    ) -> typing.Optional[FsxDataRepositoryAssociationS3AutoImportPolicy]:
        return typing.cast(typing.Optional[FsxDataRepositoryAssociationS3AutoImportPolicy], jsii.get(self, "autoImportPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[FsxDataRepositoryAssociationS3]:
        return typing.cast(typing.Optional[FsxDataRepositoryAssociationS3], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[FsxDataRepositoryAssociationS3],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbd62d23ed4b0d42624aa52117a135c7b51823c7e86b6dae3d1b44bf3e48651c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.fsxDataRepositoryAssociation.FsxDataRepositoryAssociationTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class FsxDataRepositoryAssociationTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#create FsxDataRepositoryAssociation#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#delete FsxDataRepositoryAssociation#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#update FsxDataRepositoryAssociation#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__752f01d1b3af1df1a603dd2a17e2d1921712efb79398cf799851961837073c94)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#create FsxDataRepositoryAssociation#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#delete FsxDataRepositoryAssociation#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_data_repository_association#update FsxDataRepositoryAssociation#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FsxDataRepositoryAssociationTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FsxDataRepositoryAssociationTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.fsxDataRepositoryAssociation.FsxDataRepositoryAssociationTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d69521f70447ad2ea272d2cef90383926980dfdc696ea3bfe8637f6f757b4fcb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c189e48c0ab1575d777aebf7ba702950d4d948a605b245f0ee490449ab5c29c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2edd093bbc02e4d3d6b5a41be5f7c5c9ff8dc0e06034ad40b98a765abd03886)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d720345d6342e89d4f0ca1371fff3fb148662c054f803c744a3f146075d98db3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[FsxDataRepositoryAssociationTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[FsxDataRepositoryAssociationTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[FsxDataRepositoryAssociationTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ae7777f7a96ab424057c3427f9089adddc760e646d598ec7453e2453ad7e234)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "FsxDataRepositoryAssociation",
    "FsxDataRepositoryAssociationConfig",
    "FsxDataRepositoryAssociationS3",
    "FsxDataRepositoryAssociationS3AutoExportPolicy",
    "FsxDataRepositoryAssociationS3AutoExportPolicyOutputReference",
    "FsxDataRepositoryAssociationS3AutoImportPolicy",
    "FsxDataRepositoryAssociationS3AutoImportPolicyOutputReference",
    "FsxDataRepositoryAssociationS3OutputReference",
    "FsxDataRepositoryAssociationTimeouts",
    "FsxDataRepositoryAssociationTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__ec90721a9e5929e55aaa194163a82ad752a1204608012bb9c19eead10095cf9c(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    data_repository_path: builtins.str,
    file_system_id: builtins.str,
    file_system_path: builtins.str,
    batch_import_meta_data_on_create: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    delete_data_in_filesystem: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    imported_file_chunk_size: typing.Optional[jsii.Number] = None,
    s3: typing.Optional[typing.Union[FsxDataRepositoryAssociationS3, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[FsxDataRepositoryAssociationTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__0a26def65633b33cda9e2ab46445752339dbfc00b5dd4bfa7d984995f4e82ac2(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26f6bd9b070e0d7e3423c50ffc0ae945824f3008acc399025f9d094863a49b84(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__edadb69859ac887c0259a5c1cb46aaaf948d5a6767b58c3766a479557080e1df(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b39c19a70bfc2ac8890dd575037b11db88cafa88caefd89e0eff3240a004a038(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57a5dd9f07465aed299c23dd5edab8f9821e9b3394248756c22293ea930aaaee(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc3250d5ccbe25d2c4914013489697d8844feaaf9b8fa18678e9bd5a8d707d75(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6187aadb453e0b241ffa1ce1509ae8de9a7e200dd8615a975aebb8d1c1b7c16c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__293ddc5b0faff028583fd2c9add6a7c7e610e9da0509ab47ec4ae68c15844b36(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfe794846a27560510176271728467c13cca754aebfc379ae1743d8d552dd4b6(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__374da90fb4772e40caf8a590bf6b6bc629be348ff038f51113541d5a85158a4f(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    data_repository_path: builtins.str,
    file_system_id: builtins.str,
    file_system_path: builtins.str,
    batch_import_meta_data_on_create: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    delete_data_in_filesystem: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    imported_file_chunk_size: typing.Optional[jsii.Number] = None,
    s3: typing.Optional[typing.Union[FsxDataRepositoryAssociationS3, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[FsxDataRepositoryAssociationTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__079bf72df876f92e7ef4cdebb2fec566bb7fcf5227648a5ea35ccbb6b97d08b0(
    *,
    auto_export_policy: typing.Optional[typing.Union[FsxDataRepositoryAssociationS3AutoExportPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    auto_import_policy: typing.Optional[typing.Union[FsxDataRepositoryAssociationS3AutoImportPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4900b77620816f838c129bb9dcb3c90f682ee3fa51da93e7e0ddc7529f541e8f(
    *,
    events: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29f697d5c41c45b257f661f25b4d06d189be6375c750e4b4142e056850e701cd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08b8d67c6b536f442dd5eee4686617e7fbe6e9f5cda1e337afccff56eccac01d(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cdbf364cba1097189cf07336ee3e699bf1d4aac7f7f5eb258cceceab3c2946d(
    value: typing.Optional[FsxDataRepositoryAssociationS3AutoExportPolicy],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9ee6b996702aebb4bde09145ae4667318845ad85286271bb6b00e78cf0d270b(
    *,
    events: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e52e88ac42a042300c4a9bab1bf947300787015e6868ca2df9c7632717b7120(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2d91b90f2a40e142c2d25097828c6e5fb0b0070111c8374628381708cc6aa65(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__991ac2dee7a24090bfeb8d2afad0bf58fba98baa7bade39d5e74e80b5cfce42d(
    value: typing.Optional[FsxDataRepositoryAssociationS3AutoImportPolicy],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__996c3b2e65b0186bc3f30ba790c57bd691944886a590d6214dfd9b1b1f3e72c3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbd62d23ed4b0d42624aa52117a135c7b51823c7e86b6dae3d1b44bf3e48651c(
    value: typing.Optional[FsxDataRepositoryAssociationS3],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__752f01d1b3af1df1a603dd2a17e2d1921712efb79398cf799851961837073c94(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d69521f70447ad2ea272d2cef90383926980dfdc696ea3bfe8637f6f757b4fcb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c189e48c0ab1575d777aebf7ba702950d4d948a605b245f0ee490449ab5c29c4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2edd093bbc02e4d3d6b5a41be5f7c5c9ff8dc0e06034ad40b98a765abd03886(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d720345d6342e89d4f0ca1371fff3fb148662c054f803c744a3f146075d98db3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ae7777f7a96ab424057c3427f9089adddc760e646d598ec7453e2453ad7e234(
    value: typing.Optional[typing.Union[FsxDataRepositoryAssociationTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
