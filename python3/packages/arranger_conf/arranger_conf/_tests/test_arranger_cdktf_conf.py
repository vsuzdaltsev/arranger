from arranger_conf import ArrangerConf
from arranger_conf.arranger_cdktf_conf import TfConf


def _class_name(tenant: str) -> str:
    return tenant.capitalize()


class TestTFConf:
    def test_tf_configs_should_contain_list_of_available_clusters(
        self, tenants_from_tf_conf
    ):
        assert tenants_from_tf_conf == sorted(ArrangerConf.TENANTS.keys())

    def test_ALL_STACKS_should_contain_list_of_deployed_stacks(
        self, tenants_from_tf_conf
    ):
        for tenant in [
            _class_name(tenant=_t) for _t in tenants_from_tf_conf if _t != "local"
        ]:
            assert isinstance(getattr(TfConf, tenant).ALL_STACKS, list)
            assert len(getattr(TfConf, tenant).ALL_STACKS) > 0

    def test_VALID_STACKS(self):
        assert isinstance(TfConf.Local.VALID_STACKS, dict)
        for stack_name, stack_metadata in TfConf.Local.VALID_STACKS.items():
            assert stack_name.endswith("-stack") == True

            assert isinstance(stack_metadata["class_name"], str)
            assert stack_metadata["class_name"].endswith("Stack")

            assert isinstance(stack_metadata["description"], str)
            assert len(stack_metadata["description"]) > 0

            assert isinstance(stack_metadata["depends_on"], list)

    def test_ALL_STACKS_should_contain_stacks_from_VALID_STACKS(
        self, tenants_from_tf_conf
    ):
        for tenant in [_class_name(tenant=_t) for _t in tenants_from_tf_conf]:
            for stack in getattr(TfConf, tenant).ALL_STACKS:
                assert stack in getattr(TfConf, tenant).VALID_STACKS.keys()

    def test_AWS_GLOBAL_REGION(self, tenants_from_tf_conf):
        assert [
            getattr(TfConf, _class_name(tenant=tenant)).AWS_GLOBAL_REGION == "us-east-1"
            for tenant in tenants_from_tf_conf
        ]

    def test_TENANT(self, tenants_from_tf_conf):
        for tenant in tenants_from_tf_conf:
            assert getattr(TfConf, _class_name(tenant=tenant)).TENANT == tenant
