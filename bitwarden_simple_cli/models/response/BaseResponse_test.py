import pytest
from bitwarden_simple_cli.models.response.BaseResponse import BaseResponse
from bitwarden_simple_cli.tests.fixtures_common import common_data


@pytest.fixture()
def base_response():
    return BaseResponse(common_data('cipher_response'))


def test_base_response_get_response_property_name(base_response: BaseResponse):
    uuid = 'fd8870cc-3659-40aa-9492-aa3000cedbb3'
    assert base_response.get_response_property_name('userId') == common_data('user_id')
    assert base_response.get_response_property_name('UserId') == common_data('user_id')
    assert base_response.get_response_property_name('Id') == uuid
    assert base_response.get_response_property_name('id') == uuid
    assert base_response.get_response_property_name('ID') == uuid
