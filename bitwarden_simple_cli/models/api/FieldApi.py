from bitwarden_simple_cli.enums.FieldType import FieldType
from bitwarden_simple_cli.models.response.BaseResponse import BaseResponse


class FieldApi(BaseResponse):
    name: str
    value: str
    type: FieldType

    def __init__(self, data):
        super().__init__(data)
        if data is None:
            return
        self.type = self.get_response_property_name('Type')
        self.name = self.get_response_property_name('Name')
        self.value = self.get_response_property_name('Value')
