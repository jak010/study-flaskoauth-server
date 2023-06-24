from dataclasses import dataclass

from flask import Blueprint, request
from flask import jsonify
from sqlalchemy.exc import NoResultFound

from src.models import Session
from src.models.member_model import MemberModel

member_api = Blueprint("member", __name__, url_prefix="/api/member")


@member_api.route("/", methods=("GET",))
def find_member():
    """ member 조회하기 """
    items = []
    with Session() as s:
        for row in s.query(MemberModel).all():
            items.append({
                'sequence': row.sequence,
                'member_id': row.member_id
            })

    return jsonify(data={'items': items})


@member_api.route("/", methods=("POST",))
def register_member():
    """ member 등록하기 """

    @dataclass
    class RequestForm:
        member_id: str
        password: str

    request_form = RequestForm(
        member_id=request.form['member_id'],
        password=request.form['password']
    )

    def exist(member: MemberModel):
        try:
            return s.query(MemberModel).filter(MemberModel.member_id == member.member_id).one()
        except NoResultFound:
            return False

    with Session() as s:
        new_member = MemberModel(member_id=request_form.member_id, password=request_form.password)
        if exist(new_member):
            return jsonify(data={"message": "Already Exist.."})

        s.add(new_member)

    return jsonify(data={"message": "Success"})
