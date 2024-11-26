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


class RequestAuthentication(
    cdk8s.ApiObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="securityistioiorequestauthentication.RequestAuthentication",
):
    """
    :schema: RequestAuthentication
    """

    def __init__(
        self,
        scope: constructs.Construct,
        name: builtins.str,
        *,
        spec: typing.Optional["RequestAuthenticationSpec"] = None,
    ) -> None:
        """Defines a "RequestAuthentication" API object.

        :param scope: the scope in which to define this object.
        :param name: a scope-local name for the object.
        :param spec: RequestAuthentication defines what request authentication methods are supported by a workload.
        """
        options = RequestAuthenticationOptions(spec=spec)

        jsii.create(RequestAuthentication, self, [scope, name, options])


@jsii.data_type(
    jsii_type="securityistioiorequestauthentication.RequestAuthenticationOptions",
    jsii_struct_bases=[],
    name_mapping={"spec": "spec"},
)
class RequestAuthenticationOptions:
    def __init__(
        self,
        *,
        spec: typing.Optional["RequestAuthenticationSpec"] = None,
    ) -> None:
        """
        :param spec: RequestAuthentication defines what request authentication methods are supported by a workload.

        :schema: RequestAuthentication
        """
        if isinstance(spec, dict):
            spec = RequestAuthenticationSpec(**spec)
        self._values: typing.Dict[str, typing.Any] = {}
        if spec is not None:
            self._values["spec"] = spec

    @builtins.property
    def spec(self) -> typing.Optional["RequestAuthenticationSpec"]:
        """RequestAuthentication defines what request authentication methods are supported by a workload.

        :schema: RequestAuthentication#spec
        """
        result = self._values.get("spec")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RequestAuthenticationOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="securityistioiorequestauthentication.RequestAuthenticationSpec",
    jsii_struct_bases=[],
    name_mapping={"jwt_rules": "jwtRules", "selector": "selector"},
)
class RequestAuthenticationSpec:
    def __init__(
        self,
        *,
        jwt_rules: typing.Optional[typing.List["RequestAuthenticationSpecJwtRules"]] = None,
        selector: typing.Optional["RequestAuthenticationSpecSelector"] = None,
    ) -> None:
        """RequestAuthentication defines what request authentication methods are supported by a workload.

        :param jwt_rules: Define the list of JWTs that can be validated at the selected workloads' proxy.
        :param selector: The selector determines the workloads to apply the RequestAuthentication on.

        :schema: RequestAuthenticationSpec
        """
        if isinstance(selector, dict):
            selector = RequestAuthenticationSpecSelector(**selector)
        self._values: typing.Dict[str, typing.Any] = {}
        if jwt_rules is not None:
            self._values["jwt_rules"] = jwt_rules
        if selector is not None:
            self._values["selector"] = selector

    @builtins.property
    def jwt_rules(
        self,
    ) -> typing.Optional[typing.List["RequestAuthenticationSpecJwtRules"]]:
        """Define the list of JWTs that can be validated at the selected workloads' proxy.

        :schema: RequestAuthenticationSpec#jwtRules
        """
        result = self._values.get("jwt_rules")
        return result

    @builtins.property
    def selector(self) -> typing.Optional["RequestAuthenticationSpecSelector"]:
        """The selector determines the workloads to apply the RequestAuthentication on.

        :schema: RequestAuthenticationSpec#selector
        """
        result = self._values.get("selector")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RequestAuthenticationSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="securityistioiorequestauthentication.RequestAuthenticationSpecJwtRules",
    jsii_struct_bases=[],
    name_mapping={
        "audiences": "audiences",
        "forward_original_token": "forwardOriginalToken",
        "from_headers": "fromHeaders",
        "from_params": "fromParams",
        "issuer": "issuer",
        "jwks": "jwks",
        "jwks_uri": "jwksUri",
        "output_payload_to_header": "outputPayloadToHeader",
    },
)
class RequestAuthenticationSpecJwtRules:
    def __init__(
        self,
        *,
        audiences: typing.Optional[typing.List[builtins.str]] = None,
        forward_original_token: typing.Optional[builtins.bool] = None,
        from_headers: typing.Optional[typing.List["RequestAuthenticationSpecJwtRulesFromHeaders"]] = None,
        from_params: typing.Optional[typing.List[builtins.str]] = None,
        issuer: typing.Optional[builtins.str] = None,
        jwks: typing.Optional[builtins.str] = None,
        jwks_uri: typing.Optional[builtins.str] = None,
        output_payload_to_header: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param audiences: 
        :param forward_original_token: If set to true, the orginal token will be kept for the ustream request.
        :param from_headers: List of header locations from which JWT is expected.
        :param from_params: List of query parameters from which JWT is expected.
        :param issuer: Identifies the issuer that issued the JWT.
        :param jwks: JSON Web Key Set of public keys to validate signature of the JWT.
        :param jwks_uri: 
        :param output_payload_to_header: 

        :schema: RequestAuthenticationSpecJwtRules
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if audiences is not None:
            self._values["audiences"] = audiences
        if forward_original_token is not None:
            self._values["forward_original_token"] = forward_original_token
        if from_headers is not None:
            self._values["from_headers"] = from_headers
        if from_params is not None:
            self._values["from_params"] = from_params
        if issuer is not None:
            self._values["issuer"] = issuer
        if jwks is not None:
            self._values["jwks"] = jwks
        if jwks_uri is not None:
            self._values["jwks_uri"] = jwks_uri
        if output_payload_to_header is not None:
            self._values["output_payload_to_header"] = output_payload_to_header

    @builtins.property
    def audiences(self) -> typing.Optional[typing.List[builtins.str]]:
        """
        :schema: RequestAuthenticationSpecJwtRules#audiences
        """
        result = self._values.get("audiences")
        return result

    @builtins.property
    def forward_original_token(self) -> typing.Optional[builtins.bool]:
        """If set to true, the orginal token will be kept for the ustream request.

        :schema: RequestAuthenticationSpecJwtRules#forwardOriginalToken
        """
        result = self._values.get("forward_original_token")
        return result

    @builtins.property
    def from_headers(
        self,
    ) -> typing.Optional[typing.List["RequestAuthenticationSpecJwtRulesFromHeaders"]]:
        """List of header locations from which JWT is expected.

        :schema: RequestAuthenticationSpecJwtRules#fromHeaders
        """
        result = self._values.get("from_headers")
        return result

    @builtins.property
    def from_params(self) -> typing.Optional[typing.List[builtins.str]]:
        """List of query parameters from which JWT is expected.

        :schema: RequestAuthenticationSpecJwtRules#fromParams
        """
        result = self._values.get("from_params")
        return result

    @builtins.property
    def issuer(self) -> typing.Optional[builtins.str]:
        """Identifies the issuer that issued the JWT.

        :schema: RequestAuthenticationSpecJwtRules#issuer
        """
        result = self._values.get("issuer")
        return result

    @builtins.property
    def jwks(self) -> typing.Optional[builtins.str]:
        """JSON Web Key Set of public keys to validate signature of the JWT.

        :schema: RequestAuthenticationSpecJwtRules#jwks
        """
        result = self._values.get("jwks")
        return result

    @builtins.property
    def jwks_uri(self) -> typing.Optional[builtins.str]:
        """
        :schema: RequestAuthenticationSpecJwtRules#jwksUri
        """
        result = self._values.get("jwks_uri")
        return result

    @builtins.property
    def output_payload_to_header(self) -> typing.Optional[builtins.str]:
        """
        :schema: RequestAuthenticationSpecJwtRules#outputPayloadToHeader
        """
        result = self._values.get("output_payload_to_header")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RequestAuthenticationSpecJwtRules(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="securityistioiorequestauthentication.RequestAuthenticationSpecJwtRulesFromHeaders",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "prefix": "prefix"},
)
class RequestAuthenticationSpecJwtRulesFromHeaders:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param name: The HTTP header name.
        :param prefix: The prefix that should be stripped before decoding the token.

        :schema: RequestAuthenticationSpecJwtRulesFromHeaders
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if prefix is not None:
            self._values["prefix"] = prefix

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        """The HTTP header name.

        :schema: RequestAuthenticationSpecJwtRulesFromHeaders#name
        """
        result = self._values.get("name")
        return result

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        """The prefix that should be stripped before decoding the token.

        :schema: RequestAuthenticationSpecJwtRulesFromHeaders#prefix
        """
        result = self._values.get("prefix")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RequestAuthenticationSpecJwtRulesFromHeaders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="securityistioiorequestauthentication.RequestAuthenticationSpecSelector",
    jsii_struct_bases=[],
    name_mapping={"match_labels": "matchLabels"},
)
class RequestAuthenticationSpecSelector:
    def __init__(
        self,
        *,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        """The selector determines the workloads to apply the RequestAuthentication on.

        :param match_labels: 

        :schema: RequestAuthenticationSpecSelector
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if match_labels is not None:
            self._values["match_labels"] = match_labels

    @builtins.property
    def match_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """
        :schema: RequestAuthenticationSpecSelector#matchLabels
        """
        result = self._values.get("match_labels")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RequestAuthenticationSpecSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "RequestAuthentication",
    "RequestAuthenticationOptions",
    "RequestAuthenticationSpec",
    "RequestAuthenticationSpecJwtRules",
    "RequestAuthenticationSpecJwtRulesFromHeaders",
    "RequestAuthenticationSpecSelector",
]

publication.publish()
