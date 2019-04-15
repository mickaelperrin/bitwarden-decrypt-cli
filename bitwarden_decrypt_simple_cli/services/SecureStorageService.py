from bitwarden_decrypt_simple_cli.services.CryptoService import CryptoService
from bitwarden_decrypt_simple_cli.services.StorageService import StorageService


class SecureStorageService:

    cryptoService: CryptoService = None
    storageService: StorageService = None

    def __init__(self, storage_service: StorageService, crypto_service: CryptoService):
        self.cryptoService = crypto_service
        self.storageService = storage_service

    def decrypt(self, enc_value) -> str:
        return 'Decrypted value of ' + enc_value

    def get(self, key: str):
        value = self.storageService.get(self._make_protected_storage_key(key))
        if value is None:
            return None
        return self.decrypt(value)

    @staticmethod
    def _make_protected_storage_key(key) -> str:
        return '__PROTECTED__' + key