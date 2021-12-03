# XENOBOT Assistant
from . import *
from telethon import Button, custom

from userbot import bot

from userbot import ALIVE_NAME
OWNER_NAME = ALIVE_NAME
OWNER_ID = bot.uid


XENO_USER = bot.me.first_name
SempleBoy = bot.uid

xeno_mention = f"[{XENO_USER}](tg://user?id={SempleBoy})"
XENO_logo = "./userbot/resources/pics/-6163428037589314866_121.jpg"
XENO_logo1 = "./userbot/resources/pics/-4965507108355287505_121.jpg"
XENO_logo2 = "./userbot/resources/pics/-4965507108355287505_121.jpg"
XENO_logo4 = "./userbot/resources/pics/-4965507108355287505_121.jpg"
XENO_logo3 = "./userbot/resources/pics/-4965507108355287505_121.jpg"
XENOversion = "𝚅1.𝙾"

perf = "[ Xeno UsᴇʀBᴏᴛ ]"


DEVLIST = [
    "1938996006"
]

async def setit(event, name, value):
    try:
        event.set(name, value)
    except BaseException:
        return await event.edit("`Something Went Wrong`")


def get_back_button(name):
    button = [Button.inline("« Bᴀᴄᴋ", data=f"{name}")]
    return button
