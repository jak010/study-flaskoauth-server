from __future__ import annotations

# Setup
from authlib.integrations.flask_oauth2.authorization_server import AuthorizationServer
from authlib.integrations.sqla_oauth2 import (
    create_query_client_func,
    create_save_token_func,
    create_revocation_endpoint,
    create_bearer_token_validator,
)

# grant
from authlib.oauth2.rfc6749 import grants

from .model import (Client, Token, db)

# custom oaut2lib
from .oauth2lib.grant import AuthorizationCodeGrant

oauth_server = AuthorizationServer(
    query_client=create_query_client_func(db.session, Client),
    save_token=create_save_token_func(db.session, Token)
)


def config_auth(app):
    oauth_server.init_app(app)
    # support all grants

    # 1. AuthorizationCodeGrant 방식
    oauth_server.register_grant(AuthorizationCodeGrant)

    # 2. ImplicitGrant 방식
    oauth_server.register_grant(grants.ImplicitGrant)
