from base64 import b64decode, b64encode
from bitwarden_simple_cli.models.domain.SymmetricCryptoKey import SymmetricCryptoKey
from bitwarden_simple_cli.services.CryptoService import CryptoService
from bitwarden_simple_cli.services.StorageService import StorageService
from bitwarden_simple_cli.services.Tools import T
from os import environ as os_environ


class SecureStorageService:

    cryptoService: CryptoService
    storageService: StorageService

    def __init__(self, storage_service: StorageService, crypto_service: CryptoService):
        self.cryptoService = crypto_service
        self.storageService = storage_service

    def decrypt(self, enc_value) -> str:
        try:
            session_key = self._get_session_key()
            if session_key is None:
                return ''
            dec_value = self.cryptoService.decrypt_from_bytes(b64decode(enc_value), session_key)
            if dec_value is None:
                T.error('Failed to decrypt')
                return ''
            return b64encode(dec_value)
        except Exception as e:
            T.error(e)
            T.error('Decrypt error')

    def get(self, key: str):
        value = self.storageService.get(self._make_protected_storage_key(key))
        if value is None:
            return None
        return self.decrypt(value)

    @staticmethod
    def _get_session_key():
        try:
            if os_environ.get('BW_SESSION'):
                return SymmetricCryptoKey(b64decode(os_environ['BW_SESSION']))
        except Exception as e:
            T.error(e)
            print('Session key is invalid.')
        return None

    @staticmethod
    def _make_protected_storage_key(key) -> str:
        return '__PROTECTED__' + key
