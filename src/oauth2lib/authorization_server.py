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


def query_client_func():
    return create_query_client_func(db.session, ClientModel)


def save_token_func():
    return create_save_token_func(db.session, ClientTokenModel)


class AuthorizationProxy:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = args[0]
        return cls._instance

    @classmethod
    def config(cls, flask_app):
        print("?")
        oauth = AuthorizationServer(
            query_client=query_client_func(),
            save_token=save_token_func()
        )
        oauth.init_app(flask_app)

        return cls(oauth)

    # def adapt_authorization_code_grant(self):
    #     self.oauth.register_grant(authorization_code_grant.AuthorizationCodeGrant)
    #
    # def __call__(self, *args, **kwargs):
    #     return self._instance

# def config_auth(app):
#     oauth_server.init_app(app)
#
#     Grant Adapt
# oauth_server.register_grant(authorization_code_grant.AuthorizationCodeGrant)
