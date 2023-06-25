from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from flask import Blueprint, request
from flask import jsonify

from src.domain.client import client_service

if TYPE_CHECKING:
    pass

client_api = Blueprint("client", __name__, url_prefix="/api/client")


@client_api.route("", methods=("GET",))
def get_client():
    """ client 조회하기 """
    client_list = client_service.get_client_list()
    return jsonify(data={
        'items': [{
            "sequence": client.sequence,
            "member_sequence": client.member_sequence,
            "client_id": client.client_id,
            "client_secret": client.client_secret,
            "client_id_issued_at": client.client_id_issued_at,
            "client_secret_expires_at": client.client_secret_expires_at,
            "client_metadata": {
                'client_name': client.client_name,
                'client_uri': client.client_uri,
                'redirect_uris': client.redirect_uris,
                'response_type': client.response_type
            }
        } for client in client_list]
    })


@client_api.route("", methods=("POST",))
def add_client():
    """ client 등록하기 """

    @dataclass
    class RequestForm:
        client_name: str
        client_uri: str
        redirect_uri: str

    request_form = RequestForm(
        client_name=request.form['client_name'],
        client_uri=request.form['client_uri'],
        redirect_uri=request.form['redirect_uri']
    )

    client = client_service.create_client(
        request_form=request_form,
        grant_type="authorization_code"
    )

    return jsonify(data={
        'client_id': client.client_id,
        'client_secret': client.client_secret,
        'client_id_issued_at': client.client_id_issued_at
    })
