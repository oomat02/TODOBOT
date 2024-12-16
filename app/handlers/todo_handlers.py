from aiogram import F, Router, types 
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile

from app.states import CreateTodoState
from app.keyboards import main_kb, tasks_kb, get_task_kb
from app.users import add_todo, delete_todo_from_db, get_task_detail, update_todo_from_db

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
    await state.update_data(due_date=due_date)
    await message.answer('Теперь отправьте изображение')
    await state.set_state(CreateTodoState.waiting_for_image)

@router.message(CreateTodoState.waiting_for_image)
async def set_todo_image(message: types.Message, state: FSMContext):
    image_path = None  
    if message.photo:
        file_id = message.photo[-1].file_id
        file = await message.bot.get_file(file_id)
        image_path = f'media/{file.file_id}.jpg'
        await message.bot.download_file(file.file_path, image_path)

    user_data = await state.get_data()
    add_todo(message.from_user.id, user_data['description'], image_path)
    await message.answer('Задача успешно добавлена!', reply_markup=main_kb)
    await state.clear()

@router.message(F.text == 'Список задач')
async def list_todo(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    await message.answer('Вот ваши Todo!',reply_markup=tasks_kb(user_id))

@router.callback_query(F.data.startswith('task_'))
async def show_task_details(callback: types.CallbackQuery, state: FSMContext):
    task_id = callback.data[5:]
    task = get_task_detail(callback.from_user.id, task_id)
    text = f"Ваша задача: \n" \
           f"ID: {task['id']}\n" \
           f"Описание: {task['description']}\n" \
           f"Дедлайн: {task['due_date']}"
    await callback.message.answer_photo(photo=FSInputFile(task['image'])if task ['image'] else None, caption=text, reply_markup=get_task_kb(task_id))

@router.callback_query(F.data.startswith('ud_'))
async def update_todo(callback: types.CallbackQuery, state: FSMContext):
    task_id = callback.data[3:]
    task = get_task_detail(callback.from_user.id, task_id)
    text = f"Ваша задача: \n" \
           f"ID: {task['id']}\n" \
           f"Описание: {task['description']}\n" \
           f"Дедлайн: {task['due_date']}"
    await callback.message.answer(text=text, reply_markup=get_task_kb(callback.message.from_user.id, task_id))

@router.callback_query(F.data.startswith('rm_'))
async def delete_todo(callback: types.CallbackQuery, state: FSMContext):
    task_id = callback.data[5:]
    delete_todo_from_db(callback.from_user.id, task_id)
    await callback.message.answer('Ваша тудушка успешно удалена!')


@router.callback_query(F.data.startswith('up_'))
async def update_todo_from_db(callback: types.CallbackQuery, state: FSMContext):
    task_id = callback.data[3:]
    update_todo_from_db(callback.from_user.id, task_id)
    await callback.message.answer('Ваша тудушка успешно обновлена!')

