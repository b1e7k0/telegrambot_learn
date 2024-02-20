import random

from aiogram import Router, types, F
from aiogram.filters import Command
from data_base.base import DB
from random import choice
categories_router = Router()

@categories_router.message(Command('categories'))
async def books_categories(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Романтика", callback_data="romantic"),
                types.InlineKeyboardButton(text="Триллер", callback_data="triller")
            ],
            [
                types.InlineKeyboardButton(text="Фэнтези", callback_data="fantasy"),
                types.InlineKeyboardButton(text="Утопия", callback_data="utopya")
            ]
        ]
    )
    await message.answer("Выберите категорию", reply_markup=kb)


@categories_router.callback_query(F.data == "romantic")
async def show_romantic_books(callback: types.CallbackQuery):
    r_book = random.choice(DB.)
    await callback.message.answer()

@categories_router.callback_query(F.data == "triller")
async def show_triller_books(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Повелитель мух", url="https://liteka.ru/english/library/3182-lord-of-the-flies"),
                types.InlineKeyboardButton(text="Над пропастью во ржи", url="https://www.litres.ru/book/dzherom-devid-selindzher-48197/nad-propastu-vo-rzhi-127781/")
            ],
            [
                types.InlineKeyboardButton(text="1984", url="https://www.litres.ru/audiobook/dzhordzh-oruell/1984-63615603/"),
                types.InlineKeyboardButton(text="Ночь в Лиссабоне", url="https://www.litres.ru/book/erih-mariya-remark/noch-v-lissabone-27061646/chitat-onlayn/")
            ]
        ]
    )
    await callback.message.answer("Выберите Произведние", reply_markup=kb)

@categories_router.callback_query(F.data == "fantasy")
async def show_fantasy_books(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Фридрих Ницше", url="https://www.litres.ru/book/v-cherepenchuk/nicshe-principy-idei-sudba-45113627/"),
                types.InlineKeyboardButton(text="Имманиул Кант", url="https://www.litres.ru/book/natalya-petrovna-serdceva/kant-principy-idei-sudba-43295964/")
            ],
            [
                types.InlineKeyboardButton(text="Искусство побеждать в спорах(А. Шопэнгауер)", url="https://www.litres.ru/audiobook/artur-shopengauer/iskusstvo-pobezhdat-v-sporah-mysli-67940763/"),
            ]
            ]
    )
    await callback.message.answer("Выберите Произведние", reply_markup=kb)

@categories_router.callback_query(F.data == "utopya")
async def show_utopya_books(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Книга пяти колец", url="https://www.litres.ru/book/miyamoto-musasi/kniga-pyati-kolec-145152/")
            ],
            [
                types.InlineKeyboardButton(text="Самурай без меча", url="https://www.litres.ru/book/kitami-masao/samuray-bez-mecha-10315367/")
            ],
            [
                types.InlineKeyboardButton(text="Великое учение", url="https://www.litres.ru/book/konfuciy/velikoe-uchenie-39147279/")
            ]
        ]
    )
    await callback.message.answer("Выберите Произведние", reply_markup=kb)