__author__ = 'jikel'
from django.http import HttpResponseRedirect
from StoreDAO import *


def validate_register_form(request, msg):
    msg = None
    if not request:
        msg = 'None Request'
        return False
    username = request.POST["username"]
    password = request.POST["password"]
    re_password = request.POST["re_password"]
    store_name = request.POST["store_name"]
    if not username or not password or not re_password or not store_name:
        msg = 'Parameter is missing!'
        return False
    if password != re_password:
        msg = "Two passwords are not the same."
        return False
    if get_store_by_username(username):
        msg = 'Username exists.'
        return False
    if get_store_by_store_name(store_name):
        msg = 'Story name exists.'
        return False
    return True
