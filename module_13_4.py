from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

import asyncio

from pyexpat.errors import messages

api = "7257768067:AAErulgPP6DOkAqrvErIGlFun8hb04mWO-E"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.")

@dp.message_handler(text="Calories")
async def set_age(message):
    await message.answer("Введите свой возраст: ")
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой рост в (см): ")
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(weight=message.text)
    await message.answer("Введите свой вес в (кг): ")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(calories=message.text)
    data = await state.get_data()

    await message.answer(f"Ваша норма калорий  , 10 * {data['weight']} + 6.25 * {data['growth']} + 5 * {data['age']} + 5, ккал")
    await state.finish()

@dp.message_handler()
async def all_massages(message):
    await message.answer("Введите команду /start, чтобы начать общение.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)