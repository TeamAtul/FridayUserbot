from telethon.utils import pack_bot_file_id
from friday-userbot.utils import friday_on_cmd, edit_or_reply, sudo_cmd
from friday-userbot import bot
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
from friday-userbot.plugins import inlinestats
from telethon import custom, events, Button
from friday-userbot import CMD_LIST
from friday-userbot.utils import friday_on_cmd, edit_or_reply, sudo_cmd
from telethon.utils import get_display_name
from friday-userbot.utils import friday_on_cmd, sudo_cmd
from friday-userbot.Configs import Config
from telethon import events
from datetime import datetime
from friday-userbot.utils import friday_on_cmd, edit_or_reply, sudo_cmd
import time
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from friday-userbot import Lastupdate, bot
from friday-userbot.plugins.sql_helper.botusers_sql import add_me_in_db, his_userid
from friday-userbot.plugins.sql_helper.idadder_sql import add_usersid_in_db, get_all_users

@tgbot.on(events.NewMessage(pattern="^/id"))
async def _(event):
    if event.reply_to_msg_id:
        await event.get_input_chat()
        r_msg = await event.get_reply_message()
        if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await tgbot.send_message(
                event.chat_id,
                "Current Chat ID: `{}`\nFrom User ID: `{}`\nBot API File ID: `{}`".format(
                    str(event.chat_id), str(r_msg.from_id), bot_api_file_id
                )
            )
        else:
            await tgbot.send_message(
                event.chat_id,
                "Current Chat ID: `{}`\nFrom User ID: `{}`".format(
                    str(event.chat_id), str(r_msg.from_id)
                )
            )
    else:
        await tgbot.send_message(event.chat_id, "Current Chat ID: `{}`".format(str(event.chat_id)))
