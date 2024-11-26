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


class AuthorizationPolicy(
    cdk8s.ApiObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="securityistioioauthorizationpolicy.AuthorizationPolicy",
):
    """
    :schema: AuthorizationPolicy
    """

    def __init__(
        self,
        scope: constructs.Construct,
        name: builtins.str,
        *,
        spec: typing.Optional["AuthorizationPolicySpec"] = None,
    ) -> None:
        """Defines a "AuthorizationPolicy" API object.

        :param scope: the scope in which to define this object.
        :param name: a scope-local name for the object.
        :param spec: Configuration for access control on workloads. See more details at: https://istio.io/docs/reference/config/security/authorization-policy.html
        """
        options = AuthorizationPolicyOptions(spec=spec)

        jsii.create(AuthorizationPolicy, self, [scope, name, options])


@jsii.data_type(
    jsii_type="securityistioioauthorizationpolicy.AuthorizationPolicyOptions",
    jsii_struct_bases=[],
    name_mapping={"spec": "spec"},
)
class AuthorizationPolicyOptions:
    def __init__(
        self,
        *,
        spec: typing.Optional["AuthorizationPolicySpec"] = None,
    ) -> None:
        """
        :param spec: Configuration for access control on workloads. See more details at: https://istio.io/docs/reference/config/security/authorization-policy.html

        :schema: AuthorizationPolicy
        """
        if isinstance(spec, dict):
            spec = AuthorizationPolicySpec(**spec)
        self._values: typing.Dict[str, typing.Any] = {}
        if spec is not None:
            self._values["spec"] = spec

    @builtins.property
    def spec(self) -> typing.Optional["AuthorizationPolicySpec"]:
        """Configuration for access control on workloads.

        See more details at: https://istio.io/docs/reference/config/security/authorization-policy.html

        :schema: AuthorizationPolicy#spec
        """
        result = self._values.get("spec")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuthorizationPolicyOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="securityistioioauthorizationpolicy.AuthorizationPolicySpec",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "provider": "provider",
        "rules": "rules",
        "selector": "selector",
    },
)
class AuthorizationPolicySpec:
    def __init__(
        self,
        *,
        action: typing.Optional["AuthorizationPolicySpecAction"] = None,
        provider: typing.Optional["AuthorizationPolicySpecProvider"] = None,
        rules: typing.Optional[typing.List["AuthorizationPolicySpecRules"]] = None,
        selector: typing.Optional["AuthorizationPolicySpecSelector"] = None,
    ) -> None:
        """Configuration for access control on workloads.

        See more details at: https://istio.io/docs/reference/config/security/authorization-policy.html

        :param action: Optional.
        :param provider: Specifies detailed configuration of the CUSTOM action.
        :param rules: Optional.
        :param selector: Optional.

        :schema: AuthorizationPolicySpec
        """
        if isinstance(provider, dict):
            provider = AuthorizationPolicySpecProvider(**provider)
        if isinstance(selector, dict):
            selector = AuthorizationPolicySpecSelector(**selector)
        self._values: typing.Dict[str, typing.Any] = {}
        if action is not None:
            self._values["action"] = action
        if provider is not None:
            self._values["provider"] = provider
        if rules is not None:
            self._values["rules"] = rules
        if selector is not None:
            self._values["selector"] = selector

    @builtins.property
    def action(self) -> typing.Optional["AuthorizationPolicySpecAction"]:
        """Optional.

        :schema: AuthorizationPolicySpec#action
        """
        result = self._values.get("action")
        return result

    @builtins.property
    def provider(self) -> typing.Optional["AuthorizationPolicySpecProvider"]:
        """Specifies detailed configuration of the CUSTOM action.

        :schema: AuthorizationPolicySpec#provider
        """
        result = self._values.get("provider")
        return result

    @builtins.property
    def rules(self) -> typing.Optional[typing.List["AuthorizationPolicySpecRules"]]:
        """Optional.

        :schema: AuthorizationPolicySpec#rules
        """
        result = self._values.get("rules")
        return result

    @builtins.property
    def selector(self) -> typing.Optional["AuthorizationPolicySpecSelector"]:
        """Optional.

        :schema: AuthorizationPolicySpec#selector
        """
        result = self._values.get("selector")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuthorizationPolicySpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="securityistioioauthorizationpolicy.AuthorizationPolicySpecAction"
)
class AuthorizationPolicySpecAction(enum.Enum):
    """Optional.

    :schema: AuthorizationPolicySpecAction
    """

    ALLOW = "ALLOW"
    """ALLOW."""
    DENY = "DENY"
    """DENY."""
    AUDIT = "AUDIT"
    """AUDIT."""
    CUSTOM = "CUSTOM"
    """CUSTOM."""


