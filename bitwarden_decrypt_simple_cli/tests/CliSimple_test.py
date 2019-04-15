import pytest
from bitwarden_decrypt_simple_cli.CliSimple import CliSimple
from bitwarden_decrypt_simple_cli.__version__ import __version__

uuid_personal = 'fd8870cc-3659-40aa-9492-aa3000cedbb'
nl = '\n'

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
    return CliSimple('script', 'get', uuid_personal)


@pytest.fixture
def cli_get_uuid_username():
    return CliSimple('script', 'get', uuid_personal, 'username')


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


def test_get_uuid(cli_get_uuid, capsys):
    cli_get_uuid.run()
    std = capsys.readouterr()
    assert std.out == 'getting password of ' + uuid_personal + nl


def test_get_uuid_username(cli_get_uuid_username, capsys):
    cli_get_uuid_username.run()
    std = capsys.readouterr()
    assert std.out == 'getting username of ' + uuid_personal + nl
