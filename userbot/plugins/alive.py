import time
import random
import time
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot
from userbot.Config import Config
from telethon import version
from userbot import ALIVE_NAME, StartTime, LEGENDversion
from LEGENDBOT.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp
from . import *
async def reply_id(event):
    reply_to_id = None
    if event.sender_id in Config.SUDO_USERS:
        reply_to_id = event.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    return reply_to_id


DEFAULTUSER = ALIVE_NAME or "Xeno UsᴇʀBᴏᴛ 🇮🇳"
LEGEND_IMG = Config.ALIVE_PIC
CUSTOM_ALIVE_TEXT = Config.ALIVE_MSG or "Xeno UsᴇʀBᴏᴛ Is Alive"
CUSTOM_YOUR_GROUP =Config.YOUR_GROUP or "@XenoChats"

Legend = bot.uid

mention = f"[{DEFAULTUSER}](tg://user?id={Legend})"


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


uptime = get_readable_time((time.time() - StartTime))


@bot.on(admin_cmd(outgoing=True, pattern="legend$"))
@bot.on(sudo_cmd(pattern="legend$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)

    if  XENO_IMG:
        XENO_caption = f"**{CUSTOM_ALIVE_TEXT}**\n"
        
        XENO_caption += f"~~~~~~~~~~~~~~~~~~~~~~~\n"
        XENO_caption += f"        **Xᴇɴᴏ Sᴛᴀᴛs** \n"
        XENO_caption += f"•_• **Master**          : {mention}\n\n"
        XENO_caption += f"•_• **XenoBᴏᴛ**   : {XENOversion}\n"
        XENO_caption += f"•_• **Telethon**     : `{version.__version__}`\n"
        XENO_caption += f"•_• **Uptime**         : `{uptime}`\n"
        XENO_caption += f"•_• **Group**           : [𝙶𝚛𝚘𝚞𝚙](t.me/XenoChats)\n"
        XENO_caption += f"•_• **My Group**  : {CUSTOM_YOUR_GROUP}\n"   

        await alive.client.send_file(
            alive.chat_id, LEGEND_IMG, caption=LEGEND_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**{CUSTOM_ALIVE_TEXT}**\n\n"
            f"~~~~~~~~~~~~~~~~~~~~~~~ \n"
            f"         𝕭𝖔𝖙 𝕾𝖙𝖆𝖙𝖚𝖘\n"
            f"•⚡• 𝕿єℓєτнοи    : `{version.__version__}`\n"
            f"🇮🇳 Xeno UsᴇʀBᴏᴛ  : `{XENOversion}`\n"
            f"🇮🇳 υρτιмє        : `{uptime}`\n"
            f"🔱 ɱαรƭεɾ        : {mention}\n"
            f"🔱 σωɳεɾ         : [ℓєgєи∂](t.me/Its_LegendBoy)\n"
        )


msg = f"""
**  |• Xeno UsᴇʀBᴏᴛ Is Aʟɪᴠᴇ •|**

{Config.ALIVE_MSG}

**    Xeno UsᴇʀBᴏᴛ Stats**
**•_•Master    :** **{mention}**
**•_•Xeno Bᴏᴛ  :** {XENOversion}
**•_•Telethon  :** {version.__version__}
**•_•Abuse     :**  {abuse_m}
**•_•Sudo      :**  {is_sudo}
**•_•Gender    :** {Config.BOY_OR_GIRL}
"""
botname = Config.BOT_USERNAME

@bot.on(admin_cmd(pattern="alive$"))
@bot.on(admin_cmd(pattern="alive$", allow_sudo=True))
async def xeno_a(event):
    try:
        xeno = await bot.inline_query(botname, "alive")
        await xeno[0].click(event.chat_id)
        if event.sender_id == SempleBoy:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg)

CmdHelp("alive").add_command(
    'bot', None, 'Ｕｓｅ & Ｓｅｅ'
).add()
