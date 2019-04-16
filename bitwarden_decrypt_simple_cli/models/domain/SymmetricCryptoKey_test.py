import pytest
from bitwarden_decrypt_simple_cli.models.domain.SymmetricCryptoKey import SymmetricCryptoKey
from bitwarden_decrypt_simple_cli.tests.fixtures_common import common_data
from base64 import b64decode


def test_symmetric_crypto_key():
    key=b64decode(common_data('protected_key_decoded'))
    sck = SymmetricCryptoKey(key)
    assert int(sck.encType) == 0
    assert sck.encKey == key
    assert sck.macKey is None

