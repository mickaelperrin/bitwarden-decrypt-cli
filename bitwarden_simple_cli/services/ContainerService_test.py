import pytest
from bitwarden_simple_cli.services.ContainerService import ContainerService
from bitwarden_simple_cli.services.StorageService import StorageService
from bitwarden_simple_cli.services.SecureStorageService import SecureStorageService
from bitwarden_simple_cli.services.CryptoService import CryptoService


def test_container_service():
    storage_service = StorageService()
    crypto_service = CryptoService(storage_service)
    secure_storage_service = SecureStorageService(storage_service, crypto_service)
    container_service = ContainerService()
    container_service.add_service(crypto_service)
    container_service.add_service(secure_storage_service)
    container_service2 = ContainerService()
    assert container_service.get_crypto_service() == crypto_service
    assert container_service.get_secure_storage_service() == secure_storage_service
    assert container_service2.get_crypto_service() == crypto_service
    assert container_service2.get_secure_storage_service() == secure_storage_service