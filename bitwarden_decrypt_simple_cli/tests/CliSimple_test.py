import pytest
from bitwarden_decrypt_simple_cli.CliSimple import CliSimple
from bitwarden_decrypt_simple_cli.__version__ import __version__
from bitwarden_decrypt_simple_cli.tests.fixtures_common import common_data, bw_session, no_bw_session

nl = common_data("nl")

@pytest.fixture
def cli_version():
    return CliSimple('script', 'version')


@pytest.fixture
def cli_empty():
    return CliSimple('script')


@pytest.fixture
def cli_get_empty():
    return CliSimple('script', 'get')


@pytest.fixture
def cli_get_uuid():
    return CliSimple('script', 'get', common_data('uuid_personal'))


@pytest.fixture
def cli_get_uuid_username():
    return CliSimple('script', 'get', common_data('uuid_personal'), 'username')


def test_version(cli_version, capsys):
    cli_version.run()
    std = capsys.readouterr()
    assert std.out == 'Version: ' + __version__ + nl


def test_get_empty(cli_get_empty, capsys):
    with pytest.raises(SystemExit) as exit_code:
        cli_get_empty.run()
    std = capsys.readouterr()
    assert exit_code.type == SystemExit
    assert exit_code.value.code == 1
    assert std.out.find('Error:') != -1
    assert std.out.find('Usage:') != -1


@pytest.mark.usefixtures("no_bw_session")
def test_get_uuid(cli_get_uuid, capsys, no_bw_session):
    with pytest.raises(SystemExit) as exit_code:
        cli_get_uuid.run()
    std = capsys.readouterr()
    assert std.out.find('BW_SESSION is not set') != -1
    assert exit_code.type == SystemExit
    assert exit_code.value.code == 1


@pytest.mark.usefixtures("bw_session")
def test_get_uuid(cli_get_uuid, capsys, bw_session):
    cli_get_uuid.run()
    std = capsys.readouterr()
    assert std.out == 'getting password of ' + common_data('uuid_personal') + nl


def test_get_uuid_username(cli_get_uuid_username, capsys):
    cli_get_uuid_username.run()
    std = capsys.readouterr()
    assert std.out == 'getting username of ' + common_data('uuid_personal') + nl
