'''
# `aws_acmpca_certificate`

Refer to the Terraform Registory for docs: [`aws_acmpca_certificate`](https://www.terraform.io/docs/providers/aws/r/acmpca_certificate).
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


class AcmpcaCertificate(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.acmpcaCertificate.AcmpcaCertificate",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate aws_acmpca_certificate}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        certificate_authority_arn: builtins.str,
        certificate_signing_request: builtins.str,
        signing_algorithm: builtins.str,
        validity: typing.Union["AcmpcaCertificateValidity", typing.Dict[builtins.str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        template_arn: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate aws_acmpca_certificate} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param certificate_authority_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate#certificate_authority_arn AcmpcaCertificate#certificate_authority_arn}.
        :param certificate_signing_request: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate#certificate_signing_request AcmpcaCertificate#certificate_signing_request}.
        :param signing_algorithm: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate#signing_algorithm AcmpcaCertificate#signing_algorithm}.
        :param validity: validity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate#validity AcmpcaCertificate#validity}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate#id AcmpcaCertificate#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param template_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate#template_arn AcmpcaCertificate#template_arn}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c612d9a3a798cb3b9f36c24d8f0d4346ba3cae103ebfee8e49e46b0f463dda3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AcmpcaCertificateConfig(
            certificate_authority_arn=certificate_authority_arn,
            certificate_signing_request=certificate_signing_request,
            signing_algorithm=signing_algorithm,
            validity=validity,
            id=id,
            template_arn=template_arn,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putValidity")
    def put_validity(self, *, type: builtins.str, value: builtins.str) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate#type AcmpcaCertificate#type}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate#value AcmpcaCertificate#value}.
        '''
        value_ = AcmpcaCertificateValidity(type=type, value=value)

        return typing.cast(None, jsii.invoke(self, "putValidity", [value_]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTemplateArn")
    def reset_template_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTemplateArn", []))

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
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificate"))

    @builtins.property
    @jsii.member(jsii_name="certificateChain")
    def certificate_chain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateChain"))

    @builtins.property
    @jsii.member(jsii_name="validity")
    def validity(self) -> "AcmpcaCertificateValidityOutputReference":
        return typing.cast("AcmpcaCertificateValidityOutputReference", jsii.get(self, "validity"))

    @builtins.property
    @jsii.member(jsii_name="certificateAuthorityArnInput")
    def certificate_authority_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateAuthorityArnInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateSigningRequestInput")
    def certificate_signing_request_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateSigningRequestInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="signingAlgorithmInput")
    def signing_algorithm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "signingAlgorithmInput"))

    @builtins.property
    @jsii.member(jsii_name="templateArnInput")
    def template_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateArnInput"))

    @builtins.property
    @jsii.member(jsii_name="validityInput")
    def validity_input(self) -> typing.Optional["AcmpcaCertificateValidity"]:
        return typing.cast(typing.Optional["AcmpcaCertificateValidity"], jsii.get(self, "validityInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateAuthorityArn")
    def certificate_authority_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateAuthorityArn"))

    @certificate_authority_arn.setter
    def certificate_authority_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__470eaabe52219fcd658551112eaa1fb45f432f03fbf28f20fe59f907c35da495)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateAuthorityArn", value)

    @builtins.property
    @jsii.member(jsii_name="certificateSigningRequest")
    def certificate_signing_request(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateSigningRequest"))

    @certificate_signing_request.setter
    def certificate_signing_request(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5dbc7b7811cb9fb7107bd3cb5aa1a39ca35a9a797458d572492bc70834238af3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateSigningRequest", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f29019604694e1b8bbfe27054ab0b624888b6b3dd4452e477aabddfcddab999)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="signingAlgorithm")
    def signing_algorithm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "signingAlgorithm"))

    @signing_algorithm.setter
    def signing_algorithm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b032bd3677f64a4c718f1391e5e4a8abd4500b15a30431fb14e8d747f867855c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signingAlgorithm", value)

    @builtins.property
    @jsii.member(jsii_name="templateArn")
    def template_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "templateArn"))

    @template_arn.setter
    def template_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9cf2a48ff9765904744743c8b6896febfc922f7e2f947442553b3bab41825591)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateArn", value)


