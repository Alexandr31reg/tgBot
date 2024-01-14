import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Это была команда старт')


@dp.message()
async def echo(message: types.Message):
    text = message.text

    if text in ['Привет', 'привет', 'hi', 'hello']:
        await message.answer('И тебе привет!')
    elif text in ['Пока', 'пока', 'пакеда', 'До свидания']:
        await message.answer('И тебе пока')
    else:
        await message.answer(message.text)


async def main():
    await dp.start_polling(bot)


print("Бот запущен")
asyncio.run(main())
