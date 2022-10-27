from pprint import pprint as pp


def todo_list():
    todo_list_data = []

    def todo_list_instance(fn=None, **kwargs):
        return fn(todo_list_data, **kwargs) if fn is not None else todo_list_data
    return todo_list_instance


def add_todo(todo_list_data, todo):
    todo_list_data.append(todo)
    return todo_list_data


def get_todo(todo_list_data, todo_title):
    todo = None
    for todo_instance in todo_list_data:
        if todo_instance['title'] == todo_title:
            todo = todo_instance
            break

    return todo


def update_todo(todo_list_data, todo_title, updates):
    todo = get_todo(todo_list_data, todo_title)

    if todo is None:
        raise ValueError(f"A todo with title: {todo_title} doesn't appear to be on your list.")

    todo.update(updates)

    return todo_list_data


def remove_todo(todo_list_data, todo_title):
    todo = get_todo(todo_list_data, todo_title)

    if todo is None:
        raise ValueError(f"A todo with this title: {todo_title} doesn't appear to be on your list.")
    if not todo['status']:
        raise ValueError(f'Task: {todo_title} seems not to be done, change the status to True to remove it.')

    todo_list_data.remove(todo)

    return todo_list_data


def filter_done_todo(todo_list_data):
    done_todo_list = []

    for todo_instance in todo_list_data:
        if todo_instance['status']:
            done_todo_list.append(todo_instance)

    return done_todo_list


new_todos = todo_list()
new_todos(add_todo, todo={'title': 'Read a book', 'description': 'Just sit down and read', 'duration': 20, 'status': False})
new_todos(add_todo, todo={'title': 'Buy groceries', 'description': 'Go to store and buy stuff', 'duration': 30, 'status': False})
new_todos(add_todo, todo={'title': 'Meditate', 'description': 'Just sit down and relax. You deserve it', 'duration': 10, 'status': True})
new_todos(add_todo, todo={'title': 'Learn new stuff', 'description': 'Have to learn new stuff in order to be the greatest', 'duration': 40, 'status': True})
# print(new_todos(update_todo, todo_title='Meditate', updates={'status': False}))

pp(new_todos)
