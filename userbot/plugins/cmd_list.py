import asyncio

from userbot.utils import admin_cmd


# @command(pattern="^.plist", outgoing=True)
@borg.on(admin_cmd(pattern=r"plist"))
async def install(event):
    if event.fwd_from:
        return
    cmd = "ls userbot/plugins"
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await process.communicate()
    o = stdout.decode()
    _o = o.split("\n")
    o = "\n".join(_o)
    OUTPUT = f"**Plugin Siyahısı:**\n - {o}\n\n**HELP:** __Əgər Pluginin Kodlarını Bilmək İstəyirsinizsə, bunu edin:-__ \n `.help <plugin adı>` **mötərizlər < > olmadan.**\n__Pluginlər İşləməyə Bilər. Kömək Üçün__ @DarkUserBot_Support __ziyarət edin.__"
    await event.edit(OUTPUT)
