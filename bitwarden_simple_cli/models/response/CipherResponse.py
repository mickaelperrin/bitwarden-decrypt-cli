from bitwarden_simple_cli.models.api.LoginApi import LoginApi
from bitwarden_simple_cli.models.api.FieldApi import FieldApi
from bitwarden_simple_cli.models.response.BaseResponse import BaseResponse


class CipherResponse(BaseResponse):
    collectionsIds = None
    id = None
    name = None
    organizationId = None
    type = None

    def __init__(self, response):
        super().__init__(response)
        self.collectionIds = self.get_response_property_name('CollectionIds')
        self.name = self.get_response_property_name('Name')
        self.id = self.get_response_property_name('Id')
        self.organizationId = self.get_response_property_name('OrganizationId')
        self.type = self.get_response_property_name('Type')

        login = self.get_response_property_name('Login')
        if login:
            self.login = LoginApi(login)

        fields = self.get_response_property_name('Fields')
        if fields:
            self.fields = [FieldApi(field) for field in fields]
