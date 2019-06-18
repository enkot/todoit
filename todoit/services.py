from todoit.models import TodoItem, create_tables


def find_todo(id):
    todo = TodoItem.get_by_id(id)
    return todo


def get_todos():
    todos = TodoItem.select()
    return todos


def add_todo(title):
    todo = TodoItem(title=title)
    todo.save()
    return todo.id


def remove_todo(id):
    query = TodoItem.delete().where(TodoItem.id == id)
    query.execute()


def change_done_status(id, status):
    query = TodoItem.update(done=status).where(
        TodoItem.id == id)
    query.execute()


create_tables()
