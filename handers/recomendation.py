from aiogram import Router, types
from aiogram.filters import Command
from data_base.base import DB

rec_router = Router()

@rec_router.message(Command("recomendation"))
async def get_rec(message: types.Message):
    db = DB()
    rec = db.get_recomendation()
    await message.answer(f"все рекомендации: ")
    for recomendation in rec:
        text = (
                f"имя пользователя: {recomendation[1]}\n"
                f"любимое: {recomendation[4]}\n"
                f"рекомендация пользователя: {recomendation[5]}\n"
                )
        await message.answer(text=text)
