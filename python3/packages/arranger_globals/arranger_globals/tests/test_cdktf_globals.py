import time
import pytest

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

    def test_new_subnet_valid_case(self, cdktf_globals_for_cloud_tenant):
        new_subnet = cdktf_globals_for_cloud_tenant._new_subnet(
            supernet_cidr="10.62.0.0/18", subnet_index=1, subnet_prefix=24
        )
        assert new_subnet == "10.62.1.0/24"
