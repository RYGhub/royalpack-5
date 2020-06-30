import asyncio
from typing import *
import royalnet
import royalnet.commands as rc


class PingCommand(rc.Command):
    name: str = "ping"

    description: str = "Display the status of the Herald network."

    syntax: str = ""

    async def run(self, args: rc.CommandArgs, data: rc.CommandData) -> None:
        await data.reply("📶 Ping...")

        telegram_c = self.interface.call_herald_event("telegram", "pong")
        discord_c = self.interface.call_herald_event("discord", "pong")
        constellation_c = self.interface.call_herald_event("constellation", "pong")

        telegram_t = self.loop.create_task(telegram_c)
        discord_t = self.loop.create_task(discord_c)
        constellation_t = self.loop.create_task(constellation_c)

        await asyncio.sleep(10)

        try:
            telegram_r = telegram_t.result()
        except (asyncio.CancelledError, asyncio.InvalidStateError):
            telegram_r = None
        try:
            discord_r = discord_t.result()
        except (asyncio.CancelledError, asyncio.InvalidStateError):
            discord_r = None
        try:
            constellation_r = constellation_t.result()
        except (asyncio.CancelledError, asyncio.InvalidStateError):
            constellation_r = None

        lines = ["📶 [b]Pong![/b]", ""]

        if telegram_r:
            lines.append("🔵 Telegram")
        else:
            lines.append("🔴 Telegram")
        if discord_r:
            lines.append("🔵 Discord")
        else:
            lines.append("🔴 Discord")
        if constellation_r:
            lines.append("🔵 Constellation")
        else:
            lines.append("🔴 Constellation")

        await data.reply("\n".join(lines))
