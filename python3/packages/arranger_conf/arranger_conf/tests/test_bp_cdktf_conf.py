from arranger_conf import ArrangerConf
from arranger_conf.arranger_cdktf_conf import TfConf


class TestTFConf:
    def test_tf_configs_should_contain_list_of_available_clusters(
        self, clusters_from_tf_conf
    ):
        tenant_names = sorted(
            [
                name.lower()
                for name, obj in TfConf.__dict__.items()
                if isinstance(obj, type)
            ]
        )
        assert tenant_names == sorted(ArrangerConf.TENANTS.keys())

    def test_ALL_STACKS_should_contain_list_of_deployed_stacks(
        self, clusters_from_tf_conf
    ):
        for tenant in clusters_from_tf_conf:
            if tenant is not "local":
                assert isinstance(getattr(TfConf, tenant).ALL_STACKS, list)
                assert len(getattr(TfConf, tenant).ALL_STACKS) > 0

    def test_AWS_GLOBAL_REGION(self, clusters_from_tf_conf):
        assert [
            getattr(TfConf, tenant).AWS_GLOBAL_REGION == "us-east-1"
            for tenant in clusters_from_tf_conf
        ]
