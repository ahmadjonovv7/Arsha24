from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

from loader import obyekt, bot

menu = obyekt.selecet_barcha_menular()
j = 0
index = 0
keys = []
for menu in menu:
        if j % 2 == 0 and j != 0:
            index += 1
        if j % 2 == 0:
            keys.append([KeyboardButton(text=f'{menu[1]}', )])
        else:
            keys[index].append(KeyboardButton(text=f'{menu[1]}', ))
        j += 1
menu_buttons = ReplyKeyboardMarkup(keyboard=keys, resize_keyboard=True)
