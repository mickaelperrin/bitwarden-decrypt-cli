import os
import pytest
from bitwarden_simple_cli.services.StorageService import StorageService
from bitwarden_simple_cli.tests.fixtures_common import storage_service, common_data


def test_storage_service_init_without_db_path():
    storage_service = StorageService()
    assert os.path.isfile(storage_service.database_path)


@pytest.mark.usefixtures("storage_service")
def test_storage_service_init_without_db_path(storage_service):
    assert os.path.isfile(storage_service.database_path)
    assert os.path.basename(storage_service.database_path) == common_data('test_database_filename')
    assert storage_service.database is not None
    assert storage_service.database.get('userEmail') == common_data('user_email')
    assert storage_service.database.get('userId') == common_data('user_id')
    assert storage_service.database.get('__PROTECTED__key') == common_data('protected_key')
    assert 'ciphers_' + common_data('user_id') in storage_service.database
    assert 'organizations_' + common_data('user_id') in storage_service.database
    assert common_data('organization_id') in storage_service.database['organizations_' + common_data('user_id')]
