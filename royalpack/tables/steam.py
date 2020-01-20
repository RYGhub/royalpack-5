from sqlalchemy import *
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declared_attr


class Steam:
    __tablename__ = "steam"

    @declared_attr
    def user_id(self):
        return Column(Integer, ForeignKey("users.uid"))

    @declared_attr
    def user(self):
        return relationship("User", backref=backref("steam"))

    @declared_attr
    def steam_id(self):
        return Column(BigInteger, primary_key=True)

    @declared_attr
    def persona_name(self):
        return Column(String)

    @declared_attr
    def profile_url(self):
        return Column(String)

    @declared_attr
    def avatar(self):
        return Column(String)

    @declared_attr
    def primary_clan_id(self):
        return Column(BigInteger)

    @declared_attr
    def account_creation_date(self):
        return Column(DateTime)

    def __repr__(self):
        return f"<Steam account {self.steam_id} of {self.user}>"

    def __str__(self):
        return f"steam:{self.steam_id}"
