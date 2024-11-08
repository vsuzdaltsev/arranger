'''
# `aws_acmpca_certificate_authority`

Refer to the Terraform Registory for docs: [`aws_acmpca_certificate_authority`](https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority).
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


class AcmpcaCertificateAuthority(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.acmpcaCertificateAuthority.AcmpcaCertificateAuthority",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority aws_acmpca_certificate_authority}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        certificate_authority_configuration: typing.Union["AcmpcaCertificateAuthorityCertificateAuthorityConfiguration", typing.Dict[builtins.str, typing.Any]],
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        permanent_deletion_time_in_days: typing.Optional[jsii.Number] = None,
        revocation_configuration: typing.Optional[typing.Union["AcmpcaCertificateAuthorityRevocationConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["AcmpcaCertificateAuthorityTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        type: typing.Optional[builtins.str] = None,
        usage_mode: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority aws_acmpca_certificate_authority} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param certificate_authority_configuration: certificate_authority_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#certificate_authority_configuration AcmpcaCertificateAuthority#certificate_authority_configuration}
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#enabled AcmpcaCertificateAuthority#enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#id AcmpcaCertificateAuthority#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param permanent_deletion_time_in_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#permanent_deletion_time_in_days AcmpcaCertificateAuthority#permanent_deletion_time_in_days}.
        :param revocation_configuration: revocation_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#revocation_configuration AcmpcaCertificateAuthority#revocation_configuration}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#tags AcmpcaCertificateAuthority#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#tags_all AcmpcaCertificateAuthority#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#timeouts AcmpcaCertificateAuthority#timeouts}
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#type AcmpcaCertificateAuthority#type}.
        :param usage_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#usage_mode AcmpcaCertificateAuthority#usage_mode}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55321c0c1c48f20ecad667914b61c2c157aa9cc699e2758a9f1ccb955e9666a4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AcmpcaCertificateAuthorityConfig(
            certificate_authority_configuration=certificate_authority_configuration,
            enabled=enabled,
            id=id,
            permanent_deletion_time_in_days=permanent_deletion_time_in_days,
            revocation_configuration=revocation_configuration,
            tags=tags,
            tags_all=tags_all,
            timeouts=timeouts,
            type=type,
            usage_mode=usage_mode,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCertificateAuthorityConfiguration")
    def put_certificate_authority_configuration(
        self,
        *,
        key_algorithm: builtins.str,
        signing_algorithm: builtins.str,
        subject: typing.Union["AcmpcaCertificateAuthorityCertificateAuthorityConfigurationSubject", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param key_algorithm: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#key_algorithm AcmpcaCertificateAuthority#key_algorithm}.
        :param signing_algorithm: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#signing_algorithm AcmpcaCertificateAuthority#signing_algorithm}.
        :param subject: subject block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#subject AcmpcaCertificateAuthority#subject}
        '''
        value = AcmpcaCertificateAuthorityCertificateAuthorityConfiguration(
            key_algorithm=key_algorithm,
            signing_algorithm=signing_algorithm,
            subject=subject,
        )

        return typing.cast(None, jsii.invoke(self, "putCertificateAuthorityConfiguration", [value]))

    @jsii.member(jsii_name="putRevocationConfiguration")
    def put_revocation_configuration(
        self,
        *,
        crl_configuration: typing.Optional[typing.Union["AcmpcaCertificateAuthorityRevocationConfigurationCrlConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        ocsp_configuration: typing.Optional[typing.Union["AcmpcaCertificateAuthorityRevocationConfigurationOcspConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param crl_configuration: crl_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#crl_configuration AcmpcaCertificateAuthority#crl_configuration}
        :param ocsp_configuration: ocsp_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#ocsp_configuration AcmpcaCertificateAuthority#ocsp_configuration}
        '''
        value = AcmpcaCertificateAuthorityRevocationConfiguration(
            crl_configuration=crl_configuration, ocsp_configuration=ocsp_configuration
        )

        return typing.cast(None, jsii.invoke(self, "putRevocationConfiguration", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(self, *, create: typing.Optional[builtins.str] = None) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#create AcmpcaCertificateAuthority#create}.
        '''
        value = AcmpcaCertificateAuthorityTimeouts(create=create)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPermanentDeletionTimeInDays")
    def reset_permanent_deletion_time_in_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPermanentDeletionTimeInDays", []))

    @jsii.member(jsii_name="resetRevocationConfiguration")
    def reset_revocation_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRevocationConfiguration", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="resetUsageMode")
    def reset_usage_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsageMode", []))

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
    @jsii.member(jsii_name="certificateAuthorityConfiguration")
    def certificate_authority_configuration(
        self,
    ) -> "AcmpcaCertificateAuthorityCertificateAuthorityConfigurationOutputReference":
        return typing.cast("AcmpcaCertificateAuthorityCertificateAuthorityConfigurationOutputReference", jsii.get(self, "certificateAuthorityConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="certificateChain")
    def certificate_chain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateChain"))

    @builtins.property
    @jsii.member(jsii_name="certificateSigningRequest")
    def certificate_signing_request(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateSigningRequest"))

    @builtins.property
    @jsii.member(jsii_name="notAfter")
    def not_after(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notAfter"))

    @builtins.property
    @jsii.member(jsii_name="notBefore")
    def not_before(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notBefore"))

    @builtins.property
    @jsii.member(jsii_name="revocationConfiguration")
    def revocation_configuration(
        self,
    ) -> "AcmpcaCertificateAuthorityRevocationConfigurationOutputReference":
        return typing.cast("AcmpcaCertificateAuthorityRevocationConfigurationOutputReference", jsii.get(self, "revocationConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="serial")
    def serial(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serial"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "AcmpcaCertificateAuthorityTimeoutsOutputReference":
        return typing.cast("AcmpcaCertificateAuthorityTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="certificateAuthorityConfigurationInput")
    def certificate_authority_configuration_input(
        self,
    ) -> typing.Optional["AcmpcaCertificateAuthorityCertificateAuthorityConfiguration"]:
        return typing.cast(typing.Optional["AcmpcaCertificateAuthorityCertificateAuthorityConfiguration"], jsii.get(self, "certificateAuthorityConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="permanentDeletionTimeInDaysInput")
    def permanent_deletion_time_in_days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "permanentDeletionTimeInDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="revocationConfigurationInput")
    def revocation_configuration_input(
        self,
    ) -> typing.Optional["AcmpcaCertificateAuthorityRevocationConfiguration"]:
        return typing.cast(typing.Optional["AcmpcaCertificateAuthorityRevocationConfiguration"], jsii.get(self, "revocationConfigurationInput"))

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
    ) -> typing.Optional[typing.Union["AcmpcaCertificateAuthorityTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["AcmpcaCertificateAuthorityTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="usageModeInput")
    def usage_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usageModeInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__3efb64d3fab8578e712436590a712f720a159aa0fe2690cc1087736bb99f2528)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d603340f31ab6df9cd235dbb7870a9d2a0d2d7fc64e7e24ad1b3d310ffee6851)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="permanentDeletionTimeInDays")
    def permanent_deletion_time_in_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "permanentDeletionTimeInDays"))

    @permanent_deletion_time_in_days.setter
    def permanent_deletion_time_in_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2c46d6908577809136d2e2d373c84645103ee98ed71b7870f7774a8a41a747c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permanentDeletionTimeInDays", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8378142fcfce929c41f17885d42ac1d904c0a2c1798f1ddb19d11669fc8a39c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f027ac1f5805868c3c21327a37180661b4c10f02f28e90ae8097505b44cc244)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40e278ceea5d7abf659684e281bfeb77ec3e1a4342524a129a93b77970546a90)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="usageMode")
    def usage_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "usageMode"))

    @usage_mode.setter
    def usage_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d87ecda6db453e90dfde28adf9a1e4c434224609c7d01b4ab8bea903d5e169a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usageMode", value)


@jsii.data_type(
    jsii_type="aws.acmpcaCertificateAuthority.AcmpcaCertificateAuthorityCertificateAuthorityConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "key_algorithm": "keyAlgorithm",
        "signing_algorithm": "signingAlgorithm",
        "subject": "subject",
    },
)
class AcmpcaCertificateAuthorityCertificateAuthorityConfiguration:
    def __init__(
        self,
        *,
        key_algorithm: builtins.str,
        signing_algorithm: builtins.str,
        subject: typing.Union["AcmpcaCertificateAuthorityCertificateAuthorityConfigurationSubject", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param key_algorithm: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#key_algorithm AcmpcaCertificateAuthority#key_algorithm}.
        :param signing_algorithm: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#signing_algorithm AcmpcaCertificateAuthority#signing_algorithm}.
        :param subject: subject block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#subject AcmpcaCertificateAuthority#subject}
        '''
        if isinstance(subject, dict):
            subject = AcmpcaCertificateAuthorityCertificateAuthorityConfigurationSubject(**subject)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a8aae2eef32164796fe038e1566b863a44e3370c71c9808c35169b93361a12c)
            check_type(argname="argument key_algorithm", value=key_algorithm, expected_type=type_hints["key_algorithm"])
            check_type(argname="argument signing_algorithm", value=signing_algorithm, expected_type=type_hints["signing_algorithm"])
            check_type(argname="argument subject", value=subject, expected_type=type_hints["subject"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key_algorithm": key_algorithm,
            "signing_algorithm": signing_algorithm,
            "subject": subject,
        }

    @builtins.property
    def key_algorithm(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#key_algorithm AcmpcaCertificateAuthority#key_algorithm}.'''
        result = self._values.get("key_algorithm")
        assert result is not None, "Required property 'key_algorithm' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def signing_algorithm(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#signing_algorithm AcmpcaCertificateAuthority#signing_algorithm}.'''
        result = self._values.get("signing_algorithm")
        assert result is not None, "Required property 'signing_algorithm' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subject(
        self,
    ) -> "AcmpcaCertificateAuthorityCertificateAuthorityConfigurationSubject":
        '''subject block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#subject AcmpcaCertificateAuthority#subject}
        '''
        result = self._values.get("subject")
        assert result is not None, "Required property 'subject' is missing"
        return typing.cast("AcmpcaCertificateAuthorityCertificateAuthorityConfigurationSubject", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AcmpcaCertificateAuthorityCertificateAuthorityConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AcmpcaCertificateAuthorityCertificateAuthorityConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.acmpcaCertificateAuthority.AcmpcaCertificateAuthorityCertificateAuthorityConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a3491cdb4b84914d26096c66221398dae15648cda72d1b833fd5c7779c468d54)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSubject")
    def put_subject(
        self,
        *,
        common_name: typing.Optional[builtins.str] = None,
        country: typing.Optional[builtins.str] = None,
        distinguished_name_qualifier: typing.Optional[builtins.str] = None,
        generation_qualifier: typing.Optional[builtins.str] = None,
        given_name: typing.Optional[builtins.str] = None,
        initials: typing.Optional[builtins.str] = None,
        locality: typing.Optional[builtins.str] = None,
        organization: typing.Optional[builtins.str] = None,
        organizational_unit: typing.Optional[builtins.str] = None,
        pseudonym: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
        surname: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param common_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#common_name AcmpcaCertificateAuthority#common_name}.
        :param country: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#country AcmpcaCertificateAuthority#country}.
        :param distinguished_name_qualifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#distinguished_name_qualifier AcmpcaCertificateAuthority#distinguished_name_qualifier}.
        :param generation_qualifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#generation_qualifier AcmpcaCertificateAuthority#generation_qualifier}.
        :param given_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#given_name AcmpcaCertificateAuthority#given_name}.
        :param initials: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#initials AcmpcaCertificateAuthority#initials}.
        :param locality: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#locality AcmpcaCertificateAuthority#locality}.
        :param organization: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#organization AcmpcaCertificateAuthority#organization}.
        :param organizational_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#organizational_unit AcmpcaCertificateAuthority#organizational_unit}.
        :param pseudonym: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#pseudonym AcmpcaCertificateAuthority#pseudonym}.
        :param state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#state AcmpcaCertificateAuthority#state}.
        :param surname: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#surname AcmpcaCertificateAuthority#surname}.
        :param title: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#title AcmpcaCertificateAuthority#title}.
        '''
        value = AcmpcaCertificateAuthorityCertificateAuthorityConfigurationSubject(
            common_name=common_name,
            country=country,
            distinguished_name_qualifier=distinguished_name_qualifier,
            generation_qualifier=generation_qualifier,
            given_name=given_name,
            initials=initials,
            locality=locality,
            organization=organization,
            organizational_unit=organizational_unit,
            pseudonym=pseudonym,
            state=state,
            surname=surname,
            title=title,
        )

        return typing.cast(None, jsii.invoke(self, "putSubject", [value]))

    @builtins.property
    @jsii.member(jsii_name="subject")
    def subject(
        self,
    ) -> "AcmpcaCertificateAuthorityCertificateAuthorityConfigurationSubjectOutputReference":
        return typing.cast("AcmpcaCertificateAuthorityCertificateAuthorityConfigurationSubjectOutputReference", jsii.get(self, "subject"))

    @builtins.property
    @jsii.member(jsii_name="keyAlgorithmInput")
    def key_algorithm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyAlgorithmInput"))

    @builtins.property
    @jsii.member(jsii_name="signingAlgorithmInput")
    def signing_algorithm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "signingAlgorithmInput"))

    @builtins.property
    @jsii.member(jsii_name="subjectInput")
    def subject_input(
        self,
    ) -> typing.Optional["AcmpcaCertificateAuthorityCertificateAuthorityConfigurationSubject"]:
        return typing.cast(typing.Optional["AcmpcaCertificateAuthorityCertificateAuthorityConfigurationSubject"], jsii.get(self, "subjectInput"))

    @builtins.property
    @jsii.member(jsii_name="keyAlgorithm")
    def key_algorithm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyAlgorithm"))

    @key_algorithm.setter
    def key_algorithm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7dd1500a2b3e395c9671fc749ecf31fac69b95ad48a2fcf4e1cca110a61b4575)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyAlgorithm", value)

    @builtins.property
    @jsii.member(jsii_name="signingAlgorithm")
    def signing_algorithm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "signingAlgorithm"))

    @signing_algorithm.setter
    def signing_algorithm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0b0c82db142aa93be843f465c3acfb8c3692f38606c90c4e9a77fdadf4e28e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signingAlgorithm", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AcmpcaCertificateAuthorityCertificateAuthorityConfiguration]:
        return typing.cast(typing.Optional[AcmpcaCertificateAuthorityCertificateAuthorityConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AcmpcaCertificateAuthorityCertificateAuthorityConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2966cf00c8a9c9e1d8dd3135264055fda1f85035b59efe497064ef5d2b7cf8f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.acmpcaCertificateAuthority.AcmpcaCertificateAuthorityCertificateAuthorityConfigurationSubject",
    jsii_struct_bases=[],
    name_mapping={
        "common_name": "commonName",
        "country": "country",
        "distinguished_name_qualifier": "distinguishedNameQualifier",
        "generation_qualifier": "generationQualifier",
        "given_name": "givenName",
        "initials": "initials",
        "locality": "locality",
        "organization": "organization",
        "organizational_unit": "organizationalUnit",
        "pseudonym": "pseudonym",
        "state": "state",
        "surname": "surname",
        "title": "title",
    },
)
class AcmpcaCertificateAuthorityCertificateAuthorityConfigurationSubject:
    def __init__(
        self,
        *,
        common_name: typing.Optional[builtins.str] = None,
        country: typing.Optional[builtins.str] = None,
        distinguished_name_qualifier: typing.Optional[builtins.str] = None,
        generation_qualifier: typing.Optional[builtins.str] = None,
        given_name: typing.Optional[builtins.str] = None,
        initials: typing.Optional[builtins.str] = None,
        locality: typing.Optional[builtins.str] = None,
        organization: typing.Optional[builtins.str] = None,
        organizational_unit: typing.Optional[builtins.str] = None,
        pseudonym: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
        surname: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param common_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#common_name AcmpcaCertificateAuthority#common_name}.
        :param country: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#country AcmpcaCertificateAuthority#country}.
        :param distinguished_name_qualifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#distinguished_name_qualifier AcmpcaCertificateAuthority#distinguished_name_qualifier}.
        :param generation_qualifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#generation_qualifier AcmpcaCertificateAuthority#generation_qualifier}.
        :param given_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#given_name AcmpcaCertificateAuthority#given_name}.
        :param initials: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#initials AcmpcaCertificateAuthority#initials}.
        :param locality: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#locality AcmpcaCertificateAuthority#locality}.
        :param organization: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#organization AcmpcaCertificateAuthority#organization}.
        :param organizational_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#organizational_unit AcmpcaCertificateAuthority#organizational_unit}.
        :param pseudonym: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#pseudonym AcmpcaCertificateAuthority#pseudonym}.
        :param state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#state AcmpcaCertificateAuthority#state}.
        :param surname: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#surname AcmpcaCertificateAuthority#surname}.
        :param title: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#title AcmpcaCertificateAuthority#title}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__284efeffd3ca8c61b39f87931feb63d402522de00cc5947d6a9bf0e9e291dd6e)
            check_type(argname="argument common_name", value=common_name, expected_type=type_hints["common_name"])
            check_type(argname="argument country", value=country, expected_type=type_hints["country"])
            check_type(argname="argument distinguished_name_qualifier", value=distinguished_name_qualifier, expected_type=type_hints["distinguished_name_qualifier"])
            check_type(argname="argument generation_qualifier", value=generation_qualifier, expected_type=type_hints["generation_qualifier"])
            check_type(argname="argument given_name", value=given_name, expected_type=type_hints["given_name"])
            check_type(argname="argument initials", value=initials, expected_type=type_hints["initials"])
            check_type(argname="argument locality", value=locality, expected_type=type_hints["locality"])
            check_type(argname="argument organization", value=organization, expected_type=type_hints["organization"])
            check_type(argname="argument organizational_unit", value=organizational_unit, expected_type=type_hints["organizational_unit"])
            check_type(argname="argument pseudonym", value=pseudonym, expected_type=type_hints["pseudonym"])
            check_type(argname="argument state", value=state, expected_type=type_hints["state"])
            check_type(argname="argument surname", value=surname, expected_type=type_hints["surname"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if common_name is not None:
            self._values["common_name"] = common_name
        if country is not None:
            self._values["country"] = country
        if distinguished_name_qualifier is not None:
            self._values["distinguished_name_qualifier"] = distinguished_name_qualifier
        if generation_qualifier is not None:
            self._values["generation_qualifier"] = generation_qualifier
        if given_name is not None:
            self._values["given_name"] = given_name
        if initials is not None:
            self._values["initials"] = initials
        if locality is not None:
            self._values["locality"] = locality
        if organization is not None:
            self._values["organization"] = organization
        if organizational_unit is not None:
            self._values["organizational_unit"] = organizational_unit
        if pseudonym is not None:
            self._values["pseudonym"] = pseudonym
        if state is not None:
            self._values["state"] = state
        if surname is not None:
            self._values["surname"] = surname
        if title is not None:
            self._values["title"] = title

    @builtins.property
    def common_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#common_name AcmpcaCertificateAuthority#common_name}.'''
        result = self._values.get("common_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def country(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#country AcmpcaCertificateAuthority#country}.'''
        result = self._values.get("country")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def distinguished_name_qualifier(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#distinguished_name_qualifier AcmpcaCertificateAuthority#distinguished_name_qualifier}.'''
        result = self._values.get("distinguished_name_qualifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def generation_qualifier(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#generation_qualifier AcmpcaCertificateAuthority#generation_qualifier}.'''
        result = self._values.get("generation_qualifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def given_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#given_name AcmpcaCertificateAuthority#given_name}.'''
        result = self._values.get("given_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def initials(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#initials AcmpcaCertificateAuthority#initials}.'''
        result = self._values.get("initials")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def locality(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#locality AcmpcaCertificateAuthority#locality}.'''
        result = self._values.get("locality")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def organization(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#organization AcmpcaCertificateAuthority#organization}.'''
        result = self._values.get("organization")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def organizational_unit(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#organizational_unit AcmpcaCertificateAuthority#organizational_unit}.'''
        result = self._values.get("organizational_unit")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pseudonym(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#pseudonym AcmpcaCertificateAuthority#pseudonym}.'''
        result = self._values.get("pseudonym")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def state(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#state AcmpcaCertificateAuthority#state}.'''
        result = self._values.get("state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def surname(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#surname AcmpcaCertificateAuthority#surname}.'''
        result = self._values.get("surname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#title AcmpcaCertificateAuthority#title}.'''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AcmpcaCertificateAuthorityCertificateAuthorityConfigurationSubject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AcmpcaCertificateAuthorityCertificateAuthorityConfigurationSubjectOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.acmpcaCertificateAuthority.AcmpcaCertificateAuthorityCertificateAuthorityConfigurationSubjectOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d7ee5e594747a2e0eca37fb4ae6730e4dc2e07d12685ff03c63a9eb7f3c72635)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCommonName")
    def reset_common_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCommonName", []))

    @jsii.member(jsii_name="resetCountry")
    def reset_country(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCountry", []))

    @jsii.member(jsii_name="resetDistinguishedNameQualifier")
    def reset_distinguished_name_qualifier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDistinguishedNameQualifier", []))

    @jsii.member(jsii_name="resetGenerationQualifier")
    def reset_generation_qualifier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGenerationQualifier", []))

    @jsii.member(jsii_name="resetGivenName")
    def reset_given_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGivenName", []))

    @jsii.member(jsii_name="resetInitials")
    def reset_initials(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitials", []))

    @jsii.member(jsii_name="resetLocality")
    def reset_locality(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocality", []))

    @jsii.member(jsii_name="resetOrganization")
    def reset_organization(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrganization", []))

    @jsii.member(jsii_name="resetOrganizationalUnit")
    def reset_organizational_unit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrganizationalUnit", []))

    @jsii.member(jsii_name="resetPseudonym")
    def reset_pseudonym(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPseudonym", []))

    @jsii.member(jsii_name="resetState")
    def reset_state(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetState", []))

    @jsii.member(jsii_name="resetSurname")
    def reset_surname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSurname", []))

    @jsii.member(jsii_name="resetTitle")
    def reset_title(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTitle", []))

    @builtins.property
    @jsii.member(jsii_name="commonNameInput")
    def common_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commonNameInput"))

    @builtins.property
    @jsii.member(jsii_name="countryInput")
    def country_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "countryInput"))

    @builtins.property
    @jsii.member(jsii_name="distinguishedNameQualifierInput")
    def distinguished_name_qualifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "distinguishedNameQualifierInput"))

    @builtins.property
    @jsii.member(jsii_name="generationQualifierInput")
    def generation_qualifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "generationQualifierInput"))

    @builtins.property
    @jsii.member(jsii_name="givenNameInput")
    def given_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "givenNameInput"))

    @builtins.property
    @jsii.member(jsii_name="initialsInput")
    def initials_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "initialsInput"))

    @builtins.property
    @jsii.member(jsii_name="localityInput")
    def locality_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "localityInput"))

    @builtins.property
    @jsii.member(jsii_name="organizationalUnitInput")
    def organizational_unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "organizationalUnitInput"))

    @builtins.property
    @jsii.member(jsii_name="organizationInput")
    def organization_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "organizationInput"))

    @builtins.property
    @jsii.member(jsii_name="pseudonymInput")
    def pseudonym_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pseudonymInput"))

    @builtins.property
    @jsii.member(jsii_name="stateInput")
    def state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stateInput"))

    @builtins.property
    @jsii.member(jsii_name="surnameInput")
    def surname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "surnameInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="commonName")
    def common_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "commonName"))

    @common_name.setter
    def common_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a47ccb9f0fcc553b2ce1381cebdbfa8e5775e3c0c703f83c0f14b3d26417ee2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "commonName", value)

    @builtins.property
    @jsii.member(jsii_name="country")
    def country(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "country"))

    @country.setter
    def country(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54e84660cee05c32795d453367cd9be73ebf095ca3c69b479aa77792ba02b279)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "country", value)

    @builtins.property
    @jsii.member(jsii_name="distinguishedNameQualifier")
    def distinguished_name_qualifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "distinguishedNameQualifier"))

    @distinguished_name_qualifier.setter
    def distinguished_name_qualifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6a562e5ceee12db93b915114f5a093728abcce153efcde8af49f4970e8fc9cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "distinguishedNameQualifier", value)

    @builtins.property
    @jsii.member(jsii_name="generationQualifier")
    def generation_qualifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "generationQualifier"))

    @generation_qualifier.setter
    def generation_qualifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9ba21d25028d9b655c5156d013ec8d14da465b898167251627019545bec8042)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "generationQualifier", value)

    @builtins.property
    @jsii.member(jsii_name="givenName")
    def given_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "givenName"))

    @given_name.setter
    def given_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__960847712bfd2a320e99603697d3ebac7a174ee9b23c38bf31f8fa0ee653caad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "givenName", value)

    @builtins.property
    @jsii.member(jsii_name="initials")
    def initials(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "initials"))

    @initials.setter
    def initials(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4af6ec7e553cdcd57f4ab87ada190e2b650ab5534766bcfd9d0d21469b33fada)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initials", value)

    @builtins.property
    @jsii.member(jsii_name="locality")
    def locality(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "locality"))

    @locality.setter
    def locality(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bc6f00965cd36e501092a9f2d2247687741ab30adc99cdeaa3ae40f0f840b75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "locality", value)

    @builtins.property
    @jsii.member(jsii_name="organization")
    def organization(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "organization"))

    @organization.setter
    def organization(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc53d889582a3f57755ac42518422c8ebd4955bde41b5256a99772b861e16404)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organization", value)

    @builtins.property
    @jsii.member(jsii_name="organizationalUnit")
    def organizational_unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "organizationalUnit"))

    @organizational_unit.setter
    def organizational_unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50cf4c7523ba1d3f86349b246c53400c7805a46589ecaf0d2d2523a71ae56426)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organizationalUnit", value)

    @builtins.property
    @jsii.member(jsii_name="pseudonym")
    def pseudonym(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pseudonym"))

    @pseudonym.setter
    def pseudonym(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e80bfb01fe97a100d663858aae36913cc91f3c549d342c6662a8990348c96c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pseudonym", value)

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @state.setter
    def state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7db54000fff6ebf1759413087a44d14cbff0c6d92f0695b7b5d785f20a19fe2a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "state", value)

    @builtins.property
    @jsii.member(jsii_name="surname")
    def surname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "surname"))

    @surname.setter
    def surname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3bb6d4683a7cb9e7a4a3b57332a68f4fba8b6f37ef9198361be6e9e4ac7fcf0a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "surname", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a70aba611ed2ebbb58d61788eb5b5fdd6521759bea23870bba98f74ee81fb8c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AcmpcaCertificateAuthorityCertificateAuthorityConfigurationSubject]:
        return typing.cast(typing.Optional[AcmpcaCertificateAuthorityCertificateAuthorityConfigurationSubject], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AcmpcaCertificateAuthorityCertificateAuthorityConfigurationSubject],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e1898c66d3a7fb356539aefa1f935d905a96f8dbe39ab85589372008f45b457)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.acmpcaCertificateAuthority.AcmpcaCertificateAuthorityConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "certificate_authority_configuration": "certificateAuthorityConfiguration",
        "enabled": "enabled",
        "id": "id",
        "permanent_deletion_time_in_days": "permanentDeletionTimeInDays",
        "revocation_configuration": "revocationConfiguration",
        "tags": "tags",
        "tags_all": "tagsAll",
        "timeouts": "timeouts",
        "type": "type",
        "usage_mode": "usageMode",
    },
)
class AcmpcaCertificateAuthorityConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        certificate_authority_configuration: typing.Union[AcmpcaCertificateAuthorityCertificateAuthorityConfiguration, typing.Dict[builtins.str, typing.Any]],
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        permanent_deletion_time_in_days: typing.Optional[jsii.Number] = None,
        revocation_configuration: typing.Optional[typing.Union["AcmpcaCertificateAuthorityRevocationConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["AcmpcaCertificateAuthorityTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        type: typing.Optional[builtins.str] = None,
        usage_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param certificate_authority_configuration: certificate_authority_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#certificate_authority_configuration AcmpcaCertificateAuthority#certificate_authority_configuration}
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#enabled AcmpcaCertificateAuthority#enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#id AcmpcaCertificateAuthority#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param permanent_deletion_time_in_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#permanent_deletion_time_in_days AcmpcaCertificateAuthority#permanent_deletion_time_in_days}.
        :param revocation_configuration: revocation_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#revocation_configuration AcmpcaCertificateAuthority#revocation_configuration}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#tags AcmpcaCertificateAuthority#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#tags_all AcmpcaCertificateAuthority#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#timeouts AcmpcaCertificateAuthority#timeouts}
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#type AcmpcaCertificateAuthority#type}.
        :param usage_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#usage_mode AcmpcaCertificateAuthority#usage_mode}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(certificate_authority_configuration, dict):
            certificate_authority_configuration = AcmpcaCertificateAuthorityCertificateAuthorityConfiguration(**certificate_authority_configuration)
        if isinstance(revocation_configuration, dict):
            revocation_configuration = AcmpcaCertificateAuthorityRevocationConfiguration(**revocation_configuration)
        if isinstance(timeouts, dict):
            timeouts = AcmpcaCertificateAuthorityTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0362bca8942d500408ea76788fd0401908af5bc34bb43b403dfdd9aa3a6dad90)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument certificate_authority_configuration", value=certificate_authority_configuration, expected_type=type_hints["certificate_authority_configuration"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument permanent_deletion_time_in_days", value=permanent_deletion_time_in_days, expected_type=type_hints["permanent_deletion_time_in_days"])
            check_type(argname="argument revocation_configuration", value=revocation_configuration, expected_type=type_hints["revocation_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument usage_mode", value=usage_mode, expected_type=type_hints["usage_mode"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "certificate_authority_configuration": certificate_authority_configuration,
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
        if enabled is not None:
            self._values["enabled"] = enabled
        if id is not None:
            self._values["id"] = id
        if permanent_deletion_time_in_days is not None:
            self._values["permanent_deletion_time_in_days"] = permanent_deletion_time_in_days
        if revocation_configuration is not None:
            self._values["revocation_configuration"] = revocation_configuration
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if type is not None:
            self._values["type"] = type
        if usage_mode is not None:
            self._values["usage_mode"] = usage_mode

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
    def certificate_authority_configuration(
        self,
    ) -> AcmpcaCertificateAuthorityCertificateAuthorityConfiguration:
        '''certificate_authority_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#certificate_authority_configuration AcmpcaCertificateAuthority#certificate_authority_configuration}
        '''
        result = self._values.get("certificate_authority_configuration")
        assert result is not None, "Required property 'certificate_authority_configuration' is missing"
        return typing.cast(AcmpcaCertificateAuthorityCertificateAuthorityConfiguration, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#enabled AcmpcaCertificateAuthority#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#id AcmpcaCertificateAuthority#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def permanent_deletion_time_in_days(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#permanent_deletion_time_in_days AcmpcaCertificateAuthority#permanent_deletion_time_in_days}.'''
        result = self._values.get("permanent_deletion_time_in_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def revocation_configuration(
        self,
    ) -> typing.Optional["AcmpcaCertificateAuthorityRevocationConfiguration"]:
        '''revocation_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#revocation_configuration AcmpcaCertificateAuthority#revocation_configuration}
        '''
        result = self._values.get("revocation_configuration")
        return typing.cast(typing.Optional["AcmpcaCertificateAuthorityRevocationConfiguration"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#tags AcmpcaCertificateAuthority#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#tags_all AcmpcaCertificateAuthority#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["AcmpcaCertificateAuthorityTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#timeouts AcmpcaCertificateAuthority#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["AcmpcaCertificateAuthorityTimeouts"], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#type AcmpcaCertificateAuthority#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def usage_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#usage_mode AcmpcaCertificateAuthority#usage_mode}.'''
        result = self._values.get("usage_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AcmpcaCertificateAuthorityConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.acmpcaCertificateAuthority.AcmpcaCertificateAuthorityRevocationConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "crl_configuration": "crlConfiguration",
        "ocsp_configuration": "ocspConfiguration",
    },
)
class AcmpcaCertificateAuthorityRevocationConfiguration:
    def __init__(
        self,
        *,
        crl_configuration: typing.Optional[typing.Union["AcmpcaCertificateAuthorityRevocationConfigurationCrlConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        ocsp_configuration: typing.Optional[typing.Union["AcmpcaCertificateAuthorityRevocationConfigurationOcspConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param crl_configuration: crl_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#crl_configuration AcmpcaCertificateAuthority#crl_configuration}
        :param ocsp_configuration: ocsp_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#ocsp_configuration AcmpcaCertificateAuthority#ocsp_configuration}
        '''
        if isinstance(crl_configuration, dict):
            crl_configuration = AcmpcaCertificateAuthorityRevocationConfigurationCrlConfiguration(**crl_configuration)
        if isinstance(ocsp_configuration, dict):
            ocsp_configuration = AcmpcaCertificateAuthorityRevocationConfigurationOcspConfiguration(**ocsp_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1b4d21353e960c82fd386ae22b14897dcc8a626e6151db84f61d9359b1b0f68)
            check_type(argname="argument crl_configuration", value=crl_configuration, expected_type=type_hints["crl_configuration"])
            check_type(argname="argument ocsp_configuration", value=ocsp_configuration, expected_type=type_hints["ocsp_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if crl_configuration is not None:
            self._values["crl_configuration"] = crl_configuration
        if ocsp_configuration is not None:
            self._values["ocsp_configuration"] = ocsp_configuration

    @builtins.property
    def crl_configuration(
        self,
    ) -> typing.Optional["AcmpcaCertificateAuthorityRevocationConfigurationCrlConfiguration"]:
        '''crl_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#crl_configuration AcmpcaCertificateAuthority#crl_configuration}
        '''
        result = self._values.get("crl_configuration")
        return typing.cast(typing.Optional["AcmpcaCertificateAuthorityRevocationConfigurationCrlConfiguration"], result)

    @builtins.property
    def ocsp_configuration(
        self,
    ) -> typing.Optional["AcmpcaCertificateAuthorityRevocationConfigurationOcspConfiguration"]:
        '''ocsp_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#ocsp_configuration AcmpcaCertificateAuthority#ocsp_configuration}
        '''
        result = self._values.get("ocsp_configuration")
        return typing.cast(typing.Optional["AcmpcaCertificateAuthorityRevocationConfigurationOcspConfiguration"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AcmpcaCertificateAuthorityRevocationConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.acmpcaCertificateAuthority.AcmpcaCertificateAuthorityRevocationConfigurationCrlConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "expiration_in_days": "expirationInDays",
        "custom_cname": "customCname",
        "enabled": "enabled",
        "s3_bucket_name": "s3BucketName",
        "s3_object_acl": "s3ObjectAcl",
    },
)
class AcmpcaCertificateAuthorityRevocationConfigurationCrlConfiguration:
    def __init__(
        self,
        *,
        expiration_in_days: jsii.Number,
        custom_cname: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        s3_bucket_name: typing.Optional[builtins.str] = None,
        s3_object_acl: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param expiration_in_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#expiration_in_days AcmpcaCertificateAuthority#expiration_in_days}.
        :param custom_cname: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#custom_cname AcmpcaCertificateAuthority#custom_cname}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#enabled AcmpcaCertificateAuthority#enabled}.
        :param s3_bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#s3_bucket_name AcmpcaCertificateAuthority#s3_bucket_name}.
        :param s3_object_acl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#s3_object_acl AcmpcaCertificateAuthority#s3_object_acl}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__746a34ef1260243f381bd4b4edce1822eba9e7fca86ba4029bd6898ce05841cf)
            check_type(argname="argument expiration_in_days", value=expiration_in_days, expected_type=type_hints["expiration_in_days"])
            check_type(argname="argument custom_cname", value=custom_cname, expected_type=type_hints["custom_cname"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument s3_bucket_name", value=s3_bucket_name, expected_type=type_hints["s3_bucket_name"])
            check_type(argname="argument s3_object_acl", value=s3_object_acl, expected_type=type_hints["s3_object_acl"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "expiration_in_days": expiration_in_days,
        }
        if custom_cname is not None:
            self._values["custom_cname"] = custom_cname
        if enabled is not None:
            self._values["enabled"] = enabled
        if s3_bucket_name is not None:
            self._values["s3_bucket_name"] = s3_bucket_name
        if s3_object_acl is not None:
            self._values["s3_object_acl"] = s3_object_acl

    @builtins.property
    def expiration_in_days(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#expiration_in_days AcmpcaCertificateAuthority#expiration_in_days}.'''
        result = self._values.get("expiration_in_days")
        assert result is not None, "Required property 'expiration_in_days' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def custom_cname(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#custom_cname AcmpcaCertificateAuthority#custom_cname}.'''
        result = self._values.get("custom_cname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#enabled AcmpcaCertificateAuthority#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def s3_bucket_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#s3_bucket_name AcmpcaCertificateAuthority#s3_bucket_name}.'''
        result = self._values.get("s3_bucket_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_object_acl(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#s3_object_acl AcmpcaCertificateAuthority#s3_object_acl}.'''
        result = self._values.get("s3_object_acl")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AcmpcaCertificateAuthorityRevocationConfigurationCrlConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AcmpcaCertificateAuthorityRevocationConfigurationCrlConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.acmpcaCertificateAuthority.AcmpcaCertificateAuthorityRevocationConfigurationCrlConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a7236c6ea1678def059d47a12d36514e1c157aadc6267a58e1c78e8addbd54d8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCustomCname")
    def reset_custom_cname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomCname", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetS3BucketName")
    def reset_s3_bucket_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3BucketName", []))

    @jsii.member(jsii_name="resetS3ObjectAcl")
    def reset_s3_object_acl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3ObjectAcl", []))

    @builtins.property
    @jsii.member(jsii_name="customCnameInput")
    def custom_cname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customCnameInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="expirationInDaysInput")
    def expiration_in_days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "expirationInDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="s3BucketNameInput")
    def s3_bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3BucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="s3ObjectAclInput")
    def s3_object_acl_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3ObjectAclInput"))

    @builtins.property
    @jsii.member(jsii_name="customCname")
    def custom_cname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customCname"))

    @custom_cname.setter
    def custom_cname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6ac87fb5f5eedc33b1cad1e24c1db9486be1cb0a51e7ee7ee420978260dee95)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customCname", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__69cdb01550f9babce2a8554064f55b917383b7d487a15de9a39d706fb7ff3779)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="expirationInDays")
    def expiration_in_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "expirationInDays"))

    @expiration_in_days.setter
    def expiration_in_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8286c671adeb50ff809441e1673c46a63103c1176b3a6a93ce8d2e5f6d1dddd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expirationInDays", value)

    @builtins.property
    @jsii.member(jsii_name="s3BucketName")
    def s3_bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3BucketName"))

    @s3_bucket_name.setter
    def s3_bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__168711cca9d680b24b03d84777043a056bb17aa2fdb69fa6a7a7ff3b500e41c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3BucketName", value)

    @builtins.property
    @jsii.member(jsii_name="s3ObjectAcl")
    def s3_object_acl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3ObjectAcl"))

    @s3_object_acl.setter
    def s3_object_acl(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86b0b8f67c9be49990a3dab8859729e4e0b498d6953ea5f8079b63fbea35bb60)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3ObjectAcl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AcmpcaCertificateAuthorityRevocationConfigurationCrlConfiguration]:
        return typing.cast(typing.Optional[AcmpcaCertificateAuthorityRevocationConfigurationCrlConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AcmpcaCertificateAuthorityRevocationConfigurationCrlConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5e28760ffdfb407ccf428678d60c0307d89ab0f2b51e04e5139330dd065513d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.acmpcaCertificateAuthority.AcmpcaCertificateAuthorityRevocationConfigurationOcspConfiguration",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "ocsp_custom_cname": "ocspCustomCname"},
)
class AcmpcaCertificateAuthorityRevocationConfigurationOcspConfiguration:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        ocsp_custom_cname: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#enabled AcmpcaCertificateAuthority#enabled}.
        :param ocsp_custom_cname: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#ocsp_custom_cname AcmpcaCertificateAuthority#ocsp_custom_cname}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a20cf81593f06ab79a00ee3bfff4f298665a1a6be3bd94b807601cc015fe742)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument ocsp_custom_cname", value=ocsp_custom_cname, expected_type=type_hints["ocsp_custom_cname"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "enabled": enabled,
        }
        if ocsp_custom_cname is not None:
            self._values["ocsp_custom_cname"] = ocsp_custom_cname

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#enabled AcmpcaCertificateAuthority#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def ocsp_custom_cname(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#ocsp_custom_cname AcmpcaCertificateAuthority#ocsp_custom_cname}.'''
        result = self._values.get("ocsp_custom_cname")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AcmpcaCertificateAuthorityRevocationConfigurationOcspConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AcmpcaCertificateAuthorityRevocationConfigurationOcspConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.acmpcaCertificateAuthority.AcmpcaCertificateAuthorityRevocationConfigurationOcspConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__450eeffb8f4827443f0e19388a1b459b01e91401f8a9952b19ce07ec16bb5fe2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetOcspCustomCname")
    def reset_ocsp_custom_cname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOcspCustomCname", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="ocspCustomCnameInput")
    def ocsp_custom_cname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ocspCustomCnameInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__e87ec7ad15411fb91e4956f3a87d264b4233c52a6831798df1624644647b85fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="ocspCustomCname")
    def ocsp_custom_cname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ocspCustomCname"))

    @ocsp_custom_cname.setter
    def ocsp_custom_cname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c2093fc32620b3a33a6ed31064e1f8ad617e7bcb6058de503bb70245e952c3f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ocspCustomCname", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AcmpcaCertificateAuthorityRevocationConfigurationOcspConfiguration]:
        return typing.cast(typing.Optional[AcmpcaCertificateAuthorityRevocationConfigurationOcspConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AcmpcaCertificateAuthorityRevocationConfigurationOcspConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0924f43ddf9bee8daca2033887ed0ff3ba1aeb382390f352868ed827d1230f47)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AcmpcaCertificateAuthorityRevocationConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.acmpcaCertificateAuthority.AcmpcaCertificateAuthorityRevocationConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f6ae4a60e8d4e5dbddb2c040175786ea61051229d9a456258423c45972573007)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCrlConfiguration")
    def put_crl_configuration(
        self,
        *,
        expiration_in_days: jsii.Number,
        custom_cname: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        s3_bucket_name: typing.Optional[builtins.str] = None,
        s3_object_acl: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param expiration_in_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#expiration_in_days AcmpcaCertificateAuthority#expiration_in_days}.
        :param custom_cname: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#custom_cname AcmpcaCertificateAuthority#custom_cname}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#enabled AcmpcaCertificateAuthority#enabled}.
        :param s3_bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#s3_bucket_name AcmpcaCertificateAuthority#s3_bucket_name}.
        :param s3_object_acl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#s3_object_acl AcmpcaCertificateAuthority#s3_object_acl}.
        '''
        value = AcmpcaCertificateAuthorityRevocationConfigurationCrlConfiguration(
            expiration_in_days=expiration_in_days,
            custom_cname=custom_cname,
            enabled=enabled,
            s3_bucket_name=s3_bucket_name,
            s3_object_acl=s3_object_acl,
        )

        return typing.cast(None, jsii.invoke(self, "putCrlConfiguration", [value]))

    @jsii.member(jsii_name="putOcspConfiguration")
    def put_ocsp_configuration(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        ocsp_custom_cname: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#enabled AcmpcaCertificateAuthority#enabled}.
        :param ocsp_custom_cname: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#ocsp_custom_cname AcmpcaCertificateAuthority#ocsp_custom_cname}.
        '''
        value = AcmpcaCertificateAuthorityRevocationConfigurationOcspConfiguration(
            enabled=enabled, ocsp_custom_cname=ocsp_custom_cname
        )

        return typing.cast(None, jsii.invoke(self, "putOcspConfiguration", [value]))

    @jsii.member(jsii_name="resetCrlConfiguration")
    def reset_crl_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCrlConfiguration", []))

    @jsii.member(jsii_name="resetOcspConfiguration")
    def reset_ocsp_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOcspConfiguration", []))

    @builtins.property
    @jsii.member(jsii_name="crlConfiguration")
    def crl_configuration(
        self,
    ) -> AcmpcaCertificateAuthorityRevocationConfigurationCrlConfigurationOutputReference:
        return typing.cast(AcmpcaCertificateAuthorityRevocationConfigurationCrlConfigurationOutputReference, jsii.get(self, "crlConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="ocspConfiguration")
    def ocsp_configuration(
        self,
    ) -> AcmpcaCertificateAuthorityRevocationConfigurationOcspConfigurationOutputReference:
        return typing.cast(AcmpcaCertificateAuthorityRevocationConfigurationOcspConfigurationOutputReference, jsii.get(self, "ocspConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="crlConfigurationInput")
    def crl_configuration_input(
        self,
    ) -> typing.Optional[AcmpcaCertificateAuthorityRevocationConfigurationCrlConfiguration]:
        return typing.cast(typing.Optional[AcmpcaCertificateAuthorityRevocationConfigurationCrlConfiguration], jsii.get(self, "crlConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="ocspConfigurationInput")
    def ocsp_configuration_input(
        self,
    ) -> typing.Optional[AcmpcaCertificateAuthorityRevocationConfigurationOcspConfiguration]:
        return typing.cast(typing.Optional[AcmpcaCertificateAuthorityRevocationConfigurationOcspConfiguration], jsii.get(self, "ocspConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AcmpcaCertificateAuthorityRevocationConfiguration]:
        return typing.cast(typing.Optional[AcmpcaCertificateAuthorityRevocationConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AcmpcaCertificateAuthorityRevocationConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81950c242472df381cf7a77a01c52b63e6d36a4adf1c14ddad3540a75eb9ce2c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.acmpcaCertificateAuthority.AcmpcaCertificateAuthorityTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create"},
)
class AcmpcaCertificateAuthorityTimeouts:
    def __init__(self, *, create: typing.Optional[builtins.str] = None) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#create AcmpcaCertificateAuthority#create}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02a64d6097355be6fd38f82dfbb419747bc3c7f6911e5cd186a840e3f28af967)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/acmpca_certificate_authority#create AcmpcaCertificateAuthority#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AcmpcaCertificateAuthorityTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AcmpcaCertificateAuthorityTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.acmpcaCertificateAuthority.AcmpcaCertificateAuthorityTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2d4bd43a6197e209f680fc5f2c9c3a3687076aa5b1f8fc2b4a9bda11d9f10903)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f51d1b120050b5c4e97f6a99bca5040f38bdecfaee3d23d4e3f14e4f95a7970)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AcmpcaCertificateAuthorityTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AcmpcaCertificateAuthorityTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AcmpcaCertificateAuthorityTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7c74fab7ff59a0306c047cb9c39950995b0646ce1beaf0263a3c27c9070640c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "AcmpcaCertificateAuthority",
    "AcmpcaCertificateAuthorityCertificateAuthorityConfiguration",
    "AcmpcaCertificateAuthorityCertificateAuthorityConfigurationOutputReference",
    "AcmpcaCertificateAuthorityCertificateAuthorityConfigurationSubject",
    "AcmpcaCertificateAuthorityCertificateAuthorityConfigurationSubjectOutputReference",
    "AcmpcaCertificateAuthorityConfig",
    "AcmpcaCertificateAuthorityRevocationConfiguration",
    "AcmpcaCertificateAuthorityRevocationConfigurationCrlConfiguration",
    "AcmpcaCertificateAuthorityRevocationConfigurationCrlConfigurationOutputReference",
    "AcmpcaCertificateAuthorityRevocationConfigurationOcspConfiguration",
    "AcmpcaCertificateAuthorityRevocationConfigurationOcspConfigurationOutputReference",
    "AcmpcaCertificateAuthorityRevocationConfigurationOutputReference",
    "AcmpcaCertificateAuthorityTimeouts",
    "AcmpcaCertificateAuthorityTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__55321c0c1c48f20ecad667914b61c2c157aa9cc699e2758a9f1ccb955e9666a4(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    certificate_authority_configuration: typing.Union[AcmpcaCertificateAuthorityCertificateAuthorityConfiguration, typing.Dict[builtins.str, typing.Any]],
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    permanent_deletion_time_in_days: typing.Optional[jsii.Number] = None,
    revocation_configuration: typing.Optional[typing.Union[AcmpcaCertificateAuthorityRevocationConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[AcmpcaCertificateAuthorityTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    type: typing.Optional[builtins.str] = None,
    usage_mode: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__3efb64d3fab8578e712436590a712f720a159aa0fe2690cc1087736bb99f2528(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d603340f31ab6df9cd235dbb7870a9d2a0d2d7fc64e7e24ad1b3d310ffee6851(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2c46d6908577809136d2e2d373c84645103ee98ed71b7870f7774a8a41a747c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8378142fcfce929c41f17885d42ac1d904c0a2c1798f1ddb19d11669fc8a39c0(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f027ac1f5805868c3c21327a37180661b4c10f02f28e90ae8097505b44cc244(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40e278ceea5d7abf659684e281bfeb77ec3e1a4342524a129a93b77970546a90(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d87ecda6db453e90dfde28adf9a1e4c434224609c7d01b4ab8bea903d5e169a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a8aae2eef32164796fe038e1566b863a44e3370c71c9808c35169b93361a12c(
    *,
    key_algorithm: builtins.str,
    signing_algorithm: builtins.str,
    subject: typing.Union[AcmpcaCertificateAuthorityCertificateAuthorityConfigurationSubject, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3491cdb4b84914d26096c66221398dae15648cda72d1b833fd5c7779c468d54(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7dd1500a2b3e395c9671fc749ecf31fac69b95ad48a2fcf4e1cca110a61b4575(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0b0c82db142aa93be843f465c3acfb8c3692f38606c90c4e9a77fdadf4e28e6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2966cf00c8a9c9e1d8dd3135264055fda1f85035b59efe497064ef5d2b7cf8f8(
    value: typing.Optional[AcmpcaCertificateAuthorityCertificateAuthorityConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__284efeffd3ca8c61b39f87931feb63d402522de00cc5947d6a9bf0e9e291dd6e(
    *,
    common_name: typing.Optional[builtins.str] = None,
    country: typing.Optional[builtins.str] = None,
    distinguished_name_qualifier: typing.Optional[builtins.str] = None,
    generation_qualifier: typing.Optional[builtins.str] = None,
    given_name: typing.Optional[builtins.str] = None,
    initials: typing.Optional[builtins.str] = None,
    locality: typing.Optional[builtins.str] = None,
    organization: typing.Optional[builtins.str] = None,
    organizational_unit: typing.Optional[builtins.str] = None,
    pseudonym: typing.Optional[builtins.str] = None,
    state: typing.Optional[builtins.str] = None,
    surname: typing.Optional[builtins.str] = None,
    title: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7ee5e594747a2e0eca37fb4ae6730e4dc2e07d12685ff03c63a9eb7f3c72635(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a47ccb9f0fcc553b2ce1381cebdbfa8e5775e3c0c703f83c0f14b3d26417ee2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54e84660cee05c32795d453367cd9be73ebf095ca3c69b479aa77792ba02b279(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6a562e5ceee12db93b915114f5a093728abcce153efcde8af49f4970e8fc9cf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9ba21d25028d9b655c5156d013ec8d14da465b898167251627019545bec8042(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__960847712bfd2a320e99603697d3ebac7a174ee9b23c38bf31f8fa0ee653caad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4af6ec7e553cdcd57f4ab87ada190e2b650ab5534766bcfd9d0d21469b33fada(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bc6f00965cd36e501092a9f2d2247687741ab30adc99cdeaa3ae40f0f840b75(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc53d889582a3f57755ac42518422c8ebd4955bde41b5256a99772b861e16404(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50cf4c7523ba1d3f86349b246c53400c7805a46589ecaf0d2d2523a71ae56426(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e80bfb01fe97a100d663858aae36913cc91f3c549d342c6662a8990348c96c1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7db54000fff6ebf1759413087a44d14cbff0c6d92f0695b7b5d785f20a19fe2a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bb6d4683a7cb9e7a4a3b57332a68f4fba8b6f37ef9198361be6e9e4ac7fcf0a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a70aba611ed2ebbb58d61788eb5b5fdd6521759bea23870bba98f74ee81fb8c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e1898c66d3a7fb356539aefa1f935d905a96f8dbe39ab85589372008f45b457(
    value: typing.Optional[AcmpcaCertificateAuthorityCertificateAuthorityConfigurationSubject],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0362bca8942d500408ea76788fd0401908af5bc34bb43b403dfdd9aa3a6dad90(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    certificate_authority_configuration: typing.Union[AcmpcaCertificateAuthorityCertificateAuthorityConfiguration, typing.Dict[builtins.str, typing.Any]],
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    permanent_deletion_time_in_days: typing.Optional[jsii.Number] = None,
    revocation_configuration: typing.Optional[typing.Union[AcmpcaCertificateAuthorityRevocationConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[AcmpcaCertificateAuthorityTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    type: typing.Optional[builtins.str] = None,
    usage_mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1b4d21353e960c82fd386ae22b14897dcc8a626e6151db84f61d9359b1b0f68(
    *,
    crl_configuration: typing.Optional[typing.Union[AcmpcaCertificateAuthorityRevocationConfigurationCrlConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    ocsp_configuration: typing.Optional[typing.Union[AcmpcaCertificateAuthorityRevocationConfigurationOcspConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__746a34ef1260243f381bd4b4edce1822eba9e7fca86ba4029bd6898ce05841cf(
    *,
    expiration_in_days: jsii.Number,
    custom_cname: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    s3_bucket_name: typing.Optional[builtins.str] = None,
    s3_object_acl: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7236c6ea1678def059d47a12d36514e1c157aadc6267a58e1c78e8addbd54d8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6ac87fb5f5eedc33b1cad1e24c1db9486be1cb0a51e7ee7ee420978260dee95(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69cdb01550f9babce2a8554064f55b917383b7d487a15de9a39d706fb7ff3779(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8286c671adeb50ff809441e1673c46a63103c1176b3a6a93ce8d2e5f6d1dddd(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__168711cca9d680b24b03d84777043a056bb17aa2fdb69fa6a7a7ff3b500e41c2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86b0b8f67c9be49990a3dab8859729e4e0b498d6953ea5f8079b63fbea35bb60(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5e28760ffdfb407ccf428678d60c0307d89ab0f2b51e04e5139330dd065513d(
    value: typing.Optional[AcmpcaCertificateAuthorityRevocationConfigurationCrlConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a20cf81593f06ab79a00ee3bfff4f298665a1a6be3bd94b807601cc015fe742(
    *,
    enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ocsp_custom_cname: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__450eeffb8f4827443f0e19388a1b459b01e91401f8a9952b19ce07ec16bb5fe2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e87ec7ad15411fb91e4956f3a87d264b4233c52a6831798df1624644647b85fb(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c2093fc32620b3a33a6ed31064e1f8ad617e7bcb6058de503bb70245e952c3f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0924f43ddf9bee8daca2033887ed0ff3ba1aeb382390f352868ed827d1230f47(
    value: typing.Optional[AcmpcaCertificateAuthorityRevocationConfigurationOcspConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6ae4a60e8d4e5dbddb2c040175786ea61051229d9a456258423c45972573007(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81950c242472df381cf7a77a01c52b63e6d36a4adf1c14ddad3540a75eb9ce2c(
    value: typing.Optional[AcmpcaCertificateAuthorityRevocationConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02a64d6097355be6fd38f82dfbb419747bc3c7f6911e5cd186a840e3f28af967(
    *,
    create: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d4bd43a6197e209f680fc5f2c9c3a3687076aa5b1f8fc2b4a9bda11d9f10903(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f51d1b120050b5c4e97f6a99bca5040f38bdecfaee3d23d4e3f14e4f95a7970(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7c74fab7ff59a0306c047cb9c39950995b0646ce1beaf0263a3c27c9070640c(
    value: typing.Optional[typing.Union[AcmpcaCertificateAuthorityTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
