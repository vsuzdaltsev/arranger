from arranger_conf import ArrangerConf
from arranger_conf.arranger_cdktf_conf import TfConf


class TestTFConf:
    def test_tf_configs_should_contain_list_of_available_clusters(
        self, tenants_from_tf_conf
    ):
        assert tenants_from_tf_conf == sorted(ArrangerConf.TENANTS.keys())

    def test_ALL_STACKS_should_contain_list_of_deployed_stacks(
        self, tenants_from_tf_conf
    ):
        for tenant in [
            tenant.capitalize() for tenant in tenants_from_tf_conf if tenant != "local"
        ]:
            assert isinstance(getattr(TfConf, tenant).ALL_STACKS, list)
            assert len(getattr(TfConf, tenant).ALL_STACKS) > 0

    def test_AWS_GLOBAL_REGION(self, tenants_from_tf_conf):
        assert [
            getattr(TfConf, tenant.capitalize()).AWS_GLOBAL_REGION == "us-east-1"
            for tenant in tenants_from_tf_conf
        ]

    def test_TENANT(self, tenants_from_tf_conf):
        for tenant in tenants_from_tf_conf:
            assert getattr(TfConf, tenant.capitalize()).TENANT == tenant
