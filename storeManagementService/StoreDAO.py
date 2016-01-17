from models import *

DATABASE = "StoreManagement"
ADDRESS = "localhost"


def create_store(username, password, store_name, balance):
    connect(DATABASE)
    store = Store()
    store.username = username
    store.password = password
    store.storeName = store_name
    store.balance = 0
    store.items = []
    store.save()


def get_store(u, p):
    connect(DATABASE)
    query_result = Store.objects(username=u, password=p)
    if len(query_result) == 0:
        return None
    elif len(query_result) == 1:
        return query_result[0]
    else:
        raise Exception("Duplicate store accounts, username:'u'.", u)
        return None


def get_store_by_id(store_id):
    connect(DATABASE)
    query_result = Store.objects(id=store_id)
    if len(query_result) == 0:
        return None
    elif len(query_result) == 1:
        return query_result[0]
    else:
        raise Exception("Duplicate store accounts, storeId:'id'.", id)
        return None


def add_item(item, store):
    connect(DATABASE)
    store.items.append(item.to_dbref())
    store.save()


def get_store_by_username(u):
    connect(DATABASE)
    query_result = Store.objects(username=u)
    if len(query_result) == 0:
        return None
    elif len(query_result) == 1:
        return query_result[0]
    else:
        raise Exception("Duplicate store accounts, username:'u'.", u)
        return None


def get_store_by_store_name(store_name):
    connect(DATABASE)
    query_result = Store.objects(storeName=store_name)
    if len(query_result) == 0:
        return None
    elif len(query_result) == 1:
        return query_result[0]
    else:
        raise Exception("Duplicate store accounts, store name:'store_name'.", store_name)
        return None
