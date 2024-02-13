from aiogram import Router, types, F
from aiogram.filters import Command

start_router = Router()

@start_router.message(Command('start'))
async def start_command(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
                [
                    types.InlineKeyboardButton(text="Наш адресс", url="https://www.google.com/maps/place/Book%D0%B8%D0%BD%D0%B3%D0%B5%D0%BC/@42.8570134,74.5358878,13z/data=!4m10!1m2!2m1!1z0LrQvdC40LbQvdGL0Lk!3m6!1s0x389eb634222f0baf:0x37b39c4056ffb723!8m2!3d42.8570134!4d74.6121055!15sCg7QutC90LjQttC90YvQuVoQIg7QutC90LjQttC90YvQuZIBCmJvb2tfc3RvcmXgAQA!16s%2Fg%2F11byz6kdsp?authuser=0&entry=ttu"),
                    types.InlineKeyboardButton(text="Наш Инстаграмм", url="https://instagram.com/neboskrob1")
                ],
                [
                    types.InlineKeyboardButton(text="О нас", callback_data="about_us")
                ]
            ]
        )
    await message.answer(f"Здраствуйте уважаемый {message.from_user.first_name}!", reply_markup=kb)

@start_router.callback_query(F.data == "about_us")
async def show_about_us(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("Что-то о нас")


