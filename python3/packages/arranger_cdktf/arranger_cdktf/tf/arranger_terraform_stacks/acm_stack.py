from typing import List

from arranger_automation_aws.helpers import Route53Helper
from arranger_cdktf.imports.aws.acm_certificate import AcmCertificate
from arranger_cdktf.imports.aws.acm_certificate_validation import (
    AcmCertificateValidation,
)
from arranger_cdktf.imports.aws.data_aws_route53_zone import DataAwsRoute53Zone
from arranger_cdktf.imports.aws.route53_record import Route53Record
from arranger_cdktf.imports.null import NullProvider
from arranger_cdktf.imports.null import Resource as NullResource

from .basic_stack import AwsBasicStack, Construct, TfConf


class AcmStack(AwsBasicStack):
    def __init__(self, scope: Construct, ns: str, config: TfConf):
        super().__init__(scope, ns, config=config)

        self.global_provider = self.globals.global_automation(scope=self)
        self.provider = self.globals.automation(scope=self)
        self.global_region = self.globals.aws_global_region
        self.hosted_zone_domain_name = self.globals.hosted_zone_domain_name
        self.custom_domains = self.globals.custom_domains()
        self.zone = self._zone()
        self.update_delegated_ns_servers = self._update_delegated_ns_servers()
        self.cert = self._cert()
        self.cert_london = self._cert_london()
        self.validation_record = self._validation_record()
        self.cert_validation = self._cert_validation()

    def _zone(self) -> type(DataAwsRoute53Zone):
        return DataAwsRoute53Zone(
            self,
            id_=f"{self.hosted_zone_domain_name}-zone",
            name=self.hosted_zone_domain_name,
            provider=self.global_provider,
            # tags=self.globals.common_tags(),
        )

    def _update_delegated_ns_servers(self) -> type(NullResource):
        null = None
        zone_exist = Route53Helper.hosted_zone_id(
            zone_name=self.hosted_zone_domain_name,
            profile=self.globals.aws_profile,
        )

        if zone_exist:
            nameservers = self._normalized_domain_servers(
                servers=Route53Helper.hosted_zone_nameservers(
                    zone_name=self.hosted_zone_domain_name,
                    profile=self.globals.aws_profile,
                )
            )
            null = NullResource(
                self,
                id="update-delegated-ns-servers",
                depends_on=[self.zone],
                provider=NullProvider(self, id="null-provider"),
            )
            cmd = "aws route53domains update-domain-nameservers"
            # "--region us-east-1". us-east-1 region is used for global route53domains operations.
            region = f"--region {self.global_region}"
            domain = f"--domain-name {self.hosted_zone_domain_name}"
            profile = f"--profile {self.globals.aws_profile}"
            local_command = " ".join(
                [cmd, region, domain, f"--nameservers {nameservers}", profile]
            )

            null.add_override(
                "provisioner", [{"local-exec": {"command": local_command}}]
            )

        return null

    def _cert(self) -> type(AcmCertificate):
        """
        Cert must be in us-east-1 region:
        https://aws.amazon.com/premiumsupport/knowledge-center/migrate-ssl-cert-us-east/
        """

        return AcmCertificate(
            scope=self,
            id_=f"{self.hosted_zone_domain_name}-cert",
            domain_name=self.hosted_zone_domain_name,
            validation_method="DNS",
            subject_alternative_names=self._subject_alternative_names(),
            provider=self.global_provider,
            # depends_on=[self.update_delegated_ns_servers],
            # options=AcmCertificateOptions(),
            tags=self.stack_tags,
            lifecycle=self.lifecycle_policy(),
        )

    # def _cert(self) -> type(AcmCertificate):
    #     """
    #     Cert must be in us-east-1 region:
    #     https://aws.amazon.com/premiumsupport/knowledge-center/migrate-ssl-cert-us-east/
    #     """
    #     alternative_names = self.custom_domains
    #     domain_name = self.hosted_zone_domain_name
    #
    #     if domain_name in alternative_names:
    #         alternative_names.remove(domain_name)
    #
    #     return AcmCertificate(
    #         self,
    #         id_=f"{domain_name}-cert",
    #         domain_name=domain_name,
    #         validation_method="DNS",
    #         subject_alternative_names=alternative_names,
    #         provider=self.global_provider,
    #         # depends_on=[self.update_delegated_ns_servers],
    #         # options=AcmCertificateOptions(),
    #         tags=self.stack_tags,
    #         lifecycle=self.lifecycle_policy(),
    #     )

    def _cert_london(self) -> type(AcmCertificate):
        alternative_names = self.custom_domains
        domain_name = self.hosted_zone_domain_name

        if domain_name in alternative_names:
            alternative_names.remove(domain_name)

        return AcmCertificate(
            scope=self,
            id_=f"{domain_name}-cert-home-region",
            domain_name=domain_name,
            validation_method="DNS",
            subject_alternative_names=alternative_names,
            provider=self.provider,
            # depends_on=[self.update_delegated_ns_servers],
            # options=AcmCertificateOptions(),
            tags=self.stack_tags,
            lifecycle=self.lifecycle_policy(),
        )

    def _validation_record(self) -> type(Route53Record):
        record = Route53Record(
            scope=self,
            id_="CertValidationRecord",
            name="${each.value.name}",
            type="${each.value.type}",
            records=["${each.value.record}"],
            zone_id=self.zone.zone_id,
            ttl=60,
            allow_overwrite=True,
            depends_on=[self.cert],
            provider=self.global_provider,
        )
        # https://github.com/hashicorp/terraform-cdk/issues/430#issuecomment-831511019

        cert = self.cert
        fui = cert.friendly_unique_id
        hcl_override = [
            "${{"
            + f"for dvo in aws_acm_certificate.{fui}.domain_validation_options : dvo.domain_name => "
            + "{",
            "name   = dvo.resource_record_name",
            "record = dvo.resource_record_value",
            "type   = dvo.resource_record_type",
            "}}}",
        ]

        record.add_override("for_each", "\n".join(hcl_override))

        return record

    def _cert_validation(self) -> type(AcmCertificateValidation):
        crt_validation = AcmCertificateValidation(
            scope=self,
            id_="cert-validation",
            certificate_arn=self.cert.arn,
            depends_on=[self.validation_record],
            provider=self.global_provider,
        )

        validation_record = self.validation_record
        fui = validation_record.friendly_unique_id
        crt_validation.add_override(
            "validation_record_fqdns",
            "${" + f"[for record in aws_route53_record.{fui} : record.fqdn]" + "}",
        )

        return crt_validation

    @staticmethod
    def _normalized_domain_servers(servers: List) -> str:
        return " ".join(["Name=" + srv for srv in servers])

    def _subject_alternative_names(self) -> List[str]:
        return self.globals.custom_domains()
