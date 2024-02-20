from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from os import getenv
from data_base.base import DB


load_dotenv()
bot = Bot(token=getenv('TOKEN'))
dp = Dispatcher()
db = DB()


async def set_commands():
    await bot.set_my_commands([
        types.BotCommand(command="start", description="Начало"),
        types.BotCommand(command="pic", description="Получить картинку"),
        types.BotCommand(command="opros", description="пройти опрос"),
        types.BotCommand(command="myinfo", description="Моя информация"),
        types.BotCommand(command='recomendation', description='Рекомендации'),
        types.BotCommand(command="categories", description="категории")
    ])

