import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
from os import getenv
import logging
import random
import os


load_dotenv()
bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher()

@dp.message(Command('start'))
async def start_command(message: types.Message):
    print(message.text)
    await message.answer(f"Здраствуйте уважаемый {message.from_user.first_name}!")

@dp.message(Command('myinfo'))
async def send_user_info(message: types.Message):
    await message.answer(f"Ваш ник: {message.from_user.username}\n"
                         f" Ваше имя: {message.from_user.first_name}\n "
                         f"Ваш id: {message.from_user.id}")




@dp.message(Command("random_pic"))
async def send_picture(message: types.Message):
    folder_path = "./images"
    files = os.listdir(folder_path)
    random_file = random.choice(files)
    file_path = os.path.join(folder_path, random_file)
    photo = types.FSInputFile(file_path)
    await message.answer_photo(photo=photo, caption=f'Лови котика')

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())