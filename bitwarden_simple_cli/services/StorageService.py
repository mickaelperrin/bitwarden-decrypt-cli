from os import environ, path as os_path
from platform import system
from json import load as json_load
from bitwarden_simple_cli.models.domain.CipherString import CipherString


class StorageService:

    app_path: str
    database_path: str
    database_filename: str = 'data.json'

    def __init__(self, database_path=None):
        self.database_path = self.set_database_path(database_path)
        self.database = self._read_datase_file()

    def get(self, key):
        return self.database.get(key)

    @staticmethod
    def guess_database_dir():
        if environ.get('BITWARDENCLI_APPDATA_DIR'):
            return environ.get('BITWARDENCLI_APPDATA_DIR')
        elif system() == 'Linux':
            return environ.get('XDG_CONFIG_HOME')
        elif system() == 'Darwin':
            return os_path.join(environ.get('HOME'), 'Library/Application Support/Bitwarden CLI')
        elif system() == 'Windows':
            return os_path.join(environ.get('APPDATA'), 'Bitwarden CLI')
        else:
            return os_path.join(environ.get('HOME'), '.config/Bitwarden CLI')

    def list_ciphers(self, user_id):
        ciphers = self.database.get('ciphers_' + user_id)
        list = []
        for k, cipher in ciphers.items():
            list.append(dict(id=cipher['id'], name=CipherString(cipher['name']), org_id=cipher.get('organizationId')))
        return list

    def _read_datase_file(self):
        with open(self.database_path, 'r') as fp:
            try:
                database = json_load(fp)
                return database
            except ValueError:
                print("error loading JSON")

    def set_database_path(self, path):
        if path is None:
            return self.set_database_path(os_path.join(self.guess_database_dir(), self.database_filename))
        if os_path.isfile(path):
            return path
        raise Exception('Database file not found at ' + path)
