from arranger_conf import ArrangerConf


class TestArrangerConf:
    def test_PROJECT_NAME(self):
        assert isinstance(ArrangerConf.PROJECT_NAME, str)
        assert ArrangerConf.PROJECT_NAME != ""

    def test_TENANTS(self):
        assert isinstance(ArrangerConf.TENANTS, dict)
        assert ArrangerConf.TENANTS
