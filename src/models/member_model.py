from . import db

from sqlalchemy import Column, Integer, VARCHAR


class MemberModel(db.Model):
    __tablename__ = "member"

    sequence = Column(Integer, primary_key=True)
    member_id = Column(VARCHAR(255), nullable=True)
    password = Column(VARCHAR(255), nullable=True)
