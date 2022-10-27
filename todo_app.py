def todo_list():
    todo_list_data = []

    def todo_list_instance(fn=None, **kwargs):
        return fn(todo_list_data, **kwargs) if fn is not None else todo_list_data
    return todo_list_instance


def add_todo(todo_list_data, todo):
    todo_list_data.append(todo)
    return todo_list_data


new_todos = todo_list()
new_todos(add_todo, todo={'name': 'Read a book', 'description': 'Just sit down and read', 'duration': 20, 'status': False})
new_todos(add_todo, todo={'name': 'Buy groceries', 'description': 'Go to store and buy stuff', 'duration': 30, 'status': False})
print(new_todos(add_todo, todo={'name': 'Meditate', 'description': '', 'duration': 10, 'status': True}))
