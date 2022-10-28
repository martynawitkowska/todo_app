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


def filter_todos(todo_list_data, status=True):
    filtered_todo_list = []

    for todo_instance in todo_list_data:
        if todo_instance['status'] and status:
            filtered_todo_list.append(todo_instance)
        elif not todo_instance['status'] and not status:
            filtered_todo_list.append(todo_instance)

    return filtered_todo_list


def remove_all_done_todos(todo_list_data):

    for todo_instance in todo_list_data.copy():
        if todo_instance['status']:
            todo_list_data.remove(todo_instance)

    return todo_list_data


new_todos = todo_list()
new_todos(add_todo, todo={'title': 'Read a book', 'description': 'Just sit down and read', 'duration': 20, 'status': False})
new_todos(add_todo, todo={'title': 'Buy groceries', 'description': 'Go to store and buy stuff', 'duration': 30, 'status': False})
new_todos(add_todo, todo={'title': 'Exercise', 'description': 'Just move bitch', 'duration': 30, 'status': True})
new_todos(add_todo, todo={'title': 'Meditate', 'description': 'Just sit down and relax. You deserve it', 'duration': 10, 'status': True})
new_todos(add_todo, todo={'title': 'Start using brain', 'description': 'Just use it', 'duration': 30, 'status': True})
new_todos(add_todo, todo={'title': 'Some task to do', 'description': 'Some description', 'duration': 30, 'status': False})
new_todos(add_todo, todo={'title': 'Some other task to do', 'description': 'Some other description', 'duration': 30, 'status': True})
# new_todos(update_todo, todo_title='Read a book', updates={'status': True})
pp(new_todos(remove_all_done_todos))




