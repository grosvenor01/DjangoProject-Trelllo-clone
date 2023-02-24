from django.db import models
from mongoengine import *
from django.utils import timezone
from mongoengine import connect
connect("todo_db")

class user(Document):
    username=StringField(max_length =200)
    email=EmailField(max_length=254)
    password=StringField(max_length =200)

class table_list(Document):
    todo=ListField(StringField(max_length=1000),default=[])
    in_progress=ListField(StringField(max_length=1000),default=[])
    done=ListField(StringField(max_length=1000),default=[])
    table_name=StringField(max_length =200)
    date = DateTimeField(required=False,default=timezone.now)
    user = ReferenceField("user",reverse_delete_rule=CASCADE)

    