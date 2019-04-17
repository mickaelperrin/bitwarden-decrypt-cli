import pytest
from bitwarden_simple_cli.models.domain.SymmetricCryptoKey import SymmetricCryptoKey
from bitwarden_simple_cli.tests.fixtures_common import common_data
from base64 import b64decode, b64encode


def test_symmetric_crypto_key_aes_cbc_256_b64():
    key = b64decode(common_data('protected_key_decoded'))
    sck = SymmetricCryptoKey(key)
    assert sck.encType.value == 0
    assert sck.encKey == key
    assert sck.macKey is None


def test_symmetric_crypto_key_aes_cbc_256_hmac_sha_256_b64():
    key = b64decode(common_data('BW_SESSION'))
    sck = SymmetricCryptoKey(key)
    assert sck.encType.value == 2
    assert sck.encKeyB64 == b'Tyy0rDgzvA/jgHsqUtKIgNnAWaRtHKZoSs6pa10qWQc='
    assert sck. macKeyB64 == b'9EJhbXdv8Z/EzScvBbtpz0TVQ6Z95O7buPVtaUFVPGY='