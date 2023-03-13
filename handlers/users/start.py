import datetime

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

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
    tur = obyekt.select_type(nomi=text)
    maxsulotlar = obyekt.select_maxsulotlar(tur_id=tur[0])
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
    maxsulot_buttons = ReplyKeyboardMarkup(keyboard=keys, resize_keyboard=True)
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id,text='Maxsulotlarni tanlang',reply_markup=maxsulot_buttons)



menular = obyekt.selecet_XAMMA_maxsulotlar()
print(menular)
@dp.message_handler(text=[menu[1] for menu in menular])
async def bot_start(message: types.Message):
    text = message.text
    print(text)
    """(1, 'krasofka', 'https://t.me/turkiyadonali/6327', 219, 'Dastafka bepul', 'Oyoq kiyimlar 👟')"""
    maxsulot = obyekt.select_maxsulot(nomi=text)
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
    await bot.send_photo(chat_id=user_id,photo=max_rasmi,caption=malumot)





# """https://dog.ceo/api/breeds/image/random"""
#
# import requests
# @dp.message_handler(commands='dogs')
# async def bot_start(message: types.Message):
#     url_manzil = "https://dog.ceo/api/breeds/image/random"
#     malumot = requests.get(url_manzil).json()
#     rasm_manzili = malumot['message']
#     await bot.send_photo(chat_id=message.from_user.id,photo=rasm_manzili)









import requests


def get_redirected_url(url_to_request):
    get_request = requests.get(url_to_request)
    redirected_url = str(get_request.url)

    return redirected_url


class TikTokApi:
    def __init__(self):
        self.main_url = 'https://www.tiktok.com/node/{}'
        self.api_url = 'https://www.tiktok.com/api/{}'
        self.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}

    def _make_request(self, url_path, params=None):
        get_request = requests.get(self.main_url.format(url_path), headers=self.headers, params=params)
        response_json = get_request.json()

        return response_json

    def get_music_by_id(self, music_id):
        url_path = 'share/music/original-sound-{}'.format(music_id)
        response_json = self._make_request(url_path)

        return response_json

    def get_music_by_url(self, music_url):
        redirected_url = get_redirected_url(music_url)
        music_id = redirected_url.split('?')[0].split('-')[-1]
        music_info = self.get_music_by_id(music_id)

        return music_info

    def get_music_feed_by_id(self, music_id, max_cursor=0, count=10):
        params = {"type": 4, "secUid": "", "id": music_id, "count": count, "minCursor": 0,
                  "maxCursor": max_cursor, "shareUid": "", "lang": "", "verifyFp": ""}

        url_path = 'video/feed'
        response_json = self._make_request(url_path, params)

        return response_json

    def get_music_feed_by_url(self, music_url, max_cursor=0, count=10):
        redirected_url = get_redirected_url(music_url)
        music_id = redirected_url.split('?')[0].split('-')[-1]

        params = {"type": 4, "secUid": "", "id": music_id, "count": count, "minCursor": 0,
                  "maxCursor": max_cursor, "shareUid": "", "lang": "", "verifyFp": ""}

        url_path = 'video/feed'
        response_json = self._make_request(url_path, params)

        return response_json

    def get_trending_feed(self, max_cursor=0, count=10):
        params = {"type": 5, "secUid": "", "id": 1, "count": count, "minCursor": 0, "maxCursor": max_cursor,
                  "shareUid": "", "lang": "", "verifyFp": ""}

        url_path = 'video/feed'
        response_json = self._make_request(url_path, params)

        return response_json

    def get_user_by_username(self, username):
        url_path = 'share/user/@{}'.format(username)
        response_json = self._make_request(url_path)

        return response_json

    def get_user_by_url(self, user_url):
        redirected_url = get_redirected_url(user_url)
        username = redirected_url.split('?')[0].split('@')[1]
        response_json = self.get_user_by_username(username)

        return response_json

    def get_user_feed_by_id(self, user_id, max_cursor=0, count=10):
        params = {"type": 1, "secUid": "", "id": user_id, "count": count, "minCursor": 0, "maxCursor": max_cursor,
                  "shareUid": "", "lang": "", "verifyFp": ""}

        url_path = 'video/feed'
        response_json = self._make_request(url_path, params)

        return response_json

    def get_user_feed_by_username(self, username, max_cursor=0, count=10):
        user_info = self.get_user_by_username(username)
        user_id = user_info['userInfo']['user']['id']

        response_json = self.get_user_feed_by_id(user_id, max_cursor, count)

        return response_json

    def get_user_feed_by_url(self, user_url, max_cursor=0, count=10):
        user_info = self.get_user_by_url(user_url)
        user_id = user_info['userInfo']['user']['id']

        params = {"type": 1, "secUid": "", "id": user_id, "count": count, "minCursor": 0, "maxCursor": max_cursor,
                  "shareUid": "", "lang": "", "verifyFp": ""}

        url_path = 'video/feed'
        response_json = self._make_request(url_path, params)

        return response_json

    def get_challenge_info(self, challenge):
        url_path = 'share/tag/{}'.format(challenge)

        response_json = self._make_request(url_path,)

        return response_json

    def get_challenge_feed(self, challenge, max_cursor=0, count=10):
        challenge_info = self.get_challenge_info(challenge)
        challenge_id = challenge_info['challengeInfo']['challenge']['id']

        params = {"type": 3, "secUid": "", "id": challenge_id, "count": count, "minCursor": 0,
                  "maxCursor": max_cursor, "shareUid": "", "lang": "", "verifyFp": ""}

        url_path = 'video/feed'
        response_json = self._make_request(url_path, params)

        return response_json

    def get_video_by_id(self, video_id):
        return video_id

    def get_video_by_url(self, video_url):
        redirected_url = get_redirected_url(video_url)
        if 'com/v/' in redirected_url:
            video_id = redirected_url.split('/v/')[1].split('.')[0].replace('/', '')
        else:
            video_id = redirected_url.split('/video/')[1].split('?')[0].replace('/', '')

        response_json = self.get_video_by_id(video_id)

        return response_json














