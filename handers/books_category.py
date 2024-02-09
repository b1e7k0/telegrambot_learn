from aiogram import Router, types
from aiogram.filters import Command

categories_router = Router

@categories_router.messege(Command('categories'))
async def books_categories(messege: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Русская классика", callback_data="russian"),
                types.InlineKeyboardButton(text="Английская классика", callback_data="england")
            ],
            [
                types.InlineKeyboardButton(text="Западная Философия", callback_data="west"),
                types.InlineKeyboardButton(text="Восточная мудрость", callback_data="east")
            ]
        ]
    )
    await messege.answer("Выберите категорию", reply_markup=kb)


