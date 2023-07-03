import time
import logging

from aiogram import Bot, Dispatcher, executor, types

from config import TOKEN

logging.basicConfig(filename='bot.log', level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    text = f'Здравствуйте, {user_full_name}! Введи ваше ФИО:'
    logging.info(f'{user_id=} {time.asctime()}')
    await message.reply(text)

@dp.message_handler()
async def latin_conv(message: types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    name = message.text

    if not name.replace(' ', '').isalpha():
        text = 'ФИО может содержать только буквы. Введите ФИО еще раз (через пробел)'
        await message.reply(text)
        logging.info(f'{user_id=} {time.asctime()} ошибка ввода ФИО')
        return

    translit = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i', 
            'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 
            'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': 'ie','ы': 'y', 
            'ь': '', 'э': 'e', 'ю': 'iu', 'я': 'ia', ' ': ' '}
    
    result = []
    for word in name.split():
        res = ''
        for char in word.lower():
            res += translit[char]
        result.append(res)

    name_latin = ' '.join(result).title()

    text = f'Ваше ФИО латиницей: {name_latin}'
    logging.info(f'{user_id=} {time.asctime()} send message {text}')
    await bot.send_message(user_id, text)


if __name__ == '__main__':
    executor.start_polling(dp)