@jsii.data_type(
    jsii_type="aws.acmpcaCertificate.AcmpcaCertificateConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "certificate_authority_arn": "certificateAuthorityArn",
        "certificate_signing_request": "certificateSigningRequest",
        "signing_algorithm": "signingAlgorithm",
        "validity": "validity",
        "id": "id",
        "template_arn": "templateArn",
    },
)
class AcmpcaCertificateConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        certificate_authority_arn: builtins.str,
        certificate_signing_request: builtins.str,
        signing_algorithm: builtins.str,
        validity: typing.Union["AcmpcaCertificateValidity", typing.Dict[builtins.str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        template_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param certificate_authority_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate#certificate_authority_arn AcmpcaCertificate#certificate_authority_arn}.
        :param certificate_signing_request: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate#certificate_signing_request AcmpcaCertificate#certificate_signing_request}.
        :param signing_algorithm: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate#signing_algorithm AcmpcaCertificate#signing_algorithm}.
        :param validity: validity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate#validity AcmpcaCertificate#validity}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate#id AcmpcaCertificate#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param template_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate#template_arn AcmpcaCertificate#template_arn}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(validity, dict):
            validity = AcmpcaCertificateValidity(**validity)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6deee7827f57552ca85ea165d8de59f9d0bcfe408b1733cf8a1ee32393e1ad1e)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument certificate_authority_arn", value=certificate_authority_arn, expected_type=type_hints["certificate_authority_arn"])
            check_type(argname="argument certificate_signing_request", value=certificate_signing_request, expected_type=type_hints["certificate_signing_request"])
            check_type(argname="argument signing_algorithm", value=signing_algorithm, expected_type=type_hints["signing_algorithm"])
            check_type(argname="argument validity", value=validity, expected_type=type_hints["validity"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument template_arn", value=template_arn, expected_type=type_hints["template_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "certificate_authority_arn": certificate_authority_arn,
            "certificate_signing_request": certificate_signing_request,
            "signing_algorithm": signing_algorithm,
            "validity": validity,
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
        if template_arn is not None:
            self._values["template_arn"] = template_arn

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
    def certificate_authority_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate#certificate_authority_arn AcmpcaCertificate#certificate_authority_arn}.'''
        result = self._values.get("certificate_authority_arn")
        assert result is not None, "Required property 'certificate_authority_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate_signing_request(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate#certificate_signing_request AcmpcaCertificate#certificate_signing_request}.'''
        result = self._values.get("certificate_signing_request")
        assert result is not None, "Required property 'certificate_signing_request' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def signing_algorithm(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate#signing_algorithm AcmpcaCertificate#signing_algorithm}.'''
        result = self._values.get("signing_algorithm")
        assert result is not None, "Required property 'signing_algorithm' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def validity(self) -> "AcmpcaCertificateValidity":
        '''validity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate#validity AcmpcaCertificate#validity}
        '''
        result = self._values.get("validity")
        assert result is not None, "Required property 'validity' is missing"
        return typing.cast("AcmpcaCertificateValidity", result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate#id AcmpcaCertificate#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def template_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate#template_arn AcmpcaCertificate#template_arn}.'''
        result = self._values.get("template_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AcmpcaCertificateConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.acmpcaCertificate.AcmpcaCertificateValidity",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "value": "value"},
)
class AcmpcaCertificateValidity:
    def __init__(self, *, type: builtins.str, value: builtins.str) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate#type AcmpcaCertificate#type}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate#value AcmpcaCertificate#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d900873d9bb0ee6972eb09a213a8e1e01332b880e87621313e589d089bb5715)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
            "value": value,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate#type AcmpcaCertificate#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate#value AcmpcaCertificate#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AcmpcaCertificateValidity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AcmpcaCertificateValidityOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.acmpcaCertificate.AcmpcaCertificateValidityOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ff692a3bfdd153c56d0738aaa046dd08df26abe95a5788ee2261db0a0cc74492)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be5181158393899a12a91feb773c8ce083fb9cc02429d28d0be32ac07ace821f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53ff5a98d5842fd2e2ddd7af6b5190d0abb894fcbbe7daeb3c57e8f2365627ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AcmpcaCertificateValidity]:
        return typing.cast(typing.Optional[AcmpcaCertificateValidity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[AcmpcaCertificateValidity]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c5b952d4db4b81b0c61178464488096037cdd66d1505b8416568042ca8ffccb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "AcmpcaCertificate",
    "AcmpcaCertificateConfig",
    "AcmpcaCertificateValidity",
    "AcmpcaCertificateValidityOutputReference",
]

publication.publish()

def _typecheckingstub__5c612d9a3a798cb3b9f36c24d8f0d4346ba3cae103ebfee8e49e46b0f463dda3(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    certificate_authority_arn: builtins.str,
    certificate_signing_request: builtins.str,
    signing_algorithm: builtins.str,
    validity: typing.Union[AcmpcaCertificateValidity, typing.Dict[builtins.str, typing.Any]],
    id: typing.Optional[builtins.str] = None,
    template_arn: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__470eaabe52219fcd658551112eaa1fb45f432f03fbf28f20fe59f907c35da495(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dbc7b7811cb9fb7107bd3cb5aa1a39ca35a9a797458d572492bc70834238af3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f29019604694e1b8bbfe27054ab0b624888b6b3dd4452e477aabddfcddab999(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b032bd3677f64a4c718f1391e5e4a8abd4500b15a30431fb14e8d747f867855c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cf2a48ff9765904744743c8b6896febfc922f7e2f947442553b3bab41825591(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6deee7827f57552ca85ea165d8de59f9d0bcfe408b1733cf8a1ee32393e1ad1e(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    certificate_authority_arn: builtins.str,
    certificate_signing_request: builtins.str,
    signing_algorithm: builtins.str,
    validity: typing.Union[AcmpcaCertificateValidity, typing.Dict[builtins.str, typing.Any]],
    id: typing.Optional[builtins.str] = None,
    template_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d900873d9bb0ee6972eb09a213a8e1e01332b880e87621313e589d089bb5715(
    *,
    type: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff692a3bfdd153c56d0738aaa046dd08df26abe95a5788ee2261db0a0cc74492(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be5181158393899a12a91feb773c8ce083fb9cc02429d28d0be32ac07ace821f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53ff5a98d5842fd2e2ddd7af6b5190d0abb894fcbbe7daeb3c57e8f2365627ae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c5b952d4db4b81b0c61178464488096037cdd66d1505b8416568042ca8ffccb(
    value: typing.Optional[AcmpcaCertificateValidity],
) -> None:
    """Type checking stubs"""
    pass
