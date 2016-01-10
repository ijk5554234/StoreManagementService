from pymongo import MongoClient
from models import *

DATABASE = "StoreManagement"
ADDRESS = "localhost"


def create_item(name, category, cost, price, desc):
    connect(DATABASE)
    query_result = Item.objects(name=name)
    if len(query_result) > 0:
        return False
    item = Item()
    item.name = name
    item.category = category
    item.cost = cost
    item.price = price
    item.description = desc
    item.save()
    return item



