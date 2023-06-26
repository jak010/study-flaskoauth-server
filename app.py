from flask import Flask
from flask_migrate import Migrate

from src.models import db
from src import config
from src.oauth2lib.authorization_server import AuthorizationProxy

from authlib.oauth2.rfc6750 import BearerTokenGenerator, BearerToken, BearerTokenValidator

migrate = Migrate()

proxy = AuthorizationProxy()
proxy.add_authorization_grant()


def create_app():
    flask_app = Flask(__name__)
    flask_app.config.from_object(config.DevConfig)

    # db Setup
    db.init_app(flask_app)
    migrate.init_app(flask_app, db)

    # EndPoint Setup
    from .src.apiv1.member import member_api
    from .src.apiv1.client import client_api
    from .src.apiv1.auth import auth_api
    from .src.apiv1.token import token_api

    flask_app.register_blueprint(member_api)
    flask_app.register_blueprint(client_api)
    flask_app.register_blueprint(auth_api)
    flask_app.register_blueprint(token_api)

    return flask_app