@jsii.data_type(
    jsii_type="securityistioioauthorizationpolicy.AuthorizationPolicySpecProvider",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class AuthorizationPolicySpecProvider:
    def __init__(self, *, name: typing.Optional[builtins.str] = None) -> None:
        """Specifies detailed configuration of the CUSTOM action.

        :param name: Specifies the name of the extension provider.

        :schema: AuthorizationPolicySpecProvider
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        """Specifies the name of the extension provider.

        :schema: AuthorizationPolicySpecProvider#name
        """
        result = self._values.get("name")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuthorizationPolicySpecProvider(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="securityistioioauthorizationpolicy.AuthorizationPolicySpecRules",
    jsii_struct_bases=[],
    name_mapping={"from_": "from", "to": "to", "when": "when"},
)
class AuthorizationPolicySpecRules:
    def __init__(
        self,
        *,
        from_: typing.Optional[typing.List["AuthorizationPolicySpecRulesFrom"]] = None,
        to: typing.Optional[typing.List["AuthorizationPolicySpecRulesTo"]] = None,
        when: typing.Optional[typing.List["AuthorizationPolicySpecRulesWhen"]] = None,
    ) -> None:
        """
        :param from_: Optional.
        :param to: Optional.
        :param when: Optional.

        :schema: AuthorizationPolicySpecRules
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if from_ is not None:
            self._values["from_"] = from_
        if to is not None:
            self._values["to"] = to
        if when is not None:
            self._values["when"] = when

    @builtins.property
    def from_(self) -> typing.Optional[typing.List["AuthorizationPolicySpecRulesFrom"]]:
        """Optional.

        :schema: AuthorizationPolicySpecRules#from
        """
        result = self._values.get("from_")
        return result

    @builtins.property
    def to(self) -> typing.Optional[typing.List["AuthorizationPolicySpecRulesTo"]]:
        """Optional.

        :schema: AuthorizationPolicySpecRules#to
        """
        result = self._values.get("to")
        return result

    @builtins.property
    def when(self) -> typing.Optional[typing.List["AuthorizationPolicySpecRulesWhen"]]:
        """Optional.

        :schema: AuthorizationPolicySpecRules#when
        """
        result = self._values.get("when")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuthorizationPolicySpecRules(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="securityistioioauthorizationpolicy.AuthorizationPolicySpecRulesFrom",
    jsii_struct_bases=[],
    name_mapping={"source": "source"},
)
class AuthorizationPolicySpecRulesFrom:
    def __init__(
        self,
        *,
        source: typing.Optional["AuthorizationPolicySpecRulesFromSource"] = None,
    ) -> None:
        """
        :param source: Source specifies the source of a request.

        :schema: AuthorizationPolicySpecRulesFrom
        """
        if isinstance(source, dict):
            source = AuthorizationPolicySpecRulesFromSource(**source)
        self._values: typing.Dict[str, typing.Any] = {}
        if source is not None:
            self._values["source"] = source

    @builtins.property
    def source(self) -> typing.Optional["AuthorizationPolicySpecRulesFromSource"]:
        """Source specifies the source of a request.

        :schema: AuthorizationPolicySpecRulesFrom#source
        """
        result = self._values.get("source")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuthorizationPolicySpecRulesFrom(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="securityistioioauthorizationpolicy.AuthorizationPolicySpecRulesFromSource",
    jsii_struct_bases=[],
    name_mapping={
        "ip_blocks": "ipBlocks",
        "namespaces": "namespaces",
        "not_ip_blocks": "notIpBlocks",
        "not_namespaces": "notNamespaces",
        "not_principals": "notPrincipals",
        "not_remote_ip_blocks": "notRemoteIpBlocks",
        "not_request_principals": "notRequestPrincipals",
        "principals": "principals",
        "remote_ip_blocks": "remoteIpBlocks",
        "request_principals": "requestPrincipals",
    },
)
class AuthorizationPolicySpecRulesFromSource:
    def __init__(
        self,
        *,
        ip_blocks: typing.Optional[typing.List[builtins.str]] = None,
        namespaces: typing.Optional[typing.List[builtins.str]] = None,
        not_ip_blocks: typing.Optional[typing.List[builtins.str]] = None,
        not_namespaces: typing.Optional[typing.List[builtins.str]] = None,
        not_principals: typing.Optional[typing.List[builtins.str]] = None,
        not_remote_ip_blocks: typing.Optional[typing.List[builtins.str]] = None,
        not_request_principals: typing.Optional[typing.List[builtins.str]] = None,
        principals: typing.Optional[typing.List[builtins.str]] = None,
        remote_ip_blocks: typing.Optional[typing.List[builtins.str]] = None,
        request_principals: typing.Optional[typing.List[builtins.str]] = None,
    ) -> None:
        """Source specifies the source of a request.

        :param ip_blocks: Optional.
        :param namespaces: Optional.
        :param not_ip_blocks: Optional.
        :param not_namespaces: Optional.
        :param not_principals: Optional.
        :param not_remote_ip_blocks: Optional.
        :param not_request_principals: Optional.
        :param principals: Optional.
        :param remote_ip_blocks: Optional.
        :param request_principals: Optional.

        :schema: AuthorizationPolicySpecRulesFromSource
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if ip_blocks is not None:
            self._values["ip_blocks"] = ip_blocks
        if namespaces is not None:
            self._values["namespaces"] = namespaces
        if not_ip_blocks is not None:
            self._values["not_ip_blocks"] = not_ip_blocks
        if not_namespaces is not None:
            self._values["not_namespaces"] = not_namespaces
        if not_principals is not None:
            self._values["not_principals"] = not_principals
        if not_remote_ip_blocks is not None:
            self._values["not_remote_ip_blocks"] = not_remote_ip_blocks
        if not_request_principals is not None:
            self._values["not_request_principals"] = not_request_principals
        if principals is not None:
            self._values["principals"] = principals
        if remote_ip_blocks is not None:
            self._values["remote_ip_blocks"] = remote_ip_blocks
        if request_principals is not None:
            self._values["request_principals"] = request_principals

    @builtins.property
    def ip_blocks(self) -> typing.Optional[typing.List[builtins.str]]:
        """Optional.

        :schema: AuthorizationPolicySpecRulesFromSource#ipBlocks
        """
        result = self._values.get("ip_blocks")
        return result

    @builtins.property
    def namespaces(self) -> typing.Optional[typing.List[builtins.str]]:
        """Optional.

        :schema: AuthorizationPolicySpecRulesFromSource#namespaces
        """
        result = self._values.get("namespaces")
        return result

    @builtins.property
    def not_ip_blocks(self) -> typing.Optional[typing.List[builtins.str]]:
        """Optional.

        :schema: AuthorizationPolicySpecRulesFromSource#notIpBlocks
        """
        result = self._values.get("not_ip_blocks")
        return result

    @builtins.property
    def not_namespaces(self) -> typing.Optional[typing.List[builtins.str]]:
        """Optional.

        :schema: AuthorizationPolicySpecRulesFromSource#notNamespaces
        """
        result = self._values.get("not_namespaces")
        return result

    @builtins.property
    def not_principals(self) -> typing.Optional[typing.List[builtins.str]]:
        """Optional.

        :schema: AuthorizationPolicySpecRulesFromSource#notPrincipals
        """
        result = self._values.get("not_principals")
        return result

    @builtins.property
    def not_remote_ip_blocks(self) -> typing.Optional[typing.List[builtins.str]]:
        """Optional.

        :schema: AuthorizationPolicySpecRulesFromSource#notRemoteIpBlocks
        """
        result = self._values.get("not_remote_ip_blocks")
        return result

    @builtins.property
    def not_request_principals(self) -> typing.Optional[typing.List[builtins.str]]:
        """Optional.

        :schema: AuthorizationPolicySpecRulesFromSource#notRequestPrincipals
        """
        result = self._values.get("not_request_principals")
        return result

    @builtins.property
    def principals(self) -> typing.Optional[typing.List[builtins.str]]:
        """Optional.

        :schema: AuthorizationPolicySpecRulesFromSource#principals
        """
        result = self._values.get("principals")
        return result

    @builtins.property
    def remote_ip_blocks(self) -> typing.Optional[typing.List[builtins.str]]:
        """Optional.

        :schema: AuthorizationPolicySpecRulesFromSource#remoteIpBlocks
        """
        result = self._values.get("remote_ip_blocks")
        return result

    @builtins.property
    def request_principals(self) -> typing.Optional[typing.List[builtins.str]]:
        """Optional.

        :schema: AuthorizationPolicySpecRulesFromSource#requestPrincipals
        """
        result = self._values.get("request_principals")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuthorizationPolicySpecRulesFromSource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="securityistioioauthorizationpolicy.AuthorizationPolicySpecRulesTo",
    jsii_struct_bases=[],
    name_mapping={"operation": "operation"},
)
class AuthorizationPolicySpecRulesTo:
    def __init__(
        self,
        *,
        operation: typing.Optional["AuthorizationPolicySpecRulesToOperation"] = None,
    ) -> None:
        """
        :param operation: Operation specifies the operation of a request.

        :schema: AuthorizationPolicySpecRulesTo
        """
        if isinstance(operation, dict):
            operation = AuthorizationPolicySpecRulesToOperation(**operation)
        self._values: typing.Dict[str, typing.Any] = {}
        if operation is not None:
            self._values["operation"] = operation

    @builtins.property
    def operation(self) -> typing.Optional["AuthorizationPolicySpecRulesToOperation"]:
        """Operation specifies the operation of a request.

        :schema: AuthorizationPolicySpecRulesTo#operation
        """
        result = self._values.get("operation")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuthorizationPolicySpecRulesTo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="securityistioioauthorizationpolicy.AuthorizationPolicySpecRulesToOperation",
    jsii_struct_bases=[],
    name_mapping={
        "hosts": "hosts",
        "methods": "methods",
        "not_hosts": "notHosts",
        "not_methods": "notMethods",
        "not_paths": "notPaths",
        "not_ports": "notPorts",
        "paths": "paths",
        "ports": "ports",
    },
)
class AuthorizationPolicySpecRulesToOperation:
    def __init__(
        self,
        *,
        hosts: typing.Optional[typing.List[builtins.str]] = None,
        methods: typing.Optional[typing.List[builtins.str]] = None,
        not_hosts: typing.Optional[typing.List[builtins.str]] = None,
        not_methods: typing.Optional[typing.List[builtins.str]] = None,
        not_paths: typing.Optional[typing.List[builtins.str]] = None,
        not_ports: typing.Optional[typing.List[builtins.str]] = None,
        paths: typing.Optional[typing.List[builtins.str]] = None,
        ports: typing.Optional[typing.List[builtins.str]] = None,
    ) -> None:
        """Operation specifies the operation of a request.

        :param hosts: Optional.
        :param methods: Optional.
        :param not_hosts: Optional.
        :param not_methods: Optional.
        :param not_paths: Optional.
        :param not_ports: Optional.
        :param paths: Optional.
        :param ports: Optional.

        :schema: AuthorizationPolicySpecRulesToOperation
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if hosts is not None:
            self._values["hosts"] = hosts
        if methods is not None:
            self._values["methods"] = methods
        if not_hosts is not None:
            self._values["not_hosts"] = not_hosts
        if not_methods is not None:
            self._values["not_methods"] = not_methods
        if not_paths is not None:
            self._values["not_paths"] = not_paths
        if not_ports is not None:
            self._values["not_ports"] = not_ports
        if paths is not None:
            self._values["paths"] = paths
        if ports is not None:
            self._values["ports"] = ports

    @builtins.property
    def hosts(self) -> typing.Optional[typing.List[builtins.str]]:
        """Optional.

        :schema: AuthorizationPolicySpecRulesToOperation#hosts
        """
        result = self._values.get("hosts")
        return result

    @builtins.property
    def methods(self) -> typing.Optional[typing.List[builtins.str]]:
        """Optional.

        :schema: AuthorizationPolicySpecRulesToOperation#methods
        """
        result = self._values.get("methods")
        return result

    @builtins.property
    def not_hosts(self) -> typing.Optional[typing.List[builtins.str]]:
        """Optional.

        :schema: AuthorizationPolicySpecRulesToOperation#notHosts
        """
        result = self._values.get("not_hosts")
        return result

    @builtins.property
    def not_methods(self) -> typing.Optional[typing.List[builtins.str]]:
        """Optional.

        :schema: AuthorizationPolicySpecRulesToOperation#notMethods
        """
        result = self._values.get("not_methods")
        return result

    @builtins.property
    def not_paths(self) -> typing.Optional[typing.List[builtins.str]]:
        """Optional.

        :schema: AuthorizationPolicySpecRulesToOperation#notPaths
        """
        result = self._values.get("not_paths")
        return result

    @builtins.property
    def not_ports(self) -> typing.Optional[typing.List[builtins.str]]:
        """Optional.

        :schema: AuthorizationPolicySpecRulesToOperation#notPorts
        """
        result = self._values.get("not_ports")
        return result

    @builtins.property
    def paths(self) -> typing.Optional[typing.List[builtins.str]]:
        """Optional.

        :schema: AuthorizationPolicySpecRulesToOperation#paths
        """
        result = self._values.get("paths")
        return result

    @builtins.property
    def ports(self) -> typing.Optional[typing.List[builtins.str]]:
        """Optional.

        :schema: AuthorizationPolicySpecRulesToOperation#ports
        """
        result = self._values.get("ports")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuthorizationPolicySpecRulesToOperation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="securityistioioauthorizationpolicy.AuthorizationPolicySpecRulesWhen",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "not_values": "notValues", "values": "values"},
)
class AuthorizationPolicySpecRulesWhen:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        not_values: typing.Optional[typing.List[builtins.str]] = None,
        values: typing.Optional[typing.List[builtins.str]] = None,
    ) -> None:
        """
        :param key: The name of an Istio attribute.
        :param not_values: Optional.
        :param values: Optional.

        :schema: AuthorizationPolicySpecRulesWhen
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if not_values is not None:
            self._values["not_values"] = not_values
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        """The name of an Istio attribute.

        :schema: AuthorizationPolicySpecRulesWhen#key
        """
        result = self._values.get("key")
        return result

    @builtins.property
    def not_values(self) -> typing.Optional[typing.List[builtins.str]]:
        """Optional.

        :schema: AuthorizationPolicySpecRulesWhen#notValues
        """
        result = self._values.get("not_values")
        return result

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        """Optional.

        :schema: AuthorizationPolicySpecRulesWhen#values
        """
        result = self._values.get("values")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuthorizationPolicySpecRulesWhen(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="securityistioioauthorizationpolicy.AuthorizationPolicySpecSelector",
    jsii_struct_bases=[],
    name_mapping={"match_labels": "matchLabels"},
)
class AuthorizationPolicySpecSelector:
    def __init__(
        self,
        *,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        """Optional.

        :param match_labels: 

        :schema: AuthorizationPolicySpecSelector
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if match_labels is not None:
            self._values["match_labels"] = match_labels

    @builtins.property
    def match_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """
        :schema: AuthorizationPolicySpecSelector#matchLabels
        """
        result = self._values.get("match_labels")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuthorizationPolicySpecSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AuthorizationPolicy",
    "AuthorizationPolicyOptions",
    "AuthorizationPolicySpec",
    "AuthorizationPolicySpecAction",
    "AuthorizationPolicySpecProvider",
    "AuthorizationPolicySpecRules",
    "AuthorizationPolicySpecRulesFrom",
    "AuthorizationPolicySpecRulesFromSource",
    "AuthorizationPolicySpecRulesTo",
    "AuthorizationPolicySpecRulesToOperation",
    "AuthorizationPolicySpecRulesWhen",
    "AuthorizationPolicySpecSelector",
]

publication.publish()
