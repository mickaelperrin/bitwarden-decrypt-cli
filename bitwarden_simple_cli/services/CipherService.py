from bitwarden_simple_cli.models.domain.Cipher import Cipher
from bitwarden_simple_cli.services.StorageService import StorageService
from bitwarden_simple_cli.services.UserService import UserService

Keys = dict(
    ciphersPrefix='ciphers_',
    localData='sitesLocalData',
    neverDomains='neverDomains'
)


class CipherService:
    storageService = None
    userService = None

    def __init__(self, storage_service: StorageService, user_service: UserService):
        self.storageService = storage_service
        self.userService = user_service

    def get(self, uuid: str):
        user_id = self.userService.get_user_id()
        local_data = self.storageService.get(Keys['localData'])
        ciphers = self.storageService.get(Keys['ciphersPrefix'] + user_id)
        if ciphers is None or uuid not in ciphers:
            return None
        return Cipher(ciphers[uuid], False, local_data[uuid] if local_data else None)
