from aiogram.utils.keyboard import InlineKeyboardBuilder


def getInlineStartKeyBoard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Получить данные заявок на корм', callback_data='getAllRequest')
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup(one_time_keyboard=True)
