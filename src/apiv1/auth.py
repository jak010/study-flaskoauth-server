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

auth_api = Blueprint("auth", __name__, url_prefix="/api/auth")


@auth_api.route("/code", methods=("POST",))
def code():
    """Input Data
      - client_id,response_type,grant_type,redirect_uri,scope,state
    # 1. 등록된 client_id의 redirect_uri로 향하는 서버가 열려있어야함 (python -m http.server 5002)
    # 2. AuthorizationCode를 등록할 수 있게 save_authorization_code() 가 선언되어있어야함
    """

    client = client_service.get_client(request.form['client_id'])
    grant_member = member_service.find_member(sequence=client.member_sequence)

    oauth_requst = proxy.oauth.create_oauth2_request(request)

    # grant_user에 대한 검증은 grants.authorization_code_grant에서 이뤄진다.
    # - create_authorization_response에서 사용하는 grant_user에 대한 검증은 인수를 입력받았는지 아니지임

    response: FlaskResponse = proxy.oauth.create_authorization_response(
        request=oauth_requst, grant_user=grant_member
    )

    def get_data(response):
        parsed_url = urlparse(response.location)
        query = parse_qs(parsed_url.query)

        return {
            "redirect_url": parsed_url.netloc,
            "authorization_code": query.get('code', None)[0]
        }

    _data = get_data(response)

    return jsonify(data={
        'redirect_url': _data['redirect_url'],
        'authorization_code': _data['authorization_code']
    })


@auth_api.route("/code/data", methods=("GET",))
def code_only_data():
    """ AuthorizationCode 발급 시 데이터를 참조하기 위한 FakeView """

    from werkzeug.datastructures import MultiDict
    fake_request = Request({})
    fake_request.method = 'POST'
    fake_request.form = MultiDict([
        ("client_id", 'bccXf0CjTWcO8pGWxsU8GLx8'),
        ("response_type", 'code'),
        ("grant_type", 'authorization_code'),
        ("redirect_uri", 'http://localhost:5002'),
        ("scope", ''),
        ("state", ''),
    ])
    fake_request.base_url = "http://localhost:"
    fake_request.url = "http://localhost:5001/"

    grant_member = member_service.find_member(sequence=1)

    response: FlaskResponse = proxy.oauth.create_authorization_response(
        request=fake_request, grant_user=grant_member
    )

    def get_data(response):
        parsed_url = urlparse(response.location)
        query = parse_qs(parsed_url.query)

        return {
            "redirect_url": parsed_url.netloc,
            "authorization_code": query.get('code', None)[0]
        }

    _data = get_data(response)

    return jsonify(data={
        'redirect_url': _data['redirect_url'],
        'authorization_code': _data['authorization_code']
    })


    # precondition
    # grant_member = member_service.find_member(sequence=member_sequence)
    # grant: AuthorizationCodeGrant = proxy.oauth.get_consent_grant(
    #     request=fake_request,
    #     end_user=grant_member
    # )
    #
    # return jsonify(
    #     data={
    #         "code": grant.generate_authorization_code(),
    #         "redirect_uri": grant.redirect_uri
    #     })
