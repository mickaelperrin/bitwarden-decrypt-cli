from .__version__ import __version__
from sys import exit
from bitwarden_simple_cli.Bitwarden import Bitwarden
from bitwarden_simple_cli.exceptions.ManagedException import ManagedException
from uuid import UUID


def is_uuid(uuid_string, version=4):
    try:
        uid = UUID(uuid_string, version=version)
        return uid.hex == uuid_string.replace('-', '')
    except ValueError:
        return False


class CliSimple:

    action: str
    field: str
    script_name: str
    uuid: str

    def __init__(self, script_name, action='version', field='password', uuid=None):
        self.field = field
        self.uuid = uuid
        if uuid is None and is_uuid(self.field):
            self.field = 'password'
            self.uuid = field
        self.action = action
        self.script_name = script_name

    def run(self):
        if self.action == 'get':
            if self.uuid is None:
                print('Error: UUID is required to get secret')
                print(self.usage())
                exit(1)
            return self.get(self.uuid, self.field)
        elif self.action == 'list':
            return self.list()
        else:
            return self.version()

    @staticmethod
    def usage(action='get'):
        if action == 'get':
            print('Usage: get UUID [field]')

    @staticmethod
    def get(uuid, field):
        try:
            app = Bitwarden()
            return app.get(uuid, field)
        except ManagedException as e:
            exit(e.args[0])

    @staticmethod
    def list():
        app = Bitwarden()
        return app.list()

    @staticmethod
    def version():
        print('Version: ' + __version__)
