"""Global functions. Basic classes."""

from abc import ABC
import ipaddress


class NotIPv4Error(Exception):
    pass


def validate_subnets(func):
    def check(*args):
        from arranger_automation.validate import ValidateSubnets

        return ValidateSubnets(ranges=func(*args)).validate()

    return check


def validate_ipv4(func):
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


class BySubEnvironment(ArrangerMixin):
    pass


class ByTenant(ArrangerMixin):
    pass
