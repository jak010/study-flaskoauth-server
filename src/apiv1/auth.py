from __future__ import annotations

from typing import TYPE_CHECKING
from flask import jsonify
from flask import (
    Blueprint,
    request

)
from flask import jsonify

from src.oauth2lib.authorization_server import AuthorizationProxy

from dataclasses import dataclass
from typing import Optional

if TYPE_CHECKING:
    pass

auth_api = Blueprint("auth", __name__, url_prefix="/api/auth")


@auth_api.route("", methods=("POST",))
def auth():
    """Input Data
      - client_id,response_type,grant_type,redirect_uri,scope,state
    """

    proxy = AuthorizationProxy()
    #
    print(proxy)
    print(type(proxy))
    print(dir(proxy))

    # oauth_requst = proxy.oauth.create_oauth2_request(request)
    #
    # print(oauth_requst)

    # return proxy.oauth.create_authorization_response(oauth_requst)
    return jsonify()
