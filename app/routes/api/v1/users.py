from . import v1 as api
from ....models import User, Permission
from ....lib.response import response as format_response
from flask import request, session


@api.route("/users/")
async def users_root():
    return format_response(request, {}, 200, "OK!")


@api.route("/users/register/")
async def users_register():
    return format_response(request, {}, 200, "OK!")


@api.route("/users/login/")
async def users_login():
    return format_response(request, {}, 200, "OK!")


@api.route("/users/fetch/")
async def users_fetch():
    # Fetches public data
    return format_response(request, {}, 200, "OK!")


@api.route("/users/update/")
async def users_passwd():
    # Password, Displayname or Email change
    return format_response(request, {}, 200, "OK!")


@api.route("/users/delete/")
async def users_delete():
    return format_response(request, {}, 200, "OK!")
