import os
from loader import bot
import dotenv
from aiogram import Dispatcher

dotenv.load_dotenv(".env")
ADMINS = [os.getenv("ADMIN")]


async def startup(dp: Dispatcher):
    for person in ADMINS:
        await bot.send_message(text="Started", chat_id=person)


async def shutdown(dp: Dispatcher):
    for person in ADMINS:
        await bot.send_message(text="Shutting down now", chat_id=person)
