import time
from json import dumps

from flask import Request, Response, make_response, redirect


def response(
    request: Request,
    data: dict,
    status: int,
    msg: str | None = None,
    redirect_path: str | None = None,
    cookies: list[tuple[str, any, int]] = [],
    api_version: float = 1.0,
):
    header = {
        "version": api_version,
        "ip": request.remote_addr,
        "host": request.host,
        "secure": request.is_secure,
        "status": status,
        "message": msg if not isinstance(msg, type(None)) else str(status),
        "redirect": redirect_path
        if not isinstance(redirect_path, type(None))
        else False,
        "route": request.path,
    }
    rsp = Response(
        dumps({**header, **data}), mimetype="application/json", status=status
    )
    if header["redirect"]:
        rsp = make_response(redirect(header["redirect"], code=302, Response=rsp))
    # Set cookies
    for c_name, c_value, c_lifetime in cookies:
        rsp.set_cookie(c_name, c_value, expires=time.time() + c_lifetime)
    return rsp
