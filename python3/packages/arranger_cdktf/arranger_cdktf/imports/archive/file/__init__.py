'''
# `archive_file`

Refer to the Terraform Registory for docs: [`archive_file`](https://registry.terraform.io/providers/hashicorp/archive/2.4.0/docs/resources/file).
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


class File(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="archive.file.File",
):
    '''Represents a {@link https://registry.terraform.io/providers/hashicorp/archive/2.4.0/docs/resources/file archive_file}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        output_path: builtins.str,
        type: builtins.str,
        excludes: typing.Optional[typing.Sequence[builtins.str]] = None,
        exclude_symlink_directories: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        output_file_mode: typing.Optional[builtins.str] = None,
        source: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["FileSource", typing.Dict[builtins.str, typing.Any]]]]] = None,
        source_content: typing.Optional[builtins.str] = None,
        source_content_filename: typing.Optional[builtins.str] = None,
        source_dir: typing.Optional[builtins.str] = None,
        source_file: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/hashicorp/archive/2.4.0/docs/resources/file archive_file} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param output_path: The output of the archive file. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/archive/2.4.0/docs/resources/file#output_path File#output_path}
        :param type: The type of archive to generate. NOTE: ``zip`` is supported. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/archive/2.4.0/docs/resources/file#type File#type}
        :param excludes: Specify files to ignore when reading the ``source_dir``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/archive/2.4.0/docs/resources/file#excludes File#excludes}
        :param exclude_symlink_directories: Boolean flag indicating whether symbolically linked directories should be excluded during the creation of the archive. Defaults to false. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/archive/2.4.0/docs/resources/file#exclude_symlink_directories File#exclude_symlink_directories}
        :param output_file_mode: String that specifies the octal file mode for all archived files. For example: ``"0666"``. Setting this will ensure that cross platform usage of this module will not vary the modes of archived files (and ultimately checksums) resulting in more deterministic behavior. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/archive/2.4.0/docs/resources/file#output_file_mode File#output_file_mode}
        :param source: source block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/archive/2.4.0/docs/resources/file#source File#source}
        :param source_content: Add only this content to the archive with ``source_content_filename`` as the filename. One and only one of ``source``, ``source_content_filename`` (with ``source_content``), ``source_file``, or ``source_dir`` must be specified. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/archive/2.4.0/docs/resources/file#source_content File#source_content}
        :param source_content_filename: Set this as the filename when using ``source_content``. One and only one of ``source``, ``source_content_filename`` (with ``source_content``), ``source_file``, or ``source_dir`` must be specified. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/archive/2.4.0/docs/resources/file#source_content_filename File#source_content_filename}
        :param source_dir: Package entire contents of this directory into the archive. One and only one of ``source``, ``source_content_filename`` (with ``source_content``), ``source_file``, or ``source_dir`` must be specified. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/archive/2.4.0/docs/resources/file#source_dir File#source_dir}
        :param source_file: Package this file into the archive. One and only one of ``source``, ``source_content_filename`` (with ``source_content``), ``source_file``, or ``source_dir`` must be specified. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/archive/2.4.0/docs/resources/file#source_file File#source_file}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7ee412048fe6f8f8924e3c1fc966fa39c82747cdee6bb81cf01e646f77bce2b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = FileConfig(
            output_path=output_path,
            type=type,
            excludes=excludes,
            exclude_symlink_directories=exclude_symlink_directories,
            output_file_mode=output_file_mode,
            source=source,
            source_content=source_content,
            source_content_filename=source_content_filename,
            source_dir=source_dir,
            source_file=source_file,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="putSource")
    def put_source(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["FileSource", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3197d3b4b4d2d85cbc957dfc0ecf072bfb30ec9237589b33029ab917f891484)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSource", [value]))

    @jsii.member(jsii_name="resetExcludes")
    def reset_excludes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcludes", []))

    @jsii.member(jsii_name="resetExcludeSymlinkDirectories")
    def reset_exclude_symlink_directories(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcludeSymlinkDirectories", []))

    @jsii.member(jsii_name="resetOutputFileMode")
    def reset_output_file_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOutputFileMode", []))

    @jsii.member(jsii_name="resetSource")
    def reset_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSource", []))

    @jsii.member(jsii_name="resetSourceContent")
    def reset_source_content(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceContent", []))

    @jsii.member(jsii_name="resetSourceContentFilename")
    def reset_source_content_filename(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceContentFilename", []))

    @jsii.member(jsii_name="resetSourceDir")
    def reset_source_dir(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceDir", []))

    @jsii.member(jsii_name="resetSourceFile")
    def reset_source_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceFile", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="outputBase64Sha256")
    def output_base64_sha256(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outputBase64Sha256"))

    @builtins.property
    @jsii.member(jsii_name="outputBase64Sha512")
    def output_base64_sha512(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outputBase64Sha512"))

    @builtins.property
    @jsii.member(jsii_name="outputMd5")
    def output_md5(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outputMd5"))

    @builtins.property
    @jsii.member(jsii_name="outputSha")
    def output_sha(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outputSha"))

    @builtins.property
    @jsii.member(jsii_name="outputSha256")
    def output_sha256(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outputSha256"))

    @builtins.property
    @jsii.member(jsii_name="outputSha512")
    def output_sha512(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outputSha512"))

    @builtins.property
    @jsii.member(jsii_name="outputSize")
    def output_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "outputSize"))

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> "FileSourceList":
        return typing.cast("FileSourceList", jsii.get(self, "source"))

    @builtins.property
    @jsii.member(jsii_name="excludesInput")
    def excludes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "excludesInput"))

    @builtins.property
    @jsii.member(jsii_name="excludeSymlinkDirectoriesInput")
    def exclude_symlink_directories_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "excludeSymlinkDirectoriesInput"))

    @builtins.property
    @jsii.member(jsii_name="outputFileModeInput")
    def output_file_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "outputFileModeInput"))

    @builtins.property
    @jsii.member(jsii_name="outputPathInput")
    def output_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "outputPathInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceContentFilenameInput")
    def source_content_filename_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceContentFilenameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceContentInput")
    def source_content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceContentInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceDirInput")
    def source_dir_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceDirInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceFileInput")
    def source_file_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceFileInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceInput")
    def source_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["FileSource"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["FileSource"]]], jsii.get(self, "sourceInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="excludes")
    def excludes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "excludes"))

    @excludes.setter
    def excludes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ba868880f20e445dba8ade3e97c19c001295dab858ac8b79f58238da03f9394)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "excludes", value)

    @builtins.property
    @jsii.member(jsii_name="excludeSymlinkDirectories")
    def exclude_symlink_directories(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "excludeSymlinkDirectories"))

    @exclude_symlink_directories.setter
    def exclude_symlink_directories(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e0be0c26154dac5ef315b71f277bf19195d0dbfeb89bbd119d1cab23fc257de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "excludeSymlinkDirectories", value)

    @builtins.property
    @jsii.member(jsii_name="outputFileMode")
    def output_file_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outputFileMode"))

    @output_file_mode.setter
    def output_file_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fb6d1395d9b7726bf0047dff5e6c9eee35bf761683e44c2fe839f81b94a5a1e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outputFileMode", value)

    @builtins.property
    @jsii.member(jsii_name="outputPath")
    def output_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outputPath"))

    @output_path.setter
    def output_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c18d7713cf9b29421b1019f4bba6e873e6860f779271d020e717d8f649f99f46)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outputPath", value)

    @builtins.property
    @jsii.member(jsii_name="sourceContent")
    def source_content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceContent"))

    @source_content.setter
    def source_content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a8e9ea58e1dad4c16b9980e7b3b6375efa984070dffd9cc89e0eff77345cfe7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceContent", value)

    @builtins.property
    @jsii.member(jsii_name="sourceContentFilename")
    def source_content_filename(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceContentFilename"))

    @source_content_filename.setter
    def source_content_filename(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fff1b1545daced3c67ebf16ea981c72697c4a3207e6e7d7dc2574fa61e055535)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceContentFilename", value)

    @builtins.property
    @jsii.member(jsii_name="sourceDir")
    def source_dir(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceDir"))

    @source_dir.setter
    def source_dir(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8b479734081d511084002c8e0f523a539cf9d389043a60ee7b422d7f1c1f224)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceDir", value)

    @builtins.property
    @jsii.member(jsii_name="sourceFile")
    def source_file(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceFile"))

    @source_file.setter
    def source_file(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94ca3cee3d5cee67c76fefbca08e9c5294b4ea6a3e5cb8dad36aaee0dbb03c7c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceFile", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df4f99e1c9d6d6264ec8968aef44d44fa86a3718aa5af43d31f24cffb4c437a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)


@jsii.data_type(
    jsii_type="archive.file.FileConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "output_path": "outputPath",
        "type": "type",
        "excludes": "excludes",
        "exclude_symlink_directories": "excludeSymlinkDirectories",
        "output_file_mode": "outputFileMode",
        "source": "source",
        "source_content": "sourceContent",
        "source_content_filename": "sourceContentFilename",
        "source_dir": "sourceDir",
        "source_file": "sourceFile",
    },
)
class FileConfig(_cdktf_9a9027ec.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
        output_path: builtins.str,
        type: builtins.str,
        excludes: typing.Optional[typing.Sequence[builtins.str]] = None,
        exclude_symlink_directories: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        output_file_mode: typing.Optional[builtins.str] = None,
        source: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["FileSource", typing.Dict[builtins.str, typing.Any]]]]] = None,
        source_content: typing.Optional[builtins.str] = None,
        source_content_filename: typing.Optional[builtins.str] = None,
        source_dir: typing.Optional[builtins.str] = None,
        source_file: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param output_path: The output of the archive file. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/archive/2.4.0/docs/resources/file#output_path File#output_path}
        :param type: The type of archive to generate. NOTE: ``zip`` is supported. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/archive/2.4.0/docs/resources/file#type File#type}
        :param excludes: Specify files to ignore when reading the ``source_dir``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/archive/2.4.0/docs/resources/file#excludes File#excludes}
        :param exclude_symlink_directories: Boolean flag indicating whether symbolically linked directories should be excluded during the creation of the archive. Defaults to false. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/archive/2.4.0/docs/resources/file#exclude_symlink_directories File#exclude_symlink_directories}
        :param output_file_mode: String that specifies the octal file mode for all archived files. For example: ``"0666"``. Setting this will ensure that cross platform usage of this module will not vary the modes of archived files (and ultimately checksums) resulting in more deterministic behavior. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/archive/2.4.0/docs/resources/file#output_file_mode File#output_file_mode}
        :param source: source block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/archive/2.4.0/docs/resources/file#source File#source}
        :param source_content: Add only this content to the archive with ``source_content_filename`` as the filename. One and only one of ``source``, ``source_content_filename`` (with ``source_content``), ``source_file``, or ``source_dir`` must be specified. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/archive/2.4.0/docs/resources/file#source_content File#source_content}
        :param source_content_filename: Set this as the filename when using ``source_content``. One and only one of ``source``, ``source_content_filename`` (with ``source_content``), ``source_file``, or ``source_dir`` must be specified. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/archive/2.4.0/docs/resources/file#source_content_filename File#source_content_filename}
        :param source_dir: Package entire contents of this directory into the archive. One and only one of ``source``, ``source_content_filename`` (with ``source_content``), ``source_file``, or ``source_dir`` must be specified. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/archive/2.4.0/docs/resources/file#source_dir File#source_dir}
        :param source_file: Package this file into the archive. One and only one of ``source``, ``source_content_filename`` (with ``source_content``), ``source_file``, or ``source_dir`` must be specified. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/archive/2.4.0/docs/resources/file#source_file File#source_file}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a257e58df775399c33c8b76196ffcbeb115c43e2675f74707778bed8a1a9d7a5)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument output_path", value=output_path, expected_type=type_hints["output_path"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument excludes", value=excludes, expected_type=type_hints["excludes"])
            check_type(argname="argument exclude_symlink_directories", value=exclude_symlink_directories, expected_type=type_hints["exclude_symlink_directories"])
            check_type(argname="argument output_file_mode", value=output_file_mode, expected_type=type_hints["output_file_mode"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument source_content", value=source_content, expected_type=type_hints["source_content"])
            check_type(argname="argument source_content_filename", value=source_content_filename, expected_type=type_hints["source_content_filename"])
            check_type(argname="argument source_dir", value=source_dir, expected_type=type_hints["source_dir"])
            check_type(argname="argument source_file", value=source_file, expected_type=type_hints["source_file"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "output_path": output_path,
            "type": type,
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
        if excludes is not None:
            self._values["excludes"] = excludes
        if exclude_symlink_directories is not None:
            self._values["exclude_symlink_directories"] = exclude_symlink_directories
        if output_file_mode is not None:
            self._values["output_file_mode"] = output_file_mode
        if source is not None:
            self._values["source"] = source
        if source_content is not None:
            self._values["source_content"] = source_content
        if source_content_filename is not None:
            self._values["source_content_filename"] = source_content_filename
        if source_dir is not None:
            self._values["source_dir"] = source_dir
        if source_file is not None:
            self._values["source_file"] = source_file

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
    def count(
        self,
    ) -> typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]], result)

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
    def output_path(self) -> builtins.str:
        '''The output of the archive file.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/archive/2.4.0/docs/resources/file#output_path File#output_path}
        '''
        result = self._values.get("output_path")
        assert result is not None, "Required property 'output_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of archive to generate. NOTE: ``zip`` is supported.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/archive/2.4.0/docs/resources/file#type File#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def excludes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify files to ignore when reading the ``source_dir``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/archive/2.4.0/docs/resources/file#excludes File#excludes}
        '''
        result = self._values.get("excludes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def exclude_symlink_directories(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Boolean flag indicating whether symbolically linked directories should be excluded during the creation of the archive. Defaults to false.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/archive/2.4.0/docs/resources/file#exclude_symlink_directories File#exclude_symlink_directories}
        '''
        result = self._values.get("exclude_symlink_directories")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def output_file_mode(self) -> typing.Optional[builtins.str]:
        '''String that specifies the octal file mode for all archived files.

        For example: ``"0666"``. Setting this will ensure that cross platform usage of this module will not vary the modes of archived files (and ultimately checksums) resulting in more deterministic behavior.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/archive/2.4.0/docs/resources/file#output_file_mode File#output_file_mode}
        '''
        result = self._values.get("output_file_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["FileSource"]]]:
        '''source block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/archive/2.4.0/docs/resources/file#source File#source}
        '''
        result = self._values.get("source")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["FileSource"]]], result)

    @builtins.property
    def source_content(self) -> typing.Optional[builtins.str]:
        '''Add only this content to the archive with ``source_content_filename`` as the filename.

        One and only one of ``source``, ``source_content_filename`` (with ``source_content``), ``source_file``, or ``source_dir`` must be specified.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/archive/2.4.0/docs/resources/file#source_content File#source_content}
        '''
        result = self._values.get("source_content")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_content_filename(self) -> typing.Optional[builtins.str]:
        '''Set this as the filename when using ``source_content``.

        One and only one of ``source``, ``source_content_filename`` (with ``source_content``), ``source_file``, or ``source_dir`` must be specified.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/archive/2.4.0/docs/resources/file#source_content_filename File#source_content_filename}
        '''
        result = self._values.get("source_content_filename")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_dir(self) -> typing.Optional[builtins.str]:
        '''Package entire contents of this directory into the archive.

        One and only one of ``source``, ``source_content_filename`` (with ``source_content``), ``source_file``, or ``source_dir`` must be specified.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/archive/2.4.0/docs/resources/file#source_dir File#source_dir}
        '''
        result = self._values.get("source_dir")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_file(self) -> typing.Optional[builtins.str]:
        '''Package this file into the archive.

        One and only one of ``source``, ``source_content_filename`` (with ``source_content``), ``source_file``, or ``source_dir`` must be specified.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/archive/2.4.0/docs/resources/file#source_file File#source_file}
        '''
        result = self._values.get("source_file")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FileConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="archive.file.FileSource",
    jsii_struct_bases=[],
    name_mapping={"content": "content", "filename": "filename"},
)
class FileSource:
    def __init__(self, *, content: builtins.str, filename: builtins.str) -> None:
        '''
        :param content: Add this content to the archive with ``filename`` as the filename. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/archive/2.4.0/docs/resources/file#content File#content}
        :param filename: Set this as the filename when declaring a ``source``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/archive/2.4.0/docs/resources/file#filename File#filename}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86a61218108eda0d8c6b8ba18cec03b02e2b0af2ae504247123c2034de4b07c3)
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument filename", value=filename, expected_type=type_hints["filename"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "content": content,
            "filename": filename,
        }

    @builtins.property
    def content(self) -> builtins.str:
        '''Add this content to the archive with ``filename`` as the filename.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/archive/2.4.0/docs/resources/file#content File#content}
        '''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def filename(self) -> builtins.str:
        '''Set this as the filename when declaring a ``source``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/archive/2.4.0/docs/resources/file#filename File#filename}
        '''
        result = self._values.get("filename")
        assert result is not None, "Required property 'filename' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FileSource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FileSourceList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="archive.file.FileSourceList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0928e95715b12fb452e8ba23681f3c27a80e8b29beec4fced9b1a199e7af92fb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "FileSourceOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a30d78c6befbc67b047bc4f7a0c5f5dfcc9ed32acc9be5c5adce32c5a522d2c)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("FileSourceOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d8c7613c700a4e0ffc2e09e335a79e54d28a25cf019ee7c581de29e1800335e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9910c00269ad9d1bd640d90f362d1557e76ea2db0c7c0b7449cfd4c4c2808f4c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a8711917087684eefd1ad2b46912ce77a8b4c12aeba0a36d8eeb37ce639f0da6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[FileSource]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[FileSource]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[FileSource]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a1a72b2f9120b97c96fd7628d15447a63ff5439cb99008a16f4edad26fa8bdb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class FileSourceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="archive.file.FileSourceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__be70feb9d04e06d9abfe30d98a2ae8034838b4e0c5ff14f045b9f97a4a1e2e36)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="contentInput")
    def content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentInput"))

    @builtins.property
    @jsii.member(jsii_name="filenameInput")
    def filename_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filenameInput"))

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d673775379d5f9417f4a26f65bece1347b065604a29a19b00b4d950dc784b42e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="filename")
    def filename(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "filename"))

    @filename.setter
    def filename(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2046e691e3d8575e7d53751a94753fd4c2ec1270eb97757f83c3c8600c1ff2a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filename", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, FileSource]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, FileSource]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, FileSource]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__304b351b0a5f4f19fe74cae7af9e52a2095847672faf31c7ff1e8e9af148041e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "File",
    "FileConfig",
    "FileSource",
    "FileSourceList",
    "FileSourceOutputReference",
]

publication.publish()

def _typecheckingstub__c7ee412048fe6f8f8924e3c1fc966fa39c82747cdee6bb81cf01e646f77bce2b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    output_path: builtins.str,
    type: builtins.str,
    excludes: typing.Optional[typing.Sequence[builtins.str]] = None,
    exclude_symlink_directories: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    output_file_mode: typing.Optional[builtins.str] = None,
    source: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[FileSource, typing.Dict[builtins.str, typing.Any]]]]] = None,
    source_content: typing.Optional[builtins.str] = None,
    source_content_filename: typing.Optional[builtins.str] = None,
    source_dir: typing.Optional[builtins.str] = None,
    source_file: typing.Optional[builtins.str] = None,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3197d3b4b4d2d85cbc957dfc0ecf072bfb30ec9237589b33029ab917f891484(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[FileSource, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ba868880f20e445dba8ade3e97c19c001295dab858ac8b79f58238da03f9394(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e0be0c26154dac5ef315b71f277bf19195d0dbfeb89bbd119d1cab23fc257de(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fb6d1395d9b7726bf0047dff5e6c9eee35bf761683e44c2fe839f81b94a5a1e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c18d7713cf9b29421b1019f4bba6e873e6860f779271d020e717d8f649f99f46(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a8e9ea58e1dad4c16b9980e7b3b6375efa984070dffd9cc89e0eff77345cfe7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fff1b1545daced3c67ebf16ea981c72697c4a3207e6e7d7dc2574fa61e055535(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8b479734081d511084002c8e0f523a539cf9d389043a60ee7b422d7f1c1f224(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94ca3cee3d5cee67c76fefbca08e9c5294b4ea6a3e5cb8dad36aaee0dbb03c7c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df4f99e1c9d6d6264ec8968aef44d44fa86a3718aa5af43d31f24cffb4c437a4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a257e58df775399c33c8b76196ffcbeb115c43e2675f74707778bed8a1a9d7a5(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    output_path: builtins.str,
    type: builtins.str,
    excludes: typing.Optional[typing.Sequence[builtins.str]] = None,
    exclude_symlink_directories: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    output_file_mode: typing.Optional[builtins.str] = None,
    source: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[FileSource, typing.Dict[builtins.str, typing.Any]]]]] = None,
    source_content: typing.Optional[builtins.str] = None,
    source_content_filename: typing.Optional[builtins.str] = None,
    source_dir: typing.Optional[builtins.str] = None,
    source_file: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86a61218108eda0d8c6b8ba18cec03b02e2b0af2ae504247123c2034de4b07c3(
    *,
    content: builtins.str,
    filename: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0928e95715b12fb452e8ba23681f3c27a80e8b29beec4fced9b1a199e7af92fb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a30d78c6befbc67b047bc4f7a0c5f5dfcc9ed32acc9be5c5adce32c5a522d2c(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d8c7613c700a4e0ffc2e09e335a79e54d28a25cf019ee7c581de29e1800335e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9910c00269ad9d1bd640d90f362d1557e76ea2db0c7c0b7449cfd4c4c2808f4c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8711917087684eefd1ad2b46912ce77a8b4c12aeba0a36d8eeb37ce639f0da6(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a1a72b2f9120b97c96fd7628d15447a63ff5439cb99008a16f4edad26fa8bdb(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[FileSource]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be70feb9d04e06d9abfe30d98a2ae8034838b4e0c5ff14f045b9f97a4a1e2e36(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d673775379d5f9417f4a26f65bece1347b065604a29a19b00b4d950dc784b42e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2046e691e3d8575e7d53751a94753fd4c2ec1270eb97757f83c3c8600c1ff2a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__304b351b0a5f4f19fe74cae7af9e52a2095847672faf31c7ff1e8e9af148041e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, FileSource]],
) -> None:
    """Type checking stubs"""
    pass
