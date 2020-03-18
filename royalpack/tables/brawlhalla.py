from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declared_attr
import steam


class Brawlhalla:
    __tablename__ = "brawlhalla"

    @declared_attr
    def brawlhalla_id(self):
        return Column(Integer, primary_key=True)

    @declared_attr
    def _steamid(self):
        return Column(BigInteger, ForeignKey("steam._steamid"), primary_key=True)

    @declared_attr
    def steam(self):
        return relationship("Steam", backref=backref("brawlhalla", uselist=False))

    @property
    def steamid(self):
        return steam.SteamID(self._steamid)

    @declared_attr
    def name(self):
        return Column(String)

    @declared_attr
    def rating_1v1(self):
        return Column(Integer)

    @property
    def tier_1v1(self):
        return Column(String)
