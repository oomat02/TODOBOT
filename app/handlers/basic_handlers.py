from aiogram import types, Router, F
from aiogram.filters import Command

from app.keyboards import main_kb

router = Router()

@router.message(Command('start'))
async def start(message: types.Message):
    await message.answer('Добро пожаловать TODO BOT!',
    reply_markup=main_kb)

 
@router.message(Command('help')) 
async def help_command(message: types.Message): 
    first_message = () 
    await message.answer('Инструкция по использованию бота') 
 
    second_message = () 
    await message.answer('\n Бот позволяет управлять задачами с помощью кнопок. Вот доступные функции:1. Список задач Показывает список всех ваших задач с их ID. Используйте ID для работы с конкретной задачей. 2. Конкретная задача Выберите задачу по ID, чтобы увидеть ее описание и дату выполнения. 3. Создание задачи Позволяет добавить новую задачу. Бот запросит описание и дату выполнения. 4. Удаление задачи Удаляет задачу по ID. Просто выберите задачу из списка для удаления 5. Обновление задачи Позволяет изменить описание или дату выполнения выбранной задачи.Используйте кнопки ниже для управления задачами!')



















