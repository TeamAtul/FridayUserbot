from telethon.utils import pack_bot_file_id
from fridayfridayfridayuserbot.utils import friday_on_cmd, edit_or_reply, sudo_cmd
from fridayfridayfridayuserbot import bot
from telethon import events, custom, Button
from telethon.tl.types import (
    Channel,
    Chat,
    User
)

import emoji
import asyncio
from googletrans import Translator
import re
import io
from math import ceil
from fridayfridayfridayuserbot.plugins import inlinestats
from telethon import custom, events, Button
from fridayfridayfridayuserbot import CMD_LIST
from fridayfridayfridayuserbot.utils import friday_on_cmd, edit_or_reply, sudo_cmd
from telethon.utils import get_display_name
from fridayfridayfridayuserbot.utils import friday_on_cmd, sudo_cmd
from fridayfridayfridayuserbot.Configs import Config
from telethon import events
from datetime import datetime
from fridayfridayfridayuserbot.utils import friday_on_cmd, edit_or_reply, sudo_cmd
import time
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from fridayfridayfridayuserbot import Lastupdate, bot
from fridayfridayfridayuserbot.plugins.sql_helper.botusers_sql import add_me_in_db, his_userid
from fridayfridayfridayuserbot.plugins.sql_helper.idadder_sql import add_usersid_in_db, get_all_users
import time
from uniborg.util import friday_on_cmd, sudo_cmd
from fridayfridayfridayuserbot import ALIVE_NAME
from datetime import datetime
from fridayfridayfridayuserbot import Lastupdate
from fridayfridayfridayuserbot.plugins import currentversion

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/22535f8051a58af113586.jpg"
pm_caption = "➥ **ASSISTANT IS:** `ONLINE`\n\n"
pm_caption += "➥ **SYSTEMS STATS**\n"
pm_caption += "➥ **Telethon Version:** `1.15.0` \n"
pm_caption += "➥ **Python:** `3.7.4` \n"
pm_caption += "➥ **Database Status:**  `Functional`\n"
pm_caption += "➥ **Current Branch** : `master`\n"
pm_caption += f"➥ **Version** : `{currentversion}`\n"
pm_caption += f"➥ **My Boss** : {DEFAULTUSER} \n"
pm_caption += "➥ **Heroku Database** : `AWS - Working Properly`\n\n"
pm_caption += "➥ **License** : [GNU General Public License v3.0](github.com/StarkGang/FridayUserbot/blob/master/LICENSE)\n"
pm_caption += "➥ **Copyright** : By [StarkGang@Github](GitHub.com/StarkGang)\n"
pm_caption += "[Assistant By Friday 🇮🇳](https://telegra.ph/FRIDAY-06-15)"

# only Owner Can Use it 
@tgbot.on(events.NewMessage(pattern="^/alive", func=lambda e: e.sender_id == bot.uid))
async def friday(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
