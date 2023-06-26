from __future__ import annotations

from typing import TYPE_CHECKING
from urllib.parse import urlparse, parse_qs

from flask import (
    Blueprint,
    request,
    Request
)
from flask import jsonify

from app import proxy
from src.domain.client import client_service
from src.domain.member import member_service

if TYPE_CHECKING:
    from flask.wrappers import Response as FlaskResponse
    from authlib.oauth2.rfc6749.grants.authorization_code import AuthorizationCodeGrant

token_api = Blueprint("token", __name__, url_prefix="/api/auth")


@token_api.route("/token", methods=("POST",))
def get_token():
    """ AuthorizationCode를 통해 Token 발급받기

    ReuestData
    - client_id, client_secret, code, grant_type, redirect_uri, response_type

    """
    user = member_service.find_member(sequence=1)

    # auth를 통해 token을 발급받기 위해선 client secret도 필요함
    token_response = proxy.oauth.create_token_response(request=request)
    print(token_response)

    return token_response
