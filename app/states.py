from aiogram.fsm.state import StatesGroup, State

class CreateTodoState(StatesGroup):
    waiting_for_description = State()
    waiting_for_due_date = State()
    waiting_for_image = State()
    
class UpdateTodoState(StatesGroup):
    waiting_for_description = State()
    waiting_for_due_date = State()
    waiting_for_image = State()
    