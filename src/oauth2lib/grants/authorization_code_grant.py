from __future__ import annotations

from authlib.oauth2.rfc6749 import grants

# from ..models import AuthorizationCode, db,

from src.models import db

from src.models import MemberModel, ClientModel, ClientTokenModel, ClientCodeModel


class AuthorizationCodeGrant(grants.AuthorizationCodeGrant):
    TOKEN_ENDPOINT_AUTH_METHODS = ['client_secret_post', "post"]

    def authenticate_user(self, authorization_code):
        return db.session.query(MemberModel).one()

    def save_authorization_code(self, code, request):
        ...
        # auth_code = ClientCodeModel(
        #     code=code,
        #     client_id=request.client.client_id,
        #     redirect_uri=request.redirect_uri,
        #     scope=request.scope,
        #     user_id=1
        # )
        #
        # db.session.add(auth_code)
        # db.session.commit()
        # return auth_code

    def query_authorization_code(self, code, client):
        ...
        # auth_code = AuthorizationCode.query.filter_by(
        #     code=code, client_id=client.client_id).first()
        #
        # return auth_code

    def delete_authorization_code(self, authorization_code):
        ...
