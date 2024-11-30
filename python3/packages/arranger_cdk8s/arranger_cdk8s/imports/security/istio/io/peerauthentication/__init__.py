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


class PeerAuthentication(
    cdk8s.ApiObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="securityistioiopeerauthentication.PeerAuthentication",
):
    """
    :schema: PeerAuthentication
    """

    def __init__(
        self,
        scope: constructs.Construct,
        name: builtins.str,
        *,
        spec: typing.Optional["PeerAuthenticationSpec"] = None,
    ) -> None:
        """Defines a "PeerAuthentication" API object.

        :param scope: the scope in which to define this object.
        :param name: a scope-local name for the object.
        :param spec: PeerAuthentication defines how traffic will be tunneled (or not) to the sidecar.
        """
        options = PeerAuthenticationOptions(spec=spec)

        jsii.create(PeerAuthentication, self, [scope, name, options])


@jsii.data_type(
    jsii_type="securityistioiopeerauthentication.PeerAuthenticationOptions",
    jsii_struct_bases=[],
    name_mapping={"spec": "spec"},
)
class PeerAuthenticationOptions:
    def __init__(
        self,
        *,
        spec: typing.Optional["PeerAuthenticationSpec"] = None,
    ) -> None:
        """
        :param spec: PeerAuthentication defines how traffic will be tunneled (or not) to the sidecar.

        :schema: PeerAuthentication
        """
        if isinstance(spec, dict):
            spec = PeerAuthenticationSpec(**spec)
        self._values: typing.Dict[str, typing.Any] = {}
        if spec is not None:
            self._values["spec"] = spec

    @builtins.property
    def spec(self) -> typing.Optional["PeerAuthenticationSpec"]:
        """PeerAuthentication defines how traffic will be tunneled (or not) to the sidecar.

        :schema: PeerAuthentication#spec
        """
        result = self._values.get("spec")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PeerAuthenticationOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="securityistioiopeerauthentication.PeerAuthenticationSpec",
    jsii_struct_bases=[],
    name_mapping={
        "mtls": "mtls",
        "port_level_mtls": "portLevelMtls",
        "selector": "selector",
    },
)
class PeerAuthenticationSpec:
    def __init__(
        self,
        *,
        mtls: typing.Optional["PeerAuthenticationSpecMtls"] = None,
        port_level_mtls: typing.Optional[typing.Mapping[builtins.str, "PeerAuthenticationSpecPortLevelMtls"]] = None,
        selector: typing.Optional["PeerAuthenticationSpecSelector"] = None,
    ) -> None:
        """PeerAuthentication defines how traffic will be tunneled (or not) to the sidecar.

        :param mtls: Mutual TLS settings for workload.
        :param port_level_mtls: Port specific mutual TLS settings.
        :param selector: The selector determines the workloads to apply the ChannelAuthentication on.

        :schema: PeerAuthenticationSpec
        """
        if isinstance(mtls, dict):
            mtls = PeerAuthenticationSpecMtls(**mtls)
        if isinstance(selector, dict):
            selector = PeerAuthenticationSpecSelector(**selector)
        self._values: typing.Dict[str, typing.Any] = {}
        if mtls is not None:
            self._values["mtls"] = mtls
        if port_level_mtls is not None:
            self._values["port_level_mtls"] = port_level_mtls
        if selector is not None:
            self._values["selector"] = selector

    @builtins.property
    def mtls(self) -> typing.Optional["PeerAuthenticationSpecMtls"]:
        """Mutual TLS settings for workload.

        :schema: PeerAuthenticationSpec#mtls
        """
        result = self._values.get("mtls")
        return result

    @builtins.property
    def port_level_mtls(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, "PeerAuthenticationSpecPortLevelMtls"]]:
        """Port specific mutual TLS settings.

        :schema: PeerAuthenticationSpec#portLevelMtls
        """
        result = self._values.get("port_level_mtls")
        return result

    @builtins.property
    def selector(self) -> typing.Optional["PeerAuthenticationSpecSelector"]:
        """The selector determines the workloads to apply the ChannelAuthentication on.

        :schema: PeerAuthenticationSpec#selector
        """
        result = self._values.get("selector")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PeerAuthenticationSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="securityistioiopeerauthentication.PeerAuthenticationSpecMtls",
    jsii_struct_bases=[],
    name_mapping={"mode": "mode"},
)
class PeerAuthenticationSpecMtls:
    def __init__(
        self,
        *,
        mode: typing.Optional["PeerAuthenticationSpecMtlsMode"] = None,
    ) -> None:
        """Mutual TLS settings for workload.

        :param mode: Defines the mTLS mode used for peer authentication.

        :schema: PeerAuthenticationSpecMtls
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if mode is not None:
            self._values["mode"] = mode

    @builtins.property
    def mode(self) -> typing.Optional["PeerAuthenticationSpecMtlsMode"]:
        """Defines the mTLS mode used for peer authentication.

        :schema: PeerAuthenticationSpecMtls#mode
        """
        result = self._values.get("mode")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PeerAuthenticationSpecMtls(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="securityistioiopeerauthentication.PeerAuthenticationSpecMtlsMode"
)
class PeerAuthenticationSpecMtlsMode(enum.Enum):
    """Defines the mTLS mode used for peer authentication.

    :schema: PeerAuthenticationSpecMtlsMode
    """

    UNSET = "UNSET"
    """UNSET."""
    DISABLE = "DISABLE"
    """DISABLE."""
    PERMISSIVE = "PERMISSIVE"
    """PERMISSIVE."""
    STRICT = "STRICT"
    """STRICT."""


@jsii.data_type(
    jsii_type="securityistioiopeerauthentication.PeerAuthenticationSpecPortLevelMtls",
    jsii_struct_bases=[],
    name_mapping={"mode": "mode"},
)
class PeerAuthenticationSpecPortLevelMtls:
    def __init__(
        self,
        *,
        mode: typing.Optional["PeerAuthenticationSpecPortLevelMtlsMode"] = None,
    ) -> None:
        """
        :param mode: Defines the mTLS mode used for peer authentication.

        :schema: PeerAuthenticationSpecPortLevelMtls
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if mode is not None:
            self._values["mode"] = mode

    @builtins.property
    def mode(self) -> typing.Optional["PeerAuthenticationSpecPortLevelMtlsMode"]:
        """Defines the mTLS mode used for peer authentication.

        :schema: PeerAuthenticationSpecPortLevelMtls#mode
        """
        result = self._values.get("mode")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PeerAuthenticationSpecPortLevelMtls(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="securityistioiopeerauthentication.PeerAuthenticationSpecPortLevelMtlsMode"
)
class PeerAuthenticationSpecPortLevelMtlsMode(enum.Enum):
    """Defines the mTLS mode used for peer authentication.

    :schema: PeerAuthenticationSpecPortLevelMtlsMode
    """

    UNSET = "UNSET"
    """UNSET."""
    DISABLE = "DISABLE"
    """DISABLE."""
    PERMISSIVE = "PERMISSIVE"
    """PERMISSIVE."""
    STRICT = "STRICT"
    """STRICT."""


@jsii.data_type(
    jsii_type="securityistioiopeerauthentication.PeerAuthenticationSpecSelector",
    jsii_struct_bases=[],
    name_mapping={"match_labels": "matchLabels"},
)
class PeerAuthenticationSpecSelector:
    def __init__(
        self,
        *,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        """The selector determines the workloads to apply the ChannelAuthentication on.

        :param match_labels: 

        :schema: PeerAuthenticationSpecSelector
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if match_labels is not None:
            self._values["match_labels"] = match_labels

    @builtins.property
    def match_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """
        :schema: PeerAuthenticationSpecSelector#matchLabels
        """
        result = self._values.get("match_labels")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PeerAuthenticationSpecSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "PeerAuthentication",
    "PeerAuthenticationOptions",
    "PeerAuthenticationSpec",
    "PeerAuthenticationSpecMtls",
    "PeerAuthenticationSpecMtlsMode",
    "PeerAuthenticationSpecPortLevelMtls",
    "PeerAuthenticationSpecPortLevelMtlsMode",
    "PeerAuthenticationSpecSelector",
]

publication.publish()
