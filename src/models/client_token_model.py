from __future__ import annotations

import time

from sqlalchemy import Column, String, Text, Integer

from . import db


class ClientTokenModel(db.Model):
    __tablename__ = 'client_token'

    """ Specification
      Ref :: from authlib.integrations.sqla_oauth2 import OAuth2TokenMixin
    """
    sequence = Column(Integer, primary_key=True)
    client_id = Column(String(48))
    member_id = Column(String(48))
    token_type = Column(String(40))
    access_token = Column(String(255), unique=True, nullable=False)
    refresh_token = Column(String(255), index=True)
    scope = Column(Text, default='')
    issued_at = Column(
        Integer, nullable=False, default=lambda: int(time.time())
    )
    access_token_revoked_at = Column(Integer, nullable=False, default=0)
    refresh_token_revoked_at = Column(Integer, nullable=False, default=0)
    expires_in = Column(Integer, nullable=False, default=0)

    def check_client(self, client):
        return self.client_id == client.get_client_id()

    def get_scope(self):
        return self.scope

    def get_expires_in(self):
        return self.expires_in

    def is_revoked(self):
        return self.access_token_revoked_at or self.refresh_token_revoked_at

    def is_expired(self):
        if not self.expires_in:
            return False

        expires_at = self.issued_at + self.expires_in
        return expires_at < time.time()
