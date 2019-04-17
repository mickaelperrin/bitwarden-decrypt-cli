import pytest
from json import loads as json_loads
from os import path
from bitwarden_decrypt_simple_cli.services.StorageService import StorageService
from bitwarden_decrypt_simple_cli.services.SecureStorageService import SecureStorageService
from bitwarden_decrypt_simple_cli.services.CryptoService import CryptoService
from bitwarden_decrypt_simple_cli.services.UserService import UserService
from bitwarden_decrypt_simple_cli.services.CipherService import CipherService
from bitwarden_decrypt_simple_cli.models.response.CipherResponse import CipherResponse


def common_data(item):
    cipher_response = '{ \
          "id": "fd8870cc-3659-40aa-9492-aa3000cedbb3",\
          "organizationId": null,\
          "folderId": null,\
          "userId": "03780246-7f1d-4221-8615-aa3000cd8123",\
          "edit": true,\
          "organizationUseTotp": false,\
          "favorite": false,\
          "revisionDate": "2019-04-15T12:33:08.86Z",\
          "type": 1,\
          "name": "2.0kujUcYqA6RWlE48DHI65A==|9dihaVyPdkV2v063b8HrIA==|fe7GxuKn3pOkAr1iCVUCt1nmBpqwzFb6FKOR51Ck2Do=",\
          "notes": "2.UEB/CebzJLPkgGJ0htun1g==|bX5nHZtvkMKl3b/7OHCuOg==|m9j9A/HDG5Rw4bO2bHCVeQ3tMYT1ij85tZIw2DPbk0k=",\
          "collectionIds": [],\
          "login": {\
            "username": "2.VCFAUwS1C2y8hgD++BnDkQ==|Eh5Yno4nP6r347/GWL+/l6GQfavxtcPFBmvwzR6Tg9Q=|rghduKsyaAo75q5NLmFiHER16+Tv7Jf49zzl4ks6M14=", \
            "password": "2.bg59wtouG3ERlX1FThUUOA==|3/ovu/2ADKNnjpq7OjjoIttiSeqUDOrguYGcZNhKU34=|QcgJxBN6ea1Fbo3J0V8n3F9tUcAumfA3e01nDN+ihN8=", \
            "passwordRevisionDate": null, \
            "totp": null, \
            "uris": [ \
              { \
                "match": null, \
                "uri": "2.kS2d1arj/MM9h+mIW9RMAQ==|CNdUog9M8mByYXTFgkbYRg==|RC89j2K9sNcxqDf9f+aujnQm0LRNwXvqKQK0lIipDXQ=" \
              }, \
              { \
                "match": null, \
                "uri": "2.XnKvUBwgh4rVhlc2Kswqgg==|FCGHFqpj5jOWnS+SCmvF/A==|TPiRhI4mAZg05wEyXV7VdCbiQo0EVZ0BagDJrvxWcOw=" \
              } \
            ] \
          },\
          "fields": [\
            {\
              "type": 0,\
              "name": "2.8cD6Lg0308EZTEgeiuvDhQ==|rbd5+MnoZmzm9ZGI2mB0iQzJ7HysVkQFXue48eAN0eA=|vyLz6vqsIFSHdW7xQmwzbg5jm2hsUb/pS/9aIYvS1Fs=",\
              "value": "2.OEt4B5y21WB5tmkd6Gmk5w==|vXsHoRujWZj2OZNA9/iF5bIlBeWa0pI+ttr8/rgxAjA=|MZ/DDsntVddSFoY3mUPNe3JBUjCOc1ZK4PIEin9L0Oo="\
            },\
            {\
              "type": 1,\
              "name": "2.p0BEx6HRXvfA+0TeHFi4nA==|UW5dXnW4rlQocnHOTcLM/FOlQLbjQh/k+g65Yrh6COw=|jq42Sp0sgs6H+DyuLEDQ5UY7sbRj4DYMr8PAVD5G+OU=",\
              "value": "2.si7K0uetUvT5BUAeFskx9Q==|4iKxRN3/6TUfhRWXGQijsaS3K7NTlE5v04WqhfeCcH8=|Dgo2TwZHRxeyLID/LkKBQIPvc5IJatbupFOiIc15K4E="\
            },\
            {\
              "type": 2,\
              "name": "2.49fH9DjGRS6RRTL4I9zZSg==|/k3uffKs1wQbdQU1oFnt6YbBHVtd/tl2XQQQbkPdtWM=|2vrIYiZnFhHk0hx0lNdIo8FkQDKJlmDRIDDpj9hyvhw=",\
              "value": "2.53eXq9PhlhbUH1QASmZvKg==|djHCRO2WazzxcL2mjzxF5Q==|UVXokiiqBb/9rb/VQ+gOa6PpV0iifc1Ye5AhHMqClG0="\
            },\
            {\
              "type": 2,\
              "name": "2.QDn0bwKJbEgjWAATLJqWAg==|Csoq4Sr6O8byHZoiU70PwyBt9txNTN2Fjz2sl9ZD190=|nwzx3YGpgxk2Tu/bg0M8CEF+yHU4zhjfQOGxjSZVpUQ=",\
              "value": "2.zGBCnWTtRfxuuwdr8MstVw==|RX24BmIJvcef9/A95Idbhg==|jr+Wp+kiBsvAp/HbsXRxr1WSqNDnyQATfdl9Y2nuTBU="\
            }\
          ]\
        }'
    return dict(
        BW_SESSION='Tyy0rDgzvA/jgHsqUtKIgNnAWaRtHKZoSs6pa10qWQf0QmFtd2/xn8TNJy8Fu2nPRNVDpn3k7tu49W1pQVU8Zg==',
        cipher_response=json_loads(cipher_response),
        nl='\n',
        organization_id='1ff51ccd-0a25-46a2-a3cd-aa3000cfa874',
        protected_key='ArxoewBOPtCYZKqn34f8CoMQVUrNZnrhGU9OYuJu8UpB7DngEwf/TEHjbxPJJhUDG+DnPQR76J9d12/4tnGT5C6ZaLxxInRooT4AuX2ljIrSppCee1AvzIMu7ljGhR++ng==',
        protected_key_decoded=b'/lCGAMDGAq+mjRP3FJv+VNDDnbrYcVGnsiPeXTm4NfU=',
        test_database_filename='data.json',
        user_email='dev+bitwarden@mickaelperrin.fr',
        user_id='03780246-7f1d-4221-8615-aa3000cd8123',
        uuid_login_organization='fe6e74aa-a099-4cc1-ae8e-aa3000d02c14',
        uuid_login_personal='fd8870cc-3659-40aa-9492-aa3000cedbb3',
        uuid_note_personal='450cbad2-580b-4523-bce8-aa3000cf641a'
    ).get(item)


