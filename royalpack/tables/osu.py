from typing import *
import aiohttp
import datetime
from sqlalchemy import *
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declared_attr

from ..types import Updatable, oauth_refresh


# noinspection PyAttributeOutsideInit
class Osu(Updatable):
    __tablename__ = "osu"

    @declared_attr
    def user_id(self):
        return Column(Integer, ForeignKey("users.uid"))

    @declared_attr
    def user(self):
        return relationship("User", backref=backref("osu"))

    @declared_attr
    def access_token(self):
        return Column(String, nullable=False)

    @declared_attr
    def refresh_token(self):
        return Column(String, nullable=False)

    @declared_attr
    def expiration_date(self):
        return Column(DateTime, nullable=False)

    @declared_attr
    def osu_id(self):
        return Column(Integer, primary_key=True)

    @declared_attr
    def username(self):
        return Column(String)

    async def refresh(self, *, client_id, client_secret, base_url, path):
        j = await oauth_refresh(url="https://osu.ppy.sh/oauth/token",
                                client_id=client_id,
                                client_secret=client_secret,
                                redirect_uri=f"{base_url}{path}",
                                refresh_code=self.refresh_token)
        self.access_token = j["access_token"]
        self.refresh_token = j["refresh_token"]
        self.expiration_date = datetime.datetime.now() + datetime.timedelta(seconds=j["expires_in"])

    async def refresh_if_expired(self, *, client_id, client_secret, base_url, path):
        if datetime.datetime.now() >= self.expiration_date:
            await self.refresh(client_id=client_id, client_secret=client_secret, base_url=base_url, path=path)
