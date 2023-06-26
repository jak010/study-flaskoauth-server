import os

BASE_DIR = os.path.dirname(__file__)


class Config(object):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:1234@localhost:5501/oos"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

    DEBUG = False


class DevConfig(Config):
    DEBUG = True
    SECRET_KEY = "dev"
    OAUTH2_SCOPES_SUPPORTED = True