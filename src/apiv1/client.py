from flask import Blueprint, request, session, url_for
from flask import render_template, redirect, jsonify
from authlib.oauth2.rfc6749.grants.authorization_code import AuthorizationCodeGrant

from dataclasses import dataclass

from src.domain.client import client_service

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from authlib.integrations.flask_oauth2.authorization_server import AuthorizationServer
    from authlib.oauth2.rfc6749.wrappers import OAuth2Request
    from flask.wrappers import Response

client_api = Blueprint("client", __name__, url_prefix="/api/client")


@client_api.route("", methods=("GET",))
def get_client():
    """ client 조회하기 """
    return jsonify(data={})


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

    client = client_service.add_authorization_client(request_form)

    print(client)

    return jsonify(data={})
