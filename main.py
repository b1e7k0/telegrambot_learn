import asyncio
from aiogram import types
from bot import bot, dp
import logging
from handers import (
    start_router,
    pic_router,
    myinfo_router,
    categories_router,
    opros_router
)

async def main():
    await bot.set_my_commands([
        types.BotCommand(command="start", description="Начало"),
        types.BotCommand(command="random_pic", description="Получить картинку"),
        types.BotCommand(command="myinfo", description="Информация обо мне"),
        types.BotCommand(command="categories", description="категории книг"),
        types.BotCommand(command="opros", description="пройти опрос")
    ])
    dp.include_router(start_router)
    dp.include_router(myinfo_router)
    dp.include_router(pic_router)
    dp.include_router(categories_router)
    dp.include_router(opros_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())