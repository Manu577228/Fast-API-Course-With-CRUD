from fastapi import FastAPI

api = FastAPI()

all_todos = [
    {'todo_id' : 1, 'todo_name': 'Sports', 'todo_description': 'Excercise'},
    {'todo_id' : 2, 'todo_name': 'Read', 'todo_description': 'Read 8 Pages'},
    {'todo_id' : 3, 'todo_name': 'Shop', 'todo_description': 'Shopping'},
    {'todo_id' : 4, 'todo_name': 'Study', 'todo_description': 'Study'},
    {'todo_id' : 5, 'todo_name': 'Meditate', 'todo_description': 'Meditate'},
]


# Sample Example
@api.get('/')
def index():
    return {"Hello World"}

# GET, POST, PUT, DELETE

# http://127.0.0.1:8000/todos?first_n=3
@api.get('/todos/{todo_id}')
def get_todo(todo_id: int):
    for todo in all_todos:
        if todo['todo_id'] == todo_id:
            return {'result': todo}
        
@api.get('/todos')
def get_todos(first_n: int = None):
    if first_n:
        return all_todos[:first_n]
    else:
        return all_todos

@api.post('/todos')
def create_todo(todo: dict):
    new_todo_id = max(todo['todo_id'] for todo in all_todos) + 1

    new_todo = {
        'todo_id': new_todo_id,
        'todo_name': todo['todo_name'],
        'todo_description': todo['todo_description']
    }

    all_todos.append(new_todo)

    return new_todo

@api.put('/todos/{todo_id}')
def update_todo(todo_id: int, updated_todo: dict):
    for todo in all_todos:
        if todo['todo_id'] == todo_id:
            todo['todo_name'] = update_todo['todo_name']
            todo['todo_description'] = update_todo['todo_description']
            return todo
    return "Error, not found"

@api.delete('todos/{todo_id}')
def delete_todo(todo_id: int):
    for index, todo in enumerate(all_todos):
        if todo['todo_id'] == todo_id:
            deleted_todo = all_todos.pop(index)
            return deleted_todo
        return "Error not found"