from loader import dp, bot
from aiogram.types import Message
from menus.main_menu import MAIN_MENU


async def start(message: Message):
    message_one = "Hi \nThis bot can help you find new people and awesome spend time \nDon't forget to be " \n  "polite with other people"
    animation = open("assets/flame.gif", "rb")
    await bot.send_animation(caption=message_one,
                             animation=animation,
                             reply_markup=MAIN_MENU,
                             chat_id=message.from_user.id)


def commands_file_handlers():
    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(help_command, commands=["help"])
