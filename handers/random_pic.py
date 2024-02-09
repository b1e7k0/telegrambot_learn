from aiogram import Router, types, F
from aiogram.filters import Command
import random
import os


pic_router = Router

@pic_router.message(Command("random_pic"))
async def send_picture(message: types.Message):
    folder_path = "./images"
    files = os.listdir(folder_path)
    random_file = random.choice(files)
    file_path = os.path.join(folder_path, random_file)
    photo = types.FSInputFile(file_path)
    await message.answer_photo(photo=photo, caption=f'Лови котика')