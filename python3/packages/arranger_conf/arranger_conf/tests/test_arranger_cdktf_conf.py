from arranger_conf import ArrangerConf
from arranger_conf.arranger_cdktf_conf import TfConf


class TestTFConf:
    def test_tf_configs_should_contain_list_of_available_clusters(
        self, clusters_from_tf_conf
    ):
        assert [_cl.lower() for _cl in clusters_from_tf_conf] == sorted(
            ArrangerConf.TENANTS.keys()
        )

    def test_ALL_STACKS_should_contain_list_of_deployed_stacks(
        self, clusters_from_tf_conf
    ):
        for tenant in clusters_from_tf_conf:
            if tenant is not "Local":
                assert isinstance(getattr(TfConf, tenant).ALL_STACKS, list)
                assert len(getattr(TfConf, tenant).ALL_STACKS) > 0

    def test_AWS_GLOBAL_REGION(self, clusters_from_tf_conf):
        assert [
            getattr(TfConf, tenant).AWS_GLOBAL_REGION == "us-east-1"
            for tenant in clusters_from_tf_conf
        ]

    def test_TENANT(self, clusters_from_tf_conf):
        for tenant_class_name in clusters_from_tf_conf:
            tenant = tenant_class_name.lower()
            assert getattr(TfConf, tenant_class_name).TENANT == tenant
