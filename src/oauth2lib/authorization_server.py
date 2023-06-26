from __future__ import annotations
from functools import cached_property
# Setup
from authlib.integrations.flask_oauth2.authorization_server import AuthorizationServer, create_token_generator
from authlib.integrations.sqla_oauth2 import (
    create_query_client_func,
    create_save_token_func,
    create_revocation_endpoint,
    create_bearer_token_validator,
)

from authlib.oauth2.rfc6750 import BearerTokenGenerator, BearerToken, BearerTokenValidator
# from .model import (Client, Token, db)

from src.models import db, ClientModel, ClientTokenModel

# custom oaut2lib
from .grants import authorization_code_grant


# oauth_server = AuthorizationServer(
#     query_client=create_query_client_func(db.session, ClientModel),
#     save_token=create_save_token_func(db.session, ClientTokenModel)
# )


class AuthorizationProxy:
    _config = {
        "OAUTH2_TOKEN_EXPIRES_IN": {
            'authorization_code': 864000,
            'urn:ietf:params:oauth:grant-type:jwt-bearer': 3600,
        }
    }

    def __init__(self):
        self._oauth = AuthorizationServer(
            query_client=create_query_client_func(db.session, ClientModel),
            save_token=self.create_save_token(db.session, ClientTokenModel)
        )
        self._oauth.register_token_generator(
            'default',
            BearerToken(access_token_generator=create_token_generator(token_generator_conf=True)).generate
        )

    @property
    def oauth(self):
        return self._oauth

    def config(self, flask_app):
        self._oauth.init_app(flask_app)

    def add_authorization_grant(self):
        self._oauth.register_grant(authorization_code_grant.AuthorizationCodeGrant)

    def create_save_token(self, session, token_model):
        def save_token(token, request):
            if request.user:
                member_id = request.user.get_member_id()
            else:
                member_id = None
            client = request.client
            item = token_model(
                client_id=client.client_id,
                member_id=member_id,
                **token
            )
            session.add(item)
            session.commit()

        return save_token

# def config_auth(app):
#     oauth_server.init_app(app)
#
#     Grant Adapt
# oauth_server.register_grant(authorization_code_grant.AuthorizationCodeGrant)
