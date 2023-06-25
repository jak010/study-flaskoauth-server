from typing import List

from src.models import Session
from src.models.member_model import MemberModel
from typing import Optional
from sqlalchemy.exc import NoResultFound
from .member_entity import MemberEntity


def member_list():
    items = []

    with Session() as s:
        query = s.query(MemberModel).all()
        for row in query:
            items.append({
                'sequence': row.sequence,
                'member_id': row.member_id
            })

    return items


def is_exist(member: MemberModel):
    with Session() as s:
        try:
            return s.query(MemberModel).filter(MemberModel.member_id == member.member_id).one()
        except NoResultFound:
            return False


def find_member(sequence) -> MemberEntity:
    with Session() as s:
        try:
            member = s.query(MemberModel).filter(MemberModel.sequence == sequence).one()
            return MemberEntity(
                sequence=member.sequence,
                member_id=member.member_id,
                password=member.password
            )
        except NoResultFound:
            return None


def create_member(request_form) -> Optional[MemberModel]:
    new_member = MemberModel(member_id=request_form.member_id, password=request_form.password)

    if is_exist(new_member):
        raise Exception("Already Exist Member")

    with Session() as s:
        s.add(new_member)
        return new_member
