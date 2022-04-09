from Helper.helper import start_text, help_text
from config import bot
from telethon import events

class start():

    @bot.on(events.NewMessage(pattern=r"^/start$|^/start@AnimeGallery_ByKazeBot"))
    async def event_handler_start(event):
        await bot.send_message(
            event.chat_id,
            start_text,
            file='https://tenor.com/view/chika-fujiwara-kaguya-sama-love-is-war-anime-wink-smile-gif-18043249'
        )

    @bot.on(events.NewMessage(pattern=r"^/help$|^/help@AnimeGallery_ByKazeBot"))
    async def event_handler_help(event):
        await bot.send_message(
            event.chat_id,
            help_text
            )

    @bot.on(events.NewMessage(pattern="/source"))
    async def event_handler_source(event):
        await bot.send_message(
            event.chat_id,
            '[Source Code On Github](https://github.com/PunyaChael/AnimeGalleryBot)\nThis bot was hosted on Heroku'
        )
    