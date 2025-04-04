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

def data_baza_words():
    words = [["Hello World", "Привет Мир", "EN_RU"],
             ["Hello", "привет", "EN_RU"]]

def creating(cod):
    id = random.randint(100, 10000000).__str__()
    cod = f'{cod[2: -1]}_{id}'
    con.execute(f"""CREATE TABLE IF NOT EXISTS \"{cod}\"
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        worlds TEXT,
        translate TEXT,
        language TEXT,
        mistekes INTEGER)""")
    con.commit()

    return f"""{cod}и{id}"""

def add_world(world, name, id_tg):
    con.execute(f'''SELECT (world)={world} FROM users WHERE (name, id_tg)=(?, ?)''', (name, id_tg, ))
    con.commit()


def dellit_profil(name, password):
    cursor.execute(f"DELETE FROM users WHERE (name, password) VALUES (?,?)""", (name, password, ))
    con.commit()
        