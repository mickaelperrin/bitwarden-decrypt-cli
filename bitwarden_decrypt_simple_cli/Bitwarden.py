from os import environ
from bitwarden_decrypt_simple_cli.services.CryptoService import CryptoService
from bitwarden_decrypt_simple_cli.services.SecureStorageService import SecureStorageService
from bitwarden_decrypt_simple_cli.services.StorageService import StorageService


class Bitwarden:
    cryptoService: CryptoService
    secureStorageService: SecureStorageService
    storageService: StorageService

    def __init__(self):
        self.storageService = StorageService()
        self.cryptoService = CryptoService(self.storageService)
        self.secureStorageService = SecureStorageService(self.storageService, self.cryptoService)

    def _exit_if_no_session(self):
        if not environ.get('BW_SESSION'):
            print('Environement variable BW_SESSION is not set.')
            exit(1)

    def get(self, uuid, field):
        self._exit_if_no_session()
        print('getting ' + field + ' of ' + uuid)
