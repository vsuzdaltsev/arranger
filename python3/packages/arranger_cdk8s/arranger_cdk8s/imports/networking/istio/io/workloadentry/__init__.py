import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from ._jsii import *

import cdk8s
import constructs


class WorkloadEntry(
    cdk8s.ApiObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="networkingistioioworkloadentry.WorkloadEntry",
):
    """
    :schema: WorkloadEntry
    """

    def __init__(
        self,
        scope: constructs.Construct,
        name: builtins.str,
        *,
        spec: typing.Optional["WorkloadEntrySpec"] = None,
    ) -> None:
        """Defines a "WorkloadEntry" API object.

        :param scope: the scope in which to define this object.
        :param name: a scope-local name for the object.
        :param spec: Configuration affecting VMs onboarded into the mesh. See more details at: https://istio.io/docs/reference/config/networking/workload-entry.html
        """
        options = WorkloadEntryOptions(spec=spec)

        jsii.create(WorkloadEntry, self, [scope, name, options])


@jsii.data_type(
    jsii_type="networkingistioioworkloadentry.WorkloadEntryOptions",
    jsii_struct_bases=[],
    name_mapping={"spec": "spec"},
)
class WorkloadEntryOptions:
    def __init__(self, *, spec: typing.Optional["WorkloadEntrySpec"] = None) -> None:
        """
        :param spec: Configuration affecting VMs onboarded into the mesh. See more details at: https://istio.io/docs/reference/config/networking/workload-entry.html

        :schema: WorkloadEntry
        """
        if isinstance(spec, dict):
            spec = WorkloadEntrySpec(**spec)
        self._values: typing.Dict[str, typing.Any] = {}
        if spec is not None:
            self._values["spec"] = spec

    @builtins.property
    def spec(self) -> typing.Optional["WorkloadEntrySpec"]:
        """Configuration affecting VMs onboarded into the mesh.

        See more details at: https://istio.io/docs/reference/config/networking/workload-entry.html

        :schema: WorkloadEntry#spec
        """
        result = self._values.get("spec")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkloadEntryOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioioworkloadentry.WorkloadEntrySpec",
    jsii_struct_bases=[],
    name_mapping={
        "address": "address",
        "labels": "labels",
        "locality": "locality",
        "network": "network",
        "ports": "ports",
        "service_account": "serviceAccount",
        "weight": "weight",
    },
)
class WorkloadEntrySpec:
    def __init__(
        self,
        *,
        address: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        locality: typing.Optional[builtins.str] = None,
        network: typing.Optional[builtins.str] = None,
        ports: typing.Optional[typing.Mapping[builtins.str, jsii.Number]] = None,
        service_account: typing.Optional[builtins.str] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        """Configuration affecting VMs onboarded into the mesh.

        See more details at: https://istio.io/docs/reference/config/networking/workload-entry.html

        :param address: 
        :param labels: One or more labels associated with the endpoint.
        :param locality: The locality associated with the endpoint.
        :param network: 
        :param ports: Set of ports associated with the endpoint.
        :param service_account: 
        :param weight: The load balancing weight associated with the endpoint.

        :schema: WorkloadEntrySpec
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if address is not None:
            self._values["address"] = address
        if labels is not None:
            self._values["labels"] = labels
        if locality is not None:
            self._values["locality"] = locality
        if network is not None:
            self._values["network"] = network
        if ports is not None:
            self._values["ports"] = ports
        if service_account is not None:
            self._values["service_account"] = service_account
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def address(self) -> typing.Optional[builtins.str]:
        """
        :schema: WorkloadEntrySpec#address
        """
        result = self._values.get("address")
        return result

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """One or more labels associated with the endpoint.

        :schema: WorkloadEntrySpec#labels
        """
        result = self._values.get("labels")
        return result

    @builtins.property
    def locality(self) -> typing.Optional[builtins.str]:
        """The locality associated with the endpoint.

        :schema: WorkloadEntrySpec#locality
        """
        result = self._values.get("locality")
        return result

    @builtins.property
    def network(self) -> typing.Optional[builtins.str]:
        """
        :schema: WorkloadEntrySpec#network
        """
        result = self._values.get("network")
        return result

    @builtins.property
    def ports(self) -> typing.Optional[typing.Mapping[builtins.str, jsii.Number]]:
        """Set of ports associated with the endpoint.

        :schema: WorkloadEntrySpec#ports
        """
        result = self._values.get("ports")
        return result

    @builtins.property
    def service_account(self) -> typing.Optional[builtins.str]:
        """
        :schema: WorkloadEntrySpec#serviceAccount
        """
        result = self._values.get("service_account")
        return result

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        """The load balancing weight associated with the endpoint.

        :schema: WorkloadEntrySpec#weight
        """
        result = self._values.get("weight")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkloadEntrySpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "WorkloadEntry",
    "WorkloadEntryOptions",
    "WorkloadEntrySpec",
]

publication.publish()
