from os import environ
from bitwarden_decrypt_simple_cli.services.StorageService import StorageService


class Bitwarden:

    def __init__(self):
        self.storageService = StorageService()

    def _exit_if_no_session(self):
        if not environ.get('BW_SESSION'):
            print('Environement variable BW_SESSION is not set.')
            exit(1)

    def get(self, uuid, field):
        self._exit_if_no_session()
        print('getting ' + field + ' of ' + uuid)