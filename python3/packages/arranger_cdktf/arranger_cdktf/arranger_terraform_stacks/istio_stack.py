import json

from arranger_cdktf.imports.helm.release import Release
from arranger_cdktf.imports.kubernetes.namespace import Namespace, NamespaceMetadata
from arranger_cdktf.imports.kubernetes.manifest import Manifest
from arranger_cdktf.imports.null import Resource as NullResource

from .basic_stack import AwsBasicStack, Construct, TfConf


class BasicAwsIstioStack(AwsBasicStack):
    """Install Istio service mesh."""

    ISTIO_VERSION = "1.23.2"

    @property
    def _name_prefix(self) -> str:
        return "istio"

    def __init__(self, scope: Construct, ns: str, config: type(TfConf)):
        super().__init__(scope, ns, config)

        self.kubeconfig = self._generate_kube_config_eks()  # FIXME: check sanity
        self.aws_provider = self.globals.automation(scope=self)

        self.vpc = self._aws_eks_main_vpc()

        self.vnet_ip_range = self.globals.ip_ranges["vpc-main"]
        self.subnets = self.vnet_ip_range["subnets"]

        self.k8s_provider = self.globals.k8s_provider(scope=self)
        self.helm_provider = self.globals.helm_provider(scope=self)
        self.null_provider = self.globals.null_provider(scope=self)

        self.istio_system_namespace = self._istio_system_namespace()
        self.istio_ingress_namespace = self._istio_ingress_namespace()

        self.istio_base_helm_release = self._istio_base_helm_release()
        self.istiod_helm_release = self._istiod_helm_release()
        self.istio_ingress_helm_release = self._istio_ingress_helm_release()

        self.kiali_helm_release = self._kiali_helm_release()

        # self.crds = self._crds()

    def _istio_system_namespace(self) -> type(Namespace):
        return Namespace(
            scope=self,
            id_=f"istio-system-namespace-{self.globals.cluster_name_alias}",
            metadata=NamespaceMetadata(name="istio-system"),
            provider=self.k8s_provider,
        )

    def _istio_ingress_namespace(self) -> Namespace:
        return Namespace(
            scope=self,
            id_=f"istio-ingress-namespace-{self.globals.cluster_name_alias}",
            metadata=NamespaceMetadata(
                name="istio-ingress", labels={"istio-injection": "enabled"}
            ),
            provider=self.k8s_provider,
        )

    def _istio_base_helm_release(self) -> Release:
        return Release(
            scope=self,
            id_=self._name(object_type="helm-release-istio-base"),
            name="istio",
            namespace=self.istio_system_namespace.id,
            chart="base",
            repository="https://istio-release.storage.googleapis.com/charts",
            version=self.ISTIO_VERSION,
            wait=True,
            provider=self.helm_provider,
            depends_on=[self.istio_system_namespace],
            upgrade_install=True,
        )

    def _istiod_helm_release(self) -> Release:
        def _autoscaling() -> str:
            return json.dumps({"pilot": {"autoscaleEnabled": True}})

        def _tracing() -> str:
            return json.dumps({"tracing": {"enabled": True, "provider": "zipkin"}})

        # TODO: add https://github.com/istio/istio/blob/master/samples/addons/extras/prometheus-operator.yaml
        return Release(
            scope=self,
            id_=self._name(object_type="helm-release-istiod"),
            name="istiod",
            namespace=self.istio_system_namespace.id,
            chart="istiod",
            repository="https://istio-release.storage.googleapis.com/charts",
            version=self.ISTIO_VERSION,
            values=[_autoscaling(), _tracing()],
            wait=True,
            provider=self.helm_provider,
            depends_on=[self.istio_system_namespace],
            upgrade_install=True,
        )

    def _istio_ingress_helm_release(self) -> Release:
        def _internal_lb() -> str:
            from arranger_automation_aws.helpers import SubnetHelper

            private_subnet_ids = ",".join(
                sorted(
                    SubnetHelper().public_subnet_ids(
                        region=self.globals.aws_region,
                        profile=self.globals.aws_profile,
                        filter_by=f"vpc-main-subnet-.*-{self.globals.cluster_name_alias}-private",
                    )
                )
            )
            _lb_tag = "service.beta.kubernetes.io/aws-load-balancer"

            return json.dumps(
                {
                    "labels": {
                        "version": self.ISTIO_VERSION,
                    },
                    "service": {
                        "annotations": {
                            f"{_lb_tag}-type": "nlb",
                            f"{_lb_tag}-internal": "true",
                            f"{_lb_tag}-additional-resource-tags": "NLBSource=api-gateway",
                            f"{_lb_tag}-subnets": private_subnet_ids,
                            f"{_lb_tag}-proxy-protocol": "*",
                        },
                        "ports": [
                            {
                                "port": 15021,
                                "targetPort": 15021,
                                "name": "status-port",
                                "protocol": "TCP",
                            },
                            {
                                "port": 80,
                                "targetPort": 80,
                                "name": "http2",
                                "protocol": "TCP",
                            },
                        ],
                        "externalTrafficPolicy": "Local",
                    },
                    "autoscaling": {
                        "minReplicas": 3,
                    },
                }
            )

        return Release(
            scope=self,
            id_=self._name(object_type="helm-release-istio-ingress"),
            name=self.globals.istio_ingress_name,
            namespace=self.istio_ingress_namespace.id,
            chart="gateway",
            repository="https://istio-release.storage.googleapis.com/charts",
            version=self.ISTIO_VERSION,
            values=[_internal_lb()],
            wait=True,
            provider=self.helm_provider,
            depends_on=[self.istio_ingress_namespace, self.istiod_helm_release],
            upgrade_install=True,
        )

    def _crds(self) -> type(NullResource):
        uniq_name = self._name(object_type="crd")
        cmd = (
            f"export KUBECONFIG={self.globals.where_kubeconfig} ; "
            + "kubectl get crd gateways.gateway.networking.k8s.io &> /dev/null || { kubectl kustomize 'github.com/kubernetes-sigs/gateway-api/config/crd?ref=v0.6.1' | kubectl apply -f -; }"
        )

        null = NullResource(
            self,
            id=uniq_name,
            provider=self.null_provider,
            depends_on=[self.istio_ingress_helm_release],
        )

        null.add_override(
            "provisioner",
            [
                {
                    "local-exec": {"command": cmd},
                },
                # {
                #     "local-exec": {
                #         "command": cmd(
                #             action="delete", postfix="--ignore-not-found=true"
                #         ),
                #         "when": "destroy",
                #     },
                # },
            ],
        )

        return null

    def _kiali_helm_release(self) -> type(Release):

        return Release(
            scope=self,
            id_=self._name(object_type="helm-release-kiali"),
            name="kiali",
            namespace=self.istio_system_namespace.id,
            chart="kiali-server",
            repository="https://kiali.org/helm-charts",
            version="2.0.0",
            values=[
                json.dumps(
                    {
                        "external_services": {
                            "prometheus": {
                                "url": f"http://kube-prometheus-stack-prometheus.monitoring:9090"
                            },
                            "grafana": {
                                "url": f"http://kube-prometheus-stack-grafana.monitoring:80"
                            },
                        }
                    }
                )
            ],
            wait=True,
            provider=self.helm_provider,
            depends_on=[self.istio_system_namespace],
            upgrade_install=True,
        )
