from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from AdminBot.core.utils.stateForms import CreatingVolunteerSteps

'''

    GET_PHONE = State()
    GET_EMAIL = State()
    GET_PASSPORT = State()
    DONE = State()
'''



router = Router()


@router.callback_query(F.data == "insertVolunteer")
async def stepVolunteerId(call: CallbackQuery, state: FSMContext):
    await state.set_state(CreatingVolunteerSteps.GET_ID)
    await call.message.answer('Введите id волонтера')


@router.message(CreatingVolunteerSteps.GET_ID, F.text)
async def stepVolunteerFirstName(message: Message, state: FSMContext):
    await state.update_data(volunteer_id=message.text)
    await state.set_state(CreatingVolunteerSteps.GET_FIRST_NAME)
    await message.answer('Введите имя волонтера')

@router.message(CreatingVolunteerSteps.GET_FIRST_NAME, F.text)
async def stepVolunteerLastName(message: Message, state: FSMContext):
    await state.update_data(volunteer_first_name=message.text)
    await state.set_state(CreatingVolunteerSteps.GET_LAST_NAME)
    await message.answer('Введите фамилию волонтера')


@router.message(CreatingVolunteerSteps.GET_LAST_NAME, F.text)
async def stepVolunteerGetPhone(message: Message, state: FSMContext):
    await state.update_data(volunteer_last_name=message.text)
    await state.set_state(CreatingVolunteerSteps.GET_PHONE)
    await message.answer('Введите телефон волонтера')

@router.message(CreatingVolunteerSteps.GET_PHONE, F.text)
async def stepVolunteerGetPhone(message: Message, state: FSMContext):
    await state.update_data(volunteer_phone=message.text)
    await state.set_state(CreatingVolunteerSteps.GET_EMAIL)
    await message.answer('Введите email волонтера')

@router.message(CreatingVolunteerSteps.GET_EMAIL, F.text)
async def stepVolunteerGetPhone(message: Message, state: FSMContext):
    await state.update_data(volunteer_email=message.text)
    await state.set_state(CreatingVolunteerSteps.GET_PASSPORT)
    await message.answer('Введите паспорт волонтера')

@router.message(CreatingVolunteerSteps.GET_PASSPORT, F.text)
async def stepVolunteerGetPhone(message: Message, state: FSMContext):
    await state.update_data(volunteer_passport=message.text)
    await state.set_state(CreatingVolunteerSteps.DONE)
    await message.answer('Анкета создана')
    user_data = await state.get_data()
    await message.answer(f'Анкета Волонтера:\n'
                         f'id: {user_data["volunteer_id"]}\n'
                         f'Имя: {user_data["volunteer_first_name"]}\n'
                         f'Фамилия: {user_data["volunteer_last_name"]}\n'
                         f'Телефон: {user_data["volunteer_phone"]}\n'
                         f'Email: {user_data["volunteer_email"]}\n'
                         f'Паспорт: {user_data["volunteer_passport"]}\n'
                         )
    # нужно сделать сохрание анкеты в бд
    await state.clear()
