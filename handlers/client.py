from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from keyboards import client


user = Router()


@user.message(CommandStart())
async def cmd_start(msg: Message):
    await msg.answer('Рады приветствовать вас в нашем магазине',
                     reply_markup=client.get_start_kb())


@user.message(F.text == "📦 В наличии")
async def show_availability(msg: Message):
    text = (
        "🏒 Восстановленные клюшки:\n"
        " • Под правый хват: 7 шт\n"
        " • Под левый хват: 3 шт\n"
        "🧵 Лента в наличии:\n"
        " • Черная (12 мм): 22 м\n"
        " • Белая (10 мм): 8 м\n"
        " • Красная (12 мм): 15 м\n\n"
    )
    await msg.answer(text)


@user.message(F.text == '♻️ Восстановленные')
async def choice_sticks(msg: Message):
    await msg.answer('Тут какая-то хуйня')