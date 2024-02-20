from aiogram import Router, types, F
from aiogram.filters import Command
from data_base.base import DB

categories_router = Router()

@categories_router.message(Command('categories'))
async def books_categories(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[]
    )
    db = DB()
    for category in db.get_genre():
        kb.inline_keyboard.append([types.InlineKeyboardButton(text=f'{category[1]}', callback_data=f'cat_{category[0]}')])
    await message.answer('Выберите категорию', reply_markup=kb)


@categories_router.callback_query(F.data.startwith('cat_'))
async def books_by_category(callback: types.CallbackQuery):
    cat_id = int(callback.data.replace('cat_', ""))
    db = DB
    books = db.books_by_cat(cat_id)
    if len(books) == 0:
        await callback.message.answer("Книги такого жанра нет")
    else:
        for book in books:
            text = (
                f"автор: {book[1]}\n"
                f"название книги: {book[2]}\n"
                f"год выпуска: {book[3]}\n"
                f"описание: {book[4]}"
                            )
            await callback.message.answer(text=text)
