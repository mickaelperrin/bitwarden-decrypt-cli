from bitwarden_simple_cli.services.StorageService import StorageService


class UserService:

    email = None
    stamp = None
    storageService = None
    userId = None

    def __init__(self, storage_service: StorageService):
        self.storageService = storage_service

    def get_user_id(self):
        if self.userId:
            return self.userId
        self.userId = self.storageService.get('userId')
        return self.userId
