from aiogram.fsm.state import StatesGroup, State


class CreatingAdminSteps(StatesGroup):
    GET_ID = State()
    GET_FIRST_NAME = State()
    GET_LAST_NAME = State()
    GET_PHONE = State()
    GET_PHOTO = State()
    GET_PASSPORT = State()
    GET_DISTRICT = State()
    DONE = State()


class CreatingVolunteerSteps(StatesGroup):
    GET_ID = State()
    GET_FIRST_NAME = State()
    GET_LAST_NAME = State()
    GET_PHONE = State()
    GET_EMAIL = State()
    GET_PASSPORT = State()
    DONE = State()