from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

from storeManagementService.ItemDAO import *
from storeManagementService.StoreDAO import *
from storeManagementService.form_validator import validate_register_form


def login(request):
    if not request.POST:
        return render(request, "login.html")
    ctx = {}
    ctx.update(csrf(request))
    username = request.POST["username"]
    password = request.POST["password"]
    store = get_store(username, password)
    if not store:
        msg = 'Username/password combination is not found!'
        return render(request, "login.html", {"msg": msg})
    request.session["storeName"] = store.storeName
    request.session["username"] = store.username
    request.session["storeId"] = str(store.id)
    return HttpResponseRedirect("/index/")


def index(request):
    if 'username' not in request.session:
        return HttpResponseRedirect("/login/")

    connect('StoreManagement')
    store = get_store_by_id(request.session["storeId"])
    items = store.items
    return render(request, 'index.html', {"items": items, "storeName": request.session["storeName"]}, )


def register(request):
    request.session.clear()
    if not request.POST:
        return render(request, "register.html")
    ctx = {}
    ctx.update(csrf(request))
    msg = None
    if not validate_register_form(request, msg):
        render("register.html", {"msg": msg})
    username = request.POST["username"]
    password = request.POST["password"]
    store_name = request.POST["store_name"]
    create_store(username, password, store_name, 0)
    store = get_store(username, password)
    if not store:
        msg = "Username/password combination is not found!"
        render("login.html", {"msg": msg})
    request.session["storeName"] = store.storeName
    request.session["username"] = store.username
    request.session["storeId"] = str(store.id)
    return HttpResponseRedirect("/")


def logout(request):
    request.session = None
    request = None
    return HttpResponseRedirect("/")


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
    return HttpResponseRedirect("/index/")

