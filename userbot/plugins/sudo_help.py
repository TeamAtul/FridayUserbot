from fridayfridayfridayuserbot import SUDO_LIST
from fridayfridayfridayuserbot.utils import sudo_cmd, edit_or_reply

@friday.on(sudo_cmd(pattern="help ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    plugin_name = event.pattern_match.group(1)
    help_string = "**SUDO COMMANDS** \n"
    try:
        for i in SUDO_LIST[plugin_name]:
            help_string += f"$× `{i}`"
            help_string += "\n"
        await event.reply(f"{help_string}")
    except:
        await event.reply(f"`{plugin_name}` __May Not Have Sudo Or Is Not Valid__")
