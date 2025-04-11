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

def creating(cod):
    id = random.randint(100, 10000000).__str__()
    cod = f'{cod[2: -1]}п{id}'
    con.execute(f"""CREATE TABLE IF NOT EXISTS \"{cod}\"
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        worlds TEXT,
        translate TEXT,
        language TEXT,
        mistekes INTEGER)""")
    con.commit()

    return f"""{cod}п{id}"""

def add_world(cod_name, world, translate, language):
    cursor.execute(f"""INSERT INTO {cod_name} (wolds, translater, language) VALUES (?, ?, ?)""", (world, translate, language))
    con.commit()


def dellit_profil(name, password):
    cursor.execute(f"DELETE FROM users WHERE (name, password) VALUES (?,?)""", (name, password, ))
    con.commit()

def data_baza_words(cod_name):
    words = [["Hello World", "Привет Мир", "EN_RU"],
             ["hello", "привет", "EN_RU"]]
    for i in words:
        add_world(cod_name, i[0], i[1], i[2])