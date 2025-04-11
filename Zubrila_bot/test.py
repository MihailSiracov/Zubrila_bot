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

def code(tg_id):
    code = "SIR_"
    command = f'{code * 10}Lol='
    command = bytes(command, 'utf-8')
    command = Fernet(command)
    ans = command.encrypt(tg_id.encode()).__str__()

    print(ans)
    return ans

def decode(ans):
    cmmand = Fernet(bytes(f"{'Sire' * 10}Lol=", 'utf-8'))
    ans = str(ans)
    ans = cmmand.decrypt(ans).decode()
    return ans

print(code("345678"))
print(decode(code("345678")))