from __future__ import annotations

from typing import List

from src.oauth2lib.client_factory import ClientFactory
from src.models.client_model import ClientModel

from src.domain.member import member_service
from src.domain.client.client_entity import ClientEntity

from src.models import Session


def create_client(request_form, grant_type):
    member = member_service.find_member(4)

    if member:
        with Session() as session:
            new_client = ClientFactory.with_type(
                member=member,
                client_name=request_form.client_name,
                client_uri=request_form.client_uri,
                redirect_uri=request_form.redirect_uri,
                client_grant_type=grant_type
            )
            session.add(new_client)

            return ClientEntity.of_model(client_model=new_client)


def get_client_list() -> List[ClientEntity]:
    items = []
    with Session() as session:
        clients = session.query(ClientModel).all()
        for client in clients:
            items.append(ClientEntity.of_model(client_model=client))

    return items
