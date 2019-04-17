from bitwarden_simple_cli.enums.EncryptionType import EncryptionType
from bitwarden_simple_cli.services.Tools import T
import bitwarden_simple_cli.services.ContainerService as ContainerService


class CipherString:

    encryptedString: str = None
    encryptionType: EncryptionType = None
    decryptedValue: str = None
    data: str = None
    ic: str = None
    mac: str = None

    def __init__(self, encrypted_string_or_type: str, data: str = None, iv: str = None, mac: str = None):
        if data:
            enc_type = EncryptionType(encrypted_string_or_type)
            self.encryptedString = encrypted_string_or_type + '.' + data

            if iv:
                self.encryptedString += '|' + iv

            if mac:
                self.encryptedString += '|' + mac

            self.encryptionType = enc_type
            self.data = data
            self.iv = iv
            self.mac = mac
            return

        self.encryptedString = str(encrypted_string_or_type)
        if self.encryptedString is None:
            return

        header_pieces = self.encryptedString.split('.')
        if len(header_pieces) == 2:
            try:
                self.encryptionType = EncryptionType(int(header_pieces[0]))
                enc_pieces = header_pieces[1].split('|')
            except Exception as e:
                T.error(e)
                return
        else:
            enc_pieces = self.encryptedString.split('|')
            self.encryptionType = EncryptionType.AesCbc128_HmacSha256_B64 \
                if len(enc_pieces) == 3 else EncryptionType.AesCbc256_B64

        if self.encryptionType == EncryptionType.AesCbc128_HmacSha256_B64 \
                or self.encryptionType == EncryptionType.AesCbc256_HmacSha256_B64:
            if len(enc_pieces) != 3:
                return
            self.iv = enc_pieces[0]
            self.data = enc_pieces[1]
            self.mac = enc_pieces[2]
        elif self.encryptionType == EncryptionType.AesCbc256_B64:
            if len(enc_pieces) != 2:
                return
            self.iv = enc_pieces[0]
            self.data = enc_pieces[1]
        elif self.encryptionType == EncryptionType.Rsa2048_OaepSha256_B64 \
                or self.encryptionType == EncryptionType.Rsa2048_OaepSha1_B64:
            if len(enc_pieces) != 1:
                return
            self.data = enc_pieces[0]
        else:
            return

    def decrypt(self, org_id):
        if self.decryptedValue:
            return self.decryptedValue

        cypto_service = ContainerService.ContainerService().get_crypto_service()
        if not cypto_service:
            raise Exception('Container service not initialized')

        try:
            org_key = cypto_service.get_org_key(org_id)
            self.decryptedValue = cypto_service.decrypt_to_utf8(self, org_key)
        except Exception as e:
            T.error(e)
            self.decryptedValue = '[error: cannot decrypt]'
        return self.decryptedValue
