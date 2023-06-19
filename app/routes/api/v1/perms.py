from . import v1 as api
from ....models import User, Permission
from ....lib.response import response as format_response
from flask import request, session


@api.route("/perms/")
async def perms_root():
    return format_response(request, {}, 200, "OK!")


@api.route("/perms/create/")
async def perms_create():
    return format_response(request, {}, 200, "OK!")


@api.route("/perms/fetch/")
async def perms_fetch():
    return format_response(request, {}, 200, "OK!")


@api.route("/perms/update/")
async def perms_passwd():
    # Update a perm resource
    return format_response(request, {}, 200, "OK!")


@api.route("/perms/delete/")
async def perms_delete():
    return format_response(request, {}, 200, "OK!")
