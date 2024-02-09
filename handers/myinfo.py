from aiogram import Router, types, F
from aiogram.filters import Command

myinfo_router = Router

@myinfo_router.message(Command('myinfo'))
async def send_user_info(message: types.Message):
    await message.answer(f"Ваш ник: {message.from_user.username}\n"
                         f" Ваше имя: {message.from_user.first_name}\n "
                         f"Ваш id: {message.from_user.id}")
