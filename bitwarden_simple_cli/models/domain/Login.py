from bitwarden_simple_cli.models.domain.DomainBase import Domain
from bitwarden_simple_cli.models.domain.CipherString import CipherString
from bitwarden_simple_cli.models.data.LoginData import LoginData
from bitwarden_simple_cli.models.domain.LoginUri import LoginUri


class Login(Domain):
    username: CipherString
    password: CipherString
    uris: [] = None

    def __init__(self, obj: LoginData, already_encrypted=False):
        super().__init__()
        if obj is None:
            return

        self.build_domain_model(self, obj,
                                {
                                  'username': None,
                                  'password': None
                                }, already_encrypted, [])

        if obj.get('uris'):
            self.uris = []
            for uri in obj['uris']:
                self.uris.append(LoginUri(uri, already_encrypted))

    def decrypt_field(self, field, org_id):
        return self[field].decrypt(org_id)

    def decrypt_uri(self, org_id, i=1):
        # Only process first URI at the moment
        return self.uris[i-1].decrypt(org_id)
