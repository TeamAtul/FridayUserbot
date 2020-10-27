"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
# CREDITS: @GangsterAz, @sekretcelovek
import time
from datetime import datetime

from uniborg.util import admin_cmd
from uniborg.util import sudo_cmd

from userbot import ALIVE_NAME
from userbot import Lastupdate
from userbot.plugins import currentversion

# Functions


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - Lastupdate))
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/3ac99d5d56bbd4074bb17.gif"
pm_caption = "➥ **DARK USER BOT:** `ƏLA İŞLƏYİR`\n\n"
pm_caption += "➥ **SİSTEM HAQQINDA**\n"
pm_caption += "➥ **Telethon Versiya:** `1.15.0` \n"
pm_caption += "➥ **Python:** `3.7.4` \n"
pm_caption += f"➥ **İşləmə zamanı** : `{uptime}` \n"
pm_caption += "➥ **Hazırkı vəziyyət** : `master`\n"
pm_caption += f"➥ **Versiya** : `{currentversion}`\n"
pm_caption += f"➥ **Boss** : {DEFAULTUSER} \n"
pm_caption += "➥ **Lisenziya** : [GNU General Public License v3.0](github.com/DarkWebAze/DarkUserbot/blob/master/LICENSE)\n"
pm_caption += "🇦🇿DARK USER BOT🇦🇿"


@borg.on(admin_cmd(pattern=r"alive"))
@borg.on(sudo_cmd(pattern=r"alive", allow_sudo=True))
async def friday(alive):
    await alive.get_chat()
    """ Botun işlədiyini .alive kodu ilə yoxlayın.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()
