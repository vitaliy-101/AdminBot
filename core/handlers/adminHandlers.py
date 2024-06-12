from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from AdminBot.core.utils.stateForms import CreatingAdminSteps


router = Router()


@router.callback_query(F.data == "insertAdmin")
async def stepAdminId(call: CallbackQuery, state: FSMContext):
    await state.set_state(CreatingAdminSteps.GET_ID)
    await call.message.answer('Введите id нового администратора')


@router.message(CreatingAdminSteps.GET_ID, F.text)
async def stepAdminFirstName(message: Message, state: FSMContext):
    await state.update_data(admin_id=message.text)
    await state.set_state(CreatingAdminSteps.GET_FIRST_NAME)
    await message.answer('Введите имя администратора')


@router.message(CreatingAdminSteps.GET_FIRST_NAME, F.text)
async def stepAdminLastName(message: Message, state: FSMContext):
    await state.update_data(admin_first_name=message.text)
    await state.set_state(CreatingAdminSteps.GET_LAST_NAME)
    await message.answer('Введите фамилию администратора')


@router.message(CreatingAdminSteps.GET_LAST_NAME, F.text)
async def stepAdminGetPhone(message: Message, state: FSMContext):
    await state.update_data(admin_last_name=message.text)
    await state.set_state(CreatingAdminSteps.GET_PHONE)
    await message.answer('Введите номер телефона администратора')


@router.message(CreatingAdminSteps.GET_PHONE, F.text)
async def stepAdminGetPhone(message: Message, state: FSMContext):
    await state.update_data(admin_phone=message.text)
    await state.set_state(CreatingAdminSteps.GET_PHOTO)
    await message.answer('Отправьте фотографию администратора')


@router.message(CreatingAdminSteps.GET_PHOTO, F.photo)
async def stepAdminGetPhoto(message: Message, state: FSMContext):
    # нужно сделать сохрание фото
    await state.update_data(admin_photo=message.photo[-1].file_id)
    await state.set_state(CreatingAdminSteps.GET_PASSPORT)
    await message.answer('Отправьте паспорт администратора')


@router.message(CreatingAdminSteps.GET_PASSPORT, F.text)
async def stepAdminGetPassport(message: Message, state: FSMContext):
    await state.update_data(admin_passport=message.text)
    await state.set_state(CreatingAdminSteps.GET_DISTRICT)
    await message.answer('Отправьте район работы администратора')


@router.message(CreatingAdminSteps.GET_DISTRICT, F.text)
async def stepAdminGetDistrict(message: Message, state: FSMContext):
    await state.update_data(admin_district=message.text)
    await state.set_state(CreatingAdminSteps.DONE)
    await message.answer('Анкета администратор создана')
    user_data = await state.get_data()
    await message.answer(f'Анкета администратора:\n'
                         f'Имя: {user_data["admin_first_name"]}\n'
                         f'Фамилия: {user_data["admin_last_name"]}:\n'
                         f'Фотография: {user_data["admin_photo"]}\n'
                         f'Id: {user_data["admin_id"]}\n'
                         f'Номер телефона: {user_data["admin_phone"]}\n'
                         f'Паспорт: {user_data["admin_passport"]}\n'
                         f'Район: {user_data["admin_district"]}')

    # нужно сделать сохрание анкеты в бд
    await state.clear()


