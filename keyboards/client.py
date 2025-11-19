from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

# ReplyKeyboard


def get_start_kb():
    builder = ReplyKeyboardBuilder()
    builder.button(text='📦 В наличии')
    builder.button(text='♻️ Восстановленные')
    builder.button(text='Лента')
    builder.adjust(1, 2)
    return builder.as_markup(resize_keyboard=True)


# InlineKeyBoard

def choosing_side_stick():
    builder = InlineKeyboardBuilder()
    builder.button(text='Левый хват', callback_data='left_side')
    builder.button(text='Правый хват', callback_data='right_side')
    builder.button(text='Назад', callback_data='back')
    builder.adjust(2, 1)
    return builder.as_markup()


def show_left_sticks():
    builder = InlineKeyboardBuilder()
    builder.button(text='->', callback_data='➡️_left')
    builder.button(text='<-', callback_data='⬅️_left')
    builder.button(text='назад', callback_data='back_choosing_stick')
    builder.adjust(2, 1)
    return builder.as_markup()


def show_right_sticks():
    builder = InlineKeyboardBuilder()
    builder.button(text='->', callback_data='➡️_right')
    builder.button(text='<-', callback_data='⬅️_right')
    builder.button(text='назад', callback_data='back_choosing_stick')
    builder.adjust(2, 1)
    return builder.as_markup()









