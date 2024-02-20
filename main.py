import asyncio
from aiogram import Bot
from bot import bot, dp, db, set_commands
import logging
from handers import (
    start_router,
    pic_router,
    myinfo_router,
    categories_router,
    opros_router
)

async def on_startup(bot: Bot):
    db.create_tables()
    db.populate_tables()


async def main():
    await set_commands()
    dp.include_router(start_router)
    dp.include_router(myinfo_router)
    dp.include_router(pic_router)
    dp.include_router(categories_router)
    dp.include_router(opros_router)
    dp.startup.register(on_startup)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())