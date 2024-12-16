import json

TODO_FILE = 'todos.json'

def load_todo():
    try:
        with open(TODO_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    except:
        return {}
    
def save_todo(data):
    with open(TODO_FILE, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def add_todo(user_id, description, due_date, image=None):
    data = load_todo()
    user_tasks = data.get(str(user_id), [])
    task_id = len(user_tasks) + 1
    task = {'id': task_id, 'description': description, 'due_date': due_date, 'image': image}
    user_tasks.append(task)
    data[str(user_id)] = user_tasks
    save_todo(data)
    
def list_of_todo(user_id):
    data = load_todo()
    user_tasks = data.get(str(user_id), [])
    todos = [(todo['id'], todo['description'][:10]) for todo in user_tasks]
    return todos

def delete_todo_from_db(user_id, task_id):
    data = load_todo()
    user_tasks = data.get(str(user_id), [])
    new_tasks = [task for task in user_tasks if task ['id'] != int(task_id)]
    data[str(user_id)] = new_tasks
    save_todo(data)

def update_todo_from_db(user_id, task_id):
    data = load_todo()
    user_tasks = data.get(str(user_id), [])
    new_tasks = [task for task in user_tasks if task ['id'] != int(task_id)]
    data[str(user_id)] = new_tasks
    save_todo(data)

def get_task_detail(user_id, task_id):
    data = load_todo()
    user_tasks = data.get(str(user_id), [])
    task = [task for task in user_tasks if task.get('id') == int(task_id)][0]
    return task