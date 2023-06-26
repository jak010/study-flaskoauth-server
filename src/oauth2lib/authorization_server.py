from __future__ import annotations
from functools import cached_property
# Setup
from authlib.integrations.flask_oauth2.authorization_server import AuthorizationServer
from authlib.integrations.sqla_oauth2 import (
    create_query_client_func,
    create_save_token_func,
    create_revocation_endpoint,
    create_bearer_token_validator,
)

# from .model import (Client, Token, db)

from src.models import db, ClientModel, ClientTokenModel

# custom oaut2lib
from .grants import authorization_code_grant

oauth_server = AuthorizationServer(
    query_client=create_query_client_func(db.session, ClientModel),
    save_token=create_save_token_func(db.session, ClientTokenModel)
)


class AuthorizationProxy:

    def __init__(self):
        self._oauth = AuthorizationServer(
            query_client=create_query_client_func(db.session, ClientModel),
            save_token=create_save_token_func(db.session, ClientTokenModel)
        )

    @property
    def oauth(self):
        return self._oauth

    def config(self, flask_app):
        self._oauth.init_app(flask_app)

    def add_authorization_grant(self):
        self._oauth.register_grant(authorization_code_grant.AuthorizationCodeGrant)

# def config_auth(app):
#     oauth_server.init_app(app)
#
#     Grant Adapt
# oauth_server.register_grant(authorization_code_grant.AuthorizationCodeGrant)
