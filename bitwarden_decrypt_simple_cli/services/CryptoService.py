from bitwarden_decrypt_simple_cli.services.StorageService import StorageService


class CryptoService:

    storageService: StorageService

    def __init__(self, storage_service: StorageService):
        self.storageService = storage_service

    def get_key(self):
        if self.key:
            return self.key

        key = self.secureStorageService.get(Keys['key'])

        if key:
            self.key = SymmetricCryptoKey(b64decode(key))

        return self.key if key else None

    def has_key(self):
        return self.get_key() is not None