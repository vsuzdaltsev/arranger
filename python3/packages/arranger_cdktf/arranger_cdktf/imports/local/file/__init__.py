'''
# `local_file`

Refer to the Terraform Registory for docs: [`local_file`](https://www.terraform.io/docs/providers/local/r/file).
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
    jsii_type="local.file.File",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/local/r/file local_file}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        filename: builtins.str,
        content: typing.Optional[builtins.str] = None,
        content_base64: typing.Optional[builtins.str] = None,
        directory_permission: typing.Optional[builtins.str] = None,
        file_permission: typing.Optional[builtins.str] = None,
        sensitive_content: typing.Optional[builtins.str] = None,
        source: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/local/r/file local_file} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param filename: The path to the file that will be created. Missing parent directories will be created. If the file already exists, it will be overridden with the given content. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/local/r/file#filename File#filename}
        :param content: Content to store in the file, expected to be a UTF-8 encoded string. Conflicts with ``sensitive_content``, ``content_base64`` and ``source``. Exactly one of these four arguments must be specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/local/r/file#content File#content}
        :param content_base64: Content to store in the file, expected to be binary encoded as base64 string. Conflicts with ``content``, ``sensitive_content`` and ``source``. Exactly one of these four arguments must be specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/local/r/file#content_base64 File#content_base64}
        :param directory_permission: Permissions to set for directories created (before umask), expressed as string in `numeric notation <https://en.wikipedia.org/wiki/File-system_permissions#Numeric_notation>`_. Default value is ``"0777"``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/local/r/file#directory_permission File#directory_permission}
        :param file_permission: Permissions to set for the output file (before umask), expressed as string in `numeric notation <https://en.wikipedia.org/wiki/File-system_permissions#Numeric_notation>`_. Default value is ``"0777"``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/local/r/file#file_permission File#file_permission}
        :param sensitive_content: Sensitive content to store in the file, expected to be an UTF-8 encoded string. Will not be displayed in diffs. Conflicts with ``content``, ``content_base64`` and ``source``. Exactly one of these four arguments must be specified. If in need to use *sensitive* content, please use the ```local_sensitive_file`` <./sensitive_file.html>`_ resource instead. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/local/r/file#sensitive_content File#sensitive_content}
        :param source: Path to file to use as source for the one we are creating. Conflicts with ``content``, ``sensitive_content`` and ``content_base64``. Exactly one of these four arguments must be specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/local/r/file#source File#source}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5320dce262c26b03d92948f0a4a5a38119b9d557506315430d8c29a373a8da4f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = FileConfig(
            filename=filename,
            content=content,
            content_base64=content_base64,
            directory_permission=directory_permission,
            file_permission=file_permission,
            sensitive_content=sensitive_content,
            source=source,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetContent")
    def reset_content(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContent", []))

    @jsii.member(jsii_name="resetContentBase64")
    def reset_content_base64(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentBase64", []))

    @jsii.member(jsii_name="resetDirectoryPermission")
    def reset_directory_permission(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDirectoryPermission", []))

    @jsii.member(jsii_name="resetFilePermission")
    def reset_file_permission(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilePermission", []))

    @jsii.member(jsii_name="resetSensitiveContent")
    def reset_sensitive_content(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSensitiveContent", []))

    @jsii.member(jsii_name="resetSource")
    def reset_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSource", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="contentBase64Sha256")
    def content_base64_sha256(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentBase64Sha256"))

    @builtins.property
    @jsii.member(jsii_name="contentBase64Sha512")
    def content_base64_sha512(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentBase64Sha512"))

    @builtins.property
    @jsii.member(jsii_name="contentMd5")
    def content_md5(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentMd5"))

    @builtins.property
    @jsii.member(jsii_name="contentSha1")
    def content_sha1(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentSha1"))

    @builtins.property
    @jsii.member(jsii_name="contentSha256")
    def content_sha256(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentSha256"))

    @builtins.property
    @jsii.member(jsii_name="contentSha512")
    def content_sha512(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentSha512"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="contentBase64Input")
    def content_base64_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentBase64Input"))

    @builtins.property
    @jsii.member(jsii_name="contentInput")
    def content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentInput"))

    @builtins.property
    @jsii.member(jsii_name="directoryPermissionInput")
    def directory_permission_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "directoryPermissionInput"))

    @builtins.property
    @jsii.member(jsii_name="filenameInput")
    def filename_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filenameInput"))

    @builtins.property
    @jsii.member(jsii_name="filePermissionInput")
    def file_permission_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filePermissionInput"))

    @builtins.property
    @jsii.member(jsii_name="sensitiveContentInput")
    def sensitive_content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sensitiveContentInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceInput")
    def source_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceInput"))

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__861268ddfc47222dbd86ea65466a7716ec8301a27526f4d61756dbbb3b14474b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="contentBase64")
    def content_base64(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentBase64"))

    @content_base64.setter
    def content_base64(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0cc406aa3b28524cd56570e3c2f4494b8720b4aad6a4aa04898af8c8fe98d815)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentBase64", value)

    @builtins.property
    @jsii.member(jsii_name="directoryPermission")
    def directory_permission(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "directoryPermission"))

    @directory_permission.setter
    def directory_permission(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e25f941381c12ec87ed805b1080101c01c211b4fc2acec551432c2f0673eae9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "directoryPermission", value)

    @builtins.property
    @jsii.member(jsii_name="filename")
    def filename(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "filename"))

    @filename.setter
    def filename(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__765a84efd5963d8655ba3e6f6ab8bc30c8dc7d5dd3fdbc5b3a34495ce9bfcb0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filename", value)

    @builtins.property
    @jsii.member(jsii_name="filePermission")
    def file_permission(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "filePermission"))

    @file_permission.setter
    def file_permission(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdee4422f97dff3ab72331ca292bc76c93b2be5235eebcd94ab99e9d6cc474d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filePermission", value)

    @builtins.property
    @jsii.member(jsii_name="sensitiveContent")
    def sensitive_content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sensitiveContent"))

    @sensitive_content.setter
    def sensitive_content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02b745448c918767027663905a5dae1b4baf7ba3c7ea8c4de021cf42839da350)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sensitiveContent", value)

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "source"))

    @source.setter
    def source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c433d7a31c6e6679571d804f138f802021a1f7df9321f661521a393364dfc173)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value)


@jsii.data_type(
    jsii_type="local.file.FileConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "filename": "filename",
        "content": "content",
        "content_base64": "contentBase64",
        "directory_permission": "directoryPermission",
        "file_permission": "filePermission",
        "sensitive_content": "sensitiveContent",
        "source": "source",
    },
)
class FileConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        filename: builtins.str,
        content: typing.Optional[builtins.str] = None,
        content_base64: typing.Optional[builtins.str] = None,
        directory_permission: typing.Optional[builtins.str] = None,
        file_permission: typing.Optional[builtins.str] = None,
        sensitive_content: typing.Optional[builtins.str] = None,
        source: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param filename: The path to the file that will be created. Missing parent directories will be created. If the file already exists, it will be overridden with the given content. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/local/r/file#filename File#filename}
        :param content: Content to store in the file, expected to be a UTF-8 encoded string. Conflicts with ``sensitive_content``, ``content_base64`` and ``source``. Exactly one of these four arguments must be specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/local/r/file#content File#content}
        :param content_base64: Content to store in the file, expected to be binary encoded as base64 string. Conflicts with ``content``, ``sensitive_content`` and ``source``. Exactly one of these four arguments must be specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/local/r/file#content_base64 File#content_base64}
        :param directory_permission: Permissions to set for directories created (before umask), expressed as string in `numeric notation <https://en.wikipedia.org/wiki/File-system_permissions#Numeric_notation>`_. Default value is ``"0777"``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/local/r/file#directory_permission File#directory_permission}
        :param file_permission: Permissions to set for the output file (before umask), expressed as string in `numeric notation <https://en.wikipedia.org/wiki/File-system_permissions#Numeric_notation>`_. Default value is ``"0777"``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/local/r/file#file_permission File#file_permission}
        :param sensitive_content: Sensitive content to store in the file, expected to be an UTF-8 encoded string. Will not be displayed in diffs. Conflicts with ``content``, ``content_base64`` and ``source``. Exactly one of these four arguments must be specified. If in need to use *sensitive* content, please use the ```local_sensitive_file`` <./sensitive_file.html>`_ resource instead. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/local/r/file#sensitive_content File#sensitive_content}
        :param source: Path to file to use as source for the one we are creating. Conflicts with ``content``, ``sensitive_content`` and ``content_base64``. Exactly one of these four arguments must be specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/local/r/file#source File#source}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5763406b0395af49601708b9200c113749d9be3537456492e34bea01eeca2b3e)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument filename", value=filename, expected_type=type_hints["filename"])
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument content_base64", value=content_base64, expected_type=type_hints["content_base64"])
            check_type(argname="argument directory_permission", value=directory_permission, expected_type=type_hints["directory_permission"])
            check_type(argname="argument file_permission", value=file_permission, expected_type=type_hints["file_permission"])
            check_type(argname="argument sensitive_content", value=sensitive_content, expected_type=type_hints["sensitive_content"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "filename": filename,
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
        if content is not None:
            self._values["content"] = content
        if content_base64 is not None:
            self._values["content_base64"] = content_base64
        if directory_permission is not None:
            self._values["directory_permission"] = directory_permission
        if file_permission is not None:
            self._values["file_permission"] = file_permission
        if sensitive_content is not None:
            self._values["sensitive_content"] = sensitive_content
        if source is not None:
            self._values["source"] = source

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
    def filename(self) -> builtins.str:
        '''The path to the file that will be created.

        Missing parent directories will be created.
        If the file already exists, it will be overridden with the given content.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/local/r/file#filename File#filename}
        '''
        result = self._values.get("filename")
        assert result is not None, "Required property 'filename' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content(self) -> typing.Optional[builtins.str]:
        '''Content to store in the file, expected to be a UTF-8 encoded string.

        Conflicts with ``sensitive_content``, ``content_base64`` and ``source``.
        Exactly one of these four arguments must be specified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/local/r/file#content File#content}
        '''
        result = self._values.get("content")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def content_base64(self) -> typing.Optional[builtins.str]:
        '''Content to store in the file, expected to be binary encoded as base64 string.

        Conflicts with ``content``, ``sensitive_content`` and ``source``.
        Exactly one of these four arguments must be specified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/local/r/file#content_base64 File#content_base64}
        '''
        result = self._values.get("content_base64")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def directory_permission(self) -> typing.Optional[builtins.str]:
        '''Permissions to set for directories created (before umask), expressed as string in `numeric notation <https://en.wikipedia.org/wiki/File-system_permissions#Numeric_notation>`_. Default value is ``"0777"``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/local/r/file#directory_permission File#directory_permission}
        '''
        result = self._values.get("directory_permission")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def file_permission(self) -> typing.Optional[builtins.str]:
        '''Permissions to set for the output file (before umask), expressed as string in `numeric notation <https://en.wikipedia.org/wiki/File-system_permissions#Numeric_notation>`_. Default value is ``"0777"``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/local/r/file#file_permission File#file_permission}
        '''
        result = self._values.get("file_permission")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sensitive_content(self) -> typing.Optional[builtins.str]:
        '''Sensitive content to store in the file, expected to be an UTF-8 encoded string.

        Will not be displayed in diffs.
        Conflicts with ``content``, ``content_base64`` and ``source``.
        Exactly one of these four arguments must be specified.
        If in need to use *sensitive* content, please use the ```local_sensitive_file`` <./sensitive_file.html>`_
        resource instead.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/local/r/file#sensitive_content File#sensitive_content}
        '''
        result = self._values.get("sensitive_content")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source(self) -> typing.Optional[builtins.str]:
        '''Path to file to use as source for the one we are creating.

        Conflicts with ``content``, ``sensitive_content`` and ``content_base64``.
        Exactly one of these four arguments must be specified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/local/r/file#source File#source}
        '''
        result = self._values.get("source")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FileConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "File",
    "FileConfig",
]

publication.publish()

def _typecheckingstub__5320dce262c26b03d92948f0a4a5a38119b9d557506315430d8c29a373a8da4f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    filename: builtins.str,
    content: typing.Optional[builtins.str] = None,
    content_base64: typing.Optional[builtins.str] = None,
    directory_permission: typing.Optional[builtins.str] = None,
    file_permission: typing.Optional[builtins.str] = None,
    sensitive_content: typing.Optional[builtins.str] = None,
    source: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__861268ddfc47222dbd86ea65466a7716ec8301a27526f4d61756dbbb3b14474b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cc406aa3b28524cd56570e3c2f4494b8720b4aad6a4aa04898af8c8fe98d815(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e25f941381c12ec87ed805b1080101c01c211b4fc2acec551432c2f0673eae9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__765a84efd5963d8655ba3e6f6ab8bc30c8dc7d5dd3fdbc5b3a34495ce9bfcb0c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdee4422f97dff3ab72331ca292bc76c93b2be5235eebcd94ab99e9d6cc474d5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02b745448c918767027663905a5dae1b4baf7ba3c7ea8c4de021cf42839da350(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c433d7a31c6e6679571d804f138f802021a1f7df9321f661521a393364dfc173(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5763406b0395af49601708b9200c113749d9be3537456492e34bea01eeca2b3e(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    filename: builtins.str,
    content: typing.Optional[builtins.str] = None,
    content_base64: typing.Optional[builtins.str] = None,
    directory_permission: typing.Optional[builtins.str] = None,
    file_permission: typing.Optional[builtins.str] = None,
    sensitive_content: typing.Optional[builtins.str] = None,
    source: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
