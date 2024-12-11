from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.users import list_of_todo


main_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Список задач')],
    [KeyboardButton(text='Создать задачу')],
    [KeyboardButton(text='Обновить задачу')],
    [KeyboardButton(text='Удалить задачу')],
    [KeyboardButton(text='Задача по ID')],
])

def tasks_kb(user_id):
    tasks = list_of_todo(user_id)
    keyboard = InlineKeyboardBuilder()
    for task in tasks:
        keyboard.add(InlineKeyboardButton(text=str(task), callback_data=f'task_{task}'))
    return keyboard.adjust(2).as_markup()