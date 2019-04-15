import pytest
from os import path
from bitwarden_decrypt_simple_cli.services.StorageService import StorageService


def common_data(item):
    return dict(
        BW_SESSION='Tyy0rDgzvA/jgHsqUtKIgNnAWaRtHKZoSs6pa10qWQf0QmFtd2/xn8TNJy8Fu2nPRNVDpn3k7tu49W1pQVU8Zg==',
        nl='\n',
        test_database_filename='bitwarden_db.json',
        uuid_personal='fd8870cc-3659-40aa-9492-aa3000cedbb'
    ).get(item)


@pytest.fixture
def no_bw_session(monkeypatch):
    monkeypatch.delenv('BW_SESSION')


@pytest.fixture
def bw_session(monkeypatch):
    monkeypatch.setenv('BW_SESSION', common_data('BW_SESSION'))


@pytest.fixture
def db_test():
    return StorageService(path.join(path.dirname(__file__), common_data('test_database_filename')))