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


class IstioOperator(
    cdk8s.ApiObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="installistioioistiooperator.IstioOperator",
):
    """
    :schema: IstioOperator
    """

    def __init__(
        self,
        scope: constructs.Construct,
        name: builtins.str,
        *,
        spec: typing.Any = None,
    ) -> None:
        """Defines a "IstioOperator" API object.

        :param scope: the scope in which to define this object.
        :param name: a scope-local name for the object.
        :param spec: Specification of the desired state of the istio control plane resource. More info: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
        """
        options = IstioOperatorOptions(spec=spec)

        jsii.create(IstioOperator, self, [scope, name, options])


@jsii.data_type(
    jsii_type="installistioioistiooperator.IstioOperatorOptions",
    jsii_struct_bases=[],
    name_mapping={"spec": "spec"},
)
class IstioOperatorOptions:
    def __init__(self, *, spec: typing.Any = None) -> None:
        """
        :param spec: Specification of the desired state of the istio control plane resource. More info: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status

        :schema: IstioOperator
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if spec is not None:
            self._values["spec"] = spec

    @builtins.property
    def spec(self) -> typing.Any:
        """Specification of the desired state of the istio control plane resource.

        More info: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status

        :schema: IstioOperator#spec
        """
        result = self._values.get("spec")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IstioOperatorOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IstioOperator",
    "IstioOperatorOptions",
]

publication.publish()
