from aiogram import F, Router, types 
from aiogram.fsm.context import FSMContext

from app.states import CreateTodoState
from app.keyboards import main_kb
from app.users import add_todo

router = Router()

@router.message(F.text == 'Создать задачу')
async def create_todo(message: types.Message, state: FSMContext):
    await message.answer('Введите описание задачи')
    await state.set_state(CreateTodoState.waiting_for_description)

@router.message(CreateTodoState.waiting_for_description)
async def set_todo_description(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer('Теперь введите дату выполнения задачи(в формате YYYY-MM-DD)')
    await state.set_state(CreateTodoState.waiting_for_due_date)

@router.message(CreateTodoState.waiting_for_due_date)
async def set_todo_due_date(message: types.Message, state: FSMContext):
    due_date = message.text
    user_data = await state.get_data()
    add_todo(message.from_user.id, user_data['description'], due_date)
    await message.answer('Задача успешно добавлена!',
    reply_markup=main_kb)
    await state.clear()

#TODO: написать функцию для чтения списка задач юзера - Список задач - Список из Inline Кнопок где будут айди задачи
