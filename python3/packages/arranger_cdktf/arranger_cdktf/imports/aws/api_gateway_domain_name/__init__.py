'''
# `aws_api_gateway_domain_name`

Refer to the Terraform Registory for docs: [`aws_api_gateway_domain_name`](https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name).
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


class ApiGatewayDomainName(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.apiGatewayDomainName.ApiGatewayDomainName",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name aws_api_gateway_domain_name}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        domain_name: builtins.str,
        certificate_arn: typing.Optional[builtins.str] = None,
        certificate_body: typing.Optional[builtins.str] = None,
        certificate_chain: typing.Optional[builtins.str] = None,
        certificate_name: typing.Optional[builtins.str] = None,
        certificate_private_key: typing.Optional[builtins.str] = None,
        endpoint_configuration: typing.Optional[typing.Union["ApiGatewayDomainNameEndpointConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        mutual_tls_authentication: typing.Optional[typing.Union["ApiGatewayDomainNameMutualTlsAuthentication", typing.Dict[builtins.str, typing.Any]]] = None,
        ownership_verification_certificate_arn: typing.Optional[builtins.str] = None,
        regional_certificate_arn: typing.Optional[builtins.str] = None,
        regional_certificate_name: typing.Optional[builtins.str] = None,
        security_policy: typing.Optional[builtins.str] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name aws_api_gateway_domain_name} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#domain_name ApiGatewayDomainName#domain_name}.
        :param certificate_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#certificate_arn ApiGatewayDomainName#certificate_arn}.
        :param certificate_body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#certificate_body ApiGatewayDomainName#certificate_body}.
        :param certificate_chain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#certificate_chain ApiGatewayDomainName#certificate_chain}.
        :param certificate_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#certificate_name ApiGatewayDomainName#certificate_name}.
        :param certificate_private_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#certificate_private_key ApiGatewayDomainName#certificate_private_key}.
        :param endpoint_configuration: endpoint_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#endpoint_configuration ApiGatewayDomainName#endpoint_configuration}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#id ApiGatewayDomainName#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param mutual_tls_authentication: mutual_tls_authentication block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#mutual_tls_authentication ApiGatewayDomainName#mutual_tls_authentication}
        :param ownership_verification_certificate_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#ownership_verification_certificate_arn ApiGatewayDomainName#ownership_verification_certificate_arn}.
        :param regional_certificate_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#regional_certificate_arn ApiGatewayDomainName#regional_certificate_arn}.
        :param regional_certificate_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#regional_certificate_name ApiGatewayDomainName#regional_certificate_name}.
        :param security_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#security_policy ApiGatewayDomainName#security_policy}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#tags ApiGatewayDomainName#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#tags_all ApiGatewayDomainName#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__503bf2fe914cf384a912f45c9f1fb809f9d3a2d682cb1529ccd322b2f97f724f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ApiGatewayDomainNameConfig(
            domain_name=domain_name,
            certificate_arn=certificate_arn,
            certificate_body=certificate_body,
            certificate_chain=certificate_chain,
            certificate_name=certificate_name,
            certificate_private_key=certificate_private_key,
            endpoint_configuration=endpoint_configuration,
            id=id,
            mutual_tls_authentication=mutual_tls_authentication,
            ownership_verification_certificate_arn=ownership_verification_certificate_arn,
            regional_certificate_arn=regional_certificate_arn,
            regional_certificate_name=regional_certificate_name,
            security_policy=security_policy,
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

    @jsii.member(jsii_name="putEndpointConfiguration")
    def put_endpoint_configuration(
        self,
        *,
        types: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#types ApiGatewayDomainName#types}.
        '''
        value = ApiGatewayDomainNameEndpointConfiguration(types=types)

        return typing.cast(None, jsii.invoke(self, "putEndpointConfiguration", [value]))

    @jsii.member(jsii_name="putMutualTlsAuthentication")
    def put_mutual_tls_authentication(
        self,
        *,
        truststore_uri: builtins.str,
        truststore_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param truststore_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#truststore_uri ApiGatewayDomainName#truststore_uri}.
        :param truststore_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#truststore_version ApiGatewayDomainName#truststore_version}.
        '''
        value = ApiGatewayDomainNameMutualTlsAuthentication(
            truststore_uri=truststore_uri, truststore_version=truststore_version
        )

        return typing.cast(None, jsii.invoke(self, "putMutualTlsAuthentication", [value]))

    @jsii.member(jsii_name="resetCertificateArn")
    def reset_certificate_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificateArn", []))

    @jsii.member(jsii_name="resetCertificateBody")
    def reset_certificate_body(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificateBody", []))

    @jsii.member(jsii_name="resetCertificateChain")
    def reset_certificate_chain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificateChain", []))

    @jsii.member(jsii_name="resetCertificateName")
    def reset_certificate_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificateName", []))

    @jsii.member(jsii_name="resetCertificatePrivateKey")
    def reset_certificate_private_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificatePrivateKey", []))

    @jsii.member(jsii_name="resetEndpointConfiguration")
    def reset_endpoint_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndpointConfiguration", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMutualTlsAuthentication")
    def reset_mutual_tls_authentication(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMutualTlsAuthentication", []))

    @jsii.member(jsii_name="resetOwnershipVerificationCertificateArn")
    def reset_ownership_verification_certificate_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOwnershipVerificationCertificateArn", []))

    @jsii.member(jsii_name="resetRegionalCertificateArn")
    def reset_regional_certificate_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegionalCertificateArn", []))

    @jsii.member(jsii_name="resetRegionalCertificateName")
    def reset_regional_certificate_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegionalCertificateName", []))

    @jsii.member(jsii_name="resetSecurityPolicy")
    def reset_security_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityPolicy", []))

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
    @jsii.member(jsii_name="certificateUploadDate")
    def certificate_upload_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateUploadDate"))

    @builtins.property
    @jsii.member(jsii_name="cloudfrontDomainName")
    def cloudfront_domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudfrontDomainName"))

    @builtins.property
    @jsii.member(jsii_name="cloudfrontZoneId")
    def cloudfront_zone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudfrontZoneId"))

    @builtins.property
    @jsii.member(jsii_name="endpointConfiguration")
    def endpoint_configuration(
        self,
    ) -> "ApiGatewayDomainNameEndpointConfigurationOutputReference":
        return typing.cast("ApiGatewayDomainNameEndpointConfigurationOutputReference", jsii.get(self, "endpointConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="mutualTlsAuthentication")
    def mutual_tls_authentication(
        self,
    ) -> "ApiGatewayDomainNameMutualTlsAuthenticationOutputReference":
        return typing.cast("ApiGatewayDomainNameMutualTlsAuthenticationOutputReference", jsii.get(self, "mutualTlsAuthentication"))

    @builtins.property
    @jsii.member(jsii_name="regionalDomainName")
    def regional_domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "regionalDomainName"))

    @builtins.property
    @jsii.member(jsii_name="regionalZoneId")
    def regional_zone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "regionalZoneId"))

    @builtins.property
    @jsii.member(jsii_name="certificateArnInput")
    def certificate_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateArnInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateBodyInput")
    def certificate_body_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateBodyInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateChainInput")
    def certificate_chain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateChainInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateNameInput")
    def certificate_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateNameInput"))

    @builtins.property
    @jsii.member(jsii_name="certificatePrivateKeyInput")
    def certificate_private_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificatePrivateKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="domainNameInput")
    def domain_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainNameInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointConfigurationInput")
    def endpoint_configuration_input(
        self,
    ) -> typing.Optional["ApiGatewayDomainNameEndpointConfiguration"]:
        return typing.cast(typing.Optional["ApiGatewayDomainNameEndpointConfiguration"], jsii.get(self, "endpointConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="mutualTlsAuthenticationInput")
    def mutual_tls_authentication_input(
        self,
    ) -> typing.Optional["ApiGatewayDomainNameMutualTlsAuthentication"]:
        return typing.cast(typing.Optional["ApiGatewayDomainNameMutualTlsAuthentication"], jsii.get(self, "mutualTlsAuthenticationInput"))

    @builtins.property
    @jsii.member(jsii_name="ownershipVerificationCertificateArnInput")
    def ownership_verification_certificate_arn_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ownershipVerificationCertificateArnInput"))

    @builtins.property
    @jsii.member(jsii_name="regionalCertificateArnInput")
    def regional_certificate_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionalCertificateArnInput"))

    @builtins.property
    @jsii.member(jsii_name="regionalCertificateNameInput")
    def regional_certificate_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionalCertificateNameInput"))

    @builtins.property
    @jsii.member(jsii_name="securityPolicyInput")
    def security_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "securityPolicyInput"))

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
    @jsii.member(jsii_name="certificateArn")
    def certificate_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateArn"))

    @certificate_arn.setter
    def certificate_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04529f21594923d4682bf3360bf3a0cb2b927a74bfc2b4d7afde1cf6b06c7d7c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateArn", value)

    @builtins.property
    @jsii.member(jsii_name="certificateBody")
    def certificate_body(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateBody"))

    @certificate_body.setter
    def certificate_body(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c309742f710f221ffb0bcd2b858f0ed0a523b0099d55bc7877875ff2a8c5c0ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateBody", value)

    @builtins.property
    @jsii.member(jsii_name="certificateChain")
    def certificate_chain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateChain"))

    @certificate_chain.setter
    def certificate_chain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d67ffb3cd702596e9bdd8bb9314c78a1748a38478dcb7a3ccd0cd71cdf5f3d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateChain", value)

    @builtins.property
    @jsii.member(jsii_name="certificateName")
    def certificate_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateName"))

    @certificate_name.setter
    def certificate_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51fd76cbfa2ab82a81f65616a793367fd453f087d9a3e41af1f07a9611e20356)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateName", value)

    @builtins.property
    @jsii.member(jsii_name="certificatePrivateKey")
    def certificate_private_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificatePrivateKey"))

    @certificate_private_key.setter
    def certificate_private_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5b484be5c9f1db48463c6a78a58207b4073c99a54750405947ebcd90be58c96)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificatePrivateKey", value)

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee5bcfd0e2ca3c5d93463763472c3aa0222ca1abe63d828eadcdadf50771bf88)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e494b270ea92e91e9a7e5d7e0f53b94337cec501f00f6435596a3c2fc3ae6741)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ownershipVerificationCertificateArn")
    def ownership_verification_certificate_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ownershipVerificationCertificateArn"))

    @ownership_verification_certificate_arn.setter
    def ownership_verification_certificate_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f161363c2c397088d701a5b218eaa37195499e184f35e3d9a042ec93880649aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ownershipVerificationCertificateArn", value)

    @builtins.property
    @jsii.member(jsii_name="regionalCertificateArn")
    def regional_certificate_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "regionalCertificateArn"))

    @regional_certificate_arn.setter
    def regional_certificate_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2823479db1d15b2ca1e6274fcc037f1fb2e2d0b43ae342d4a8a6363277d71594)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regionalCertificateArn", value)

    @builtins.property
    @jsii.member(jsii_name="regionalCertificateName")
    def regional_certificate_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "regionalCertificateName"))

    @regional_certificate_name.setter
    def regional_certificate_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8c66a092d1922eb0ca28044e1cfc7d35016db0d719719003d31ab0abaf7d565)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regionalCertificateName", value)

    @builtins.property
    @jsii.member(jsii_name="securityPolicy")
    def security_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "securityPolicy"))

    @security_policy.setter
    def security_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8cd0882e253f64cd907b09f32f575da1b8f7978194113b0f3113a41e856f17ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__679e8a2941852289d5674b73666fae01e2e0fc2346dc231cb1eba3b8ed16655a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99417cda75adccbd5e93640e40ba4a9965e9099970e84733c2bea657a1b1e3ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.apiGatewayDomainName.ApiGatewayDomainNameConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "domain_name": "domainName",
        "certificate_arn": "certificateArn",
        "certificate_body": "certificateBody",
        "certificate_chain": "certificateChain",
        "certificate_name": "certificateName",
        "certificate_private_key": "certificatePrivateKey",
        "endpoint_configuration": "endpointConfiguration",
        "id": "id",
        "mutual_tls_authentication": "mutualTlsAuthentication",
        "ownership_verification_certificate_arn": "ownershipVerificationCertificateArn",
        "regional_certificate_arn": "regionalCertificateArn",
        "regional_certificate_name": "regionalCertificateName",
        "security_policy": "securityPolicy",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class ApiGatewayDomainNameConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        domain_name: builtins.str,
        certificate_arn: typing.Optional[builtins.str] = None,
        certificate_body: typing.Optional[builtins.str] = None,
        certificate_chain: typing.Optional[builtins.str] = None,
        certificate_name: typing.Optional[builtins.str] = None,
        certificate_private_key: typing.Optional[builtins.str] = None,
        endpoint_configuration: typing.Optional[typing.Union["ApiGatewayDomainNameEndpointConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        mutual_tls_authentication: typing.Optional[typing.Union["ApiGatewayDomainNameMutualTlsAuthentication", typing.Dict[builtins.str, typing.Any]]] = None,
        ownership_verification_certificate_arn: typing.Optional[builtins.str] = None,
        regional_certificate_arn: typing.Optional[builtins.str] = None,
        regional_certificate_name: typing.Optional[builtins.str] = None,
        security_policy: typing.Optional[builtins.str] = None,
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
        :param domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#domain_name ApiGatewayDomainName#domain_name}.
        :param certificate_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#certificate_arn ApiGatewayDomainName#certificate_arn}.
        :param certificate_body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#certificate_body ApiGatewayDomainName#certificate_body}.
        :param certificate_chain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#certificate_chain ApiGatewayDomainName#certificate_chain}.
        :param certificate_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#certificate_name ApiGatewayDomainName#certificate_name}.
        :param certificate_private_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#certificate_private_key ApiGatewayDomainName#certificate_private_key}.
        :param endpoint_configuration: endpoint_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#endpoint_configuration ApiGatewayDomainName#endpoint_configuration}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#id ApiGatewayDomainName#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param mutual_tls_authentication: mutual_tls_authentication block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#mutual_tls_authentication ApiGatewayDomainName#mutual_tls_authentication}
        :param ownership_verification_certificate_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#ownership_verification_certificate_arn ApiGatewayDomainName#ownership_verification_certificate_arn}.
        :param regional_certificate_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#regional_certificate_arn ApiGatewayDomainName#regional_certificate_arn}.
        :param regional_certificate_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#regional_certificate_name ApiGatewayDomainName#regional_certificate_name}.
        :param security_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#security_policy ApiGatewayDomainName#security_policy}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#tags ApiGatewayDomainName#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#tags_all ApiGatewayDomainName#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(endpoint_configuration, dict):
            endpoint_configuration = ApiGatewayDomainNameEndpointConfiguration(**endpoint_configuration)
        if isinstance(mutual_tls_authentication, dict):
            mutual_tls_authentication = ApiGatewayDomainNameMutualTlsAuthentication(**mutual_tls_authentication)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d37ecfb9b4af98aec1c7432b4393240fb89f411d637ced5411c985617a599a9d)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument certificate_arn", value=certificate_arn, expected_type=type_hints["certificate_arn"])
            check_type(argname="argument certificate_body", value=certificate_body, expected_type=type_hints["certificate_body"])
            check_type(argname="argument certificate_chain", value=certificate_chain, expected_type=type_hints["certificate_chain"])
            check_type(argname="argument certificate_name", value=certificate_name, expected_type=type_hints["certificate_name"])
            check_type(argname="argument certificate_private_key", value=certificate_private_key, expected_type=type_hints["certificate_private_key"])
            check_type(argname="argument endpoint_configuration", value=endpoint_configuration, expected_type=type_hints["endpoint_configuration"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument mutual_tls_authentication", value=mutual_tls_authentication, expected_type=type_hints["mutual_tls_authentication"])
            check_type(argname="argument ownership_verification_certificate_arn", value=ownership_verification_certificate_arn, expected_type=type_hints["ownership_verification_certificate_arn"])
            check_type(argname="argument regional_certificate_arn", value=regional_certificate_arn, expected_type=type_hints["regional_certificate_arn"])
            check_type(argname="argument regional_certificate_name", value=regional_certificate_name, expected_type=type_hints["regional_certificate_name"])
            check_type(argname="argument security_policy", value=security_policy, expected_type=type_hints["security_policy"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_name": domain_name,
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
        if certificate_arn is not None:
            self._values["certificate_arn"] = certificate_arn
        if certificate_body is not None:
            self._values["certificate_body"] = certificate_body
        if certificate_chain is not None:
            self._values["certificate_chain"] = certificate_chain
        if certificate_name is not None:
            self._values["certificate_name"] = certificate_name
        if certificate_private_key is not None:
            self._values["certificate_private_key"] = certificate_private_key
        if endpoint_configuration is not None:
            self._values["endpoint_configuration"] = endpoint_configuration
        if id is not None:
            self._values["id"] = id
        if mutual_tls_authentication is not None:
            self._values["mutual_tls_authentication"] = mutual_tls_authentication
        if ownership_verification_certificate_arn is not None:
            self._values["ownership_verification_certificate_arn"] = ownership_verification_certificate_arn
        if regional_certificate_arn is not None:
            self._values["regional_certificate_arn"] = regional_certificate_arn
        if regional_certificate_name is not None:
            self._values["regional_certificate_name"] = regional_certificate_name
        if security_policy is not None:
            self._values["security_policy"] = security_policy
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
    def domain_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#domain_name ApiGatewayDomainName#domain_name}.'''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#certificate_arn ApiGatewayDomainName#certificate_arn}.'''
        result = self._values.get("certificate_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate_body(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#certificate_body ApiGatewayDomainName#certificate_body}.'''
        result = self._values.get("certificate_body")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate_chain(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#certificate_chain ApiGatewayDomainName#certificate_chain}.'''
        result = self._values.get("certificate_chain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#certificate_name ApiGatewayDomainName#certificate_name}.'''
        result = self._values.get("certificate_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate_private_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#certificate_private_key ApiGatewayDomainName#certificate_private_key}.'''
        result = self._values.get("certificate_private_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def endpoint_configuration(
        self,
    ) -> typing.Optional["ApiGatewayDomainNameEndpointConfiguration"]:
        '''endpoint_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#endpoint_configuration ApiGatewayDomainName#endpoint_configuration}
        '''
        result = self._values.get("endpoint_configuration")
        return typing.cast(typing.Optional["ApiGatewayDomainNameEndpointConfiguration"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#id ApiGatewayDomainName#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mutual_tls_authentication(
        self,
    ) -> typing.Optional["ApiGatewayDomainNameMutualTlsAuthentication"]:
        '''mutual_tls_authentication block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#mutual_tls_authentication ApiGatewayDomainName#mutual_tls_authentication}
        '''
        result = self._values.get("mutual_tls_authentication")
        return typing.cast(typing.Optional["ApiGatewayDomainNameMutualTlsAuthentication"], result)

    @builtins.property
    def ownership_verification_certificate_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#ownership_verification_certificate_arn ApiGatewayDomainName#ownership_verification_certificate_arn}.'''
        result = self._values.get("ownership_verification_certificate_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def regional_certificate_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#regional_certificate_arn ApiGatewayDomainName#regional_certificate_arn}.'''
        result = self._values.get("regional_certificate_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def regional_certificate_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#regional_certificate_name ApiGatewayDomainName#regional_certificate_name}.'''
        result = self._values.get("regional_certificate_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#security_policy ApiGatewayDomainName#security_policy}.'''
        result = self._values.get("security_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#tags ApiGatewayDomainName#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#tags_all ApiGatewayDomainName#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiGatewayDomainNameConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.apiGatewayDomainName.ApiGatewayDomainNameEndpointConfiguration",
    jsii_struct_bases=[],
    name_mapping={"types": "types"},
)
class ApiGatewayDomainNameEndpointConfiguration:
    def __init__(self, *, types: typing.Sequence[builtins.str]) -> None:
        '''
        :param types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#types ApiGatewayDomainName#types}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76d590513e8c032b7dca76ed90555a3332f10bb0539b7deff5add60159977991)
            check_type(argname="argument types", value=types, expected_type=type_hints["types"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "types": types,
        }

    @builtins.property
    def types(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#types ApiGatewayDomainName#types}.'''
        result = self._values.get("types")
        assert result is not None, "Required property 'types' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiGatewayDomainNameEndpointConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiGatewayDomainNameEndpointConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.apiGatewayDomainName.ApiGatewayDomainNameEndpointConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8653be68eb3ee1f81516794ac60fa5c876c75deb9240f8ff946ce09dda434a1f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="typesInput")
    def types_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "typesInput"))

    @builtins.property
    @jsii.member(jsii_name="types")
    def types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "types"))

    @types.setter
    def types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6091c1fba090131699227939e088fe17426a394d59654a2ba4ee21d07495f121)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "types", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ApiGatewayDomainNameEndpointConfiguration]:
        return typing.cast(typing.Optional[ApiGatewayDomainNameEndpointConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApiGatewayDomainNameEndpointConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d725e07d2eaf697fb7c038a1e509e4fd293900fc2c85ea2b8cb995eeaf8409a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.apiGatewayDomainName.ApiGatewayDomainNameMutualTlsAuthentication",
    jsii_struct_bases=[],
    name_mapping={
        "truststore_uri": "truststoreUri",
        "truststore_version": "truststoreVersion",
    },
)
class ApiGatewayDomainNameMutualTlsAuthentication:
    def __init__(
        self,
        *,
        truststore_uri: builtins.str,
        truststore_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param truststore_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#truststore_uri ApiGatewayDomainName#truststore_uri}.
        :param truststore_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#truststore_version ApiGatewayDomainName#truststore_version}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a332cc251d68ab99033055210883dfcf3eaa15ad71472c4a528e0b98c649c36)
            check_type(argname="argument truststore_uri", value=truststore_uri, expected_type=type_hints["truststore_uri"])
            check_type(argname="argument truststore_version", value=truststore_version, expected_type=type_hints["truststore_version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "truststore_uri": truststore_uri,
        }
        if truststore_version is not None:
            self._values["truststore_version"] = truststore_version

    @builtins.property
    def truststore_uri(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#truststore_uri ApiGatewayDomainName#truststore_uri}.'''
        result = self._values.get("truststore_uri")
        assert result is not None, "Required property 'truststore_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def truststore_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#truststore_version ApiGatewayDomainName#truststore_version}.'''
        result = self._values.get("truststore_version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiGatewayDomainNameMutualTlsAuthentication(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiGatewayDomainNameMutualTlsAuthenticationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.apiGatewayDomainName.ApiGatewayDomainNameMutualTlsAuthenticationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c673a43582281f6acedf72c39bdc538a582cb64a26d8ef3edf7f84ba32b4df89)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetTruststoreVersion")
    def reset_truststore_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTruststoreVersion", []))

    @builtins.property
    @jsii.member(jsii_name="truststoreUriInput")
    def truststore_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "truststoreUriInput"))

    @builtins.property
    @jsii.member(jsii_name="truststoreVersionInput")
    def truststore_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "truststoreVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="truststoreUri")
    def truststore_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "truststoreUri"))

    @truststore_uri.setter
    def truststore_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0bdc3aa231eb8bb4fe3331215d462c68515a2960d8525837caa0cd46181c075)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "truststoreUri", value)

    @builtins.property
    @jsii.member(jsii_name="truststoreVersion")
    def truststore_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "truststoreVersion"))

    @truststore_version.setter
    def truststore_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__241ba9ae244a2fcd7390e995ef90c44e37d82d1e7b4ebf619a796438eaa0c5e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "truststoreVersion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ApiGatewayDomainNameMutualTlsAuthentication]:
        return typing.cast(typing.Optional[ApiGatewayDomainNameMutualTlsAuthentication], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApiGatewayDomainNameMutualTlsAuthentication],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8e763326df784eb9661cbdd7be11bc500126407cea1981f731ec2963f0a4a3c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ApiGatewayDomainName",
    "ApiGatewayDomainNameConfig",
    "ApiGatewayDomainNameEndpointConfiguration",
    "ApiGatewayDomainNameEndpointConfigurationOutputReference",
    "ApiGatewayDomainNameMutualTlsAuthentication",
    "ApiGatewayDomainNameMutualTlsAuthenticationOutputReference",
]

