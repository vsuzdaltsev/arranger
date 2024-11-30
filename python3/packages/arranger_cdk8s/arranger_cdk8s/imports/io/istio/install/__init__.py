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
    jsii_type="ioistioinstall.IstioOperator",
):
    '''
    :schema: IstioOperator
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        spec: typing.Any = None,
    ) -> None:
        '''Defines a "IstioOperator" API object.

        :param scope: the scope in which to define this object.
        :param id: a scope-local name for the object.
        :param spec: Specification of the desired state of the istio control plane resource. More info: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
        '''
        props = IstioOperatorProps(spec=spec)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="manifest") # type: ignore[misc]
    @builtins.classmethod
    def manifest(cls, *, spec: typing.Any = None) -> typing.Any:
        '''Renders a Kubernetes manifest for "IstioOperator".

        This can be used to inline resource manifests inside other objects (e.g. as templates).

        :param spec: Specification of the desired state of the istio control plane resource. More info: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
        '''
        props = IstioOperatorProps(spec=spec)

        return typing.cast(typing.Any, jsii.sinvoke(cls, "manifest", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="GVK")
    def GVK(cls) -> cdk8s.GroupVersionKind:
        '''Returns the apiVersion and kind for "IstioOperator".'''
        return typing.cast(cdk8s.GroupVersionKind, jsii.sget(cls, "GVK"))


@jsii.data_type(
    jsii_type="ioistioinstall.IstioOperatorProps",
    jsii_struct_bases=[],
    name_mapping={"spec": "spec"},
)
class IstioOperatorProps:
    def __init__(self, *, spec: typing.Any = None) -> None:
        '''
        :param spec: Specification of the desired state of the istio control plane resource. More info: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status

        :schema: IstioOperator
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if spec is not None:
            self._values["spec"] = spec

    @builtins.property
    def spec(self) -> typing.Any:
        '''Specification of the desired state of the istio control plane resource.

        More info: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status

        :schema: IstioOperator#spec
        '''
        result = self._values.get("spec")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IstioOperatorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IstioOperator",
    "IstioOperatorProps",
]

publication.publish()
