from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


kb_reply = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Регистрация'),
            KeyboardButton(text='Информация'),
            KeyboardButton(text='Рассчитать')
        ],
        [KeyboardButton(text='Купить')]
    ], resize_keyboard=True
)

kb_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories'),
            InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
        ]
    ], resize_keyboard=True
)

kb_inline_buy = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='БАД 1', callback_data='product_buying'),
            InlineKeyboardButton(text='БАД 2', callback_data='product_buying'),
            InlineKeyboardButton(text='БАД 3', callback_data='product_buying'),
            InlineKeyboardButton(text='БАД 4', callback_data='product_buying'),
        ]
    ]
)