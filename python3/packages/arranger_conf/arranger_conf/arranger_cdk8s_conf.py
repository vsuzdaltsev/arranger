"""K8s manifests configuration."""

import inspect

from .arranger_cdk8s_conf_lib import Local as LocalCluster
from .arranger_cdk8s_conf_lib import Sandbox1 as Sandbox1Cluster
from .arranger_cdk8s_conf_lib import Switchdev1 as Switchdev1Cluster


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

    class Local(LocalCluster):
        pass

    class D1(Switchdev1Cluster):
        pass

    class D2(Switchdev1Cluster):
        class IdentityVerificationMs(Switchdev1Cluster.IdentityVerificationMs):
            def CONFIG_MAP_DATA(self, attr):
                return super().CONFIG_MAP_DATA(self, attr) | {
                    "OVERRIDE": "test_value",
                }

    class D3(Switchdev1Cluster):
        pass

    class D4(Switchdev1Cluster):
        pass

    class D5(Switchdev1Cluster):
        pass

    class D6(Switchdev1Cluster):
        pass

    class D7(Switchdev1Cluster):
        pass

    class D8(Switchdev1Cluster):
        pass

    class D9(Switchdev1Cluster):
        pass

    class D10(Switchdev1Cluster):
        pass

    class D11(Switchdev1Cluster):
        pass

    class D12(Switchdev1Cluster):
        pass

    class D13(Switchdev1Cluster):
        pass

    class D14(Switchdev1Cluster):
        pass

    class D15(Switchdev1Cluster):
        pass

    class D16(Switchdev1Cluster):
        pass

    class D17(Switchdev1Cluster):
        pass

    class D18(Switchdev1Cluster):
        pass

    class D19(Switchdev1Cluster):
        pass

    class Sand1(Sandbox1Cluster):
        pass

    class Sand2(Sandbox1Cluster):
        pass
