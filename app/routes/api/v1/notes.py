from . import v1 as api
from ....models import User, Permission, Note
from ....lib.response import response as format_response
from flask import request, session


@api.route("/notes/")
async def notes_root():
    return format_response(request, {}, 200, "OK!")


@api.route("/notes/create/")
async def notes_create():
    return format_response(request, {}, 200, "OK!")


@api.route("/notes/get/")
async def notes_get():
    return format_response(request, {}, 200, "OK!")


@api.route("/notes/fetch/")
async def notes_fetch():
    return format_response(request, {}, 200, "OK!")


@api.route("/notes/update/")
async def notes_update():
    return format_response(request, {}, 200, "OK!")


@api.route("/notes/delete/")
async def notes_delete():
    return format_response(request, {}, 200, "OK!")
