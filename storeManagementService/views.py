from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

from storeManagementService.ItemDAO import *
from storeManagementService.StoreDAO import *


def login(request):
    if not request.POST:
        return render(request, "login.html")
    ctx = {}
    ctx.update(csrf(request))
    username = request.POST["username"]
    password = request.POST["password"]
    store = get_store(username, password)
    if not store:
        msg = "Username/password combination is not found!"
        render(request, "login.html", msg)
    request.session["storeName"] = store.storeName
    request.session["username"] = store.username
    request.session["storeId"] = str(store.id)
    return HttpResponseRedirect("/")


def index(request):
    request.session
    if 'username' not in request.session:
        return HttpResponseRedirect("/login/")

    connect('StoreManagement')
    store = get_store_by_id(request.session["storeId"])
    items = store.items
    # for item in Item.objects:
    #     items.append(item)
    return render(request, 'index.html', {"items": items, "storeName": request.session["storeName"]}, )


def create_new_item(request):
    if not request.POST:
        return render(request, "index.html")
    ctx = {}
    ctx.update(csrf(request))
    name = request.POST["name"]
    category = request.POST["category"]
    cost = request.POST["cost"]
    price = request.POST["price"]
    desc = request.POST["description"]
    item = create_item(name, category, cost, price, desc)
    store = get_store_by_id(request.session["storeId"])
    add_item(item, store)
    return HttpResponseRedirect("/")

