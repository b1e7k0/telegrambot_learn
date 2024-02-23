from aiogram import Router, types
from aiogram.filters import Command
from bot import bot, scheduler

scheduled_message_router = Router()


async def send_my_message(chat_id: int, message):
        await bot.send_message(chat_id=chat_id, text=message)


@scheduled_message_router.message(Command("reppeler"))
async def send_later(message: types.Message):
    scheduler.add_job(
        send_my_message,
        'interval',
        seconds=10,
        kwargs={'chat_id': message.from_user.id,
                "message": message.text.replace("/reppeler ", " ")
                }
    )
    await message.answer(" ")



# @scheduled_message_router.message(content_types=['text'])
# def handle_message(message):
#     if message.text.lower().startswith('напомни'):
#         send_my_message().reminder_text = message.text[7:].strip()
#     else:
#         send_my_message().reminder_text = None