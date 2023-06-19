from flask import Blueprint, request

from ....lib.response import response as format_response

v1 = Blueprint("APIv1", __name__)


@v1.route("/")
async def root():
    return format_response(request, {}, 200, "OK!")


from .events import *
from .notes import *
from .perms import *
from .statuses import *
from .subjects import *
from .users import *
