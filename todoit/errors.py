from peewee import DoesNotExist
from merry import Merry

merry = Merry()


@merry._except(DoesNotExist)
def does_not_exist():
    print(f'Item does not exist')


@merry._except(Exception)
def catch_all(e):
    print(f'Unexpected error: {e}')
