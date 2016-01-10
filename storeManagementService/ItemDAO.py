from pymongo import MongoClient
from models import *

DATABASE = "StoreManagement"
ADDRESS = "localhost"


def createItem(name, category, cost, price, store_id):
    connect(DATABASE)
    query_result = Item.objects(name=name, storeId=store_id)
    if len(query_result) > 0:
        return False
    item = Item()
    item.name = name
    item.category = category
    item.cost = cost
    item.price = price
    item.store = store_id
    item.save()
    return True





