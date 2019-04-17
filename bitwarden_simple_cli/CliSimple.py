from .__version__ import __version__
from sys import exit
from bitwarden_simple_cli.Bitwarden import Bitwarden


class CliSimple:

    action: str
    field: str
    script_name: str
    uuid: str

    def __init__(self, script_name, action='version', uuid=None, field='password'):
        self.action = action
        self.field = field
        self.script_name = script_name
        self.uuid = uuid

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
        app = Bitwarden()
        return app.get(uuid, field)

    @staticmethod
    def list():
        app = Bitwarden()
        return app.list()

    @staticmethod
    def version():
        print('Version: ' + __version__)
