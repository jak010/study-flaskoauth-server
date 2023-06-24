from flask import Flask
from flask_migrate import Migrate

# from .src.model import db
# from .src.oauth2 import config_auth
from .src.models import db
from .src import config

migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # db Setup
    db.init_app(app)
    migrate.init_app(app, db)

    # Auth Setup
    # config_auth(app)

    # EndPoint Setup
    from .src.apiv1.member import member_api
    app.register_blueprint(member_api)

    return app
