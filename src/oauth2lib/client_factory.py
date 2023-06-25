from __future__ import annotations

import json
import time

from werkzeug.security import gen_salt
from src.domain.member.member_entity import MemberEntity

from src.models import ClientModel
from typing import Literal


class ClientFactory:
    """ grant type에 따라 ClientModel을 생성해줌 """

    @classmethod
    def with_type(cls,
                  member: MemberEntity,
                  client_name: str,
                  client_uri: str,
                  redirect_uri: str,
                  client_grant_type: Literal["authorization_code"]
                  ):
        _new_client = cls(
            member=member,
            client_name=client_name,
            client_uri=client_uri,
            redirect_uris=redirect_uri,
        )

        if client_grant_type == 'authorization_code':
            return _new_client.authorization_code_client()

    def __init__(
            self,
            member: MemberEntity,
            client_name: str,
            client_uri: str,
            redirect_uris: str,
    ):
        self.member = member
        self.client_name = client_name
        self.client_uri = client_uri
        self.redirect_uris = redirect_uris

    @property
    def _client_id(self):
        return gen_salt(24)

    @property
    def _client_secret(self):
        return gen_salt(48)

    @property
    def _client_id_issued_at(self):
        return int(time.time())

    @property
    def _client_secret_expires_at(self):
        return int(time.time()) + 86400

    def authorization_code_client(self):
        # TODO: Entity 모델로 변경해야될지 고민해봐야됨
        return ClientModel(
            member_sequence=self.member.sequence,
            client_id=self._client_id,
            client_secret=self._client_secret,
            client_id_issued_at=self._client_id_issued_at,
            client_secret_expires_at=self._client_secret_expires_at,
            client_metadata=json.dumps({
                'client_name': self.client_name,
                'client_uri': self.client_uri,
                'redirect_uris': [self.redirect_uris],
                'response_type': 'code',
                'grant_types': ['authorization_code']
            })
        )
