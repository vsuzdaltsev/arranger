import inspect

import pytest

from arranger_conf.arranger_cdktf_conf import TfConf


@pytest.fixture(scope="module")
def clusters_from_tf_conf():
    return sorted(
        [
            cls_attribute.__name__
            for cls_attribute in TfConf.__dict__.values()
            if inspect.isclass(cls_attribute) and (cls_attribute, TfConf)
        ]
    )
