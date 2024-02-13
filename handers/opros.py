from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from keybord.opros_genre_kb import opros_genre_kb

opros_router = Router()

class Opros(StatesGroup):
    name = State()
    age = State()
    genre = State()
    favorite = State()
    recommendation = State()


@opros_router.message(Command('opros'))
async def start_op(message: types.Message, state: FSMContext):
    await state.set_state(Opros.name)
    await message.answer("Как вас зовут?")

@opros_router.message(Command("stop"))
async def stop_reg(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Спасибо за уделенное время, приходите позже!")

@opros_router.message(Opros.name)
async def proces_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Opros.age)
    await message.answer(f"Cколько вам лет {message.text} ?")

@opros_router.message( Opros.age)
async def proces_age(message: types.Message, state: FSMContext):
    remove_kb = opros_genre_kb()
    await state.update_data(age=message.text)
    await state.set_state(Opros.genre)
    await message.answer("Какой ваш любимый жанр?", reply_markup=remove_kb)

@opros_router.message(Opros.genre)
async def process_favorite(message: types.Message, state: FSMContext):
    await state.update_data(genre=message.text)
    await state.set_state(Opros.favorite)
    await message.answer("Ваша любимая книга/книги")

@opros_router.message(Opros.favorite)
async def process_rec(message: types.Message, state: FSMContext):
    await state.update_data(favorite=message.text)
    await state.set_state(Opros.recommendation)
    await message.answer("Какую книгу вы бы посоветовали начинающим читателям)?")

@opros_router.message(Opros.recommendation)
async def process(message: types.Message, state: FSMContext):
    await state.update_data(recommendation=message.text)
    await message.answer("Спасибо за уделённое время")
    data = await state.get_data()
    await message.answer(f"Ваши данные: {data}")
    await state.clear()