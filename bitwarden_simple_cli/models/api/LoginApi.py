from bitwarden_simple_cli.models.response.BaseResponse import BaseResponse


class LoginApi(BaseResponse):
    username: str
    password: str

    def __init__(self, data):
        super().__init__(data)
        if data is None:
            return
        self.username = self.get_response_property_name('Username')
        self.password = self.get_response_property_name('Password')
