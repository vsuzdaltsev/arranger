import time


SUPPORTED_CLOUDS = ["aws"]


class TestCdktfGlobals:
    def test_common_tags(self, cdktf_globals_for_local_tenant):
        tenant = "local"
        common_tags = cdktf_globals_for_local_tenant.common_tags()

        assert common_tags["created_by"] == "cdktf"
        assert common_tags["caution"] == "do not modify manually"
        assert isinstance(common_tags["code"], str)
        assert common_tags["tenant"] == tenant
        assert isinstance(common_tags["created_at"], type(time.ctime()))

    def test_cloud_with_absent_attribute(self, cdktf_globals_for_local_tenant):
        assert cdktf_globals_for_local_tenant.cloud is None

    def test_cloud_with_existing_attribute(self, cdktf_globals_for_cloud_tenant):
        assert cdktf_globals_for_cloud_tenant.cloud in SUPPORTED_CLOUDS
