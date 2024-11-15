import time

from arranger_globals import CdktfGlobals


class TestCdktfGlobals:
    def test_common_tags(self):
        tenant = "local"

        common_tags = CdktfGlobals(tenant=tenant).common_tags()
        assert common_tags["created_by"] == "cdktf"
        assert common_tags["caution"] == "do not modify manually"
        assert isinstance(common_tags["code"], str)
        assert common_tags["tenant"] == tenant
        assert isinstance(common_tags["created_at"], type(time.ctime()))
