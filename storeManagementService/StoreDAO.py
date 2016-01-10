from pymongo import MongoClient
from models import *

DATABASE = "StoreManagement"
ADDRESS = "localhost"


def createStore(username, password, balance):
    connect("StoreManagement")
    store = Store()
    store.username = username
    store.password = password
    store.balance = 0
    store.save()


def getStore(u, p):
    connect("StoreManagement")
    query_result = Store.objects(username=u, password=p)
    if len(query_result) == 0:
        return None
    elif len(query_result) == 1:
        return query_result[0]
    else:
        raise Exception('Duplicate store accounts!')
        return

