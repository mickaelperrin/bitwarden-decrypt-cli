import pytest


@pytest.fixture()
def common_data():
    return dict(
        BW_SESSION='Tyy0rDgzvA/jgHsqUtKIgNnAWaRtHKZoSs6pa10qWQf0QmFtd2/xn8TNJy8Fu2nPRNVDpn3k7tu49W1pQVU8Zg==',
        nl='\n',
        uuid_personal='fd8870cc-3659-40aa-9492-aa3000cedbb'
    )

@pytest.fixture
def no_bw_session(monkeypatch):
    monkeypatch.delenv('BW_SESSION')


@pytest.fixture
def bw_session(monkeypatch):
    monkeypatch.setenv('BW_SESSION', BW_SESSION)