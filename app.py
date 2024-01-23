from common.bot_cmd_list import private
from handlers.user_private import user_private_router
from handlers.user_group import user_group_router
import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())


ALLOWED_UPDATE = ['message, edited_message']

bot = Bot(token=os.getenv('TOKEN_API'))
dp = Dispatcher()

dp.include_router(user_private_router)
dp.include_router(user_group_router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    # await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats)
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATE)


print("Бот готов к работе")
asyncio.run(main())
