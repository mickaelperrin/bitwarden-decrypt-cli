import pytest
from bitwarden_simple_cli.models.response.CipherResponse import CipherResponse
from bitwarden_simple_cli.tests.fixtures_common import common_data, cipher_response
from bitwarden_simple_cli.models.api.LoginApi import LoginApi
from bitwarden_simple_cli.models.api.FieldApi import FieldApi


def test_base_response_get_response_property_name(cipher_response: CipherResponse):
    assert cipher_response.name == '2.0kujUcYqA6RWlE48DHI65A==|9dihaVyPdkV2v063b8HrIA==|fe7GxuKn3pOkAr1iCVUCt1nmBpqwzFb6FKOR51Ck2Do='
    assert cipher_response.id == 'fd8870cc-3659-40aa-9492-aa3000cedbb3'
    assert cipher_response.organizationId is None
    assert cipher_response.type == 1
    assert isinstance(cipher_response.login, LoginApi)
    assert cipher_response.login.username == '2.VCFAUwS1C2y8hgD++BnDkQ==|Eh5Yno4nP6r347/GWL+/l6GQfavxtcPFBmvwzR6Tg9Q=|rghduKsyaAo75q5NLmFiHER16+Tv7Jf49zzl4ks6M14='
    assert cipher_response.login.password == '2.bg59wtouG3ERlX1FThUUOA==|3/ovu/2ADKNnjpq7OjjoIttiSeqUDOrguYGcZNhKU34=|QcgJxBN6ea1Fbo3J0V8n3F9tUcAumfA3e01nDN+ihN8='
    assert type(cipher_response.fields).__name__ == 'list'
    assert len(cipher_response.fields) == 4
    field = cipher_response.fields[0]
    assert isinstance(field, FieldApi)
    assert field.type == 0
    assert field.name == '2.8cD6Lg0308EZTEgeiuvDhQ==|rbd5+MnoZmzm9ZGI2mB0iQzJ7HysVkQFXue48eAN0eA=|vyLz6vqsIFSHdW7xQmwzbg5jm2hsUb/pS/9aIYvS1Fs='
    assert field.value == '2.OEt4B5y21WB5tmkd6Gmk5w==|vXsHoRujWZj2OZNA9/iF5bIlBeWa0pI+ttr8/rgxAjA=|MZ/DDsntVddSFoY3mUPNe3JBUjCOc1ZK4PIEin9L0Oo='


