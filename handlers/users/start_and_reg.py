from aiogram.types import Message
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from keys.keys import kb_ask, kb_menu_after_reg, kb_reg
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
    ask = State()
    name = State()
    password = State()
    profil = State()



@router.message(Command('start'))
async  def fun_start(message: types.Message, state: FSMContext):
    us_id = message.from_user.id
    print(us_id)
    dt_profils = finding_profils_by_id(message.from_user.id)
    if len(dt_profils) >= 1:
        await state.set_state(FormUrl.profil)
        dt_profils.append([0, 0, "Зарегистрировать новый аккаунт"])
        builder = ReplyKeyboardBuilder()
        print(dt_profils)
        for profil in dt_profils:
            builder.add(types.KeyboardButton(text=f'{profil[2]}'))
            builder.adjust(1)
        await message.answer(text='ДРАСТЕ! Выберите профиль:', reply_markup=builder.as_markup(resize_keyboard=True))
    elif len(dt_profils) == 0:
        await state.set_state(FormUrl.ask)
        builder = ReplyKeyboardBuilder()
        for button in kb_ask:
            builder.add(button)
            builder.adjust(1)
        await message.answer(text='ДРАСТЕ! Вы хотите зарегистрироваться или нет?',
                             reply_markup=builder.as_markup(resize_keyboard=True))

@router.message(FormUrl.profil)
async def get_gender(message: types.Message, state: FSMContext):
    await state.update_data(profil=message.text)
    await state.set_state(state.clear())
    data = await state.get_data()
    print(data)
    if data["profil"] == "Зарегистрировать новый аккаунт":
        await state.set_state(not FormUrl)
        builder = ReplyKeyboardBuilder()
        for button in kb_reg:
            builder.add(button)
            builder.adjust(1)
        await message.answer(
            text='Тогда нажмите нажмите на кнопку: "/reg" или в пропишите команду: "/reg" предварительно выйдя из аккаунта',
            reply_markup=builder.as_markup(resize_keyboard=True))
    else:
        builder = ReplyKeyboardBuilder()
        for button in kb_menu_after_reg:
            builder.add(button)
            builder.adjust(1)
        await message.answer(text=f'Здравствуйте {data["profil"]}',
                             reply_markup=builder.as_markup(resize_keyboard=True))


@router.message(FormUrl.ask)
async def get_gender(message: types.Message, state: FSMContext):
    await state.update_data(ask=message.text)
    global name, passwords
    data = await state.get_data()
    if data["ask"] == "Войти в акаунт":
        await state.set_state(FormUrl.name)
        await message.answer(text='Введите имя')
    if data["ask"] == "Зарегистрироваться":
        await state.set_state(not FormUrl)
        builder = ReplyKeyboardBuilder()
        for button in kb_reg:
            builder.add(button)
            builder.adjust(1)
        await message.answer(text='Тогда нажмите нажмите на кнопку: "/reg" или в пропишите команду: "/reg" предварительно выйдя из аккаунта',
                         reply_markup=builder.as_markup(resize_keyboard=True))


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
    adding(id_tg=message.from_user.id, name=data["name"], password=data["password"], name_of_table=creating(cod=com(message.from_user.id)))
    await message.answer(text='Вы зарегистрированы')






