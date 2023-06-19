from . import v1 as api
from ....models import User, Permission, Feed
from ....lib.response import response as format_response
from flask import request, session


@api.route("/statuses/")
async def statuses_root():
    return format_response(request, {}, 200, "OK!")


@api.route("/statuses/post/")
async def statuses_create():
    return format_response(request, {}, 200, "OK!")


@api.route("/statuses/get/")
async def statuses_get():
    return format_response(request, {}, 200, "OK!")


@api.route("/statuses/fetch/")
async def statuses_fetch():
    return format_response(request, {}, 200, "OK!")


@api.route("/statuses/update/")
async def statuses_update():
    return format_response(request, {}, 200, "OK!")


@api.route("/statuses/delete/")
async def statuses_delete():
    return format_response(request, {}, 200, "OK!")
