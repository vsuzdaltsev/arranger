"""Manipulate Kubernetes LoadBalancer objects."""

import os
from typing import Any, List

from kubernetes import client, config

from arranger_automation.log import Log


class BasicLoadBalancers:
    def __repr__(self) -> str:
        """Class instance representation."""
        return f"{super().__repr__()}: {self.__dict__}"

    def __init__(self):
        self.log = Log.logger(desc=type(self).__name__)
        self.client = client.CoreV1Api()

    @classmethod
    def auth(cls) -> Any:
        """Authorize Kubernetes client."""
        if os.getenv("KUBECONFIG"):
            config.load_kube_config()
        else:
            config.load_incluster_config()

    def external_addresses(self, address_type: str = "hostname") -> List:
        """External addresses."""
        addresses = []
        for svc in self.client.list_service_for_all_namespaces().items:
            self.log.debug(f">> Service name: {svc.metadata.name}.")
            if svc.status.load_balancer.ingress is not None:
                for load_balancer in svc.status.load_balancer.ingress:
                    addresses.append(getattr(load_balancer, address_type))

        return list(set(addresses))

    def hostnames(self) -> List:
        """List of external hostnames."""
        return self.external_addresses(address_type="hostname")

    def ips(self) -> List:
        """List of external ips."""
        return self.external_addresses(address_type="ip")


if __name__ == "__main__":
    BasicLoadBalancers.auth()
    print(f">> Hostnames: {BasicLoadBalancers().hostnames()}")
    print(f">> Ips: {BasicLoadBalancers().ips()}")
    print(f">> External addresses: {BasicLoadBalancers().external_addresses()}")
    print(
        f">> External addresses of type hostname: {BasicLoadBalancers().external_addresses(address_type='hostname')}"
    )
    print(
        f">> External addresses of type ip: {BasicLoadBalancers().external_addresses(address_type='ip')}"
    )
