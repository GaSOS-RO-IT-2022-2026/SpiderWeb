from . import v1 as api
from ....models import User, Permission, Event
from ....lib.response import response as format_response
from flask import request, session


@api.route("/events/")
async def events_root():
    return format_response(request, {}, 200, "OK!")


@api.route("/events/create/")
async def events_create():
    return format_response(request, {}, 200, "OK!")


@api.route("/events/get/")
async def events_get():
    return format_response(request, {}, 200, "OK!")


@api.route("/events/fetch/")
async def events_fetch():
    return format_response(request, {}, 200, "OK!")


@api.route("/events/update/")
async def events_update():
    return format_response(request, {}, 200, "OK!")


@api.route("/events/delete/")
async def events_delete():
    return format_response(request, {}, 200, "OK!")
