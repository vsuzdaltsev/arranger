import time

from arranger_conf import ArrangerConf


SUPPORTED_CLOUDS = ["aws"]


class TestCdktfGlobals:
    def test_common_tags(self, globals_for_local_tenant):
        tenant = "local"
        common_tags = globals_for_local_tenant.common_tags()

        assert common_tags["created_by"] == "cdktf"
        assert common_tags["caution"] == "do not modify manually"
        assert isinstance(common_tags["code"], str)
        assert common_tags["tenant"] == tenant
        assert isinstance(common_tags["created_at"], type(time.ctime()))

    def test_cloud_with_absent_attribute(self, globals_for_local_tenant):
        assert globals_for_local_tenant.cloud is None

    def test_cloud_with_existing_attribute(self, globals_for_cloud_tenant):
        assert globals_for_cloud_tenant.cloud in SUPPORTED_CLOUDS

    def test_new_subnet_valid_case(self, globals_for_cloud_tenant):
        subnet1 = globals_for_cloud_tenant._new_subnet(
            supernet_cidr="10.62.0.0/18", subnet_index=1, subnet_prefix=24
        )
        subnet2 = globals_for_cloud_tenant._new_subnet(
            supernet_cidr="10.62.0.0/18", subnet_index=2, subnet_prefix=24
        )
        subnet3 = globals_for_cloud_tenant._new_subnet(
            supernet_cidr="10.62.0.0/18", subnet_index=3, subnet_prefix=24
        )

        assert subnet1 == "10.62.1.0/24"
        assert subnet2 == "10.62.2.0/24"
        assert subnet3 == "10.62.3.0/24"

    def test_sub_environments_when_they_exist(
        self,
        globals_for_cloud_tenant,
        cloud_tenant,
    ):
        assert globals_for_cloud_tenant.sub_environments == ArrangerConf.TENANTS.get(
            cloud_tenant
        ).get("sub_environments")

    def test_sub_environments_when_they_dont_exist(
        self,
        globals_for_local_tenant,
        local_tenant,
    ):
        assert (
            globals_for_local_tenant.sub_environments
            == ArrangerConf.TENANTS.get(local_tenant).get("sub_environments")
            is None
        )

    def test_run_cmd(self, globals_for_cloud_tenant):
        assert globals_for_cloud_tenant.run_cmd(["echo OK"]) == "OK"

    def test_aws_backend_s3bucket_name_first(self, globals_for_cloud_tenant):
        ArrangerConf.PROJECT_NAME = "my-first-arranger-project"

        assert (
            globals_for_cloud_tenant._aws_backend_s3bucket_name
            == "my-fi-arranger-tf-remote-states-development1"
        )
    def test_aws_backend_s3bucket_name_second(self, globals_for_cloud_tenant):
        ArrangerConf.PROJECT_NAME = "ololo-foo-bar"

        assert (
                globals_for_cloud_tenant._aws_backend_s3bucket_name
                == "ololo-arranger-tf-remote-states-development1"
        )