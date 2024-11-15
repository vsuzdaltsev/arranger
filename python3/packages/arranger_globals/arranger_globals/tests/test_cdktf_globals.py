import time

from arranger_globals import CdktfGlobals

supported_clouds = ["aws"]


class TestCdktfGlobals:
    def test_common_tags(self):
        tenant = "local"

        common_tags = CdktfGlobals(tenant=tenant).common_tags()
        assert common_tags["created_by"] == "cdktf"
        assert common_tags["caution"] == "do not modify manually"
        assert isinstance(common_tags["code"], str)
        assert common_tags["tenant"] == tenant
        assert isinstance(common_tags["created_at"], type(time.ctime()))

    def test_cloud_with_absent_attribute(self):
        assert CdktfGlobals(tenant="local").cloud is None

    def test_cloud_with_existing_attribute(self):
        assert CdktfGlobals(tenant="development1").cloud in supported_clouds
