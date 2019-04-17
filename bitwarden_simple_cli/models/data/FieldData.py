from bitwarden_simple_cli.enums.FieldType import FieldType
from bitwarden_simple_cli.models.api.FieldApi import FieldApi


class FieldData:
    type: FieldType
    name: str
    value: str

    def __init__(self, response: FieldApi):
        if response is None:
            return

        self.type = response.type
        self.name = response.name
        self.value = response.value

    def __getattr__(self, item):
        return self.item
