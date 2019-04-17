from os import environ
from sys import exit, stdout, stderr
from bitwarden_simple_cli.services.ContainerService import ContainerService
from bitwarden_simple_cli.services.CryptoService import CryptoService
from bitwarden_simple_cli.services.SecureStorageService import SecureStorageService
from bitwarden_simple_cli.services.StorageService import StorageService
from bitwarden_simple_cli.services.UserService import UserService
from bitwarden_simple_cli.services.CipherService import CipherService


class Bitwarden:
    containerService: ContainerService
    cryptoService: CryptoService
    secureStorageService: SecureStorageService
    storageService: StorageService

    def __init__(self):
        self.storageService = StorageService()
        self.cryptoService = CryptoService(self.storageService)
        self.secureStorageService = SecureStorageService(self.storageService, self.cryptoService)
        self.userService = UserService(self.storageService)
        self.cipherService = CipherService(self.storageService, self.userService)
        self.containerService = ContainerService()
        self.containerService.add_service(self.cryptoService)
        self.containerService.add_service(self.secureStorageService)

    def _exit_if_no_session(self):
        if not environ.get('BW_SESSION'):
            print('Environement variable BW_SESSION is not set.')
            exit(1)
        if not self.cryptoService.has_key():
            print('Vault is locked.')
            exit(1)

    def get(self, uuid, field):
        self._exit_if_no_session()
        cipher = self.cipherService.get(uuid)
        if cipher is None:
            print('Unable to find entry with id :' + uuid, file=stderr)
            exit(1)
        decrypted_value = cipher.decrypt_field(field)
        if type(decrypted_value).__name__ == 'bytes':
            print(str(decrypted_value, 'utf-8'), end='')
        elif type(decrypted_value).__name__ == 'list':
            for item in decrypted_value:
                print(str(item, 'utf-8'))
        else:
            print(decrypted_value, file=stderr)

    def list(self):
        self._exit_if_no_session()
        ciphers = self.storageService.list_ciphers(self.userService.get_user_id())
        for cipher in ciphers:
            print(cipher['id'] + ' ' + str(cipher['name'].decrypt(cipher['org_id']), 'utf-8'))


