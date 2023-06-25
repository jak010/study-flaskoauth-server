from dataclasses import dataclass

from flask import Blueprint, request
from flask import jsonify
from sqlalchemy.exc import NoResultFound

from src.domain.member import member_service

from src.models import Session
from src.models.member_model import MemberModel

member_api = Blueprint("member", __name__, url_prefix="/api/member")


@member_api.route("", methods=("GET",))
def find_member():
    """ member 조회하기 """
    return jsonify(
        data={
            'items': member_service.member_list()
        }
    )


@member_api.route("", methods=("POST",))
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

    member_service.create_member(request_form=request_form)

    return jsonify(data={"message": "Success"})
