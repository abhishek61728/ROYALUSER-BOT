from userbot import *
from userbot.utils import *
from userbot.cmdhelp import CmdHelp
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User

#credits hell boy
#edited by @No_Needz_Approval

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Royal User"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

royal = bot.uid

PM_IMG = "https://telegra.ph/file/c3db400c8952d1919e74a.mp4"
pm_caption = "__**🔥🔥RȏʏѧʟUṡєя-Bȏṭ🔥🔥**__\n\n"

pm_caption += (
    f"               __↼Mａｓｔｅｒ⇀__\n**『[{DEFAULTUSER}](tg://user?id={royal})』**\n\n"
)

pm_caption += "🛡️Tєʟєṭһȏṅє🛡️ : `1.15.0` \n"

pm_caption += f"😈Rȏʏѧʟ-Bȏṭ😈  : __**{royalversion}**__\n"

pm_caption += f"⚜️ꜱᴜᴅᴏ⚜️             : `{sudou}`\n"

pm_caption += "⚠️ᴄʜᴀɴɴᴇʟ⚠️    : [ᴊᴏɪɴ](https://t.me/RoyalBot_Official)\n"

pm_caption += "🔥ᴄʀᴇᴀᴛᴏʀ🔥     : [ɴᴜʙ ʜᴇʀᴇ](https://t.me/No_Needz_Approval)\n"

pm_caption += "😆ᴏᴡɴᴇʀ😆        : [ɴᴜʙ ʜᴇʀᴇ](https://t.me/Apoorvroy86)\n"

pm_caption += "🤩ꜱᴜᴩᴩᴏʀᴛᴇʀ🤩: [ʜᴇʟʟʙᴏy](https://t.me/Kraken_The_BadASS)\n"

pm_caption += "    [✨ʀᴇᴩᴏ✨](https://github.com/abhishek61728/ROYALUSER-BOT) 🔹 [📜ʟɪᴄᴇɴꜱᴇ📜](https://github.com/abhishek61728/ROYALUSER-BOT/blob/main/LICENSE)"


@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()

CmdHelp("alive").add_command(
  'alive', None, 'Check weather the bot is alive or not'
).add_command(
  'royal', None, 'Check weather the bot is alive or not. In your custom Alive Pic and Alive Msg'
).add()
