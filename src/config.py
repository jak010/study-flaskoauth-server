import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = "mysql://root:1234@localhost:5501/oos"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True

DEBUG = True

SECRET_KEY = "dev"
