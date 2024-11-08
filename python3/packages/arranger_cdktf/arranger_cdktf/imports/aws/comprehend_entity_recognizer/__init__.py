'''
# `aws_comprehend_entity_recognizer`

Refer to the Terraform Registory for docs: [`aws_comprehend_entity_recognizer`](https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer).
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


class ComprehendEntityRecognizer(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.comprehendEntityRecognizer.ComprehendEntityRecognizer",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer aws_comprehend_entity_recognizer}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        data_access_role_arn: builtins.str,
        input_data_config: typing.Union["ComprehendEntityRecognizerInputDataConfig", typing.Dict[builtins.str, typing.Any]],
        language_code: builtins.str,
        name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        model_kms_key_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ComprehendEntityRecognizerTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        version_name: typing.Optional[builtins.str] = None,
        version_name_prefix: typing.Optional[builtins.str] = None,
        volume_kms_key_id: typing.Optional[builtins.str] = None,
        vpc_config: typing.Optional[typing.Union["ComprehendEntityRecognizerVpcConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer aws_comprehend_entity_recognizer} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param data_access_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#data_access_role_arn ComprehendEntityRecognizer#data_access_role_arn}.
        :param input_data_config: input_data_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#input_data_config ComprehendEntityRecognizer#input_data_config}
        :param language_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#language_code ComprehendEntityRecognizer#language_code}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#name ComprehendEntityRecognizer#name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#id ComprehendEntityRecognizer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param model_kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#model_kms_key_id ComprehendEntityRecognizer#model_kms_key_id}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#tags ComprehendEntityRecognizer#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#tags_all ComprehendEntityRecognizer#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#timeouts ComprehendEntityRecognizer#timeouts}
        :param version_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#version_name ComprehendEntityRecognizer#version_name}.
        :param version_name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#version_name_prefix ComprehendEntityRecognizer#version_name_prefix}.
        :param volume_kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#volume_kms_key_id ComprehendEntityRecognizer#volume_kms_key_id}.
        :param vpc_config: vpc_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#vpc_config ComprehendEntityRecognizer#vpc_config}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e824471da268ba99e1656b5386bdc1b91a2a4a522df1f525d9be53d9745f59a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ComprehendEntityRecognizerConfig(
            data_access_role_arn=data_access_role_arn,
            input_data_config=input_data_config,
            language_code=language_code,
            name=name,
            id=id,
            model_kms_key_id=model_kms_key_id,
            tags=tags,
            tags_all=tags_all,
            timeouts=timeouts,
            version_name=version_name,
            version_name_prefix=version_name_prefix,
            volume_kms_key_id=volume_kms_key_id,
            vpc_config=vpc_config,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putInputDataConfig")
    def put_input_data_config(
        self,
        *,
        entity_types: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ComprehendEntityRecognizerInputDataConfigEntityTypes", typing.Dict[builtins.str, typing.Any]]]],
        annotations: typing.Optional[typing.Union["ComprehendEntityRecognizerInputDataConfigAnnotations", typing.Dict[builtins.str, typing.Any]]] = None,
        augmented_manifests: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ComprehendEntityRecognizerInputDataConfigAugmentedManifests", typing.Dict[builtins.str, typing.Any]]]]] = None,
        data_format: typing.Optional[builtins.str] = None,
        documents: typing.Optional[typing.Union["ComprehendEntityRecognizerInputDataConfigDocuments", typing.Dict[builtins.str, typing.Any]]] = None,
        entity_list: typing.Optional[typing.Union["ComprehendEntityRecognizerInputDataConfigEntityList", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param entity_types: entity_types block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#entity_types ComprehendEntityRecognizer#entity_types}
        :param annotations: annotations block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#annotations ComprehendEntityRecognizer#annotations}
        :param augmented_manifests: augmented_manifests block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#augmented_manifests ComprehendEntityRecognizer#augmented_manifests}
        :param data_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#data_format ComprehendEntityRecognizer#data_format}.
        :param documents: documents block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#documents ComprehendEntityRecognizer#documents}
        :param entity_list: entity_list block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#entity_list ComprehendEntityRecognizer#entity_list}
        '''
        value = ComprehendEntityRecognizerInputDataConfig(
            entity_types=entity_types,
            annotations=annotations,
            augmented_manifests=augmented_manifests,
            data_format=data_format,
            documents=documents,
            entity_list=entity_list,
        )

        return typing.cast(None, jsii.invoke(self, "putInputDataConfig", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#create ComprehendEntityRecognizer#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#delete ComprehendEntityRecognizer#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#update ComprehendEntityRecognizer#update}.
        '''
        value = ComprehendEntityRecognizerTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putVpcConfig")
    def put_vpc_config(
        self,
        *,
        security_group_ids: typing.Sequence[builtins.str],
        subnets: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#security_group_ids ComprehendEntityRecognizer#security_group_ids}.
        :param subnets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#subnets ComprehendEntityRecognizer#subnets}.
        '''
        value = ComprehendEntityRecognizerVpcConfig(
            security_group_ids=security_group_ids, subnets=subnets
        )

        return typing.cast(None, jsii.invoke(self, "putVpcConfig", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetModelKmsKeyId")
    def reset_model_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetModelKmsKeyId", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetVersionName")
    def reset_version_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersionName", []))

    @jsii.member(jsii_name="resetVersionNamePrefix")
    def reset_version_name_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersionNamePrefix", []))

    @jsii.member(jsii_name="resetVolumeKmsKeyId")
    def reset_volume_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumeKmsKeyId", []))

    @jsii.member(jsii_name="resetVpcConfig")
    def reset_vpc_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpcConfig", []))

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
    @jsii.member(jsii_name="inputDataConfig")
    def input_data_config(
        self,
    ) -> "ComprehendEntityRecognizerInputDataConfigOutputReference":
        return typing.cast("ComprehendEntityRecognizerInputDataConfigOutputReference", jsii.get(self, "inputDataConfig"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ComprehendEntityRecognizerTimeoutsOutputReference":
        return typing.cast("ComprehendEntityRecognizerTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="vpcConfig")
    def vpc_config(self) -> "ComprehendEntityRecognizerVpcConfigOutputReference":
        return typing.cast("ComprehendEntityRecognizerVpcConfigOutputReference", jsii.get(self, "vpcConfig"))

    @builtins.property
    @jsii.member(jsii_name="dataAccessRoleArnInput")
    def data_access_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataAccessRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="inputDataConfigInput")
    def input_data_config_input(
        self,
    ) -> typing.Optional["ComprehendEntityRecognizerInputDataConfig"]:
        return typing.cast(typing.Optional["ComprehendEntityRecognizerInputDataConfig"], jsii.get(self, "inputDataConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="languageCodeInput")
    def language_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "languageCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="modelKmsKeyIdInput")
    def model_kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modelKmsKeyIdInput"))

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
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["ComprehendEntityRecognizerTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ComprehendEntityRecognizerTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="versionNameInput")
    def version_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionNameInput"))

    @builtins.property
    @jsii.member(jsii_name="versionNamePrefixInput")
    def version_name_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionNamePrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeKmsKeyIdInput")
    def volume_kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeKmsKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcConfigInput")
    def vpc_config_input(
        self,
    ) -> typing.Optional["ComprehendEntityRecognizerVpcConfig"]:
        return typing.cast(typing.Optional["ComprehendEntityRecognizerVpcConfig"], jsii.get(self, "vpcConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="dataAccessRoleArn")
    def data_access_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataAccessRoleArn"))

    @data_access_role_arn.setter
    def data_access_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__764b22c695dcce3f1f8e0ae59ecdc00a0fe36b5885e4b27f18d6afd099056fd7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataAccessRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35583f3b52d917dc40e4571bc985aad26efeebfa4c7db12d405dc5c2623fae48)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="languageCode")
    def language_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "languageCode"))

    @language_code.setter
    def language_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05896076a428d6553ebc01185fd8f5fbad39b5223840c3023bd2b2891dd29f13)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "languageCode", value)

    @builtins.property
    @jsii.member(jsii_name="modelKmsKeyId")
    def model_kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "modelKmsKeyId"))

    @model_kms_key_id.setter
    def model_kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7061fd1c9509465cb368cd9851d3544c03907b637576123756fa753f8095b57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "modelKmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a3d0492dcc0c102043f5fa8a19269976be1d3fac106d823d30ef07b24e8ba68)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58827e7a9c6ab511a2601833d6003a40c5ad8ad5c245568857afd7b66c1986c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1d07face4a26985ef0538749b8c5bafa62ead8fcac59530871c2e1aff425710)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="versionName")
    def version_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "versionName"))

    @version_name.setter
    def version_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4a4fd6040f1ccc1eae5554949d114d85fd4fdd52ece9c9d98102ed8a0692788)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "versionName", value)

    @builtins.property
    @jsii.member(jsii_name="versionNamePrefix")
    def version_name_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "versionNamePrefix"))

    @version_name_prefix.setter
    def version_name_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52cb1a3ad8bb78a7ef7315d4c8290f807b82383f8ccaa7f1c14017d6c4a17d23)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "versionNamePrefix", value)

    @builtins.property
    @jsii.member(jsii_name="volumeKmsKeyId")
    def volume_kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeKmsKeyId"))

    @volume_kms_key_id.setter
    def volume_kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3454d6cd8e82aa1a11eca02885fd034c4cb9fe851f8dc7d61d228a6bce2c0872)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeKmsKeyId", value)


