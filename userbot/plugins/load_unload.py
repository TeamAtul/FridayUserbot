import asyncio
import os
from datetime import datetime
from pathlib import Path

from userbot.utils import admin_cmd, load_module, remove_plugin, sudo_cmd


@borg.on(admin_cmd(pattern="load ?(.*)", outgoing=True))
async def load(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match.group(1)
    try:
        try:
            remove_plugin(shortname)
        except:
            pass
        load_module(shortname)
        await event.edit(f"Uğurla yükləndi: {shortname}")
    except Exception as e:
        await event.edit(f"Aşağıdakı səhvə görə {shortname} yüklənmədi.\n{str(e)}")


@borg.on(admin_cmd(pattern="unload ?(.*)", outgoing=True))
async def unload(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match.group(1)
    try:
        remove_plugin(shortname)
        await event.edit(f"**Uğurla silindi!** {shortname}")
    except Exception as e:
        await event.edit(
            "**Uğurla silindi!** {shortname}\n{}".format(shortname, str(e))
        )
