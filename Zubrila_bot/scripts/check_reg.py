import sqlite3


from loader import router, cursor, con, scheduler, bot

import json
import random

from cryptography.fernet import Fernet

from scripts.manager_reg_users_data import finding_profils_by_id, finding_profil_n_tg_id

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


def not_ex():
    async def get_gender(message: types.Message, state: FSMContext):
        return await message.answer(text="Вы не зашли в профиль, или не зарегистрировались, просьба принять какоенибудь из ранее упомянутых мер!")
def dek_chek_reg(tg_id, name, need):
    answer_of_finding = finding_profil_n_tg_id(tg_id, name)
    if answer_of_finding == []:
        return not_ex()
    if need == "men_pers_db":
        return name, answer_of_finding[4]