# HiTechRocket Project  <t.me/HiTechRockets>

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from string.plugins import 
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from string import botz as bot
from string import LOGGER

pm_start_text = """
Heya [{}](tg://user?id={}), I'm Song Downloader Bot 🎵

Just send me the song name you want to download.
eg: ```/song Hello World``` \n ```/video Hello World``` \n ```/yts Hello World```

A bot by @GalaxyLanka
"""


@bot.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Source", url="https://github.com/prabhasha-p/VidsRobot"
                    ),
                    InlineKeyboardButton(
                        text="Developer", url="https://t.me/Prabha_sha"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)


bot.start()
LOGGER.info("TheBot is online.")
idle()
