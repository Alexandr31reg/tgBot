from re import I
from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command, or_f
from filters.chat_types import ChatTypeFilter
from aiogram.types.web_app_info import WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder

def webapp_builder() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.button(
        text='Open page', web_app=WebAppInfo(
            url="https://alexandr31reg.github.io/"
            )
    )
    return builder.as_markup()

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Привет, я виртуальный помощник', reply_markup=webapp_builder())


# @user_private_router.message(F.text.lower() == "меню")
@user_private_router.message(or_f(Command('menu'), (F.text.lower() == "меню")))
async def menu_cmd(message: types.Message):
    await message.answer("Вот меню:")


@user_private_router.message(F.text.lower() == "о нас")
@user_private_router.message(Command('about'))
async def menu_cmd_about(message: types.Message):
    await message.answer("О нас:")


@user_private_router.message(F.text.lower() == "варианты оплаты")
@user_private_router.message(Command('payment'))
async def payment_cmd(message: types.Message):
    await message.answer("Варивнты оплаты:")


@user_private_router.message((F.text.lower().contains('доставк')) | (F.text.lower() == 'варианты доставки'))
@user_private_router.message(Command('shipping'))
async def menu_cmd(message: types.Message):
    await message.answer("Варианты доставки:")
