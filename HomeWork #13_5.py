from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

api = "**********************************************"
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

button_calc = KeyboardButton(text = 'Расчитать')
button_info = KeyboardButton(text = 'Информация')
keyboard = ReplyKeyboardMarkup(resize_keyboard = True).row(button_calc, button_info)

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer("Привет! Давай посчитаем калории...", reply_markup = keyboard)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text = ['Расчитать'])
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(first = message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(second = message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state = UserState.weight)
async def send_calories(message, state):
    await state.update_data(third = message.text)
    data = await state.get_data()
    calories = 10 * float(data['third']) + 6.25 * float(data['second']) - 5 * float(data['first'])
    await message.answer(f"Ваша норма калорий: {calories}")
    await state.finish()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)