from os import environ


class Bitwarden:

    def _exit_if_no_session(self):
        if not environ.get('BW_SESSION'):
            print('Environement variable BW_SESSION is not set.')
            exit(1)

    def get(self, uuid, field):
        self._exit_if_no_session()
        print('getting ' + field + ' of ' + uuid)