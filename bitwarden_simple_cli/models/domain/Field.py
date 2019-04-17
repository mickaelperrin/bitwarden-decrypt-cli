from bitwarden_simple_cli.models.domain.CipherString import CipherString
from bitwarden_simple_cli.models.domain.DomainBase import Domain
from bitwarden_simple_cli.models.data.FieldData import FieldData
from bitwarden_simple_cli.enums.FieldType import FieldType


class Field(Domain):

    name: CipherString
    value: CipherString
    type: FieldType

    def __init__(self, obj: FieldData, already_encrypted=False):
        super().__init__()
        if obj is None:
            return
        self.type = FieldType(int(obj['type']))
        self.build_domain_model(self, obj, {
            'name': None,
            'value': None,
        }, already_encrypted, [])
