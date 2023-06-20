from flask import render_template, request

from . import www


@www.route("/")
async def root():
    return "Hello World!"


@www.route("/debug/<template>")
async def root_debug(template: str):
    try:
        return render_template(template + ".html", **request.args)
    except Exception as e:
        return f"Exception raised: {e}"
