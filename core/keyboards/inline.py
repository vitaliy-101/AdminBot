from aiogram.utils.keyboard import InlineKeyboardBuilder


def getInlineStartKeyBoard():
    keyboard_builder = InlineKeyboardBuilder()
    # keyboard_builder.button(text='Получить данные заявок на кор', callback_data='getAllRequest')
    keyboard_builder.button(text='Настройки пользователей', callback_data='getUsersSettings')
    keyboard_builder.button(text='Настройки пункта', callback_data='getPointSettings')
    keyboard_builder.button(text='Работа с волонтерами', callback_data='getVolunteerWork')
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup(one_time_keyboard=True)


def getInlineUserSettingsKeyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Добавить нового администратора', callback_data='insertAdmin')
    keyboard_builder.button(text='Удалить администратора', callback_data='deleteAdmin')
    keyboard_builder.button(text='Добавить нового волонтера', callback_data='insertVolunteer')
    keyboard_builder.button(text='Удалить волонтера', callback_data='deleteVolunteer')
    keyboard_builder.button(text='Изменить данные волонтера', callback_data='updateVolunteer')
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup(one_time_keyboard=True)
