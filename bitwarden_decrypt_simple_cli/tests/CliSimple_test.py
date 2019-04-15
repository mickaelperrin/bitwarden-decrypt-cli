import pytest
from bitwarden_decrypt_simple_cli.CliSimple import CliSimple
from bitwarden_decrypt_simple_cli.__version__ import __version__

BW_SESSION = 'Tyy0rDgzvA/jgHsqUtKIgNnAWaRtHKZoSs6pa10qWQf0QmFtd2/xn8TNJy8Fu2nPRNVDpn3k7tu49W1pQVU8Zg=='
nl = '\n'
uuid_personal = 'fd8870cc-3659-40aa-9492-aa3000cedbb'


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


@pytest.fixture
def no_bw_session(monkeypatch):
    monkeypatch.delenv('BW_SESSION')


@pytest.fixture
def bw_session(monkeypatch):
    monkeypatch.setenv('BW_SESSION', BW_SESSION)


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


def test_get_uuid(cli_get_uuid, capsys, no_bw_session):
    with pytest.raises(SystemExit) as exit_code:
        cli_get_uuid.run()
    std = capsys.readouterr()
    assert std.out.find('BW_SESSION is not set') != -1
    assert exit_code.type == SystemExit
    assert exit_code.value.code == 1


def test_get_uuid(cli_get_uuid, capsys, bw_session):
    cli_get_uuid.run()
    std = capsys.readouterr()
    assert std.out == 'getting password of ' + uuid_personal + nl


def test_get_uuid_username(cli_get_uuid_username, capsys):
    cli_get_uuid_username.run()
    std = capsys.readouterr()
    assert std.out == 'getting username of ' + uuid_personal + nl
