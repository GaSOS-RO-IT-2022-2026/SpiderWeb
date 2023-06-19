from . import v1 as api
from ....models import User, Permission, Subject
from ....lib.response import response as format_response
from flask import request, session


@api.route("/subjects/")
async def subjects_root():
    return format_response(request, {}, 200, "OK!")


@api.route("/subjects/create/")
async def subjects_create():
    return format_response(request, {}, 200, "OK!")


@api.route("/subjects/get/")
async def subjects_get():
    return format_response(request, {}, 200, "OK!")


@api.route("/subjects/fetch/")
async def subjects_fetch():
    return format_response(request, {}, 200, "OK!")


@api.route("/subjects/update/")
async def subjects_update():
    return format_response(request, {}, 200, "OK!")


@api.route("/subjects/delete/")
async def subjects_delete():
    return format_response(request, {}, 200, "OK!")
