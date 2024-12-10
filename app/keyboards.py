from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Список задач')],
    [KeyboardButton(text='Создать задачу')],
    [KeyboardButton(text='Обновить задачу')],
    [KeyboardButton(text='Удалить задачу')],
    [KeyboardButton(text='Задача по ID')],
])

