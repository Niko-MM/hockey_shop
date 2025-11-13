from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_start_kb():
    builder = ReplyKeyboardBuilder()
    builder.button(text='📦 В наличии')
    builder.button(text='♻️ Восстановленные')
    builder.button(text='Лента')
    builder.adjust(1, 2)
    return builder.as_markup(resize_keyboard=True)





