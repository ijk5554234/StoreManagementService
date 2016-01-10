from __future__ import unicode_literals

from mongoengine import *


class Store(Document):
    username = StringField()
    password = StringField()
    storeName = StringField()
    balance = DecimalField()
    items = ListField(ReferenceField("Item"))

    def __unicode__(self):
        return self.username

    def __str__(self):
        return self.username


class Item(Document):
    category = StringField(max_length=50)
    name = StringField(max_length=50)
    cost = DecimalField()
    price = DecimalField()
    description = StringField()

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


