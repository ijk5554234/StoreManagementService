from pymongo import MongoClient
from models import *

DATABASE = "StoreManagement"
ADDRESS = "localhost"


def createStore(username, password, balance):
    connect(DATABASE)
    store = Store()
    store.username = username
    store.password = password
    store.balance = 0
    store.items = []
    store.save()


def getStore(u, p):
    connect(DATABASE)
    query_result = Store.objects(username=u, password=p)
    if len(query_result) == 0:
        return None
    elif len(query_result) == 1:
        return query_result[0]
    else:
        raise Exception('Duplicate store accounts!')
        return None


def get_store_by_id(store_id):
    connect(DATABASE)
    query_result = Store.objects(id=store_id)
    if len(query_result) == 0:
        return None
    elif len(query_result) == 1:
        return query_result[0]
    else:
        raise Exception('Duplicate store accounts!')
        return None


def add_item(item, store):
    connect(DATABASE)
    store.items.append(item.to_dbref())
    store.save()

