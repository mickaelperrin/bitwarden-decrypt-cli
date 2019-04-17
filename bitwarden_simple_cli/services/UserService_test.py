from bitwarden_simple_cli.services.UserService import UserService
from bitwarden_simple_cli.tests.fixtures_common import user_service, common_data


def test_cipher_service(user_service: UserService):
    assert user_service.get_user_id() == common_data('user_id')
