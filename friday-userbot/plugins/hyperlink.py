# For UniBorg
# By Priyam Kalra
# Syntax (.hl <link>)

from friday-friday-userbot.utils import friday_on_cmd


@friday.on(friday_on_cmd(pattern="hl ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input = event.pattern_match.group(1)
    await event.edit("[ㅤㅤㅤㅤㅤㅤㅤ](" + input + ")")
