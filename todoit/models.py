from peewee import SqliteDatabase, Model, CharField, TextField, BooleanField

DATABASE = 'data.db'

database = SqliteDatabase(DATABASE)


class BaseModel(Model):
    class Meta:
        database = database


class TodoItem(BaseModel):
    title = CharField()
    body = TextField(default='')
    done = BooleanField(default=False)


def create_tables():
    with database:
        database.create_tables([TodoItem])
