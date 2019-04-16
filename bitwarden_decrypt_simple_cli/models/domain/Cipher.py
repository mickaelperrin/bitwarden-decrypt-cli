from bitwarden_decrypt_simple_cli.models.data.CipherData import CipherData
from bitwarden_decrypt_simple_cli.models.domain.DomainBase import Domain
from bitwarden_decrypt_simple_cli.models.domain.Field import Field
from bitwarden_decrypt_simple_cli.enums.CipherType import CipherType
from bitwarden_decrypt_simple_cli.models.domain.Login import Login


class Cipher(Domain):
    id = None
    fields = None
    login = None
    folderId = None
    name = None
    response = None
    type: CipherType
    userId = None
    organizationId = None

    def __init__(self, obj: CipherData, already_encrypted=False, local_data=None):
        super().__init__()
        if obj is None:
            return
        self.build_domain_model(self, obj,
                                {
                                  'id': None,
                                  'userId': None,
                                  'organizationId': None,
                                  'folderId': None,
                                  'name': None,
                                  'notes': None
                                }, already_encrypted,
                                [
                                  'id',
                                  'userId',
                                  'organizationId',
                                  'folderId'
                                ])

        self.type = CipherType(int(obj['type']))

        if self.type == CipherType.Login:
            self.login = Login(obj['login'], already_encrypted)

        if obj.get('fields'):
            self.fields = []
            for field in obj['fields']:
                self.fields.append(Field(field, already_encrypted))

    def decrypt_field(self, field):
        if field in ['username', 'password']:
            return self.login.decrypt_field(field, self.organizationId)
        if field == 'uri':
            return self.login.decrypt_uri(self.organizationId, 1)
