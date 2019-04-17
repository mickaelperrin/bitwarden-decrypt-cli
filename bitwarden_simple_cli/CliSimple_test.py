import pytest
from bitwarden_simple_cli.CliSimple import CliSimple
from bitwarden_simple_cli.__version__ import __version__
from bitwarden_simple_cli.tests.fixtures_common import common_data, bw_session, no_bw_session

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
    return CliSimple('script', 'get', common_data('uuid_login_personal'))


@pytest.fixture
def cli_get_uuid_username():
    return CliSimple('script', 'get', common_data('uuid_login_personal'), 'username')


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
    assert std.out == 'login_p_password'


@pytest.mark.usefixtures("bw_session")
def test_get_login_organization_password(cli_get_uuid_username, capsys):
    CliSimple('script', 'get', common_data('uuid_login_organization'), 'password').run()
    std = capsys.readouterr()
    assert std.out == 'acme_login1_password'


@pytest.mark.usefixtures("bw_session")
def test_get_login_personal_username(cli_get_uuid_username, capsys):
    cli_get_uuid_username.run()
    std = capsys.readouterr()
    assert std.out == 'login_p_username'


@pytest.mark.usefixtures("bw_session")
def test_get_login_organization_username(cli_get_uuid_username, capsys):
    CliSimple('script', 'get', common_data('uuid_login_organization'), 'username').run()
    std = capsys.readouterr()
    assert std.out == 'acme_login1'


@pytest.mark.usefixtures("bw_session")
def test_get_login_personal_uri(capsys):
    CliSimple('script', 'get', common_data('uuid_login_personal'), 'uri').run()
    std = capsys.readouterr()
    assert std.out == 'login_p_uri1'


@pytest.mark.usefixtures("bw_session")
def test_get_login_organization_uri(cli_get_uuid_username, capsys):
    CliSimple('script', 'get', common_data('uuid_login_organization'), 'uri').run()
    std = capsys.readouterr()
    assert std.out == 'acme_login1_url1'


@pytest.mark.usefixtures("bw_session")
def test_get_login_personal_uris(capsys):
    CliSimple('script', 'get', common_data('uuid_login_personal'), 'uris').run()
    std = capsys.readouterr()
    assert std.out == 'login_p_uri1\nlogin_p_uri2\n'


@pytest.mark.usefixtures("bw_session")
def test_get_login_organization_uris(cli_get_uuid_username, capsys):
    CliSimple('script', 'get', common_data('uuid_login_organization'), 'uris').run()
    std = capsys.readouterr()
    assert std.out == 'acme_login1_url1\nacme_login2_url2\n'


@pytest.mark.usefixtures("bw_session")
def test_get_login_personal_name(capsys):
    CliSimple('script', 'get', common_data('uuid_login_personal'), 'name').run()
    std = capsys.readouterr()
    assert std.out == 'login personnal'


@pytest.mark.usefixtures("bw_session")
def test_get_login_organization_name(cli_get_uuid_username, capsys):
    CliSimple('script', 'get', common_data('uuid_login_organization'), 'name').run()
    std = capsys.readouterr()
    assert std.out == 'acme login 1'


@pytest.mark.usefixtures("bw_session")
def test_get_login_personal_notes(capsys):
    CliSimple('script', 'get', common_data('uuid_login_personal'), 'notes').run()
    std = capsys.readouterr()
    assert std.out == 'login_p_notes'


@pytest.mark.usefixtures("bw_session")
def test_get_login_organization_notes(cli_get_uuid_username, capsys):
    CliSimple('script', 'get', common_data('uuid_login_organization'), 'notes').run()
    std = capsys.readouterr()
    assert std.out == 'acme_login1_note'


@pytest.mark.usefixtures("bw_session")
def test_get_note_personal_notes(capsys):
    CliSimple('script', 'get', common_data('uuid_note_personal'), 'notes').run()
    std = capsys.readouterr()
    assert std.out == 'note_p_content'


@pytest.mark.usefixtures("bw_session")
def test_get_note_personal_name(capsys):
    CliSimple('script', 'get', common_data('uuid_note_personal'), 'name').run()
    std = capsys.readouterr()
    assert std.out == 'note personal'


@pytest.mark.usefixtures("bw_session")
def test_get_login_organization_custom_field_text(cli_get_uuid_username, capsys):
    CliSimple('script', 'get', common_data('uuid_login_organization'), 'acme_login1_customfield_text1').run()
    std = capsys.readouterr()
    assert std.out == 'acme_login1_customfield_text1_value'


@pytest.mark.usefixtures("bw_session")
def test_get_login_personal_custom_field_text(cli_get_uuid_username, capsys):
    CliSimple('script', 'get', common_data('uuid_login_personal'), 'login_p_custom_text').run()
    std = capsys.readouterr()
    assert std.out == 'login_p_custom_text_value'


@pytest.mark.usefixtures("bw_session")
def test_get_login_personal_custom_field_hidden(cli_get_uuid_username, capsys):
    CliSimple('script', 'get', common_data('uuid_login_personal'), 'login_p_custom_hidden').run()
    std = capsys.readouterr()
    assert std.out == 'login_p_custom_hidden_value'


@pytest.mark.usefixtures("bw_session")
def test_get_login_personal_custom_field_unchecked(cli_get_uuid_username, capsys):
    CliSimple('script', 'get', common_data('uuid_login_personal'), 'login_p_custom_unchecked').run()
    std = capsys.readouterr()
    assert std.out == 'false'


@pytest.mark.usefixtures("bw_session")
def test_get_note_personal_customfield(capsys):
    CliSimple('script', 'get', common_data('uuid_note_personal'), 'note_p_custom_field_text').run()
    std = capsys.readouterr()
    assert std.out == 'note_p_custom_field_text_value'


@pytest.mark.usefixtures("bw_session")
def test_list(capsys):
    CliSimple('script', 'list').run()
    std = capsys.readouterr()
    assert std.out == \
"fe6e74aa-a099-4cc1-ae8e-aa3000d02c14 acme login 1\n\
fd8870cc-3659-40aa-9492-aa3000cedbb3 login personnal\n\
450cbad2-580b-4523-bce8-aa3000cf641a note personal\n"