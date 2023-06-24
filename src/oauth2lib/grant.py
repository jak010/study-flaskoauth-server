from authlib.oauth2.rfc6749 import grants

from ..model import AuthorizationCode, db, User


class AuthorizationCodeGrant(grants.AuthorizationCodeGrant):
    TOKEN_ENDPOINT_AUTH_METHODS = ['client_secret_post']

    def authenticate_user(self, authorization_code):
        return db.session.query(User).one()

    def save_authorization_code(self, code, request):
        auth_code = AuthorizationCode(
            code=code,
            client_id=request.client.client_id,
            redirect_uri=request.redirect_uri,
            scope=request.scope,
            user_id=1
        )

        db.session.add(auth_code)
        db.session.commit()
        return auth_code

    def query_authorization_code(self, code, client):
        auth_code = AuthorizationCode.query.filter_by(
            code=code, client_id=client.client_id).first()

        return auth_code

    def delete_authorization_code(self, authorization_code):
        ...
