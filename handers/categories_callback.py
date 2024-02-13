from aiogram import Router, types, F


books_router = Router()

@books_router.callback_query(F.data == "russian")
async def show_russian_books(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Мастер и Маргарита", url="https://ru.wikipedia.org/wiki/%D0%9C%D0%B0%D1%81%D1%82%D0%B5%D1%80_%D0%B8_%D0%9C%D0%B0%D1%80%D0%B3%D0%B0%D1%80%D0%B8%D1%82%D0%B0"),
                types.InlineKeyboardButton(text="Война и Мир", url="https://ilibrary.ru/text/11/index.html")
            ],
            [
                types.InlineKeyboardButton(text="Обломов", url="https://ilibrary.ru/text/475/p.1/index.html"),
                types.InlineKeyboardButton(text="Преступление и Наказание", url="https://ilibrary.ru/text/69/p.1/index.html")
            ]
        ]
    )
    await callback.message.answer("Выберите Произведние", reply_markup=kb)

@books_router.callback_query(F.data == "england")
async def show_england_books(callback: types.CallbackQuery):
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

@books_router.callback_query(F.data == "west")
async def show_phylosophy_books(callback: types.CallbackQuery):
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

@books_router.callback_query(F.data == "east")
async def show_mudrost_books(callback: types.CallbackQuery):
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
