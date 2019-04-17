from bitwarden_simple_cli.enums.EncryptionType import EncryptionType
from base64 import b64encode


class SymmetricCryptoKey:
    key = None
    encKey = None
    macKey = None
    encType = None

    keyB64 = None
    encKeyB64 = None
    macKeyB64 = None

    meta = None

    def __init__(self, key, enc_type=None):
        if not key:
            raise Exception('Must provide ke')

        if enc_type is None:
            if len(key) == 32:
                enc_type = EncryptionType.AesCbc256_B64
            elif len(key) == 64:
                enc_type = EncryptionType.AesCbc256_HmacSha256_B64
            else:
                raise Exception('Unable to determine encType.')

        self.key = key
        self.encType = enc_type

        if enc_type == EncryptionType.AesCbc256_B64 and len(key) == 32:
            self.encKey = key
            self.macKey = None
        elif enc_type == EncryptionType.AesCbc128_HmacSha256_B64 and len(key) == 32:
            self.encKey = key[0:16]
            self.macKey = key[16:32]
        elif enc_type == EncryptionType.AesCbc256_HmacSha256_B64 and len(key) == 64:
            self.encKey = key[0:32]
            self.macKey = key[32:64]
        else:
            raise Exception('Unsupported encType/key length.')

        if self.key:
            self.keyB64 = b64encode(self.key)
        if self.encKey:
            self.encKeyB64 = b64encode(self.encKey)
        if self.macKey:
            self.macKeyB64 = b64encode(self.macKey)
