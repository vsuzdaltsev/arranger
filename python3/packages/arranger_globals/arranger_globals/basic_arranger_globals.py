"""Global functions. Basic classes."""

from abc import ABC
import ipaddress
import re
from typing import Any, Callable, Dict, List, Union


class NotIPv4Error(Exception):
    pass


def validate_subnets(func: Callable) -> Callable:
    def check(*args):
        from arranger_automation.validate import ValidateSubnets

        return ValidateSubnets(ranges=func(*args)).validate()

    return check


def to_kebab(s: str) -> str:
    s = s.replace("_", "-").replace(" ", "-")
    s = re.sub(r"(?<!^)(?=[A-Z])", "-", s)

    return s.lower()


def validate_ipv4(func: Callable) -> Callable:
    def is_ip_v4(value):
        try:
            ipaddress.ip_address(address=value)
        except ValueError:
            ipaddress.ip_network(address=value)
        return value

    def check(*args):
        returned_value = func(*args)

        if isinstance(returned_value, str):
            is_ip_v4(returned_value)

            return returned_value

        if isinstance(returned_value, list):
            for ip in returned_value:
                is_ip_v4(ip)

            return returned_value

        return NotIPv4Error(
            f"'{func} must return a string or a list of strings. But it is returning '{returned_value}'."
        )

    return check


class ArrangerMixin(ABC):
    def __repr__(self) -> str:
        return f"{super().__repr__()}: {self.__dict__}"

    @property
    def cli_container_root(self) -> str:
        return "/opt/arranger"

    @property
    def aws_region(self) -> str:
        from arranger_conf.arranger_conf import ArrangerConf

        try:
            return ArrangerConf.TENANTS[self.tenant]["aws_region"]
        except KeyError as err:
            self.log.debug(
                f">> Cluster '{self.tenant}' doesn't have "
                f"'aws_region' attribute. Error: {err}. Returning empty string.."
            )
            return ""

    @property
    def aws_profile(self) -> str:
        from arranger_conf.arranger_conf import ArrangerConf

        return ArrangerConf.TENANTS[self.tenant]["aws_profile"]

    @property
    def aws_account_id(self) -> str:
        from arranger_conf.arranger_conf import ArrangerConf

        return ArrangerConf.TENANTS[self.tenant]["aws_account_id"]

    @property
    def where_kubeconfig(self) -> str:
        return f"{self.cli_container_root}/{self.tenant}_kube_config.yaml"

    @property
    def hosted_zone_domain_name(self) -> str:
        from arranger_conf.arranger_conf import ArrangerConf

        return ArrangerConf.TENANTS[self.tenant]["domain"]

    @property
    def kube_prometheus_stack_name(self) -> str:
        return "kube-prometheus-stack"

    @property
    def all_services(self) -> Dict[str, Any]:
        from arranger_conf.arranger_cdk8s_conf import K8sConf

        return getattr(K8sConf, self.environment.capitalize()).ALL_SERVICES


class ByEnvironment(ArrangerMixin):
    def __init__(self, environment: str, **kwargs: Dict[str, Any]):
        from arranger_automation.log import Log

        self.log = Log().logger(desc=self.__class__.__name__)
        self.environment = environment
        self.kwargs = kwargs

        if kwargs.get("config"):
            self.config = kwargs.get("config")

    @property
    def tenant(self) -> str:
        from arranger_conf import ArrangerConf

        for cluster_name, cluster_conf in ArrangerConf.TENANTS.items():
            if self.environment == cluster_name:
                return cluster_name

            envs = cluster_conf.get("environments")
            if envs and self.environment in envs:
                return cluster_name

        def tools_envs_from_all_environments():
            from arranger_conf import K8sConf

            if self.environment in (env.lower() for env in K8sConf.ALL_ENVIRONMENTS):
                return (
                    getattr(K8sConf, self.tenant.capitalize())
                    .__mro__[1]
                    .__mro__[0]
                    .__name__.lower()
                )

        try:
            return tools_envs_from_all_environments()
        except BaseException as err:
            err_msg = (
                f"Environment '{self.environment}' isn't a part of existing clusters. "
                f"Valid value is one of {self.all_environments}. "
                f"Can't find tenant for '{self.environment}'."
            )
            raise ValueError(err_msg) from err

    @property
    def all_environments(self) -> List[str]:
        from arranger_conf.arranger_cdk8s_conf import K8sConf

        return [e.lower() for e in K8sConf.ALL_ENVIRONMENTS]

    @property
    def is_environment(self) -> Union[bool, None]:
        from arranger_conf.arranger_conf import ArrangerConf

        for cluster_name, cluster_conf in ArrangerConf.TENANTS.items():
            if self.environment == cluster_name:
                return False

            if cluster_conf.get(
                "environments"
            ) and self.environment in cluster_conf.get("environments"):
                return True

        return None


class ByTenant(ArrangerMixin):
    def __init__(self, tenant: str, **kwargs: Dict[str, Any]):
        from arranger_automation.log import Log

        self.log = Log().logger(desc=self.__class__.__name__)
        self.tenant = tenant
        self.kwargs = kwargs

        if kwargs.get("config"):
            self.config = kwargs.get("config")
