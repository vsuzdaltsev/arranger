"""K8s manifests configuration."""

import inspect

from .arranger_cdk8s_conf_lib import Development1 as Development1Cluster


class K8sConf:
    @classmethod
    @property
    def ALL_ENVIRONMENTS(cls):
        return sorted(
            [
                cls_attribute.__name__
                for cls_attribute in cls.__dict__.values()
                if inspect.isclass(cls_attribute) and (cls_attribute, cls)
            ]
        )

    class D1(Development1Cluster):
        pass

    class D2(Development1Cluster):
        pass

    class D3(Development1Cluster):
        pass

    class D4(Development1Cluster):
        pass

    class D5(Development1Cluster):
        pass

    class D6(Development1Cluster):
        pass

    class D7(Development1Cluster):
        pass

    class D8(Development1Cluster):
        pass

    class D9(Development1Cluster):
        pass

    class D10(Development1Cluster):
        pass

    class D11(Development1Cluster):
        pass

    class D12(Development1Cluster):
        pass

    class D13(Development1Cluster):
        pass

    class D14(Development1Cluster):
        pass

    class D15(Development1Cluster):
        pass

    class D16(Development1Cluster):
        pass

    class D17(Development1Cluster):
        pass

    class D18(Development1Cluster):
        pass

    class D19(Development1Cluster):
        pass
