from bitwarden_simple_cli.enums.CipherType import CipherType
from bitwarden_simple_cli.models.data.FieldData import FieldData
from bitwarden_simple_cli.models.data.LoginData import LoginData
from bitwarden_simple_cli.models.response.CipherResponse import CipherResponse


class CipherData:
    collectionIds: []
    fields: []
    id: str
    login: LoginData
    organizationId: str
    type: CipherType
    userId: str

    def __init(self, response: CipherResponse, user_id: str, collection_ids: []):
        if response is None:
            return

        self.id = response.id
        self.organizationId = response.organizationId
        self.type = CipherType(int(response.type))
        self.userId = user_id

        if collection_ids:
            self.collectionIds = collection_ids
        else:
            self.collectionIds = response.collectionsIds

        if self.type == CipherType.Login:
            self.login = LoginData(response.login)

        if response.fields:
            self.fields = []
            for field in response.fields:
                self.fields.append(FieldData(field))

    def __getattr__(self, item):
        return self.item
