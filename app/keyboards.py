from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
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
    for task_id, task_desk in tasks:
        keyboard.add(InlineKeyboardButton(text=str(task_desk), callback_data=f'task_{task_id}'))
    return keyboard.adjust(2).as_markup()

def get_task_kb(task_id):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Обновить задачу', callback_data=f'update_{task_id}')],
            [InlineKeyboardButton(text='Удалить задачу', callback_data=f'rm_{task_id}')]
        ]
    )
