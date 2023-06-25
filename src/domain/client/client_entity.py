from dataclasses import dataclass

from src.models import ClientModel


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
            client_metadata=client_model.client_metadata,
        )
