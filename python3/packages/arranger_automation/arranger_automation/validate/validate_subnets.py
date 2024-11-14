import ipaddress
from typing import Dict, List

from arranger_automation.log import Log


class InvalidSubnet(Exception):
    pass


class ValidateSubnets:
    def __init__(self, ranges: Dict):
        self.log = Log().logger(desc=self.__class__.__name__)
        self.ranges = ranges
        self.subnets_by_vnets = {}

    @staticmethod
    def _is_subnet(vnet_cidr: str, subnet_cidr: str) -> bool:
        vnet = ipaddress.IPv4Network(vnet_cidr)
        subnet = ipaddress.IPv4Network(subnet_cidr)

        return subnet.subnet_of(vnet)

    def _vnet_ranges(self, vnet_name: str) -> List[str]:
        return self.ranges[vnet_name]["cidr"]

    def _vnet_subnets(self, vnet_name: str) -> List[str]:
        subnets = []
        subnets_metadata = self.ranges[vnet_name].get("subnets")

        if subnets_metadata:
            for subnet_name in subnets_metadata:
                if subnet_name:
                    subnets.append(subnet_name)

        return subnets

    def _subnet_cidrs(self, vnet_name: str) -> List[str]:
        return [
            self.ranges[vnet_name]["subnets"][subnet_name]["cidr"]
            for subnet_name in self._vnet_subnets(vnet_name=vnet_name)
        ]

    def _subnet_cidrs_flattened(self, vnet_name: str) -> List[str]:
        return [
            vnet_name
            for sublist in self._subnet_cidrs(vnet_name=vnet_name)
            for vnet_name in sublist
        ]

    def _validate_vnet(self, vnet_name: str) -> None:
        subnets_by_vnet = {}
        for vnet_cidr in self._vnet_ranges(vnet_name=vnet_name):
            vnet_cidrs = {}

            for subnet_cidr in self._subnet_cidrs_flattened(vnet_name=vnet_name):
                _subnet_cidr_is_subnet = self._subnet_cidr_is_subnet(
                    subnet_cidr, vnet_cidr
                )

                if vnet_cidrs.get(vnet_cidr):
                    vnet_cidrs[vnet_cidr].update(_subnet_cidr_is_subnet)
                else:
                    vnet_cidrs.update({vnet_cidr: _subnet_cidr_is_subnet})

                subnets_by_vnet.update(vnet_cidrs)
        self.subnets_by_vnets.update(subnets_by_vnet)

    def _subnet_cidr_is_subnet(self, subnet_cidr: str, vnet_cidr: str) -> Dict:
        return {
            subnet_cidr: self._is_subnet(vnet_cidr=vnet_cidr, subnet_cidr=subnet_cidr)
        }

    def _validation_struct(self) -> Dict:
        if self.ranges:
            for vnet_name in self.ranges:
                self._validate_vnet(vnet_name)

        return self.subnets_by_vnets

    def validate(self) -> Dict:
        not_subnets = []
        subnets = []

        for vnet in self._validation_struct().items():
            for subnet in vnet[1].items():
                if subnet[1] is True:
                    subnets.append(subnet[0])
                else:
                    not_subnets.append(subnet[0])

        not_subnets = list(set(not_subnets) - set(subnets))

        self.log.debug(f">> Valid subnets: subnets. Invalid subnets: {not_subnets}.")

        if not_subnets:
            raise InvalidSubnet(
                f">> The {not_subnets} subnets are not valid subnets "
                f"for {list(self._validation_struct().keys())} supernets."
            )

        return self.ranges


if __name__ == "__main__":
    import json

    from arranger_conf.arranger_conf import ArrangerConf
    from arranger_globals import CdktfGlobals

    aggr = {}
    for tenant in sorted(AppConf.TENANTS.keys()):
        _globals = CdktfGlobals(tenant=tenant)

        aggr.update({tenant: ValidateSubnets(ranges=_globals.ip_ranges).validate()})

    print(json.dumps(aggr))
