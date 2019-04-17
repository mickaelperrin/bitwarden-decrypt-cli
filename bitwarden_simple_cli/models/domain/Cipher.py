from bitwarden_simple_cli.models.data.CipherData import CipherData
from bitwarden_simple_cli.models.domain.DomainBase import Domain
from bitwarden_simple_cli.models.domain.Field import Field
from bitwarden_simple_cli.enums.CipherType import CipherType
from bitwarden_simple_cli.models.domain.Login import Login


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
        if field in ['name', 'notes']:
            return self.__getattribute__(field).decrypt(self.organizationId)
        elif field in ['username', 'password']:
            return self.login.decrypt_field(field, self.organizationId)
        elif field == 'uri':
            return self.login.decrypt_uri(self.organizationId, 1)
        elif field == 'uris':
            return [self.login.decrypt_uri(self.organizationId, i) for i in range(1, len(self.login.uris)+1)]
        elif len(self.fields) > 0:
            # try custom fields
            for custom_field in self.fields:
                if str(custom_field.name.decrypt(self.organizationId), 'utf-8') == field:
                    return custom_field.value.decrypt(self.organizationId)

