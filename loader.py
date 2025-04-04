from aiogram import Bot, Dispatcher, Router
from config.token import TOKEN
import sqlite3
from apscheduler.schedulers.asyncio import AsyncIOScheduler

router = Router()
dp = Dispatcher()
dp.include_router(router)
bot = Bot(TOKEN)
admin_id = [310373667]

con = sqlite3.connect("../Zubrila_bot/all_data/data.db")
command = '{code * 10}Lol='
cursor = con.cursor()



scheduler = AsyncIOScheduler(timezone='Europe/Moscow')