from . import db

from sqlalchemy import Column, Integer, String, Text

from authlib.integrations.sqla_oauth2 import OAuth2ClientMixin

from authlib.oauth2.rfc6749 import ClientMixin
import json


class ClientModel(db.Model):
    __tablename__ = 'client'

    sequence = Column(Integer, primary_key=True)
    member_sequence = Column(Integer, nullable=False)
    client_id = Column(String(48), index=True)
    client_secret = Column(String(120))
    client_id_issued_at = Column(Integer, nullable=False, default=0)
    client_secret_expires_at = Column(Integer, nullable=False, default=0)
    client_metadata = Column('client_metadata', Text)

    """json
    - client metadata는 적어도 아래의 정보를 가지고 있어야함
      - 아래 예시에서 response_types와, grent_types는 AuthorizationCodeGrant에서 요구하는 스펙이다.
    {
        "client_name": "",
        "client_uri": "",
        "redirect_uris":"",
        "response_types":"code",
        ”grant_types”: [”authorization_code”]
    }
    """

    @property
    def client_metadata_dict(self):
        """ class 내부에 client_metadata를 dict로 다루기 위해 분리함 """
        data = json.loads(self.client_metadata)
        self.__dict__['client_metadata_dict'] = data
        return data

    @property
    def redirect_uris(self):
        return self.client_metadata_dict.get('redirect_uris', [])

    @property
    def response_types(self):
        return self.client_metadata_dict.get('response_types', [])

    def check_redirect_uri(self, redirect_uri):
        return redirect_uri in self.redirect_uris

    def check_response_type(self, response_type):
        return response_type in self.response_types
