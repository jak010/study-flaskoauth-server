from src.oauth2lib.client_factory import ClientFactory

from src.domain.member import member_service


def add_authorization_client(requst_form):
    member = member_service.find_member(1)
    print(member.member_id)
    new_client = ClientFactory.with_type(
        member=member,
        client_name=requst_form.client_name,
        client_uri=requst_form.client_uri,
        redirect_uri=requst_form.redirect_uri,
        client_grant_type='authorization_code'
    )

    print(new_client)


