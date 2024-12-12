from aiogram import F, Router, types 
from aiogram.fsm.context import FSMContext

from app.states import CreateTodoState
from app.keyboards import main_kb, tasks_kb, get_delete_kb
from app.users import add_todo, delete_todo_from_db, get_task_detail

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



@router.message(F.text == 'Список задач')
async def list_todo(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    await message.answer('Вот ваши Todo!',reply_markup=tasks_kb(user_id))

@router.callback_query(F.data.startswith('task_'))
async def delete_todo(callback: types.CallbackQuery, state: FSMContext):
    task_id = callback.data[5:]
    task = get_task_detail(callback.from_user.id, task_id)
    text = f'Ваша задача: \n' \
            f'ID: {task['id']}' \
            f'Описание: {task['description']}' \
            f'Дедлайн: {task['due_date']}'
    await callback.message.answer(text=text, reply_markup=get_delete_kb(callback.message.from_user.id, task_id))

@router.callback_query(F.data.startswith('rm_'))
async def delete_todo(callback: types.CallbackQuery, state: FSMContext):
    task_id = callback.data[5:]
    delete_todo_from_db(callback.from_user.id, task_id)
    await callback.message.answer('Ваша тудушка успешно удалена!')