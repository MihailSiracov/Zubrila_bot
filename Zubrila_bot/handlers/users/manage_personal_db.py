import sqlite3

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from loader import router, cursor, con, scheduler, bot
from aiogram import F
import json
import random

from cryptography.fernet import Fernet

@router.message(F.text == "Настройки списка фраз")
async def get_gender(message: types.Message, state: FSMContext):
    await message.answer(text='srdftygvhuijkol')
