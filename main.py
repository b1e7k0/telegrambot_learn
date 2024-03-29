import asyncio
from aiogram import Bot
from bot import bot, dp, db, set_commands, scheduler
import logging
from handers import (
    start_router,
    pic_router,
    myinfo_router,
    categories_router,
    opros_router,
    rec_router,
    scheduled_message_router
)

async def on_startup(bot: Bot):
    db.create_table()
    db.populate_tables()



async def main():
    await set_commands()
    dp.include_router(start_router)
    dp.include_router(myinfo_router)
    dp.include_router(pic_router)
    dp.include_router(categories_router)
    dp.include_router(opros_router)
    dp.include_router(rec_router)
    dp.startup.register(on_startup)
    dp.include_router(scheduled_message_router)
    scheduler.start()
    scheduler.shutdown()
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())