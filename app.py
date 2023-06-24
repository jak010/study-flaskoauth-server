from flask import Flask
from flask_migrate import Migrate

from .src.model import db
from .src.oauth2 import config_auth

migrate = Migrate()


def create_app():
    from .src import config

    app = Flask(__name__)
    app.config.from_object(config)

    # db Setup
    db.init_app(app)
    migrate.init_app(app, db)

    # Auth Setup
    config_auth(app)

    # EndPoint Setup
    from .src.api import bp
    app.register_blueprint(bp)

    return app
