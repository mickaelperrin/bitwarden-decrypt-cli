from bitwarden_decrypt_simple_cli.services.CryptoService import CryptoService
from bitwarden_decrypt_simple_cli.services.SecureStorageService import SecureStorageService


class ContainerService:

    class __ContainerService:

        services = dict()

        def add_service(self, service):
            self.services[type(service).__name__] = service

        def get_crypto_service(self) -> CryptoService:
            return self.services['CryptoService']

        def get_secure_storage_service(self) -> SecureStorageService:
            return self.services['SecureStorageService']

        def get_service(self, service):
            return self.services[service]

    instance = None

    @classmethod
    def __new__(cls, arg=None):
        if not ContainerService.instance:
            ContainerService.instance = ContainerService.__ContainerService()
        return ContainerService.instance

    def __getattr__(self, item):
        return getattr(self.instance, item)

    def __setattr__(self, key, value):
        return setattr(self.instance, key, value)
