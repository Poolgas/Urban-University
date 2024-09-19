from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
import Bot_Token

api = Bot_Token.Token  # Добавьте свой токен
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

kb_reply = ReplyKeyboardMarkup(resize_keyboard=True)
button_calculate_reply = KeyboardButton(text='Рассчитать')
button_info_reply = KeyboardButton(text='Информация')
kb_reply.insert(button_calculate_reply)
kb_reply.insert(button_info_reply)

kb_inline = InlineKeyboardMarkup(resize_keyboar=True)
button_calculate_inline = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_formula_inline = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb_inline.add(button_calculate_inline)
kb_inline.insert(button_formula_inline)

@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer(text='Выберите опцию:', reply_markup=kb_inline)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer(text='10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()
    await call.answer()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=int(message.text))
    await message.answer('Введите свой рост(см):')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=float(message.text))
    await message.answer('Введите свой вес(кг):')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_colories(message, state):
    await state.update_data(weight=float(message.text))
    data = await state.get_data()
    colories = (10 * data['weight'] + 6.25 * data['growth'] - 5 * data['age'] + 5)
    await message.answer(f'Ваша норма колорий: {colories}')
    await state.finish()


@dp.message_handler(commands=['start'])
async def start(message):
    print('Привет! Я бот помогающий твоему здоровью.')
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb_reply)

@dp.message_handler()
async def all_message(message):
    print('Введите команду /start, чтобы начать общение')
    await message.answer('Введите команду /start, чтобы начать общение')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
