import textwrap
import click

from todoit.errors import merry
from todoit.services import find_todo, get_todos, add_todo, change_done_status, remove_todo


@click.group()
def cli():
    pass


@cli.command()
def list():
    """Shows todo list."""
    todos = get_todos()

    if not todos:
        return click.secho(f'Todo list is empty.', fg='yellow')

    for todo in todos:
        checked = ' '
        color = None

        if todo.done:
            checked = '✘'
            color = 'green'

        title = textwrap.shorten(todo.title, width=40,
                                 placeholder="...").ljust(40)
        status_text = click.style(f'{checked}  {title}', fg=color)
        click.echo(f'{todo.id}  {status_text}')


@cli.command()
@click.argument('title')
@merry._try
def add(title):
    """Add new item to list."""
    if not title:
        return click.secho(f'Todo title can\'t be empty.', fg='red')
    id = add_todo(title)
    click.echo(f'Todo created with ID:{id}.')


@cli.command()
@click.argument('id')
@merry._try
def done(id):
    """Change item status to Done."""
    find_todo(id)
    change_done_status(id, True)
    click.echo(f'Todo:{id} changed status to Done.')


@cli.command()
@click.argument('id')
@merry._try
def undone(id):
    """Change item status to Undone."""
    find_todo(id)
    change_done_status(id, False)
    click.echo(f'Todo:{id} changed status to Undone.')


@cli.command()
@click.argument('id')
@merry._try
def remove(id):
    """Remove item from list."""
    find_todo(id)
    remove_todo(id)
    click.echo(f'Todo:{id} removed.')
