"""Emoji
Mövcud Kodlar:
.support
"""
import asyncio

from userbot.utils import admin_cmd


@borg.on(admin_cmd("dark"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 36)
    # input_str = event.pattern_match.group(1)
    # if input_str == "support":
    await event.edit("support qrup üçün")
    animation_chars = [
        "Bura Basın",
        "[Support Group](https://t.me/DARKUSERBOT_SUPPORT)",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
