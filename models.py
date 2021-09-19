from peewee import SqliteDatabase, Model, IntegerField, DateTimeField
from datetime import datetime

import settings


database = SqliteDatabase(settings.SQLITE_PATH)


class BaseModel(Model):
    class Meta:
        database = database


class Product(BaseModel):
    product_id = IntegerField(unique=True)
    created_at = DateTimeField(default=datetime.now)
