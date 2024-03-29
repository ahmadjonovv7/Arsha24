import datetime

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

from keyboards.default.menuu import menu_buttons
from loader import dp, obyekt, bot

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum sizni Supreme uz botda korganimizdan hursandmiz, {message.from_user.full_name}!",reply_markup=menu_buttons)



@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    ism = message.from_user.first_name
    familya = message.from_user.last_name
    username = message.from_user.username
    user_id = message.from_user.id
    date = datetime.datetime.now()
    try:
        obyekt.user_qoshish(ism=ism,tg_id=user_id,fam=familya,username=username,date=date)
    except Exception:
        pass
    await message.answer(f"{message.from_user.full_name}!")


@dp.message_handler(commands='reklama', chat_id ='1358690178')
async def bot_start(message: types.Message):
    userlar = obyekt.selecet_barcha_user()
    print(userlar)

    for user in userlar:
        await bot.send_photo(chat_id=user[4], photo='https://t.me/UstozShogird/26311',caption='salom')


@dp.message_handler(text='Ortga')
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id,text='Maxsulotlarni tanlang',reply_markup=menu_buttons)


menular = obyekt.selecet_barcha_menular()
@dp.message_handler(text=[menu[1] for menu in menular])
async def bot_start(message: types.Message):
    text = message.text
    print(text)
    tur = obyekt.select_maxsulotlar(nomi=text)
    print(tur)
    maxsulotlar = obyekt.select_maxsulotlar(tur=text[0])
    j = 0
    index = 0
    keys = []
    for menu in maxsulotlar:
        if j % 2 == 0 and j != 0:
            index += 1
        if j % 2 == 0:
            keys.append([KeyboardButton(text=f'{menu[1]}', )])
        else:
            keys[index].append(KeyboardButton(text=f'{menu[1]}', ))
        j += 1
    keys.append([KeyboardButton(text='Bosh menu ')])
    menu_buttons = ReplyKeyboardMarkup(keyboard=keys, resize_keyboard=True)
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id,text='Maxsulotlarni tanlang',reply_markup=menu_buttons)



menular = obyekt.selecet_XAMMA_maxsulotlar()
print(menular)
@dp.message_handler(text=[menu[1] for menu in menular])
async def bot_start(message: types.Message):
    text = message.text
    print(text)
    """(1, 'krasofka', 'https://t.me/turkiyadonali/6327', 219, 'Dastafka bepul', 'Oyoq kiyimlar 👟')"""
    maxsulot = obyekt.select_maxsulot(nomi=text)
    max_id = maxsulot(0)
    max_nomi = maxsulot[1]
    max_narxi = maxsulot[3]
    max_rasmi = maxsulot[2]
    max_text = maxsulot[4]
    user_id = message.from_user.id
    malumot = f"#New Collection  \n \n" \
              f"🔠 Бренд: {max_nomi} \n" \
              f"💸Цена: {max_narxi} \n" \
              f" {max_text}  \n " \
              f"🧑🏻‍💻 Buyurtma berish uchun: @ahmadjonovv7 \n"
    await bot.send_photo(chat_id=user_id,photo=max_rasmi,caption=malumot,
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton(text="Sotib olish",callback_data=f"buy{max_id}")
                ]
            ]))



@dp.callback_query_handler()
async def bot_start(xabar: CallbackQuery):
    malumot = xabar.data
    print(malumot)
    await bot.send_message(f"Salom{xabar.from_user.full_name}")