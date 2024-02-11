from quart import current_app as app
from quart import render_template


@app.errorhandler(400)
async def error_400(error):
    return await render_template(
        "errors/400.html",
    ), 400


@app.errorhandler(401)
async def error_401(error):
    return await render_template(
        "errors/401.html",
    ), 401


@app.errorhandler(403)
async def error_403(error):
    return await render_template(
        "errors/403.html",
    ), 403


@app.errorhandler(404)
async def error_404(error):
    return await render_template(
        "errors/404.html",
    ), 404


@app.errorhandler(405)
async def error_405(error):
    return await render_template(
        "errors/405.html",
    ), 405


@app.errorhandler(500)
async def error_500(error):
    return await render_template(
        "errors/500.html",
    ), 500
