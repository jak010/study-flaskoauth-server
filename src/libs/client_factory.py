import time

from werkzeug.security import gen_salt

from ..model import Client
import json


def get_random_client_id():
    return gen_salt(24)


def get_random_client_secret():
    return gen_salt(48)


class ClientFactory:

    @classmethod
    def get_client(cls, client_name: str):
        return cls(
            client_name=client_name,
            client_uri="http://localhost:5000"
        ).emit()

    def __init__(self, client_name: str, client_uri: str):
        self.client_name = client_name
        self.client_uri = client_uri

        self._client_id = get_random_client_id()
        self.client_id_issued_at = int(time.time())

        self.client_secret = get_random_client_secret()
        self.client_secret_expires_at = int(time.time()) + 86400

    def emit(self) -> Client:
        return Client(
            user_id='1',
            client_id=self.client_id,
            client_id_issued_at=self.client_id_issued_at,
            client_secret=self.client_secret,
            client_secret_expires_at=self.client_secret_expires_at,
            _client_metadata=json.dumps({
                'client_name': self.client_name,
                'client_uri': self.client_uri
            })
        )
