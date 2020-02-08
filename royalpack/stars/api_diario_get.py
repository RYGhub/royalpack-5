from starlette.requests import Request
from starlette.responses import *
from royalnet.constellation.api import *
from royalnet.utils import *
from ..tables import *


class ApiDiarioGetStar(ApiStar):
    path = "/api/diario/get/v1"

    async def api(self, data: ApiData) -> dict:
        try:
            diario_id = int(data["diario_id"])
        except ValueError:
            raise InvalidParameterError("'diario_id' is not a valid int.")
        entry: Diario = await asyncify(data.session.query(self.alchemy.get(Diario)).get, diario_id)
        if entry is None:
            raise NotFoundError("No such diario entry.")
        return entry.json()
