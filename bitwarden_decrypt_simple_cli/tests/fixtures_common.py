import pytest
from os import path
from bitwarden_decrypt_simple_cli.services.StorageService import StorageService
from bitwarden_decrypt_simple_cli.services.SecureStorageService import SecureStorageService
from bitwarden_decrypt_simple_cli.services.CryptoService import CryptoService


def common_data(item):
    return dict(
        BW_SESSION='Tyy0rDgzvA/jgHsqUtKIgNnAWaRtHKZoSs6pa10qWQf0QmFtd2/xn8TNJy8Fu2nPRNVDpn3k7tu49W1pQVU8Zg==',
        nl='\n',
        organization_id='1ff51ccd-0a25-46a2-a3cd-aa3000cfa874',
        protected_key='ArxoewBOPtCYZKqn34f8CoMQVUrNZnrhGU9OYuJu8UpB7DngEwf/TEHjbxPJJhUDG+DnPQR76J9d12/4tnGT5C6ZaLxxInRooT4AuX2ljIrSppCee1AvzIMu7ljGhR++ng==',
        protected_key_decoded=b'/lCGAMDGAq+mjRP3FJv+VNDDnbrYcVGnsiPeXTm4NfU=',
        test_database_filename='bitwarden_db.json',
        user_email='dev+bitwarden@mickaelperrin.fr',
        user_id='03780246-7f1d-4221-8615-aa3000cd8123',
        uuid_personal='fd8870cc-3659-40aa-9492-aa3000cedbb'
    ).get(item)


@pytest.fixture
def no_bw_session(monkeypatch):
    monkeypatch.delenv('BW_SESSION')


@pytest.fixture
def bw_session(monkeypatch):
    monkeypatch.setenv('BW_SESSION', common_data('BW_SESSION'))


@pytest.fixture
def storage_service():
    return StorageService(path.join(path.dirname(__file__), common_data('test_database_filename')))


@pytest.fixture()
def secure_storage_service():
    storage_service = StorageService(path.join(path.dirname(__file__), common_data('test_database_filename')))
    return SecureStorageService(storage_service, CryptoService(storage_service))
