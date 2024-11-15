import pytest


@pytest.fixture(scope="function")
def cdktf_globals_for_local_tenant():
    from arranger_globals import CdktfGlobals

    return CdktfGlobals(tenant="local")
