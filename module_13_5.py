from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio


api = "Здесь токен от бота"
bot = Bot(token = api)
dp = Dispatcher(bot, storage= MemoryStorage())

keyB = ReplyKeyboardMarkup(resize_keyboard=True) # автоматически подстраиваем размер кнопок на экране
button_1 = KeyboardButton(text = 'Расчитать') # создаем кнопки на экране
button_2 = KeyboardButton(text = 'Информация')
keyB.add(button_1)
keyB.add(button_2)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup = keyB)

@dp.message_handler(text = 'Расчитать')
async def set_age(message):
    await message.answer('Введите свой возраст.')
    await UserState.age.set()

@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(age = message.text)
    await message.answer('Введите свой рост.')
    await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth = message.text)
    await message.answer('Введите свой вес.')
    await UserState.weight.set()

@dp.message_handler(state = UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight = message.text)
    data = await state.get_data()
    await message.answer(f'Если Вы являетесь мужчиной, для Вас норма калорий: {int(data["weight"])*10+float(data["growth"])*6.25+int(data["age"])*5}')
    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)