@pytest.fixture
def no_bw_session(monkeypatch):
    monkeypatch.delenv('BW_SESSION')


@pytest.fixture
def bw_session(monkeypatch):
    monkeypatch.setenv('BW_SESSION', common_data('BW_SESSION'))
    monkeypatch.setenv('BITWARDENCLI_APPDATA_DIR', path.dirname(__file__))


@pytest.fixture
def storage_service():
    return StorageService(path.join(path.dirname(__file__), common_data('test_database_filename')))


@pytest.fixture()
def secure_storage_service():
    storage_service = StorageService(path.join(path.dirname(__file__), common_data('test_database_filename')))
    return SecureStorageService(storage_service, CryptoService(storage_service))


@pytest.mark.usefixtures("bw_session")
@pytest.fixture()
def crypto_service():
    storage_service = StorageService(path.join(path.dirname(__file__), common_data('test_database_filename')))
    return CryptoService(storage_service)


@pytest.fixture()
def user_service():
    storage_service = StorageService(path.join(path.dirname(__file__), common_data('test_database_filename')))
    return UserService(storage_service)


@pytest.fixture()
def cipher_service():
    storage_service = StorageService(path.join(path.dirname(__file__), common_data('test_database_filename')))
    user_service = UserService(storage_service)
    return CipherService(storage_service, user_service)


@pytest.fixture()
def cipher_response():
    return CipherResponse(common_data('cipher_response'))
