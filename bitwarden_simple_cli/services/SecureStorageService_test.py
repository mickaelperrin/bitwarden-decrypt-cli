import pytest
from bitwarden_simple_cli.tests.fixtures_common import common_data, secure_storage_service, bw_session


@pytest.mark.usefixtures("bw_session")
def test_secure_storage_service_get(secure_storage_service):
    assert secure_storage_service.get('userId') is None
    assert secure_storage_service.get('key') == b'/lCGAMDGAq+mjRP3FJv+VNDDnbrYcVGnsiPeXTm4NfU='


