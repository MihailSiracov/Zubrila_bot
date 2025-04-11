from aiogram.types import Message
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from keys.keys import kb_ask
from loader import router
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram import types
from aiogram import F

from scripts.manager_reg_users_data import finding_profils_by_id, finding_profil_n_p, adding, dellit_profil