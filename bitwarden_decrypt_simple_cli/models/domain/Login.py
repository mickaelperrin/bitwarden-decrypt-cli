from bitwarden_decrypt_simple_cli.models.domain.DomainBase import Domain
from bitwarden_decrypt_simple_cli.models.domain.CipherString import CipherString
from bitwarden_decrypt_simple_cli.models.data.LoginData import LoginData


class Login(Domain):
    username: CipherString
    password: CipherString

    def __init__(self, obj: LoginData, already_encrypted=False):
        super().__init__()
        if obj is None:
            return

        self.build_domain_model(self, obj,
                                {
                                  'username': None,
                                  'password': None
                                }, already_encrypted, [])

    def decrypt_field(self, field, org_id):
        return self[field].decrypt(org_id)
