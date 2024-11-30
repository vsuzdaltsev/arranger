import pytest

from arranger_globals import CdktfGlobals


@pytest.fixture(scope="function")
def local_tenant():
    return "local"


@pytest.fixture(scope="function")
def cloud_tenant():
    return "development1"


@pytest.fixture(scope="function")
def globals_for_local_tenant(local_tenant):
    return CdktfGlobals(tenant=local_tenant)


@pytest.fixture(scope="function")
def globals_for_cloud_tenant(cloud_tenant):
    return CdktfGlobals(tenant=cloud_tenant)
