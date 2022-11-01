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


def mark_todo_as_done(todo_list_data, todo_title):
    update_todo(todo_list_data, todo_title, updates={'status': True})
    return f"Todo: {todo_title} is done!"


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
