import sqlite3

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from loader import router, cursor, con, scheduler, bot
from aiogram import F
import json

con.execute(f"""CREATE TABLE IF NOT EXISTS users
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    password TEXT,
    id_tg TEXT,
    name_of_table TEXT)""")

def finding_profils_by_id(id_tg):

    cursor.execute('SELECT * FROM users WHERE id_tg=(?)', (id_tg, ))
    answer = cursor.fetchall()
    return answer

def finding_profil(name, password):
    con.execute('SELECT * FROM users WHERE (name, password) VALUES (?, ?)', (name, password, ))
    answer = cursor.fetchall()
    return answer

def adding(id_tg, name, password, name_of_table):
    cursor.execute(f"""INSERT INTO users (id_tg, name, password, name_of_table) VALUES (?, ?, ?, ?)""", (id_tg, name, password, name_of_table,))
    con.commit()

def dellit_profil(name, password):
    cursor.execute(f"DELETE FROM users WHERE (name, password) VALUES (?,?)""", (name, password, ))
    con.commit()