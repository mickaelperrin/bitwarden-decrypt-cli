import pytest
from bitwarden_simple_cli.models.domain.Cipher import Cipher
from bitwarden_simple_cli.services.StorageService import StorageService
from bitwarden_simple_cli.tests.fixtures_common import common_data, storage_service
from bitwarden_simple_cli.services.CipherService import Keys
from bitwarden_simple_cli.models.domain.Login import Login
from bitwarden_simple_cli.enums.CipherType import CipherType


@pytest.fixture()
def cipher_login_personal(storage_service: StorageService):
    cipher_response = storage_service.get(Keys['ciphersPrefix'] + common_data('user_id'))\
        [common_data('uuid_login_personal')]
    return Cipher(cipher_response)


def test_cipher_login_personal(cipher_login_personal: Cipher):
    assert cipher_login_personal.id == 'fd8870cc-3659-40aa-9492-aa3000cedbb3'
    assert cipher_login_personal.organizationId is None
    assert cipher_login_personal.type == CipherType.Login
    assert isinstance(cipher_login_personal.login, Login)
    assert type(cipher_login_personal.fields).__name__ == 'list'
    assert len(cipher_login_personal.fields) == 4
    #TODO: cipherString tests
