class MemberEntity:
    def __init__(self,
                 sequence: int,
                 member_id: str,
                 password: str,
                 ):
        self.sequence = sequence
        self.member_id = member_id
        self.password = password

    def __repr__(self):
        return f"MemberEntity(" \
               f" sequence={self.sequence}," \
               f" member_id={self.member_id}," \
               f" password={self.password})"

    def to_dict(self):
        return dict(sequence=self.sequence, member_id=self.member_id, passwod=self.password)
