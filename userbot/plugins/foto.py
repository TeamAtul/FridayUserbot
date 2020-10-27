"""Kod: `.foto`  **Qarşı Şəxsin Bütün Profil Şəklini Atır**
\n Kod: `.foto (nömrə)`  **İstənilən Nömrəli Şəkli Atır** .
"""
import logging

from userbot.utils import admin_cmd

logger = logging.getLogger(__name__)


if 1 == 1:

    name = "Profil Şəkilləri"

    client = borg

    @borg.on(admin_cmd(pattern="foto(.*)"))
    async def potocmd(event):

        """Göstərdiyiniz şəxsin profil şəklini alma, kanal vəya qrupda"""

        id = "".join(event.raw_text.split(maxsplit=2)[1:])

        user = await event.get_reply_message()

        chat = event.input_chat

        if user:

            photos = await event.client.get_profile_photos(user.sender)

        else:

            photos = await event.client.get_profile_photos(chat)

        if id.strip() == "":

            try:

                await event.client.send_file(event.chat_id, photos)

            except a:

                photo = await event.client.download_profile_photo(chat)

                await borg.send_file(event.chat_id, photo)

        else:

            try:

                id = int(id)

                if id <= 0:

                    await event.edit("`ID nömrəsi səhvdir!`")

                    return

            except:

                await event.edit("`Mənimlə məzələnirsən ?`")

                return

            if int(id) <= (len(photos)):

                send_photos = await event.client.download_media(photos[id - 1])

                await borg.send_file(event.chat_id, send_photos)

            else:

                await event.edit("`Şəkil yoxdu dostum!`")

                return
