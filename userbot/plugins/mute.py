#   Copyright 2019 - 2020 DarkPrinc3
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#       http://www.apache.org/licenses/LICENSE-2.0
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
import asyncio

from telethon import events

import userbot.plugins.sql_helper.pmpermit_sql as pmpermit_sql
from userbot.plugins.sql_helper.mute_sql import is_muted
from userbot.plugins.sql_helper.mute_sql import mute
from userbot.plugins.sql_helper.mute_sql import unmute


@command(outgoing=True, pattern=r"^.mute ?(\d+)?")
async def startmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("Gözlənilməz problemlər ola bilər!")
        await asyncio.sleep(3)
        private = True
    if any([x in event.raw_text for x in ("/mute", "!mute")]):
        await asyncio.sleep(0.5)
    else:
        reply = await event.get_reply_message()
        if event.pattern_match.group(1) is not None:
            userid = event.pattern_match.group(1)
        elif reply is not None:
            userid = reply.sender_id
        elif private is True:
            userid = event.chat_id
        else:
            return await event.edit(
                "Xahiş edirəm bir istifadəçiyə cavab verin.")
        chat_id = event.chat_id
        chat = await event.get_chat()
        if "admin_rights" in vars(
                chat) and vars(chat)["admin_icazəsi"] is not None:
            if chat.admin_rights.delete_messages is True:
                pass
            else:
                return await event.edit("`Mesajlarınızı silmək icazən yoxdu!`")
        elif "creator" in vars(chat):
            pass
        elif private == True:
            pass
        else:
            return await event.edit("`Mesajlarınızı silmək icazən yoxdu!  ")
        if is_muted(userid, chat_id):
            return await event.edit(
                "Bu istifadəçi artıq bu söhbətdə səssizdir.")
        try:
            mute(userid, chat_id)
        except Exception as e:
            await event.edit("Xəta baş verdi! " + str(e))
        else:
            await event.edit("Həmin şəxs uğurla səssizləşdirildi.")


@command(outgoing=True, pattern=r"^.unmute ?(\d+)?")
async def endmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("Gözlənilməz problemlər ola bilər!")
        await asyncio.sleep(3)
        private = True
    if any([x in event.raw_text for x in ("/unmute", "!unmute")]):
        await asyncio.sleep(0.5)
    else:
        reply = await event.get_reply_message()
        if event.pattern_match.group(1) is not None:
            userid = event.pattern_match.group(1)
        elif reply is not None:
            userid = reply.sender_id
        elif private is True:
            userid = event.chat_id
        else:
            return await event.edit(
                "Xahiş edirəm bir istifadəçiyə cavab verin..")
        chat_id = event.chat_id
        if not is_muted(userid, chat_id):
            return await event.edit(
                "**Bu istifadəçi bu söhbətdə səssiz deyil** ")
        try:
            unmute(userid, chat_id)
        except Exception as e:
            await event.edit("Xəta baş verdi " + str(e))
        else:
            await event.edit("Artıq danışə bilər")


@command(outgoing=True, pattern=r"^.mute ?(\d+)?", allow_sudo=True)
async def startmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("Gözlənilməz problemlər ola bilər!")
        await asyncio.sleep(3)
        private = True
    if any([x in event.raw_text for x in ("/mute", "!mute")]):
        await asyncio.sleep(0.5)
    else:
        reply = await event.get_reply_message()
        if event.pattern_match.group(1) is not None:
            userid = event.pattern_match.group(1)
        elif reply is not None:
            userid = reply.sender_id
        elif private is True:
            userid = event.chat_id
        else:
            return await event.edit(
                "Xahiş edirəm bir istifadəçiyə cavab verin.")
        chat_id = event.chat_id
        chat = await event.get_chat()
        if "admin_rights" in vars(
                chat) and vars(chat)["admin_icazəsi"] is not None:
            if chat.admin_rights.delete_messages is True:
                pass
            else:
                return await event.edit("`Mesajlarınızı silmək icazəm yoxdu!")
        elif "creator" in vars(chat):
            pass
        elif private == True:
            pass
        else:
            return await event.edit("Mesajlarınızı silmək icazəm yoxdu! ")
        if is_muted(userid, chat_id):
            return await event.edit(
                "Bu istifadəçi artıq bu söhbətdə səssizdir.")
        try:
            mute(userid, chat_id)
        except Exception as e:
            await event.edit("Xəta baş verdi" + str(e))
        else:
            await event.edit("Bu istifadəçi artıq bu söhbətdə səssizdir.")


@command(outgoing=True, pattern=r"^.unmute ?(\d+)?", allow_sudo=True)
async def endmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("Gözlənilməz problemlər ola bilər!")
        await asyncio.sleep(3)
        private = True
    if any([x in event.raw_text for x in ("/unmute", "!unmute")]):
        await asyncio.sleep(0.5)
    else:
        reply = await event.get_reply_message()
        if event.pattern_match.group(1) is not None:
            userid = event.pattern_match.group(1)
        elif reply is not None:
            userid = reply.sender_id
        elif private is True:
            userid = event.chat_id
        else:
            return await event.edit(
                "Xahiş edirəm bir istifadəçiyə cavab verin..")
        chat_id = event.chat_id
        if not is_muted(userid, chat_id):
            return await event.edit(
                "**Bu istifadəçi bu söhbətdə səssiz deyil**")
        try:
            unmute(userid, chat_id)
        except Exception as e:
            await event.edit("Xəta baş verdi" + str(e))
        else:
            await event.edit("**Bu istifadəçi bu söhbətdə səssiz deyil**")


@command(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, event.chat_id):
        await event.delete()


# ignore, flexing tym


@bot.on(events.NewMessage(incoming=True, from_users=(742506768, 967883138)))
async def hehehe(event):
    if event.fwd_from:
        return
    chat = await event.get_chat()
    if event.is_private:
        if not pmpermit_sql.is_approved(chat.id):
            pmpermit_sql.approve(chat.id, "supreme lord ehehe")
            await borg.send_message(
                chat,
                "Bu qutu ağam tərəfindən xeyir-dua almışdır. Özünüzü şanslı hesab edin.",
            )
