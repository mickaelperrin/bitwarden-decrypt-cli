#!/usr/bin/env python3
import sys
from bitwarden_decrypt_simple_cli.__version__ import __version__


class CLI:

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
                self.usage()
                sys.exit(1)
            self.get(self.uuid, self.field)
        else:
            self.version()

    def usage(self, action='get'):
        if action == 'get':
            print('Usage: get UUID [field]')

    @staticmethod
    def get(uuid, field):
        print('get ' + field + ' of ' + uuid)

    @staticmethod
    def version():
        print('Version: ' + __version__)


if __name__ == '__main__':
    cli = CLI(*sys.argv)
    cli.run()
