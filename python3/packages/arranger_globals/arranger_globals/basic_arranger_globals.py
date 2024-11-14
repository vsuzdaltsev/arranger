"""Global functions. Basic classes."""

from abc import ABC
import ipaddress
from typing import Callable, Dict


class NotIPv4Error(Exception):
    pass


def validate_subnets(func: Callable) -> Callable:
    def check(*args):
        from arranger_automation.validate import ValidateSubnets

        return ValidateSubnets(ranges=func(*args)).validate()

    return check


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


class BySubEnvironment(ArrangerMixin):
    def __init__(self, sub_environment: str, **kwargs: Dict):
        from arranger_automation.log import Log

        self.log = Log().logger(desc=self.__class__.__name__)
        self.sub_environment = sub_environment
        self.kwargs = kwargs

        if kwargs.get("config"):
            self.config = kwargs.get("config")


class ByTenant(ArrangerMixin):
    def __init__(self, tenant: str, **kwargs: Dict):
        from arranger_automation.log import Log

        self.log = Log().logger(desc=self.__class__.__name__)
        self.tenant = tenant
        self.kwargs = kwargs

        if kwargs.get("config"):
            self.config = kwargs.get("config")
