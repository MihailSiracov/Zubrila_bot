from  aiogram import  types

kb_menu_after_reg = [
    types.KeyboardButton(text='Начать урок'),
    types.KeyboardButton(text='Настройки списка фраз')

]

kb_worlds_list = [
    types.KeyboardButton(text='Добавить фразу'),
    types.KeyboardButton(text='Удолить фразу'),
    types.KeyboardButton(text='Закрыть список')
]

kb_ask = [
    types.KeyboardButton(text='Зарегистрироваться'),
    types.KeyboardButton(text='Войти в акаунт')
]

kb_reg = [
    types.KeyboardButton(text='/reg')
]
