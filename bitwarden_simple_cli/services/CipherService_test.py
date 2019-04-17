import pytest
from bitwarden_simple_cli.services.CipherService import CipherService
from bitwarden_simple_cli.tests.fixtures_common import bw_session, cipher_service, common_data


@pytest.mark.usefixtures("bw_session")
def test_cipher_service(cipher_service):
    cipher = cipher_service.get(common_data('uuid_login_personal'))
    assert cipher.id == 'fd8870cc-3659-40aa-9492-aa3000cedbb3'
    assert cipher.organizationId is None
    assert cipher.userId == common_data('user_id')
