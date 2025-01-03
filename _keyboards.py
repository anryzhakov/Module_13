from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

kb_start = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton('Рассчитать'),
            KeyboardButton('Информация')
        ]
    ], resize_keyboard = True
)

kb_inline = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories'),
            InlineKeyboardButton('Формула расчёта', callback_data='formulas')
        ]
    ], resize_keyboard = True
)