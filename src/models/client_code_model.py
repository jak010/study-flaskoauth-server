import time
from sqlalchemy import Column, String, Text, Integer

from . import db


class ClientCodeModel(db.Model):
    __tablename__ = 'client_code'

    sequence = Column(Integer, primary_key=True)
    code = Column(String(120), unique=True, nullable=False)
    client_id = Column(String(48))
    redirect_uri = Column(Text, default='')
    response_type = Column(Text, default='')
    scope = Column(Text, default='')
    nonce = Column(Text)
    auth_time = Column(
        Integer, nullable=False,
        default=lambda: int(time.time())
    )

    code_challenge = Column(Text)
    code_challenge_method = Column(String(48))

    def is_expired(self):
        return self.auth_time + 300 < time.time()

    def get_redirect_uri(self):
        return self.redirect_uri

    def get_scope(self):
        return self.scope

    def get_auth_time(self):
        return self.auth_time

    def get_nonce(self):
        return self.nonce
