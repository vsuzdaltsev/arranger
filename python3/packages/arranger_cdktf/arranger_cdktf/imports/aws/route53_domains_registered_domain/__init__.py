'''
# `aws_route53domains_registered_domain`

Refer to the Terraform Registory for docs: [`aws_route53domains_registered_domain`](https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain).
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


class Route53DomainsRegisteredDomain(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.route53DomainsRegisteredDomain.Route53DomainsRegisteredDomain",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain aws_route53domains_registered_domain}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        domain_name: builtins.str,
        admin_contact: typing.Optional[typing.Union["Route53DomainsRegisteredDomainAdminContact", typing.Dict[builtins.str, typing.Any]]] = None,
        admin_privacy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        auto_renew: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        name_server: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["Route53DomainsRegisteredDomainNameServer", typing.Dict[builtins.str, typing.Any]]]]] = None,
        registrant_contact: typing.Optional[typing.Union["Route53DomainsRegisteredDomainRegistrantContact", typing.Dict[builtins.str, typing.Any]]] = None,
        registrant_privacy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tech_contact: typing.Optional[typing.Union["Route53DomainsRegisteredDomainTechContact", typing.Dict[builtins.str, typing.Any]]] = None,
        tech_privacy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        timeouts: typing.Optional[typing.Union["Route53DomainsRegisteredDomainTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        transfer_lock: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain aws_route53domains_registered_domain} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#domain_name Route53DomainsRegisteredDomain#domain_name}.
        :param admin_contact: admin_contact block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#admin_contact Route53DomainsRegisteredDomain#admin_contact}
        :param admin_privacy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#admin_privacy Route53DomainsRegisteredDomain#admin_privacy}.
        :param auto_renew: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#auto_renew Route53DomainsRegisteredDomain#auto_renew}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#id Route53DomainsRegisteredDomain#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name_server: name_server block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#name_server Route53DomainsRegisteredDomain#name_server}
        :param registrant_contact: registrant_contact block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#registrant_contact Route53DomainsRegisteredDomain#registrant_contact}
        :param registrant_privacy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#registrant_privacy Route53DomainsRegisteredDomain#registrant_privacy}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#tags Route53DomainsRegisteredDomain#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#tags_all Route53DomainsRegisteredDomain#tags_all}.
        :param tech_contact: tech_contact block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#tech_contact Route53DomainsRegisteredDomain#tech_contact}
        :param tech_privacy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#tech_privacy Route53DomainsRegisteredDomain#tech_privacy}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#timeouts Route53DomainsRegisteredDomain#timeouts}
        :param transfer_lock: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#transfer_lock Route53DomainsRegisteredDomain#transfer_lock}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebacca01986aaab2b11a8cf39a2cd7c3893af7c7cbd224ddacc231d6415e5a07)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = Route53DomainsRegisteredDomainConfig(
            domain_name=domain_name,
            admin_contact=admin_contact,
            admin_privacy=admin_privacy,
            auto_renew=auto_renew,
            id=id,
            name_server=name_server,
            registrant_contact=registrant_contact,
            registrant_privacy=registrant_privacy,
            tags=tags,
            tags_all=tags_all,
            tech_contact=tech_contact,
            tech_privacy=tech_privacy,
            timeouts=timeouts,
            transfer_lock=transfer_lock,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAdminContact")
    def put_admin_contact(
        self,
        *,
        address_line1: typing.Optional[builtins.str] = None,
        address_line2: typing.Optional[builtins.str] = None,
        city: typing.Optional[builtins.str] = None,
        contact_type: typing.Optional[builtins.str] = None,
        country_code: typing.Optional[builtins.str] = None,
        email: typing.Optional[builtins.str] = None,
        extra_params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        fax: typing.Optional[builtins.str] = None,
        first_name: typing.Optional[builtins.str] = None,
        last_name: typing.Optional[builtins.str] = None,
        organization_name: typing.Optional[builtins.str] = None,
        phone_number: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
        zip_code: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param address_line1: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#address_line_1 Route53DomainsRegisteredDomain#address_line_1}.
        :param address_line2: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#address_line_2 Route53DomainsRegisteredDomain#address_line_2}.
        :param city: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#city Route53DomainsRegisteredDomain#city}.
        :param contact_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#contact_type Route53DomainsRegisteredDomain#contact_type}.
        :param country_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#country_code Route53DomainsRegisteredDomain#country_code}.
        :param email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#email Route53DomainsRegisteredDomain#email}.
        :param extra_params: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#extra_params Route53DomainsRegisteredDomain#extra_params}.
        :param fax: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#fax Route53DomainsRegisteredDomain#fax}.
        :param first_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#first_name Route53DomainsRegisteredDomain#first_name}.
        :param last_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#last_name Route53DomainsRegisteredDomain#last_name}.
        :param organization_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#organization_name Route53DomainsRegisteredDomain#organization_name}.
        :param phone_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#phone_number Route53DomainsRegisteredDomain#phone_number}.
        :param state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#state Route53DomainsRegisteredDomain#state}.
        :param zip_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#zip_code Route53DomainsRegisteredDomain#zip_code}.
        '''
        value = Route53DomainsRegisteredDomainAdminContact(
            address_line1=address_line1,
            address_line2=address_line2,
            city=city,
            contact_type=contact_type,
            country_code=country_code,
            email=email,
            extra_params=extra_params,
            fax=fax,
            first_name=first_name,
            last_name=last_name,
            organization_name=organization_name,
            phone_number=phone_number,
            state=state,
            zip_code=zip_code,
        )

        return typing.cast(None, jsii.invoke(self, "putAdminContact", [value]))

    @jsii.member(jsii_name="putNameServer")
    def put_name_server(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["Route53DomainsRegisteredDomainNameServer", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9705c5d8180be58e73df7c21bba296138d54100bd4572c8309d61b52cc9efc45)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNameServer", [value]))

    @jsii.member(jsii_name="putRegistrantContact")
    def put_registrant_contact(
        self,
        *,
        address_line1: typing.Optional[builtins.str] = None,
        address_line2: typing.Optional[builtins.str] = None,
        city: typing.Optional[builtins.str] = None,
        contact_type: typing.Optional[builtins.str] = None,
        country_code: typing.Optional[builtins.str] = None,
        email: typing.Optional[builtins.str] = None,
        extra_params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        fax: typing.Optional[builtins.str] = None,
        first_name: typing.Optional[builtins.str] = None,
        last_name: typing.Optional[builtins.str] = None,
        organization_name: typing.Optional[builtins.str] = None,
        phone_number: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
        zip_code: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param address_line1: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#address_line_1 Route53DomainsRegisteredDomain#address_line_1}.
        :param address_line2: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#address_line_2 Route53DomainsRegisteredDomain#address_line_2}.
        :param city: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#city Route53DomainsRegisteredDomain#city}.
        :param contact_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#contact_type Route53DomainsRegisteredDomain#contact_type}.
        :param country_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#country_code Route53DomainsRegisteredDomain#country_code}.
        :param email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#email Route53DomainsRegisteredDomain#email}.
        :param extra_params: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#extra_params Route53DomainsRegisteredDomain#extra_params}.
        :param fax: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#fax Route53DomainsRegisteredDomain#fax}.
        :param first_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#first_name Route53DomainsRegisteredDomain#first_name}.
        :param last_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#last_name Route53DomainsRegisteredDomain#last_name}.
        :param organization_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#organization_name Route53DomainsRegisteredDomain#organization_name}.
        :param phone_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#phone_number Route53DomainsRegisteredDomain#phone_number}.
        :param state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#state Route53DomainsRegisteredDomain#state}.
        :param zip_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#zip_code Route53DomainsRegisteredDomain#zip_code}.
        '''
        value = Route53DomainsRegisteredDomainRegistrantContact(
            address_line1=address_line1,
            address_line2=address_line2,
            city=city,
            contact_type=contact_type,
            country_code=country_code,
            email=email,
            extra_params=extra_params,
            fax=fax,
            first_name=first_name,
            last_name=last_name,
            organization_name=organization_name,
            phone_number=phone_number,
            state=state,
            zip_code=zip_code,
        )

        return typing.cast(None, jsii.invoke(self, "putRegistrantContact", [value]))

    @jsii.member(jsii_name="putTechContact")
    def put_tech_contact(
        self,
        *,
        address_line1: typing.Optional[builtins.str] = None,
        address_line2: typing.Optional[builtins.str] = None,
        city: typing.Optional[builtins.str] = None,
        contact_type: typing.Optional[builtins.str] = None,
        country_code: typing.Optional[builtins.str] = None,
        email: typing.Optional[builtins.str] = None,
        extra_params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        fax: typing.Optional[builtins.str] = None,
        first_name: typing.Optional[builtins.str] = None,
        last_name: typing.Optional[builtins.str] = None,
        organization_name: typing.Optional[builtins.str] = None,
        phone_number: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
        zip_code: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param address_line1: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#address_line_1 Route53DomainsRegisteredDomain#address_line_1}.
        :param address_line2: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#address_line_2 Route53DomainsRegisteredDomain#address_line_2}.
        :param city: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#city Route53DomainsRegisteredDomain#city}.
        :param contact_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#contact_type Route53DomainsRegisteredDomain#contact_type}.
        :param country_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#country_code Route53DomainsRegisteredDomain#country_code}.
        :param email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#email Route53DomainsRegisteredDomain#email}.
        :param extra_params: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#extra_params Route53DomainsRegisteredDomain#extra_params}.
        :param fax: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#fax Route53DomainsRegisteredDomain#fax}.
        :param first_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#first_name Route53DomainsRegisteredDomain#first_name}.
        :param last_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#last_name Route53DomainsRegisteredDomain#last_name}.
        :param organization_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#organization_name Route53DomainsRegisteredDomain#organization_name}.
        :param phone_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#phone_number Route53DomainsRegisteredDomain#phone_number}.
        :param state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#state Route53DomainsRegisteredDomain#state}.
        :param zip_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#zip_code Route53DomainsRegisteredDomain#zip_code}.
        '''
        value = Route53DomainsRegisteredDomainTechContact(
            address_line1=address_line1,
            address_line2=address_line2,
            city=city,
            contact_type=contact_type,
            country_code=country_code,
            email=email,
            extra_params=extra_params,
            fax=fax,
            first_name=first_name,
            last_name=last_name,
            organization_name=organization_name,
            phone_number=phone_number,
            state=state,
            zip_code=zip_code,
        )

        return typing.cast(None, jsii.invoke(self, "putTechContact", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#create Route53DomainsRegisteredDomain#create}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#update Route53DomainsRegisteredDomain#update}.
        '''
        value = Route53DomainsRegisteredDomainTimeouts(create=create, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAdminContact")
    def reset_admin_contact(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdminContact", []))

    @jsii.member(jsii_name="resetAdminPrivacy")
    def reset_admin_privacy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdminPrivacy", []))

    @jsii.member(jsii_name="resetAutoRenew")
    def reset_auto_renew(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoRenew", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetNameServer")
    def reset_name_server(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNameServer", []))

    @jsii.member(jsii_name="resetRegistrantContact")
    def reset_registrant_contact(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegistrantContact", []))

    @jsii.member(jsii_name="resetRegistrantPrivacy")
    def reset_registrant_privacy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegistrantPrivacy", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTechContact")
    def reset_tech_contact(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTechContact", []))

    @jsii.member(jsii_name="resetTechPrivacy")
    def reset_tech_privacy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTechPrivacy", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetTransferLock")
    def reset_transfer_lock(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransferLock", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="abuseContactEmail")
    def abuse_contact_email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "abuseContactEmail"))

    @builtins.property
    @jsii.member(jsii_name="abuseContactPhone")
    def abuse_contact_phone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "abuseContactPhone"))

    @builtins.property
    @jsii.member(jsii_name="adminContact")
    def admin_contact(
        self,
    ) -> "Route53DomainsRegisteredDomainAdminContactOutputReference":
        return typing.cast("Route53DomainsRegisteredDomainAdminContactOutputReference", jsii.get(self, "adminContact"))

    @builtins.property
    @jsii.member(jsii_name="creationDate")
    def creation_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "creationDate"))

    @builtins.property
    @jsii.member(jsii_name="expirationDate")
    def expiration_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expirationDate"))

    @builtins.property
    @jsii.member(jsii_name="nameServer")
    def name_server(self) -> "Route53DomainsRegisteredDomainNameServerList":
        return typing.cast("Route53DomainsRegisteredDomainNameServerList", jsii.get(self, "nameServer"))

    @builtins.property
    @jsii.member(jsii_name="registrantContact")
    def registrant_contact(
        self,
    ) -> "Route53DomainsRegisteredDomainRegistrantContactOutputReference":
        return typing.cast("Route53DomainsRegisteredDomainRegistrantContactOutputReference", jsii.get(self, "registrantContact"))

    @builtins.property
    @jsii.member(jsii_name="registrarName")
    def registrar_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "registrarName"))

    @builtins.property
    @jsii.member(jsii_name="registrarUrl")
    def registrar_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "registrarUrl"))

    @builtins.property
    @jsii.member(jsii_name="reseller")
    def reseller(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "reseller"))

    @builtins.property
    @jsii.member(jsii_name="statusList")
    def status_list(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "statusList"))

    @builtins.property
    @jsii.member(jsii_name="techContact")
    def tech_contact(
        self,
    ) -> "Route53DomainsRegisteredDomainTechContactOutputReference":
        return typing.cast("Route53DomainsRegisteredDomainTechContactOutputReference", jsii.get(self, "techContact"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "Route53DomainsRegisteredDomainTimeoutsOutputReference":
        return typing.cast("Route53DomainsRegisteredDomainTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="updatedDate")
    def updated_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "updatedDate"))

    @builtins.property
    @jsii.member(jsii_name="whoisServer")
    def whois_server(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "whoisServer"))

    @builtins.property
    @jsii.member(jsii_name="adminContactInput")
    def admin_contact_input(
        self,
    ) -> typing.Optional["Route53DomainsRegisteredDomainAdminContact"]:
        return typing.cast(typing.Optional["Route53DomainsRegisteredDomainAdminContact"], jsii.get(self, "adminContactInput"))

    @builtins.property
    @jsii.member(jsii_name="adminPrivacyInput")
    def admin_privacy_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "adminPrivacyInput"))

    @builtins.property
    @jsii.member(jsii_name="autoRenewInput")
    def auto_renew_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "autoRenewInput"))

    @builtins.property
    @jsii.member(jsii_name="domainNameInput")
    def domain_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameServerInput")
    def name_server_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Route53DomainsRegisteredDomainNameServer"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Route53DomainsRegisteredDomainNameServer"]]], jsii.get(self, "nameServerInput"))

    @builtins.property
    @jsii.member(jsii_name="registrantContactInput")
    def registrant_contact_input(
        self,
    ) -> typing.Optional["Route53DomainsRegisteredDomainRegistrantContact"]:
        return typing.cast(typing.Optional["Route53DomainsRegisteredDomainRegistrantContact"], jsii.get(self, "registrantContactInput"))

    @builtins.property
    @jsii.member(jsii_name="registrantPrivacyInput")
    def registrant_privacy_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "registrantPrivacyInput"))

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
    @jsii.member(jsii_name="techContactInput")
    def tech_contact_input(
        self,
    ) -> typing.Optional["Route53DomainsRegisteredDomainTechContact"]:
        return typing.cast(typing.Optional["Route53DomainsRegisteredDomainTechContact"], jsii.get(self, "techContactInput"))

    @builtins.property
    @jsii.member(jsii_name="techPrivacyInput")
    def tech_privacy_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "techPrivacyInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["Route53DomainsRegisteredDomainTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["Route53DomainsRegisteredDomainTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="transferLockInput")
    def transfer_lock_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "transferLockInput"))

    @builtins.property
    @jsii.member(jsii_name="adminPrivacy")
    def admin_privacy(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "adminPrivacy"))

    @admin_privacy.setter
    def admin_privacy(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4883cc343d710843ceb34ca2ca670c6184c104a019f87bab9b6d8d84834c7ff8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminPrivacy", value)

    @builtins.property
    @jsii.member(jsii_name="autoRenew")
    def auto_renew(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "autoRenew"))

    @auto_renew.setter
    def auto_renew(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__072f095377b1832a4367d17e9d412d2173f601d99b48f90828d742104cf46b2a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoRenew", value)

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f616340bad8b18c5c19bcc53f7c49e947af87f2d3f39cc9cc30a6475af4fe3ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__029e36151f3be9de3f4cc23ef571db0686e149e7b14088232ca1cf523f08b85a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="registrantPrivacy")
    def registrant_privacy(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "registrantPrivacy"))

    @registrant_privacy.setter
    def registrant_privacy(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ada9eba9910eaeecd3cf902a6b948be9293615eabe084fe569f8a61fc0e46f95)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "registrantPrivacy", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c0c3f49ef2ab31fa6bd942084d1c8d97ffbd32afa6d2a166c2cb2634a900a1f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06547bedcd00f147ba500e513c2a25b23e6eb9d15b0344834b9a5f5b507d8793)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="techPrivacy")
    def tech_privacy(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "techPrivacy"))

    @tech_privacy.setter
    def tech_privacy(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73d4e2c48751797dd567688c2e27875737fbae02616c903f69b96b545e3a9a4d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "techPrivacy", value)

    @builtins.property
    @jsii.member(jsii_name="transferLock")
    def transfer_lock(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "transferLock"))

    @transfer_lock.setter
    def transfer_lock(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__182c77ce2c2e47091379715edfd8b5e75d4a205a9f0377fff7e85293afdb5558)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transferLock", value)


@jsii.data_type(
    jsii_type="aws.route53DomainsRegisteredDomain.Route53DomainsRegisteredDomainAdminContact",
    jsii_struct_bases=[],
    name_mapping={
        "address_line1": "addressLine1",
        "address_line2": "addressLine2",
        "city": "city",
        "contact_type": "contactType",
        "country_code": "countryCode",
        "email": "email",
        "extra_params": "extraParams",
        "fax": "fax",
        "first_name": "firstName",
        "last_name": "lastName",
        "organization_name": "organizationName",
        "phone_number": "phoneNumber",
        "state": "state",
        "zip_code": "zipCode",
    },
)
class Route53DomainsRegisteredDomainAdminContact:
    def __init__(
        self,
        *,
        address_line1: typing.Optional[builtins.str] = None,
        address_line2: typing.Optional[builtins.str] = None,
        city: typing.Optional[builtins.str] = None,
        contact_type: typing.Optional[builtins.str] = None,
        country_code: typing.Optional[builtins.str] = None,
        email: typing.Optional[builtins.str] = None,
        extra_params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        fax: typing.Optional[builtins.str] = None,
        first_name: typing.Optional[builtins.str] = None,
        last_name: typing.Optional[builtins.str] = None,
        organization_name: typing.Optional[builtins.str] = None,
        phone_number: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
        zip_code: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param address_line1: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#address_line_1 Route53DomainsRegisteredDomain#address_line_1}.
        :param address_line2: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#address_line_2 Route53DomainsRegisteredDomain#address_line_2}.
        :param city: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#city Route53DomainsRegisteredDomain#city}.
        :param contact_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#contact_type Route53DomainsRegisteredDomain#contact_type}.
        :param country_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#country_code Route53DomainsRegisteredDomain#country_code}.
        :param email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#email Route53DomainsRegisteredDomain#email}.
        :param extra_params: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#extra_params Route53DomainsRegisteredDomain#extra_params}.
        :param fax: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#fax Route53DomainsRegisteredDomain#fax}.
        :param first_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#first_name Route53DomainsRegisteredDomain#first_name}.
        :param last_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#last_name Route53DomainsRegisteredDomain#last_name}.
        :param organization_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#organization_name Route53DomainsRegisteredDomain#organization_name}.
        :param phone_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#phone_number Route53DomainsRegisteredDomain#phone_number}.
        :param state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#state Route53DomainsRegisteredDomain#state}.
        :param zip_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#zip_code Route53DomainsRegisteredDomain#zip_code}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a087d955d3695b3d55ea15197650fa8867722a0adc556d43cec425a71217e61c)
            check_type(argname="argument address_line1", value=address_line1, expected_type=type_hints["address_line1"])
            check_type(argname="argument address_line2", value=address_line2, expected_type=type_hints["address_line2"])
            check_type(argname="argument city", value=city, expected_type=type_hints["city"])
            check_type(argname="argument contact_type", value=contact_type, expected_type=type_hints["contact_type"])
            check_type(argname="argument country_code", value=country_code, expected_type=type_hints["country_code"])
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument extra_params", value=extra_params, expected_type=type_hints["extra_params"])
            check_type(argname="argument fax", value=fax, expected_type=type_hints["fax"])
            check_type(argname="argument first_name", value=first_name, expected_type=type_hints["first_name"])
            check_type(argname="argument last_name", value=last_name, expected_type=type_hints["last_name"])
            check_type(argname="argument organization_name", value=organization_name, expected_type=type_hints["organization_name"])
            check_type(argname="argument phone_number", value=phone_number, expected_type=type_hints["phone_number"])
            check_type(argname="argument state", value=state, expected_type=type_hints["state"])
            check_type(argname="argument zip_code", value=zip_code, expected_type=type_hints["zip_code"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if address_line1 is not None:
            self._values["address_line1"] = address_line1
        if address_line2 is not None:
            self._values["address_line2"] = address_line2
        if city is not None:
            self._values["city"] = city
        if contact_type is not None:
            self._values["contact_type"] = contact_type
        if country_code is not None:
            self._values["country_code"] = country_code
        if email is not None:
            self._values["email"] = email
        if extra_params is not None:
            self._values["extra_params"] = extra_params
        if fax is not None:
            self._values["fax"] = fax
        if first_name is not None:
            self._values["first_name"] = first_name
        if last_name is not None:
            self._values["last_name"] = last_name
        if organization_name is not None:
            self._values["organization_name"] = organization_name
        if phone_number is not None:
            self._values["phone_number"] = phone_number
        if state is not None:
            self._values["state"] = state
        if zip_code is not None:
            self._values["zip_code"] = zip_code

    @builtins.property
    def address_line1(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#address_line_1 Route53DomainsRegisteredDomain#address_line_1}.'''
        result = self._values.get("address_line1")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def address_line2(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#address_line_2 Route53DomainsRegisteredDomain#address_line_2}.'''
        result = self._values.get("address_line2")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def city(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#city Route53DomainsRegisteredDomain#city}.'''
        result = self._values.get("city")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def contact_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#contact_type Route53DomainsRegisteredDomain#contact_type}.'''
        result = self._values.get("contact_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def country_code(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#country_code Route53DomainsRegisteredDomain#country_code}.'''
        result = self._values.get("country_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def email(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#email Route53DomainsRegisteredDomain#email}.'''
        result = self._values.get("email")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def extra_params(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#extra_params Route53DomainsRegisteredDomain#extra_params}.'''
        result = self._values.get("extra_params")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def fax(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#fax Route53DomainsRegisteredDomain#fax}.'''
        result = self._values.get("fax")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def first_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#first_name Route53DomainsRegisteredDomain#first_name}.'''
        result = self._values.get("first_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def last_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#last_name Route53DomainsRegisteredDomain#last_name}.'''
        result = self._values.get("last_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def organization_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#organization_name Route53DomainsRegisteredDomain#organization_name}.'''
        result = self._values.get("organization_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def phone_number(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#phone_number Route53DomainsRegisteredDomain#phone_number}.'''
        result = self._values.get("phone_number")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def state(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#state Route53DomainsRegisteredDomain#state}.'''
        result = self._values.get("state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def zip_code(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#zip_code Route53DomainsRegisteredDomain#zip_code}.'''
        result = self._values.get("zip_code")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Route53DomainsRegisteredDomainAdminContact(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Route53DomainsRegisteredDomainAdminContactOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.route53DomainsRegisteredDomain.Route53DomainsRegisteredDomainAdminContactOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7ef7d83549553902714caeee04403167749fca6547fadb78395b8bc892db3d50)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAddressLine1")
    def reset_address_line1(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAddressLine1", []))

    @jsii.member(jsii_name="resetAddressLine2")
    def reset_address_line2(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAddressLine2", []))

    @jsii.member(jsii_name="resetCity")
    def reset_city(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCity", []))

    @jsii.member(jsii_name="resetContactType")
    def reset_contact_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContactType", []))

    @jsii.member(jsii_name="resetCountryCode")
    def reset_country_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCountryCode", []))

    @jsii.member(jsii_name="resetEmail")
    def reset_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmail", []))

    @jsii.member(jsii_name="resetExtraParams")
    def reset_extra_params(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExtraParams", []))

    @jsii.member(jsii_name="resetFax")
    def reset_fax(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFax", []))

    @jsii.member(jsii_name="resetFirstName")
    def reset_first_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFirstName", []))

    @jsii.member(jsii_name="resetLastName")
    def reset_last_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLastName", []))

    @jsii.member(jsii_name="resetOrganizationName")
    def reset_organization_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrganizationName", []))

    @jsii.member(jsii_name="resetPhoneNumber")
    def reset_phone_number(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPhoneNumber", []))

    @jsii.member(jsii_name="resetState")
    def reset_state(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetState", []))

    @jsii.member(jsii_name="resetZipCode")
    def reset_zip_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZipCode", []))

    @builtins.property
    @jsii.member(jsii_name="addressLine1Input")
    def address_line1_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "addressLine1Input"))

    @builtins.property
    @jsii.member(jsii_name="addressLine2Input")
    def address_line2_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "addressLine2Input"))

    @builtins.property
    @jsii.member(jsii_name="cityInput")
    def city_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cityInput"))

    @builtins.property
    @jsii.member(jsii_name="contactTypeInput")
    def contact_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contactTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="countryCodeInput")
    def country_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "countryCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="emailInput")
    def email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailInput"))

    @builtins.property
    @jsii.member(jsii_name="extraParamsInput")
    def extra_params_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "extraParamsInput"))

    @builtins.property
    @jsii.member(jsii_name="faxInput")
    def fax_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "faxInput"))

    @builtins.property
    @jsii.member(jsii_name="firstNameInput")
    def first_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "firstNameInput"))

    @builtins.property
    @jsii.member(jsii_name="lastNameInput")
    def last_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lastNameInput"))

    @builtins.property
    @jsii.member(jsii_name="organizationNameInput")
    def organization_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "organizationNameInput"))

    @builtins.property
    @jsii.member(jsii_name="phoneNumberInput")
    def phone_number_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "phoneNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="stateInput")
    def state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stateInput"))

    @builtins.property
    @jsii.member(jsii_name="zipCodeInput")
    def zip_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zipCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="addressLine1")
    def address_line1(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "addressLine1"))

    @address_line1.setter
    def address_line1(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a092abf482adc1b6f575ccc60285ba242ed6e00b3c0731a9d3d33b755881c5ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "addressLine1", value)

    @builtins.property
    @jsii.member(jsii_name="addressLine2")
    def address_line2(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "addressLine2"))

    @address_line2.setter
    def address_line2(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f63188c925a7685e843f2f01d3120d1e5bed295a1949b90071ddb74f818df9e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "addressLine2", value)

    @builtins.property
    @jsii.member(jsii_name="city")
    def city(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "city"))

    @city.setter
    def city(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a52f954b473fd3592b5ded705d83a975f7f65e63f54bbd3239b74bc8fbfe1f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "city", value)

    @builtins.property
    @jsii.member(jsii_name="contactType")
    def contact_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contactType"))

    @contact_type.setter
    def contact_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7311eddaffb091f8d4149d768b82999902e82d790c48566081f34a38f367787d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contactType", value)

    @builtins.property
    @jsii.member(jsii_name="countryCode")
    def country_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "countryCode"))

    @country_code.setter
    def country_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45e06ef816d10c5cc1a3aa31d8b597a15ee18a818900ef3730de848bc7171b2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "countryCode", value)

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "email"))

    @email.setter
    def email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d58e3140a6ece4bb2538f79304df966e088e478ec8e0c5d6d24de9177adef6b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)

    @builtins.property
    @jsii.member(jsii_name="extraParams")
    def extra_params(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "extraParams"))

    @extra_params.setter
    def extra_params(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__371f00f0c043a26f5d858ebaf1b984ec9af1331753eb6dc2907c27897d6b7532)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "extraParams", value)

    @builtins.property
    @jsii.member(jsii_name="fax")
    def fax(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fax"))

    @fax.setter
    def fax(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b859b69a88eb75b16c1913d566a2010e52d04b1e04193a70fab1ade3bdd14fa0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fax", value)

    @builtins.property
    @jsii.member(jsii_name="firstName")
    def first_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "firstName"))

    @first_name.setter
    def first_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c55022a4787cac257525e96392efa9ce531218988d9844f0751393b81b54a63)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firstName", value)

    @builtins.property
    @jsii.member(jsii_name="lastName")
    def last_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastName"))

    @last_name.setter
    def last_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1725b40170fbaf7bb29c3a426f2343562312160fbfb781f9f83b1f5ef667519a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lastName", value)

    @builtins.property
    @jsii.member(jsii_name="organizationName")
    def organization_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "organizationName"))

    @organization_name.setter
    def organization_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02b760d8c4e9f43d5b5d7cf1b2f52708c314904e0c95161b03f82fdf0d517ff0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organizationName", value)

    @builtins.property
    @jsii.member(jsii_name="phoneNumber")
    def phone_number(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "phoneNumber"))

    @phone_number.setter
    def phone_number(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0cdf4e06e657539a462cd40189be87c27612edb99f2503c443391954ff57335)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "phoneNumber", value)

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @state.setter
    def state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ab8f44ca9f47b068baca1ba7804ea8bddcb96995164ea263563271f11e9ca56)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "state", value)

    @builtins.property
    @jsii.member(jsii_name="zipCode")
    def zip_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zipCode"))

    @zip_code.setter
    def zip_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba5a70f67d63e109e2b897cc4014817277e05d2576758c55e0c9d3946976ca54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zipCode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Route53DomainsRegisteredDomainAdminContact]:
        return typing.cast(typing.Optional[Route53DomainsRegisteredDomainAdminContact], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Route53DomainsRegisteredDomainAdminContact],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe17cfe35d1f7548b164dee35c22c44e3656976521aadc886321144516768622)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.route53DomainsRegisteredDomain.Route53DomainsRegisteredDomainConfig",
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
        "admin_contact": "adminContact",
        "admin_privacy": "adminPrivacy",
        "auto_renew": "autoRenew",
        "id": "id",
        "name_server": "nameServer",
        "registrant_contact": "registrantContact",
        "registrant_privacy": "registrantPrivacy",
        "tags": "tags",
        "tags_all": "tagsAll",
        "tech_contact": "techContact",
        "tech_privacy": "techPrivacy",
        "timeouts": "timeouts",
        "transfer_lock": "transferLock",
    },
)
class Route53DomainsRegisteredDomainConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        admin_contact: typing.Optional[typing.Union[Route53DomainsRegisteredDomainAdminContact, typing.Dict[builtins.str, typing.Any]]] = None,
        admin_privacy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        auto_renew: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        name_server: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["Route53DomainsRegisteredDomainNameServer", typing.Dict[builtins.str, typing.Any]]]]] = None,
        registrant_contact: typing.Optional[typing.Union["Route53DomainsRegisteredDomainRegistrantContact", typing.Dict[builtins.str, typing.Any]]] = None,
        registrant_privacy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tech_contact: typing.Optional[typing.Union["Route53DomainsRegisteredDomainTechContact", typing.Dict[builtins.str, typing.Any]]] = None,
        tech_privacy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        timeouts: typing.Optional[typing.Union["Route53DomainsRegisteredDomainTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        transfer_lock: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#domain_name Route53DomainsRegisteredDomain#domain_name}.
        :param admin_contact: admin_contact block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#admin_contact Route53DomainsRegisteredDomain#admin_contact}
        :param admin_privacy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#admin_privacy Route53DomainsRegisteredDomain#admin_privacy}.
        :param auto_renew: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#auto_renew Route53DomainsRegisteredDomain#auto_renew}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#id Route53DomainsRegisteredDomain#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name_server: name_server block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#name_server Route53DomainsRegisteredDomain#name_server}
        :param registrant_contact: registrant_contact block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#registrant_contact Route53DomainsRegisteredDomain#registrant_contact}
        :param registrant_privacy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#registrant_privacy Route53DomainsRegisteredDomain#registrant_privacy}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#tags Route53DomainsRegisteredDomain#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#tags_all Route53DomainsRegisteredDomain#tags_all}.
        :param tech_contact: tech_contact block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#tech_contact Route53DomainsRegisteredDomain#tech_contact}
        :param tech_privacy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#tech_privacy Route53DomainsRegisteredDomain#tech_privacy}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#timeouts Route53DomainsRegisteredDomain#timeouts}
        :param transfer_lock: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#transfer_lock Route53DomainsRegisteredDomain#transfer_lock}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(admin_contact, dict):
            admin_contact = Route53DomainsRegisteredDomainAdminContact(**admin_contact)
        if isinstance(registrant_contact, dict):
            registrant_contact = Route53DomainsRegisteredDomainRegistrantContact(**registrant_contact)
        if isinstance(tech_contact, dict):
            tech_contact = Route53DomainsRegisteredDomainTechContact(**tech_contact)
        if isinstance(timeouts, dict):
            timeouts = Route53DomainsRegisteredDomainTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83c2573e70b1de8f8c0f91d7a99494f272350f882cca5feeffd1a6542cb242e6)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument admin_contact", value=admin_contact, expected_type=type_hints["admin_contact"])
            check_type(argname="argument admin_privacy", value=admin_privacy, expected_type=type_hints["admin_privacy"])
            check_type(argname="argument auto_renew", value=auto_renew, expected_type=type_hints["auto_renew"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name_server", value=name_server, expected_type=type_hints["name_server"])
            check_type(argname="argument registrant_contact", value=registrant_contact, expected_type=type_hints["registrant_contact"])
            check_type(argname="argument registrant_privacy", value=registrant_privacy, expected_type=type_hints["registrant_privacy"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument tech_contact", value=tech_contact, expected_type=type_hints["tech_contact"])
            check_type(argname="argument tech_privacy", value=tech_privacy, expected_type=type_hints["tech_privacy"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument transfer_lock", value=transfer_lock, expected_type=type_hints["transfer_lock"])
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
        if admin_contact is not None:
            self._values["admin_contact"] = admin_contact
        if admin_privacy is not None:
            self._values["admin_privacy"] = admin_privacy
        if auto_renew is not None:
            self._values["auto_renew"] = auto_renew
        if id is not None:
            self._values["id"] = id
        if name_server is not None:
            self._values["name_server"] = name_server
        if registrant_contact is not None:
            self._values["registrant_contact"] = registrant_contact
        if registrant_privacy is not None:
            self._values["registrant_privacy"] = registrant_privacy
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if tech_contact is not None:
            self._values["tech_contact"] = tech_contact
        if tech_privacy is not None:
            self._values["tech_privacy"] = tech_privacy
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if transfer_lock is not None:
            self._values["transfer_lock"] = transfer_lock

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#domain_name Route53DomainsRegisteredDomain#domain_name}.'''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def admin_contact(
        self,
    ) -> typing.Optional[Route53DomainsRegisteredDomainAdminContact]:
        '''admin_contact block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#admin_contact Route53DomainsRegisteredDomain#admin_contact}
        '''
        result = self._values.get("admin_contact")
        return typing.cast(typing.Optional[Route53DomainsRegisteredDomainAdminContact], result)

    @builtins.property
    def admin_privacy(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#admin_privacy Route53DomainsRegisteredDomain#admin_privacy}.'''
        result = self._values.get("admin_privacy")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def auto_renew(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#auto_renew Route53DomainsRegisteredDomain#auto_renew}.'''
        result = self._values.get("auto_renew")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#id Route53DomainsRegisteredDomain#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name_server(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Route53DomainsRegisteredDomainNameServer"]]]:
        '''name_server block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#name_server Route53DomainsRegisteredDomain#name_server}
        '''
        result = self._values.get("name_server")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Route53DomainsRegisteredDomainNameServer"]]], result)

    @builtins.property
    def registrant_contact(
        self,
    ) -> typing.Optional["Route53DomainsRegisteredDomainRegistrantContact"]:
        '''registrant_contact block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#registrant_contact Route53DomainsRegisteredDomain#registrant_contact}
        '''
        result = self._values.get("registrant_contact")
        return typing.cast(typing.Optional["Route53DomainsRegisteredDomainRegistrantContact"], result)

    @builtins.property
    def registrant_privacy(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#registrant_privacy Route53DomainsRegisteredDomain#registrant_privacy}.'''
        result = self._values.get("registrant_privacy")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#tags Route53DomainsRegisteredDomain#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#tags_all Route53DomainsRegisteredDomain#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tech_contact(
        self,
    ) -> typing.Optional["Route53DomainsRegisteredDomainTechContact"]:
        '''tech_contact block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#tech_contact Route53DomainsRegisteredDomain#tech_contact}
        '''
        result = self._values.get("tech_contact")
        return typing.cast(typing.Optional["Route53DomainsRegisteredDomainTechContact"], result)

    @builtins.property
    def tech_privacy(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#tech_privacy Route53DomainsRegisteredDomain#tech_privacy}.'''
        result = self._values.get("tech_privacy")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["Route53DomainsRegisteredDomainTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#timeouts Route53DomainsRegisteredDomain#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["Route53DomainsRegisteredDomainTimeouts"], result)

    @builtins.property
    def transfer_lock(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#transfer_lock Route53DomainsRegisteredDomain#transfer_lock}.'''
        result = self._values.get("transfer_lock")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Route53DomainsRegisteredDomainConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.route53DomainsRegisteredDomain.Route53DomainsRegisteredDomainNameServer",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "glue_ips": "glueIps"},
)
class Route53DomainsRegisteredDomainNameServer:
    def __init__(
        self,
        *,
        name: builtins.str,
        glue_ips: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#name Route53DomainsRegisteredDomain#name}.
        :param glue_ips: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#glue_ips Route53DomainsRegisteredDomain#glue_ips}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1ba14b3e57fac5f0be5692d218d7ead510c3dbf9db637ea4f7c60fee8267c7f)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument glue_ips", value=glue_ips, expected_type=type_hints["glue_ips"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if glue_ips is not None:
            self._values["glue_ips"] = glue_ips

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#name Route53DomainsRegisteredDomain#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def glue_ips(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#glue_ips Route53DomainsRegisteredDomain#glue_ips}.'''
        result = self._values.get("glue_ips")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Route53DomainsRegisteredDomainNameServer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Route53DomainsRegisteredDomainNameServerList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.route53DomainsRegisteredDomain.Route53DomainsRegisteredDomainNameServerList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__80ddf97ade8458778c1000d753bab322b2032dff92526e44ae28d74e8f711cef)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Route53DomainsRegisteredDomainNameServerOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ad192e3a6b228d921b3af1cda9d7b4112eb4652b6f18682c88265c6b1d0168a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Route53DomainsRegisteredDomainNameServerOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17dcbebce9737135e20bbae7aa6d6d7e722d09429ae76e8a5dfba65e4eb3f0f4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d76a1f9522256041d15d57494af6379b40106ea65b7464f3e2773f5a0e1d7bc7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e429de63ca815de5761170518c39bc24902587b8474331cb365d808237fedd6e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Route53DomainsRegisteredDomainNameServer]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Route53DomainsRegisteredDomainNameServer]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Route53DomainsRegisteredDomainNameServer]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__347a849416f96228b471f944e6d20b4d14bb5685b2ce408d2db109c78c0c7298)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Route53DomainsRegisteredDomainNameServerOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.route53DomainsRegisteredDomain.Route53DomainsRegisteredDomainNameServerOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2a9df746c0b438d8f74d0d57078e6f86269a2d4e1ccbf8995e24ca1675aa20a6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetGlueIps")
    def reset_glue_ips(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGlueIps", []))

    @builtins.property
    @jsii.member(jsii_name="glueIpsInput")
    def glue_ips_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "glueIpsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="glueIps")
    def glue_ips(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "glueIps"))

    @glue_ips.setter
    def glue_ips(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a52457d7bd0bd77dd6503786d67687c41aa92b1e1b65182937469557bf86cef4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "glueIps", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac5ea35baad061094da4cd01988471f9b6000fa9ffe16cce94d4afd78454a38a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[Route53DomainsRegisteredDomainNameServer, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Route53DomainsRegisteredDomainNameServer, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Route53DomainsRegisteredDomainNameServer, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2daa791007739d3576424d86e7f686e295021fba773b156e9b5bb296960615c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.route53DomainsRegisteredDomain.Route53DomainsRegisteredDomainRegistrantContact",
    jsii_struct_bases=[],
    name_mapping={
        "address_line1": "addressLine1",
        "address_line2": "addressLine2",
        "city": "city",
        "contact_type": "contactType",
        "country_code": "countryCode",
        "email": "email",
        "extra_params": "extraParams",
        "fax": "fax",
        "first_name": "firstName",
        "last_name": "lastName",
        "organization_name": "organizationName",
        "phone_number": "phoneNumber",
        "state": "state",
        "zip_code": "zipCode",
    },
)
class Route53DomainsRegisteredDomainRegistrantContact:
    def __init__(
        self,
        *,
        address_line1: typing.Optional[builtins.str] = None,
        address_line2: typing.Optional[builtins.str] = None,
        city: typing.Optional[builtins.str] = None,
        contact_type: typing.Optional[builtins.str] = None,
        country_code: typing.Optional[builtins.str] = None,
        email: typing.Optional[builtins.str] = None,
        extra_params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        fax: typing.Optional[builtins.str] = None,
        first_name: typing.Optional[builtins.str] = None,
        last_name: typing.Optional[builtins.str] = None,
        organization_name: typing.Optional[builtins.str] = None,
        phone_number: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
        zip_code: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param address_line1: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#address_line_1 Route53DomainsRegisteredDomain#address_line_1}.
        :param address_line2: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#address_line_2 Route53DomainsRegisteredDomain#address_line_2}.
        :param city: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#city Route53DomainsRegisteredDomain#city}.
        :param contact_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#contact_type Route53DomainsRegisteredDomain#contact_type}.
        :param country_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#country_code Route53DomainsRegisteredDomain#country_code}.
        :param email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#email Route53DomainsRegisteredDomain#email}.
        :param extra_params: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#extra_params Route53DomainsRegisteredDomain#extra_params}.
        :param fax: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#fax Route53DomainsRegisteredDomain#fax}.
        :param first_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#first_name Route53DomainsRegisteredDomain#first_name}.
        :param last_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#last_name Route53DomainsRegisteredDomain#last_name}.
        :param organization_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#organization_name Route53DomainsRegisteredDomain#organization_name}.
        :param phone_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#phone_number Route53DomainsRegisteredDomain#phone_number}.
        :param state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#state Route53DomainsRegisteredDomain#state}.
        :param zip_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#zip_code Route53DomainsRegisteredDomain#zip_code}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b21b9a1f19197daa03dbc8eb6b9698fd78a109ee66a40a449a7dda0edb23fba)
            check_type(argname="argument address_line1", value=address_line1, expected_type=type_hints["address_line1"])
            check_type(argname="argument address_line2", value=address_line2, expected_type=type_hints["address_line2"])
            check_type(argname="argument city", value=city, expected_type=type_hints["city"])
            check_type(argname="argument contact_type", value=contact_type, expected_type=type_hints["contact_type"])
            check_type(argname="argument country_code", value=country_code, expected_type=type_hints["country_code"])
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument extra_params", value=extra_params, expected_type=type_hints["extra_params"])
            check_type(argname="argument fax", value=fax, expected_type=type_hints["fax"])
            check_type(argname="argument first_name", value=first_name, expected_type=type_hints["first_name"])
            check_type(argname="argument last_name", value=last_name, expected_type=type_hints["last_name"])
            check_type(argname="argument organization_name", value=organization_name, expected_type=type_hints["organization_name"])
            check_type(argname="argument phone_number", value=phone_number, expected_type=type_hints["phone_number"])
            check_type(argname="argument state", value=state, expected_type=type_hints["state"])
            check_type(argname="argument zip_code", value=zip_code, expected_type=type_hints["zip_code"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if address_line1 is not None:
            self._values["address_line1"] = address_line1
        if address_line2 is not None:
            self._values["address_line2"] = address_line2
        if city is not None:
            self._values["city"] = city
        if contact_type is not None:
            self._values["contact_type"] = contact_type
        if country_code is not None:
            self._values["country_code"] = country_code
        if email is not None:
            self._values["email"] = email
        if extra_params is not None:
            self._values["extra_params"] = extra_params
        if fax is not None:
            self._values["fax"] = fax
        if first_name is not None:
            self._values["first_name"] = first_name
        if last_name is not None:
            self._values["last_name"] = last_name
        if organization_name is not None:
            self._values["organization_name"] = organization_name
        if phone_number is not None:
            self._values["phone_number"] = phone_number
        if state is not None:
            self._values["state"] = state
        if zip_code is not None:
            self._values["zip_code"] = zip_code

    @builtins.property
    def address_line1(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#address_line_1 Route53DomainsRegisteredDomain#address_line_1}.'''
        result = self._values.get("address_line1")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def address_line2(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#address_line_2 Route53DomainsRegisteredDomain#address_line_2}.'''
        result = self._values.get("address_line2")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def city(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#city Route53DomainsRegisteredDomain#city}.'''
        result = self._values.get("city")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def contact_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#contact_type Route53DomainsRegisteredDomain#contact_type}.'''
        result = self._values.get("contact_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def country_code(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#country_code Route53DomainsRegisteredDomain#country_code}.'''
        result = self._values.get("country_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def email(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#email Route53DomainsRegisteredDomain#email}.'''
        result = self._values.get("email")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def extra_params(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#extra_params Route53DomainsRegisteredDomain#extra_params}.'''
        result = self._values.get("extra_params")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def fax(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#fax Route53DomainsRegisteredDomain#fax}.'''
        result = self._values.get("fax")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def first_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#first_name Route53DomainsRegisteredDomain#first_name}.'''
        result = self._values.get("first_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def last_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#last_name Route53DomainsRegisteredDomain#last_name}.'''
        result = self._values.get("last_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def organization_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#organization_name Route53DomainsRegisteredDomain#organization_name}.'''
        result = self._values.get("organization_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def phone_number(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#phone_number Route53DomainsRegisteredDomain#phone_number}.'''
        result = self._values.get("phone_number")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def state(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#state Route53DomainsRegisteredDomain#state}.'''
        result = self._values.get("state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def zip_code(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#zip_code Route53DomainsRegisteredDomain#zip_code}.'''
        result = self._values.get("zip_code")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Route53DomainsRegisteredDomainRegistrantContact(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Route53DomainsRegisteredDomainRegistrantContactOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.route53DomainsRegisteredDomain.Route53DomainsRegisteredDomainRegistrantContactOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ab403787f298ce851d79834f2acd655c939fabf8e8be1be64c4b33a8dbe28d20)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAddressLine1")
    def reset_address_line1(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAddressLine1", []))

    @jsii.member(jsii_name="resetAddressLine2")
    def reset_address_line2(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAddressLine2", []))

    @jsii.member(jsii_name="resetCity")
    def reset_city(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCity", []))

    @jsii.member(jsii_name="resetContactType")
    def reset_contact_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContactType", []))

    @jsii.member(jsii_name="resetCountryCode")
    def reset_country_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCountryCode", []))

    @jsii.member(jsii_name="resetEmail")
    def reset_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmail", []))

    @jsii.member(jsii_name="resetExtraParams")
    def reset_extra_params(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExtraParams", []))

    @jsii.member(jsii_name="resetFax")
    def reset_fax(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFax", []))

    @jsii.member(jsii_name="resetFirstName")
    def reset_first_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFirstName", []))

    @jsii.member(jsii_name="resetLastName")
    def reset_last_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLastName", []))

    @jsii.member(jsii_name="resetOrganizationName")
    def reset_organization_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrganizationName", []))

    @jsii.member(jsii_name="resetPhoneNumber")
    def reset_phone_number(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPhoneNumber", []))

    @jsii.member(jsii_name="resetState")
    def reset_state(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetState", []))

    @jsii.member(jsii_name="resetZipCode")
    def reset_zip_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZipCode", []))

    @builtins.property
    @jsii.member(jsii_name="addressLine1Input")
    def address_line1_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "addressLine1Input"))

    @builtins.property
    @jsii.member(jsii_name="addressLine2Input")
    def address_line2_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "addressLine2Input"))

    @builtins.property
    @jsii.member(jsii_name="cityInput")
    def city_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cityInput"))

    @builtins.property
    @jsii.member(jsii_name="contactTypeInput")
    def contact_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contactTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="countryCodeInput")
    def country_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "countryCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="emailInput")
    def email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailInput"))

    @builtins.property
    @jsii.member(jsii_name="extraParamsInput")
    def extra_params_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "extraParamsInput"))

    @builtins.property
    @jsii.member(jsii_name="faxInput")
    def fax_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "faxInput"))

    @builtins.property
    @jsii.member(jsii_name="firstNameInput")
    def first_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "firstNameInput"))

    @builtins.property
    @jsii.member(jsii_name="lastNameInput")
    def last_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lastNameInput"))

    @builtins.property
    @jsii.member(jsii_name="organizationNameInput")
    def organization_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "organizationNameInput"))

    @builtins.property
    @jsii.member(jsii_name="phoneNumberInput")
    def phone_number_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "phoneNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="stateInput")
    def state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stateInput"))

    @builtins.property
    @jsii.member(jsii_name="zipCodeInput")
    def zip_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zipCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="addressLine1")
    def address_line1(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "addressLine1"))

    @address_line1.setter
    def address_line1(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__196d8dc70a2c2db4d396a85c9ec20319fda6870483d5a8f119775b2b803febdf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "addressLine1", value)

    @builtins.property
    @jsii.member(jsii_name="addressLine2")
    def address_line2(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "addressLine2"))

    @address_line2.setter
    def address_line2(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb5f9b34d81f7967e71cd0256190b7523a4a2f8b4fa8a2cd597aadc7f62e130d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "addressLine2", value)

    @builtins.property
    @jsii.member(jsii_name="city")
    def city(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "city"))

    @city.setter
    def city(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7c9335c98718130c95796cc6aee255bdb315bb5c76c951a038d4a929c366be4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "city", value)

    @builtins.property
    @jsii.member(jsii_name="contactType")
    def contact_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contactType"))

    @contact_type.setter
    def contact_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45893ce66250ebce457313cd207f87b7875160d0526afd3612ddcb3849a93112)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contactType", value)

    @builtins.property
    @jsii.member(jsii_name="countryCode")
    def country_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "countryCode"))

    @country_code.setter
    def country_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4e0d148199a009b4677db944528f31ad78d02e90a93b0965bdfcca5224ea5e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "countryCode", value)

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "email"))

    @email.setter
    def email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2533630d312eb0d461213e4f393e4e15f38547344b2554ef71f63674932c0716)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)

    @builtins.property
    @jsii.member(jsii_name="extraParams")
    def extra_params(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "extraParams"))

    @extra_params.setter
    def extra_params(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__055ab668042ebf8b118a75b3776cf8462237b19b1e87a0033e0622e9fc768e25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "extraParams", value)

    @builtins.property
    @jsii.member(jsii_name="fax")
    def fax(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fax"))

    @fax.setter
    def fax(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c5c7d3d922ae8f98a21a0e8b6c4c27a72cfea2e38834dc4a216c58d15518718)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fax", value)

    @builtins.property
    @jsii.member(jsii_name="firstName")
    def first_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "firstName"))

    @first_name.setter
    def first_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d58d898c63809cdde441c6bb84ad2da01b8f315c662cce3cec404bdff6b9315)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firstName", value)

    @builtins.property
    @jsii.member(jsii_name="lastName")
    def last_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastName"))

    @last_name.setter
    def last_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44ec0f961b243e7523f47e28c4daa84af3bfe79e9b9f859a078403a17509b5cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lastName", value)

    @builtins.property
    @jsii.member(jsii_name="organizationName")
    def organization_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "organizationName"))

    @organization_name.setter
    def organization_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d325e01e85dcf8b1c2665f648bc756167e293622cce60b838fe496d12b3663da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organizationName", value)

    @builtins.property
    @jsii.member(jsii_name="phoneNumber")
    def phone_number(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "phoneNumber"))

    @phone_number.setter
    def phone_number(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c92ffc05c4a9cd7365f6376de04d2ff4b3fd20192d982ff2dc70119ead42d4b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "phoneNumber", value)

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @state.setter
    def state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2746338f5abfc0658219fe97b31d2ced64eca80bcd4c856050823070ee706cbf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "state", value)

    @builtins.property
    @jsii.member(jsii_name="zipCode")
    def zip_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zipCode"))

    @zip_code.setter
    def zip_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86324a5dd37c1e71da314ea594141b778faf68099b5e25f80812fd58fdb4d017)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zipCode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Route53DomainsRegisteredDomainRegistrantContact]:
        return typing.cast(typing.Optional[Route53DomainsRegisteredDomainRegistrantContact], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Route53DomainsRegisteredDomainRegistrantContact],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78002aefe84e4e3e53eee0952770772aa16e789a661f73eb80bdba3b8ddc384e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.route53DomainsRegisteredDomain.Route53DomainsRegisteredDomainTechContact",
    jsii_struct_bases=[],
    name_mapping={
        "address_line1": "addressLine1",
        "address_line2": "addressLine2",
        "city": "city",
        "contact_type": "contactType",
        "country_code": "countryCode",
        "email": "email",
        "extra_params": "extraParams",
        "fax": "fax",
        "first_name": "firstName",
        "last_name": "lastName",
        "organization_name": "organizationName",
        "phone_number": "phoneNumber",
        "state": "state",
        "zip_code": "zipCode",
    },
)
class Route53DomainsRegisteredDomainTechContact:
    def __init__(
        self,
        *,
        address_line1: typing.Optional[builtins.str] = None,
        address_line2: typing.Optional[builtins.str] = None,
        city: typing.Optional[builtins.str] = None,
        contact_type: typing.Optional[builtins.str] = None,
        country_code: typing.Optional[builtins.str] = None,
        email: typing.Optional[builtins.str] = None,
        extra_params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        fax: typing.Optional[builtins.str] = None,
        first_name: typing.Optional[builtins.str] = None,
        last_name: typing.Optional[builtins.str] = None,
        organization_name: typing.Optional[builtins.str] = None,
        phone_number: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
        zip_code: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param address_line1: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#address_line_1 Route53DomainsRegisteredDomain#address_line_1}.
        :param address_line2: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#address_line_2 Route53DomainsRegisteredDomain#address_line_2}.
        :param city: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#city Route53DomainsRegisteredDomain#city}.
        :param contact_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#contact_type Route53DomainsRegisteredDomain#contact_type}.
        :param country_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#country_code Route53DomainsRegisteredDomain#country_code}.
        :param email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#email Route53DomainsRegisteredDomain#email}.
        :param extra_params: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#extra_params Route53DomainsRegisteredDomain#extra_params}.
        :param fax: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#fax Route53DomainsRegisteredDomain#fax}.
        :param first_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#first_name Route53DomainsRegisteredDomain#first_name}.
        :param last_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#last_name Route53DomainsRegisteredDomain#last_name}.
        :param organization_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#organization_name Route53DomainsRegisteredDomain#organization_name}.
        :param phone_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#phone_number Route53DomainsRegisteredDomain#phone_number}.
        :param state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#state Route53DomainsRegisteredDomain#state}.
        :param zip_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#zip_code Route53DomainsRegisteredDomain#zip_code}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e3e9712c89d3c69f2ae229d9223315bf93d2fe3407ed493275de0fce7ffee70)
            check_type(argname="argument address_line1", value=address_line1, expected_type=type_hints["address_line1"])
            check_type(argname="argument address_line2", value=address_line2, expected_type=type_hints["address_line2"])
            check_type(argname="argument city", value=city, expected_type=type_hints["city"])
            check_type(argname="argument contact_type", value=contact_type, expected_type=type_hints["contact_type"])
            check_type(argname="argument country_code", value=country_code, expected_type=type_hints["country_code"])
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument extra_params", value=extra_params, expected_type=type_hints["extra_params"])
            check_type(argname="argument fax", value=fax, expected_type=type_hints["fax"])
            check_type(argname="argument first_name", value=first_name, expected_type=type_hints["first_name"])
            check_type(argname="argument last_name", value=last_name, expected_type=type_hints["last_name"])
            check_type(argname="argument organization_name", value=organization_name, expected_type=type_hints["organization_name"])
            check_type(argname="argument phone_number", value=phone_number, expected_type=type_hints["phone_number"])
            check_type(argname="argument state", value=state, expected_type=type_hints["state"])
            check_type(argname="argument zip_code", value=zip_code, expected_type=type_hints["zip_code"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if address_line1 is not None:
            self._values["address_line1"] = address_line1
        if address_line2 is not None:
            self._values["address_line2"] = address_line2
        if city is not None:
            self._values["city"] = city
        if contact_type is not None:
            self._values["contact_type"] = contact_type
        if country_code is not None:
            self._values["country_code"] = country_code
        if email is not None:
            self._values["email"] = email
        if extra_params is not None:
            self._values["extra_params"] = extra_params
        if fax is not None:
            self._values["fax"] = fax
        if first_name is not None:
            self._values["first_name"] = first_name
        if last_name is not None:
            self._values["last_name"] = last_name
        if organization_name is not None:
            self._values["organization_name"] = organization_name
        if phone_number is not None:
            self._values["phone_number"] = phone_number
        if state is not None:
            self._values["state"] = state
        if zip_code is not None:
            self._values["zip_code"] = zip_code

    @builtins.property
    def address_line1(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#address_line_1 Route53DomainsRegisteredDomain#address_line_1}.'''
        result = self._values.get("address_line1")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def address_line2(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#address_line_2 Route53DomainsRegisteredDomain#address_line_2}.'''
        result = self._values.get("address_line2")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def city(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#city Route53DomainsRegisteredDomain#city}.'''
        result = self._values.get("city")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def contact_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#contact_type Route53DomainsRegisteredDomain#contact_type}.'''
        result = self._values.get("contact_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def country_code(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#country_code Route53DomainsRegisteredDomain#country_code}.'''
        result = self._values.get("country_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def email(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#email Route53DomainsRegisteredDomain#email}.'''
        result = self._values.get("email")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def extra_params(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#extra_params Route53DomainsRegisteredDomain#extra_params}.'''
        result = self._values.get("extra_params")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def fax(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#fax Route53DomainsRegisteredDomain#fax}.'''
        result = self._values.get("fax")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def first_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#first_name Route53DomainsRegisteredDomain#first_name}.'''
        result = self._values.get("first_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def last_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#last_name Route53DomainsRegisteredDomain#last_name}.'''
        result = self._values.get("last_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def organization_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#organization_name Route53DomainsRegisteredDomain#organization_name}.'''
        result = self._values.get("organization_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def phone_number(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#phone_number Route53DomainsRegisteredDomain#phone_number}.'''
        result = self._values.get("phone_number")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def state(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#state Route53DomainsRegisteredDomain#state}.'''
        result = self._values.get("state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def zip_code(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#zip_code Route53DomainsRegisteredDomain#zip_code}.'''
        result = self._values.get("zip_code")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Route53DomainsRegisteredDomainTechContact(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Route53DomainsRegisteredDomainTechContactOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.route53DomainsRegisteredDomain.Route53DomainsRegisteredDomainTechContactOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9eda2871fa3f5e5bba1c6a4295013d371cfb7fe451555c49330dd44fdc81cff0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAddressLine1")
    def reset_address_line1(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAddressLine1", []))

    @jsii.member(jsii_name="resetAddressLine2")
    def reset_address_line2(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAddressLine2", []))

    @jsii.member(jsii_name="resetCity")
    def reset_city(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCity", []))

    @jsii.member(jsii_name="resetContactType")
    def reset_contact_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContactType", []))

    @jsii.member(jsii_name="resetCountryCode")
    def reset_country_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCountryCode", []))

    @jsii.member(jsii_name="resetEmail")
    def reset_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmail", []))

    @jsii.member(jsii_name="resetExtraParams")
    def reset_extra_params(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExtraParams", []))

    @jsii.member(jsii_name="resetFax")
    def reset_fax(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFax", []))

    @jsii.member(jsii_name="resetFirstName")
    def reset_first_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFirstName", []))

    @jsii.member(jsii_name="resetLastName")
    def reset_last_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLastName", []))

    @jsii.member(jsii_name="resetOrganizationName")
    def reset_organization_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrganizationName", []))

    @jsii.member(jsii_name="resetPhoneNumber")
    def reset_phone_number(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPhoneNumber", []))

    @jsii.member(jsii_name="resetState")
    def reset_state(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetState", []))

    @jsii.member(jsii_name="resetZipCode")
    def reset_zip_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZipCode", []))

    @builtins.property
    @jsii.member(jsii_name="addressLine1Input")
    def address_line1_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "addressLine1Input"))

    @builtins.property
    @jsii.member(jsii_name="addressLine2Input")
    def address_line2_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "addressLine2Input"))

    @builtins.property
    @jsii.member(jsii_name="cityInput")
    def city_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cityInput"))

    @builtins.property
    @jsii.member(jsii_name="contactTypeInput")
    def contact_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contactTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="countryCodeInput")
    def country_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "countryCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="emailInput")
    def email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailInput"))

    @builtins.property
    @jsii.member(jsii_name="extraParamsInput")
    def extra_params_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "extraParamsInput"))

    @builtins.property
    @jsii.member(jsii_name="faxInput")
    def fax_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "faxInput"))

    @builtins.property
    @jsii.member(jsii_name="firstNameInput")
    def first_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "firstNameInput"))

    @builtins.property
    @jsii.member(jsii_name="lastNameInput")
    def last_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lastNameInput"))

    @builtins.property
    @jsii.member(jsii_name="organizationNameInput")
    def organization_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "organizationNameInput"))

    @builtins.property
    @jsii.member(jsii_name="phoneNumberInput")
    def phone_number_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "phoneNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="stateInput")
    def state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stateInput"))

    @builtins.property
    @jsii.member(jsii_name="zipCodeInput")
    def zip_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zipCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="addressLine1")
    def address_line1(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "addressLine1"))

    @address_line1.setter
    def address_line1(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee18e777ef60af77ced45e647cd6049bbc36cea75a66cf943a0a7909525cf465)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "addressLine1", value)

    @builtins.property
    @jsii.member(jsii_name="addressLine2")
    def address_line2(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "addressLine2"))

    @address_line2.setter
    def address_line2(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2766ab99f4b090da7fdcce440adaee865481523346a7f9508cd8dfe4f5808017)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "addressLine2", value)

    @builtins.property
    @jsii.member(jsii_name="city")
    def city(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "city"))

    @city.setter
    def city(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c9638d91e91c5a34d1a8b00088f24bd07384b7e8570859ac787cc16d41fad51)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "city", value)

    @builtins.property
    @jsii.member(jsii_name="contactType")
    def contact_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contactType"))

    @contact_type.setter
    def contact_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56ba1ad71263fe1252f9887205ae0c657db0f032b1eb935c60e91756d0d30c07)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contactType", value)

    @builtins.property
    @jsii.member(jsii_name="countryCode")
    def country_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "countryCode"))

    @country_code.setter
    def country_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4194a5d119aae3c6bb9db31f5df160aa7d8af7d644a99fad810f70d31973441)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "countryCode", value)

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "email"))

    @email.setter
    def email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36feb81b2e2f8648bd51aa24b5da43110d6e8da897ac9552f986ac61cabdef5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)

    @builtins.property
    @jsii.member(jsii_name="extraParams")
    def extra_params(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "extraParams"))

    @extra_params.setter
    def extra_params(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04057037566f858e669f48543db2b7de1adc14c58352c752112ffee1e5056e3f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "extraParams", value)

    @builtins.property
    @jsii.member(jsii_name="fax")
    def fax(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fax"))

    @fax.setter
    def fax(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c45f393aaa55e19a1b03cc7487e37ba09970155efab53c88b326b2358f37d2be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fax", value)

    @builtins.property
    @jsii.member(jsii_name="firstName")
    def first_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "firstName"))

    @first_name.setter
    def first_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9573fa88e11842d24c395416ba877aefe4fc53384754692945ae2a6c9a0f91ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firstName", value)

    @builtins.property
    @jsii.member(jsii_name="lastName")
    def last_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastName"))

    @last_name.setter
    def last_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1de648922ad6a3fd927c043db62267497c8b580690b668aa58a38fd666e600b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lastName", value)

    @builtins.property
    @jsii.member(jsii_name="organizationName")
    def organization_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "organizationName"))

    @organization_name.setter
    def organization_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__394f36b9c822dff2d790d65eaf8b84afb0c02b89fdb25dfb5085499ffca15384)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organizationName", value)

    @builtins.property
    @jsii.member(jsii_name="phoneNumber")
    def phone_number(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "phoneNumber"))

    @phone_number.setter
    def phone_number(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f4e06f06407e5021972bc5621afe1844703cf62f572a0677f89cb860d19918e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "phoneNumber", value)

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @state.setter
    def state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58e4ee43f4e1bbf1bf498d984f6f4b85e74900cade4f9520acaff3d150c26cbd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "state", value)

    @builtins.property
    @jsii.member(jsii_name="zipCode")
    def zip_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zipCode"))

    @zip_code.setter
    def zip_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be73802d28b8db980632f0b77e27b8b5e8ae55a1bd7b5ddfe9580eea23ae83ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zipCode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Route53DomainsRegisteredDomainTechContact]:
        return typing.cast(typing.Optional[Route53DomainsRegisteredDomainTechContact], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Route53DomainsRegisteredDomainTechContact],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f43d2aa0703e522da4700b3983ca488d3cc6a8d07d4d2b1e1b1676c7d9af8e00)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.route53DomainsRegisteredDomain.Route53DomainsRegisteredDomainTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "update": "update"},
)
class Route53DomainsRegisteredDomainTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#create Route53DomainsRegisteredDomain#create}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#update Route53DomainsRegisteredDomain#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca446d45cf457b53218bfa0ab9bcc587bd7b4b1431305b3c9c095ab5960cbe74)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#create Route53DomainsRegisteredDomain#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/route53domains_registered_domain#update Route53DomainsRegisteredDomain#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Route53DomainsRegisteredDomainTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Route53DomainsRegisteredDomainTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.route53DomainsRegisteredDomain.Route53DomainsRegisteredDomainTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f1931c01c13271a47880dce2a3462c9336307af14feff35ae9073698dd2239f7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__6e1fa838d34a19d7911d689557c4f022f986813b3a540a189fd24c5c5db6f2ca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d16fe9060af5e3e06b8c2ab26443d53f3c9451780606fbcf812754b068ab0a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[Route53DomainsRegisteredDomainTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Route53DomainsRegisteredDomainTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Route53DomainsRegisteredDomainTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68e18a8a32d7b3cf50800a0335e85697ad1229d5f331f039db5400b15d2d8bb3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Route53DomainsRegisteredDomain",
    "Route53DomainsRegisteredDomainAdminContact",
    "Route53DomainsRegisteredDomainAdminContactOutputReference",
    "Route53DomainsRegisteredDomainConfig",
    "Route53DomainsRegisteredDomainNameServer",
    "Route53DomainsRegisteredDomainNameServerList",
    "Route53DomainsRegisteredDomainNameServerOutputReference",
    "Route53DomainsRegisteredDomainRegistrantContact",
    "Route53DomainsRegisteredDomainRegistrantContactOutputReference",
    "Route53DomainsRegisteredDomainTechContact",
    "Route53DomainsRegisteredDomainTechContactOutputReference",
    "Route53DomainsRegisteredDomainTimeouts",
    "Route53DomainsRegisteredDomainTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__ebacca01986aaab2b11a8cf39a2cd7c3893af7c7cbd224ddacc231d6415e5a07(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    domain_name: builtins.str,
    admin_contact: typing.Optional[typing.Union[Route53DomainsRegisteredDomainAdminContact, typing.Dict[builtins.str, typing.Any]]] = None,
    admin_privacy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    auto_renew: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    name_server: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Route53DomainsRegisteredDomainNameServer, typing.Dict[builtins.str, typing.Any]]]]] = None,
    registrant_contact: typing.Optional[typing.Union[Route53DomainsRegisteredDomainRegistrantContact, typing.Dict[builtins.str, typing.Any]]] = None,
    registrant_privacy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tech_contact: typing.Optional[typing.Union[Route53DomainsRegisteredDomainTechContact, typing.Dict[builtins.str, typing.Any]]] = None,
    tech_privacy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    timeouts: typing.Optional[typing.Union[Route53DomainsRegisteredDomainTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    transfer_lock: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
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

def _typecheckingstub__9705c5d8180be58e73df7c21bba296138d54100bd4572c8309d61b52cc9efc45(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Route53DomainsRegisteredDomainNameServer, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4883cc343d710843ceb34ca2ca670c6184c104a019f87bab9b6d8d84834c7ff8(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__072f095377b1832a4367d17e9d412d2173f601d99b48f90828d742104cf46b2a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f616340bad8b18c5c19bcc53f7c49e947af87f2d3f39cc9cc30a6475af4fe3ce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__029e36151f3be9de3f4cc23ef571db0686e149e7b14088232ca1cf523f08b85a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ada9eba9910eaeecd3cf902a6b948be9293615eabe084fe569f8a61fc0e46f95(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c0c3f49ef2ab31fa6bd942084d1c8d97ffbd32afa6d2a166c2cb2634a900a1f(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06547bedcd00f147ba500e513c2a25b23e6eb9d15b0344834b9a5f5b507d8793(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73d4e2c48751797dd567688c2e27875737fbae02616c903f69b96b545e3a9a4d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__182c77ce2c2e47091379715edfd8b5e75d4a205a9f0377fff7e85293afdb5558(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a087d955d3695b3d55ea15197650fa8867722a0adc556d43cec425a71217e61c(
    *,
    address_line1: typing.Optional[builtins.str] = None,
    address_line2: typing.Optional[builtins.str] = None,
    city: typing.Optional[builtins.str] = None,
    contact_type: typing.Optional[builtins.str] = None,
    country_code: typing.Optional[builtins.str] = None,
    email: typing.Optional[builtins.str] = None,
    extra_params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    fax: typing.Optional[builtins.str] = None,
    first_name: typing.Optional[builtins.str] = None,
    last_name: typing.Optional[builtins.str] = None,
    organization_name: typing.Optional[builtins.str] = None,
    phone_number: typing.Optional[builtins.str] = None,
    state: typing.Optional[builtins.str] = None,
    zip_code: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ef7d83549553902714caeee04403167749fca6547fadb78395b8bc892db3d50(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a092abf482adc1b6f575ccc60285ba242ed6e00b3c0731a9d3d33b755881c5ba(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f63188c925a7685e843f2f01d3120d1e5bed295a1949b90071ddb74f818df9e6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a52f954b473fd3592b5ded705d83a975f7f65e63f54bbd3239b74bc8fbfe1f2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7311eddaffb091f8d4149d768b82999902e82d790c48566081f34a38f367787d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45e06ef816d10c5cc1a3aa31d8b597a15ee18a818900ef3730de848bc7171b2d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d58e3140a6ece4bb2538f79304df966e088e478ec8e0c5d6d24de9177adef6b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__371f00f0c043a26f5d858ebaf1b984ec9af1331753eb6dc2907c27897d6b7532(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b859b69a88eb75b16c1913d566a2010e52d04b1e04193a70fab1ade3bdd14fa0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c55022a4787cac257525e96392efa9ce531218988d9844f0751393b81b54a63(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1725b40170fbaf7bb29c3a426f2343562312160fbfb781f9f83b1f5ef667519a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02b760d8c4e9f43d5b5d7cf1b2f52708c314904e0c95161b03f82fdf0d517ff0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0cdf4e06e657539a462cd40189be87c27612edb99f2503c443391954ff57335(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ab8f44ca9f47b068baca1ba7804ea8bddcb96995164ea263563271f11e9ca56(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba5a70f67d63e109e2b897cc4014817277e05d2576758c55e0c9d3946976ca54(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe17cfe35d1f7548b164dee35c22c44e3656976521aadc886321144516768622(
    value: typing.Optional[Route53DomainsRegisteredDomainAdminContact],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83c2573e70b1de8f8c0f91d7a99494f272350f882cca5feeffd1a6542cb242e6(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    domain_name: builtins.str,
    admin_contact: typing.Optional[typing.Union[Route53DomainsRegisteredDomainAdminContact, typing.Dict[builtins.str, typing.Any]]] = None,
    admin_privacy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    auto_renew: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    name_server: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Route53DomainsRegisteredDomainNameServer, typing.Dict[builtins.str, typing.Any]]]]] = None,
    registrant_contact: typing.Optional[typing.Union[Route53DomainsRegisteredDomainRegistrantContact, typing.Dict[builtins.str, typing.Any]]] = None,
    registrant_privacy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tech_contact: typing.Optional[typing.Union[Route53DomainsRegisteredDomainTechContact, typing.Dict[builtins.str, typing.Any]]] = None,
    tech_privacy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    timeouts: typing.Optional[typing.Union[Route53DomainsRegisteredDomainTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    transfer_lock: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1ba14b3e57fac5f0be5692d218d7ead510c3dbf9db637ea4f7c60fee8267c7f(
    *,
    name: builtins.str,
    glue_ips: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80ddf97ade8458778c1000d753bab322b2032dff92526e44ae28d74e8f711cef(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ad192e3a6b228d921b3af1cda9d7b4112eb4652b6f18682c88265c6b1d0168a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17dcbebce9737135e20bbae7aa6d6d7e722d09429ae76e8a5dfba65e4eb3f0f4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d76a1f9522256041d15d57494af6379b40106ea65b7464f3e2773f5a0e1d7bc7(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e429de63ca815de5761170518c39bc24902587b8474331cb365d808237fedd6e(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__347a849416f96228b471f944e6d20b4d14bb5685b2ce408d2db109c78c0c7298(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Route53DomainsRegisteredDomainNameServer]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a9df746c0b438d8f74d0d57078e6f86269a2d4e1ccbf8995e24ca1675aa20a6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a52457d7bd0bd77dd6503786d67687c41aa92b1e1b65182937469557bf86cef4(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac5ea35baad061094da4cd01988471f9b6000fa9ffe16cce94d4afd78454a38a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2daa791007739d3576424d86e7f686e295021fba773b156e9b5bb296960615c7(
    value: typing.Optional[typing.Union[Route53DomainsRegisteredDomainNameServer, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b21b9a1f19197daa03dbc8eb6b9698fd78a109ee66a40a449a7dda0edb23fba(
    *,
    address_line1: typing.Optional[builtins.str] = None,
    address_line2: typing.Optional[builtins.str] = None,
    city: typing.Optional[builtins.str] = None,
    contact_type: typing.Optional[builtins.str] = None,
    country_code: typing.Optional[builtins.str] = None,
    email: typing.Optional[builtins.str] = None,
    extra_params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    fax: typing.Optional[builtins.str] = None,
    first_name: typing.Optional[builtins.str] = None,
    last_name: typing.Optional[builtins.str] = None,
    organization_name: typing.Optional[builtins.str] = None,
    phone_number: typing.Optional[builtins.str] = None,
    state: typing.Optional[builtins.str] = None,
    zip_code: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab403787f298ce851d79834f2acd655c939fabf8e8be1be64c4b33a8dbe28d20(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__196d8dc70a2c2db4d396a85c9ec20319fda6870483d5a8f119775b2b803febdf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb5f9b34d81f7967e71cd0256190b7523a4a2f8b4fa8a2cd597aadc7f62e130d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7c9335c98718130c95796cc6aee255bdb315bb5c76c951a038d4a929c366be4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45893ce66250ebce457313cd207f87b7875160d0526afd3612ddcb3849a93112(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4e0d148199a009b4677db944528f31ad78d02e90a93b0965bdfcca5224ea5e5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2533630d312eb0d461213e4f393e4e15f38547344b2554ef71f63674932c0716(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__055ab668042ebf8b118a75b3776cf8462237b19b1e87a0033e0622e9fc768e25(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c5c7d3d922ae8f98a21a0e8b6c4c27a72cfea2e38834dc4a216c58d15518718(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d58d898c63809cdde441c6bb84ad2da01b8f315c662cce3cec404bdff6b9315(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44ec0f961b243e7523f47e28c4daa84af3bfe79e9b9f859a078403a17509b5cc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d325e01e85dcf8b1c2665f648bc756167e293622cce60b838fe496d12b3663da(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c92ffc05c4a9cd7365f6376de04d2ff4b3fd20192d982ff2dc70119ead42d4b0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2746338f5abfc0658219fe97b31d2ced64eca80bcd4c856050823070ee706cbf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86324a5dd37c1e71da314ea594141b778faf68099b5e25f80812fd58fdb4d017(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78002aefe84e4e3e53eee0952770772aa16e789a661f73eb80bdba3b8ddc384e(
    value: typing.Optional[Route53DomainsRegisteredDomainRegistrantContact],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e3e9712c89d3c69f2ae229d9223315bf93d2fe3407ed493275de0fce7ffee70(
    *,
    address_line1: typing.Optional[builtins.str] = None,
    address_line2: typing.Optional[builtins.str] = None,
    city: typing.Optional[builtins.str] = None,
    contact_type: typing.Optional[builtins.str] = None,
    country_code: typing.Optional[builtins.str] = None,
    email: typing.Optional[builtins.str] = None,
    extra_params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    fax: typing.Optional[builtins.str] = None,
    first_name: typing.Optional[builtins.str] = None,
    last_name: typing.Optional[builtins.str] = None,
    organization_name: typing.Optional[builtins.str] = None,
    phone_number: typing.Optional[builtins.str] = None,
    state: typing.Optional[builtins.str] = None,
    zip_code: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9eda2871fa3f5e5bba1c6a4295013d371cfb7fe451555c49330dd44fdc81cff0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee18e777ef60af77ced45e647cd6049bbc36cea75a66cf943a0a7909525cf465(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2766ab99f4b090da7fdcce440adaee865481523346a7f9508cd8dfe4f5808017(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c9638d91e91c5a34d1a8b00088f24bd07384b7e8570859ac787cc16d41fad51(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56ba1ad71263fe1252f9887205ae0c657db0f032b1eb935c60e91756d0d30c07(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4194a5d119aae3c6bb9db31f5df160aa7d8af7d644a99fad810f70d31973441(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36feb81b2e2f8648bd51aa24b5da43110d6e8da897ac9552f986ac61cabdef5a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04057037566f858e669f48543db2b7de1adc14c58352c752112ffee1e5056e3f(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c45f393aaa55e19a1b03cc7487e37ba09970155efab53c88b326b2358f37d2be(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9573fa88e11842d24c395416ba877aefe4fc53384754692945ae2a6c9a0f91ee(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1de648922ad6a3fd927c043db62267497c8b580690b668aa58a38fd666e600b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__394f36b9c822dff2d790d65eaf8b84afb0c02b89fdb25dfb5085499ffca15384(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f4e06f06407e5021972bc5621afe1844703cf62f572a0677f89cb860d19918e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58e4ee43f4e1bbf1bf498d984f6f4b85e74900cade4f9520acaff3d150c26cbd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be73802d28b8db980632f0b77e27b8b5e8ae55a1bd7b5ddfe9580eea23ae83ae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f43d2aa0703e522da4700b3983ca488d3cc6a8d07d4d2b1e1b1676c7d9af8e00(
    value: typing.Optional[Route53DomainsRegisteredDomainTechContact],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca446d45cf457b53218bfa0ab9bcc587bd7b4b1431305b3c9c095ab5960cbe74(
    *,
    create: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1931c01c13271a47880dce2a3462c9336307af14feff35ae9073698dd2239f7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e1fa838d34a19d7911d689557c4f022f986813b3a540a189fd24c5c5db6f2ca(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d16fe9060af5e3e06b8c2ab26443d53f3c9451780606fbcf812754b068ab0a1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68e18a8a32d7b3cf50800a0335e85697ad1229d5f331f039db5400b15d2d8bb3(
    value: typing.Optional[typing.Union[Route53DomainsRegisteredDomainTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
