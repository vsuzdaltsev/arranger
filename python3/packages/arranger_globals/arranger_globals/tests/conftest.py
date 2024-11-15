import pytest

from arranger_globals import CdktfGlobals


@pytest.fixture(scope="function")
def cdktf_globals_for_local_tenant():
    return CdktfGlobals(tenant="local")


@pytest.fixture(scope="function")
def cdktf_globals_for_cloud_tenant():
    return CdktfGlobals(tenant="development1")
