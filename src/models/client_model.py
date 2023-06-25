from . import db

from sqlalchemy import Column, Integer, String, Text

from authlib.integrations.sqla_oauth2 import OAuth2ClientMixin


class ClientModel(db.Model, OAuth2ClientMixin):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)

    client_id = Column(String(48), index=True)
    client_secret = Column(String(120))
    client_id_issued_at = Column(Integer, nullable=False, default=0)
    client_secret_expires_at = Column(Integer, nullable=False, default=0)

    _client_metadata = Column('client_metadata', Text)
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
