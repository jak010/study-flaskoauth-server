from flask import Blueprint, request, session, url_for
from flask import render_template, redirect, jsonify
from authlib.oauth2.rfc6749.grants.authorization_code import AuthorizationCodeGrant
# from .oauth2 import oauth_server
#
# from .libs.client_factory import ClientFactory
# from .model import User
# from ..app import db

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from authlib.integrations.flask_oauth2.authorization_server import AuthorizationServer
    from authlib.oauth2.rfc6749.wrappers import OAuth2Request
    from flask.wrappers import Response

client_api = Blueprint("client", __name__, url_prefix="/client")


@client_api.route("", methods=("GET",))
def get_client():
    """ client 조회하기 """
    return jsonify(data={})


@client_api.route("", methods=("POST",))
def add_client():
    """ client 등록하기 """
    return jsonify(data={})
