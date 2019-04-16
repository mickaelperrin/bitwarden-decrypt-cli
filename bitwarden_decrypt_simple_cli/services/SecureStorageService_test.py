import pytest
from bitwarden_decrypt_simple_cli.tests.fixtures_common import common_data, secure_storage_service


@pytest.mark.usefixtures("secure_storage_service")
def test_secure_storage_service_get(secure_storage_service):
    assert secure_storage_service.get('userId') is None
    assert secure_storage_service.get('key') == 'Decrypted value of ' + common_data('protected_key')