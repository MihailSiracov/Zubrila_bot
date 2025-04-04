from aiogram.types import Message
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from keys.keys import kb_ask, kb_menu_after_reg
from loader import router, command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram import types
from aiogram import F

from scripts.manager_persanal_db import creating, add_world, dellit_profil

from scripts.manager_reg_users_data import finding_profils_by_id, finding_profil, adding, dellit_profil
from scripts.manager_coding import com


class FormUrl(StatesGroup):
    name = State()
    password = State()


@router.message(Command('reg'))
async def get_gender(message: types.Message, state: FSMContext):
    await state.update_data(ask=message.text)
    await state.set_state(FormUrl.name)
    await message.answer(text='Введите имя', reply_markup=types.ReplyKeyboardRemove())

@router.message(FormUrl.name)
async def get_gender(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(FormUrl.password)
    await message.answer(text='Введите пароль')

@router.message(FormUrl.password)
async def get_gender(message: types.Message, state: FSMContext):
    await state.update_data(password=message.text)
    await state.set_state(not FormUrl)
    data = await state.get_data()
    adding(id_tg=message.from_user.id, name=data["name"], password=data["password"], name_of_table=creating(cod=com(command, message.from_user.id)))
    await message.answer(text='Вы зарегистрированы')