from aiogram import Bot, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from core.utils.dbConnection import Request
from core.keyboards.inline import getInlineStartKeyBoard
from aiogram.types import CallbackQuery
from asyncpg import Record

router = Router()


@router.message(Command(commands=['start']))
async def startBotMessage(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}!\nЭто админ бот, который поможет тебе '
                         f'обрабатывать заявки пользователей, желающих покормить животных!))',
                         reply_markup=getInlineStartKeyBoard())


@router.callback_query(F.data == 'getAllRequest')
async def aboutUs(call: CallbackQuery, request: Request):
    await call.message.answer(getAllRequestsMessage(await request.getAllRequests()))


def getAllRequestsMessage(allRequests):
    message = "ЗАЯВКИ:\n"
    message += "-------------------------------------------\n"
    for record in allRequests:
        message += f"name: {record['name']}\nsurname: {record['surname']}\nemail: {record['email']}\nphone: {record['phone']}\n"
        message += "-------------------------------------------\n"
    return message