@jsii.data_type(
    jsii_type="aws.comprehendEntityRecognizer.ComprehendEntityRecognizerConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "data_access_role_arn": "dataAccessRoleArn",
        "input_data_config": "inputDataConfig",
        "language_code": "languageCode",
        "name": "name",
        "id": "id",
        "model_kms_key_id": "modelKmsKeyId",
        "tags": "tags",
        "tags_all": "tagsAll",
        "timeouts": "timeouts",
        "version_name": "versionName",
        "version_name_prefix": "versionNamePrefix",
        "volume_kms_key_id": "volumeKmsKeyId",
        "vpc_config": "vpcConfig",
    },
)
class ComprehendEntityRecognizerConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        data_access_role_arn: builtins.str,
        input_data_config: typing.Union["ComprehendEntityRecognizerInputDataConfig", typing.Dict[builtins.str, typing.Any]],
        language_code: builtins.str,
        name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        model_kms_key_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ComprehendEntityRecognizerTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        version_name: typing.Optional[builtins.str] = None,
        version_name_prefix: typing.Optional[builtins.str] = None,
        volume_kms_key_id: typing.Optional[builtins.str] = None,
        vpc_config: typing.Optional[typing.Union["ComprehendEntityRecognizerVpcConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param data_access_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#data_access_role_arn ComprehendEntityRecognizer#data_access_role_arn}.
        :param input_data_config: input_data_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#input_data_config ComprehendEntityRecognizer#input_data_config}
        :param language_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#language_code ComprehendEntityRecognizer#language_code}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#name ComprehendEntityRecognizer#name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#id ComprehendEntityRecognizer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param model_kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#model_kms_key_id ComprehendEntityRecognizer#model_kms_key_id}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#tags ComprehendEntityRecognizer#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#tags_all ComprehendEntityRecognizer#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#timeouts ComprehendEntityRecognizer#timeouts}
        :param version_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#version_name ComprehendEntityRecognizer#version_name}.
        :param version_name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#version_name_prefix ComprehendEntityRecognizer#version_name_prefix}.
        :param volume_kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#volume_kms_key_id ComprehendEntityRecognizer#volume_kms_key_id}.
        :param vpc_config: vpc_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#vpc_config ComprehendEntityRecognizer#vpc_config}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(input_data_config, dict):
            input_data_config = ComprehendEntityRecognizerInputDataConfig(**input_data_config)
        if isinstance(timeouts, dict):
            timeouts = ComprehendEntityRecognizerTimeouts(**timeouts)
        if isinstance(vpc_config, dict):
            vpc_config = ComprehendEntityRecognizerVpcConfig(**vpc_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8814f540aa4fbd6032441f45f54386741983ad10afc403cf0e7d4061617bdac)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument data_access_role_arn", value=data_access_role_arn, expected_type=type_hints["data_access_role_arn"])
            check_type(argname="argument input_data_config", value=input_data_config, expected_type=type_hints["input_data_config"])
            check_type(argname="argument language_code", value=language_code, expected_type=type_hints["language_code"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument model_kms_key_id", value=model_kms_key_id, expected_type=type_hints["model_kms_key_id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument version_name", value=version_name, expected_type=type_hints["version_name"])
            check_type(argname="argument version_name_prefix", value=version_name_prefix, expected_type=type_hints["version_name_prefix"])
            check_type(argname="argument volume_kms_key_id", value=volume_kms_key_id, expected_type=type_hints["volume_kms_key_id"])
            check_type(argname="argument vpc_config", value=vpc_config, expected_type=type_hints["vpc_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "data_access_role_arn": data_access_role_arn,
            "input_data_config": input_data_config,
            "language_code": language_code,
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
        if id is not None:
            self._values["id"] = id
        if model_kms_key_id is not None:
            self._values["model_kms_key_id"] = model_kms_key_id
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if version_name is not None:
            self._values["version_name"] = version_name
        if version_name_prefix is not None:
            self._values["version_name_prefix"] = version_name_prefix
        if volume_kms_key_id is not None:
            self._values["volume_kms_key_id"] = volume_kms_key_id
        if vpc_config is not None:
            self._values["vpc_config"] = vpc_config

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
    def data_access_role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#data_access_role_arn ComprehendEntityRecognizer#data_access_role_arn}.'''
        result = self._values.get("data_access_role_arn")
        assert result is not None, "Required property 'data_access_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def input_data_config(self) -> "ComprehendEntityRecognizerInputDataConfig":
        '''input_data_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#input_data_config ComprehendEntityRecognizer#input_data_config}
        '''
        result = self._values.get("input_data_config")
        assert result is not None, "Required property 'input_data_config' is missing"
        return typing.cast("ComprehendEntityRecognizerInputDataConfig", result)

    @builtins.property
    def language_code(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#language_code ComprehendEntityRecognizer#language_code}.'''
        result = self._values.get("language_code")
        assert result is not None, "Required property 'language_code' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#name ComprehendEntityRecognizer#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#id ComprehendEntityRecognizer#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def model_kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#model_kms_key_id ComprehendEntityRecognizer#model_kms_key_id}.'''
        result = self._values.get("model_kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#tags ComprehendEntityRecognizer#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#tags_all ComprehendEntityRecognizer#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ComprehendEntityRecognizerTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#timeouts ComprehendEntityRecognizer#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ComprehendEntityRecognizerTimeouts"], result)

    @builtins.property
    def version_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#version_name ComprehendEntityRecognizer#version_name}.'''
        result = self._values.get("version_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version_name_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#version_name_prefix ComprehendEntityRecognizer#version_name_prefix}.'''
        result = self._values.get("version_name_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def volume_kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#volume_kms_key_id ComprehendEntityRecognizer#volume_kms_key_id}.'''
        result = self._values.get("volume_kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc_config(self) -> typing.Optional["ComprehendEntityRecognizerVpcConfig"]:
        '''vpc_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#vpc_config ComprehendEntityRecognizer#vpc_config}
        '''
        result = self._values.get("vpc_config")
        return typing.cast(typing.Optional["ComprehendEntityRecognizerVpcConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComprehendEntityRecognizerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.comprehendEntityRecognizer.ComprehendEntityRecognizerInputDataConfig",
    jsii_struct_bases=[],
    name_mapping={
        "entity_types": "entityTypes",
        "annotations": "annotations",
        "augmented_manifests": "augmentedManifests",
        "data_format": "dataFormat",
        "documents": "documents",
        "entity_list": "entityList",
    },
)
class ComprehendEntityRecognizerInputDataConfig:
    def __init__(
        self,
        *,
        entity_types: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ComprehendEntityRecognizerInputDataConfigEntityTypes", typing.Dict[builtins.str, typing.Any]]]],
        annotations: typing.Optional[typing.Union["ComprehendEntityRecognizerInputDataConfigAnnotations", typing.Dict[builtins.str, typing.Any]]] = None,
        augmented_manifests: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ComprehendEntityRecognizerInputDataConfigAugmentedManifests", typing.Dict[builtins.str, typing.Any]]]]] = None,
        data_format: typing.Optional[builtins.str] = None,
        documents: typing.Optional[typing.Union["ComprehendEntityRecognizerInputDataConfigDocuments", typing.Dict[builtins.str, typing.Any]]] = None,
        entity_list: typing.Optional[typing.Union["ComprehendEntityRecognizerInputDataConfigEntityList", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param entity_types: entity_types block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#entity_types ComprehendEntityRecognizer#entity_types}
        :param annotations: annotations block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#annotations ComprehendEntityRecognizer#annotations}
        :param augmented_manifests: augmented_manifests block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#augmented_manifests ComprehendEntityRecognizer#augmented_manifests}
        :param data_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#data_format ComprehendEntityRecognizer#data_format}.
        :param documents: documents block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#documents ComprehendEntityRecognizer#documents}
        :param entity_list: entity_list block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#entity_list ComprehendEntityRecognizer#entity_list}
        '''
        if isinstance(annotations, dict):
            annotations = ComprehendEntityRecognizerInputDataConfigAnnotations(**annotations)
        if isinstance(documents, dict):
            documents = ComprehendEntityRecognizerInputDataConfigDocuments(**documents)
        if isinstance(entity_list, dict):
            entity_list = ComprehendEntityRecognizerInputDataConfigEntityList(**entity_list)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba9466e6c5330cd64cd540121c7b3bfb9e573ffe07472db22aa8482ac2129058)
            check_type(argname="argument entity_types", value=entity_types, expected_type=type_hints["entity_types"])
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument augmented_manifests", value=augmented_manifests, expected_type=type_hints["augmented_manifests"])
            check_type(argname="argument data_format", value=data_format, expected_type=type_hints["data_format"])
            check_type(argname="argument documents", value=documents, expected_type=type_hints["documents"])
            check_type(argname="argument entity_list", value=entity_list, expected_type=type_hints["entity_list"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "entity_types": entity_types,
        }
        if annotations is not None:
            self._values["annotations"] = annotations
        if augmented_manifests is not None:
            self._values["augmented_manifests"] = augmented_manifests
        if data_format is not None:
            self._values["data_format"] = data_format
        if documents is not None:
            self._values["documents"] = documents
        if entity_list is not None:
            self._values["entity_list"] = entity_list

    @builtins.property
    def entity_types(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ComprehendEntityRecognizerInputDataConfigEntityTypes"]]:
        '''entity_types block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#entity_types ComprehendEntityRecognizer#entity_types}
        '''
        result = self._values.get("entity_types")
        assert result is not None, "Required property 'entity_types' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ComprehendEntityRecognizerInputDataConfigEntityTypes"]], result)

    @builtins.property
    def annotations(
        self,
    ) -> typing.Optional["ComprehendEntityRecognizerInputDataConfigAnnotations"]:
        '''annotations block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#annotations ComprehendEntityRecognizer#annotations}
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional["ComprehendEntityRecognizerInputDataConfigAnnotations"], result)

    @builtins.property
    def augmented_manifests(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ComprehendEntityRecognizerInputDataConfigAugmentedManifests"]]]:
        '''augmented_manifests block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#augmented_manifests ComprehendEntityRecognizer#augmented_manifests}
        '''
        result = self._values.get("augmented_manifests")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ComprehendEntityRecognizerInputDataConfigAugmentedManifests"]]], result)

    @builtins.property
    def data_format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#data_format ComprehendEntityRecognizer#data_format}.'''
        result = self._values.get("data_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def documents(
        self,
    ) -> typing.Optional["ComprehendEntityRecognizerInputDataConfigDocuments"]:
        '''documents block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#documents ComprehendEntityRecognizer#documents}
        '''
        result = self._values.get("documents")
        return typing.cast(typing.Optional["ComprehendEntityRecognizerInputDataConfigDocuments"], result)

    @builtins.property
    def entity_list(
        self,
    ) -> typing.Optional["ComprehendEntityRecognizerInputDataConfigEntityList"]:
        '''entity_list block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#entity_list ComprehendEntityRecognizer#entity_list}
        '''
        result = self._values.get("entity_list")
        return typing.cast(typing.Optional["ComprehendEntityRecognizerInputDataConfigEntityList"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComprehendEntityRecognizerInputDataConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.comprehendEntityRecognizer.ComprehendEntityRecognizerInputDataConfigAnnotations",
    jsii_struct_bases=[],
    name_mapping={"s3_uri": "s3Uri", "test_s3_uri": "testS3Uri"},
)
class ComprehendEntityRecognizerInputDataConfigAnnotations:
    def __init__(
        self,
        *,
        s3_uri: builtins.str,
        test_s3_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param s3_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#s3_uri ComprehendEntityRecognizer#s3_uri}.
        :param test_s3_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#test_s3_uri ComprehendEntityRecognizer#test_s3_uri}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae734a8edd5e24d2e3e770beac3a86c39db0e03e27276dc6db259acefbc6c658)
            check_type(argname="argument s3_uri", value=s3_uri, expected_type=type_hints["s3_uri"])
            check_type(argname="argument test_s3_uri", value=test_s3_uri, expected_type=type_hints["test_s3_uri"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "s3_uri": s3_uri,
        }
        if test_s3_uri is not None:
            self._values["test_s3_uri"] = test_s3_uri

    @builtins.property
    def s3_uri(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#s3_uri ComprehendEntityRecognizer#s3_uri}.'''
        result = self._values.get("s3_uri")
        assert result is not None, "Required property 's3_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def test_s3_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#test_s3_uri ComprehendEntityRecognizer#test_s3_uri}.'''
        result = self._values.get("test_s3_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComprehendEntityRecognizerInputDataConfigAnnotations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComprehendEntityRecognizerInputDataConfigAnnotationsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.comprehendEntityRecognizer.ComprehendEntityRecognizerInputDataConfigAnnotationsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__799441ae42218800901141f446cea7c32e62353184cdeac76a2d1be010fc8407)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetTestS3Uri")
    def reset_test_s3_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTestS3Uri", []))

    @builtins.property
    @jsii.member(jsii_name="s3UriInput")
    def s3_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3UriInput"))

    @builtins.property
    @jsii.member(jsii_name="testS3UriInput")
    def test_s3_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "testS3UriInput"))

    @builtins.property
    @jsii.member(jsii_name="s3Uri")
    def s3_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3Uri"))

    @s3_uri.setter
    def s3_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3852831f50635d63c66cd1ba88aaca15b9d9de6d948cc046ee6dfee3b851854)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3Uri", value)

    @builtins.property
    @jsii.member(jsii_name="testS3Uri")
    def test_s3_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "testS3Uri"))

    @test_s3_uri.setter
    def test_s3_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8572e29cf5e4a903145c1a325821e991aa994f777eb67b59e3efb827d52b500d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "testS3Uri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComprehendEntityRecognizerInputDataConfigAnnotations]:
        return typing.cast(typing.Optional[ComprehendEntityRecognizerInputDataConfigAnnotations], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComprehendEntityRecognizerInputDataConfigAnnotations],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76febfe7d510233e2b7e74e328e9a8040f63ef0ac0b67cf8b14548ce8714d9da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.comprehendEntityRecognizer.ComprehendEntityRecognizerInputDataConfigAugmentedManifests",
    jsii_struct_bases=[],
    name_mapping={
        "attribute_names": "attributeNames",
        "s3_uri": "s3Uri",
        "annotation_data_s3_uri": "annotationDataS3Uri",
        "document_type": "documentType",
        "source_documents_s3_uri": "sourceDocumentsS3Uri",
        "split": "split",
    },
)
class ComprehendEntityRecognizerInputDataConfigAugmentedManifests:
    def __init__(
        self,
        *,
        attribute_names: typing.Sequence[builtins.str],
        s3_uri: builtins.str,
        annotation_data_s3_uri: typing.Optional[builtins.str] = None,
        document_type: typing.Optional[builtins.str] = None,
        source_documents_s3_uri: typing.Optional[builtins.str] = None,
        split: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param attribute_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#attribute_names ComprehendEntityRecognizer#attribute_names}.
        :param s3_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#s3_uri ComprehendEntityRecognizer#s3_uri}.
        :param annotation_data_s3_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#annotation_data_s3_uri ComprehendEntityRecognizer#annotation_data_s3_uri}.
        :param document_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#document_type ComprehendEntityRecognizer#document_type}.
        :param source_documents_s3_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#source_documents_s3_uri ComprehendEntityRecognizer#source_documents_s3_uri}.
        :param split: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#split ComprehendEntityRecognizer#split}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ca422026ad3b28c8a8851de11829f90194482562148e7461306f80dc8aba575)
            check_type(argname="argument attribute_names", value=attribute_names, expected_type=type_hints["attribute_names"])
            check_type(argname="argument s3_uri", value=s3_uri, expected_type=type_hints["s3_uri"])
            check_type(argname="argument annotation_data_s3_uri", value=annotation_data_s3_uri, expected_type=type_hints["annotation_data_s3_uri"])
            check_type(argname="argument document_type", value=document_type, expected_type=type_hints["document_type"])
            check_type(argname="argument source_documents_s3_uri", value=source_documents_s3_uri, expected_type=type_hints["source_documents_s3_uri"])
            check_type(argname="argument split", value=split, expected_type=type_hints["split"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "attribute_names": attribute_names,
            "s3_uri": s3_uri,
        }
        if annotation_data_s3_uri is not None:
            self._values["annotation_data_s3_uri"] = annotation_data_s3_uri
        if document_type is not None:
            self._values["document_type"] = document_type
        if source_documents_s3_uri is not None:
            self._values["source_documents_s3_uri"] = source_documents_s3_uri
        if split is not None:
            self._values["split"] = split

    @builtins.property
    def attribute_names(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#attribute_names ComprehendEntityRecognizer#attribute_names}.'''
        result = self._values.get("attribute_names")
        assert result is not None, "Required property 'attribute_names' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def s3_uri(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#s3_uri ComprehendEntityRecognizer#s3_uri}.'''
        result = self._values.get("s3_uri")
        assert result is not None, "Required property 's3_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def annotation_data_s3_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#annotation_data_s3_uri ComprehendEntityRecognizer#annotation_data_s3_uri}.'''
        result = self._values.get("annotation_data_s3_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def document_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#document_type ComprehendEntityRecognizer#document_type}.'''
        result = self._values.get("document_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_documents_s3_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#source_documents_s3_uri ComprehendEntityRecognizer#source_documents_s3_uri}.'''
        result = self._values.get("source_documents_s3_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def split(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#split ComprehendEntityRecognizer#split}.'''
        result = self._values.get("split")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComprehendEntityRecognizerInputDataConfigAugmentedManifests(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComprehendEntityRecognizerInputDataConfigAugmentedManifestsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.comprehendEntityRecognizer.ComprehendEntityRecognizerInputDataConfigAugmentedManifestsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1d83ae0452196bbb8a5f41d02576f364b3849c124a44bdfccd5c5f15b45e8d37)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ComprehendEntityRecognizerInputDataConfigAugmentedManifestsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9d0de31c25effe3adbe178ec12135c1a90901cf3fe9ac3739017ff3f123ac01)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ComprehendEntityRecognizerInputDataConfigAugmentedManifestsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb8fc39d910063d94aea7682ea01b9f116a229c476c3231e10b8dd0cc28ac417)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a8dc76c0bd9492c124fe9f9e130ba64b680f3e200c64747515572e1a0ad76c0f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e04c2605555ece9debf34af5c8c2ba793889808d868bfdcf1854b6c94c793355)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ComprehendEntityRecognizerInputDataConfigAugmentedManifests]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ComprehendEntityRecognizerInputDataConfigAugmentedManifests]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ComprehendEntityRecognizerInputDataConfigAugmentedManifests]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__875cbc0f1b45a82fdcf32477152ac4e2d585ca8a877b52cc95f55250d0ea6415)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ComprehendEntityRecognizerInputDataConfigAugmentedManifestsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.comprehendEntityRecognizer.ComprehendEntityRecognizerInputDataConfigAugmentedManifestsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d012596a9f73963ee27989c2cd8cc59697d690b83a53027870f4617bbb50cd99)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAnnotationDataS3Uri")
    def reset_annotation_data_s3_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnnotationDataS3Uri", []))

    @jsii.member(jsii_name="resetDocumentType")
    def reset_document_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDocumentType", []))

    @jsii.member(jsii_name="resetSourceDocumentsS3Uri")
    def reset_source_documents_s3_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceDocumentsS3Uri", []))

    @jsii.member(jsii_name="resetSplit")
    def reset_split(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSplit", []))

    @builtins.property
    @jsii.member(jsii_name="annotationDataS3UriInput")
    def annotation_data_s3_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "annotationDataS3UriInput"))

    @builtins.property
    @jsii.member(jsii_name="attributeNamesInput")
    def attribute_names_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "attributeNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="documentTypeInput")
    def document_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "documentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="s3UriInput")
    def s3_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3UriInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceDocumentsS3UriInput")
    def source_documents_s3_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceDocumentsS3UriInput"))

    @builtins.property
    @jsii.member(jsii_name="splitInput")
    def split_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "splitInput"))

    @builtins.property
    @jsii.member(jsii_name="annotationDataS3Uri")
    def annotation_data_s3_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "annotationDataS3Uri"))

    @annotation_data_s3_uri.setter
    def annotation_data_s3_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3602ef5e70b3a624d7559d37dc0d6f790b90e145c028760ab676d47e8313cbba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "annotationDataS3Uri", value)

    @builtins.property
    @jsii.member(jsii_name="attributeNames")
    def attribute_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attributeNames"))

    @attribute_names.setter
    def attribute_names(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec1528f81b894b6a3f4783699de4a9b18de5f0dcedb672cad0405ab51014bae1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attributeNames", value)

    @builtins.property
    @jsii.member(jsii_name="documentType")
    def document_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "documentType"))

    @document_type.setter
    def document_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__682ebdbae1569fc273d45174e673990bfe67b7d66b977f751bfe597b0bfdd4f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "documentType", value)

    @builtins.property
    @jsii.member(jsii_name="s3Uri")
    def s3_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3Uri"))

    @s3_uri.setter
    def s3_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10de2976fd89692ab81ccc04cce0a32794221199f4ff34054533f73a7028dab7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3Uri", value)

    @builtins.property
    @jsii.member(jsii_name="sourceDocumentsS3Uri")
    def source_documents_s3_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceDocumentsS3Uri"))

    @source_documents_s3_uri.setter
    def source_documents_s3_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b29a866f122c684a4bfd208660e9a62d554ebdde9cca9371af43c5635484a44)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceDocumentsS3Uri", value)

    @builtins.property
    @jsii.member(jsii_name="split")
    def split(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "split"))

    @split.setter
    def split(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b4fabbcdf966ce6f95cead696254228036b36e4f5d11e2a6162296b37d16488)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "split", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ComprehendEntityRecognizerInputDataConfigAugmentedManifests, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ComprehendEntityRecognizerInputDataConfigAugmentedManifests, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ComprehendEntityRecognizerInputDataConfigAugmentedManifests, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c017b2bbe5044589d623e45682e0599972cd96802393fcefc1a1f54618266bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.comprehendEntityRecognizer.ComprehendEntityRecognizerInputDataConfigDocuments",
    jsii_struct_bases=[],
    name_mapping={
        "s3_uri": "s3Uri",
        "input_format": "inputFormat",
        "test_s3_uri": "testS3Uri",
    },
)
class ComprehendEntityRecognizerInputDataConfigDocuments:
    def __init__(
        self,
        *,
        s3_uri: builtins.str,
        input_format: typing.Optional[builtins.str] = None,
        test_s3_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param s3_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#s3_uri ComprehendEntityRecognizer#s3_uri}.
        :param input_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#input_format ComprehendEntityRecognizer#input_format}.
        :param test_s3_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#test_s3_uri ComprehendEntityRecognizer#test_s3_uri}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07e7e4b601f6e131ba75512de30947a0203ea4995eaec81a7b48f972e08a54b4)
            check_type(argname="argument s3_uri", value=s3_uri, expected_type=type_hints["s3_uri"])
            check_type(argname="argument input_format", value=input_format, expected_type=type_hints["input_format"])
            check_type(argname="argument test_s3_uri", value=test_s3_uri, expected_type=type_hints["test_s3_uri"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "s3_uri": s3_uri,
        }
        if input_format is not None:
            self._values["input_format"] = input_format
        if test_s3_uri is not None:
            self._values["test_s3_uri"] = test_s3_uri

    @builtins.property
    def s3_uri(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#s3_uri ComprehendEntityRecognizer#s3_uri}.'''
        result = self._values.get("s3_uri")
        assert result is not None, "Required property 's3_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def input_format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#input_format ComprehendEntityRecognizer#input_format}.'''
        result = self._values.get("input_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def test_s3_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#test_s3_uri ComprehendEntityRecognizer#test_s3_uri}.'''
        result = self._values.get("test_s3_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComprehendEntityRecognizerInputDataConfigDocuments(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComprehendEntityRecognizerInputDataConfigDocumentsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.comprehendEntityRecognizer.ComprehendEntityRecognizerInputDataConfigDocumentsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__803fd0bc891b718670f2d9afde915e1f1eb39d536adafdc1f729439da9a2da86)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetInputFormat")
    def reset_input_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInputFormat", []))

    @jsii.member(jsii_name="resetTestS3Uri")
    def reset_test_s3_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTestS3Uri", []))

    @builtins.property
    @jsii.member(jsii_name="inputFormatInput")
    def input_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "inputFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="s3UriInput")
    def s3_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3UriInput"))

    @builtins.property
    @jsii.member(jsii_name="testS3UriInput")
    def test_s3_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "testS3UriInput"))

    @builtins.property
    @jsii.member(jsii_name="inputFormat")
    def input_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "inputFormat"))

    @input_format.setter
    def input_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83f296cdae095412c2f9db59e0f1dc8df1dd6c1b1b66f2389f301684b67a24d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inputFormat", value)

    @builtins.property
    @jsii.member(jsii_name="s3Uri")
    def s3_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3Uri"))

    @s3_uri.setter
    def s3_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89ddce4afe6ed213dcf5256939490e58d6ea2f686974f4674c952f1dd6e73b9b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3Uri", value)

    @builtins.property
    @jsii.member(jsii_name="testS3Uri")
    def test_s3_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "testS3Uri"))

    @test_s3_uri.setter
    def test_s3_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7419371c660c428bd2092bac74e62e39c02ad35dfc615407a6322fe5839ab29c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "testS3Uri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComprehendEntityRecognizerInputDataConfigDocuments]:
        return typing.cast(typing.Optional[ComprehendEntityRecognizerInputDataConfigDocuments], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComprehendEntityRecognizerInputDataConfigDocuments],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52ea011386b8605e558fa416e16447ab963b8b0a672689948d2920994daf6208)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.comprehendEntityRecognizer.ComprehendEntityRecognizerInputDataConfigEntityList",
    jsii_struct_bases=[],
    name_mapping={"s3_uri": "s3Uri"},
)
class ComprehendEntityRecognizerInputDataConfigEntityList:
    def __init__(self, *, s3_uri: builtins.str) -> None:
        '''
        :param s3_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#s3_uri ComprehendEntityRecognizer#s3_uri}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57fddd89ccf99b881e2365a8c6ba4eb71a88d3d49eaa93d029281c438e18ad0b)
            check_type(argname="argument s3_uri", value=s3_uri, expected_type=type_hints["s3_uri"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "s3_uri": s3_uri,
        }

    @builtins.property
    def s3_uri(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#s3_uri ComprehendEntityRecognizer#s3_uri}.'''
        result = self._values.get("s3_uri")
        assert result is not None, "Required property 's3_uri' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComprehendEntityRecognizerInputDataConfigEntityList(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComprehendEntityRecognizerInputDataConfigEntityListOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.comprehendEntityRecognizer.ComprehendEntityRecognizerInputDataConfigEntityListOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e6aca489603de9eb44a40a45f26a06d8f68fc5603e5890763e1f0a13797838b5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="s3UriInput")
    def s3_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3UriInput"))

    @builtins.property
    @jsii.member(jsii_name="s3Uri")
    def s3_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3Uri"))

    @s3_uri.setter
    def s3_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2c73ab8ee4a57cc9556dec8100411a2210101a64d18707f836dc0a94482dcd4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3Uri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComprehendEntityRecognizerInputDataConfigEntityList]:
        return typing.cast(typing.Optional[ComprehendEntityRecognizerInputDataConfigEntityList], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComprehendEntityRecognizerInputDataConfigEntityList],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c93de4494a879ec673bd6cb28cb15b2c13dda4706727586654ee250495cc1c7e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.comprehendEntityRecognizer.ComprehendEntityRecognizerInputDataConfigEntityTypes",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class ComprehendEntityRecognizerInputDataConfigEntityTypes:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#type ComprehendEntityRecognizer#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc17e26f8aa6ebc9aae5c074458f747b56c5f7b6b936a34b5df5c1dd28863388)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#type ComprehendEntityRecognizer#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComprehendEntityRecognizerInputDataConfigEntityTypes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComprehendEntityRecognizerInputDataConfigEntityTypesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.comprehendEntityRecognizer.ComprehendEntityRecognizerInputDataConfigEntityTypesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f14f5e390329e9f414805d357ff7a43f1645bc2acfe47ff01c08342641a838ee)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ComprehendEntityRecognizerInputDataConfigEntityTypesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1c07de606b1bdbba14b85d8935ba57ed41fa324de411140c859fd64a85c5f1d)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ComprehendEntityRecognizerInputDataConfigEntityTypesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4f71428dd7fe5432f7da7a83205e3cebe9f27d1027101c25ec89d6d8483cd28)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7201771c0f7ffb07644b0c7d49c732de57c855357cbe78a6c6f9f0c94d7a00ce)
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
            type_hints = typing.get_type_hints(_typecheckingstub__084c0cf18e58f8b87945f9cf68d1e39d67b15be92a8f26d4e083b3fc0f3ebe78)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ComprehendEntityRecognizerInputDataConfigEntityTypes]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ComprehendEntityRecognizerInputDataConfigEntityTypes]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ComprehendEntityRecognizerInputDataConfigEntityTypes]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2ea56be426996513323ce7aabdcfc059a4c07cfd13737fdfeba6d326eb25daa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ComprehendEntityRecognizerInputDataConfigEntityTypesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.comprehendEntityRecognizer.ComprehendEntityRecognizerInputDataConfigEntityTypesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__53cc13dfe6f1401f27a4d94ee4259095182a761b1d1fb0b301396ce2215c57a7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3bfac4640ce06907bf53ea98f4dc3f2ffd8e0023f387497517ac7f60e8a7f76)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ComprehendEntityRecognizerInputDataConfigEntityTypes, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ComprehendEntityRecognizerInputDataConfigEntityTypes, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ComprehendEntityRecognizerInputDataConfigEntityTypes, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2c9f96af5144b327bab35926d7532aa0f3c5bd92e485d4be114698df30eedf6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ComprehendEntityRecognizerInputDataConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.comprehendEntityRecognizer.ComprehendEntityRecognizerInputDataConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e4bd65ec941fb8725abd5fb810bffeaac24e918a3b217a2a60dac292637ae6aa)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAnnotations")
    def put_annotations(
        self,
        *,
        s3_uri: builtins.str,
        test_s3_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param s3_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#s3_uri ComprehendEntityRecognizer#s3_uri}.
        :param test_s3_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#test_s3_uri ComprehendEntityRecognizer#test_s3_uri}.
        '''
        value = ComprehendEntityRecognizerInputDataConfigAnnotations(
            s3_uri=s3_uri, test_s3_uri=test_s3_uri
        )

        return typing.cast(None, jsii.invoke(self, "putAnnotations", [value]))

    @jsii.member(jsii_name="putAugmentedManifests")
    def put_augmented_manifests(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ComprehendEntityRecognizerInputDataConfigAugmentedManifests, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52746128517cefff4ba399e5084bad2d114643553381f0fef23af8e63fb23b1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAugmentedManifests", [value]))

    @jsii.member(jsii_name="putDocuments")
    def put_documents(
        self,
        *,
        s3_uri: builtins.str,
        input_format: typing.Optional[builtins.str] = None,
        test_s3_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param s3_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#s3_uri ComprehendEntityRecognizer#s3_uri}.
        :param input_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#input_format ComprehendEntityRecognizer#input_format}.
        :param test_s3_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#test_s3_uri ComprehendEntityRecognizer#test_s3_uri}.
        '''
        value = ComprehendEntityRecognizerInputDataConfigDocuments(
            s3_uri=s3_uri, input_format=input_format, test_s3_uri=test_s3_uri
        )

        return typing.cast(None, jsii.invoke(self, "putDocuments", [value]))

    @jsii.member(jsii_name="putEntityList")
    def put_entity_list(self, *, s3_uri: builtins.str) -> None:
        '''
        :param s3_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#s3_uri ComprehendEntityRecognizer#s3_uri}.
        '''
        value = ComprehendEntityRecognizerInputDataConfigEntityList(s3_uri=s3_uri)

        return typing.cast(None, jsii.invoke(self, "putEntityList", [value]))

    @jsii.member(jsii_name="putEntityTypes")
    def put_entity_types(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ComprehendEntityRecognizerInputDataConfigEntityTypes, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be2121305b657130b900a13029a0a4c8e4bda1a6a29bef14dbe8b0260afd338b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEntityTypes", [value]))

    @jsii.member(jsii_name="resetAnnotations")
    def reset_annotations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnnotations", []))

    @jsii.member(jsii_name="resetAugmentedManifests")
    def reset_augmented_manifests(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAugmentedManifests", []))

    @jsii.member(jsii_name="resetDataFormat")
    def reset_data_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataFormat", []))

    @jsii.member(jsii_name="resetDocuments")
    def reset_documents(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDocuments", []))

    @jsii.member(jsii_name="resetEntityList")
    def reset_entity_list(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEntityList", []))

    @builtins.property
    @jsii.member(jsii_name="annotations")
    def annotations(
        self,
    ) -> ComprehendEntityRecognizerInputDataConfigAnnotationsOutputReference:
        return typing.cast(ComprehendEntityRecognizerInputDataConfigAnnotationsOutputReference, jsii.get(self, "annotations"))

    @builtins.property
    @jsii.member(jsii_name="augmentedManifests")
    def augmented_manifests(
        self,
    ) -> ComprehendEntityRecognizerInputDataConfigAugmentedManifestsList:
        return typing.cast(ComprehendEntityRecognizerInputDataConfigAugmentedManifestsList, jsii.get(self, "augmentedManifests"))

    @builtins.property
    @jsii.member(jsii_name="documents")
    def documents(
        self,
    ) -> ComprehendEntityRecognizerInputDataConfigDocumentsOutputReference:
        return typing.cast(ComprehendEntityRecognizerInputDataConfigDocumentsOutputReference, jsii.get(self, "documents"))

    @builtins.property
    @jsii.member(jsii_name="entityList")
    def entity_list(
        self,
    ) -> ComprehendEntityRecognizerInputDataConfigEntityListOutputReference:
        return typing.cast(ComprehendEntityRecognizerInputDataConfigEntityListOutputReference, jsii.get(self, "entityList"))

    @builtins.property
    @jsii.member(jsii_name="entityTypes")
    def entity_types(self) -> ComprehendEntityRecognizerInputDataConfigEntityTypesList:
        return typing.cast(ComprehendEntityRecognizerInputDataConfigEntityTypesList, jsii.get(self, "entityTypes"))

    @builtins.property
    @jsii.member(jsii_name="annotationsInput")
    def annotations_input(
        self,
    ) -> typing.Optional[ComprehendEntityRecognizerInputDataConfigAnnotations]:
        return typing.cast(typing.Optional[ComprehendEntityRecognizerInputDataConfigAnnotations], jsii.get(self, "annotationsInput"))

    @builtins.property
    @jsii.member(jsii_name="augmentedManifestsInput")
    def augmented_manifests_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ComprehendEntityRecognizerInputDataConfigAugmentedManifests]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ComprehendEntityRecognizerInputDataConfigAugmentedManifests]]], jsii.get(self, "augmentedManifestsInput"))

    @builtins.property
    @jsii.member(jsii_name="dataFormatInput")
    def data_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="documentsInput")
    def documents_input(
        self,
    ) -> typing.Optional[ComprehendEntityRecognizerInputDataConfigDocuments]:
        return typing.cast(typing.Optional[ComprehendEntityRecognizerInputDataConfigDocuments], jsii.get(self, "documentsInput"))

    @builtins.property
    @jsii.member(jsii_name="entityListInput")
    def entity_list_input(
        self,
    ) -> typing.Optional[ComprehendEntityRecognizerInputDataConfigEntityList]:
        return typing.cast(typing.Optional[ComprehendEntityRecognizerInputDataConfigEntityList], jsii.get(self, "entityListInput"))

    @builtins.property
    @jsii.member(jsii_name="entityTypesInput")
    def entity_types_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ComprehendEntityRecognizerInputDataConfigEntityTypes]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ComprehendEntityRecognizerInputDataConfigEntityTypes]]], jsii.get(self, "entityTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="dataFormat")
    def data_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataFormat"))

    @data_format.setter
    def data_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdf6e919b7f65b40eb954bf793676d63d2c2a588d8599a0b34d653ad4fe2bdb6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataFormat", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComprehendEntityRecognizerInputDataConfig]:
        return typing.cast(typing.Optional[ComprehendEntityRecognizerInputDataConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComprehendEntityRecognizerInputDataConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a100fd41ae4b9f507379546ba5b400656bf20069a4239a53527132144e70746a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.comprehendEntityRecognizer.ComprehendEntityRecognizerTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class ComprehendEntityRecognizerTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#create ComprehendEntityRecognizer#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#delete ComprehendEntityRecognizer#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#update ComprehendEntityRecognizer#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2d208e034a230f74694beb3fb6c8a93b38cba7a2ecd4ab2417400f42f48e998)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#create ComprehendEntityRecognizer#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#delete ComprehendEntityRecognizer#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#update ComprehendEntityRecognizer#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComprehendEntityRecognizerTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComprehendEntityRecognizerTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.comprehendEntityRecognizer.ComprehendEntityRecognizerTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__709c5979f1481cf32a168a798d7d4f988e1270abe35ba15e56eb8408a37ae035)
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
            type_hints = typing.get_type_hints(_typecheckingstub__20ebe74cc8dafaaeddec08206c79405cfbc6a26368ef8c1d36bd0af000a34e21)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cffef8e6a4fc1749562bb6032976c40526cae0fd9d455a2e986db409d86682bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de44cc050ba104dff125822f80c4f34088ec3b3e600651378498b9f3d098b912)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ComprehendEntityRecognizerTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ComprehendEntityRecognizerTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ComprehendEntityRecognizerTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef322d12cde1a5d4cbe0c6f23bb7bf9817193729b369e5389a63f55549fc9640)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.comprehendEntityRecognizer.ComprehendEntityRecognizerVpcConfig",
    jsii_struct_bases=[],
    name_mapping={"security_group_ids": "securityGroupIds", "subnets": "subnets"},
)
class ComprehendEntityRecognizerVpcConfig:
    def __init__(
        self,
        *,
        security_group_ids: typing.Sequence[builtins.str],
        subnets: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#security_group_ids ComprehendEntityRecognizer#security_group_ids}.
        :param subnets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#subnets ComprehendEntityRecognizer#subnets}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__857317aa713e7b960e54506d4d89339f914d683a2ceb91e821165907cda1a5a6)
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument subnets", value=subnets, expected_type=type_hints["subnets"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "security_group_ids": security_group_ids,
            "subnets": subnets,
        }

    @builtins.property
    def security_group_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#security_group_ids ComprehendEntityRecognizer#security_group_ids}.'''
        result = self._values.get("security_group_ids")
        assert result is not None, "Required property 'security_group_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def subnets(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_entity_recognizer#subnets ComprehendEntityRecognizer#subnets}.'''
        result = self._values.get("subnets")
        assert result is not None, "Required property 'subnets' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComprehendEntityRecognizerVpcConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComprehendEntityRecognizerVpcConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.comprehendEntityRecognizer.ComprehendEntityRecognizerVpcConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2a134954ad594de4326d6cd237e1df9f03ea47bf9a8377f4b9ebd0a80fb06c91)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="securityGroupIdsInput")
    def security_group_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetsInput")
    def subnets_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetsInput"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16bb4c54a38dfe975c6d7a5924e346a76b563b1dc19ac53b16d42515ade04912)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="subnets")
    def subnets(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnets"))

    @subnets.setter
    def subnets(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15bc5610dbb5ca80c72bb24dc18b26a3b3418be3ac1f92dcfa5f465f2ae4e90b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnets", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ComprehendEntityRecognizerVpcConfig]:
        return typing.cast(typing.Optional[ComprehendEntityRecognizerVpcConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComprehendEntityRecognizerVpcConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4643abd80b90606b809dc0199506475cf8d6ef30c7ff4d05bf1e252b3ebfc832)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ComprehendEntityRecognizer",
    "ComprehendEntityRecognizerConfig",
    "ComprehendEntityRecognizerInputDataConfig",
    "ComprehendEntityRecognizerInputDataConfigAnnotations",
    "ComprehendEntityRecognizerInputDataConfigAnnotationsOutputReference",
    "ComprehendEntityRecognizerInputDataConfigAugmentedManifests",
    "ComprehendEntityRecognizerInputDataConfigAugmentedManifestsList",
    "ComprehendEntityRecognizerInputDataConfigAugmentedManifestsOutputReference",
    "ComprehendEntityRecognizerInputDataConfigDocuments",
    "ComprehendEntityRecognizerInputDataConfigDocumentsOutputReference",
    "ComprehendEntityRecognizerInputDataConfigEntityList",
    "ComprehendEntityRecognizerInputDataConfigEntityListOutputReference",
    "ComprehendEntityRecognizerInputDataConfigEntityTypes",
    "ComprehendEntityRecognizerInputDataConfigEntityTypesList",
    "ComprehendEntityRecognizerInputDataConfigEntityTypesOutputReference",
    "ComprehendEntityRecognizerInputDataConfigOutputReference",
    "ComprehendEntityRecognizerTimeouts",
    "ComprehendEntityRecognizerTimeoutsOutputReference",
    "ComprehendEntityRecognizerVpcConfig",
    "ComprehendEntityRecognizerVpcConfigOutputReference",
]

publication.publish()

def _typecheckingstub__5e824471da268ba99e1656b5386bdc1b91a2a4a522df1f525d9be53d9745f59a(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    data_access_role_arn: builtins.str,
    input_data_config: typing.Union[ComprehendEntityRecognizerInputDataConfig, typing.Dict[builtins.str, typing.Any]],
    language_code: builtins.str,
    name: builtins.str,
    id: typing.Optional[builtins.str] = None,
    model_kms_key_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[ComprehendEntityRecognizerTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    version_name: typing.Optional[builtins.str] = None,
    version_name_prefix: typing.Optional[builtins.str] = None,
    volume_kms_key_id: typing.Optional[builtins.str] = None,
    vpc_config: typing.Optional[typing.Union[ComprehendEntityRecognizerVpcConfig, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__764b22c695dcce3f1f8e0ae59ecdc00a0fe36b5885e4b27f18d6afd099056fd7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35583f3b52d917dc40e4571bc985aad26efeebfa4c7db12d405dc5c2623fae48(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05896076a428d6553ebc01185fd8f5fbad39b5223840c3023bd2b2891dd29f13(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7061fd1c9509465cb368cd9851d3544c03907b637576123756fa753f8095b57(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a3d0492dcc0c102043f5fa8a19269976be1d3fac106d823d30ef07b24e8ba68(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58827e7a9c6ab511a2601833d6003a40c5ad8ad5c245568857afd7b66c1986c3(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1d07face4a26985ef0538749b8c5bafa62ead8fcac59530871c2e1aff425710(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4a4fd6040f1ccc1eae5554949d114d85fd4fdd52ece9c9d98102ed8a0692788(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52cb1a3ad8bb78a7ef7315d4c8290f807b82383f8ccaa7f1c14017d6c4a17d23(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3454d6cd8e82aa1a11eca02885fd034c4cb9fe851f8dc7d61d228a6bce2c0872(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8814f540aa4fbd6032441f45f54386741983ad10afc403cf0e7d4061617bdac(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    data_access_role_arn: builtins.str,
    input_data_config: typing.Union[ComprehendEntityRecognizerInputDataConfig, typing.Dict[builtins.str, typing.Any]],
    language_code: builtins.str,
    name: builtins.str,
    id: typing.Optional[builtins.str] = None,
    model_kms_key_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[ComprehendEntityRecognizerTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    version_name: typing.Optional[builtins.str] = None,
    version_name_prefix: typing.Optional[builtins.str] = None,
    volume_kms_key_id: typing.Optional[builtins.str] = None,
    vpc_config: typing.Optional[typing.Union[ComprehendEntityRecognizerVpcConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba9466e6c5330cd64cd540121c7b3bfb9e573ffe07472db22aa8482ac2129058(
    *,
    entity_types: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ComprehendEntityRecognizerInputDataConfigEntityTypes, typing.Dict[builtins.str, typing.Any]]]],
    annotations: typing.Optional[typing.Union[ComprehendEntityRecognizerInputDataConfigAnnotations, typing.Dict[builtins.str, typing.Any]]] = None,
    augmented_manifests: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ComprehendEntityRecognizerInputDataConfigAugmentedManifests, typing.Dict[builtins.str, typing.Any]]]]] = None,
    data_format: typing.Optional[builtins.str] = None,
    documents: typing.Optional[typing.Union[ComprehendEntityRecognizerInputDataConfigDocuments, typing.Dict[builtins.str, typing.Any]]] = None,
    entity_list: typing.Optional[typing.Union[ComprehendEntityRecognizerInputDataConfigEntityList, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae734a8edd5e24d2e3e770beac3a86c39db0e03e27276dc6db259acefbc6c658(
    *,
    s3_uri: builtins.str,
    test_s3_uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__799441ae42218800901141f446cea7c32e62353184cdeac76a2d1be010fc8407(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3852831f50635d63c66cd1ba88aaca15b9d9de6d948cc046ee6dfee3b851854(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8572e29cf5e4a903145c1a325821e991aa994f777eb67b59e3efb827d52b500d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76febfe7d510233e2b7e74e328e9a8040f63ef0ac0b67cf8b14548ce8714d9da(
    value: typing.Optional[ComprehendEntityRecognizerInputDataConfigAnnotations],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ca422026ad3b28c8a8851de11829f90194482562148e7461306f80dc8aba575(
    *,
    attribute_names: typing.Sequence[builtins.str],
    s3_uri: builtins.str,
    annotation_data_s3_uri: typing.Optional[builtins.str] = None,
    document_type: typing.Optional[builtins.str] = None,
    source_documents_s3_uri: typing.Optional[builtins.str] = None,
    split: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d83ae0452196bbb8a5f41d02576f364b3849c124a44bdfccd5c5f15b45e8d37(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9d0de31c25effe3adbe178ec12135c1a90901cf3fe9ac3739017ff3f123ac01(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb8fc39d910063d94aea7682ea01b9f116a229c476c3231e10b8dd0cc28ac417(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8dc76c0bd9492c124fe9f9e130ba64b680f3e200c64747515572e1a0ad76c0f(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e04c2605555ece9debf34af5c8c2ba793889808d868bfdcf1854b6c94c793355(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__875cbc0f1b45a82fdcf32477152ac4e2d585ca8a877b52cc95f55250d0ea6415(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ComprehendEntityRecognizerInputDataConfigAugmentedManifests]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d012596a9f73963ee27989c2cd8cc59697d690b83a53027870f4617bbb50cd99(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3602ef5e70b3a624d7559d37dc0d6f790b90e145c028760ab676d47e8313cbba(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec1528f81b894b6a3f4783699de4a9b18de5f0dcedb672cad0405ab51014bae1(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__682ebdbae1569fc273d45174e673990bfe67b7d66b977f751bfe597b0bfdd4f4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10de2976fd89692ab81ccc04cce0a32794221199f4ff34054533f73a7028dab7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b29a866f122c684a4bfd208660e9a62d554ebdde9cca9371af43c5635484a44(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b4fabbcdf966ce6f95cead696254228036b36e4f5d11e2a6162296b37d16488(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c017b2bbe5044589d623e45682e0599972cd96802393fcefc1a1f54618266bb(
    value: typing.Optional[typing.Union[ComprehendEntityRecognizerInputDataConfigAugmentedManifests, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07e7e4b601f6e131ba75512de30947a0203ea4995eaec81a7b48f972e08a54b4(
    *,
    s3_uri: builtins.str,
    input_format: typing.Optional[builtins.str] = None,
    test_s3_uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__803fd0bc891b718670f2d9afde915e1f1eb39d536adafdc1f729439da9a2da86(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83f296cdae095412c2f9db59e0f1dc8df1dd6c1b1b66f2389f301684b67a24d7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89ddce4afe6ed213dcf5256939490e58d6ea2f686974f4674c952f1dd6e73b9b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7419371c660c428bd2092bac74e62e39c02ad35dfc615407a6322fe5839ab29c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52ea011386b8605e558fa416e16447ab963b8b0a672689948d2920994daf6208(
    value: typing.Optional[ComprehendEntityRecognizerInputDataConfigDocuments],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57fddd89ccf99b881e2365a8c6ba4eb71a88d3d49eaa93d029281c438e18ad0b(
    *,
    s3_uri: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6aca489603de9eb44a40a45f26a06d8f68fc5603e5890763e1f0a13797838b5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2c73ab8ee4a57cc9556dec8100411a2210101a64d18707f836dc0a94482dcd4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c93de4494a879ec673bd6cb28cb15b2c13dda4706727586654ee250495cc1c7e(
    value: typing.Optional[ComprehendEntityRecognizerInputDataConfigEntityList],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc17e26f8aa6ebc9aae5c074458f747b56c5f7b6b936a34b5df5c1dd28863388(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f14f5e390329e9f414805d357ff7a43f1645bc2acfe47ff01c08342641a838ee(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1c07de606b1bdbba14b85d8935ba57ed41fa324de411140c859fd64a85c5f1d(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4f71428dd7fe5432f7da7a83205e3cebe9f27d1027101c25ec89d6d8483cd28(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7201771c0f7ffb07644b0c7d49c732de57c855357cbe78a6c6f9f0c94d7a00ce(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__084c0cf18e58f8b87945f9cf68d1e39d67b15be92a8f26d4e083b3fc0f3ebe78(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2ea56be426996513323ce7aabdcfc059a4c07cfd13737fdfeba6d326eb25daa(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ComprehendEntityRecognizerInputDataConfigEntityTypes]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53cc13dfe6f1401f27a4d94ee4259095182a761b1d1fb0b301396ce2215c57a7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3bfac4640ce06907bf53ea98f4dc3f2ffd8e0023f387497517ac7f60e8a7f76(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2c9f96af5144b327bab35926d7532aa0f3c5bd92e485d4be114698df30eedf6(
    value: typing.Optional[typing.Union[ComprehendEntityRecognizerInputDataConfigEntityTypes, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4bd65ec941fb8725abd5fb810bffeaac24e918a3b217a2a60dac292637ae6aa(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52746128517cefff4ba399e5084bad2d114643553381f0fef23af8e63fb23b1a(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ComprehendEntityRecognizerInputDataConfigAugmentedManifests, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be2121305b657130b900a13029a0a4c8e4bda1a6a29bef14dbe8b0260afd338b(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ComprehendEntityRecognizerInputDataConfigEntityTypes, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdf6e919b7f65b40eb954bf793676d63d2c2a588d8599a0b34d653ad4fe2bdb6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a100fd41ae4b9f507379546ba5b400656bf20069a4239a53527132144e70746a(
    value: typing.Optional[ComprehendEntityRecognizerInputDataConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2d208e034a230f74694beb3fb6c8a93b38cba7a2ecd4ab2417400f42f48e998(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__709c5979f1481cf32a168a798d7d4f988e1270abe35ba15e56eb8408a37ae035(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20ebe74cc8dafaaeddec08206c79405cfbc6a26368ef8c1d36bd0af000a34e21(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cffef8e6a4fc1749562bb6032976c40526cae0fd9d455a2e986db409d86682bc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de44cc050ba104dff125822f80c4f34088ec3b3e600651378498b9f3d098b912(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef322d12cde1a5d4cbe0c6f23bb7bf9817193729b369e5389a63f55549fc9640(
    value: typing.Optional[typing.Union[ComprehendEntityRecognizerTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__857317aa713e7b960e54506d4d89339f914d683a2ceb91e821165907cda1a5a6(
    *,
    security_group_ids: typing.Sequence[builtins.str],
    subnets: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a134954ad594de4326d6cd237e1df9f03ea47bf9a8377f4b9ebd0a80fb06c91(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16bb4c54a38dfe975c6d7a5924e346a76b563b1dc19ac53b16d42515ade04912(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15bc5610dbb5ca80c72bb24dc18b26a3b3418be3ac1f92dcfa5f465f2ae4e90b(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4643abd80b90606b809dc0199506475cf8d6ef30c7ff4d05bf1e252b3ebfc832(
    value: typing.Optional[ComprehendEntityRecognizerVpcConfig],
) -> None:
    """Type checking stubs"""
    pass