#
# from datetime import datetime
# from tqdm import tqdm
# import requests
# import re
# import sys
#
# # Banner
# print('''
#
# 01001001 01101110 01110011 01110100 01100001 01010011 01100001 01110110 01100101
#                         [Coded By Sameera Madushan]
#
# ''')
#
#
# # Function to check the internet connection
# # Got this from https://stackoverflow.com/a/24460981
# def connection(url='http://www.google.com/', timeout=5):
#     try:
#         req = requests.get(url, timeout=timeout)
#         req.raise_for_status()
#         print("You're connected to internet\n")
#         return True
#     except requests.HTTPError as e:
#         print("Checking internet connection failed, status code {0}.".format(
#             e.response.status_code))
#     except requests.ConnectionError:
#         print("No internet connection available.")
#     return False
#
#
# # Function to download an instagram photo or video
# def download_image_video():
#     url = input("Please enter image URL: ")
#     x = re.match(r'^(https:)[/][/]www.([^/]+[.])*instagram.com', url)
#
#     try:
#         if x:
#             request_image = requests.get(url)
#             src = request_image.content.decode('utf-8')
#             check_type = re.search(r'<meta name="medium" content=[\'"]?([^\'" >]+)', src)
#             check_type_f = check_type.group()
#             final = re.sub('<meta name="medium" content="', '', check_type_f)
#
#             if final == "image":
#                 print("\nDownloading the image...")
#                 extract_image_link = re.search(r'meta property="og:image" content=[\'"]?([^\'" >]+)', src)
#                 image_link = extract_image_link.group()
#                 final = re.sub('meta property="og:image" content="', '', image_link)
#                 _response = requests.get(final).content
#                 file_size_request = requests.get(final, stream=True)
#                 file_size = int(file_size_request.headers['Content-Length'])
#                 block_size = 1024
#                 filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
#                 t = tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)
#                 with open(filename + '.jpg', 'wb') as f:
#                     for data in file_size_request.iter_content(block_size):
#                         t.update(len(data))
#                         f.write(data)
#                 t.close()
#                 print("Image downloaded successfully")
#
#             if final == "video":
#                 msg = input("You are trying to download a video. Do you want to continue? (Yes or No): ".lower())
#
#                 if msg == "yes":
#                     print("Downloading the video...")
#                     extract_video_link = re.search(r'meta property="og:video" content=[\'"]?([^\'" >]+)', src)
#                     video_link = extract_video_link.group()
#                     final = re.sub('meta property="og:video" content="', '', video_link)
#                     _response = requests.get(final).content
#                     file_size_request = requests.get(final, stream=True)
#                     file_size = int(file_size_request.headers['Content-Length'])
#                     block_size = 1024
#                     filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
#                     t = tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)
#                     with open(filename + '.mp4', 'wb') as f:
#                         for data in file_size_request.iter_content(block_size):
#                             t.update(len(data))
#                             f.write(data)
#                     t.close()
#                     print("Rasm yuklab olindi")
#
#                 if msg == "no":
#                     exit()
#         else:
#             print("Entered URL is not an instagram.com URL.")
#     except AttributeError:
#         print("Unknown URL")
#
#
# # Function to download profile picture of instagram accounts
# def pp_download():
#     url = input("Please enter the URL of the profile: ")
#     x = re.match(r'^(https:)[/][/]www.([^/]+[.])*instagram.com', url)
#
#     if x:
#         check_url1 = re.match(r'^(https:)[/][/]www.([^/]+[.])*instagram.com[/].*\?hl=[a-z-]{2,5}', url)
#         check_url2 = re.match(
#             r'^(https:)[/][/]www.([^/]+[.])*instagram.com$|^(https:)[/][/]www.([^/]+[.])*instagram.com/$', url)
#         check_url3 = re.match(r'^(https:)[/][/]www.([^/]+[.])*instagram.com[/][a-zA-Z0-9_]{1,}$', url)
#         check_url4 = re.match(r'^(https:)[/][/]www.([^/]+[.])*instagram.com[/][a-zA-Z0-9_]{1,}[/]$', url)
#
#         if check_url3:
#             final_url = url + '/?__a=1'
#
#         if check_url4:
#             final_url = url + '?__a=1'
#
#         if check_url2:
#             final_url = print("Please enter an URL related to a profile")
#             exit()
#
#         if check_url1:
#             alpha = check_url1.group()
#             final_url = re.sub('\\?hl=[a-z-]{2,5}', '?__a=1', alpha)
#
#     try:
#         if check_url3 or check_url4 or check_url2 or check_url1:
#             req = requests.get(final_url)
#             get_status = requests.get(final_url).status_code
#             get_content = req.content.decode('utf-8')
#
#             if get_status == 200:
#                 print("\nDownloading the image...")
#                 find_pp = re.search(r'profile_pic_url_hd\":\"([^\'\" >]+)', get_content)
#                 pp_link = find_pp.group()
#                 pp_final = re.sub('profile_pic_url_hd":"', '', pp_link)
#                 file_size_request = requests.get(pp_final, stream=True)
#                 file_size = int(file_size_request.headers['Content-Length'])
#                 block_size = 1024
#                 filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
#                 t = tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)
#                 with open(filename + '.jpg', 'wb') as f:
#                     for data in file_size_request.iter_content(block_size):
#                         t.update(len(data))
#                         f.write(data)
#                 t.close()
#                 print("Profile picture downloaded successfully")
#
#     except Exception:
#         print('error')
#
#
# if connection() == True:
#     try:
#         while True:
#             a = "Instagram profil rasmini yuklab olish uchun 'A' tugmasini bosing.\nInstagram fotosurati yoki videosini yuklab olish uchun 'B' tugmasini bosing.\nChiqish uchun 'Q' tugmasini bosing. "
#             print(a)
#             select = str(input("\nInstaSave > ")).upper()
#             try:
#                 if select == 'A':
#                     pp_download()
#                 if select == 'B':
#                     download_image_video()
#                 if select == 'Q':
#                     sys.exit()
#                 else:
#                     sys.exit()
#             except (KeyboardInterrupt):
#                 print("Programme Interrupted")
#     except(KeyboardInterrupt):
#         print("\nProgramme Interrupted")
# else:
#     sys.exit()
#
