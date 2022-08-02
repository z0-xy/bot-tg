import os
import logging
from aiogram import Bot, Dispatcher, executor, types
# from config import TOKEN
logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
def tranlate(s: str):
    k_lower ={'а': 'a',
 'б': 'b',
 'в': 'v',
 'г': 'g',
 'д': 'd',
 'е': 'e',
 'ж': 'zh',
 'з': 'z',
 'и': 'i',
 'й': 'i',
 'к': 'k',
 'л': 'l',
 'м': 'm',
 'н': 'n',
 'о': 'o',
 'п': 'p',
 'р': 'r',
 'с': 's',
 'т': 't',
 'у': 'u',
 'ф': 'f',
 'х': 'kh',
 'ц': 'ts',
 'ч': 'ch',
 'ш': 'sh',
 'щ': 'shch',
 'ъ': 'ie',
 'ы': 'y',
 'э': 'e',
 'ю': 'iu',
 'я': 'ia',
 'ё': 'e'}
    k_upper = {'Ё': 'E',
 'А': 'A',
 'Б': 'B',
 'В': 'V',
 'Г': 'G',
 'Д': 'D',
 'Е': 'E',
 'Ж': 'ZH',
 'З': 'Z',
 'И': 'I',
 'Й': 'I',
 'К': 'K',
 'Л': 'L',
 'М': 'M',
 'Н': 'N',
 'О': 'O',
 'П': 'P',
 'Р': 'R',
 'С': 'S',
 'Т': 'T',
 'У': 'U',
 'Ф': 'F',
 'Х': 'KH',
 'Ц': 'TS',
 'Ч': 'CH',
 'Ш': 'SH',
 'Щ': 'SHCH',
 'Ъ': 'IE',
 'Ы': 'Y',
 'Э': 'E',
 'Ю': 'IU',
 'Я': 'IA'}
    spec = {' ':' ','-':'-'}
    b = True
    new_text=''
    all='абвгдежзийклмнопрстуфхцчшщъыэюяёЁАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЭЮЯ -'
    for i in k_lower.keys():
        all+=i
    for i in k_upper.keys():
        all+=i
    for i in spec.keys():
        all+=i
    for i in s:
        if i in all:
            if i.islower():
                new_text+=(k_lower[i])
            elif i in spec:
                new_text+=i
            else:
                new_text+=(k_upper[i])
        else:
            b = False
    if b is True:
        return (new_text)
    else:
        return('Incorrect input, repeat request')

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_name = message.from_user.first_name
    user_id = message.from_user.id
    text = f'Hi, {user_name} \nEnter your text to translation'
    logging.info(f'{user_name} {user_id} send message: {message.text}')
    await message.reply(text)

@dp.message_handler()
async def send_echo(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = message.text
    logging.info(f'{user_name} {user_id} send message: {text}')
    await bot.send_message(user_id, tranlate(text))
if __name__ == '__main__':
    executor.start_polling(dp)