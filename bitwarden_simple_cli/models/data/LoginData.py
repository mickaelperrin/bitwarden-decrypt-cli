from bitwarden_simple_cli.models.api.LoginApi import LoginApi


class LoginData:
    username: str
    password: str

    def __init__(self, data: LoginApi):
        if data is None:
            return

        self.username = data.username
        self.password = data.password

    def __getattr__(self, item):
        return self.item
