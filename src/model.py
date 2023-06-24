# from __future__ import annotations


# from authlib.integrations.sqla_oauth2 import (
#     OAuth2ClientMixin,
#     OAuth2TokenMixin,
#     OAuth2AuthorizationCodeMixin
# )
#
# from sqlalchemy import Column, Integer, ForeignKey
# from sqlalchemy.orm import relationship
#
# from flask_sqlalchemy import SQLAlchemy
#
# db = SQLAlchemy()
#
#
# # https://docs.authlib.org/en/latest/flask/2/authorization-server.html
# # - `23.06.22: 위 문서에 따라 구현하는 중
#
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#
#     def get_user_id(self):
#         return self.id
#
#
# class Client(db.Model, OAuth2ClientMixin):
#     id = Column(Integer, primary_key=True)
#     user_id = Column(
#         Integer, ForeignKey('user.id', ondelete='CASCADE')
#     )
#     user = relationship('User')
#
#
# class Token(db.Model, OAuth2TokenMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(
#         db.Integer, db.ForeignKey('user.id', ondelete='CASCADE')
#     )
#     user = db.relationship('User')
#
#
# class AuthorizationCode(db.Model, OAuth2AuthorizationCodeMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(
#         db.Integer, db.ForeignKey('user.id', ondelete='CASCADE')
#     )
#     user = db.relationship('User')
