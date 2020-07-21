from typing import *
import itsdangerous

from royalnet.backpack import tables as rbt
import royalnet.commands as rc

from .abstract.linker import LinkerCommand
from ..types import Updatable
from ..stars.api_auth_login_osu import ApiAuthLoginOsuStar


class OsuCommand(LinkerCommand):
    name = "osu"

    description = "Connetti e sincronizza il tuo account di osu!"

    @property
    def client_id(self):
        return self.config[self.name]['client_id']

    @property
    def client_secret(self):
        return self.config[self.name]['client_secret']

    @property
    def base_url(self):
        return self.config['base_url']

    @property
    def secret_key(self):
        return self.config['secret_key']

    async def get_updatables_of_user(self, session, user: rbt.User) -> List[Updatable]:
        return []

    async def get_updatables(self, session) -> List[Updatable]:
        return []

    async def create(self,
                     session,
                     user: rbt.User,
                     args: rc.CommandArgs,
                     data: Optional[rc.CommandData] = None) -> Optional[Updatable]:
        serializer = itsdangerous.URLSafeSerializer(self.secret_key, salt="osu")
        await data.reply("🔑 [b]Login necessario[/b]\n"
                         f"[url=https://osu.ppy.sh/oauth/authorize"
                         f"?client_id={self.client_id}"
                         f"&redirect_uri={self.base_url}{ApiAuthLoginOsuStar.path}"
                         f"&response_type=code"
                         f"&state={serializer.dumps(user.uid)}]"
                         f"Connetti osu! a Royalnet"
                         f"[/url]")
        return None

    async def update(self, session, obj, change: Callable[[str, Any], Awaitable[None]]):
        pass

    async def on_increase(self, session, obj: Updatable, attribute: str, old: Any, new: Any) -> None:
        pass

    async def on_unchanged(self, session, obj: Updatable, attribute: str, old: Any, new: Any) -> None:
        pass

    async def on_decrease(self, session, obj: Updatable, attribute: str, old: Any, new: Any) -> None:
        pass

    async def on_first(self, session, obj: Updatable, attribute: str, old: None, new: Any) -> None:
        pass

    async def on_reset(self, session, obj: Updatable, attribute: str, old: Any, new: None) -> None:
        pass
