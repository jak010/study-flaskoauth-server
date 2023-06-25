from dataclasses import dataclass

from src.models import ClientModel
import json


@dataclass
class ClientEntity:
    sequence: int
    member_sequence: int
    client_id: str
    client_secret: str
    client_id_issued_at: int
    client_secret_expires_at: int
    client_metadata: dict

    @classmethod
    def of_model(cls, client_model: ClientModel):
        return cls(
            sequence=client_model.sequence,
            member_sequence=client_model.member_sequence,
            client_id=client_model.client_id,
            client_secret=client_model.client_secret,
            client_id_issued_at=client_model.client_id_issued_at,
            client_secret_expires_at=client_model.client_secret_expires_at,
            client_metadata=json.loads(client_model.client_metadata),
        )

    @property
    def client_name(self):
        return self.client_metadata.get('client_name', None)

    @property
    def client_uri(self):
        return self.client_metadata.get('client_uri', None)

    @property
    def redirect_uris(self):
        return self.client_metadata.get('redirect_uris', None)

    @property
    def response_type(self):
        return self.client_metadata.get('response_type', None)
