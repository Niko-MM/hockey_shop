from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
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
async def choos_side_stick(msg:Message):
    await msg.answer('В наличии столько-то клюшек', reply_markup=ReplyKeyboardRemove())
    await msg.answer('Выберите хват клюшки', reply_markup=client.choosing_side_stick())


@user.callback_query(F.data == 'left_side')
async def choosing_left_side(callback: CallbackQuery):
    text = ('Восстановленные клюшки (левый хват)\n'
            'В наличии 3 штуки\n\n'
            'Выберите товар'
    )
    await callback.message.answer(text=text) # type: ignore
    await callback.answer()


@user.callback_query(F.data == 'right_side')
async def choosing_right_side(callback: CallbackQuery):
    text = ('Восстановленные клюшки (правый хват)\n'
            'В наличии 5 штуки\n\n'
            'Выберите товар'
    )
    if callback.message:
        await callback.message.answer(text=text) 
    await callback.answer()


@user.callback_query(F.data == 'back')
async def back_choosing_stick(callback: CallbackQuery):
    if not callback.message:
        await callback.answer()
        return

    await callback.message.edit_text( # type: ignore
        text='Выберите хват клюшки',
        reply_markup=client.choosing_side_stick()
    )
    await callback.answer()