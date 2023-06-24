from flask import Blueprint, request, session, url_for
from flask import render_template, redirect, jsonify
from authlib.oauth2.rfc6749.grants.authorization_code import AuthorizationCodeGrant
from .oauth2 import oauth_server

from .libs.client_factory import ClientFactory
from .model import User
from ..app import db

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from authlib.integrations.flask_oauth2.authorization_server import AuthorizationServer
    from authlib.oauth2.rfc6749.wrappers import OAuth2Request
    from flask.wrappers import Response

bp = Blueprint("index", __name__, url_prefix="/index")


@bp.route("", methods=("GET", "POST"))
def index():
    return jsonify(message='index')


@bp.route("/client", methods=("POST",))
def add_client():
    client = ClientFactory.get_client(client_name="test002")

    db.session.add(client)
    db.session.commit()

    return jsonify(message='index')


@bp.route("/auth", methods=("POST",))
def auth():
    # r = server.create_oauth2_request(request)

    return oauth_server.create_authorization_response(request)


@bp.route("/grant/code", methods=("POST",))
def get_grant_code():
    user = User.query.get(1)
    authorization_code_grant: AuthorizationCodeGrant = oauth_server.get_consent_grant(
        end_user=user,  # DB에 존재하는 사용자를 넣어준다.
        # request=request  # 요청 데이터 그대로 넣어준다.
    )

    return jsonify(code=authorization_code_grant.generate_authorization_code())


@bp.route("/grant/auth", methods=("POST",))
def get_grant_auth():
    user = User.query.get(1)
    grant: AuthorizationCodeGrant = oauth_server.get_consent_grant(end_user=user)

    response: Response = oauth_server.create_authorization_response(grant_user=user)

    return jsonify(
        status=response.status,
        redirect_uri=response.location,
        code=grant.generate_token(),
    )


@bp.route("/grant/client_secret_post", methods=("POST",))
def get_grant_token():
    user = User.query.get(1)
    # auth를 통해 token을 발급받기 위해선 client secret도 필요함
    token_response = oauth_server.create_token_response(request=request)
    print(token_response)

    return token_response


@bp.route("/grant", methods=("POST",))
def grant():
    """ 인증(auth)하기 전에 grant 설정 필요한 듯 """

    # E.g :: 요청 데이터에 들어있는 사용자를 검증한다.
    user = User.query.get(1)

    # AuthorizationCodeGrant, 방식으로 인증된다.
    authorization_code_grant: AuthorizationCodeGrant = oauth_server.get_consent_grant(
        end_user=user,  # DB에 존재하는 사용자를 넣어준다.
        # request=request  # 요청 데이터 그대로 넣어준다.
    )
    redirec_uri = authorization_code_grant.validate_authorization_request()
    authorization_response = authorization_code_grant.create_authorization_response(
        redirect_uri=redirec_uri,
        grant_user=user
    )
    validate_token_request = authorization_code_grant.validate_token_request()

    print("*" * 10)
    print(redirec_uri)
    print(authorization_response)
    print(validate_token_request)
    print("*" * 10)

    # authorization_code_grant.create_token_response()

    return jsonify(index="template")

# oauth_request: OAuth2Request = oauth_server.create_oauth2_request(request=request)
