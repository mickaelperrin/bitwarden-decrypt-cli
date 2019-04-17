from bitwarden_simple_cli.models.domain.DomainBase import Domain
from bitwarden_simple_cli.models.domain.CipherString import CipherString
from bitwarden_simple_cli.models.data.LoginData import LoginData


class LoginUri(Domain):
    uri: CipherString

    def __init__(self, obj: LoginData, already_encrypted: bool = False):
        super()
        if obj is None:
            return
        self.build_domain_model(self, obj,
                                {
                                    'uri': None,
                                },
                                already_encrypted,
                                [])

    def decrypt(self, org_id: str):
        return self.uri.decrypt(org_id)
