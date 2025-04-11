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

def com(tg_id):
    code = "SIR_"
    command = f'{code * 10}Sir='
    command = bytes(command, 'utf-8')
    tg_id = str(tg_id)
    command = Fernet(command)
    print(command)
    ans = command.encrypt(tg_id.encode())
    print(ans)
    return ans.__str__()


#key = Fernet.generate_key()
#command = Fernet(key)
##encrypted_text = command.encrypt(plain_text.encode())
##print(encrypted_text)
##decrypted_text = command.decrypt(encrypted_text).decode()
##print(decrypted_text)
#num = "001010"
#def encrypt_number(number):
#    num_str = str(number)
#    key = Fernet.generate_key()
#    command = Fernet(key)
#    encrypted_text = command.encrypt(num_str.encode())
#    print(encrypted_text)
#
#    encrypted_text = command.encrypt(num_str.decode())
#    print(encrypted_text)
#
#
#