publication.publish()

def _typecheckingstub__503bf2fe914cf384a912f45c9f1fb809f9d3a2d682cb1529ccd322b2f97f724f(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    domain_name: builtins.str,
    certificate_arn: typing.Optional[builtins.str] = None,
    certificate_body: typing.Optional[builtins.str] = None,
    certificate_chain: typing.Optional[builtins.str] = None,
    certificate_name: typing.Optional[builtins.str] = None,
    certificate_private_key: typing.Optional[builtins.str] = None,
    endpoint_configuration: typing.Optional[typing.Union[ApiGatewayDomainNameEndpointConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    mutual_tls_authentication: typing.Optional[typing.Union[ApiGatewayDomainNameMutualTlsAuthentication, typing.Dict[builtins.str, typing.Any]]] = None,
    ownership_verification_certificate_arn: typing.Optional[builtins.str] = None,
    regional_certificate_arn: typing.Optional[builtins.str] = None,
    regional_certificate_name: typing.Optional[builtins.str] = None,
    security_policy: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__04529f21594923d4682bf3360bf3a0cb2b927a74bfc2b4d7afde1cf6b06c7d7c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c309742f710f221ffb0bcd2b858f0ed0a523b0099d55bc7877875ff2a8c5c0ef(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d67ffb3cd702596e9bdd8bb9314c78a1748a38478dcb7a3ccd0cd71cdf5f3d7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51fd76cbfa2ab82a81f65616a793367fd453f087d9a3e41af1f07a9611e20356(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5b484be5c9f1db48463c6a78a58207b4073c99a54750405947ebcd90be58c96(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee5bcfd0e2ca3c5d93463763472c3aa0222ca1abe63d828eadcdadf50771bf88(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e494b270ea92e91e9a7e5d7e0f53b94337cec501f00f6435596a3c2fc3ae6741(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f161363c2c397088d701a5b218eaa37195499e184f35e3d9a042ec93880649aa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2823479db1d15b2ca1e6274fcc037f1fb2e2d0b43ae342d4a8a6363277d71594(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8c66a092d1922eb0ca28044e1cfc7d35016db0d719719003d31ab0abaf7d565(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cd0882e253f64cd907b09f32f575da1b8f7978194113b0f3113a41e856f17ce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__679e8a2941852289d5674b73666fae01e2e0fc2346dc231cb1eba3b8ed16655a(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99417cda75adccbd5e93640e40ba4a9965e9099970e84733c2bea657a1b1e3ed(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d37ecfb9b4af98aec1c7432b4393240fb89f411d637ced5411c985617a599a9d(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    domain_name: builtins.str,
    certificate_arn: typing.Optional[builtins.str] = None,
    certificate_body: typing.Optional[builtins.str] = None,
    certificate_chain: typing.Optional[builtins.str] = None,
    certificate_name: typing.Optional[builtins.str] = None,
    certificate_private_key: typing.Optional[builtins.str] = None,
    endpoint_configuration: typing.Optional[typing.Union[ApiGatewayDomainNameEndpointConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    mutual_tls_authentication: typing.Optional[typing.Union[ApiGatewayDomainNameMutualTlsAuthentication, typing.Dict[builtins.str, typing.Any]]] = None,
    ownership_verification_certificate_arn: typing.Optional[builtins.str] = None,
    regional_certificate_arn: typing.Optional[builtins.str] = None,
    regional_certificate_name: typing.Optional[builtins.str] = None,
    security_policy: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76d590513e8c032b7dca76ed90555a3332f10bb0539b7deff5add60159977991(
    *,
    types: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8653be68eb3ee1f81516794ac60fa5c876c75deb9240f8ff946ce09dda434a1f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6091c1fba090131699227939e088fe17426a394d59654a2ba4ee21d07495f121(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d725e07d2eaf697fb7c038a1e509e4fd293900fc2c85ea2b8cb995eeaf8409a(
    value: typing.Optional[ApiGatewayDomainNameEndpointConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a332cc251d68ab99033055210883dfcf3eaa15ad71472c4a528e0b98c649c36(
    *,
    truststore_uri: builtins.str,
    truststore_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c673a43582281f6acedf72c39bdc538a582cb64a26d8ef3edf7f84ba32b4df89(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0bdc3aa231eb8bb4fe3331215d462c68515a2960d8525837caa0cd46181c075(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__241ba9ae244a2fcd7390e995ef90c44e37d82d1e7b4ebf619a796438eaa0c5e0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8e763326df784eb9661cbdd7be11bc500126407cea1981f731ec2963f0a4a3c(
    value: typing.Optional[ApiGatewayDomainNameMutualTlsAuthentication],
) -> None:
    """Type checking stubs"""
    pass
