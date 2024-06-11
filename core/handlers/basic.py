from aiogram import Bot, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from core.utils.dbConnection import Request
from core.keyboards.inline import getInlineStartKeyBoard, getInlineUserSettingsKeyboard
from aiogram.fsm.context import FSMContext
from core.utils.stateForms import CreatingAdminSteps
from aiogram.types import CallbackQuery
from asyncpg import Record

router = Router()


@router.message(Command(commands=['start']))
async def startBotMessage(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}!\nЭто административный бот, который поможет '
                         f'контролировать процесс кормления животных. Бот позволяет администратору взаимодействовать с курьерами, '
                         f'обновлять данные пунктов хранения корма и помогать животным!))',
                         reply_markup=getInlineStartKeyBoard())


@router.callback_query(F.data == "getUsersSettings")
async def userSettingsMenu(call: CallbackQuery):
    # await call.message.answer(getAllRequestsMessage(await request.getAllRequests()))
    await call.message.answer(f'Здесь, вы можете заниматься обновлением, удалением и созданием новых '
                              f'пользователей. Пользователи делятся на два типа: Админ и Волонтер. В роли админа '
                              f'вы можете использовать функционал представленных кнопок',
                              reply_markup=getInlineUserSettingsKeyboard())


@router.callback_query(F.data == "insertAdmin")
async def stepAdminId(call: CallbackQuery, state: FSMContext):
    await state.set_state(CreatingAdminSteps.GET_ID)
    await call.message.answer('Введите id нового администратора')


@router.callback_query(CreatingAdminSteps.GET_ID, F.text)
async def stepAdminFirstName(message: Message, state: FSMContext):
    await state.update_data(admin_id=message.text)
    await state.set_state(CreatingAdminSteps.GET_FIRST_NAME)
    await message.answer('Введите имя администратора')


@router.callback_query(CreatingAdminSteps.GET_FIRST_NAME, F.text)
async def stepAdminLastName(message: Message, state: FSMContext):
    await state.update_data(admin_first_name=message.text)
    await state.set_state(CreatingAdminSteps.GET_LAST_NAME)
    await message.answer('Введите фамилию администратора')


def getAllRequestsMessage(allRequests):
    message = "ЗАЯВКИ:\n"
    message += "-------------------------------------------\n"
    for record in allRequests:
        message += f"name: {record['name']}\nsurname: {record['surname']}\nemail: {record['email']}\nphone: {record['phone']}\n"
        message += "-------------------------------------------\n"
    return message
