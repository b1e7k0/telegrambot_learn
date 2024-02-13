from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def opros_genre_kb():
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Бизнес"),
                KeyboardButton(text="Классика"),
                KeyboardButton(text="Фентези\n Фантастика")
            ],
            [
                KeyboardButton(text="История"),
                KeyboardButton(text="Детективы"),
                KeyboardButton(text="Психология")
            ]
        ],
    resize_keyboard = True
    )
    return kb