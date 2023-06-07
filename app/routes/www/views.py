from . import www

@www.route("/")
async def root():
    return "Hello World!"
